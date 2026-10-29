# Mesh {#mesh}

**Uwaga**: ta funkcja została wprowadzona w oprogramowaniu sprzętowym v4.10.

Mango 2 (GL-MG1300) i Mudi 7 (GL-E5800) nie obsługują Mesh nawet z firmware v4.10 lub nowszym. Szczegółowe informacje znajdują się w sekcji [Obsługiwane modele](#supported-models).

---

W panelu administracyjnym po lewej stronie przejdź do **MESH**.

Mesh to funkcja oparta na standardzie Wi-Fi EasyMesh™, która rozszerza zasięg Wi‑Fi w całym domu i umożliwia płynny roaming. Jeśli masz kilka routerów GL.iNet, ustaw jeden jako router główny, a pozostałe jako węzły Mesh.
Nie wiesz, który tryb wybrać? Zobacz [Porównanie trybów Mesh, Extender i Access Point](#mesh-vs-extender-vs-access-point-mode).


## Obsługiwane modele {#supported-models}

??? "Obsługiwane modele"
    - ※GL-BE14000 (Flint 4)
    - ※GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - ※GL-XE3000 (Puli AX)
    - ※GL-X3000 (Spitz AX)
    - GL-MT3000 (Beryl AX)

    **Uwaga**: modele oznaczone symbolem ※ obsługują Mesh w firmware w wersji Beta.

??? "Nieobsługiwane modele"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Szybka konfiguracja {#quick-setup}

Poniższy przykład wykorzystuje Flint 3 (GL‑BE9300) i Slate 7 (GL‑BE3600) do utworzenia sieci Mesh.

**Flint 3** jest routerem głównym, który łączy się z Internetem i zarządza wszystkimi węzłami Mesh.

**Slate 7** jest węzłem Mesh rozszerzającym zasięg Wi-Fi routera głównego.

1. Włącz węzeł Mesh i umieść go w pobliżu routera głównego.

    Podczas pierwszej konfiguracji ustaw węzeł obok routera głównego, aby przyspieszyć skanowanie. Po konfiguracji możesz przenieść go w połowę odległości między routerem a obszarem bez zasięgu Wi-Fi.

2. Zaloguj się do panelu administracyjnego węzła Mesh, przejdź do **MESH** i kliknij **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Węzeł stanie się wykrywalny. Do czasu dodania do sieci Mesh nie będzie miał połączenia sieciowego.

3. Zaloguj się do panelu routera głównego i przejdź do **INTERNET**. Połącz go z Internetem przez Ethernet, Repeater, Tethering lub Cellular.

4. Po skonfigurowaniu Internetu przejdź do **MESH** i kliknij **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. Strona przedstawia dwie metody dodawania węzłów: Wi-Fi Scan i Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Wybierz odpowiednią instrukcję.

    ??? note "Wi-Fi Scan"

        Kliknij **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Router rozpocznie wyszukiwanie pobliskich węzłów Mesh przez Wi-Fi. Wybierz urządzenia i kliknij **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Węzeł zostanie dodany do sieci Mesh. Kliknij **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Połącz port WAN węzła Mesh z portem LAN routera głównego kablem Ethernet. Sieć Ethernet Backhaul zostanie skonfigurowana automatycznie.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Po dodaniu węzła topologia pojawi się w panelu routera głównego.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Zarządzanie węzłami {#manage-nodes}

Po zakończeniu konfiguracji węzeł Mesh nie będzie dostępny pod pierwotnym adresem IP. Routerem głównym i wszystkimi węzłami można zarządzać z panelu routera głównego.

### Wyświetlanie szczegółów węzła {#view-node-details}

W panelu routera głównego przejdź do **MESH** i kliknij **Main Router** w topologii.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Można sprawdzić model, adresy IP i MAC, czas działania oraz podłączone urządzenia.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Kliknij **Mesh Node** w topologii.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Można sprawdzić model, adresy IP i MAC, wersję oprogramowania, czas działania i podłączone urządzenia węzła.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Edytowanie węzła Mesh {#edit-mesh-node}

W panelu routera głównego przejdź do **MESH** i kliknij **Mesh Node** w topologii.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Domyślna nazwa każdego węzła to „Node” i cztery ostatnie cyfry adresu MAC. Kliknij ikonę edycji, aby zmienić nazwę.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Dostęp do węzła Mesh {#access-mesh-node}

W panelu routera głównego przejdź do **MESH** i kliknij **Mesh Node** w topologii.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Nastąpi przekierowanie do strony logowania węzła pod adresem IP przydzielonym przez router główny.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Dodawanie kolejnych węzłów {#add-more-nodes}

W razie potrzeby kliknij **Add** w prawym górnym rogu topologii.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

## Porównanie trybów Mesh, Extender i Access Point {#mesh-vs-extender-vs-access-point-mode}

Wszystkie trzy tryby mogą rozszerzać zasięg Wi-Fi. Główne różnice dotyczą sposobu połączenia z routerem głównym oraz konfiguracji urządzeń i zarządzania nimi. **Backhaul** to połączenie między routerem głównym a wzmacniaczem sygnału, punktem dostępowym lub węzłem Mesh.

Tabela porównuje samodzielne tryby Extender i Access Point firmy GL.iNet z jej implementacją Mesh.

| Funkcja | Tryb Extender | Tryb Access Point | Tryb Mesh |
|---|---|---|---|
| **Bezprzewodowy backhaul** | ✅ Obsługiwany | ❌ Nie dotyczy | ✅ Obsługiwany |
| **Backhaul Ethernet** | ❌ Nieużywany w tym trybie | ✅ Obsługiwany | ✅ Obsługiwany |
| **Backhaul pełnodupleksowy** | ❌ Wi-Fi działa w półdupleksie | ✅ Ethernet | ✅ Tylko Ethernet; bezprzewodowy backhaul pozostaje półdupleksowy |
| **Bezprzewodowy backhaul 2.4/5 GHz** | ⚠️ Dostępne pasma zależą od modelu i firmware | ❌ Nie dotyczy | ⚠️ Dostępne pasma zależą od modelu i firmware |
| **Bezprzewodowy backhaul 6 GHz** | ⚠️ Zależy od modelu i firmware | ❌ Nie dotyczy | 🔜 Wkrótce |
| **Roaming Wi-Fi** | ✅ Sterowany przez klienta | ✅ Sterowany przez klienta | ✅ Sterowany przez klienta, ze wsparciem 802.11k/v |
| **Automatyczna synchronizacja ustawień Wi-Fi** | ❌ Konfiguracja osobna | ❌ Konfiguracja osobna | ✅ Z routera głównego |
| **Centralne zarządzanie węzłami** | ❌ Konfiguracja osobna | ❌ Konfiguracja osobna | ✅ Przez router główny |
| **Topologia sieci i przegląd klientów** | ❌ Brak przeglądu całej sieci Mesh | ❌ Brak przeglądu całej sieci Mesh | ✅ Dostępne na routerze głównym |
| **Centralnie zarządzana rozbudowa** | ❌ Niezależne wzmacniacze sygnału | ❌ Niezależne punkty dostępowe | ✅ Jeden router główny i maksymalnie osiem węzłów |
| **Centralnie zarządzane przeskoki bezprzewodowe** | ❌ Brak zarządzania przez Mesh | ❌ Nie dotyczy | ✅ Maksymalnie trzy przeskoki bezprzewodowe |
| **Automatyczne przełączanie między backhaulem przewodowym i bezprzewodowym** | ❌ Brak przełączania zarządzanego przez Mesh | ❌ Brak przełączania zarządzanego przez Mesh | ✅ Priorytet dla Ethernet |
| **Najlepsze zastosowanie** | Proste rozszerzenie zasięgu bezprzewodowego | Rozszerzenie zasięgu tam, gdzie dostępny jest Ethernet | Skoordynowany zasięg przy połączeniach przewodowych, bezprzewodowych lub mieszanych |

✅ Obsługiwane · ❌ Nieobsługiwane lub nie dotyczy w tym trybie · ⚠️ Zależy od sprzętu, firmware lub konfiguracji · 🔜 Planowana funkcja

Mesh synchronizuje obsługiwane ustawienia Wi-Fi sieci głównej, gościnnej, IoT i MLO. Zapewnia również centralne zarządzanie węzłami, w tym ponowne uruchamianie, usuwanie i aktualizowanie obsługiwanych węzłów GL.iNet. Węzły można dodawać przez skanowanie Wi-Fi, połączenie Ethernet lub przycisk Mesh/WPS, jeśli jest obsługiwany. Zarządzanie backhaulem obejmuje priorytet dla Ethernet, przełączanie między połączeniami przewodowymi i bezprzewodowymi oraz zapobieganie pętlom.

### Różnice w wydajności {#understanding-performance-differences}

#### Tryb Extender {#extender-mode}

Urządzenie łączy się z istniejącą siecią Wi-Fi. Moduł radiowy używany do połączenia z routerem nadrzędnym pracuje na kanale routera głównego. Klienci korzystający z tego samego modułu radiowego również używają tego kanału, więc ruch do routera nadrzędnego i ruch klientów współdzielą czas transmisji.

W obsługiwanych modelach wielopasmowych osobne moduły radiowe mogą nadal obsługiwać klientów w innych pasmach. Na przykład wzmacniacz sygnału może łączyć się z routerem nadrzędnym przez 2.4 GHz, jednocześnie obsługując klientów przez osobny moduł radiowy 5 GHz. Te dwa połączenia nie rywalizują o czas transmisji na tym samym kanale. Dostępne kombinacje zależą od modelu i firmware; tryb Extender nie jest z założenia ograniczony do jednego pasma.

Ten sam wymóg dotyczący kanału połączenia nadrzędnego dotyczy funkcji połączenia Repeater firmy GL.iNet, choć działanie Repeater i samodzielny tryb sieciowy Extender różnią się pod innymi względami.

#### Bezprzewodowy Mesh {#wireless-mesh}

W testowanej trzypasmowej konfiguracji Mesh węzeł używa **pasma 5 GHz do bezprzewodowego backhaulu**. Kanał 5 GHz węzła jest zgodny z kanałem routera głównego i nie można go zmienić niezależnie, natomiast **ustawienia osobnych kanałów 2.4 GHz i 6 GHz pozostają konfigurowalne niezależnie**. Dotyczy to ustawień kanałów, a nie tego, z którymi pasmami mogą łączyć się urządzenia klienckie. Zmiana kanału dla klientów nie zmienia pasma backhaulu.

Wpływ na wydajność zależy więc od sposobu połączenia klienta:

- **Urządzenia połączone przez 5 GHz:** jeśli telefon, laptop lub inne urządzenie łączy się z Wi-Fi 5 GHz węzła Mesh, a ten sam moduł radiowy obsługuje bezprzewodowy backhaul, połączenia współdzielą czas transmisji. Zablokowanie kanału 5 GHz węzła nie musi uniemożliwiać klientom połączenia w tym paśmie.
- **Urządzenia połączone przez 2.4 GHz lub 6 GHz:** gdy klienci korzystają z modułu radiowego innego niż bezprzewodowy backhaul 5 GHz, oba łącza nie ponoszą kosztu przekazywania ruchu na tym samym kanale.

Opis dotyczy testowanej konfiguracji, a nie wszystkich obsługiwanych modeli Mesh. Przekazywanie ruchu przez osobne moduły radiowe nie jest wyłączną cechą Mesh, a przejście z Extender na Mesh nie zapewnia automatycznej poprawy przepustowości.

#### Tryb Access Point i przewodowy Mesh {#access-point-mode-and-wired-mesh}

Oba rozwiązania używają Ethernet do połączenia z routerem głównym. Backhaul Ethernet działa w pełnym dupleksie i pozwala uniknąć przesyłania ruchu backhaulu przez Wi-Fi. Połączenia Wi-Fi klientów pozostają półdupleksowe. Przy porównywalnym sprzęcie i warunkach tryb Access Point oraz przewodowy Mesh mogą zapewniać podobną przepustowość; Mesh dodaje skoordynowaną konfigurację i zarządzanie.

Mesh nadaje priorytet backhaulowi Ethernet i obsługuje przełączenie na połączenie bezprzewodowe, gdy dostępne jest odpowiednie łącze. W testowanej konfiguracji kanał 5 GHz węzła pozostaje zgodny z kanałem routera głównego nawet przy aktywnym backhaulu Ethernet. Nie oznacza to, że ruch jest przesyłany przez bezprzewodowy backhaul. Ethernet usuwa bezprzewodowy przeskok backhaulu danych, ale pobliskie węzły i klienci korzystający z tego samego kanału Wi-Fi nadal mogą rywalizować o czas transmisji.

!!! note "Backhaul Mesh 6 GHz — Wkrótce"

    Backhaul Mesh 6 GHz będzie wymagał zgodnego sprzętu 6 GHz zarówno w routerze głównym, jak i węźle Mesh, a także obsługującego go firmware. Nie zakładaj, że wszystkie modele obsługujące Mesh będą obsługiwać tę funkcję.

    To coś innego niż połączenie klienta z istniejącą siecią Wi-Fi 6 GHz węzła. Przy backhaulu 6 GHz osobny moduł radiowy 5 GHz mógłby obsługiwać klientów bez współdzielenia czasu transmisji kanału backhaulu. Moduł radiowy jest dedykowany backhaulowi tylko wtedy, gdy jest zarezerwowany do tego celu i nie obsługuje jednocześnie klientów.

!!! important "Osobne moduły radiowe nie zmieniają Wi-Fi w pełnodupleksowe"

    Każde łącze Wi-Fi pozostaje półdupleksowe. Przekazywanie ruchu przez osobne moduły radiowe pozwala uniknąć współdzielenia jednego kanału przez łącza backhaulu i klientów, ale nie usuwa innych zakłóceń, rywalizacji o medium ani ograniczeń wielu przeskoków. Przepustowość całego połączenia nadal ograniczają wolniejsze łącze i warunki sieciowe.

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
