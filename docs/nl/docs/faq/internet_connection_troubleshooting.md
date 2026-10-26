# Internet Connection Troubleshooting FAQ {#internet-connection-troubleshooting-faq}

## V1. Wat moet ik doen als ik geen internettoegang heb? {#q1-what-should-i-do-if-i-cannot-access-the-internet}

Volg de onderstaande stappen voor eenvoudige probleemoplossing.

1. Check the physical connection.

    Controleer of de Ethernetkabel stevig is aangesloten tussen de WAN-poort van de router en het bovenliggende apparaat, zoals een modem, ONT of Ethernetaansluiting. Controleer de leds en of er gegevensoverdracht plaatsvindt.

2. Reboot devices.

    Schakel het bovenliggende apparaat en de router uit. Wacht 1–2 minuten. Schakel eerst de modem in, wacht tot deze volledig online is en schakel daarna de router in.

3. Check the WAN IP address.

    Meld je aan bij het webbeheerpaneel en ga naar **INTERNET** -> **Ethernet**. Als de verbindingsstatus blijft hangen, kan er een DHCP-probleem, MAC-binding of VLAN-vereiste zijn.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Vraag je internetprovider of je voor internettoegang **PPPoE username**, **PPPoE password** en **VLAN ID** nodig hebt.

    Meanwhile, check whether your ISP previously configured **MAC binding** on your modem/ONT.

## V2. Wanneer moet ik een MAC-adres klonen? {#q2-when-should-i-clone-a-mac-address}

Sommige internetproviders koppelen je verbinding aan het MAC-adres van het eerste verbonden apparaat, meestal je oude router of computer. Wanneer je de router vervangt, moet je dit MAC-adres klonen om internettoegang te herstellen.

Volg de onderstaande stappen om een MAC-adres naar je GL.iNet-router te klonen.

1. Noteer het MAC-adres van je oude router of de computer die eerder aan de verbinding was gekoppeld.

2. Meld je aan bij het webbeheerpaneel en ga naar **NETWORK** -> **Ethernet Port**, in sommige versies **Port Management** genoemd. Stel MAC Mode in op **Clone** of **Manual**, voer het MAC-adres in en klik op **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Start de modem, het bovenliggende apparaat, opnieuw op.

## V3. Wanneer moet ik een VLAN ID configureren? {#q3-when-do-i-need-to-configure-a-vlan-id}

Sommige internetproviders vereisen VLAN-tagging voor internetverificatie of scheiding van verkeer, vooral bij glasvezel- en IPTV-verbindingen. Vraag je provider of een VLAN ID vereist is.

Follow the steps below to configure the VLAN ID.

1. Meld je aan bij de router, ga naar **INTERNET** -> **Ethernet** en klik op **Modify**.

2. Voer de VLAN ID van je provider in en klik op **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## V4. Wat als het nog steeds niet werkt? {#q4-what-if-it-still-doesnt-work}

Sluit een pc of laptop rechtstreeks op de modem aan en controleer of je internettoegang hebt.

Als je geen internettoegang hebt, ligt het probleem mogelijk bij je internetprovider. Neem contact op voor hulp.

Als je wel internettoegang hebt, ligt het probleem mogelijk aan de routerconfiguratie. Neem contact op via [support@gl-inet.com](mailto:support@gl-inet.com) en verstrek de volgende informatie:

- Router model
- Troubleshooting steps you have tried
- Your ISP name
- Any other information you think may help us assist you

## ISP information {#isp-information}

Hieronder staat regionale informatie over internetproviders, door GL.iNet samengesteld uit klantfeedback, forums en OpenWRT-bronnen. Deze is alleen bedoeld als referentie.

| Country/Region   | ISP   | Connection Type | VLAN ID | MAC Clone Required | Additional Requirements |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| United States    | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | Must enable IP Passthrough; EAP authentication bypass needed |
| United States | Spectrum | DHCP | N/A | Yes (in some areas) | Strong MAC binding (modem reboot required) |
| United States | Verizon Fios | DHCP | N/A | No | |
| United States | Comcast Xfinity | DHCP | N/A | Yes (common) | Must reboot modem when changing router (MAC release) |
| United States | Cox Communications | DHCP | N/A | Yes | Must reboot modem when changing router (MAC release) |
| United States | Frontier Fiber | DHCP | N/A | No | |
| United States | CenturyLink / Lumen | PPPoE | 201 | No | VLANs are required in certain areas. |
| Canada | Bell Canada Fibe | PPPoE | 35 | No | |
| Germany | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 mandatory for internet; PPPoE credentials required |
| Germany | Vodafone (Kabel) | DHCP | N/A | Yes (sometimes) | MAC binding may apply; reboot modem after router change |
| Germany | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 mandatory for internet |
| Germany | DNS:NET | PPPoE | 37 | No | |
| Germany | o2(UGG) | PPPoE | 7 | No | |
| United Kingdom | BT Broadband | PPPoE | 101 | No | VLAN 101 required; PPPoE login needed |
| United Kingdom | Sky Broadband | DHCP (Option 61) | 101 | No | Requires DHCP Option 61 (client identifier) |
| Verenigd Koninkrijk | Virgin | DHCP | N.v.t. | Ja | De modem staat in bridgemodus en vereist het klonen van het MAC-adres. |
| France | Orange | DHCP / PPPoE | 832 | No | VLAN 832 required; may require Option 90 authentication |
| France | Free (Freebox) | DHCP | N/A | No | |
| France | Bouygues Telecom | DHCP | 100 | Yes | Clone Bbox MAC |
| Spain | Movistar | PPPoE | 6 | No | VLAN 6 (internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spain | DIGI | PPPoE | 20 | No | |
| Spain | Orange | DHCP | 832/835 | No | VLANs may vary by region |
| Italy | TIM | PPPoE | 835 | No | VLAN 835 required |
| Italy | Aruba | PPPoE | 835 | No | |
| Netherlands | KPN | DHCP | 6 | No | VLAN 6 required for internet |
| Netherlands | Tweak | DHCP | 34 | Yes | Cloning Experia Box MAC |
| Netherlands | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Netherlands | Odido | DHCP | 300 | No | |
| Belgium | EDPnet | PPPoE | 10 | No | |
| Bosnia and Herzegovina | BH Telecom | PPPoE | 100 | No | |
| Croatia | Terrakom | PPPoE | 905 | No | |
| Czech Republic | O2 | PPPoE | 848 | No | |
| Cyprus | Epic | PPPoE | 35 | No | |
| Cyprus | Cyta | PPPoE | 42 | No | |
| Cyprus | Cablenet | PPPoE | 42 | No | |
| Cyprus | Primetel | PPPoE | 42 | No | |
| Poland | Orange Polska | PPPoE | 35 | No | VLAN 35 required |
| Poland | T-mobile | PPPoE | 35 | No | |
| Ireland | Vodafone SIRO | PPPoE | 10 | No | |
| Ireland | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Türkiye | Turknet | PPPoE | 35 | No | |
| Türkiye | Turk Telekom | PPPoE | 35 | No | |
| Türkiye | Turkcell Superonline | PPPoE | N/A | Yes | |
| Türkiye | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Greece | Cosmote | PPPoE | 835 | No | |
| Greece | Nova | PPPoE | 835 | Yes | |
| Greece | DEI/PPC | DHCP | 835 | No | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE requires MAP-E/DS-Lite compatible router |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | No | BBIX IPoE service commonly used |
| India | Airtel | PPPoE / DHCP | N/A | No | Some regions require PPPoE |
| India | JioFiber | DHCP | N/A | No | Locked ONT in many cases |
| Singapore | Singtel | PPPoE | 10 | No | VLAN 10 required; IPTV separate VLAN |
| Singapore | StarHub | DHCP | N/A | No | DHCP-based connection |
| Australia | NBN (various ISPs) | PPPoE / DHCP | 2 (common) | Yes | VLAN 2 common but ISP-dependent |
