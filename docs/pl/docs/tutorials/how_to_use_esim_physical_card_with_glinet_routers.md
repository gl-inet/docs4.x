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

Tutaj możesz sprawdzić stan eSIM i zarządzać profilami eSIM.

Jednocześnie może być aktywny tylko jeden profil eSIM. Zielona kropka oznacza, że wybrany profil eSIM jest obecnie aktywny.

---

Powiązany artykuł:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

