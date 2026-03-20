# Zugriff auf GL.iNet Router und AdGuard Home über HTTPS

Wenn Sie HTTPS verwenden möchten, um auf Ihren GL.iNet Router und AdGuard Home zuzugreifen, folgen Sie den untenstehenden Schritten.

## 1. Zertifikat und Schlüssel auf dem GL.iNet Router aktualisieren

Beantragen Sie zunächst ein SSL-Zertifikat oder verwenden Sie ein selbstsigniertes SSL-Zertifikat.

Melden Sie sich dann per SSH an Ihrem GL.iNet Router an oder verwenden Sie WinSCP, um das aktualisierte Zertifikat und den Schlüssel auf Ihren GL.iNet Router hochzuladen. Die Pfade lauten:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. AdGuard Home aktivieren

Melden Sie sich im Web-Admin-Panel von GL.iNet an und gehen Sie zu **APPLICATIONS -> AdGuard Home**. Aktivieren Sie AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Klicken Sie anschließend oben auf dieser Seite auf **Settings Page**. Sie werden dann zur Einstellungsseite von AdGuard Home weitergeleitet.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Encryption settings bearbeiten

Navigieren Sie auf der Einstellungsseite von AdGuard Home zu Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Aktivieren Sie oben links das Kontrollkästchen Enable Encryption und tragen Sie bei HTTPS port den Wert 3001 ein.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Fügen Sie die Pfade zu Ihrem aktualisierten Zertifikat und Schlüssel hinzu und klicken Sie auf Save.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Anschließend können Sie **192.168.8.1** oder **192.168.8.1:3001** über HTTPS aufrufen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
