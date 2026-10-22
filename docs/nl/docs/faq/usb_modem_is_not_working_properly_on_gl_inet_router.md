# USB-modem werkt niet goed op een GL.iNet-router {#usb-modem-is-not-working-properly-on-glinet-router}

Sommige GL.iNet-routers hebben USB-poorten. Je kunt een USB-modem aansluiten voor internettoegang en deze samen met andere internetverbindingen gebruiken in een Multi-WAN-configuratie.

Sommige USB-modems, zoals de ZTE F50 Mobile Wi-Fi Hotspot, werken mogelijk niet goed op de router en veroorzaken regelmatig netwerkuitval.

Dit kan komen door een compatibiliteitsprobleem tussen de USB-poort van de router, meestal USB 3.0, en 2.4G-wifi. Hierdoor valt de USB-modem steeds uit en werkt internettoegang niet goed.

Schakel de USB-poort van USB 3.0 naar USB 2.0 om dit probleem op te lossen.

Access your GL.iNet router's admin panel, go to **SYSTEM -> Overview -> External Storage**.

Je ziet de optie USB Protocol Switch.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Stel deze in op USB 2.0. Er verschijnt een melding zoals hieronder. Klik op Switch om door te gaan.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Als USB 2.0 als USB-protocol wordt weergegeven, is de wijziging geslaagd.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Controleer daarna of de internetverbinding is verbeterd.

---

Gerelateerde artikelen

- [Compatible Modems](../interface_guide/internet_cellular.md#compatible-modems)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
