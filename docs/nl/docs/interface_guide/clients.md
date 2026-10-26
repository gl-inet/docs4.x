# Clients {#clients}

Ga links in het webbeheerpaneel naar **CLIENTS**.

De pagina Clients toont van links naar rechts informatie over verbonden apparaten, waaronder de apparaatnaam, het verbindingstype, het IP-adres, het MAC-adres, de snelheid en het verkeer.

## Apparaatnaam {#device-name}

De eerste kolom toont de apparaatnaam en het apparaattype, afhankelijk van de hostnaam van het apparaat.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Klik op het pictogram met drie stippen in de kolom Action en vervolgens in het vervolgkeuzemenu op **Modify** om de apparaatnaam en het type te wijzigen.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Verbindingstype {#connection-type}

Het blauwe pictogram rechts van de apparaatnaam geeft het verbindingstype of de verbindingsmethode van het apparaat aan.

Het geeft aan of het apparaat via Wi-Fi of een Ethernet-kabel met het netwerk is verbonden.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IP- en MAC-adres {#ip-and-mac-address}

De tweede kolom toont het IP- en MAC-adres van het verbonden apparaat.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Veel apparaten gebruiken willekeurige MAC-adressen. Als verbonden apparaten dit doen, verschijnt de volgende melding.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Opmerking**: als het tweede teken van het MAC-adres 2, 6, A of E is, zonder onderscheid tussen hoofdletters en kleine letters, wordt het als een willekeurig MAC-adres beschouwd. Sommige apparaten gebruiken echter een andere methode om een willekeurig MAC-adres te genereren. Deze detectiemethode is daarom mogelijk niet nauwkeurig.

## Speed {#speed}

De derde kolom toont de internetsnelheid van het verbonden apparaat. Dit is de gemiddelde snelheid over de afgelopen 3 minuten.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

**Opmerking**: het systeem begint de gemiddelde snelheid te berekenen wanneer deze pagina wordt geopend. Als de pagina bijvoorbeeld 10 seconden geopend is, wordt de gemiddelde snelheid alleen op die 10 seconden gebaseerd.

## Traffic {#traffic}

De vierde kolom toont het internetverkeer van het verbonden apparaat.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## Gereserveerd IP-adres {#reserved-ip}

In de vijfde kolom kun je met één klik een IP-adres voor een verbonden apparaat reserveren. Deze functie is geïntroduceerd in firmware v4.8.

Wanneer je voor een client in het LAN een IP-adres reserveert, ontvangt deze telkens hetzelfde IP-adres van de DHCP-server van de router.

Je kunt gereserveerde IP-adressen toewijzen aan computers of servers die permanente IP-instellingen nodig hebben.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blokkeerlijst {#blocklist}

In de zesde kolom kun je bepaalde verbonden apparaten met één klik blokkeren.

De toegangscontroleregel is standaard Blocklist. Je kunt bovenaan zo nodig overschakelen naar Allowlist.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: apparaten met een MAC-adres op de blokkeerlijst mogen geen verbinding maken met deze router.

- **Allowlist**: alleen apparaten met opgegeven MAC-adressen mogen verbinding maken. Dit is geschikt voor IoT-apparaten en zakelijk netwerkbeheer.

Je kunt bij **(1)** een lijst met MAC-adressen uit een bestand importeren of de adressen bij **(2)** handmatig invoeren om een Blocklist te maken.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Methode 1. Clients importeren**

Klik op de pagina Access Control op **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Klik op **Download Import Template** om het sjabloonbestand "mac-template.csv" te downloaden.

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Open het bestand, importeer de MAC-adressen en sla het op.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Selecteer het opgeslagen bestand of sleep het naar het uploadgebied.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Klik na een geslaagde upload op **Import** om de MAC-adressen als batch te importeren.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Methode 2. Handmatig invoeren**

Voer op de pagina Access Control handmatig het MAC-adres in van de apparaten die je wilt blokkeren en klik op **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Opmerking**: het blokkeren van een client is gebaseerd op het MAC-adres van het apparaat. Als het geblokkeerde apparaat de volgende keer een ander MAC-adres gebruikt, kan het nog steeds verbinding maken met de router.

## Action {#action}

### Details bekijken {#view-details}

Klik op het pictogram met drie stippen in de meest rechtse kolom Action en vervolgens in het vervolgkeuzemenu op **View Details** om de details van het clientapparaat te bekijken.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Op de geopende subpagina zie je alle informatie over het clientapparaat, waaronder eventuele IPv6-adressen.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modify {#modify}

Klik op het pictogram met drie stippen in de kolom Action en vervolgens in het vervolgkeuzemenu op **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Snelheid beperken {#limit-speed}

Klik op het pictogram met drie stippen in de kolom Action en vervolgens in het vervolgkeuzemenu op **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed1.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Als voor een client een snelheidslimiet is ingesteld, worden de pijlen voor de upload- en downloadsnelheid geel.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed2.png){class="glboxshadow"}

Klik op het pictogram met drie stippen in de kolom Action om de snelheidslimiet uit te schakelen.

### VPN-tunnel gebruiken {#use-vpn-tunnel}

**Opmerking**: deze optie is beschikbaar vanaf firmware v4.8 en verschijnt alleen in het menu Action als een MAC-gebaseerd beleid is geconfigureerd.

Voeg een client met MAC-gebaseerd beleid toe aan de lijst met VPN-tunnels. Ga naar VPN Dashboard om de tunnels uitgebreider aan te passen.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Sort {#sort}

De huidige sorteerregel wordt rechtsboven weergegeven. Je kunt naar een andere regel overschakelen.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.jpg){class="glboxshadow"}

De standaardsorteervolgorde is als volgt:

- Het huidige apparaat, waarmee je het Admin Panel opent, staat altijd bovenaan.
- In het gedeelte Online Clients staan apparaten die eerder verbinding hebben gemaakt hoger.
- In het gedeelte Offline Clients staan apparaten die eerder de verbinding hebben verbroken hoger.

## Settings {#settings}

Klik rechtsboven op **Settings** voor verdere handelingen.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/settings.png){class="glboxshadow"}

- **Clear Traffic Statistics**: wis met één klik de verkeersstatistieken van alle online clients. Na toepassing wordt de kolom met verkeersstatistieken op nul gezet en begint het verzamelen opnieuw.

    ![clear traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic_cleared.png){class="glboxshadow"}

- **Toggle Rate Unit**: wijzig de snelheidseenheid van de snelheidskolom tussen **KB/s** en **Kbps**.

- **Auto Remove Offline Clients**: deze functie is geïntroduceerd in firmware v4.9. Na inschakeling worden alle offline clients onmiddellijk gewist en niet meer in het gedeelte Offline Clients weergegeven.

    ![auto removal](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/auto_removal.png){class="glboxshadow"}

## Clients verwijderen {#remove-clients}

Klik in het gedeelte met offline clients rechtsboven op **Delete All** om alle offline clients te verwijderen.

Klik op het pictogram met drie stippen in de kolom Action en vervolgens in het vervolgkeuzemenu op **Remove Client** om een bepaalde client te verwijderen.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
