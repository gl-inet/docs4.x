# FAQ sulla risoluzione dei problemi di connessione Internet

## D1. Cosa devo fare se non riesco ad accedere a Internet?

Segui i passaggi seguenti per una risoluzione di base dei problemi.

1. Controlla il collegamento fisico.

    Assicurati che il cavo Ethernet sia collegato saldamente tra la porta WAN del router e il dispositivo a monte, ad esempio modem, ONT o presa Ethernet. Controlla i LED del dispositivo a monte e verifica che ci sia trasmissione attiva.

2. Riavvia i dispositivi.

    Spegni il dispositivo a monte, ad esempio il modem, e il router. Attendi 1-2 minuti. Quindi accendi prima il modem, aspetta che sia completamente online e poi accendi il router.

3. Controlla l'indirizzo IP WAN.

    Accedi al pannello di amministrazione web del router e vai alla sezione **INTERNET** -> **Ethernet**. Se rimane nello stato di connessione, come mostrato di seguito, il problema potrebbe dipendere da DHCP, binding MAC o dalla necessità di una VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Contatta il tuo ISP e verifica se per l'accesso a Internet sono necessari **PPPoE username**, **PPPoE password** e **VLAN ID**.

    Nel frattempo, verifica anche se il tuo ISP ha configurato in precedenza il **MAC binding** sul modem/ONT.

## D2. Quando dovrei clonare un indirizzo MAC?

Alcuni ISP associano la tua connessione broadband all'indirizzo MAC del primo dispositivo collegato, in genere il vecchio router o il computer. Quando sostituisci il router, dovrai clonare l'indirizzo MAC per ripristinare l'accesso a Internet.

Segui i passaggi seguenti per clonare un indirizzo MAC sul router GL.iNet.

1. Annota l'indirizzo MAC del vecchio router, oppure del computer precedentemente associato alla tua connessione broadband.

2. Accedi al pannello di amministrazione web del router e vai su **NETWORK** -> **Ethernet Port** (in alcune versioni del firmware chiamato **Port Management**). Imposta MAC Mode su **Clone** o **Manual**, inserisci manualmente l'indirizzo MAC e poi fai clic su **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Riavvia il modem, cioè il dispositivo a monte.

## D3. Quando devo configurare un VLAN ID?

Alcuni ISP richiedono il tagging VLAN per l'autenticazione Internet o per la separazione del traffico, in particolare con connessioni in fibra e IPTV. Contatta il tuo ISP e verifica se è richiesto un VLAN ID.

Segui i passaggi seguenti per configurare il VLAN ID.

1. Accedi al router e vai alla sezione **INTERNET** -> **Ethernet**. Fai clic su **Modify**.

2. Inserisci il VLAN ID fornito dal tuo ISP, quindi fai clic su **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## D4. Cosa succede se ancora non funziona?

Se il problema persiste, prova a collegare direttamente un PC o un laptop al modem e verifica se hai accesso a Internet.

Se non hai accesso a Internet, il problema potrebbe dipendere dal tuo ISP. Contatta il tuo ISP per ulteriore assistenza.

Se invece hai accesso a Internet, il problema potrebbe essere legato alla configurazione del router. Contatta il nostro supporto tecnico all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com) e fornisci le seguenti informazioni:

- Modello del router
- Passaggi di risoluzione dei problemi che hai già provato
- Nome del tuo ISP
- Qualsiasi altra informazione che possa aiutarci ad assisterti

## Informazioni sugli ISP

Di seguito trovi informazioni specifiche per area geografica sugli ISP, raccolte da GL.iNet da feedback dei clienti, forum e risorse OpenWRT, solo come riferimento.

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
| United Kingdom | Virgin | DHCP | N/A | Yes | The modem is in bridged mode and requires MAC cloning. |
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
