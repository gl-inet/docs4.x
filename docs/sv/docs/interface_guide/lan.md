# LAN {#lan}

Öppna **NETWORK** -> **LAN** på vänster sida i webbadministrationspanelen.

LAN är nätverket som enheten ansluter till via huvudnätverkets Wi-Fi eller en Ethernet-kabel.

It includes Basic settings, DHCP server settings and Address Reservation.

## Basic Settings {#basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    Detta är adressen som du anger i webbläsarens adressfält för att öppna routerns administratörssida.

    Standardvärdet är **192.168.8.1**. Du kan ändra det om det står i konflikt med nätverket.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **AP Isolation**

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

## DHCP Server {#dhcp-server}

**DHCP Server** är aktiverad som standard och tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till klientenheter.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Klicka på **Advanced** för ytterligare konfiguration vid behov.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server): En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Flera LPR-skrivarportar kan konfigureras.

## Address Reservation {#address-reservation}

När du reserverar en IP-adress för en LAN-klient får klienten samma IP-adress varje gång den använder routerns DHCP-server. Du kan reservera IP-adresser för datorer och servrar som kräver permanenta IP-inställningar.

**Obs!** Konfigurerade klienter måste ansluta till routern igen för att aktiveras.

Click **Add** to reserve an IP.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

You will see a pop-up window.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Välj **MAC** i listrutan. **IP** som motsvarar vald MAC fylls i automatiskt. Ange ett beskrivande namn och klicka på **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

När en ny IP-adressreservation har lagts till visas sidan nedan, vilket bekräftar att konfigurationen lyckades.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
