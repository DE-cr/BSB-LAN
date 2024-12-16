#!/usr/bin/env python

# ----------------------------------------------------------------------------
# sample code to show how BSB-LAN's /D datalogs could be processed using
# pandas/python, including conversion to pivoted *.csv and some plot ideas
# ----------------------------------------------------------------------------

from sys import argv
import pandas as pd

# -- read BSB-LAN /D logs into pandas dataframe:

if len(argv) > 1:
    # compile data from file names given on command line:
    df = pd.DataFrame()
    for fn in argv[1:]:
        print("Reading", fn, "...")
        df = pd.concat([df, pd.read_csv(fn, sep=";")])
else:
    print("Reading data from BSB-LAN ...")
    df = pd.read_csv("http://bsb-lan/D", sep=";")

print("Fitting data ...")

# make missing values digestible for pandas:
df.Value = pd.to_numeric(df.Value.replace("---", None))

# we want parameters without a trailing ".0":
df.Parameter = df.Parameter.astype("str").str.replace(".0", "", regex=False)

# convert Date values from string to datetime type:
df.Date = pd.to_datetime(df.Date, format="%d.%m.%Y %H:%M:%S", errors="coerce")

# drop duplicates, if any:
df = df.groupby(["Milliseconds", "Date"]).first().reset_index()

# pivot data for (much) easier access (this also drops the Milliseconds values):
df = df.pivot(
    index=["Date"], columns=["Parameter", "Description", "Unit"], values="Value"
).reset_index()

# flatten multi-index:
df.columns = [
    f"{c[0]}"
    + f'{f" - {c[1]}" if c[1] else ""}'
    + f'{f" [{c[2]}]" if c[2]==c[2] and c[2] else ""}'
    for c in df.columns.values
]

# you may want to save the processed data for faster re-loading later on:
# df.to_csv("BSB-LAN.csv", index=False)  # for compatibility with other programs
# df.to_pickle("BSB-LAN.pickle")  # to keep the Date column as datetime type

# show what data we have found:
print(df.info())
print(f"Found data from {df.Date.min()} to {df.Date.max()}")


# -----------------------------------------------------------------------------
# Usage examples (!) for data in pandas, for you to select, adapt, expand, ...
# Note: Most likely you'll need to adjust the parameter numbers used here to
#       those in your logged data! (Look for 'find_parameter_columns' below!)

import matplotlib.pyplot as plt


def find_parameter_columns(df, parameter_name_contains):
    return [c for c in df.columns if str(parameter_name_contains) in c]


# locate some parameter columns we're using:
outside_temperature_column = find_parameter_columns(df, 8700)[0]
# note: we're using heating circuit 2 (parameter 8774) here!:
flow_temperature_set_point_column = find_parameter_columns(df, 8774)[0]

# graphically show statistics for numeric data fields found:
df.boxplot(showmeans=True, rot=90)
plt.tight_layout()
plt.show()

# plot of temperature parameters, similar to BSB-LAN's /DG:
# Date values can differ within each BSB-LAN sample set, # as BSB-LAN often
# cannot query multiple parameters within the same second. Therefore we fill
# the resulting "gaps" in our data, for uninterrupted plot lines:
df.fillna(method="ffill").plot(
    x="Date", y=find_parameter_columns(df, "°"), grid=True, figsize=(19.2, 10.8)
)
plt.tight_layout()
plt.show()

# plotting rolling averages of outside temperatures:
dfx = df.set_index("Date")  # for proper handling as x axis in plots
dfx["daily"] = dfx[outside_temperature_column].rolling("D").mean()
dfx["weekly"] = dfx[outside_temperature_column].rolling("7D").mean()
dfx["monthly"] = dfx[outside_temperature_column].rolling("30D").mean()
dfx.plot(
    y=["daily", "weekly", "monthly"],
    title="Rolling averages of " + outside_temperature_column,
)
plt.tight_layout()
plt.show()


# - the following make sense mostly with data spanning multiple years:

import calendar

# infer detail columns from Date:
df["date"] = df.Date.dt.data  # just the date, without time
df["year"] = df.Date.dt.year
df["month"] = df.Date.dt.month
df["day"] = df.Date.dt.day
df["time"] = df.Date.dt.hour + (df.Date.dt.minute + df.Date.dt.second / 60) / 60

# plot temperature boxplot per year/month:
df.boxplot(outside_temperature_column, ["year", "month"], showmeans=True, rot=90)
plt.tight_layout()
plt.show()

# plot flow temperature set point over outside temperature, by year:
for year in df.year.unique():
    dfx = df.query(f"year=={year}")
    plt.scatter(
        dfx[outside_temperature_column],
        dfx[flow_temperature_set_point_column],
        0.1,
        label=year,
    )
plt.xlabel(outside_temperature_column)
plt.ylabel(flow_temperature_set_point_column)
plt.legend(markerscale=9)
plt.grid()
plt.show()


# plot y over x, in a calendar format:
def calendar_plot(df, x, y):
    fig, ax = plt.subplots(
        4, 3, sharex=True, sharey=True, layout="constrained", figsize=(10, 10)
    )
    for month in range(1, 13):
        dfm = df.query(f"month=={month}")
        a = ax.flat[month - 1]
        for year in sorted(dfm.year.unique()):
            dfmy = dfm.query(f"year=={year}")
            a.scatter(dfmy[x], dfmy[y], 0.1, alpha=0.5, label=int(year))
        if len(dfm):
            a.set_title(calendar.month_name[month])
            a.grid()
            leg = a.legend(markerscale=9)
            for lh in leg.legendHandles:
                lh.set_alpha(1)
        else:
            a.set_frame_on(False)
            a.tick_params(bottom=False, left=False)
    plt.suptitle(f"{y} over {x}", fontweight="bold")
    plt.show()


calendar_plot(df, "time", outside_temperature_column)
calendar_plot(df, "day", outside_temperature_column)
calendar_plot(df, "time", flow_temperature_set_point_column)


# bar plot of burner activity hours by year/month:
burner_status_column = find_parameter_columns(df, 8005)[0]
samples_per_hour = 60  # recommend (adjust, if necessary)

ax = (  # burner status < 17 == active:
    df[df[burner_status_column] < 17].groupby(["year", "month"]).year.count()
    / samples_per_hour
).plot(kind="bar", title="Burner Activity [h]", figsize=(10, 4))
# hide frame:
ax.set_frame_on(False)
ax.set_yticks([])
# show values with bars:
for container in ax.containers:
    ax.bar_label(container, fmt="%.0f")
plt.tight_layout()
plt.show()


# plot of daily burner activity hours and outside temperatures over time,
# with rolling average and overall means:
import re

window_d = 90  # looong rolling average window, to really smooth out kinks
df2 = pd.DataFrame()
df2["h"] = (  # burner status < 17 == active:
    df[df[burner_status_column] < 17].groupby("date").date.count() / samples_per_hour
)
df2["t"] = df.groupby("date")[outside_temperature_column].mean()
df2["h rolling"] = df2.h.rolling(window_d, center=True).mean()
df2["t rolling"] = df2.t.rolling(window_d, center=True).mean()
df2["h mean"] = df2.h.mean()
df2["t mean"] = df2.t.mean()
h_color, t_color = "red", "green"
ax = df2.plot(
    secondary_y=["t", "t rolling", "t mean"],
    style=[h_color, t_color, h_color, t_color, h_color[0] + ":", t_color[0] + ":"],
    legend=False,
    rot=90,
)
# make day curves thin, rolling averages and means wide:
for line in ax.get_lines() + ax.right_ax.get_lines():
    line.set_linewidth(2 if re.search("rolling|mean", line.get_label()) else 0.2)
ax.set_title(
    f"Daily burner activity [h] ({h_color}) and\n"
    + f"{outside_temperature_column} ({t_color}),\n"
    + f"with {window_d} days rolling average and overall means"
)
# color axis ticks to match curves:
ax.tick_params(axis="y", colors=h_color)
ax.right_ax.tick_params(axis="y", colors=t_color)
plt.tight_layout()
plt.show()


## plot of daily fuel consumption since last delivery, with total:
# only consider data since last delivery:
most_recent_delivery = "2024-03-05"  # adjust!
dfx = df.query(f'Date >= "{most_recent_delivery}"')
# calculate fuel consumption
fuel_units_per_hour = 3  # adjust, if necessary!
fuel_units = (
    dfx[dfx[burner_status_column] < 17].groupby("date").date.count()
    / samples_per_hour
    * kg_per_hour
)
# fill in gaps (days w/o (reported) burner activity):
fuel_units = fuel_units.reindex(
    pd.date_range(start=most_recent_delivery, end=pd.Timestamp.today(), freq="D")
).fillna(0)
# plot:
fuel_units.plot(
    title=f"Fuel units per day, since {most_recent_delivery}"
    + f" (overall={round(fuel_units.sum())})",
    grid=True,
    rot=90,
)
plt.tight_layout()
plt.show()
