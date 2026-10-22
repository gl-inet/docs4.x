# Vanliga frågor om felsökning av internetanslutningen {#internet-connection-troubleshooting-faq}

## F1. Vad gör jag om jag inte kommer åt internet? {#q1-what-should-i-do-if-i-cannot-access-the-internet}

Följ stegen nedan för grundläggande felsökning.

1. Kontrollera den fysiska anslutningen.

    Kontrollera att Ethernet-kabeln sitter ordentligt mellan routerns WAN-port och uppströmsenheten (t.ex. ett modem, en ONT eller ett Ethernet-uttag). Kontrollera lysdioderna på uppströmsenheten och att överföring pågår.

2. Starta om enheterna.

    Stäng av uppströmsenheten (t.ex. modemet) och routern. Vänta i 1-2 minuter. Slå sedan först på modemet, vänta tills det är helt anslutet och slå därefter på routern.

3. Kontrollera WAN-IP-adressen.

    Logga in på routerns webbadministrationspanel och gå till **INTERNET** -> avsnittet **Ethernet**. Om den fastnar i anslutningsläget enligt nedan kan det bero på ett DHCP-problem, MAC-bindning eller krav på VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Kontakta internetleverantören och kontrollera om du behöver **PPPoE username**, **PPPoE password** och **VLAN ID** för internetåtkomst.

    Kontrollera samtidigt om internetleverantören tidigare har konfigurerat **MAC binding** på modemet/ONT-enheten.

## F2. När ska jag klona en MAC-adress? {#q2-when-should-i-clone-a-mac-address}

Vissa internetleverantörer binder bredbandsanslutningen till MAC-adressen för den första anslutna enheten, vanligtvis din gamla router eller dator. När routern byts ut måste du klona MAC-adressen för att återställa internetåtkomsten.

Följ stegen nedan för att klona en MAC-adress till GL.iNet-routern.

1. Anteckna MAC-adressen för den gamla routern (eller den dator som tidigare var bunden till bredbandsanslutningen).

2. Logga in på routerns webbadministrationspanel och gå till **NETWORK** -> **Ethernet Port** (kallas **Port Management** i vissa firmwareversioner). Ställ in MAC Mode på **Clone** eller **Manual**, ange MAC-adressen manuellt och klicka sedan på **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Starta om modemet (dvs. uppströmsenheten).

## F3. När behöver jag konfigurera ett VLAN-ID? {#q3-when-do-i-need-to-configure-a-vlan-id}

Vissa internetleverantörer kräver VLAN-taggning för internetautentisering eller trafikseparering, särskilt för fiber- och IPTV-anslutningar. Kontakta internetleverantören och kontrollera om ett VLAN-ID krävs.

Följ stegen nedan för att konfigurera VLAN-ID:t.

1. Logga in på routern och gå till **INTERNET** -> avsnittet **Ethernet**. Klicka på **Modify**.

2. Ange det VLAN-ID som internetleverantören har tillhandahållit och klicka sedan på **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## F4. Vad gör jag om det fortfarande inte fungerar? {#q4-what-if-it-still-doesnt-work}

Om problemet kvarstår ansluter du en stationär eller bärbar dator direkt till modemet och kontrollerar om du kommer åt internet.

Om du inte kommer åt internet kan problemet finnas hos internetleverantören. Kontakta internetleverantören för mer hjälp.

Om du kommer åt internet kan problemet vara relaterat till routerkonfigurationen. Kontakta vår tekniska support på [support@gl-inet.com](mailto:support@gl-inet.com) och ange följande information:

- Routermodell
- Felsökningssteg som du har provat
- Internetleverantörens namn
- Annan information som du tror kan hjälpa oss att hjälpa dig

## Information om internetleverantörer {#isp-information}

Nedan finns regionspecifik information om internetleverantörer som GL.iNet har sammanställt från kundåterkoppling, forum och OpenWRT-resurser. Informationen är endast avsedd som referens.

| Land/region   | Internetleverantör   | Anslutningstyp | VLAN-ID | MAC-kloning krävs | Ytterligare krav |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| USA    | AT&T Fiber | DHCP (IP Passthrough) | N/A | Nej | IP Passthrough måste aktiveras; förbikoppling av EAP-autentisering krävs |
| USA | Spectrum | DHCP | N/A | Ja (i vissa områden) | Stark MAC-bindning (modemet måste startas om) |
| USA | Verizon Fios | DHCP | N/A | Nej | |
| USA | Comcast Xfinity | DHCP | N/A | Ja (vanligt) | Modemet måste startas om när routern byts (MAC-frisläppning) |
| USA | Cox Communications | DHCP | N/A | Ja | Modemet måste startas om när routern byts (MAC-frisläppning) |
| USA | Frontier Fiber | DHCP | N/A | Nej | |
| USA | CenturyLink / Lumen | PPPoE | 201 | Nej | VLAN krävs i vissa områden. |
| Kanada | Bell Canada Fibe | PPPoE | 35 | Nej | |
| Tyskland | Deutsche Telekom | PPPoE | 7 | Nej | VLAN 7 är obligatoriskt för internet; PPPoE-inloggningsuppgifter krävs |
| Tyskland | Vodafone (Kabel) | DHCP | N/A | Ja (ibland) | MAC-bindning kan användas; starta om modemet efter routerbyte |
| Tyskland | 1&1 / O2 (Telekom line) | PPPoE | 7 | Nej | VLAN 7 är obligatoriskt för internet |
| Tyskland | DNS:NET | PPPoE | 37 | Nej | |
| Tyskland | o2(UGG) | PPPoE | 7 | Nej | |
| Storbritannien | BT Broadband | PPPoE | 101 | Nej | VLAN 101 krävs; PPPoE-inloggning krävs |
| Storbritannien | Sky Broadband | DHCP (Option 61) | 101 | Nej | Kräver DHCP Option 61 (klientidentifierare) |
| Storbritannien | Virgin | DHCP | N/A | Ja | Modemet är i bryggläge och kräver MAC-kloning. |
| Frankrike | Orange | DHCP / PPPoE | 832 | Nej | VLAN 832 krävs; autentisering med Option 90 kan krävas |
| Frankrike | Free (Freebox) | DHCP | N/A | Nej | |
| Frankrike | Bouygues Telecom | DHCP | 100 | Ja | Klona Bbox-enhetens MAC-adress |
| Spanien | Movistar | PPPoE | 6 | Nej | VLAN 6 (internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spanien | DIGI | PPPoE | 20 | Nej | |
| Spanien | Orange | DHCP | 832/835 | Nej | VLAN kan variera mellan regioner |
| Italien | TIM | PPPoE | 835 | Nej | VLAN 835 krävs |
| Italien | Aruba | PPPoE | 835 | Nej | |
| Nederländerna | KPN | DHCP | 6 | Nej | VLAN 6 krävs för internet |
| Nederländerna | Tweak | DHCP | 34 | Ja | Klona Experia Box-enhetens MAC-adress |
| Nederländerna | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | Nej | |
| Nederländerna | Odido | DHCP | 300 | Nej | |
| Belgien | EDPnet | PPPoE | 10 | Nej | |
| Bosnien och Hercegovina | BH Telecom | PPPoE | 100 | Nej | |
| Kroatien | Terrakom | PPPoE | 905 | Nej | |
| Tjeckien | O2 | PPPoE | 848 | Nej | |
| Cypern | Epic | PPPoE | 35 | Nej | |
| Cypern | Cyta | PPPoE | 42 | Nej | |
| Cypern | Cablenet | PPPoE | 42 | Nej | |
| Cypern | Primetel | PPPoE | 42 | Nej | |
| Polen | Orange Polska | PPPoE | 35 | Nej | VLAN 35 krävs |
| Polen | T-mobile | PPPoE | 35 | Nej | |
| Irland | Vodafone SIRO | PPPoE | 10 | Nej | |
| Irland | Pure Telecom | PPPoE | 10 | Nej | |
| Österrike | A1 Telekom | PPPoE | 2 | Nej | |
| Österrike | Fonira | PPPoE | 31 | Nej | |
| Turkiet | Turknet | PPPoE | 35 | Nej | |
| Turkiet | Turk Telekom | PPPoE | 35 | Nej | |
| Turkiet | Turkcell Superonline | PPPoE | N/A | Ja | |
| Turkiet | Turksat Kablonet | DHCP/PPPoE | N/A | Nej | |
| Grekland | Cosmote | PPPoE | 835 | Nej | |
| Grekland | Nova | PPPoE | 835 | Ja | |
| Grekland | DEI/PPC | DHCP | 835 | Nej | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | Nej | IPoE kräver en router som är kompatibel med MAP-E/DS-Lite |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | Nej | BBIX IPoE-tjänsten används ofta |
| Indien | Airtel | PPPoE / DHCP | N/A | Nej | Vissa regioner kräver PPPoE |
| Indien | JioFiber | DHCP | N/A | Nej | Låst ONT i många fall |
| Singapore | Singtel | PPPoE | 10 | Nej | VLAN 10 krävs; IPTV använder ett separat VLAN |
| Singapore | StarHub | DHCP | N/A | Nej | DHCP-baserad anslutning |
| Australien | NBN (olika internetleverantörer) | PPPoE / DHCP | 2 (vanligt) | Ja | VLAN 2 är vanligt men beror på internetleverantören |
