# Guest Network {#guest-network}

Inställningarna för gästnätverk är separerade från [LAN](lan.md) sedan firmware v4.5.

Öppna **NETWORK** -> **Guest Network** på vänster sida i webbadministrationspanelen.

På sidan kan du skapa ett särskilt Wi-Fi-nätverk för besökare. Det är isolerat från det primära nätverket och förbättrar säkerheten samtidigt som det ger smidig internetåtkomst.

**Obs!** Vissa modeller, till exempel GL-MT5000 och GL-MT2500/GL-MT2500A, saknar Wi-Fi-funktion. Inställningarna för Guest Network är därför inte tillgängliga i deras webbadministrationspanel.

It includes two sections: Basic Settings and DHCP Server Settings.

## Basic Settings {#basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

- **Gateway**

    **Standardgatewayen** för Guest Network är **192.168.9.1**. Om den står i konflikt med det lokala nätverket ändrar du den.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **AP Isolation**

    Funktionen är tillgänglig från firmware v4.5.

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

- **Block WAN Subnets**

    Funktionen är tillgänglig från firmware v4.8.

    När alternativet är aktiverat kan gästnätverket inte komma åt det uppströms nätverket och dess subnät.

## DHCP Server {#dhcp-server}

If Guest Network is enabled, its DHCP server will be enabled accordingly.

DHCP-servern tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till varje klientenhet som är ansluten till Guest Network. Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Click **Advanced** for further configuration as needed.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan gästnätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server**: (Line Printer Remote Server) En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Flera LPR-skrivarportar kan konfigureras.

---

Related Articles:

- [How to set up a guest Wi-Fi network on GL.iNet routers](../tutorials/how_to_set_up_a_guest_network.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
