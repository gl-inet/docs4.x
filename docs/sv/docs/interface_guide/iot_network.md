# IoT Network {#iot-network}

**Note**: The IoT Network feature was introduced in firmware v4.9.

---

Öppna **NETWORK** -> **IoT Network** på vänster sida i webbadministrationspanelen.

På sidan kan du skapa ett särskilt Wi-Fi-nätverk för IoT-enheter. Det är isolerat från det primära nätverket och ger bättre kompatibilitet och säkerhet.

**Obs!** Vissa modeller, till exempel GL-MT5000 och GL-MT2500/GL-MT2500A, saknar Wi-Fi-funktion. Inställningarna för IoT Network är därför inte tillgängliga i deras webbadministrationspanel.

It includes two sections: Basic Settings and DHCP Server Settings.

## Basic Settings {#basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot1.png){class="glboxshadow"}

- **Gateway**

    **Standardgatewayen** för IoT Network är **192.168.10.1**. Om den står i konflikt med det lokala nätverket ändrar du den.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **AP Isolation**

    Funktionen är tillgänglig från firmware v4.5.

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

- **Block WAN Subnets**

    Funktionen är tillgänglig från firmware v4.8.

    När alternativet är aktiverat kan IoT-nätverket inte komma åt det uppströms nätverket och dess subnät.

## DHCP Server {#dhcp-server}

If IoT Network is enabled, its DHCP server will be enabled accordingly.

DHCP-servern tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till varje klientenhet som är ansluten till IoT Network. Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot2.png){class="glboxshadow"}

Click **Advanced** for further configuration as needed.

![iot network 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot3.png){class="glboxshadow"}

![iot network 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot4.png){class="glboxshadow"}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan IoT-nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server**: (Line Printer Remote Server) En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Flera LPR-skrivarportar kan konfigureras.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
