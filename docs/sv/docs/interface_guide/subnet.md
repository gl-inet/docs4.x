# Subnet {#subnet}

**Obs!** Sidan är tillgänglig på Flint 4 (GL-BE14000) och lanseras för andra modeller med firmware v4.10.

---

Öppna **NETWORK** -> **Subnet**.

På den här sidan kan du konfigurera och hantera **Main Network**, **Guest Network**, **IoT Network** och egna **VLAN Networks** centralt. Du kan skapa och hantera flera subnät för att isolera olika typer av enheter eller trafik.

## Main Network {#main-network}

**Main Network** är nätverket som enheten ansluter till via huvud-Wi-Fi eller Ethernet.

I Main Network visas gränssnittsstatus, VLAN ID, routerns IP-adress och DHCP Range.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Klicka på **Edit** nere till höger för att konfigurera Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

Konfigurationssidan innehåller grundinställningar, DHCP-serverinställningar och Address Reservation.

### Basic Settings {#basic-settings}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Detta är adressen som du anger i webbläsarens adressfält för att öppna routerns administratörssida.

    Standardvärdet är **192.168.8.1**. Du kan ändra det om det står i konflikt med nätverket.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Standard-VLAN ID för Main Network är **1** och kan inte ändras.

- **AP Isolation**

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

### DHCP Server {#dhcp-server}

**DHCP Server** är aktiverad som standard och tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till klientenheter.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klicka på **Advanced** för ytterligare konfiguration vid behov.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server): En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Flera LPR-skrivarportar kan konfigureras.

### Address Reservation {#address-reservation}

När du reserverar en IP-adress för en LAN-klient får klienten samma IP-adress varje gång den använder routerns DHCP-server. Du kan reservera IP-adresser för datorer och servrar som kräver permanenta IP-inställningar.

**Obs!** Konfigurerade klienter måste ansluta till routern igen för att aktiveras.

Click **Add** to reserve an IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

You will see a pop-up window.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Välj **MAC** i listrutan. Tillgänglig **IP** fylls i automatiskt. Ange valfritt **hostname** och eget **name** och klicka på **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

När en ny IP-adressreservation har lagts till visas sidan nedan, vilket bekräftar att konfigurationen lyckades.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Guest Network {#guest-network}

**Guest Network** ger besökare ett separat Wi-Fi-nätverk som är isolerat från huvudnätverket.

**Obs!** Vissa modeller, till exempel GL-MT5000 och GL-MT2500/GL-MT2500A, saknar Wi-Fi-funktion. Inställningarna för Guest Network är därför inte tillgängliga i deras webbadministrationspanel.

I Guest Network visas gränssnittsstatus, VLAN ID, Gateway och DHCP Range.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Klicka på **Edit** nere till höger för att öppna konfigurationspanelen för Guest Network.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

Konfigurationssidan innehåller grundinställningar och DHCP-serverinställningar.

### Basic Settings {#basic-settings_1}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    **Standardgatewayen** för Guest Network är **192.168.9.1**. Om den står i konflikt med det lokala nätverket ändrar du den.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Standard-VLAN ID för Guest Network är **9** och kan ändras.

- **AP Isolation**

    Funktionen är tillgänglig från firmware v4.5.

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

- **WAN Access Control**

    WAN Access Control styr det lokala subnätets åtkomst till internet och andra WAN-subnät.

    Three WAN access control modes are available:

    - **Unrestricted**: Tillåter obegränsad åtkomst till internet och andra WAN-subnät.

    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.

    - **Block Internet Access**: Blockerar all utgående åtkomst till internet och WAN-subnät.

### DHCP Server {#dhcp-server_1}

**DHCP Server** är aktiverad som standard och tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till klientenheter.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klicka på **Advanced** för ytterligare konfiguration vid behov.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server): Hanterar utskriftsjobb och låter nätverksenheter skicka förfrågningar till fjärrskrivare. Flera LPR-portar kan konfigureras.

## IoT Network {#iot-network}

IoT Network skapar ett separat Wi-Fi-nätverk för IoT-enheter med bättre kompatibilitet och säkerhet.

**Obs!** Vissa modeller, till exempel GL-MT5000 och GL-MT2500/GL-MT2500A, saknar Wi-Fi-funktion. Inställningarna för IoT Network är därför inte tillgängliga i deras webbadministrationspanel.

I IoT Network visas gränssnittsstatus, VLAN ID, Gateway och DHCP Range.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Klicka på **Edit** nere till höger för att öppna panelen och konfigurera Basic Settings och DHCP Server Settings.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Basic Settings {#basic-settings_2}

Du kan ange ett subnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` och `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    **Standardgatewayen** för IoT Network är **192.168.10.1**. Om den står i konflikt med det lokala nätverket ändrar du den.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Standard-VLAN ID för IoT Network är **10** och kan ändras.

- **AP Isolation**

    Funktionen är tillgänglig från firmware v4.5.

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

- **WAN Access Control**

    WAN Access Control styr det lokala subnätets åtkomst till internet och andra WAN-subnät.

    Three WAN access control modes are available:

    - **Unrestricted**: Tillåter obegränsad åtkomst till internet och andra WAN-subnät.

    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.

    - **Block Internet Access**: Blockerar all utgående åtkomst till internet och WAN-subnät.

### DHCP Server {#dhcp-server_2}

**DHCP Server** är aktiverad som standard och tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till klientenheter.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klicka på **Advanced** för ytterligare konfiguration vid behov.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server): En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Flera LPR-skrivarportar kan konfigureras.

## VLAN Networks {#vlan-networks}

Högst upp kan du skapa fler **VLAN networks** för att isolera enheter eller besökartrafik.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Klicka på **+ Add** till höger för ett nytt nätverk.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Basic Settings {#basic-settings_3}

Här konfigurerar du grundinformationen för **VLAN Networks**.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Customize a name for your newly created subnet for identification.

- **Gateway**

    Konfigurera gateway för det nya subnätet manuellt och ändra den vid konflikt med LAN-segmentet.

- **Netmask**

    Standardvärdet är **255.255.255.0**. Du kan även välja **255.255.0.0** om du behöver ett större subnät med fler IP-adresser.

- **VLAN ID**

    Tilldela ett VLAN ID mellan **9** och **4000** och undvik ID som redan används.

- **AP Isolation**

    Funktionen är tillgänglig från firmware v4.5.

    Du kan isolera klientenheter i ett separat nätverkssegment. Enheterna kan då inte kommunicera med andra enheter i samma nätverk.

- **WAN Access Control**

    WAN Access Control styr det lokala subnätets åtkomst till internet och andra WAN-subnät.

    Three WAN access control modes are available:

    - **Unrestricted**: Tillåter obegränsad åtkomst till internet och andra WAN-subnät.

    - **Block WAN Subnet**: Blocks access to other WAN-side subnets. Internet access remains available.

    - **Block Internet Access**: Blockerar all utgående åtkomst till internet och WAN-subnät.

### DHCP Server {#dhcp-server_3}

**DHCP Server** är aktiverad som standard och tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till klientenheter.

Om DHCP-servern är inaktiverad måste du konfigurera klientenheternas nätverksinställningar manuellt. Klicka [här](../tutorials/manually_configure_static_ip.md) för att läsa om manuell konfiguration av en statisk IP-adress.

Du kan ändra den första och sista IP-adressen efter behov, till exempel om nätverket utökas eller minskas, IP-adresskonflikter uppstår eller nätmaskintervallet ändras.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Klicka på **Advanced** för ytterligare konfiguration vid behov.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Den period som en DHCP-tilldelad IP-adress är giltig för en enhet.

- **Gateway**: Enheten som dirigerar trafik mellan det lokala nätverket och externa nätverk, till exempel internet.

- **DNS Server 1**: Den primära servern som översätter domännamn till IP-adresser.

- **DNS Server 2**: Den sekundära servern som används för domännamnsupplösning om den primära DNS-servern inte är tillgänglig.

- **LPR Server** (Line Printer Remote Server): En tjänst som hanterar utskriftsjobb och låter nätverksenheter skicka utskriftsförfrågningar till fjärrskrivare. Flera LPR-skrivarportar kan konfigureras.

Efter konfigurationen visas det nya VLAN-nätverket och subnätsinformationen på sidan.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
