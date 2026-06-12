# Android 5G-Hotspot kann nicht gefunden werden

Die Verbindung eines GL.iNet Routers als Repeater mit dem 5G-Hotspot eines Android-Smartphones ist eine der gängigen Möglichkeiten, auf das Internet zuzugreifen.

Wenn der 5G-Hotspot Ihres Android-Smartphones jedoch nicht gefunden wird, kann dies mit dem WLAN-Kanal zusammenhängen.

Bei einigen Android-Smartphones ist der 5G-Hotspot standardmäßig auf einen US-Kanal eingestellt. Wenn Ihr GL.iNet Router ursprünglich nicht in den USA gekauft wurde, kann dieses Problem auftreten.

Sie können den WLAN-Ländercode Ihres GL.iNet Routers in der LuCI-Oberfläche wie folgt anpassen.

1. Melden Sie sich an Ihrem GL.iNet Router an und gehen Sie zu **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Melden Sie sich in LuCI mit demselben Admin-Passwort an.

2. Bearbeiten Sie die WLAN-Einstellungen.

    Gehen Sie zu **Network** -> **Wireless**, suchen Sie das 5G-WLAN und klicken Sie rechts auf **Edit**.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. Wählen Sie US als Ländercode aus.

    Klicken Sie auf der Seite Wireless unter **Device Configuration** auf den Tab **Advanced Settings**. Wählen Sie für Ihr 5GHz-WLAN als Ländercode US (United States) aus.

    ![5gus](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. Klicken Sie vor dem Abmelden auf **Save & Apply**.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    Versuchen Sie anschließend erneut, den 5G-Hotspot Ihres Android-Smartphones zu suchen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
