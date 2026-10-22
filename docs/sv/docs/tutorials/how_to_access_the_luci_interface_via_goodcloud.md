# Öppna LuCI-gränssnittet via GoodCloud {#how-to-access-the-luci-interface-via-goodcloud}

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} överbryggar geografiska begränsningar och gör det enkelt att fjärrhantera routern. Via GoodCloud kan du öppna routerns LuCI-gränssnitt när och var som helst, göra olika inställningar på routern och enkelt hantera nätverket.

## Förberedelser {#preparation}

- Maskinvara: En GL.iNet-router som har konfigurerats med internetåtkomst och fungerar normalt.
- Nätverksmiljö: Nätverket som routern är ansluten till är stabilt och har normal internetåtkomst.
- Enhetskoppling: [Koppla GL.iNet-routern till ditt GoodCloud-konto](../interface_guide/cloud.md#bind-devices-to-cloud). Om du inte har ett GoodCloud-konto kan du [registrera](https://www.goodcloud.xyz/){target="_blank"} ett.

## Steg för att öppna LuCI-gränssnittet via GoodCloud {#steps-to-access-the-luci-interface-via-goodcloud}

### För firmwareversion 4.7 och senare {#for-firmware-version-47-or-above}

Från och med v4.7 kan användare öppna LuCI-sidan direkt från GoodCloud-plattformen utan att gå via routerns webbadministrationspanel.

1. Logga in på ditt GoodCloud-konto [här](https://www.goodcloud.xyz/){target="_blank"}.

2. Gå till **Devices** -> **Bound Devices** till vänster och klicka på namnet på enheten som du vill öppna. Ikonerna för Remote Web Access visas.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    Dialogrutan visar port 80. Ändra porten till **8080** och klicka på Apply.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Du omdirigeras till LuCI:s inloggningssida. Ange administratörslösenordet och logga in.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. Du har nu loggat in på LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### För firmwareversion 4.6 och tidigare {#for-firmware-version-46-or-below}

1. Logga in på ditt GoodCloud-konto [här](https://www.goodcloud.xyz/){target="_blank"}.

2. Gå till **Devices** -> **Bound Devices** till vänster och klicka på namnet på enheten som du vill öppna. Ikonerna för Remote Web Access visas.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    Dialogrutan visar port 80. Klicka på Apply.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Du omdirigeras till GL.iNets inloggningssida för administrationspanelen. Ange administratörslösenordet och logga in.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. När du har loggat in går du till SYSTEM -> Advanced Settings till vänster och klickar på länken till LuCI-gränssnittet.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Du omdirigeras till LuCI:s inloggningssida. Ange samma administratörslösenord och logga in.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. Du har nu loggat in på LuCI.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
