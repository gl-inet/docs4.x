# De LuCI-interface via GoodCloud openen {#how-to-access-the-luci-interface-via-goodcloud}

Met GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} kun je routers op afstand beheren. Via GoodCloud open je de LuCI-interface overal om instellingen te wijzigen en het netwerk te beheren.

## Preparation {#preparation}

- Hardware: een werkende GL.iNet-router met internetverbinding.
- Netwerkomgeving: een stabiel netwerk met normale internettoegang.
- Apparaatkoppeling: [koppel je GL.iNet-router aan GoodCloud](../interface_guide/cloud.md#bind-devices-to-cloud). [Registreer](https://www.goodcloud.xyz/){target="_blank"} zo nodig eerst een account.

## Stappen om LuCI via GoodCloud te openen {#steps-to-access-the-luci-interface-via-goodcloud}

### For Firmware Version 4.7 or Above {#for-firmware-version-47-or-above}

Vanaf v4.7 kun je LuCI rechtstreeks via GoodCloud openen zonder het webbeheerpaneel van de router.

1. Log in to your GoodCloud account [here](https://www.goodcloud.xyz/){target="_blank"}.

2. Ga links naar **Devices** -> **Bound Devices** en klik op de naam van het apparaat. De pictogrammen voor Remote Web Access verschijnen.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    Het pop-upvenster toont poort 80. Wijzig deze in **8080** en klik op Apply.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Je wordt naar de LuCI-aanmeldpagina geleid. Voer je beheerderswachtwoord in.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. You have successfully logged in to LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### For Firmware Version 4.6 or Below {#for-firmware-version-46-or-below}

1. Log in to your GoodCloud account [here](https://www.goodcloud.xyz/){target="_blank"}.

2. Ga links naar **Devices** -> **Bound Devices** en klik op de naam van het apparaat. De pictogrammen voor Remote Web Access verschijnen.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    Het pop-upvenster toont poort 80. Klik op Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Je wordt naar de aanmeldpagina van het GL.iNet-beheerpaneel geleid. Voer je beheerderswachtwoord in.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. Ga na aanmelding links naar SYSTEM -> Advanced Settings en klik op de link naar LuCI.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Je wordt naar LuCI geleid. Meld je aan met hetzelfde beheerderswachtwoord.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. You have successfully logged in to LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
