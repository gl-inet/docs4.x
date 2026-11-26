# LAN {#lan}

**Opmerking**: Deze pagina is gebaseerd op firmware v4.11 en hoger. Gebruikt je apparaat een andere firmwareversie? Selecteer hieronder de versie die bij je apparaat past.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.11 en hoger" markdown="1">

- [Firmware v4.9 en ouder](lan.md)

</div>

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **LAN**.

Op deze pagina kun je **Main Network**, **Guest Network**, **IoT Network** en aangepaste **VLAN Networks** centraal configureren en beheren. Je kunt meerdere subnetten maken en beheren om verschillende soorten apparaten of verkeer te isoleren.

## Hoofdnetwerk {#main-network}

**Main Network** is het netwerk waarmee je apparaat via het primaire Wi-Fi-netwerk of een ethernetkabel is verbonden.

In Main Network zie je de status van alle interfaces, de VLAN-ID, het IP-adres van de router en het DHCP-bereik.

![Overzicht van het hoofdnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Klik rechtsonder op **Edit** om Main Network te configureren.

![Configuratievenster van het hoofdnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

Op de configuratiepagina vind je de basisinstellingen, de instellingen van de DHCP-server en de IP-adresreserveringen.

### Basisinstellingen {#basic-settings}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![Basisinstellingen van het hoofdnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Voer dit adres in de adresbalk van je browser in om het webbeheerpaneel van de router te openen.

    Het standaardadres is **192.168.8.1**. Je kunt het wijzigen als het een conflict veroorzaakt met je netwerk.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Selecteer **255.255.0.0** als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    De VLAN-ID van Main Network staat vast op **1**.

- **AP Isolation**

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Daardoor kunnen ze niet communiceren met andere apparaten op hetzelfde netwerk.

    **Opmerking:** AP Isolation is alleen van toepassing op Wi-Fi-clients. Bekabelde apparaten vallen hierbuiten.

### DHCP-server {#dhcp-server}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters toe aan elk clientapparaat.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen van de clientapparaten handmatig configureren. Raadpleeg de handleiding voor [het handmatig instellen van een statisch IP-adres](../tutorials/manually_configure_static_ip.md).

Pas zo nodig het eerste en laatste IP-adres van het bereik aan, bijvoorbeeld als het netwerk groter of kleiner wordt, als er IP-adresconflicten optreden of als het bereik van het subnetmasker verandert.

![DHCP-basisinstellingen van het hoofdnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klik zo nodig op **Advanced** voor meer instellingen.

![Geavanceerde DHCP-instellingen van het hoofdnetwerk, deel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Geavanceerde DHCP-instellingen van het hoofdnetwerk, deel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** geeft aan hoelang een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway** is het apparaat dat verkeer routeert tussen het lokale netwerk en externe netwerken zoals internet.

- **DNS Server 1** is de primaire server die domeinnamen omzet in IP-adressen.

- **DNS Server 2** is de secundaire server die domeinnamen omzet als de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server) beheert afdruktaken en laat netwerkapparaten afdrukopdrachten naar externe printers sturen. Je kunt meerdere LPR-printerpoorten configureren.

### IP-adresreservering {#address-reservation}

Als je een IP-adres reserveert voor een client in het LAN, krijgt die client bij elke aanvraag aan de DHCP-server van de router hetzelfde IP-adres. Je kunt IP-adressen reserveren voor computers of servers die vaste IP-instellingen nodig hebben.

**Opmerking:** Clients met een nieuw gereserveerd IP-adres moeten opnieuw verbinding maken met de router om de reservering te activeren.

Klik op **Add** om een IP-adres te reserveren.

![Lijst met IP-adresreserveringen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Er verschijnt een pop-upvenster.

![Venster voor een nieuwe IP-adresreservering](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Selecteer **MAC** in de vervolgkeuzelijst. Het bijbehorende beschikbare **IP** wordt automatisch ingevuld. Vul eventueel een **hostname** en een eigen **name** in om de client makkelijker te herkennen. Klik vervolgens op **Submit**.

![Ingevulde IP-adresreservering](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Als de nieuwe IP-adresreservering is gelukt, zie je de onderstaande pagina.

![Overzicht met de nieuwe IP-adresreservering](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Gastnetwerk {#guest-network}

Het **Guest Network** biedt bezoekers een apart Wi-Fi-netwerk voor eenvoudige internettoegang. Het gastnetwerk is voor extra beveiliging gescheiden van het hoofdnetwerk.

**Opmerking**: Sommige modellen, zoals GL-MT5000 en GL-MT2500/GL-MT2500A, hebben geen Wi-Fi. De instellingen voor Guest Network zijn daarom bij deze modellen niet beschikbaar in het webbeheerpaneel.

In Guest Network zie je de interfacestatus, de VLAN-ID, de gateway en het DHCP-bereik.

![Overzicht van het gastnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Klik rechtsonder op **Edit**. Het configuratiepaneel voor Guest Network wordt rechts op de pagina geopend.

![Configuratievenster van het gastnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

Op de configuratiepagina vind je de basisinstellingen en de instellingen van de DHCP-server.

### Basisinstellingen {#guest-network-basic-settings}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![Basisinstellingen van het gastnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    De **standaardgateway** van Guest Network is **192.168.9.1**. Kies een ander adres als dit adres een conflict veroorzaakt met je lokale netwerk.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Selecteer **255.255.0.0** als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    De standaard-VLAN-ID van Guest Network is **9**. Je kunt deze zo nodig wijzigen.

- **Associated LAN Ports**

    Selecteer de LAN-poorten die je aan dit subnet wilt toewijzen. Bekabelde apparaten die op deze poorten zijn aangesloten, maken deel uit van dit netwerk.

- **AP Isolation**

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Daardoor kunnen ze niet communiceren met andere apparaten op hetzelfde netwerk.

    **Opmerking:** AP Isolation is alleen van toepassing op Wi-Fi-clients. Bekabelde apparaten vallen hierbuiten.

- **WAN Access Control**

    Met WAN Access Control regel je de toegang van het lokale subnet tot netwerken aan de WAN-zijde, waaronder internet en andere WAN-subnetten.

    Er zijn drie modi beschikbaar.

    - **Unrestricted** geeft dit subnet onbeperkte toegang tot internet en andere subnetten aan de WAN-zijde.

    - **Block WAN Subnet** blokkeert de toegang tot andere subnetten aan de WAN-zijde. Internettoegang blijft beschikbaar.

    - **Block Internet Access** blokkeert alle uitgaande toegang, ook tot internet en subnetten aan de WAN-zijde.

### DHCP-server {#guest-network-dhcp-server}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters toe aan elk clientapparaat.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen van de clientapparaten handmatig configureren. Raadpleeg de handleiding voor [het handmatig instellen van een statisch IP-adres](../tutorials/manually_configure_static_ip.md).

Pas zo nodig het eerste en laatste IP-adres van het bereik aan, bijvoorbeeld als het netwerk groter of kleiner wordt, als er IP-adresconflicten optreden of als het bereik van het subnetmasker verandert.

![DHCP-basisinstellingen van het gastnetwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klik zo nodig op **Advanced** voor meer instellingen.

![Geavanceerde DHCP-instellingen van het gastnetwerk, deel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Geavanceerde DHCP-instellingen van het gastnetwerk, deel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** geeft aan hoelang een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway** is het apparaat dat verkeer routeert tussen het lokale netwerk en externe netwerken zoals internet.

- **DNS Server 1** is de primaire server die domeinnamen omzet in IP-adressen.

- **DNS Server 2** is de secundaire server die domeinnamen omzet als de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server) beheert afdruktaken en laat netwerkapparaten afdrukopdrachten naar externe printers sturen. Je kunt meerdere LPR-printerpoorten configureren.

## IoT-netwerk {#iot-network}

IoT Network biedt een apart Wi-Fi-netwerk voor IoT-apparaten. Dit netwerk is gescheiden van het hoofdnetwerk voor betere compatibiliteit en beveiliging.

**Opmerking**: Sommige modellen, zoals GL-MT5000 en GL-MT2500/GL-MT2500A, hebben geen Wi-Fi. De instellingen voor IoT Network zijn daarom bij deze modellen niet beschikbaar in het webbeheerpaneel.

In IoT Network zie je de interfacestatus, de VLAN-ID, de gateway en het DHCP-bereik.

![Overzicht van het IoT-netwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Klik rechtsonder op **Edit**. Het configuratiepaneel voor IoT Network wordt rechts op de pagina geopend. Hier kun je de basisinstellingen en de instellingen van de DHCP-server aanpassen.

![Configuratievenster van het IoT-netwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Basisinstellingen {#iot-network-basic-settings}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![Basisinstellingen van het IoT-netwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    De **standaardgateway** van IoT Network is **192.168.10.1**. Kies een ander adres als dit adres een conflict veroorzaakt met je lokale netwerk.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Selecteer **255.255.0.0** als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    De standaard-VLAN-ID van IoT Network is **10**. Je kunt deze zo nodig wijzigen.

- **Associated LAN Ports**

    Selecteer de LAN-poorten die je aan dit subnet wilt toewijzen. Bekabelde apparaten die op deze poorten zijn aangesloten, maken deel uit van dit netwerk.

- **AP Isolation**

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Daardoor kunnen ze niet communiceren met andere apparaten op hetzelfde netwerk.

    **Opmerking:** AP Isolation is alleen van toepassing op Wi-Fi-clients. Bekabelde apparaten vallen hierbuiten.

- **WAN Access Control**

    Met WAN Access Control regel je de toegang van het lokale subnet tot netwerken aan de WAN-zijde, waaronder internet en andere WAN-subnetten.

    Er zijn drie modi beschikbaar.

    - **Unrestricted** geeft dit subnet onbeperkte toegang tot internet en andere subnetten aan de WAN-zijde.

    - **Block WAN Subnet** blokkeert de toegang tot andere subnetten aan de WAN-zijde. Internettoegang blijft beschikbaar.

    - **Block Internet Access** blokkeert alle uitgaande toegang, ook tot internet en subnetten aan de WAN-zijde.

### DHCP-server {#iot-network-dhcp-server}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters toe aan elk clientapparaat.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen van de clientapparaten handmatig configureren. Raadpleeg de handleiding voor [het handmatig instellen van een statisch IP-adres](../tutorials/manually_configure_static_ip.md).

Pas zo nodig het eerste en laatste IP-adres van het bereik aan, bijvoorbeeld als het netwerk groter of kleiner wordt, als er IP-adresconflicten optreden of als het bereik van het subnetmasker verandert.

![DHCP-basisinstellingen van het IoT-netwerk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klik zo nodig op **Advanced** voor meer instellingen.

![Geavanceerde DHCP-instellingen van het IoT-netwerk, deel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Geavanceerde DHCP-instellingen van het IoT-netwerk, deel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** geeft aan hoelang een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway** is het apparaat dat verkeer routeert tussen het lokale netwerk en externe netwerken zoals internet.

- **DNS Server 1** is de primaire server die domeinnamen omzet in IP-adressen.

- **DNS Server 2** is de secundaire server die domeinnamen omzet als de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server) beheert afdruktaken en laat netwerkapparaten afdrukopdrachten naar externe printers sturen. Je kunt meerdere LPR-printerpoorten configureren.

## VLAN-netwerken {#vlan-networks}

Bovenaan de hoofdpagina kun je zo nodig extra **VLAN networks** maken om verschillende soorten apparaten of bezoekersverkeer te isoleren.

![Overzicht voor VLAN-netwerken](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Klik rechts op **+ Add** om een nieuw netwerk te configureren.

![Configuratievenster voor VLAN-netwerken](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Basisinstellingen {#vlan-networks-basic-settings}

Op deze pagina kun je de basisinstellingen van **VLAN Networks** configureren.

![Basisinstellingen voor VLAN-netwerken](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Geef het nieuwe subnet een herkenbare naam.

- **Gateway**

    Stel de gateway voor het nieuwe subnet handmatig in. Wijzig deze als het adres een conflict veroorzaakt met het bestaande LAN-segment.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Selecteer **255.255.0.0** als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    Wijs bij het maken van een subnet een VLAN-ID tussen **9** en **4000** toe. Gebruik een vrije VLAN-ID om netwerkconflicten te voorkomen.

- **Associated LAN Ports**

    Selecteer de LAN-poorten die je aan dit subnet wilt toewijzen. Bekabelde apparaten die op deze poorten zijn aangesloten, maken deel uit van dit netwerk.

- **AP Isolation**

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Daardoor kunnen ze niet communiceren met andere apparaten op hetzelfde netwerk.

    **Opmerking:** AP Isolation is alleen van toepassing op Wi-Fi-clients. Bekabelde apparaten vallen hierbuiten.

- **WAN Access Control**

    Met WAN Access Control regel je de toegang van het lokale subnet tot netwerken aan de WAN-zijde, waaronder internet en andere WAN-subnetten.

    Er zijn drie modi beschikbaar.

    - **Unrestricted** geeft dit subnet onbeperkte toegang tot internet en andere subnetten aan de WAN-zijde.

    - **Block WAN Subnet** blokkeert de toegang tot andere subnetten aan de WAN-zijde. Internettoegang blijft beschikbaar.

    - **Block Internet Access** blokkeert alle uitgaande toegang, ook tot internet en subnetten aan de WAN-zijde.

### DHCP-server {#vlan-networks-dhcp-server}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters toe aan elk clientapparaat.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen van de clientapparaten handmatig configureren. Raadpleeg de handleiding voor [het handmatig instellen van een statisch IP-adres](../tutorials/manually_configure_static_ip.md).

Pas zo nodig het eerste en laatste IP-adres van het bereik aan, bijvoorbeeld als het netwerk groter of kleiner wordt, als er IP-adresconflicten optreden of als het bereik van het subnetmasker verandert.

![DHCP-basisinstellingen voor VLAN-netwerken](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Klik zo nodig op **Advanced** voor meer instellingen.

![Geavanceerde DHCP-instellingen voor VLAN-netwerken, deel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![Geavanceerde DHCP-instellingen voor VLAN-netwerken, deel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** geeft aan hoelang een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway** is het apparaat dat verkeer routeert tussen het lokale netwerk en externe netwerken zoals internet.

- **DNS Server 1** is de primaire server die domeinnamen omzet in IP-adressen.

- **DNS Server 2** is de secundaire server die domeinnamen omzet als de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server) beheert afdruktaken en laat netwerkapparaten afdrukopdrachten naar externe printers sturen. Je kunt meerdere LPR-printerpoorten configureren.

Na de configuratie verschijnt het nieuwe VLAN-netwerk op de huidige pagina, samen met de gegevens van het subnet.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
