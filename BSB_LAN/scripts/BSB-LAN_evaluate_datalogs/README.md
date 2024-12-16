# BSB-LAN_evaluate_datalogs.py

*Example code to show how BSB-LAN's /D datalogs could be processed using
Python, including conversion to pivoted \*.csv and some plot ideas*

## Data transformation

BSB-LAN's /D datalogs come in a format with each parameter reading in
a separate line, and the parameter's name in a column of the lines.
For most (?) purposes, a pivoted format is more useful. The example
code provided here does this transformation, e.g. from this:

```
Milliseconds;Date;Parameter;Description;Value;Unit
1235285616;16.11.2024 15:32:22;8700;Aussentemperatur;8.0;°C
1235285807;16.11.2024 15:32:22;8770;Raumtemperatur-Istwert 2;20.3;°C
1235285996;16.11.2024 15:32:22;8773;Vorlauftemperatur Istwert Heizkreis 2;29.5;°C
1235286180;16.11.2024 15:32:22;8774;Vorlauftemperatur-Sollwert resultierend HK2;29.6;°C
1235286363;16.11.2024 15:32:22;1020;Heizkennlinien-Steilheit;1.36;
1235886587;16.11.2024 15:42:23;8700;Aussentemperatur;8.0;°C
1235886775;16.11.2024 15:42:23;8770;Raumtemperatur-Istwert 2;20.3;°C
1235886959;16.11.2024 15:42:23;8773;Vorlauftemperatur Istwert Heizkreis 2;29.5;°C
1235887155;16.11.2024 15:42:23;8774;Vorlauftemperatur-Sollwert resultierend HK2;29.6;°C
```

... to this (CSV format example; uncomment `df.to_csv([...]` line to save the
pivoted data in this format for processing with another program, or use
`df.to_pickle` if you want to load the transformed data again with Python
later on):

```
Date,8700 - Aussentemperatur [°C],8770 - Raumtemperatur-Istwert 2 [°C],8773 - Vorlauftemperatur Istwert Heizkreis 2 [°C],8774 - Vorlauftemperatur-Sollwert resultierend HK2 [°C],1020 - Heizkennlinien-Steilheit
2024-11-16 15:32:22,8.0,20.3,29.5,29.6,1.36
2024-11-16 15:42:23,8.0,20.3,29.5,29.6,
```

## Example applications

The provided Python script also includes some examples on how the data could be
processed/analyzed. To see if they can be applied to your data, just execute the script!
For that, you can either provide the names of files containing BSB-LAN /D
datalogs or the script will try to load the current data directly from
`http://bsb-lan/D`.

Please note that you will probably have to *adjust* the burner parameters
used in my examples to the ones you've been logging! This should be easy
enough, though: Just replace the parameter numbers in the script - or simply
remove the code sections you don't want or for which you don't have the
logged data.

### Statistical overview

(Use `print(df.describe())` for a textual representation. Due to the long parameter
names, the boxplots become a bit squashed here.)

![BoxPlot](examples/BSB-LAN_evaluate_datalogs.py_boxplot.png)

### Similar to BSB-LAN's /DG display

...but with the option to filter to your liking, e.g. via `.query()`.
(Look into the code for examples on how to use `.query()`.)

![DG](examples/BSB-LAN_evaluate_datalogs.py_DG.png)

... or maybe like this?:

![RollingAverages](examples/BSB-LAN_evaluate_datalogs.py_outside_temp_rolling_averages.png)

### If you have data spanning multiple years (or at least months)


![BoxPlotYearMont](examples/BSB-LAN_evaluate_datalogs.py_boxplot_year_month.png)

---

![FlowOverTemp](examples/BSB-LAN_evaluate_datalogs.py_flow_over_outside.png)

---

![TempOverTime](examples/BSB-LAN_evaluate_datalogs.py_cal_8700_-_Aussentemperatur_[°C]_over_time.png)

---

![TempOverDay](examples/BSB-LAN_evaluate_datalogs.py_cal_8700_-_Aussentemperatur_[°C]_over_day.png)

---

Why a night time room temperature reduction, combined with rapid warm-up and
start forward shift, may not be the best choice when using a heat pump:

![FlowOverTime](examples/BSB-LAN_evaluate_datalogs.py_cal_8774_-_Vorlauftemperatur-Sollwert_resultierend_[°C]_over_time.png)

---

Should you have logged the burner status (parameter 8005) every minute for an
extended period of time, you can also create something like this:

![BurnerActivity](examples/BSB-LAN_evaluate_datalogs.py_burner_activity_bars.png)

... or find out how much fuel has already been used since the last delivery:

![FuelUsed](examples/BSB-LAN_evaluate_datalogs.py_fuel_used.png)

... and if you have also logged the outside temperatures with it, you can plot
something like this:

![BurnerActivityAndTemp](examples/BSB-LAN_evaluate_datalogs.py_burner_activity_plots.png)