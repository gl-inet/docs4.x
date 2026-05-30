# Sieć bezprzewodowa (Firmware v4.9)

> Uwaga: Ten przewodnik dotyczy firmware v4.9 i nowszego. W przypadku wcześniejszych wersji zobacz [tutaj](wireless.md).

Zaloguj się do webowego panelu administracyjnego i przejdź do **WIRELESS**.

Strona Wireless umożliwia konfigurację różnych sieci Wi‑Fi, w tym MLO Wi‑Fi (dostępne w wybranych modelach), sieci głównej, sieci gościnnej i sieci IoT. Obsługiwane pasma Wi‑Fi różnią się w zależności od modelu.

## Multi-Link Operation (MLO)

??? "Obsługiwane modele"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Nieobsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation) to jedna z kluczowych funkcji Wi‑Fi 7 (802.11be), zaprojektowana w celu poprawy wydajności sieci, znacznego zmniejszenia opóźnień i zwiększenia stabilności połączenia poprzez jednoczesne wykorzystanie wielu pasm częstotliwości, takich jak 2.4 GHz, 5 GHz i 6 GHz.

Klientom Wi‑Fi 7 zaleca się łączenie z MLO Wi‑Fi, co znacząco poprawia przepustowość i niezawodność sieci dzięki połączeniom wielopasmowym.

Kliknij **Add**, aby skonfigurować sieć MLO Wi‑Fi, a następnie kliknij **Apply**. Pamiętaj, że dostępne pasma Wi‑Fi różnią się w zależności od modelu.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo2.png){class="glboxshadow"}

- **Wi-Fi Band**: Wybierz co najmniej dwa pasma radiowe.
- **Wi-Fi Security**: Jeśli wybrane jest pasmo 6 GHz, jedyną dostępną i zalecaną opcją jest WPA3-SAE. Działa najlepiej z większością urządzeń obsługujących MLO.
- **Enable Randomized BSSID**: Jeśli wybrane jest pasmo 6 GHz, identyfikator BSSID 6 GHz dla MLO Wi‑Fi zostanie zsynchronizowany z główną siecią Wi‑Fi.

Po włączeniu strona będzie wyglądać następująco.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo3.png){class="glboxshadow"}

## Sieć główna

Sieć główna to podstawowa sieć Wi‑Fi, która domyślnie obsługuje jednoczesne nadawanie w różnych pasmach radiowych. Dla każdego pasma możesz skonfigurować osobne ustawienia, takie jak SSID Wi‑Fi, tryb zabezpieczeń, hasło, Randomized BSSID, moc TX, szerokość pasma i kanał.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main.png){class="glboxshadow"}

Kliknij ikonę koła zębatego po prawej stronie, aby wyświetlić lub zmodyfikować ustawienia Wi‑Fi dla każdego pasma. Pamiętaj, że dostępne pasma Wi‑Fi różnią się w zależności od modelu.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_2.4g.png){class="glboxshadow"}

## Sieć gościnna

Sieć gościnna to dedykowana sieć Wi‑Fi dla odwiedzających, z wszystkimi pasmami domyślnie wyłączonymi. Dla każdego pasma możesz ją włączyć i skonfigurować podstawowe ustawienia sieci, takie jak SSID Wi‑Fi, tryb zabezpieczeń, hasło oraz Randomized BSSID.

Kliknij **Add**, aby skonfigurować sieć Guest Wi‑Fi, a następnie kliknij **Apply**. Pamiętaj, że dostępne pasma Wi‑Fi różnią się w zależności od modelu.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest2.png){class="glboxshadow"}

Po włączeniu strona będzie wyglądać następująco.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest3.png){class="glboxshadow"}

## Sieć IoT

Sieć IoT to dedykowana sieć Wi‑Fi dla urządzeń inteligentnych, z wszystkimi pasmami domyślnie wyłączonymi. Dla każdego pasma możesz ją włączyć i skonfigurować podstawowe ustawienia sieci, takie jak SSID Wi‑Fi, tryb zabezpieczeń, hasło oraz Randomized BSSID.

Kliknij **Add**, aby skonfigurować sieć IoT Wi‑Fi, a następnie kliknij **Apply**. Pamiętaj, że ta sieć nie obejmuje pasma 6 GHz, a dostępne pasma Wi‑Fi różnią się w zależności od modelu.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot2.png){class="glboxshadow"}

Po włączeniu strona będzie wyglądać następująco.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot3.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"}.
