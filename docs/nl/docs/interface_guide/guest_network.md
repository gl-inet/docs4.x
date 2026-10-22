# Guest Network {#guest-network}

De instellingen voor het gastnetwerk zijn sinds firmware v4.5 van [LAN](lan.md) gescheiden.

Ga links in het webbeheerpaneel naar **NETWORK** -> **Guest Network**.

Op deze pagina kun je een speciaal Wi-Fi-netwerk voor bezoekers maken. Dit netwerk is van het primaire netwerk gescheiden en biedt daardoor betere beveiliging en eenvoudige internettoegang.

**Opmerking**: sommige modellen, zoals GL-MT5000 en GL-MT2500/GL-MT2500A, hebben geen Wi-Fi-functie. De instellingen voor Guest Network zijn daarom niet beschikbaar in hun webbeheerpaneel.

De pagina bevat twee gedeelten: Basic Settings en DHCP Server Settings.

## Basisinstellingen {#basic-settings}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

- **Gateway**

    De **standaardgateway** van Guest Network is **192.168.9.1**. Wijzig deze als er een conflict met je lokale netwerk optreedt.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Je kunt ook **255.255.0.0** selecteren als je een groter subnet met meer IP-adressen nodig hebt.

- **AP Isolation**

    Deze functie is beschikbaar sinds firmware v4.5.

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Deze apparaten kunnen dan niet met andere apparaten in hetzelfde netwerk communiceren.

- **Block WAN Subnets**

    Deze functie is beschikbaar sinds firmware v4.8.

    Wanneer dit is ingeschakeld, heeft het gastnetwerk geen toegang tot het upstream netwerk en het bijbehorende subnet.

## DHCP-server {#dhcp-server}

Wanneer Guest Network is ingeschakeld, wordt de bijbehorende DHCP-server ook ingeschakeld.

De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters toe aan elk clientapparaat dat met Guest Network is verbonden. Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen voor clientapparaten handmatig configureren. Klik [hier](../tutorials/manually_configure_static_ip.md) om te lezen hoe je handmatig een statisch IP-adres configureert.

Je kunt de begin- en eind-IP-adressen aanpassen, bijvoorbeeld wanneer je netwerk groter of kleiner wordt, IP-adresconflicten optreden of het bereik van het subnetmasker wordt gewijzigd.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Klik zo nodig op **Advanced** voor verdere configuratie.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: de periode waarin een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway**: het apparaat dat verkeer tussen het gastnetwerk en externe netwerken, zoals internet, routeert.

- **DNS Server 1**: de primaire server die domeinnamen in IP-adressen omzet.

- **DNS Server 2**: de secundaire server voor domeinnaamomzetting wanneer de primaire DNS-server niet beschikbaar is.

- **LPR Server**: een Line Printer Remote Server-dienst die afdruktaken beheert en netwerkapparaten afdrukverzoeken naar externe printers laat verzenden. Je kunt meerdere LPR-printerpoorten configureren.

---

Gerelateerde artikelen:

- [Een gastnetwerk instellen op GL.iNet-routers](../tutorials/how_to_set_up_a_guest_network.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
