# Jak korzystać z fizycznej karty eSIM z routerami GL.iNet?

Ten przewodnik pokazuje, jak korzystać z fizycznej karty eSIM zakupionej w sklepie internetowym GL.iNet z routerami GL.iNet.

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Funkcje

Najważniejsze cechy fizycznej karty eSIM:

- Obsługuje sieci 4G i 5G, zapewniając niezawodne i szybkie połączenia.
- Zarządzaj profilami eSIM bez wysiłku — dodawaj, usuwaj lub włączaj je.
- Wybieraj i kupuj preferowane pakiety danych w większości sklepów eSIM na całym świecie w dowolnym czasie.
- Współpracuje z profilami eSIM z większości globalnych sklepów eSIM.
- Kupuj profile eSIM online bez podawania danych osobowych, co zmniejsza ryzyko naruszenia prywatności.
- Zawiera profil startowy z 1 GB bezpłatnych danych dla USA i Europy oraz 100 MB danych globalnych, ważnych przez 1 rok od daty aktywacji.
- Kompatybilna z wybranymi urządzeniami GL.iNet.

## Obsługiwane modele

| Model routera                  | Obsługa   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | ※        |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**Modele oznaczone symbolem ※**:

1. Aktualne stabilne oprogramowanie układowe nie obsługuje eSIM. Aby korzystać z funkcji eSIM, należy zainstalować oprogramowanie z obsługą eSIM. [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}, aby uzyskać więcej informacji.
    
2. Jeśli korzystasz z modelu ※ z modułem EP06-A, eSIM nie jest obsługiwany ze względu na brak wsparcia dla określonych poleceń AT w oprogramowaniu Qualcomm.
    
3. Jeśli korzystasz z modelu ※ z modułem EP06-E, zapoznaj się z tym [linkiem](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}, aby zaktualizować oprogramowanie modułu i zainstalować oprogramowanie z obsługą eSIM w celu włączenia funkcji eSIM.

**Modele oznaczone symbolem X**:

1. GL-E750V2 vSIM nie obsługuje funkcji eSIM.

2. GL-E5800 (Mudi 7) ma wbudowaną kartę eSIM. W związku z tym fizyczna karta eSIM zostanie rozpoznana jako zwykła karta SIM bez funkcji eSIM na Mudi 7.

## Konfiguracja fizycznej karty eSIM

Jeśli używasz fizycznej karty eSIM po raz pierwszy, obejrzyj ten film konfiguracyjny lub wykonaj poniższe kroki, aby skonfigurować ją na routerze GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Krok 1:** Włóż fizyczną kartę eSIM do routera. Skorzystaj z poniższych ilustracji, aby zrobić to prawidłowo.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Krok 2:** Otwórz przeglądarkę i wpisz „192.168.8.1” w pasku adresu, aby zalogować się do panelu administracyjnego GL.iNet.

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Krok 3:** Połącz urządzenie z internetem. 

Przejdź do **INTERNET** i kliknij **Connect** (lub **Auto Setup** w starszych wersjach firmware), aby połączyć się z internetem przez sieć komórkową.

*Ta fizyczna karta eSIM jest dostarczana z profilem startowym zawierającym 1 GB bezpłatnych danych dla USA i Europy oraz 100 MB danych globalnych, ważnych przez 1 rok od daty aktywacji. Pamiętaj, że te dane służą wyłącznie do zakupu i pobierania profili eSIM i nie są przeznaczone do ogólnego dostępu do internetu.*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Jeśli połączenie z internetem zostanie nawiązane pomyślnie, ekran będzie wyglądał następująco.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Zarządzanie profilem eSIM

**Krok 1:** Upewnij się, że na urządzeniu GL.iNet jest zainstalowana najnowsza wersja firmware.

Upewnij się, że wersja to 4.0 lub nowsza, a numer Firmware Type wynosi 0319 lub więcej.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Jeśli firmware **nie jest aktualne**, możesz zaktualizować je automatycznie online albo ręcznie.

<u>Opcja 1</u>: Aktualizacja firmware online

1. Upewnij się, że urządzenie jest połączone z internetem. 
    
2. W panelu administracyjnym WWW przejdź do **SYSTEM** > **Upgrade** > **Online Upgrade**, a następnie kliknij przycisk **Install**, aby automatycznie zaktualizować urządzenie do najnowszej wersji firmware.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Opcja 2</u>: Ręczna aktualizacja firmware

1. Pobierz firmware dla odpowiedniego modelu z obsługą eSIM [stąd](https://dl.gl-inet.com/){target="_blank"}.
    
2. W panelu administracyjnym WWW przejdź do **SYSTEM** > **Upgrade** > **Local Upgrade**. Wybierz plik firmware lub przeciągnij go do wyznaczonego obszaru, aby zaktualizować urządzenie do najnowszej wersji.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Niektóre modele, takie jak Mudi (GL-E750), Puli (GL-XE300) i Spitz (GL-X750), nie obsługują eSIM, jeśli są wyposażone w moduły Quectel EP06-A, ponieważ oprogramowanie Qualcomm nie obsługuje określonych poleceń AT.  
    
    2. Jeśli mają zainstalowane moduły EP06-E, skorzystaj z [tego linku](https://forum.gl-inet.com/t/48907){target="_blank"}, aby zaktualizować moduł do najnowszego oprogramowania z obsługą eSIM.

**Krok 2:** Przejdź do eSIM Management.

Po aktualizacji firmware poczekaj, aż urządzenie uruchomi się ponownie, a następnie zaloguj się do panelu administracyjnego GL.iNet.

Przejdź do **APPLICATIONS** > **eSIM Management**. Tutaj możesz sprawdzić bieżący stan eSIM.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Jednocześnie może być aktywny tylko jeden profil eSIM. Zielona kropka oznacza, że wybrany profil eSIM jest obecnie aktywny.

## Przewodnik po eSIM Management

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. Bieżący stan eSIM:**

Ta sekcja wyświetla podstawowe informacje o eSIM oraz szczegóły aktualnie aktywnego profilu.

- **EID:** Globalnie unikalny identyfikator eUICC (układu eSIM), używany do identyfikacji i sterowania profilami.
- **ICCID:** Integrated Circuit Card Identifier aktualnie aktywnego profilu eSIM.
- **IMSI:** International Mobile Subscriber Identity aktualnie aktywnego profilu eSIM.
- **eSIM OS Version:** Wersja systemu operacyjnego eUICC, która określa jego zgodność i możliwości.
- **eSIM Storage (remain/total):** Dostępna i całkowita pojemność pamięci eUICC do przechowywania profili eSIM.
- **eSIM Profile Number:** Liczba profili eSIM aktualnie zapisanych na eUICC.

**B. Profil startowy:**

Ta sekcja zawiera szczegóły profilu startowego. Profil startowy jest fabrycznie wyposażony w 1 GB bezpłatnych danych dla USA i Europy oraz 100 MB danych globalnych, ważnych przez 1 rok od daty aktywacji. Dane te umożliwiają pobieranie innych profili na całym świecie. Możesz również monitorować wykorzystanie profilu startowego, w tym pozostałą ilość danych, całkowitą ilość danych i datę wygaśnięcia.

**C. Profil standardowy:**

Ta sekcja wyświetla informacje o profilach standardowych. Jeśli kupisz profil eSIM w sklepie internetowym i prześlesz kod QR eSIM za pomocą funkcji **Add eSIM Profile (QR Code Install)**, profil pojawi się tutaj po zakończeniu przesyłania.

**D. Add eSIM Profile (QR Code Install):**

To podstawowa funkcja służąca do przesyłania i instalowania profili eSIM. Po zakupie profilu eSIM w sklepie internetowym otrzymasz kod QR. Kliknij ten przycisk, aby przesłać kod QR, a następnie pobrać i zainstalować profil eSIM na routerze.

**E. Export Log for Support:**

Ta sekcja umożliwia wyświetlenie wszystkich logów związanych z działaniem eSIM. Jeśli napotkasz problemy i potrzebujesz wsparcia technicznego, możesz wyeksportować te logi i udostępnić je naszemu zespołowi wsparcia przez e-mail na adres support@gl-inet.com.

**F. Top-up:**

Jeśli wykorzystasz bezpłatne i wstępnie załadowane dane dostarczone przez GL.iNet lub jeśli dane wygasną, a chcesz nadal korzystać z usługi, możesz kliknąć przycisk **Top-up**, zeskanować kod QR i kupić dodatkowe dane.

**G. Polecane sklepy z profilami eSIM:**

GL.iNet poleca dla wygody dwa partnerskie sklepy eSIM: EIOTCLUB oraz Tuge. Możesz zeskanować kody QR lub kliknąć link ([the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} lub [the Tuge eSIM Store](https://esim_store.gl-inet.com/){target="_blank"}), aby dokonać zakupu zgodnie ze swoimi potrzebami. Możesz też kupować pakiety eSIM u innych zewnętrznych dostawców według własnego wyboru.

**H. Actions:**

Ta sekcja umożliwia wygodne zarządzanie profilami eSIM, w tym ich włączanie, przełączanie i usuwanie.

## Doładowanie profilu startowego eSIM

Na potrzeby początkowej konfiguracji lub zakupu profilu eSIM GL.iNet zapewnia wstępnie załadowane dane: 100 MB do użytku globalnego oraz 1 GB dla Europy i USA. Te pakiety są celowo droższe i przeznaczone do sytuacji, w których po przyjeździe do danego miejsca bez dostępu do internetu trzeba pobrać nowy profil eSIM.

Aby doładować profil startowy eSIM, po prostu kliknij przycisk **Top-up**, zeskanuj kod QR i postępuj zgodnie z instrukcjami.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## Zakup i instalacja profilu eSIM

Po skonfigurowaniu routera wykonaj poniższe kroki, aby kupić i aktywować profil eSIM.

**Krok 1:** Kup profil eSIM w sklepach eSIM.

<u>Opcja 1</u>: Kup profil eSIM w jednym z naszych polecanych sklepów, [the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} lub [the Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}. Bezpośrednie linki do sklepów znajdziesz na ilustracji poniżej.


*Wszystkie pakiety profili eSIM zakupione w tych dwóch sklepach są w pełni zgodne z naszymi routerami. Jeśli masz pytania, skontaktuj się z naszym zespołem wsparcia pod adresem support@gl-inet.com.*

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>Opcja 2</u>: Skorzystaj z [tego linku](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"}, aby uzyskać listę sklepów przetestowanych przez GL.iNet. Pamiętaj, że nie możemy zagwarantować pełnej zgodności wszystkich pakietów z tych sklepów z routerami GL.iNet.

*Ponieważ GL.iNet nie współpracuje partnersko z tymi sklepami, nie możemy zapewnić obsługi posprzedażowej ani zwrotów związanych z tymi pakietami.*

<u>Opcja 3</u>: Kup profil eSIM u dowolnego innego zewnętrznego dostawcy.

**Krok 2**: Zainstaluj profil eSIM

Po zakupie profilu eSIM otrzymasz kod QR. Zapisz ten kod QR na komputerze. Następnie kliknij przycisk **Add eSIM Profile (QR Code Install)**, aby przesłać i zainstalować zakupiony profil eSIM.

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**Uwaga:** Jak pokazuje zielona strzałka na powyższym obrazie, poprawnie sformatowany kod QR wyświetli kod aktywacyjny rozpoczynający się od **LPA:**.

*Jednak niektóre niestandardowe kody QR mogą generować jedynie surowy kod aktywacyjny bez prefiksu LPA.
Jeśli tak się stanie, ręcznie dodaj „LPA:” na początku kodu przed kliknięciem przycisku Download & Install.*

**Krok 3:** Włącz nowy profil

Po pomyślnym przesłaniu kodu QR nowy profil eSIM pojawi się na liście w sekcji **Normal Profile**. Kliknij **Enable**, aby aktywować nowy profil eSIM. 

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**Krok 4:** Zastosuj nowy profil eSIM i połącz się z internetem

Po włączeniu profilu eSIM przejdź do **INTERNET** i kliknij **Connect**, aby zastosować profil eSIM i połączyć się z internetem.

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

*Uwaga: Niektóre profile eSIM mogą wymagać dodatkowych ustawień, takich jak APN, PIN lub TTL. W razie potrzeby kliknij **Manual Setup** lub **SIM Card Settings**, aby skonfigurować te ustawienia. W niektórych przypadkach może być konieczne ponowne uruchomienie urządzenia w celu nawiązania połączenia z internetem.*

Po pomyślnej konfiguracji profilu eSIM ekran będzie wyglądał następująco:

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**Krok 5:** Łatwe przełączanie i usuwanie profili eSIM

Możesz łatwo przełączać się między profilami eSIM, klikając **Enable** obok profilu, który chcesz aktywować. Aby usunąć profil eSIM, po prostu kliknij **Delete**.

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

