# USB-modemet fungerar inte korrekt på GL.iNet-routern {#usb-modem-is-not-working-properly-on-glinet-router}

Vissa GL.iNet-routrar har USB-portar. Du kan ansluta ett USB-modem till USB-porten för att konfigurera internetåtkomst och även skapa Multi-WAN-scenarier om anslutningen kombineras med andra internetanslutningar.

Det kan dock hända att vissa USB-modem (till exempel ZTE F50 Mobile Wi-Fi Hotspot) inte fungerar normalt med routern, vilket leder till återkommande nätverksavbrott.

Det kan bero på ett kompatibilitetsproblem mellan routerns USB-port (vanligtvis USB3.0) och 2.4G Wi-Fi. Problemet gör att USB-modemet ständigt kopplas från och inte får normal internetåtkomst.

Du kan lösa problemet genom att ändra USB-portens specifikation från USB 3.0 till USB 2.0.

Öppna administrationspanelen för GL.iNet-routern och gå till **SYSTEM -> Overview -> External Storage**.

Alternativet USB Protocol Switch visas.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Ändra det till USB 2.0. En uppmaning enligt nedan visas. Klicka på Switch för att fortsätta.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

När USB-protokollet visas som USB 2.0 är ändringen klar.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Kontrollera sedan om internetanslutningen har förbättrats.

---

Relaterade artiklar

- [Kompatibla modem](../interface_guide/internet_cellular.md#compatible-modems)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
