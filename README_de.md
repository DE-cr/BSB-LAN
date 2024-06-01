# BSB-LPB-PPS-LAN

English version can be found <A HREF="https://github.com/fredlcore/bsb_lan/blob/master/README.md">here</A>. 

BSB-LAN ist ein Adapter für den ["Boiler-System-Bus" (BSB)](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#1011-bsb), den ["Local-Process-Bus (LPB)](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#1012-lpb) und die ["Punkt-zu-Punkt-Schnittstelle" (PPS)](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#1013-pps-schnittstelle). Es gibt den Adapter für verschiedene *ESP32*-basierte Microcontroller (ESP32 NodeMCU, Olimex EVB, Olimex POE) bzw. für einen *Arduino Due* mit Ethernet-Shield zur web-basierten Kontrolle über LAN/WLAN von Heizungssystemen von Elco, Brötje und anderen Herstellern, die Siemens-Regler verwenden. Darüber hinaus ist das Logging von Werten auf Micro-SD-Karte möglich. Dieses Projekt unterstützt fast alle an den Heizungen verfügbaren Parameter und kann in vielfältiger Hinsicht eine umfangreichere und kostengünstige Alternative zum OZW 672, OCI 700 oder Remocon Net B sein.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Dieses Werk ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz</a>.

---

***Platinen erhältlich!***  
**Es sind Platinen für den ESP32 erhältlich, die einfach nur auf den jeweiligen Microcontroller aufgesteckt werden müssen. Mit dem Kauf eines Boards unterstützt Ihr darüber hinaus die Weiterentwicklung dieses Projekts. Bei Interesse bitte Frederik eine e-Mail an bsb (ät) code-it.de schicken (Deutsch/Englisch).**  

---

@1coderookie hat eine umfangreiche Sammlung an Informationen in seinem [BSB-LPB-LAN-Handbuch](https://1coderookie.github.io/BSB-LPB-LAN/) zusammengestellt - sagt ihm gerne, wenn Euch sein Projekt geholfen hat, BSB-LAN zum Fliegen zu kriegen oder unterstützt ihn über die Links auf seiner Seite.
   
***Schnellstartanleitungen für die Installation und Inbetriebnahme des BSB-LAN-Setups sind hier verfügbar:***  
***[Schnellstartanleitung für ESP32-Boards](https://1coderookie.github.io/BSB-LPB-LAN/SSA_ESP32.html)***  
***[Schnellstartanleitung für den Arduino Due](https://1coderookie.github.io/BSB-LPB-LAN/SSA_DUE.html)***  
     
---     
   
Mit Hilfe des Adapters und der BSB-LAN-Software können nun unkompliziert verschiedene Funktionen, Werte und Parameter beobachtet, geloggt und bei Bedarf web-basiert gesteuert und geändert werden.
Eine optionale Einbindung in bestehende Smart-Home-Systeme wie bspw. [FHEM](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#81-fhem), [openHAB](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#82-openhab), [HomeMatic](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#83-homematic-eq3), [ioBroker](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#84-iobroker), [Loxone](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#85-loxone), [IP-Symcon](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#86-ip-symcon), [EDOMI](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#810-edomi), [Home Assistant](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#811-home-assistant), [SmartHomeNG](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#812-smarthomeng) oder [Node-RED](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#813-node-red) kann mittels [HTTPMOD](https://1coderookie.github.io/BSB-LPB-LAN/kap08.html#812-einbindung-mittels-httpmod-modul), [MQTT](https://1coderookie.github.io/BSB-LPB-LAN/kap05.html#52-mqtt) oder [JSON](https://1coderookie.github.io/BSB-LPB-LAN/kap05.html#53-json) erfolgen. 
Darüber hinaus ist der Einsatz des Adapters als [Standalone-Logger](https://1coderookie.github.io/BSB-LPB-LAN/kap06.html#61-loggen-von-daten) ohne LAN- oder Internetanbindung bei Verwendung einer microSD-Karte ebenfalls möglich.  
Zusätzlich können [Temperatur- und Feuchtigkeitssensoren](https://1coderookie.github.io/BSB-LPB-LAN/kap07.html#71-verwendung-optionaler-sensoren-dht22-ds18b20-bme280) angeschlossen und deren Daten ebenso geloggt und ausgewertet werden. Durch die Möglichkeit, [eigenen Code in die BSB-LAN-Software zu integrieren](https://1coderookie.github.io/BSB-LPB-LAN/kap06.html#68-eigenen-code-in-bsb-lan-einbinden), bietet sich darüber hinaus ein weites Spektrum an Erweiterungsmöglichkeiten. 
   
Prinzipiell sollte diese Kombination aus Hard- und Software mit allen Heizungssystemen lauffähig sein, deren Steuerung über einen BSB oder LPB verfügt.  
Als einfache Regel kann man sagen, dass die Regler mit einem **S** in der Typenbezeichnung (RV**S** und LM**S**) kompatibel mit BSB-LAN sind und den (nahezu) kompletten Funktionsumfang bieten.  
Die folgende Auflistung gibt eine grobe Übersicht über die Reglertypen, die je nach Typ des Wärmeerzeugers (Öl, Gas, WP etc.) normalerweise verbaut sind (bzw. waren) und die mittels BSB-LAN bedient werden können. Gewisse Einzel- und Spezialfälle (wie bspw. ein RVS-Regler bei einem Gasgerät) sind hier nicht berücksichtigt. Für genauere Informationen bzgl der [Reglertypen](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#102-detaillierte-beschreibung-der-kompatiblen-regler) und der zu verwendenden [Anschlüsse](https://1coderookie.github.io/BSB-LPB-LAN/kap03.html#31-anschluss-des-adapters) lies bitte im [BSB-LPB-LAN-Handbuch](https://1coderookie.github.io/BSB-LPB-LAN/) nach.

**Gasregler:**  
- [LMU74/LMU75](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10211-lmu-regler) und (aktuelle Generation) [LMS14/LMS15](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10212-lms-regler), Anschluss via BSB  
- [LMU54/LMU64](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10211-lmu-regler), Anschluss via LPB über OCI420 Plugin  
   
**Öl-/Solar-/Zonenregler:**  
- [RVS43/RVS63/RVS46](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10222-rvs-regler), Anschluss via BSB  
- [RVA/RVP](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10221-rva--und-rvp-regler), Anschluss via PPS (modellspezifisch vereinzelt auch LPB)  
   
**Wärmepumpenregler:**  
- [RVS21/RVS61](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10222-rvs-regler), Anschluss via BSB  
   
**Weishaupt (Modell WTU):**  
- [RVS23](https://1coderookie.github.io/BSB-LPB-LAN/kap10.html#10222-rvs-regler), Anschluss via LPB      
  
**Im Folgenden werden einige Modellreihen verschiedener Hersteller aufgelistet, die i.d.R. BSB-LAN-kompatible Regler verbaut haben:**  
- Brötje: BBK, BBS, BGB, BLW (**nicht BLW NEO!**), BMR, BOB, BSK, Eurocontrol, SGB, SOB, SPK, WBS, WGB, WGB EVO, WGB Pro EVO, WGB-M, WGB-U, WOB 
- Bösch: heat pumps with RVS controller type
- Elco: Aerotop, Aquatop, Rendamax, Straton, Thision, Thision S, Thision S Plus, Trigon S Plus  
- ATAG: QR  
- Atlantic: Alféa Evolution, Axeo, Excellia, Extensa, Hynea hybrid duo gaz, Varmax  
- Austria Email: LWP, LWPK  
- Baxi: Luna Platinum
- Chappée: Klista
- CTA: Optiheat  
- Deville: 9942, 9981
- EVI Heat: Combi-7
- Fernwärme: RVD230
- Froeling: Rendagas Plus
- Fujitsu Waterstage: Comfort, Duo
- Geminox: Thrs
- Gruenenwald: Greenheat
- Hansa: SND
- Herz: Commotherm 5 DeLuxe
- Interdomo: Domostar GBK 25H/SH
- MAN/MHG: Ecostar 200
- MHG: Procon E
- Oilon: SH, SHx
- Olymp: SHS, WHS
- Sieger: TG11
- Sixmadun: TG11BE
- Termomax: Termo ÖV
- Thermics: Energie
- Thermital: TBox Clima TOP
- Tifell: Biofell
- Viessmann: Vitotwin 300-W
- Wamak: AiWa, DB
- Weishaupt: WTU
   
***Um eine detailliertere Übersicht der gemeldeten Systeme einzusehen, die bisher erfolgreich mit BSB-LAN genutzt werden, folge bitte dem entsprechenden Link:***  
- **[Brötje](https://1coderookie.github.io/BSB-LPB-LAN/kap11.html#111-brötje)**
- **[Elco](https://1coderookie.github.io/BSB-LPB-LAN/kap11.html#112-elco)**
- **[weitere Hersteller (z.B. Fujitsu, Atlantic, Weishaupt)](https://1coderookie.github.io/BSB-LPB-LAN/kap11.html#113-weitere-hersteller)**      

Wenn Deine Heizung einen der folgenden Regler enthält, aber Dein Modell noch nicht aufgeführt ist, setze Dich gerne mit uns in Verbindung, da diese Regler als kompatibel mit einem der unterstützten Bussysteme identifiziert wurden:   
AVS37, AVS55, AVS71, AVS74, AVS75, AVS77, AVS79, LMS14, LMS15, LMS15, LMU6x, LMU74, LMU75, RVA61, RVA63, RVA33, RVA36, RVA43, RVA46, RVA47, RVA53, RVA60, RVA61, RVA63, RVA65, RVA66, RVC32, RVD110, RVD115, RVD120, RVD125, RVD130, RVD135, RVD139, RVD140, RVD144, RVD145, RVD230, RVD235, RVD240, RVD245, RVD250, RVD255, RVD260, RVD265, RVL469, RVL470, RVL471, RVL472, RVL479, RVL480, RVL481, RVL482, RVP340, RVP350, RVP351, RVP360, RVP361, RVP5xx, RVS13, RVS21, RVS23, RVS26, RVS41, RVS43, RVS46, RVS47, RVS51, RVS53, RVS61, RVS63, RVS65, RVS68, RWI65, WRI80

<B>Achtung!</B><BR>
Einige Hersteller, die vormals auf BSB/LPB gesetzt haben, sind bei "günstigeren" Geräten auf andere Bus-Systeme gewechselt. Beispiele hierfür sind die Brötje WLC/WLS/BOK Geräte. Diese sind nicht kompatibel mit BSB/LPB und erlauben nur die Einstellung von wenigen Parametern durch den Benutzer. Besitzer dieser Geräte sind bis dato nicht in der Lage ihr Heizungssystem zu konfigurieren und zu überwachen, wie dies mit teureren (aber BSB/LPB-kompatiblen) Geräten, wie z.B. den oben genannten, möglich ist.
<BR><BR>
Die Forendiskussion die zum Bau dieses Adapters geführt hat, kann <A HREF="https://forum.fhem.de/index.php?topic=29762.new;topicseen#new">hier</A> nachvollzogen werden.<BR>

Bitte beachte, dass der Adapter zwar an einem Raspberry Pi genutzt werden kann, die hier angebotene Software jedoch nur auf dem ESP32 bzw. Arduino läuft! Wenn der Adapter an einem Raspberry Pi genutzt werden soll, muss stattdessen die Software bsb_gateway genutzt werden, die <A HREF="https://github.com/loehnertj/bsbgateway">hier</A> verfügbar ist. Bitte beachte, dass die Funktionalität am Raspberry deutlich weniger umfangreich ist, und dass Du für jegliche Fragen diesbezüglich den Autor von bsb_gateway kontaktieren musst.

Web-Interface screenshots:
<img src="https://github.com/fredlcore/bsb_lan/blob/master/BSB_LAN/schematics/Web-Interface.png" size="50%">
<img src="https://github.com/fredlcore/bsb_lan/blob/master/BSB_LAN/schematics/Web-Interface2.png" size="50%">

BSB-Adapterplatine in Bestückung für ESP32 Olimex Boards:
<img src="https://github.com/fredlcore/bsb_lan/blob/master/BSB_LAN/schematics/Logic%20Level%20Adapter.jpg" size="50%">

BSB-Adapterplatine auf ESP32 Olimex POE im 3D-gedruckten Projekt-Gehäuse:
<img src="https://github.com/fredlcore/bsb_lan/blob/master/BSB_LAN/schematics/Logic%20Level%20Adapter%20in%20Case.jpg" size="50%">
