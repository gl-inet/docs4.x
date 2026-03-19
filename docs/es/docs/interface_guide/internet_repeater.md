# Conectarse a Internet mediante una red Wi-Fi existente con Repeater

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Usar Repeater significa conectar el router a otra red inalámbrica existente, por ejemplo cuando utiliza Wi-Fi gratuito en un hotel o una cafetería.

Funciona en modo WISP (Wireless Internet Service Provider) de forma predeterminada, lo que significa que el router creará su propia subred y actuará como firewall para protegerle de la red pública.

## Pasos básicos

Inicie sesión en el panel web de administración del router, vaya a la sección **INTERNET** -> **Repeater** y haga clic en **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Elija en la lista de redes disponibles la red Wi-Fi a la que desea conectarse.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**Nota**: La página muestra los canales Wi-Fi compatibles con su router. Asegúrese de que la red Wi-Fi a la que se está conectando utilice uno de estos canales; de lo contrario, es posible que no aparezca en la lista de redes disponibles.

Introduzca la contraseña Wi-Fi correcta y haga clic en **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Si el SSID Wi-Fi al que desea conectarse no aparece en la lista **Available Network**, haga clic en **Join Other Network** en la esquina superior derecha e introduzca manualmente el SSID Wi-Fi y la otra información necesaria. Consulte [aquí](#join-other-network) para ver los pasos detallados.

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Para conectarse a un hotspot público, como los que ofrecen hoteles, aeropuertos o centros comerciales, consulte [Para hotspot público](#for-public-hotspot).

Para otros ajustes, consulte [Configuración avanzada](#advanced-settings).

Tras un momento, si la contraseña introducida es correcta, la conexión se realizará correctamente.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Para hotspot público {#for-public-hotspot}

Al conectar el router a un hotspot público con portal cautivo, habilitar las siguientes funciones puede ayudar a mejorar la tasa de éxito de la conexión.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

  Esta función está disponible desde la versión v4.6.

  Si esta opción está habilitada, el router entrará automáticamente en **Login Mode for Public Hotspots** cuando se conecte correctamente a un hotspot pero no a Internet. **En este modo, algunos servicios se suspenderán mientras el modo DNS cambia a automático**, lo que puede filtrar su actividad de red al proveedor del hotspot, por ejemplo un hotel o un centro comercial.

  Aunque esta opción no esté habilitada, el router le pedirá entrar en este modo cuando detecte un portal cautivo en el hotspot y no logre iniciar sesión correctamente.

  ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

  Si está habilitado, el router se hará pasar por el dispositivo cliente que utiliza para acceder al panel de administración, emulando la dirección MAC de ese dispositivo.

- **MAC Mode**

  Puede elegir qué MAC utilizará el router para conectarse al hotspot público.
  - **Factory**: Usa la dirección MAC original asignada de fábrica al dispositivo.

  - **Clone**: Clona la dirección MAC de un dispositivo cliente para la conexión. Si la MAC deseada no aparece en la lista, introduzca manualmente la dirección que desea clonar.

    Nota: Muchos dispositivos modernos usan direcciones MAC aleatorias, a menudo llamadas Private Wi-Fi Address o random hardware address, al conectarse a redes Wi-Fi. Debido a ello, la dirección MAC mostrada aquí puede no coincidir con la MAC física real del dispositivo.

  - **Random**: Genera automáticamente una dirección MAC aleatoria para la conexión.

  Al guardar la configuración de red, el **MAC Mode**, incluida cualquier dirección MAC clonada o aleatoria, queda vinculado al SSID específico que guarde. Puede cambiar manualmente estos ajustes para cada SSID en cualquier momento.

- **Auto Update MAC**: Si esta opción está habilitada, la MAC puede actualizarse automáticamente.

## Configuración avanzada {#advanced-settings}

Al unirse a la red, hay algunas opciones adicionales.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

- **Remember**: Habilite esta opción para recordar la red Wi-Fi repetida actual.

- **Lock BSSID**: Cuando está habilitado, el router se conectará solo al punto de acceso específico correspondiente al BSSID seleccionado, incluso cuando otros AP compartan el mismo SSID.

- **Manually Set Static IP**: Cuando está habilitado, puede configurar manualmente una dirección IPv4 fija, netmask, gateway y servidores DNS para la conexión de repetidor del router, en lugar de obtener estos ajustes automáticamente.

  ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

- **TTL**: TTL (Time To Live) establece el tiempo máximo que los paquetes pueden permanecer en la red y se rellena según los requisitos del operador. De forma predeterminada, el router reenvía el TTL del dispositivo cliente entrante menos uno. Si necesita camuflaje, puede establecer aquí un valor fijo. El TTL solo es válido para IPv4.

- **HL**: En IPv6, el campo HL (Hop Limit) se utiliza para limitar el número de saltos de transmisión de los paquetes de datos en la red, lo que equivale al TTL en IPv4.

- **MTU**: El valor predeterminado es 1500.

## Opciones de Repeater

Para ver las opciones de Repeater, haga clic en el icono de engranaje de la esquina superior derecha en la sección Repeater conectada.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**Para firmware v4.8**, la página **Repeater Options** se muestra de la siguiente manera.

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**:
  - No Switching mode: Cuando está habilitado, otras redes guardadas no se conectarán automáticamente cuando se desconecte la Wi-Fi actual.

  - Auto Switching mode: Cuando está habilitado, el router intentará conectarse a otras redes guardadas cuando se desconecte la Wi-Fi actual.

  - Auto Switching Without Network: Cuando está habilitado, el router no escaneará redes automáticamente cuando tenga conexión correcta en un modo distinto de repetidor y solo intentará cambiar automáticamente a otras redes guardadas cuando el router se quede sin red, lo que puede evitar la pérdida de paquetes de comunicación.

- **Band Selection**: puede seleccionar una de estas tres opciones: Auto, 5 GHz y 2.4 GHz.

  Si selecciona manualmente una banda, el router no escaneará ni se conectará a ninguna red Wi-Fi que utilice otra banda.

**Para firmware v4.7 y anteriores**, la página **Repeater Options** se muestra como sigue.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

- **Allow Switching To Other Saved Networks**. Si esta opción está habilitada, el router se conectará automáticamente a otras redes guardadas cuando no pueda conectarse a la red Wi-Fi actual.

- **Band Selection**. Si selecciona manualmente una banda, el router no escaneará ni se conectará a ninguna red Wi-Fi de otra banda.

## Gestionar redes conocidas

Para eliminar una red conocida, haga clic en **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

O haga clic en **Connect** en la sección Repeater si no hay ninguna red conectada.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

En la sección **Known Networks**, haga clic en el icono de papelera para eliminar una red conocida, o en el icono de engranaje para configurarla.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Unirse a otra red {#join-other-network}

Si el SSID no está en la lista **Available Networks**, o si el SSID está oculto, puede hacer clic en **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Introduzca el SSID, seleccione **Security** e introduzca la contraseña, si es necesario.

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

En la configuración de **Security**, hay dos o tres opciones, según el modelo.

- None, lo que significa que no se requiere contraseña.
- WPA/WPA2/WPA3, que es la opción más común y es compatible con casi todas las redes Wi-Fi.
- WPA/WPA2/WPA3 Enterprise, que requiere Extensible Authentication Protocol (EAP) para la autenticación. Se necesita un nombre de usuario y una contraseña válidos para conectarse, normalmente en redes empresariales o universitarias.

  ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

  Para obtener una guía detallada sobre cómo repetir redes EAP, haga clic [aquí](../tutorials/eap.md){target="\_blank"}.

## Reconexión

En los siguientes casos, el router intentará reconectarse automáticamente a la red Wi-Fi de vez en cuando. Puede desactivar esta función manualmente si es necesario. Para errores de SSID o contraseña, elimine la red de **Known Networks** para resolver el problema.

1. Se introdujo un SSID o una contraseña incorrectos durante la configuración de Repeater.

2. El router salió del alcance del router ascendente después de la conexión inicial.

3. El router ascendente cambia el SSID o la contraseña, o restringe el acceso después de la conexión.

El proceso de reconexión tiene tres fases diferenciadas: fase de espera, fase de escaneo y fase de conexión.

1. Fase de espera: no hay incidencias; el router espera a que se cumplan las condiciones de reconexión.

2. Fase de escaneo: puede producirse pérdida de paquetes en la banda de frecuencia escaneada. Los dispositivos nuevos pueden experimentar problemas de conexión. En los modelos GL-AXT1800 y GL-AX1800, la Guest Wi-Fi se desactivará temporalmente.

3. Fase de conexión: la Wi-Fi principal en la banda objetivo puede desconectarse durante unos segundos mientras se restablece.

**Nota**: Los problemas suelen surgir en las fases de escaneo y conexión.

## Solución de problemas

Cuando el router está conectado a una red Wi-Fi como repetidor y no hay acceso a Internet, se mostrará un mensaje amarillo como el siguiente.

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Para solucionar este problema:

1. Compruebe si el dispositivo ascendente, es decir, la red Wi-Fi a la que está conectado el router, tiene acceso a Internet.

2. Vaya a la página [Multi-WAN](multi-wan.md) para comprobar el estado de la interfaz del repetidor.

## DFS

Al conectarse a una red Wi-Fi ascendente de 5 GHz, la Wi-Fi del router seguirá a la red ascendente para usar o no el canal DFS.

- Si la Wi-Fi ascendente usa un canal DFS y puede escanearse, la Wi-Fi de 5 GHz del router usará el mismo canal.

- La Wi-Fi de 5 GHz del router cambiará a un canal no DFS si la Wi-Fi ascendente no puede escanearse o si falla la conexión.

??? "Modelos compatibles"

    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Modelos no compatibles"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Artículos relacionados

- [Página de Internet](internet.md)
- [¿Cómo establecer la prioridad de cada método de acceso a Internet?](multi-wan.md)
- [¿Cómo configurar el equilibrio de carga cuando se utilizan varios métodos de acceso a Internet al mismo tiempo?](multi-wan.md)
- [¿Cómo puedo conocer las direcciones MAC de la LAN y la Wi-Fi?](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
