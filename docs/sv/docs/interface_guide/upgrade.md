# Upgrade {#upgrade}

Öppna **SYSTEM** -> **Upgrade** för att uppdatera routerns firmware.

På vissa mobilnätsmodeller kan modulversionen också uppgraderas.

!!! Warning

    Låt strömmen vara på under uppgraderingen. Stäng **INTE** av routern. Enheten startas om automatiskt efter några minuter.

## Firmware Upgrade {#firmware-upgrade}

### Online Upgrade {#online-upgrade}

Online Upgrade söker automatiskt efter officiell firmware och hämtar och installerar den direkt på routern.

Aktuell firmwareversion visas under **Firmware Online Upgrade**.

![upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/online_upgrade.png){class="glboxshadow"}

- **Accept Preview Plan**

    När alternativet är aktiverat kan du prova nya funktioner före slutversionen och ge feedback. Versionerna kan vara instabila.

**Obs!** Om **Download Failed** visas öppnar du System -> Time Zone och synkroniserar tidszonen med webbläsaren.

![online download failed](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/online_download_failed.jpg){class="glboxshadow" width="360"}

![time zone](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/time_zone.png){class="glboxshadow"}

### Local Upgrade {#local-upgrade}

Local Upgrade supports manual firmware file upload for flashing, enabling users to upgrade, downgrade, or install beta firmware of specific versions to test newly added features.

Hämta firmwarefilen från vårt [nedladdningscenter](https://dl.gl-inet.com){target="_blank"} och öppna **Firmware Local Upgrade**.

![local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/local_upgrade.png){class="glboxshadow"}

Välj filen eller dra den till uppladdningsområdet. Systemet verifierar firmware.

![local upgrade uploaded](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/local_upgrade_uploaded.png){class="glboxshadow"}

- **Keep Settings:** Behåller aktuella inställningar och uppmanar dig att installera om egna paket. Markera INTE vid nedgradering.

Click **Install** to upgrade.

## Modem Upgrade {#modem-upgrade}

GL.iNet cellular routers allow users to upgrade the cellular modem firmware through the web Admin Panel.

Prova en moduluppgradering om mobilnätet inte fungerar eller är instabilt. Kontakta teknisk support före uppgraderingen.

### Online Upgrade {#online-upgrade_1}

Aktuell modemversion visas här. När routern är ansluten söker den automatiskt efter senaste versionen på tillverkarens server.

![modem online upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_online_upgrade.png){class="glboxshadow"}

### Local Upgrade {#local-upgrade_1}

Ladda vid behov upp en modemfirmwarefil manuellt.

![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

## DPI Online Upgrade {#dpi-online-upgrade}

DPI Online Upgrade uppdaterar DPI-motorn och signaturdatabasen för korrekt trafikidentifiering i Data Statistics, Content Filter och andra DPI-funktioner.

**Note**: This feature was introduced in firmware v4.11.

![dpi online upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/dpi_online_upgrade.png){class="glboxshadow" width=700}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
