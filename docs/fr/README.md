# Qu'est-ce que BSB-LAN ?
<div style="float:left"><svg class='logo' viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg' height=100% width=100%><path id='b' d='m98 47-63 1c-6 0-12 4-11 11v88c1 5 3 10 10 11l79-1c25-1 24-53 4-61 11-5 18-49-19-49zM48 72h52c1 10-2 18-11 19l-38 1v22l43-1c14 0 14 11 14 20H48Z'/><use href='#b' x='246'/><path d='m268 350 1-100c2-14 14-16 29-1l56 59v-69h25l-1 99c1 12-12 17-22 7l-63-64v69Zm-65-173c-112 90-67 155-34 173-4-11-7-23-6-38h60c0 29-4 31-8 40 57-35 42-86 15-112-21-21-32-40-27-63zm-10 81c13 10 18 20 24 30h-48c5-9 8-18 24-30zM21 239h25v86h77v25l-90-1s-11 1-11-12z M246 47v25h-68c-10 1-11 18 1 18l47 1c41 3 37 63 2 66l-82 1v-25h77c11 0 12-18 0-18h-48c-42-5-37-67 0-67z'/></svg></div>
[BSB-LAN est une solution logicielle](https://www.bsb-lan.de)/matérielle pour accéder au [« Boiler-System-Bus » (BSB)][BSB], au [« Local-Process-Bus (LPB) »][LPB] et à la [« Punkt-zu-Punkt-Schnittstelle » (PPS)][PPS]. Le matériel BSB-LAN est disponible pour divers microcontrôleurs basés sur *ESP32* (ESP32 NodeMCU, Olimex EVB, Olimeé POE-ISO) ainsi que pour un *Arduino Due* avec un shield Ethernet. Il permet d'accéder aux systèmes de chauffage Atlantic, Brötje, Elco et de nombreux autres fabricants via Ethernet/WiFi, à condition qu'ils utilisent l'une des cartes électroniques Siemens répertoriés ci-dessous.

BSB-LAN permet de surveiller et de contrôler le système de chauffage et d'enregistrer toutes les valeurs reçues. Ce projet prend en charge presque tous les paramètres disponibles sur les systèmes de chauffage et peut être une alternative plus complète et plus économique à l'OZW 672, à l'OCI 700 ou au Remocon Net B.

L'[intégration facultative dans les systèmes domotiques existants](homeautomation.md) tels que [Home Assistant][HomeAssistant], [ioBroker][ioBroker], [openHAB][openHAB], [Node-RED][NodeRED], [Homebridge][Homebridge], [Jeedom][Jeedom], [SmartHomeNG][SmartHomeNG], [Volkszähler][Volkszaehler], [FHEM][FHEM], [HomeMatic][Homematic], Loxone, IP-Symcon ou EDOMI est possible via [MQTT][MQTT], [JSON][JSON] ou [HTTP access][using].

L'adaptateur peut également être utilisé comme carte d'acquisition sans connexion à Internet grâce à une carte microSD.

Les capteurs de température et d'humidité peuvent également être connectés et leurs données peuvent également être enregistrées et analysées. Vous avez aussi la possibilité d'intégrer votre propre code dans le logiciel BSB-LAN, pour rajouter autant de fonctionnalités que vous le souhaitez.

# Où et comment commencer ?

- Vous êtes un utilisateur expérimenté ? Consultez les instructions de [démarrage rapide](quickstart.md) ou [mises à jour](install.md#mises-a-jour). Sinon (ou si vous rencontrez des problèmes), veuillez continuer à lire !
- Mon système de chauffage est-il pris en charge par BSB-LAN ? Veuillez consulter la [liste des systèmes de chauffage pris en charge](supported_heating_systems.md).
- Si vous savez déjà que votre système est pris en charge, en [savoir plus sur l'adaptateur BSB-LAN](bsb-lan_adapter.md) et où l'obtenir.
- Si vous avez déjà l'adaptateur, vous voudrez peut-être savoir [comment l'installer](install.md).
- Si vous avez installé l'adaptateur, vous devrez [configurer BSB-LAN](configure.md).
- Une fois que vous avez tout configuré, découvrez [comment utiliser BSB-LAN](using.md) ou en savoir plus sur les façons de [l'intégrer dans les systèmes de domotique](homeautomation.md).
- Si vous souhaitez mettre à jour BSB-LAN et que vous souhaitez savoir ce qui a changé depuis votre dernière installation, veuillez consulter le [ChangeLog](CHANGELOG.md).
- Nos [pages wiki](https://github.com/fredlcore/BSB-LAN/wiki) sont en constante évolution et fournissent des connaissances de base ainsi que des sujets plus spécialisés sur BSB-LAN et les systèmes de chauffage en général.
- Si vous rencontrez des problèmes, consultez la [page de dépannage](troubleshooting.md).
- Et avant de poser des questions à qui que ce soit, consultez d'abord nos [Foire aux questions (FAQ)](faq.md) !
