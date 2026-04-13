# Jak uzyskać dostęp do interfejsu LuCI przez GoodCloud

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} przełamuje ograniczenia geograficzne i zapewnia wygodny sposób zdalnego zarządzania routerem. Przez GoodCloud możesz uzyskać dostęp do interfejsu LuCI routera w dowolnym czasie i miejscu, wykonywać różne ustawienia na routerze i łatwo zarządzać siecią.

## Przygotowanie

- Sprzęt: Router GL.iNet skonfigurowany z dostępem do Internetu i działający normalnie.
- Środowisko sieciowe: Sieć, do której podłączony jest router, jest stabilna i może normalnie uzyskać dostęp do Internetu.
- Powiązanie urządzenia: Musisz [powiązać router GL.iNet z kontem GoodCloud](../interface_guide/cloud.md/#setup-your-goodcloud-account). Jeśli nie masz konta GoodCloud, [zarejestruj](https://www.goodcloud.xyz/){target="_blank"} je.

## Kroki dostępu do interfejsu LuCI przez GoodCloud

### Dla firmware w wersji 4.7 lub nowszej

Począwszy od v4.7, użytkownicy mogą bezpośrednio uzyskać dostęp do strony LuCI z platformy GoodCloud bez przechodzenia przez panel administratora routera.

1. Zaloguj się do swojego konta GoodCloud [tutaj](https://www.goodcloud.xyz/){target="_blank"}.

2. Po lewej stronie -> **Devices** -> **Bound Devices**, kliknij nazwę urządzenia, do którego chcesz uzyskać dostęp, a następnie zobaczysz ikony Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    Wyskakujące okno wyświetla port 80. Zmień port na **8080**, kliknij Apply.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Zostaniesz przekierowany do strony logowania LuCI. Wprowadź hasło administratora, aby się zalogować.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. Pomyślnie zalogowano do LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}    

### Dla firmware w wersji 4.6 lub starszej

1. Zaloguj się do swojego konta GoodCloud [tutaj](https://www.goodcloud.xyz/){target="_blank"}.

2. Po lewej stronie -> **Devices** -> **Bound Devices**, kliknij nazwę urządzenia, do którego chcesz uzyskać dostęp, a następnie zobaczysz ikony Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    Wyskakujące okno wyświetla port 80, kliknij Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Zostaniesz wtedy przekierowany do strony logowania do panelu administratora GL.iNet. Wprowadź hasło administratora, aby się zalogować.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. Po zalogowaniu, po lewej stronie -> SYSTEM -> Advanced Settings, kliknij hiperłącze, aby przejść do interfejsu LuCI.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Zostaniesz przekierowany do strony logowania LuCI. Wprowadź to samo hasło administratora, aby się zalogować.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. Pomyślnie zalogowano do LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.