# Clients {#clients}

Öppna **CLIENTS** på vänster sida i webbadministrationspanelen.

Sidan Clients visar information om anslutna enheter från vänster till höger: enhetsnamn, anslutningstyp, IP-adress, MAC-adress, hastighet och trafik.

## Device Name {#device-name}

Den första kolumnen visar enhetsnamn och enhetstyp, som baseras på enhetens värdnamn.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Ändra enhetsnamn och typ genom att klicka på ikonen med tre punkter i kolumnen Action och välja **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Connection Type {#connection-type}

Den blå ikonen till höger om enhetsnamnet visar enhetens anslutningstyp eller metod.

It indicates how the device is connected to the network - whether via Wi-Fi or an ethernet cable.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IP- och MAC-adress {#ip-and-mac-address}

Den andra kolumnen visar den anslutna enhetens IP- och MAC-adresser.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Många enheter använder slumpmässiga MAC-adresser. Om en ansluten enhet gör det visas följande meddelande.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Obs!** Om det andra tecknet i MAC-adressen är 2, 6, A eller E, oavsett skiftläge, betraktas den som slumpmässig. Vissa enheter kan använda andra regler, så identifieringen är inte alltid exakt.

## Speed {#speed}

Den tredje kolumnen visar den anslutna enhetens internethastighet som genomsnittet under de senaste 3 minuterna.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

**Obs!** Systemet börjar beräkna genomsnittshastigheten när sidan öppnas. Om sidan till exempel har varit öppen i 10 sekunder baseras genomsnittet endast på 10 sekunders data.

## Traffic {#traffic}

Den fjärde kolumnen visar den anslutna enhetens internettrafik.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## Reserved IP {#reserved-ip}

I den femte kolumnen kan du reservera en IP-adress för en ansluten enhet med ett klick. Funktionen introducerades i firmware v4.8.

När du reserverar en IP-adress för en LAN-klient får klienten samma IP-adress varje gång den använder routerns DHCP-server.

Du kan reservera IP-adresser för datorer eller servrar som kräver permanenta IP-inställningar.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blocklist {#blocklist}

I den sjätte kolumnen kan du blockera vissa anslutna enheter med ett klick.

Åtkomstkontrollregeln är Blocklist som standard. Du kan byta till Allowlist högst upp.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Enheter med MAC-adresser i blockeringslistan får inte ansluta till routern.

- **Allowlist**: Endast enheter med angivna MAC-adresser får ansluta. Passar IoT-enheter och företagsnätverk.

Skapa en Blocklist genom att importera MAC-adresser från en fil vid **(1)** eller ange dem manuellt vid **(2)**.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Method 1. Import Clients**

Klicka på **Import Clients** på sidan Access Control.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Klicka på **Download Import Template** för att hämta mallfilen "mac-template.csv".

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Öppna filen, importera MAC-adresserna och spara.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Select the saved file or drag it to the upload area.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

När uppladdningen är klar klickar du på **Import** för att slutföra batchimporten av MAC-adresser.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Method 2. Input Manually**

Ange MAC-adresserna för enheterna som ska blockeras manuellt på sidan Access Control och klicka på **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Obs!** Klientblockering baseras på enhetens MAC-adress. Om den blockerade enheten använder en annan MAC-adress nästa gång kan den fortfarande ansluta.

## Action {#action}

### View Details {#view-details}

Visa klientinformation genom att klicka på ikonen med tre punkter i kolumnen Action längst till höger och välja **View Details**.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Undersidan visar all information om klientenheten, däribland eventuella IPv6-adresser.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modify {#modify}

Klicka på ikonen med tre punkter i kolumnen Action och välj **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Limit Speed {#limit-speed}

Klicka på ikonen med tre punkter i kolumnen Action och välj **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed1.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

När en hastighetsgräns tillämpas på en klient blir pilarna för uppladdnings- och nedladdningshastighet gula.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed2.png){class="glboxshadow"}

Klicka på ikonen med tre punkter i kolumnen Action för att inaktivera hastighetsgränsen.

### Use VPN Tunnel {#use-vpn-tunnel}

**Obs!** Alternativet är tillgängligt från firmware v4.8 och visas endast på menyn Action om en MAC-baserad princip har konfigurerats.

Lägg till en klient i VPN-tunnellistan med en MAC-baserad princip. Hantera detaljerade tunnelinställningar på VPN Dashboard.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Sort {#sort}

Aktuell sorteringsregel visas uppe till höger och kan ändras.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.jpg){class="glboxshadow"}

The default sort order is as follows:

- Den egna enheten, som används för att öppna Admin Panel, visas alltid högst upp.
- I avsnittet Online Clients visas enheter som anslöt tidigare högre upp.
- I avsnittet Offline Clients visas enheter som kopplades från tidigare högre upp.

## Settings {#settings}

Klicka på **Settings** uppe till höger för fler åtgärder.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/settings.png){class="glboxshadow"}

- **Clear Traffic Statistics**: Rensa trafikstatistiken för alla onlineklienter med ett klick. Kolumnen återställs till noll och insamlingen startar om.

    ![clear traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic_cleared.png){class="glboxshadow"}

- **Toggle Rate Unit**: Växla hastighetskolumnens enhet mellan **KB/s** och **Kbps**.

- **Auto Remove Offline Clients**: Funktionen introducerades i firmware v4.9. När den aktiveras rensas alla offlineklienter omedelbart och visas inte i Offline Clients.

    ![auto removal](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/auto_removal.png){class="glboxshadow"}

## Remove Clients {#remove-clients}

Klicka på **Delete All** uppe till höger i avsnittet för offlineklienter för att radera alla.

Ta bort en viss klient genom att klicka på ikonen med tre punkter i kolumnen Action och välja **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
