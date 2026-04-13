# Klienci

Po lewej stronie panelu administracyjnego WWW przejdź do **CLIENTS**.

Strona **Clients** wyświetla informacje o podłączonych urządzeniach. Od lewej do prawej zobaczysz nazwę urządzenia, typ połączenia, adres IP, adres MAC, prędkość i ruch.

## Nazwa urządzenia

Pierwsza kolumna wyświetla nazwę i typ urządzenia, określane na podstawie nazwy hosta ustawionej przez użytkownika urządzenia.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Aby zmienić nazwę i typ urządzenia, kliknij ikonę trzech kropek w kolumnie Action, a następnie w menu rozwijanym kliknij **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Typ połączenia

Niebieska ikona po prawej stronie nazwy urządzenia oznacza typ/metodę połączenia urządzenia.

Wskazuje, w jaki sposób urządzenie jest podłączone do sieci — przez Wi-Fi albo kabel Ethernet.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## Adres IP i MAC

Druga kolumna zawiera adresy IP i MAC podłączonego urządzenia.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Wiele urządzeń używa losowych adresów MAC. Jeśli podłączone urządzenia korzystają z losowych adresów MAC, pojawi się poniższy komunikat.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Uwaga**: Zasada wykrywania jest następująca: jeśli drugi znak adresu MAC to 2, 6, A lub E (bez rozróżniania wielkości liter), jest on uznawany za losowy adres MAC. Jednak niektóre urządzenia mogą używać innej reguły generowania losowego adresu MAC, więc ta metoda wykrywania może nie być dokładna.

## Prędkość

Trzecia kolumna wyświetla prędkość internetową podłączonego urządzenia.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

Prędkość w tym miejscu jest średnią z 3 minut.

- Jeśli ta strona jest otwarta przez 10 sekund, wyświetlana jest średnia prędkość z ostatnich 10 sekund.
- Jeśli ta strona jest otwarta przez 30 sekund, wyświetlana jest średnia prędkość z ostatnich 30 sekund.
- Jeśli ta strona jest otwarta przez 60 sekund, wyświetlana jest średnia prędkość z ostatnich 60 sekund.
- Jeśli ta strona jest otwarta przez 3 minuty, wyświetlana jest średnia prędkość z ostatnich 3 minut.
- Jeśli ta strona jest otwarta przez 10 minut, wyświetlana jest średnia prędkość z ostatnich 3 minut.

## Ruch

Czwarta kolumna wyświetla ruch internetowy podłączonego urządzenia.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## Rezerwacja adresu IP

W piątej kolumnie możesz jednym kliknięciem zarezerwować adres IP dla wybranego podłączonego urządzenia. 

Ta funkcja jest dostępna od wersji v4.8.

Gdy przypiszesz klientowi w sieci LAN zarezerwowany adres IP, klient będzie zawsze otrzymywać ten sam adres IP przy każdym połączeniu z serwerem DHCP routera. 

Możesz przypisać zarezerwowane adresy IP komputerom lub serwerom, które wymagają stałych ustawień IP.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Lista blokowanych urządzeń {#blocklist}

W szóstej kolumnie możesz jednym kliknięciem zablokować określone podłączone urządzenia. 

Domyślną regułą kontroli dostępu jest Blocklist, a w razie potrzeby można przełączyć ją u góry na Allowlist.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Urządzenia, których adresy MAC znajdują się na liście blokowanych, nie mogą łączyć się z tym routerem.

- **Allowlist**: Łączyć się mogą tylko urządzenia z określonymi adresami MAC; rozwiązanie to nadaje się do urządzeń IoT i zarządzania siecią firmową.

Aby utworzyć Blocklist, możesz przesłać listę blokowanych urządzeń w pliku Excel w **(1)** albo ręcznie wprowadzić adresy MAC w **(2)**.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Metoda 1. Importowanie klientów**

Na stronie Access Control kliknij **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Kliknij **Download Import Template**, a pobierzesz plik o nazwie "mac-template.csv".

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Otwórz plik, wpisz adresy MAC i zapisz go.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Wybierz zapisany plik lub przeciągnij go do obszaru przesyłania.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Po pomyślnym przesłaniu kliknij **Import**, aby zakończyć zbiorczy import adresów MAC.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Metoda 2. Wprowadzanie ręczne**

Na stronie Access Control ręcznie wprowadź adresy MAC urządzeń, które chcesz zablokować, a następnie kliknij **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Uwaga**: Blokowanie klienta opiera się na adresie MAC urządzenia. Jeśli zablokowane urządzenie następnym razem użyje innego adresu MAC, nadal będzie mogło połączyć się z routerem.

## Sortowanie

Aktualny typ sortowania jest wyświetlany w prawym górnym rogu i możesz przełączyć się na inne typy sortowania.

Domyślny typ sortowania działa następująco:

- Urządzenie, z którego aktualnie korzystasz, jest zawsze na górze.
- W sekcji klientów online im później urządzenie się połączyło, tym wyżej pojawia się na liście.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Akcje

### Szczegóły klienta

Jeśli chcesz wyświetlić szczegóły urządzenia klienckiego, kliknij ikonę trzech kropek w skrajnej prawej kolumnie Action, a następnie w menu rozwijanym kliknij **View Details**.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Na otwartej podstronie zobaczysz wszystkie informacje o urządzeniu klienckim, w tym wszystkie jego adresy IPv6, jeśli są dostępne.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modyfikacja

Kliknij ikonę trzech kropek w kolumnie Action, a następnie w menu rozwijanym kliknij **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Ograniczenie prędkości

Kliknij ikonę trzech kropek w kolumnie Action, a następnie w menu rozwijanym kliknij **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Jeśli dla klienta zastosowano ograniczenie prędkości, strzałki wysyłania i pobierania przy prędkości zmienią kolor na żółty.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

Aby wyłączyć limit prędkości, kliknij ikonę trzech kropek w kolumnie Action.

### Użyj tunelu VPN

**Uwaga**: Ta opcja jest dostępna od firmware v4.8 i pojawi się w menu Action tylko wtedy, gdy skonfigurowano regułę opartą na adresach MAC.

Dodaj klienta do listy tuneli VPN za pomocą reguły opartej na adresach MAC. Jeśli potrzebujesz szczegółowo dostosować tunele, przejdź do VPN Dashboard, aby nimi zarządzać.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Usuwanie klientów offline

W sekcji klientów offline możesz kliknąć **Delete All** w prawym górnym rogu, aby usunąć wszystkich klientów offline. 

Jeśli chcesz usunąć konkretnego klienta, kliknij ikonę trzech kropek w kolumnie Action, a następnie w menu rozwijanym kliknij **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
