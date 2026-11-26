# LAN {#lan}

**Obs!** Den här sidan gäller firmware v4.11 och senare. Om enheten kör en annan firmwareversion väljer du rätt guide i listan nedan.

<div class="gl-link-select" data-label="Firmwareversion" data-placeholder="Firmware v4.11 och senare" markdown="1">

- [Firmware v4.9 och tidigare](lan.md)

</div>

---

Öppna **NETWORK** -> **LAN** på vänster sida i webbadministrationspanelen.

På den här sidan kan du konfigurera och hantera **Main Network**, **Guest Network**, **IoT Network** och egna **VLAN Networks** på ett ställe. Du kan skapa och hantera flera subnät för att isolera olika typer av enheter eller trafik.

## Huvudnätverk {#main-network}

Huvudnätverket (**Main Network**) är det nätverk som din enhet ansluter till via det primära Wi-Fi-nätverket eller en Ethernet-kabel.

För huvudnätverket visas status för alla gränssnitt, VLAN-ID, routerns IP-adress och DHCP-intervallet.

![Huvudnätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Klicka på **Edit** nere till höger för att konfigurera huvudnätverket.

![Konfigurationspanel för huvudnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

På konfigurationssidan finns grundinställningar, inställningar för DHCP-servern och adressreservationer.

### Grundinställningar {#basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![Grundinställningar för huvudnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Ange den här adressen i webbläsarens adressfält för att öppna routerns webbadministrationspanel.

    Standardadressen är **192.168.8.1**. Du kan ändra den om den står i konflikt med nätverket.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Huvudnätverkets VLAN-ID är **1** som standard och kan inte ändras.

- **AP Isolation**

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

    **Obs!** AP-isolering gäller endast Wi-Fi-klienter. Kabelanslutna enheter omfattas inte.

### DHCP-server {#dhcp-server}

DHCP-servern (**DHCP Server**) är aktiverad som standard. Den tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till varje klientenhet.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Läs mer om [hur du konfigurerar en statisk IP-adress manuellt](../tutorials/manually_configure_static_ip.md).

Du kan ändra den första och sista IP-adressen i intervallet efter behov, till exempel om nätverket växer eller krymper, om IP-adresskonflikter uppstår eller om nätmaskens adressintervall ändras.

![Grundinställningar för DHCP-servern i huvudnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicka på **Advanced** om du behöver göra fler inställningar.

![Avancerade DHCP-inställningar för huvudnätverket, del 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Avancerade DHCP-inställningar för huvudnätverket, del 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Så länge gäller den IP-adress som DHCP tilldelar enheten.

- **Gateway**. Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**. Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**. Den sekundära servern som används för domännamnsuppslagning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server). En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Du kan konfigurera flera LPR-skrivarportar.

### Adressreservation {#address-reservation}

När du reserverar en IP-adress för en LAN-klient får klienten samma adress varje gång den kontaktar routerns DHCP-server. Du kan reservera IP-adresser för datorer eller servrar som kräver permanenta IP-inställningar.

**Obs!** Klienter med reserverad adress måste återansluta till routern för att inställningen ska börja gälla.

Klicka på **Add** för att reservera en IP-adress.

![Adressreservationer i huvudnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Ett dialogfönster öppnas.

![Dialogrutan för en ny adressreservation](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Välj **MAC** i listrutan. Den tillgängliga adressen fylls i automatiskt i fältet **IP**. Du kan även ange ett värdnamn (**hostname**) och ett eget namn (**name**) för att lättare identifiera enheten. Klicka sedan på **Submit**.

![Ifyllda uppgifter för en adressreservation](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

När adressreservationen har lagts till visas den på sidan nedan.

![Listan med den nya adressreservationen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Gästnätverk {#guest-network}

Gästnätverket (**Guest Network**) ger besökare ett eget Wi-Fi-nätverk med enkel åtkomst till internet. Nätverket är isolerat från huvudnätverket, vilket förbättrar säkerheten.

**Obs!** Vissa modeller, till exempel GL-MT5000 och GL-MT2500/GL-MT2500A, saknar stöd för Wi-Fi. Inställningarna för gästnätverket visas därför inte i deras webbadministrationspanel.

För gästnätverket visas gränssnittsstatus, VLAN-ID, gateway och DHCP-intervall.

![Gästnätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Klicka på **Edit** nere till höger. Konfigurationspanelen för gästnätverket öppnas till höger på sidan.

![Konfigurationspanel för gästnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

På konfigurationssidan finns grundinställningar och inställningar för DHCP-servern.

### Grundinställningar {#guest-network-basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![Grundinställningar för gästnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    **Standardgatewayen** för gästnätverket är **192.168.9.1**. Ändra den om den står i konflikt med det lokala nätverket.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Standardvärdet för VLAN-ID i gästnätverket är **9**. Du kan ändra det vid behov.

- **Associated LAN Ports**

    Välj vilka LAN-portar som ska tillhöra subnätet. Kabelanslutna enheter på de portarna ansluts till nätverket.

- **AP Isolation**

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

    **Obs!** AP-isolering gäller endast Wi-Fi-klienter. Kabelanslutna enheter omfattas inte.

- **WAN Access Control**

    Med **WAN Access Control** styr du det lokala subnätets åtkomst till nätverk på WAN-sidan, inklusive internet och andra WAN-subnät.

    Det finns tre lägen för åtkomstkontroll på WAN-sidan.

    - **Unrestricted**. Ger subnätet obegränsad åtkomst till internet och andra subnät på WAN-sidan.

    - **Block WAN Subnet**. Blockerar åtkomst till andra subnät på WAN-sidan. Internetåtkomst är fortfarande tillgänglig.

    - **Block Internet Access**. Blockerar all utgående åtkomst, inklusive åtkomst till internet och subnät på WAN-sidan.

### DHCP-server {#guest-network-dhcp-server}

DHCP-servern (**DHCP Server**) är aktiverad som standard. Den tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till varje klientenhet.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Läs mer om [hur du konfigurerar en statisk IP-adress manuellt](../tutorials/manually_configure_static_ip.md).

Du kan ändra den första och sista IP-adressen i intervallet efter behov, till exempel om nätverket växer eller krymper, om IP-adresskonflikter uppstår eller om nätmaskens adressintervall ändras.

![Grundinställningar för DHCP-servern i gästnätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicka på **Advanced** om du behöver göra fler inställningar.

![Avancerade DHCP-inställningar för gästnätverket, del 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Avancerade DHCP-inställningar för gästnätverket, del 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Så länge gäller den IP-adress som DHCP tilldelar enheten.

- **Gateway**. Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**. Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**. Den sekundära servern som används för domännamnsuppslagning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server). En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Du kan konfigurera flera LPR-skrivarportar.

## IoT-nätverk {#iot-network}

IoT-nätverket ger IoT-enheter ett eget Wi-Fi-nätverk med bättre kompatibilitet. Det är isolerat från huvudnätverket, vilket förbättrar säkerheten.

**Obs!** Vissa modeller, till exempel GL-MT5000 och GL-MT2500/GL-MT2500A, saknar stöd för Wi-Fi. Inställningarna för IoT-nätverket visas därför inte i deras webbadministrationspanel.

För IoT-nätverket visas gränssnittsstatus, VLAN-ID, gateway och DHCP-intervall.

![IoT-nätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Klicka på **Edit** nere till höger. Konfigurationspanelen för IoT-nätverket öppnas till höger på sidan. I panelen kan du ändra grundinställningar och inställningar för DHCP-servern.

![Konfigurationspanel för IoT-nätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Grundinställningar {#iot-network-basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![Grundinställningar för IoT-nätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    **Standardgatewayen** för IoT-nätverket är **192.168.10.1**. Ändra den om den står i konflikt med det lokala nätverket.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Standardvärdet för VLAN-ID i IoT-nätverket är **10**. Du kan ändra det vid behov.

- **Associated LAN Ports**

    Välj vilka LAN-portar som ska tillhöra subnätet. Kabelanslutna enheter på de portarna ansluts till nätverket.

- **AP Isolation**

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

    **Obs!** AP-isolering gäller endast Wi-Fi-klienter. Kabelanslutna enheter omfattas inte.

- **WAN Access Control**

    Med **WAN Access Control** styr du det lokala subnätets åtkomst till nätverk på WAN-sidan, inklusive internet och andra WAN-subnät.

    Det finns tre lägen för åtkomstkontroll på WAN-sidan.

    - **Unrestricted**. Ger subnätet obegränsad åtkomst till internet och andra subnät på WAN-sidan.

    - **Block WAN Subnet**. Blockerar åtkomst till andra subnät på WAN-sidan. Internetåtkomst är fortfarande tillgänglig.

    - **Block Internet Access**. Blockerar all utgående åtkomst, inklusive åtkomst till internet och subnät på WAN-sidan.

### DHCP-server {#iot-network-dhcp-server}

DHCP-servern (**DHCP Server**) är aktiverad som standard. Den tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till varje klientenhet.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Läs mer om [hur du konfigurerar en statisk IP-adress manuellt](../tutorials/manually_configure_static_ip.md).

Du kan ändra den första och sista IP-adressen i intervallet efter behov, till exempel om nätverket växer eller krymper, om IP-adresskonflikter uppstår eller om nätmaskens adressintervall ändras.

![Grundinställningar för DHCP-servern i IoT-nätverket](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicka på **Advanced** om du behöver göra fler inställningar.

![Avancerade DHCP-inställningar för IoT-nätverket, del 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Avancerade DHCP-inställningar för IoT-nätverket, del 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Så länge gäller den IP-adress som DHCP tilldelar enheten.

- **Gateway**. Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**. Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**. Den sekundära servern som används för domännamnsuppslagning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server). En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Du kan konfigurera flera LPR-skrivarportar.

## VLAN-nätverk {#vlan-networks}

Högst upp på sidan kan du skapa fler VLAN-nätverk (**VLAN networks**) för att isolera olika typer av enheter eller besökarnas trafik.

![VLAN-nätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Klicka på **+ Add** till höger på sidan för att konfigurera ett nytt nätverk.

![Konfigurationspanel för VLAN-nätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Grundinställningar {#vlan-networks-basic-settings}

Här anger du grundinställningarna för **VLAN Networks**.

![Grundinställningar för VLAN-nätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Ange ett namn som gör det lätt att identifiera det nya subnätet.

- **Gateway**

    Konfigurera gatewayen för det nya subnätet manuellt. Byt gateway om den står i konflikt med det befintliga LAN-segmentet.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    När du skapar ett subnät måste du tilldela det ett VLAN-ID mellan **9** och **4000**. Välj ett ledigt VLAN-ID för att undvika nätverkskonflikter.

- **Associated LAN Ports**

    Välj vilka LAN-portar som ska tillhöra subnätet. Kabelanslutna enheter på de portarna ansluts till nätverket.

- **AP Isolation**

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

    **Obs!** AP-isolering gäller endast Wi-Fi-klienter. Kabelanslutna enheter omfattas inte.

- **WAN Access Control**

    Med **WAN Access Control** styr du det lokala subnätets åtkomst till nätverk på WAN-sidan, inklusive internet och andra WAN-subnät.

    Det finns tre lägen för åtkomstkontroll på WAN-sidan.

    - **Unrestricted**. Ger subnätet obegränsad åtkomst till internet och andra subnät på WAN-sidan.

    - **Block WAN Subnet**. Blockerar åtkomst till andra subnät på WAN-sidan. Internetåtkomst är fortfarande tillgänglig.

    - **Block Internet Access**. Blockerar all utgående åtkomst, inklusive åtkomst till internet och subnät på WAN-sidan.

### DHCP-server {#vlan-networks-dhcp-server}

DHCP-servern (**DHCP Server**) är aktiverad som standard. Den tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till varje klientenhet.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Läs mer om [hur du konfigurerar en statisk IP-adress manuellt](../tutorials/manually_configure_static_ip.md).

Du kan ändra den första och sista IP-adressen i intervallet efter behov, till exempel om nätverket växer eller krymper, om IP-adresskonflikter uppstår eller om nätmaskens adressintervall ändras.

![Grundinställningar för DHCP-servern i VLAN-nätverk](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Klicka på **Advanced** om du behöver göra fler inställningar.

![Avancerade DHCP-inställningar för VLAN-nätverk, del 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![Avancerade DHCP-inställningar för VLAN-nätverk, del 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**. Så länge gäller den IP-adress som DHCP tilldelar enheten.

- **Gateway**. Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**. Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**. Den sekundära servern som används för domännamnsuppslagning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server). En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Du kan konfigurera flera LPR-skrivarportar.

När konfigurationen är klar visas det nya VLAN-nätverket och dess subnätsinformation på sidan.

---

Har du fler frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
