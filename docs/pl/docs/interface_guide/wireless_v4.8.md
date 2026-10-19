# Wireless (firmware v4.8 i wcześniejsze)

Treść tej strony dotyczy wersji firmware v4.8.x i wcześniejszych. Jeśli urządzenie używa innej wersji firmware, użyj poniższego selektora, aby przejść do odpowiedniego przewodnika.

<div class="gl-link-select" data-label="Wersja firmware" data-placeholder="Firmware v4.8 i wcześniejsze" markdown="1">

- [Firmware v4.9 i nowsze](wireless.md)

</div>

---


Po lewej stronie webowego panelu administracyjnego przejdź do **WIRELESS**.

Ta strona umożliwia konfigurację oddzielnych sieci Wi‑Fi, w tym 2.4 GHz, 5 GHz, 6 GHz oraz MLO Wi‑Fi (dostępność zależy od modelu). Każde pasmo można skonfigurować jako główną sieć Wi‑Fi lub sieć gościnną, co zapewnia elastyczne zarządzanie połączeniami bezprzewodowymi.

**Uwaga**: Niektóre modele nie obsługują Wi‑Fi 5 GHz, na przykład GL-MT300N-V2 (Mango), GL-X300B (Collie) i GL-XE300 (Puli); niektóre nie mają funkcji Wi‑Fi w ogóle, na przykład GL-MT5000 (Brume 3) i GL-MT2500/GL-MT2500A (Brume 2).

## MLO Wi-Fi

| Obsługiwane modele          |   |
| :-------------------------- |:-:|
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)    | √ |
| Beryl 7 (GL-MT3600BE)       | √ |
| Flint 3e (GL-BE6500)        | √ |
| Flint 3 (GL-BE9300)         | √ |
| Slate 7 (GL-BE3600)         | √ |

MLO (Multi-Link Operation) to jedna z kluczowych funkcji Wi‑Fi 7 (802.11be), zaprojektowana w celu poprawy wydajności sieci, znacznego zmniejszenia opóźnień oraz zwiększenia stabilności połączenia poprzez jednoczesne wykorzystanie wielu pasm częstotliwości, takich jak 2.4 GHz, 5 GHz i 6 GHz.

Kliknij poniższe karty, aby dowiedzieć się więcej o ustawieniach głównej sieci MLO Wi‑Fi i gościnnej sieci MLO Wi‑Fi.

=== "MLO Wi-Fi"

    Główna sieć MLO Wi‑Fi umożliwia konfigurację wielu ustawień, w tym włączania i wyłączania Wi‑Fi, wyboru pasm radiowych (co najmniej dwóch), włączania i wyłączania **Randomized BSSID**, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła Wi‑Fi oraz widoczności SSID.

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - Jeśli pasma radiowe MLO Wi‑Fi obejmują 6 GHz, BSSID sieci MLO Wi‑Fi zostanie zsynchronizowany po zmianie BSSID sieci 6 GHz Wi‑Fi.

    - Domyślnym zabezpieczeniem dla MLO Wi‑Fi jest WPA3-SAE, odpowiednie dla większości urządzeń obsługujących MLO.

=== "Gościnne MLO Wi-Fi"

    Gościnna sieć MLO Wi‑Fi umożliwia konfigurację uproszczonych ustawień, w tym włączania i wyłączania Wi‑Fi, wyboru pasm radiowych (co najmniej dwóch), ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła oraz widoczności SSID.

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## 6 GHz Wi-Fi

| Obsługiwane modele       |   |
| :----------------------- |:-:|
| Slate 7 Pro (GL-BE10000) | √ |
| Mudi 7 (GL-E5800)        | √ |
| Flint 3 (GL-BE9300)      | √ |

Sieć 6 GHz Wi‑Fi zapewnia szybszą i bardziej stabilną łączność bezprzewodową przy mniejszym zatłoczeniu niż pasma 2.4 GHz i 5 GHz.

Kliknij poniższe karty, aby dowiedzieć się więcej o ustawieniach głównej sieci 6 GHz Wi‑Fi i gościnnej sieci 6 GHz Wi‑Fi.

=== "6 GHz Wi-Fi"

    Główna sieć 6 GHz Wi‑Fi umożliwia konfigurację wielu ustawień, w tym włączania i wyłączania Wi‑Fi, ustawiania mocy TX, włączania i wyłączania **Randomized BSSID**, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła Wi‑Fi, widoczności SSID, trybu Wi‑Fi, szerokości pasma oraz kanału.

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - **Enable PSC**: gdy PSC (Preferred Scanning Channel) jest włączone, zarezerwowane zostaną tylko kanały o lepszej łączności, aby zapewnić połączenia urządzeń 6 GHz.

=== "Gościnne 6 GHz Wi-Fi"

    Gościnna sieć 6 GHz Wi‑Fi umożliwia konfigurację uproszczonych ustawień, w tym włączania i wyłączania Wi‑Fi, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła oraz widoczności SSID.

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## 5 GHz Wi-Fi

Kliknij poniższe karty, aby dowiedzieć się więcej o ustawieniach głównej sieci 5 GHz Wi‑Fi i gościnnej sieci 5 GHz Wi‑Fi.

=== "5 GHz Wi-Fi"

    Główna sieć 5 GHz Wi‑Fi umożliwia konfigurację wielu ustawień, w tym włączania i wyłączania Wi‑Fi, ustawiania mocy TX, włączania i wyłączania **Randomized BSSID**, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła Wi‑Fi, widoczności SSID, trybu Wi‑Fi, szerokości pasma oraz kanału.

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "Gościnne 5 GHz Wi-Fi"

    Gościnna sieć 5 GHz Wi‑Fi umożliwia konfigurację uproszczonych ustawień, w tym włączania i wyłączania Wi‑Fi, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła oraz widoczności SSID.

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## 2.4 GHz Wi-Fi

Kliknij poniższe karty, aby dowiedzieć się więcej o ustawieniach głównej sieci 2.4 GHz Wi‑Fi i gościnnej sieci 2.4 GHz Wi‑Fi.

=== "2.4 GHz Wi-Fi"

    Główna sieć 2.4 GHz Wi‑Fi umożliwia konfigurację wielu ustawień, w tym włączania i wyłączania Wi‑Fi, ustawiania mocy TX, włączania i wyłączania **Randomized BSSID**, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła Wi‑Fi, widoczności SSID, trybu Wi‑Fi, szerokości pasma oraz kanału.

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "Gościnne 2.4 GHz Wi-Fi"

    Gościnna sieć 2.4 GHz Wi‑Fi umożliwia konfigurację uproszczonych ustawień, w tym włączania i wyłączania Wi‑Fi, ustawiania nazwy Wi‑Fi (SSID), zabezpieczeń Wi‑Fi, hasła oraz widoczności SSID.

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Ogólne ustawienia Wi-Fi

* Najedź kursorem na ikonę kodu QR obok SSID sieci Wi‑Fi, aby wyświetlić jej kod QR Wi‑Fi. Możesz zeskanować go telefonem lub tabletem, aby szybko połączyć się z odpowiednią siecią Wi‑Fi.

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: funkcja domyślnie włączona, która zapobiega śledzeniu routera przez stały BSSID. Szczegóły znajdziesz w sekcji [Randomized BSSID](#randomized-bssid).

* **Bandwidth** i **Channel** nie mogą być modyfikowane, gdy router działa w [trybie repeatera](internet_repeater.md), ponieważ są zgodne z ustawieniami powielanej sieci.

* Gdy **Channel** jest ustawiony na **Auto**, router nie będzie automatycznie przełączać Wi‑Fi na kanał DFS.

* Przy zmianie **Channel** z kanału nie-DFS na kanał DFS pojawi się następujące ostrzeżenie.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* Gdy **Bandwidth** jest ustawiona na **160 MHz** (dostępne tylko w niektórych modelach), Wi‑Fi będzie zawsze korzystać z kanału DFS, nawet jeśli dla ustawienia Channel wybierzesz kanał nie-DFS lub Auto.

## Losowy BSSID {#randomized-bssid}

Randomized BSSID to funkcja ochrony prywatności dostępna od firmware v4.6 i domyślnie włączona. Zapobiega lokalizowaniu i śledzeniu routera za pomocą stałego BSSID sieci Wi-Fi (adresu MAC interfejsu bezprzewodowego routera).

**Dlaczego stały BSSID zagraża prywatności**

Mobilne systemy operacyjne, takie jak Android i iOS, wykorzystują pozycjonowanie Wi-Fi oparte na danych zbieranych od użytkowników do świadczenia usług lokalizacyjnych:

1. Urządzenia klienckie, takie jak telefony i laptopy, okresowo przesyłają wykryte identyfikatory BSSID wraz z własną lokalizacją GPS na serwer dostawcy systemu operacyjnego lub producenta urządzenia.

2. Dostawcy łączą te dane w globalnej bazie przypisującej identyfikatory BSSID do lokalizacji.

3. Dowolne urządzenie z włączonym Wi-Fi, nawet bez GPS, może wysłać zapytanie do tej bazy, aby oszacować swoją lokalizację na podstawie pobliskich identyfikatorów BSSID.

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

W rezultacie router ze stałym BSSID działa jak stały znacznik lokalizacji: można go zdalnie zlokalizować i śledzić jego przemieszczanie się, na przykład podczas podróży. Atakujący mogą też odpytywać takie bazy, aby lokalizować routery lub identyfikować ich cechy na podstawie informacji o producencie zawartych w BSSID (OUI).

**Jak Randomized BSSID Cię chroni**

Gdy funkcja jest włączona, router generuje losowy BSSID i odnawia go przy każdym uruchomieniu. Ponieważ BSSID stale się zmienia, nie można go już powiązać ze stałą lokalizacją w bazach dostawców. Przerywa to powiązanie między BSSID a lokalizacją wykorzystywane do śledzenia.

| Stan | Działanie |
| ----------------- | ---------------------- |
| Włączona (domyślnie) | Przy każdym uruchomieniu generowany jest nowy losowy BSSID |
| Wyłączona | Router używa swojego rzeczywistego fabrycznego adresu MAC jako BSSID |

**Uwagi**:

1. BSSID zmienia się tylko po ponownym uruchomieniu routera; podczas jego pracy pozostaje taki sam.
2. BSSID gościnnej sieci Wi-Fi pozostaje zgodny z BSSID głównej sieci Wi-Fi w tym samym paśmie częstotliwości.
3. Jeśli pasma radiowe MLO Wi-Fi obejmują 6 GHz, BSSID MLO Wi-Fi synchronizuje się z BSSID sieci Wi-Fi 6 GHz.
4. Randomized BSSID blokuje śledzenie przez BSSID routera, ale nie powstrzymuje urządzeń klienckich przed zgłaszaniem własnej lokalizacji i nie zapewnia pełnej ochrony prywatności: nadal można obserwować SSID, kanał i charakterystykę sygnału.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"}.
