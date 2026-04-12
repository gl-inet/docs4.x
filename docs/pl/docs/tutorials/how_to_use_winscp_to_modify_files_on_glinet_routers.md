# Jak używać WinSCP do modyfikowania plików na routerach GL.iNet

WinSCP to łatwe narzędzie do edytowania, kopiowania i pobierania plików lub katalogów na routerze. Możesz kopiować pliki między komputerem lokalnym a routerem przy użyciu protokołów przesyłania plików FTP, SCP, SFTP, WebDAV lub S3. Dotyczy to systemu operacyjnego Windows.

---

1. Pobierz WinSCP [stąd](https://winscp.net/eng/download.php){target="_blank"} i zainstaluj na swoim systemie Windows.

2. Połącz się z routerem, następnie uruchom WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * Protokół plików: Wybierz `SCP` jako protokół.
    * Nazwa hosta: Wprowadź adres IP routera. Jeśli nie zmieniałeś adresu IP routera, powinien to być `192.168.8.1`
    * Numer portu: `22`
    * Nazwa użytkownika i hasło: Wprowadź `root` jako nazwę użytkownika i wprowadź swoje hasło. 

    Następnie kliknij przycisk `Login`.

3. Po zalogowaniu będziesz mieć pełną kontrolę nad routerem.

    Możesz wybierać, przeglądać, edytować lub przesyłać pliki/katalogi z/do routera.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Na przykład, jeśli chcesz edytować konfigurację zapory, możesz przejść do /etc/config, znaleźć plik firewall, kliknąć go prawym przyciskiem myszy, a następnie wybrać **Edit**.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Teraz możesz swobodnie edytować zawartość pliku. Uważaj, aby nie pomieszać ustawień.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
