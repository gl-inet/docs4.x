# Zarzadzanie eSIM

W panelu administracyjnym WWW, po lewej stronie, przejdz do **APPLICATIONS** -> **eSIM Management**.

Ta strona pozwala sprawdzic status fizycznej karty eSIM i zarzadzac profilami eSIM. Sklada sie z dwoch czesci: **Current eSIM Status** oraz **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Obslugiwane modele

| Model routera                  | Obsluga   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | √         |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**Dla modeli oznaczonych symbolem ※**:

1. Aktualne stabilne oprogramowanie firmware nie obsluguje eSIM. Aby korzystac z funkcji eSIM, nalezy zainstalowac firmware z obsluga eSIM. [Skontaktuj sie z nami](https://www.gl-inet.com/contacts/){target="_blank"}, aby uzyskac wiecej informacji.

2. W modelach oznaczonych symbolem ※ z modulem EP06-A eSIM nie jest obslugiwany, poniewaz oprogramowanie Qualcomm nie udostepnia wymaganych polecen AT.

3. W przypadku GL-E750 (Mudi) oraz modeli oznaczonych symbolem ※ z modulem EP06-E zapoznaj sie z tym [linkiem](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}, aby najpierw zaktualizowac firmware modulu, a nastepnie zainstalowac firmware z obsluga eSIM i wlaczyc te funkcje.

**Dla modeli oznaczonych symbolem X**:

1. GL-E750V2 vSIM nie obsluguje funkcji eSIM.

2. GL-E5800 (Mudi 7) ma wbudowana karte eSIM. W zwiazku z tym fizyczna karta eSIM bedzie rozpoznawana na Mudi 7 jako zwykla karta SIM bez funkcji eSIM.

## Current eSIM Status

Ta sekcja wyswietla podstawowe informacje i szczegoly aktualnie aktywnego profilu eSIM.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Globalnie unikalny identyfikator eUICC (ukladu eSIM), uzywany do identyfikacji i zarzadzania profilami.
- **ICCID:** Integrated Circuit Card Identifier aktualnie aktywnego profilu eSIM.
- **IMSI:** International Mobile Subscriber Identity aktualnie aktywnego profilu eSIM.
- **eSIM OS Version:** Wersja systemu operacyjnego eUICC, ktora okresla jego zgodnosc i obslugiwane mozliwosci.
- **eSIM Storage (remain/total):** Dostepna i calkowita pojemnosc eUICC do przechowywania profili eSIM.
- **eSIM Profile Number:** Liczba profili eSIM aktualnie zapisanych na eUICC. Pamietaj, ze profile eSIM oferowane przez roznych operatorow moga miec rozne rozmiary, dlatego liczba profili, ktore mozna zapisac na eUICC, takze bedzie sie roznic.

## eSIM Profile List

Ta sekcja wyswietla informacje o profilu startowym i profilach standardowych.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: Profil startowy jest fabrycznie zaladowany 1 GB bezplatnych danych dla USA i Europy oraz 100 MB danych globalnych, waznych przez 1 rok od daty aktywacji. Dane te pozwalaja pobierac inne profile na calym swiecie. Mozesz tez monitorowac wykorzystanie profilu startowego, w tym ilosc pozostalych danych, calkowity pakiet oraz date waznosci.

- **Normal Profile**: Jesli kupisz profil eSIM i wgrasz go za pomoca kodu QR lub kodu aktywacyjnego, profil zostanie wyswietlony tutaj.

### Doladowanie profilu startowego

GL.iNet udostepnia fabrycznie zaladowany profil startowy z 100 MB danych globalnych oraz 1 GB danych waznych w Europie i USA na potrzeby poczatkowej konfiguracji i aktywacji profili eSIM. Ten pakiet jest przeznaczony do pobierania nowych profili eSIM po przybyciu do miejsca bez dostepu do Internetu.

Jesli wykorzystales juz wstepnie doladowane darmowe dane lub jesli wygasly i chcesz dalej korzystac z uslugi, mozesz doladowac profil startowy.

W sekcji **Seed Profile** kliknij po prawej stronie przycisk **Top-up**.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

W wyskakujacym oknie zeskanuj kod QR i postepuj zgodnie z instrukcjami, aby zakonczyc doladowanie.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Zakup profilu eSIM

Profile eSIM mozna kupic w naszych polecanych sklepach, sklepach przetestowanych lub u innych zewnetrznych dostawcow eSIM.

??? note "Opcja 1: zakup w naszych polecanych sklepach"

    Sa dwa polecane sklepy: [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} oraz [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    W sekcji **Normal Profile** kliknij po prawej stronie **eSIM Profile Recommended Store**.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Zeskanuj kod QR lub kliknij linki, aby kupic profile eSIM.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Uwaga**: Wszystkie pakiety profili eSIM kupione w tych dwoch sklepach sa w pelni zgodne z routerami GL.iNet. W razie pytan skontaktuj sie z naszym zespolen wsparcia pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Opcja 2: zakup w przetestowanych sklepach"

    Zapoznaj sie z [tym linkiem](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"}, aby zobaczyc liste sklepow przetestowanych przez GL.iNet.

    **Uwaga**: Nie mozemy zagwarantowac pelnej zgodnosci z routerami GL.iNet dla wszystkich profili lub pakietow z tych sklepow. Poniewaz GL.iNet nie ma z nimi partnerstwa, nie mozemy zapewnic wsparcia posprzedazowego ani pomocy przy zwrotach.

??? note "Opcja 3: zakup u innych zewnetrznych dostawcow eSIM"

    Mozesz rowniez kupic profile eSIM od innych dostawcow wedlug wlasnego wyboru.

    Nie mozemy jednak zagwarantowac pelnej zgodnosci z routerami GL.iNet dla profili eSIM kupionych od innych zewnetrznych dostawcow. Kupuj wedlug wlasnego uznania. GL.iNet nie ponosi odpowiedzialnosci za problemy z niezgodnoscia.

    W sprawie wsparcia posprzedazowego lub zwrotu skontaktuj sie z odpowiednim dostawca eSIM.

### Wgrywanie profilu eSIM

Po zakupie profilu eSIM zwykle otrzymasz kod QR lub kod aktywacyjny. Zapisz ten kod QR lokalnie, a nastepnie wykonaj ponizsze kroki, aby wgrac profil eSIM.

1. W sekcji **Normal Profile** kliknij na dole **Add eSIM Profile**.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Wgraj kod QR eSIM lub wpisz kod aktywacyjny, a nastepnie kliknij **Install**. Profil eSIM zostanie pobrany i zainstalowany na routerze.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Uwaga:**

    1. Wiekszosc profili eSIM mozna pobrac i zainstalowac tylko raz.

    2. Poprawnie sformatowany kod QR wyswietli kod aktywacyjny rozpoczynajacy sie od **LPA:**. Jednak niektore niestandardowe kody QR moga zawierac jedynie surowy kod aktywacyjny bez prefiksu LPA. W takim przypadku przed kliknieciem **Install** recznie dodaj `LPA:` na poczatku kodu.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Jesli nie kupiles jeszcze zadnego profilu eSIM, mozesz kupic go w **eSIM Profile Recommended Store**. Kliknij [tutaj](#zakup-profilu-esim), aby zobaczyc szczegoly.

3. Wlacz swoj profil eSIM.

    Po pomyslnym wgraniu nowy profil eSIM pojawi sie na liscie **Normal Profile**. Kliknij **Enable**, aby go aktywowac.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Polacz sie z Internetem.

    Po wlaczeniu profilu eSIM przejdz do **INTERNET** -> **Cellular**. Kliknij **Connect**, aby nawiazac polaczenie z Internetem przy uzyciu profilu eSIM.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Uwaga**: Niektore profile eSIM moga wymagac dodatkowej konfiguracji, takiej jak ustawienia APN, PIN lub TTL. W razie potrzeby kliknij **Manual Setup** lub **SIM Card Settings**, aby dostosowac te parametry. W niektorych przypadkach moze byc konieczne ponowne uruchomienie urzadzenia w celu nawiazania polaczenia z Internetem.*

5. Gdy router polaczy sie pomyslnie przez profil eSIM, strona bedzie wyswietlana nastepujaco:

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Eksport logu dla wsparcia

Kliknij **Export Log for Support**, aby zobaczyc wszystkie logi zwiazane z eSIM. Jesli napotkasz problemy i potrzebujesz wsparcia technicznego, wyeksportuj logi eSIM i udostepnij je naszemu zespolowi wsparcia mailowo pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Powiazane artykuly:

- [Jak korzystac z fizycznej karty eSIM z routerami GL.iNet?](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Jak korzystac z fizycznej karty eSIM z urzadzeniami Android?](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Masz jeszcze pytania? Odwiedz nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj sie z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
