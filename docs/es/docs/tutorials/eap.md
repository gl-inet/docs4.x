# Conectar routers GL.iNet a una red EAP

Algunos routers GL.iNet admiten la conexión a redes Wi-Fi EAP, Extensible Authentication Protocol.

EAP es un marco de autenticación utilizado habitualmente con **autenticación 802.1X** para redes **WPA2‑Enterprise / WPA3‑Enterprise**. Un ejemplo típico es **eduroam**, un servicio global de itinerancia Wi-Fi para educación e investigación que se basa en 802.1X y EAP.

Esta guía presenta dos formas de conectar routers GL.iNet a una red Wi-Fi EAP: mediante el Admin Panel y mediante LuCI.

## Modelos compatibles

??? "Modelos compatibles" - GL-MT3600BE (Beryl 7) - GL-E5800 (Mudi 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-B3000 (Marble) - GL-AX1800 (Flint) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus) - GL-XE300 (Puli) - GL-E750/GL-E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-AR750 (Creta) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus) - GL-X300B (Collie) - ※GL-MT6000 (Flint 2) - ※GL-MT3000 (Beryl AX) - ※GL-SFT1200 (Opal)

    **Nota:**

    1. GL-MT6000 (Flint 2) y GL-MT3000 (Beryl AX) no admiten la conexión a redes EAP con el firmware predeterminado instalado, pero GL.iNet proporciona firmware nativo OpenWrt 24 para estos modelos, que puede instalarse para habilitar la conexión a redes EAP. Busque el modelo en el [Download Center](https://dl.gl-inet.com/){target="_blank"} y vaya a la pestaña OPENWRT 24 para obtener más detalles.

    2. GL-SFT1200 (Opal) admite la conexión a redes EAP con firmware v4.8.

??? "Modelos no compatibles" - GL-MT5000 (Brume 3) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT1300 (Beryl) - GL-MT300N-V2 (Mango)

## Conectar mediante el panel de administración web

1. Inicie sesión en el panel de administración web, vaya a **INTERNET** -> **Repeater** y haga clic en **Connect**.

   ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

   Se escanearán las redes disponibles. Busque y seleccione el SSID EAP al que desea conectarse.

   ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

   O bien haga clic en **Join Other Network** en la esquina superior derecha para unirse manualmente a la red EAP.

   ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Introduzca el **SSID**.

   ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Seleccione **Security** como WPA/WPA2/WPA3 Enterprise.

   ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Introduzca **Username** y **Password**, y luego haga clic en **Apply** para conectarse.

   ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Conectar mediante LuCI

El panel de administración web de GL.iNet solo admite un número limitado de tipos EAP.

Si la red EAP de destino no puede conectarse mediante el panel de administración web, intente conectarse mediante la interfaz LuCI.

1. Inicie sesión en el panel de administración web y vaya a **SYSTEM** -> **Advanced Settings**. Instale LuCI y haga clic en **Go to LuCI**.

   ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Inicie sesión en la interfaz LuCI con la misma contraseña de administrador y vaya a Network -> Wireless.

   ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Haga clic en **Scan** en la sección 2.4G o 5G.

   ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Únase a la red que desee.

   ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Solución de problemas

Si la red EAP de destino requiere parámetros adicionales, como el tipo EAP, por ejemplo PEAP, TTLS, sufijo de dominio, identity, anonymous identity, etc., la conexión EAP mediante el panel de administración web puede fallar.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connection_failed.png){class="glboxshadow"}

Siga los pasos siguientes para conectar su router GL.iNet a redes EAP que requieren configuración avanzada mediante la interfaz LuCI.

1.  Obtenga la configuración.

    Obtenga con antelación los parámetros de configuración de la red EAP de destino. Por ejemplo:
    - EAP Type, por ejemplo PEAP, TTLS o TLS
    - Sufijo de dominio de autenticación, por ejemplo @company.com
    - Identity, normalmente el nombre de usuario completo
    - Anonymous Identity, opcional
    - Tipo de autenticación interna, por ejemplo MSCHAPv2 o PAP
    - Certificado CA, si es necesario, prepare un archivo en formato .crt

    Este es un ejemplo de la red Wi-Fi Xfinity Mobile como referencia.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2.  Inicie sesión en LuCI.

    Inicie sesión en el panel de administración web del router. Después de iniciar sesión, si antes intentó conectarse a la red EAP de destino mediante la WebGUI y falló, cancele la conexión.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/abort_connection.png){class="glboxshadow"}

    A continuación, vaya a **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Inicie sesión en LuCI con la misma contraseña de administrador.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3.  Configure el repetidor en LuCI.

    En la interfaz LuCI, vaya a Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless.png){class="glboxshadow"}

    Haga clic en el botón **Scan** en la sección 5G o 2.4G para buscar redes Wi-Fi disponibles.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_scan.png){class="glboxshadow"}

    Busque la red EAP de destino en los resultados del escaneo y haga clic en **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/scan_results.png){class="glboxshadow"}

    En la página "Joining Network", introduzca la **WPA passphrase** y haga clic en **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/joining_network.png){class="glboxshadow"}

    Se le dirigirá a la configuración de Wireless Client.

4.  Vaya a **Interface Configuration** -> **Wireless Security**.

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security.jpg){class="glboxshadow"}

    Seleccione o introduzca los parámetros de configuración correctos según su red EAP de destino, como se muestra a continuación. **Todavía no haga clic en Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security_example.png){class="glboxshadow"}

5.  Cambie a la pestaña **Advanced Settings**, especifique un nombre de interfaz, como **wlan0**, y después haga clic en **Save** en la esquina inferior derecha.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/advanced_settings.png){class="glboxshadow"}

6.  Volverá a la página Wireless, que mostrará cambios pendientes. Haga clic en el botón **Save & Apply** en la esquina inferior derecha.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/save_apply.png){class="glboxshadow"}

    Su router quedará conectado correctamente a la red EAP de destino.

7.  Verifique la conexión.

    ??? "Comprobar la conexión en la WebGUI"

        Una vez que el router se conecte correctamente a la red EAP de destino, se iluminará un icono de repetidor en la WebGUI, como se muestra a continuación.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connected_status.png){class="glboxshadow"}

        **Nota**: Como la configuración de LuCI no se sincroniza con la de la WebGUI, los detalles de la interfaz del repetidor, por ejemplo IP conectada, gateway, etc., no aparecerán en la WebGUI.

        Como se muestra en la imagen, la sección del repetidor en la parte inferior está en blanco. Sin embargo, el router ya se ha conectado a la red EAP de destino como repetidor, porque el icono del repetidor en la parte superior está iluminado.

    ??? "Comprobar la conexión mediante SSH"

        1. Inicie sesión en su router por [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"}.

        2. Introduzca **ifconfig** y pulse Enter.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig.png){class="glboxshadow"}

            Podrá comprobar el estado de la interfaz **wlan0**.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig_2.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
