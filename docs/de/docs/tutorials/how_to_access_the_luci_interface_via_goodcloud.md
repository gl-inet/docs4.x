# So greifen Sie über GoodCloud auf die LuCI-Oberfläche zu

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} überwindet geografische Einschränkungen und bietet eine praktische Möglichkeit zur Remote-Verwaltung von Routern. Über GoodCloud können Sie jederzeit und von überall auf die LuCI-Oberfläche des Routers zugreifen, verschiedene Einstellungen am Router vornehmen und das Netzwerk einfach verwalten.

## Vorbereitung

- Hardware: Ein GL.iNet-Router, der mit dem Internet verbunden wurde und ordnungsgemäß funktioniert.
- Netzwerkumgebung: Das Netzwerk, mit dem der Router verbunden ist, ist stabil und hat normalen Internetzugang.
- Gerätebindung: Sie müssen [Ihren GL.iNet-Router mit Ihrem GoodCloud-Konto verknüpfen](../interface_guide/cloud.md/#setup-your-goodcloud-account). Wenn Sie noch kein GoodCloud-Konto haben, [registrieren](https://www.goodcloud.xyz/){target="_blank"} Sie sich bitte.

## Schritte für den Zugriff auf die LuCI-Oberfläche über GoodCloud

### Für Firmware-Version 4.7 oder höher

Ab v4.7 können Benutzer direkt über die GoodCloud-Plattform auf die LuCI-Seite zugreifen, ohne den Web-Adminbereich des Routers aufzurufen.

1. Melden Sie sich [hier](https://www.goodcloud.xyz/){target="_blank"} bei Ihrem GoodCloud-Konto an.

2. Gehen Sie auf der linken Seite zu **Devices** -> **Bound Devices**. Klicken Sie auf den Namen des Geräts, auf das Sie zugreifen möchten. Danach werden die Symbole für **Remote Web Access** angezeigt.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    Im Pop-up-Fenster wird Port 80 angezeigt. Ändern Sie den Port auf **8080** und klicken Sie auf **Apply**.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Sie werden zur LuCI-Anmeldeseite weitergeleitet. Geben Sie Ihr Admin-Passwort ein, um sich anzumelden.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. Sie haben sich erfolgreich bei LuCI angemeldet.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}    

### Für Firmware-Version 4.6 oder niedriger

1. Melden Sie sich [hier](https://www.goodcloud.xyz/){target="_blank"} bei Ihrem GoodCloud-Konto an.

2. Gehen Sie auf der linken Seite zu **Devices** -> **Bound Devices**. Klicken Sie auf den Namen des Geräts, auf das Sie zugreifen möchten. Danach werden die Symbole für **Remote Web Access** angezeigt.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    Im Pop-up-Fenster wird Port 80 angezeigt. Klicken Sie auf **Apply**.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Anschließend werden Sie zur Anmeldeseite des GL.iNet-Adminbereichs weitergeleitet. Geben Sie Ihr Admin-Passwort ein, um sich anzumelden.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. Klicken Sie nach der Anmeldung links auf **SYSTEM** -> **Advanced Settings** und dann auf den Hyperlink, um zur LuCI-Oberfläche zu gelangen.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Sie werden zur LuCI-Anmeldeseite weitergeleitet. Geben Sie dasselbe Admin-Passwort ein, um sich anzumelden.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. Sie haben sich erfolgreich bei LuCI angemeldet.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
