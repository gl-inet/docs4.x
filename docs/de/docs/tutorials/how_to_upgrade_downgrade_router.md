# So aktualisieren oder downgraden Sie die Firmware Ihres Routers manuell (von v4.x auf v4.x)

In diesem Tutorial erfahren Sie, **wie Sie die Firmware Ihres Routers manuell aktualisieren oder downgraden (von v4.x auf v4.x)**. Die Schritte für das manuelle Upgrade und Downgrade der Router-Firmware sind identisch.

!!! Note "Über das Upgrade und Downgrade der Firmware Ihres Routers"

    **Upgrade:** GL.iNet-Router mit Firmware-Version 4.x bieten keine automatische Update-Funktion.

    Wenn eine neue Firmware-Version verfügbar ist, wird nach der Anmeldung im Admin-Panel des Routers der Hinweis „Upgrade Reminder“ angezeigt. Sie können auf die Schaltfläche **Upgrade** klicken, um die dort aufgeführte neueste Firmware-Version zu installieren. Wenn Sie auf eine bestimmte Firmware-Version aktualisieren möchten, folgen Sie den unten stehenden Schritten, um Ihren Router manuell zu aktualisieren.

    **Downgrade:** Sie können die Firmware Ihres Routers downgraden, um bestimmte Probleme zu beheben.

## 1. Prüfen, ob auf Ihrem Router die neueste Firmware-Version läuft (nur für ein Upgrade)

1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres Routers ein (z. B. 192.168.8.1) und melden Sie sich an.
2. Wählen Sie in der linken Seitenleiste **SYSTEM** > **Upgrade**.

## 2. Die Firmware-Datei herunterladen

1. Suchen Sie in der Suchleiste des [Firmware Download Center](https://dl.gl-inet.com/) nach Ihrem Router-Modell und wählen Sie es aus.
2. Wählen Sie im Reiter **Stable** oder in einem anderen Reiter neben der Firmware-Version, die Sie herunterladen möchten, **Download for common upgrade and uboot** aus.

## 3. Die Firmware hochladen

Die folgenden Anweisungen beschreiben das Hochladen Ihrer Firmware über das Admin-Panel des Routers. (Wenn Sie Ihre Firmware über die GL.iNet-App hochladen möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/) und richten Sie sie ein.)

1. Geben Sie in einem Webbrowser die URL zum Admin-Panel Ihres Routers ein (z. B. 192.168.8.1) und melden Sie sich an.
2. (Optional) Wenn Sie Ihre aktuellen Einstellungen sichern möchten, folgen Sie den unten stehenden Schritten.

    ??? "Ihre aktuellen Einstellungen sichern"

        a. Klicken Sie in der linken Seitenleiste auf **SYSTEM** > **Advanced Settings**.

        b. Klicken Sie auf den Link oder die Schaltfläche **Go To LuCI**, um die LuCI-Anmeldeseite aufzurufen.

        c. Geben Sie das Admin-Passwort ein und klicken Sie dann auf **Log in**.

        d. Klicken Sie auf **System** > **Backup / Flash Firmware**.

        e. Klicken Sie unter **Backup** auf **Generate archive**. Eine Datei mit Ihren aktuellen Einstellungen wird auf Ihr Gerät heruntergeladen.

        **Bitte beachten Sie, dass diese Datei nur für die Firmware-Version zum Zeitpunkt der Sicherung gilt und nicht für andere Firmware-Versionen.**

3. Klicken Sie in der linken Seitenleiste auf **SYSTEM** > **Upgrade**.
4. Klicken Sie auf **Local Upgrade** und wählen Sie die Datei aus, die Sie zuvor heruntergeladen haben.
5. Wenn Sie Ihre aktuellen Einstellungen behalten möchten (z. B. das Admin-Passwort Ihres Routers), schalten Sie **Keep Settings** ein.
6. Klicken Sie auf **Install**.

**Hinweis:** Schalten Sie den Router während des Upgrade-Vorgangs nicht aus. Nach Abschluss des Upgrades wird der Anmeldebildschirm des Routers angezeigt.

Wenn Ihre Router-Einstellungen während des Firmware-Updates verloren gegangen sind, stellen Sie Ihre Router-Einstellungen wieder her.

Wenn die obige Methode nicht funktioniert, versuchen Sie, die Firmware über [U-boot](../faq/debrick.md) zu aktualisieren.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
