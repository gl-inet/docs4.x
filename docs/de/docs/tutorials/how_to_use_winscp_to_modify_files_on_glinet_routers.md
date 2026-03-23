# So verwenden Sie WinSCP, um Dateien auf GL.iNet-Routern zu ändern

WinSCP ist ein einfaches Werkzeug zum Bearbeiten, Kopieren und Herunterladen von Dateien oder Verzeichnissen auf dem Router. Sie können Dateien zwischen einem lokalen Computer und Ihrem Router über die Dateiübertragungsprotokolle FTP, SCP, SFTP, WebDAV oder S3 kopieren. Es ist für das Windows-Betriebssystem geeignet.

---

1. Laden Sie WinSCP von [hier](https://winscp.net/eng/download.php){target="_blank"} herunter und installieren Sie es unter Windows.

2. Verbinden Sie sich mit dem Router und starten Sie dann WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * **File protocol**: Wählen Sie `SCP` als Protokoll.
    * **Host name**: Geben Sie die IP-Adresse des Routers ein. Wenn Sie die IP Ihres Routers nicht geändert haben, sollte sie `192.168.8.1` lauten.
    * **Port number**: `22`
    * **Username & Password**: Geben Sie `root` als Benutzernamen ein und tragen Sie Ihr Passwort ein.

    Klicken Sie dann auf die Schaltfläche `Login`.

3. Nach der Anmeldung haben Sie die vollständige Kontrolle über den Router.

    Sie können Dateien und Verzeichnisse auf dem Router auswählen, anzeigen, bearbeiten oder vom/zum Router übertragen.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Wenn Sie zum Beispiel die Firewall-Konfiguration bearbeiten möchten, können Sie zu /etc/config gehen, die Datei `firewall` suchen, mit der rechten Maustaste darauf klicken und dann **Edit** wählen.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Jetzt können Sie den Dateiinhalt frei bearbeiten. Achten Sie darauf, die Einstellungen nicht zu beschädigen.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
