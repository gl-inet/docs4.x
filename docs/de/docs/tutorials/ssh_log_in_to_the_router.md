# Per SSH am Router anmelden

Secure Shell (SSH) ist ein kryptografisches Netzwerkprotokoll, mit dem Netzwerkdienste sicher über ein unsicheres Netzwerk betrieben werden können. Das bekannteste Anwendungsbeispiel ist die Remote-Anmeldung an Computersystemen. Manchmal reichen bereits einfache Standardwerkzeuge aus, um per SSH auf einen Server zuzugreifen. Diese Anleitung zeigt, wie Sie sich per SSH an GL.iNet-Routern anmelden.

---

## Für Windows-Nutzer

Unter Windows gibt es mehrere Möglichkeiten, auf das Router-Terminal zuzugreifen, darunter Windows Cmd, PowerShell, Bitvise oder PuTTY.

### Mit Windows Cmd

1. Eingabeaufforderung öffnen

    Drücken Sie **Win** + **R** (Windows-Taste + R-Taste), um das Ausführen-Fenster zu öffnen. Geben Sie **cmd** ein und drücken Sie **Enter**.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Ein schwarzes Eingabeaufforderungsfenster wird angezeigt.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Am Router anmelden

    Geben Sie im Eingabeaufforderungsfenster `ssh root@192.168.8.1` ein und drücken Sie **Enter**.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Hinweis**: 192.168.8.1 ist die Standard-IP-Adresse des Routers. Wenn Sie sie zuvor geändert haben, verwenden Sie stattdessen Ihre eigene IP-Adresse.

    Geben Sie anschließend das Admin-Passwort Ihres Routers ein und drücken Sie **Enter**. **Aus Sicherheitsgründen wird das Passwort nicht auf dem Bildschirm angezeigt**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Wenn das Passwort korrekt ist, melden Sie sich erfolgreich an Ihrem Router an.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Fehlerbehebung"

    1. **Error: Connection timed out**

        Stellen Sie sicher, dass Ihr Gerät (z. B. Laptop) mit dem Router verbunden ist. Verbinden Sie sich erneut mit dem WLAN oder LAN-Port des Routers und versuchen Sie es noch einmal.

    2. **Error: Permission denied**

        Stellen Sie sicher, dass Sie das richtige Admin-Passwort eingeben. Wenn Sie das Passwort vergessen haben, setzen Sie den Router zurück, indem Sie die Taste **RESET** 10 Sekunden lang gedrückt halten.

### Mit PowerShell

1. Windows PowerShell öffnen

    Klicken Sie auf das Suchsymbol in der Taskleiste, geben Sie **PowerShell** ein, wählen Sie **Windows PowerShell** aus und **führen Sie sie als Administrator aus**.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Am Router anmelden

    Geben Sie im PowerShell-Fenster `ssh root@192.168.8.1` ein und drücken Sie **Enter**.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Hinweis**: 192.168.8.1 ist die Standard-IP-Adresse des Routers. Wenn Sie sie zuvor geändert haben, verwenden Sie stattdessen Ihre eigene IP-Adresse.

    Das System fordert Sie auf, die Verbindung zu bestätigen. Geben Sie `yes` ein und drücken Sie **Enter**.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Anschließend werden Sie aufgefordert, das Admin-Passwort des Routers einzugeben. Geben Sie das korrekte Admin-Passwort ein und drücken Sie **Enter**. **Aus Sicherheitsgründen wird das Passwort nicht auf dem Bildschirm angezeigt**.

    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

    Danach melden Sie sich erfolgreich am Terminal Ihres Routers an.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Fehlerbehebung"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Dies tritt auf, wenn sich der Sicherheitsschlüssel des Routers geändert hat (z. B. nach einem Zurücksetzen auf Werkseinstellungen oder einem Firmware-Update) oder wenn Sie zuvor eine Verbindung zu einem anderen Router hergestellt haben, wodurch die Host-Key-Prüfung fehlschlägt.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Öffnen Sie zur Behebung bitte den Datei-Explorer, wechseln Sie zu `C:\Users\Administrator\.ssh` und suchen Sie nach einer Datei mit dem Namen **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Doppelklicken Sie auf die Datei **known_hosts** und öffnen Sie sie mit dem Editor.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Löschen Sie den Eintrag, der zur IP-Adresse des Routers gehört (z. B. 192.168.8.1), und speichern Sie die Datei. Schließen Sie danach den Datei-Explorer.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Wechseln Sie zurück zu PowerShell und verwenden Sie erneut den Befehl `ssh root@192.168.8.1`, um sich mit dem Router zu verbinden. Sie werden aufgefordert, die Verbindung zu bestätigen. Geben Sie `yes` ein und drücken Sie **Enter**, geben Sie dann das Anmeldepasswort des Routers ein. Danach melden Sie sich erfolgreich am Terminal Ihres Routers an.

    2. **Was soll ich tun, wenn ich den SSH-Port des Routers geändert habe?**

        Wenn Sie den SSH-Port des Routers geändert haben, geben Sie den Port beim Verwenden des `ssh`-Befehls über den Parameter „-p“ an. Zum Beispiel:

        ``ssh -p [new port number] [username]@[router IP address]``

### Mit Bitvise

Sehen Sie sich dieses Video an, um sich per Bitvise an Ihrem Router anzumelden.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Mit PuTTY

1. PuTTY herunterladen

    Laden Sie die neueste PuTTY-Version von [hier](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"} herunter.

2. PuTTY installieren

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. PuTTY starten

    Klicken Sie im Startmenü auf **PuTTY**.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    Das folgende Konfigurationsfenster wird angezeigt.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Geben Sie bei **Host Name (or IP address)** `192.168.8.1` ein, belassen Sie **Port** auf dem Standardwert `22` und wählen Sie als Verbindungstyp **SSH** aus.

    Geben Sie bei **Saved Sessions** `Your Session` ein und klicken Sie auf **Save**.

    Klicken Sie dann unten auf **Open**.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    Es erscheint ein Sicherheitshinweis wie unten gezeigt. Klicken Sie auf **Yes**.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Geben Sie dann Ihr Admin-Passwort ein. **Aus Sicherheitsgründen wird das Passwort nicht auf dem Bildschirm angezeigt**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    Wenn Sie das oben gezeigte Bild sehen, bedeutet das, dass Sie sich erfolgreich per SSH am Router angemeldet haben.

---

## Für Linux-/Mac-Nutzer

Der Ablauf unter Linux und macOS ist im Allgemeinen gleich. Im Folgenden verwenden wir Ubuntu als Beispiel.

### Mit Ubuntu

1. Terminal starten.

    Starten Sie Ubuntu. Doppelklicken Sie auf das Terminal-Symbol, um das Terminal zu öffnen.

    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Am Router anmelden.

    Geben Sie den SSH-Anmeldebefehl ein: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    Das System fordert Sie auf, die Verbindung zu bestätigen. Geben Sie `yes` ein und drücken Sie **Enter**.

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Geben Sie anschließend das Admin-Passwort Ihres Routers ein. **Aus Sicherheitsgründen wird das Passwort nicht auf dem Bildschirm angezeigt**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    Wenn Sie das oben gezeigte Bild sehen, bedeutet das, dass Sie sich erfolgreich am Router angemeldet haben.

??? "Fehlerbehebung"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Dies tritt auf, wenn sich der Sicherheitsschlüssel des Routers geändert hat (z. B. nach einem Zurücksetzen auf Werkseinstellungen oder einem Firmware-Update) oder wenn Sie zuvor eine Verbindung zu einem anderen Router hergestellt haben, wodurch die Host-Key-Prüfung fehlschlägt.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Führen Sie in diesem Fall den Befehl aus, der oben im roten Kasten angezeigt wird. Kopieren Sie bitte genau den Befehl, der in Ihrem Terminal angezeigt wird.

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Versuchen Sie anschließend erneut, die Verbindung herzustellen.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**

        Dieser Fehler kann beim Verbinden auftreten. Er wird durch eine Änderung im OpenSSH-Paket ab Version 8.8 verursacht. Öffnen Sie zur Behebung die Datei **~/.ssh/config** mit einem Texteditor (zum Beispiel Nano oder Vim) und fügen Sie die folgenden Zeilen hinzu:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Achten Sie darauf, die Host-IP zu ändern, wenn es sich nicht um die Standard-IP handelt.

        Weitere Informationen zu diesem Problem finden Sie [hier](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
