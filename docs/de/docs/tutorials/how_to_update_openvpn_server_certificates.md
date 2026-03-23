# Wie aktualisiert man OpenVPN-Serverzertifikate?

Dieses Tutorial erklärt, wie Sie die Zertifikate des OpenVPN-Servers auf Ihren GL.iNet-Routern aktualisieren.

**Hinweis**: Für diesen Vorgang muss das Root-CA-Zertifikat aktualisiert werden. Dadurch werden alle vorhandenen Client-Zertifikate (die in den Konfigurationsdateien eingebettet sind) ungültig. Sie müssen daher alle Konfigurationsdateien für Ihre OpenVPN-Clients erneut exportieren, damit diese sich wieder mit dem Server verbinden können.

1. Melden Sie sich am webbasierten Admin Panel Ihres Routers an und gehen Sie zu **VPN** -> **OpenVPN Server**.

    Wenn Ihr OpenVPN-Server bereits läuft, stoppen Sie den Dienst.

2. Klicken Sie auf der Registerkarte Configuration auf **Advanced Configuration**, um die Einstellungen aufzuklappen.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Suchen Sie das **Server Root Certificate** und löschen Sie den gesamten Inhalt des Textfelds.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Das zugehörige Server Certificate und der Server Key werden ebenfalls automatisch entfernt, wie unten dargestellt.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Lassen Sie alle drei Felder leer und klicken Sie unten auf **Apply**. Neue Zertifikate werden automatisch erzeugt und in die Felder eingetragen.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. Die Zertifikate des OpenVPN-Servers sind jetzt aktualisiert. Klicken Sie unten auf **Export Client Configuration**, um neue Konfigurationsdateien für die Geräte zu exportieren, die sich verbinden sollen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
