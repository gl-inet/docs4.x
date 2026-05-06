# ZeroTier

ZeroTier to programowa wirtualna sieć prywatna (VPN), która umożliwia bezpieczną, szyfrowaną komunikację między urządzeniami przez internet. Tworzy prywatną, wirtualną sieć, dzięki której urządzenia mogą komunikować się tak, jakby znajdowały się w tej samej sieci lokalnej, niezależnie od swojej fizycznej lokalizacji czy topologii sieci. ZeroTier zaprojektowano tak, aby był łatwy w konfiguracji i użyciu, a ponadto oferuje takie funkcje jak szyfrowanie end-to-end, segmentacja sieci i mostkowanie sieci.

Funkcja ZeroTier na routerach GL.iNet, dostępna od firmware v4.2, pozwala routerowi dołączyć do wirtualnej sieci ZeroTier. Po połączeniu możesz uzyskać zdalny dostęp do routera, w tym do zasobów po stronie WAN i LAN.

**Uwaga**:

1. Nie zaleca się jednoczesnego używania ZeroTier z żadną z poniższych funkcji lub usług, ponieważ może to powodować konflikty routingu: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale, AstroWarp.

2. Ta funkcja jest obecnie w fazie beta i może zawierać błędy.

3. Niektóre modele, mimo że działają na oprogramowaniu v4.2 lub nowszym, nie obsługują ZeroTier z powodu niewystarczającej ilości pamięci.

## Obsługiwane modele

??? "Obsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Nieobsługiwane modele"
    - GL-X2000 (Spitz Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Konfiguracja sieci ZeroTier

Dostępne są dwie wersje ZeroTier Central: New Central i Legacy Central.

- **New Central**: Nowsza wersja ZeroTier Central z lepszą użytecznością i nowymi funkcjami. Jest zalecana nowym użytkownikom, aby zapewnić najlepsze doświadczenie i dostęp do najnowszych narzędzi.

- **Legacy Central**: Dla kont utworzonych przed listopadem 2025 r. Legacy Central nadal obsługuje obecnych użytkowników zarządzających swoimi sieciami.

Obie wersje mogą być używane równolegle, ale obecnie nie ma bezpośredniej ścieżki migracji.

Wybierz odpowiednią wersję, aby kontynuować.

### New Central

Poniżej pokazano przykład z użyciem modelu GL-MT3600BE.

1. Wejdź na [oficjalną stronę ZeroTier](https://www.zerotier.com/){target="_blank"} i zaloguj się na swoje konto.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Utwórz organizację.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Wybierz plan. W tym przykładzie wybieramy plan Personal, który obejmuje 10 urządzeń, 1 administratora sieci i 1 sieć. Jeśli potrzebujesz utworzyć więcej sieci, dodać więcej urządzeń albo skonfigurować trasy niestandardowe i DNS, wybierz plan Essential lub Scale.

    ![select plan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Twoja sieć ZeroTier została już utworzona. Zwróć uwagę na **Network ID** — 16-znakowy ciąg alfanumeryczny w prawym górnym rogu. Będzie potrzebny podczas podłączania innych urządzeń.

    ![network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Włącz ZeroTier na routerze GL.iNet.

    Zaloguj się do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **ZeroTier**.

    Włącz ZeroTier, wpisz **Network ID** na tej samej stronie i kliknij **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    Po krótkiej chwili interfejs wskaże, że wymagane jest uwierzytelnienie. Kliknij hiperłącze **ZeroTier Central**, aby przejść do ZeroTier Central.

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Autoryzuj urządzenie w ZeroTier Central.

    W ZeroTier Central znajdź urządzenie ze statusem Pending i autoryzuj je.

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Po autoryzacji strona będzie wyglądać następująco.

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Dodaj inne urządzenie (na przykład komputer lub smartfon) do tej samej sieci ZeroTier, korzystając z [tego przewodnika](https://docs.zerotier.com/platforms/){target="_blank"}.

    Poniżej znajduje się przykład z laptopem z Windows 10 Pro.
    
    1. Zainstaluj ZeroTier na laptopie, pobierając go [stąd](https://www.zerotier.com/download/){target="_blank"}.

    2. Uruchom ZeroTier. Ikona ZeroTier pojawi się w zasobniku systemowym w prawym dolnym rogu pulpitu.
        
    3. Kliknij ikonę prawym przyciskiem myszy, wybierz **Join New Network** i w wyskakującym oknie wpisz **Network ID** uzyskany w kroku 4.
        
        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Następnie przejdź do ZeroTier Central, znajdź urządzenie ze statusem Pending i je autoryzuj.

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Po autoryzacji strona będzie wyglądać następująco. Zobaczysz szczegóły urządzeń członkowskich, takie jak **Device ID**, **Name**, **Status**, **Managed IP** i **Public IP**.

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Wskazówka**: możesz kliknąć ikonę z trzema kropkami po prawej stronie, aby edytować ustawienia urządzenia członkowskiego, w tym nazwę urządzenia, adresy Managed IP i ustawienia zaawansowane.

8. Kliknij **Managed IP** routera, aby go skopiować. Następnie możesz użyć tego adresu Managed IP, aby uzyskać dostęp do routera z laptopa znajdującego się w tej samej sieci ZeroTier.

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Przetestuj połączenie.

    Na laptopie podłączonym do tej samej sieci ZeroTier otwórz przeglądarkę internetową i wpisz adres Managed IP routera uzyskany w poprzednim kroku.

    Jeśli możesz uzyskać dostęp do webowego panelu administracyjnego routera, połączenie ZeroTier działa prawidłowo.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Możesz też wykonać `ping` na adres Managed IP routera z laptopa, aby sprawdzić łączność. Jeśli otrzymasz odpowiedź, oznacza to, że połączenie ZeroTier zostało prawidłowo zestawione.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central

Poniżej pokazano przykład z użyciem modelu GL-MT2500.

1. Utwórz pierwszą sieć ZeroTier.

    Skorzystaj z oficjalnego [Getting Started Guide](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"} ZeroTier, aby utworzyć konto i sieć ZeroTier. Pamiętaj, aby zapisać **Network ID** — 16-znakowy ciąg alfanumeryczny — ponieważ będzie potrzebny podczas podłączania innych urządzeń.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Włącz ZeroTier na routerze GL.iNet.

    Zaloguj się do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **ZeroTier**.

    Włącz ZeroTier, wpisz **Network ID** na tej samej stronie i kliknij **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    Po krótkiej chwili interfejs wskaże, że wymagane jest uwierzytelnienie.
    
    Kliknij hiperłącze **ZeroTier Central**, aby przejść do ZeroTier Central.

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

3. Autoryzuj urządzenie w ZeroTier Central.

    W ZeroTier Central przejdź do sekcji **Members**. Znajdź nowe urządzenie i zaznacz pole **Auth**, aby je autoryzować. Jeśli chcesz, możesz zmienić nazwę urządzenia.
    
    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Po krótkiej chwili ZeroTier przypisze urządzeniu **Managed IP**. Zapisz ten adres IP, ponieważ będzie potrzebny podczas testowania.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

4. Dodaj inne urządzenie (na przykład komputer lub smartfon) do tej samej sieci ZeroTier, korzystając z [tego przewodnika](https://docs.zerotier.com/platforms/){target="_blank"}.

5. Przetestuj połączenie.

    Na innym urządzeniu podłączonym do tej samej sieci ZeroTier otwórz przeglądarkę internetową i wpisz adres ZeroTier Managed IP routera uzyskany w poprzednim kroku.

    Uzyskasz dostęp do webowego panelu administracyjnego routera.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

    Możesz też użyć polecenia `ping`, aby sprawdzić łączność. Szczegóły znajdziesz w [przewodniku Quickstart](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"} ZeroTier.

## Zezwól na zdalny dostęp do WAN

Jeśli ta opcja jest włączona, zasoby po stronie WAN urządzenia mogą być dostępne przez wirtualną sieć ZeroTier.

Na przykład, jak pokazano na poniższej topologii, jeśli ta funkcja jest włączona, możesz uzyskać dostęp do `GL-AXT1800` za pomocą jego adresu IP (`192.168.29.1`) z `leo-phone`. Dzieje się tak dlatego, że GL-AXT1800 jest urządzeniem warstwy nadrzędnej względem `GL-MT2500`, a to drugie jest podłączone do tej samej sieci ZeroTier co leo-phone.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Uwaga**: Aby ta funkcja działała, trzeba dodać reguły routingu do sieci ZeroTier. W Legacy Central można bezpłatnie dodać jedną trasę niestandardową, natomiast w New Central konfiguracja tras niestandardowych jest dostępna dopiero od planu Essential wzwyż. Szczegóły znajdziesz [tutaj](https://www.zerotier.com/pricing/).

Poniższe kroki pokazano na przykładzie Legacy Central.

1. Zaloguj się do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **ZeroTier**.

    Włącz **Allow Remote Access WAN** i kliknij **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    Pojawi się komunikat o konieczności skonfigurowania reguł routingu. Pozostaw tę stronę otwartą lub zapisz szczegóły trasy (Destination i Via), ponieważ będą potrzebne w następnym kroku.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Przejdź do **ZeroTier Central** i znajdź sekcję **Advanced**.

    Wprowadź szczegóły trasy (Destination i Via) uzyskane w poprzednim kroku, a następnie kliknij **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

    Po dodaniu trasy sekcja **Managed Routes** będzie wyglądać jak poniżej.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. Teraz możesz uzyskać dostęp do `GL-AXT1800` przez jego adres IP (`192.168.29.1`) z innych urządzeń. W praktyce możesz uzyskać dostęp do wszystkich urządzeń w podsieci `192.168.29.0/24`.

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Zezwól na zdalny dostęp do LAN

Jeśli ta opcja jest włączona, zasoby po stronie LAN urządzenia mogą być dostępne przez wirtualną sieć ZeroTier.

Na przykład, jak pokazano na poniższej topologii, jeśli ta funkcja jest włączona, możesz zalogować się przez SSH do `Ubuntu` za pomocą jego adresu IP (`192.168.8.110`) z `leo-phone`. Dzieje się tak dlatego, że `Ubuntu` jest urządzeniem warstwy podrzędnej względem `GL-MT2500`, a to drugie jest podłączone do tej samej sieci ZeroTier co leo-phone.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Uwaga**: Aby ta funkcja działała, trzeba dodać reguły routingu do sieci ZeroTier. W Legacy Central można bezpłatnie dodać jedną trasę niestandardową, natomiast w New Central konfiguracja tras niestandardowych jest dostępna dopiero od planu Essential wzwyż. Szczegóły znajdziesz [tutaj](https://www.zerotier.com/pricing/).

Poniższe kroki pokazano na przykładzie Legacy Central.

1. Zaloguj się do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **ZeroTier**.

    Włącz **Allow Remote Access LAN** i kliknij **Apply**.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    Pojawi się komunikat o konieczności skonfigurowania reguł routingu. Pozostaw tę stronę otwartą lub zapisz szczegóły trasy (Destination i Via), ponieważ będą potrzebne w następnym kroku.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Przejdź do **ZeroTier Central** i znajdź sekcję **Advanced**.

    Wprowadź szczegóły trasy (Destination i Via) uzyskane w poprzednim kroku, a następnie kliknij **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    Po dodaniu trasy sekcja **Managed Routes** będzie wyglądać jak poniżej.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. Teraz możesz wykonać ping albo zalogować się przez SSH do `Ubuntu` za pomocą jego adresu IP (`192.168.8.110`) z innych urządzeń. W praktyce możesz uzyskać dostęp do wszystkich urządzeń w podsieci `192.168.8.0/24`.

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Masz dodatkowe pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
