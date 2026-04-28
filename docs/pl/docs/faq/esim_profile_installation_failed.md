# Co zrobic, jesli instalacja profilu eSIM nie powiedzie sie?

Jesli probujesz dodac profil eSIM na routerze GL.iNet, ale instalacja sie nie udaje, zapoznaj sie z ponizszymi krokami rozwiazywania problemow:

1. Upewnij sie, ze router jest polaczony z Internetem.

    Upewnij sie, ze router nawiazal polaczenie z Internetem. Niestabilna siec moze wplynac na wgrywanie profilu eSIM i spowodowac, ze router nie pobierze go ani nie zainstaluje.

    Jesli to mozliwe, sproboj podlaczyc router do innego zrodla sieci, takiego jak hotspot smartfona albo publiczna siec Wi-Fi, a nastepnie ponownie wgraj profil eSIM, aby sprawdzic rezultat.

2. Zmien ustawienia DNS.

    Jesli Internet dziala prawidlowo, zaloguj sie do panelu administracyjnego WWW routera i przejdz do **NETWORK** -> **DNS**.

    Przelacz DNS Mode na **Manual DNS** i ustaw inne publiczne serwery DNS do testow, na przyklad Google DNS (`8.8.8.8`, `8.8.4.4`) lub Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Kliknij **Apply**, aby zapisac zmiany, a nastepnie sprobuj ponownie wgrac profil eSIM.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. Wylacz AdGuard Home.

    Jesli AdGuard Home jest dostepny i wlaczony na routerze, wylacz go i sprobuj ponownie zainstalowac profil eSIM.

4. Sprawdz dostepnosc profilu eSIM.

    Sprawdz, czy ten profil eSIM lub kod QR nie zostal juz aktywowany albo zainstalowany na innym urzadzeniu.

    Wiekszosc profili eSIM mozna zainstalowac tylko raz i nie da sie ich aktywowac na wielu urzadzeniach. Jesli to mozliwe, skontaktuj sie z dostawca eSIM, aby potwierdzic, czy obecny profil eSIM jest nadal dostepny. Jesli kod QR lub kod aktywacyjny wygasl, popros o nowy i sprobuj ponownie.

5. Sprawdz kod aktywacyjny.

    Poprawnie sformatowany kod QR wyswietli kod aktywacyjny rozpoczynajacy sie od **LPA:**. Jednak niektore niestandardowe kody QR moga zawierac jedynie surowy kod bez prefiksu LPA. W takim przypadku przed kliknieciem **Install** recznie dodaj `LPA:` na poczatku kodu.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Sprawdz, czy wymagany jest kod potwierdzajacy.

    Niektore profile eSIM wymagaja podczas instalacji podania kodu potwierdzajacego, na przyklad Smarty eSIM. Sprawdz pakiet eSIM albo instrukcje instalacji, aby potwierdzic, czy taki kod jest potrzebny. Jesli tak, wpisz poprawny kod.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Jesli powyzsze kroki nie rozwiaza problemu, wyeksportuj log eSIM ze strony **eSIM Management**.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Nastepnie wyslij log wraz z ponizszymi kluczowymi informacjami na adres [support@gl-inet.com](mailto:support@gl-inet.com), aby uzyskac dalsza pomoc.

    - Napotkany problem
    - Metody rozwiazywania problemow, ktore juz wyprobowales
    - Twoj dostawca eSIM

---
