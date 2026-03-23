# Verwenden Sie WinSCP, um auf Ihre freigegebenen Dateien zuzugreifen

Mit **WinSCP** können Sie mithilfe der Dateifreigabefunktion von **GL-Routers** auf Ihre freigegebenen Dateien zugreifen.

Richten Sie Ihre **WebDAV**-Links bitte im Reiter für den Netzwerkspeicher ein. Ausführliche Informationen finden Sie in der Anleitung zu [WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav).

## Links in WinSCP einrichten

Nachdem Sie WebDAV eingerichtet haben, können Sie zur Seite **Share Folders** des Netzwerkspeichers zurückkehren.

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Klicken Sie mit der rechten Maustaste auf das Symbol **"..."** und kopieren Sie den HTTPS-Link.

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Starten Sie WinSCP, wählen Sie **WebDAV** und aktivieren Sie außerdem die Verschlüsselung **TLS/SSL**. Fügen Sie dann den Link in **Host name** ein; die Portnummer wird automatisch auf 6008 geändert.

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Geben Sie Ihren Benutzernamen und Ihr Passwort ein, klicken Sie dann auf **Save** und **Login**. Danach wird der freigegebene Ordner geöffnet.

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
