# Configure dual wired Ethernet WAN via an Ethernet to USB-A adapter {#configure-dual-wired-ethernet-wan-via-an-ethernet-to-usb-a-adapter}

Je kunt op een router met één WAN-poort twee bekabelde Ethernet-WAN-verbindingen configureren via een Ethernet-naar-USB-A-adapter.

GL.iNet-routers ondersteunen gangbare Ethernet-naar-USB-A-adapters. Hiermee sluit je de bekabelde verbinding van de router van je internetprovider via USB aan en voeg je naast de WAN-poort een extra bekabelde internetverbinding toe.

## Topology {#topology}

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Setup steps {#setup-steps}

1. Sluit de Ethernet-naar-USB-A-adapter aan op de USB-poort van je GL.iNet-router en verbind het andere uiteinde met de router van je internetprovider.

2. Install the USB driver.

    Meld je aan bij het webbeheerpaneel, ga naar **Application** -> **Plug-ins** en installeer het USB-netwerkstuurprogramma voor je adapter.

    Installeer bij een Realtek-adapter bijvoorbeeld **kmod-usb-net-rtl8152**.

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Wait for installation to complete.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Connect by USB Tethering.

    Once the driver installation is complete, navigate to **INTERNET** -> **Tethering** section.

    De USB-verbinding wordt gedetecteerd en kan met de router van je internetprovider worden verbonden.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Klik op **Connect** en wacht een minuut. Een groene stip en gegevens zoals een IP-adres geven aan dat de USB Tethering-verbinding is geslaagd.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
