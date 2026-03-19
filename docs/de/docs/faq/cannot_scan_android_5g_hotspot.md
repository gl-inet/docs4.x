# Android 5G-Hotspot kann nicht gefunden werden

Die Verbindung eines GL.iNet Routers als Repeater mit dem 5G-Hotspot eines Android-Smartphones ist eine der gängigen Möglichkeiten, auf das Internet zuzugreifen.

Wenn der 5G-Hotspot Ihres Android-Smartphones jedoch nicht gefunden wird, kann dies mit dem WLAN-Ländercode zusammenhängen.

Bei einigen Android-Smartphones ist der 5G-Hotspot standardmäßig auf einen US-Kanal eingestellt. Wenn Ihr GL.iNet Router ursprünglich nicht in den USA gekauft wurde, kann dieses Problem auftreten.

Sie können den WLAN-Ländercode Ihres GL.iNet Routers auf der LuCI-Seite wie unten beschrieben ändern.

## Schritt 1. Bei LuCI anmelden

Melden Sie sich an Ihrem GL.iNet Router an und wählen Sie in der linken Seitenleiste **SYSTEM -> Advanced Settings -> Go to LuCI**. Melden Sie sich dann in LuCI mit demselben Admin-Passwort an.

## Schritt 2. WLAN-Einstellungen bearbeiten

Gehen Sie zu **Network -> Wireless**, wählen Sie das 5G-WLAN aus und bearbeiten Sie es. Wenn Sie einen GL-MT3000 verwenden, gehen Sie zu **Network -> MTK Wi-Fi**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

![mtkwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/mtkwifi.jpg){class="glboxshadow"}

## Schritt 3. US als Ländercode auswählen

Unter **Device Configuration -> Advanced Settings** wählen Sie für Ihr 5GHz-WLAN als Ländercode US (United States) aus.

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

Klicken Sie vor dem Abmelden auf **Save & Apply**.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

Versuchen Sie anschließend erneut, den 5G-Hotspot Ihres Android-Smartphones zu suchen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
