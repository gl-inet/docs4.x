# Logowanie SSH do routera

Secure Shell (SSH) to kryptograficzny protokół sieciowy służący do bezpiecznej obsługi usług sieciowych w niezabezpieczonej sieci. Najbardziej znanym zastosowaniem jest zdalny dostęp użytkowników do systemów komputerowych. Czasami potrzebujesz podstawowych narzędzi do połączenia SSH z serwerem. Ten przewodnik opisuje, jak zalogować się przez SSH do routerów GL.iNet.

---

## Dla użytkowników Windows

Istnieje kilka sposobów uzyskania dostępu do terminala routera w systemie Windows, w tym przez Windows Cmd, PowerShell, Bitvise lub PuTTY.

### Korzystanie z Wiersza polecenia systemu Windows

1. Otwórz Wiersz polecenia

    Naciśnij **Win** + **R** (klawisz Windows + klawisz R), aby otworzyć okno Uruchamianie. Wpisz **cmd** i naciśnij Enter. 

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Otworzy się czarne okno wiersza polecenia.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Zaloguj się do routera

    W oknie wiersza polecenia wpisz `ssh root@192.168.8.1` i naciśnij Enter.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Uwaga**: 192.168.8.1 to domyślny adres IP routera. Jeśli został wcześniej zmieniony, użyj własnego adresu IP.

    Następnie wpisz hasło administratora routera i naciśnij Enter. **Ze względów bezpieczeństwa hasło nie jest wyświetlane na ekranie**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Jeśli hasło jest prawidłowe, zalogujesz się do routera pomyślnie.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Rozwiązywanie problemów"

    1. **Błąd: Connection timed out**
    
        Upewnij się, że urządzenie (np. laptop) jest podłączone do routera. Połącz się ponownie z siecią Wi-Fi routera lub portem LAN i spróbuj ponownie.

    2. **Błąd: Permission denied**

        Upewnij się, że wpisujesz prawidłowe hasło administratora. Jeśli zapomniałeś hasła, zresetuj router, przytrzymując przycisk RESET przez 10 sekund.

### Korzystanie z PowerShell

1. Otwórz Windows PowerShell

    Kliknij ikonę wyszukiwania na pasku zadań, wpisz **PowerShell**, wybierz **Windows PowerShell** i **uruchom jako administrator**.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Zaloguj się do routera

    W oknie PowerShell wpisz `ssh root@192.168.8.1` i naciśnij Enter.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Uwaga**: 192.168.8.1 to domyślny adres IP routera. Jeśli został wcześniej zmieniony, użyj własnego adresu IP.

    System poprosi o potwierdzenie połączenia. Wpisz `yes` i naciśnij Enter.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Zostaniesz poproszony o wprowadzenie hasła administratora routera. Wprowadź prawidłowe hasło administratora i naciśnij Enter. **Ze względów bezpieczeństwa hasło nie jest wyświetlane na ekranie**.
    
    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}
    
    Następnie pomyślnie zalogujesz się do terminala routera.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Rozwiązywanie problemów"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Dzieje się tak, gdy klucz zabezpieczeń routera uległ zmianie (np. po resecie do ustawień fabrycznych lub aktualizacji oprogramowania układowego) lub jeśli wcześniej łączyłeś się z innym routerem, powodując niepowodzenie weryfikacji klucza hosta.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Aby to naprawić, otwórz Eksplorator plików, przejdź do `C:\Users\Administrator\.ssh` i znajdź plik o nazwie **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Kliknij dwukrotnie plik known_hosts i otwórz go w Notatniku.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Usuń wpis związany z adresem IP routera (np. 192.168.8.1) i zapisz plik. Zamknij Eksplorator plików.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Wróć do PowerShell i użyj polecenia `ssh root@192.168.8.1`, aby ponownie połączyć się z routerem. System poprosi o potwierdzenie połączenia. Wpisz `yes` i naciśnij enter, a następnie wprowadź hasło logowania routera. Pomyślnie zalogujesz się do terminala routera.

    2. **Co zrobić, jeśli zmieniłem port SSH routera?**
    
        Jeśli zmieniłeś port SSH routera, określ port za pomocą parametru "-p" podczas korzystania z polecenia ssh. Na przykład: 
        
        ``ssh -p [numer nowego portu] [nazwa użytkownika]@[adres IP routera]``

### Korzystanie z Bitvise

Obejrzyj ten film, aby zalogować się do routera przez Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Korzystanie z PuTTY

1. Pobierz PuTTY

    Pobierz najnowszą wersję PuTTY z [tej strony](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Zainstaluj PuTTY

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Uruchom PuTTY

    Kliknij **PuTTY** w menu Start.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    Zobaczysz następujące okno konfiguracji.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Wprowadź nazwę hosta (lub adres IP) `192.168.8.1`, pozostaw port jako domyślny `22`, wybierz typ połączenia jako `SSH`.

    Wprowadź `Your Session` w zapisanych sesjach i zapisz (`Save`) zawartość. 

    Następnie kliknij `Open` u dołu.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    Pojawi się alert bezpieczeństwa jak poniżej, kliknij `Yes`.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Następnie wprowadź hasło administratora. **Ze względów bezpieczeństwa hasło nie jest wyświetlane na ekranie**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    Gdy zobaczysz powyższy obraz, oznacza to, że pomyślnie zalogowałeś się do routera przez SSH.

---

## Dla użytkowników Linux/Mac

Proces w systemach Linux i Mac OS jest zasadniczo taki sam. Poniżej używamy Ubuntu jako przykładu.

### Korzystanie z Ubuntu

1. Uruchom Terminal.

    Uruchom Ubuntu. Kliknij dwukrotnie ikonę Terminal, aby uruchomić Terminal. 
    
    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Zaloguj się do routera.

    Wprowadź polecenie logowania SSH: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    System poprosi o potwierdzenie połączenia. Wpisz "yes" i naciśnij Enter. 

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Następnie wprowadź hasło administratora routera. **Ze względów bezpieczeństwa hasło nie jest wyświetlane na ekranie**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    Gdy zobaczysz powyższy obraz, oznacza to, że pomyślnie zalogowałeś się do routera.

??? "Rozwiązywanie problemów"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Dzieje się tak, gdy klucz zabezpieczeń routera uległ zmianie (np. po resecie do ustawień fabrycznych lub aktualizacji oprogramowania układowego) lub jeśli wcześniej łączyłeś się z innym routerem, powodując niepowodzenie weryfikacji klucza hosta.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Jeśli tak się stanie, uruchom polecenie z czerwonego pola powyżej. Skopiuj dokładne polecenie wyświetlane w terminalu.

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Następnie spróbuj połączyć się ponownie.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**
    
        Możesz napotkać ten błąd podczas łączenia. Błąd ten wynika ze zmiany w pakiecie Openssh od wersji 8.8. Aby to naprawić, otwórz plik **~/.ssh/config** za pomocą edytora tekstu (na przykład możesz użyć Nano lub Vim) i dodaj następujące linie:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Upewnij się, że zmieniłeś IP hosta, jeśli nie jest to adres domyślny.

        Więcej dyskusji na temat tego problemu można znaleźć [tutaj](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
