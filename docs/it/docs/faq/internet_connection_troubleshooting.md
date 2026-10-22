# FAQ sulla risoluzione dei problemi di connessione Internet {#internet-connection-troubleshooting-faq}

## D1. Cosa devo fare se non riesco ad accedere a Internet? {#q1-what-should-i-do-if-i-cannot-access-the-internet}

Segui i passaggi seguenti per una risoluzione di base dei problemi.

1. Controlla il collegamento fisico.

    Assicurati che il cavo Ethernet sia collegato saldamente tra la porta WAN del router e il dispositivo a monte, ad esempio modem, ONT o presa Ethernet. Controlla i LED del dispositivo a monte e verifica che ci sia trasmissione attiva.

2. Riavvia i dispositivi.

    Spegni il dispositivo a monte, ad esempio il modem, e il router. Attendi 1-2 minuti. Quindi accendi prima il modem, aspetta che sia completamente online e poi accendi il router.

3. Controlla l'indirizzo IP WAN.

    Accedi al pannello di amministrazione web del router e vai alla sezione **INTERNET** -> **Ethernet**. Se rimane bloccato nello stato di connessione, come mostrato di seguito, il problema potrebbe dipendere da DHCP, binding MAC o dalla necessità di una VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Contatta il tuo ISP e verifica se per l'accesso a Internet sono necessari **PPPoE username**, **PPPoE password** e **VLAN ID**.

    Nel frattempo, verifica anche se il tuo ISP ha configurato in precedenza il **MAC binding** sul modem/ONT.

## D2. Quando dovrei clonare un indirizzo MAC? {#q2-when-should-i-clone-a-mac-address}

Alcuni ISP associano la tua connessione broadband all'indirizzo MAC del primo dispositivo collegato, in genere il vecchio router o il computer. Quando sostituisci il router, dovrai clonare l'indirizzo MAC per ripristinare l'accesso a Internet.

Segui i passaggi seguenti per clonare un indirizzo MAC sul router GL.iNet.

1. Annota l'indirizzo MAC del vecchio router, oppure del computer precedentemente associato alla tua connessione broadband.

2. Accedi al pannello di amministrazione web del router e vai su **NETWORK** -> **Ethernet Port** (in alcune versioni del firmware chiamato **Port Management**). Imposta MAC Mode su **Clone** o **Manual**, inserisci manualmente l'indirizzo MAC e poi fai clic su **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Riavvia il modem, cioè il dispositivo a monte.

## D3. Quando devo configurare un VLAN ID? {#q3-when-do-i-need-to-configure-a-vlan-id}

Alcuni ISP richiedono il tagging VLAN per l'autenticazione Internet o per la separazione del traffico, in particolare con connessioni in fibra e IPTV. Contatta il tuo ISP e verifica se è richiesto un VLAN ID.

Segui i passaggi seguenti per configurare il VLAN ID.

1. Accedi al router e vai alla sezione **INTERNET** -> **Ethernet**. Fai clic su **Modify**.

2. Inserisci il VLAN ID fornito dal tuo ISP, quindi fai clic su **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## D4. Cosa succede se ancora non funziona? {#q4-what-if-it-still-doesnt-work}

Se il problema persiste, prova a collegare direttamente un PC o un laptop al modem e verifica se hai accesso a Internet.

Se non hai accesso a Internet, il problema potrebbe dipendere dal tuo ISP. Contatta il tuo ISP per ulteriore assistenza.

Se invece hai accesso a Internet, il problema potrebbe essere legato alla configurazione del router. Contatta il nostro supporto tecnico all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com) e fornisci le seguenti informazioni:

- Modello del router
- Passaggi di risoluzione dei problemi che hai già provato
- Nome del tuo ISP
- Qualsiasi altra informazione che possa aiutarci ad assisterti

## Informazioni sugli ISP {#isp-information}

Di seguito trovi informazioni specifiche per area geografica sugli ISP, raccolte da GL.iNet da feedback dei clienti, forum e risorse OpenWRT, solo come riferimento.

| Paese/Regione   | ISP   | Tipo di connessione | VLAN ID | Clonazione MAC richiesta | Requisiti aggiuntivi |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| Stati Uniti | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | È necessario abilitare IP Passthrough; richiesto il bypass dell'autenticazione EAP |
| Stati Uniti | Spectrum | DHCP | N/A | Sì (in alcune aree) | Associazione MAC rigorosa (riavvio del modem necessario) |
| Stati Uniti | Verizon Fios | DHCP | N/A | No | |
| Stati Uniti | Comcast Xfinity | DHCP | N/A | Sì (spesso) | È necessario riavviare il modem quando si cambia router (rilascio MAC) |
| Stati Uniti | Cox Communications | DHCP | N/A | Sì | È necessario riavviare il modem quando si cambia router (rilascio MAC) |
| Stati Uniti | Frontier Fiber | DHCP | N/A | No | |
| Stati Uniti | CenturyLink / Lumen | PPPoE | 201 | No | Le VLAN sono richieste in alcune aree. |
| Canada | Bell Canada Fibe | PPPoE | 35 | No | |
| Germania | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 obbligatoria per Internet; credenziali PPPoE richieste |
| Germania | Vodafone (Kabel) | DHCP | N/A | Sì (a volte) | Potrebbe essere applicata l'associazione MAC; riavviare il modem dopo il cambio del router |
| Germania | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 obbligatoria per Internet |
| Germania | DNS:NET | PPPoE | 37 | No | |
| Germania | o2(UGG) | PPPoE | 7 | No | |
| Regno Unito | BT Broadband | PPPoE | 101 | No | VLAN 101 richiesta; accesso PPPoE necessario |
| Regno Unito | Sky Broadband | DHCP (Option 61) | 101 | No | Richiede DHCP Option 61 (identificatore client) |
| Regno Unito | Virgin | DHCP | N/A | Sì | Il modem è in modalità bridge e richiede la clonazione MAC. |
| Francia | Orange | DHCP / PPPoE | 832 | No | VLAN 832 richiesta; potrebbe richiedere l'autenticazione Option 90 |
| Francia | Free (Freebox) | DHCP | N/A | No | |
| Francia | Bouygues Telecom | DHCP | 100 | Sì | Clonare il MAC del Bbox |
| Spagna | Movistar | PPPoE | 6 | No | VLAN 6 (Internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spagna | DIGI | PPPoE | 20 | No | |
| Spagna | Orange | DHCP | 832/835 | No | Le VLAN possono variare in base alla regione |
| Italia | TIM | PPPoE | 835 | No | VLAN 835 richiesta |
| Italia | Aruba | PPPoE | 835 | No | |
| Paesi Bassi | KPN | DHCP | 6 | No | VLAN 6 richiesta per Internet |
| Paesi Bassi | Tweak | DHCP | 34 | Sì | Clonazione del MAC di Experia Box |
| Paesi Bassi | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Paesi Bassi | Odido | DHCP | 300 | No | |
| Belgio | EDPnet | PPPoE | 10 | No | |
| Bosnia ed Erzegovina | BH Telecom | PPPoE | 100 | No | |
| Croazia | Terrakom | PPPoE | 905 | No | |
| Repubblica Ceca | O2 | PPPoE | 848 | No | |
| Cipro | Epic | PPPoE | 35 | No | |
| Cipro | Cyta | PPPoE | 42 | No | |
| Cipro | Cablenet | PPPoE | 42 | No | |
| Cipro | Primetel | PPPoE | 42 | No | |
| Polonia | Orange Polska | PPPoE | 35 | No | VLAN 35 richiesta |
| Polonia | T-mobile | PPPoE | 35 | No | |
| Irlanda | Vodafone SIRO | PPPoE | 10 | No | |
| Irlanda | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Turchia | Turknet | PPPoE | 35 | No | |
| Turchia | Turk Telekom | PPPoE | 35 | No | |
| Turchia | Turkcell Superonline | PPPoE | N/A | Sì | |
| Turchia | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Grecia | Cosmote | PPPoE | 835 | No | |
| Grecia | Nova | PPPoE | 835 | Sì | |
| Grecia | DEI/PPC | DHCP | 835 | No | |
| Giappone | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE richiede un router compatibile con MAP-E/DS-Lite |
| Giappone | SoftBank Hikari | PPPoE / IPoE | N/A | No | Servizio BBIX IPoE comunemente utilizzato |
| India | Airtel | PPPoE / DHCP | N/A | No | In alcune regioni è richiesto PPPoE |
| India | JioFiber | DHCP | N/A | No | ONT bloccato in molti casi |
| Singapore | Singtel | PPPoE | 10 | No | VLAN 10 richiesta; IPTV su VLAN separata |
| Singapore | StarHub | DHCP | N/A | No | Connessione basata su DHCP |
| Australia | NBN (vari ISP) | PPPoE / DHCP | 2 (comune) | Sì | VLAN 2 comune ma dipendente dall'ISP |
