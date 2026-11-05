# Conectar routers GL.iNet a una red EAP {#connect-glinet-routers-to-an-eap-network}

Algunos routers GL.iNet admiten la conexión a redes Wi-Fi EAP (Extensible Authentication Protocol) como repetidores.

EAP es un marco de autenticación utilizado habitualmente con **autenticación 802.1X** para redes **WPA2‑Enterprise / WPA3‑Enterprise**. Un ejemplo típico es **eduroam**, un servicio global de itinerancia Wi‑Fi para educación e investigación que se basa en 802.1X y EAP.

Existen varios métodos de autenticación EAP para este marco, incluidos EAP-PEAP, EAP-TLS, EAP-TTLS y EAP-FAST. Tenga en cuenta que no todos los métodos EAP son compatibles con todas las interfaces y modelos de router.

Esta guía presenta dos formas de conectar routers GL.iNet a una red Wi-Fi EAP: mediante el panel de administración web de GL.iNet y mediante LuCI. Estas dos formas ofrecen distintos métodos de autenticación EAP: la primera solo ofrece **EAP-PEAP**, mientras que la segunda ofrece **EAP-TLS**, **EAP-TTLS**, **EAP-PEAP** y **EAP-FAST**.

Algunos routers GL.iNet solo admiten la función de repetidor EAP mediante una de estas dos formas. Consulte los modelos compatibles a continuación.

### Modelos compatibles {#supported-models}

??? "Modelos compatibles"
    - <u>GL-MG1300 (Mango 2)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-AX1800 (Flint)</u><sup>1</sup>
    - <u>GL-AXT1800 (Slate AX)</u><sup>1</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - <u>GL-E750/GL-E750V2 (Mudi)</u><sup>1</sup>
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

    ---

    **Nota**:

    1. GL-MG1300 (Mango 2), GL-AX1800 (Flint), GL-AXT1800 (Slate AX) y GL-E750/GL-E750V2 (Mudi) pueden conectarse como repetidores a redes EAP-PEAP mediante el panel de administración web de GL.iNet y a redes EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST mediante LuCI.

    2. GL-MT6000 (Flint 2) y GL-MT3000 (Beryl AX) no admiten la conexión a redes EAP como repetidores con el firmware predeterminado. Sin embargo, GL.iNet proporciona firmware OpenWrt compatible con EAP para estos modelos. Tras instalar este firmware, puede configurar el router en modo repetidor y conectarlo a redes EAP-PEAP mediante el panel de administración web de GL.iNet o a redes EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST mediante LuCI.

        Busque su modelo en el [Download Center](https://dl.gl-inet.com/){target="_blank"} y seleccione la pestaña OpenWrt para descargarlo si es necesario.

    3. GL-SFT1200 (Opal) admite la conexión a redes EAP como repetidor a partir del firmware v4.8, tanto mediante el panel de administración web de GL.iNet (EAP-PEAP) como mediante LuCI (EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST).

    4. Todos los demás modelos indicados arriba solo admiten la conexión a redes EAP-PEAP como repetidores mediante el panel de administración web de GL.iNet. Otros métodos EAP (EAP-TLS, EAP-TTLS, EAP-FAST, etc.) no son compatibles.

??? "Modelos no compatibles"
    - GL-MT6000 (Fortify)
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Conectar mediante el panel de administración web {#connect-via-web-admin-panel}

Mediante el panel de administración web de GL.iNet, puede conectar su router a redes EAP-PEAP como repetidor.

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

## Conectar mediante LuCI {#connect-via-luci}

Mediante LuCI, puede conectar su router a una red EAP-TLS, EAP-TTLS, EAP-PEAP o EAP-FAST como repetidor.

Los siguientes pasos son solo de referencia. Consulte la página LuCI de su dispositivo.

1. Inicie sesión en el panel de administración web, vaya a **SYSTEM** -> **Advanced Settings**. Instale LuCI y haga clic en **Go to LuCI**.

   ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Inicie sesión en la interfaz LuCI con la misma contraseña de administrador y vaya a Network -> Wireless.

   ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Haga clic en **Scan** en la sección 2.4G o 5G.

   ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Únase a la red que desee.

   ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Solución de problemas {#troubleshooting}

Si la red EAP de destino requiere parámetros adicionales, como el tipo EAP (por ejemplo, PEAP, TTLS), sufijo de dominio, identity, anonymous identity, etc., la conexión EAP mediante el panel de administración web puede fallar.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

Siga los pasos siguientes para conectar su router GL.iNet a redes EAP que requieren configuración avanzada mediante la interfaz LuCI.

1.  Obtenga la configuración.

    Obtenga con antelación los parámetros de configuración de la red EAP de destino. Por ejemplo:
    - Tipo EAP (por ejemplo, PEAP, TTLS, TLS)
    - Sufijo de dominio de autenticación (por ejemplo, @company.com)
    - Identity (normalmente el nombre de usuario completo)
    - Anonymous Identity (opcional)
    - Tipo de autenticación interna (por ejemplo, MSCHAPv2, PAP)
    - Certificado CA (si es necesario, prepare un archivo en formato .crt)

    Este es un ejemplo de la red Wi‑Fi Xfinity Mobile como referencia.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2.  Inicie sesión en LuCI.

    Inicie sesión en el panel de administración web del router. Después de iniciar sesión, si antes intentó conectarse a la red EAP de destino mediante la WebGUI y falló, cancele la conexión.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    A continuación, vaya a **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Inicie sesión en LuCI con la misma contraseña de administrador.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3.  Configure el repetidor en LuCI.

    En la interfaz LuCI, vaya a Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    Haga clic en el botón **Scan** en la sección 5G o 2.4G para buscar redes Wi‑Fi disponibles.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    Busque la red EAP de destino en los resultados del escaneo y haga clic en **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    En la página "Joining Network", introduzca la **WPA passphrase** y haga clic en **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    Se le dirigirá a la configuración de Wireless Client.

4.  Vaya a **Interface Configuration** -> **Wireless Security**.

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    Seleccione o introduzca los parámetros de configuración correctos según su red EAP de destino, como se muestra a continuación. **Todavía no haga clic en Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5.  Cambie a la pestaña **Advanced Settings**, especifique un nombre de interfaz, como **wlan0**, y después haga clic en **Save** en la esquina inferior derecha.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6.  Volverá a la página Wireless, que mostrará cambios pendientes. Haga clic en el botón **Save & Apply** en la esquina inferior derecha.

    ![save and apply](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    Su router quedará conectado correctamente a la red EAP de destino.

7.  Verifique la conexión.

    ??? "Comprobar la conexión en la WebGUI"

        Una vez que el router se conecte correctamente a la red EAP de destino, se iluminará un icono de repetidor en la WebGUI, como se muestra a continuación.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Nota**: Como la configuración de LuCI no se sincroniza con la de la WebGUI, los detalles de la interfaz del repetidor (por ejemplo, IP conectada, gateway, etc.) no aparecerán en la WebGUI.

        Como se muestra en la imagen, la sección del repetidor en la parte inferior está en blanco. Sin embargo, el router ya se ha conectado a la red EAP de destino como repetidor, porque el icono del repetidor en la parte superior está iluminado.

    ??? "Comprobar la conexión mediante SSH"

        1. Inicie sesión en su router por [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"}.

        2. Introduzca **ifconfig** y pulse Enter.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            Podrá comprobar el estado de la interfaz **wlan0**.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
