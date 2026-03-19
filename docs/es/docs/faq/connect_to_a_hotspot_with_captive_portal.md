# Conectar un router GL.iNet a puntos de acceso públicos con portal cautivo

## ¿Qué es un portal cautivo?

Un portal cautivo es una página web en la que los puntos de acceso públicos requieren que los usuarios vean e interactúen con la página antes de que se les conceda acceso a Internet.

## ¿Por qué usar un router para puntos de acceso públicos?

- El Wi-Fi público no es seguro

  Es difícil exagerar los riesgos del Wi-Fi público. Al conectar su router GL.iNet a una red Wi-Fi pública, puede iniciar sesión directamente en su cuenta VPN a través del panel de administración del router. El router cifrará automáticamente todos los dispositivos conectados a la red local, lo que evita tener que configurar una VPN en cada dispositivo.

- Utilizarlo como repetidor para permitir la conexión de varios dispositivos

  Además, algunas redes Wi-Fi públicas, como el Wi-Fi de hotel, limitan el acceso, por ejemplo, a dos dispositivos. Cuando se viaja en grupo, esto resulta poco práctico. En su lugar, puede conectar un router de viaje al Wi-Fi del hotel y usarlo como repetidor para emitir una señal Wi-Fi a todos sus dispositivos, incluidos portátiles, teléfonos inteligentes, tabletas, etc. El Wi-Fi del hotel solo reconocerá el router de viaje como un único dispositivo, pero usted podrá conectar tantos dispositivos como quiera al Wi-Fi gratuito.

## ¿Cómo conectar el router a puntos de acceso públicos con portal cautivo?

Vea este vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Conecte un teléfono inteligente o un ordenador al router.

   Encienda el router. En su teléfono inteligente u ordenador, busque el SSID del router e introduzca la contraseña Wi-Fi. El SSID y la contraseña predeterminados están impresos en la parte inferior del router.

2. Inicie sesión en el panel de administración web del router.

   En su teléfono inteligente u ordenador, abra un navegador web e introduzca la dirección IP del router, IP predeterminada: `192.168.8.1`, en la barra de direcciones. Podrá acceder al panel de administración web del router.

   Si está iniciando sesión por primera vez, seleccione un idioma y cree una contraseña de inicio de sesión para el panel de administración web del router.

3. Conecte su router al punto de acceso público. Consulte el tutorial de [Repeater](../interface_guide/internet_repeater.md/).

## Solución de problemas

Si no puede entrar en el portal cautivo, es posible que el router no pueda acceder a Internet. Pruebe los siguientes métodos de solución de problemas.

### Método 1: Activar Public Hotspot Login Mode y Camouflage

**Nota**: Estas dos funciones solo están disponibles en el firmware v4.6 y posteriores.

Al conectar el router a un punto de acceso público, en la página **Join Network**, habilitar las siguientes funciones puede ayudar a mejorar la tasa de éxito de la conexión.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

  Si esta opción está activada, el router entrará automáticamente en Login Mode for Public Hotspots cuando se conecte correctamente a un punto de acceso, pero no a Internet. En este modo, algunos servicios se suspenderán mientras el modo DNS se cambiará a automático, lo que puede filtrar su actividad de red al proveedor del punto de acceso, por ejemplo, un hotel o un centro comercial.

- Enable Camouflage

  Si está activado, el router se hará pasar por el dispositivo cliente que utiliza para acceder al panel de administración emulando la dirección MAC de ese dispositivo.

---

### Método 2: Cambiar la configuración del router

1. Inicie sesión en el panel de administración web y vaya a NETWORK -> DNS. Asegúrese de que **DNS Rebinding Attack Protection** esté desactivado y de que **Mode** esté configurado en **Automatic**.

   ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. En el panel de administración web, vaya a VPN -> VPN Dashboard. Asegúrese de que todas las conexiones VPN estén desactivadas.

   **Para firmware v4.7 y anteriores**, la página se muestra como se indica a continuación.

   ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}

   **Para firmware v4.8 y superior**, la página se muestra como se indica a continuación.

   ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. En el panel de administración web, vaya a APPLICATIONS -> AdGuard Home. Asegúrese de que AdGuard Home esté desactivado.

   ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Abra un navegador web y vuelva a introducir o actualizar la página del portal cautivo. Espere un minuto y compruebe si se redirige automáticamente a la página de autenticación del portal cautivo.

   Si está usando un teléfono inteligente y el navegador no redirige al portal cautivo, apague el Wi-Fi del teléfono y vuelva a encenderlo; después, vuelva a conectarse al Wi-Fi del router. El portal cautivo debería aparecer directamente después de introducir la contraseña Wi-Fi.

   ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Método 3: Clonación de MAC

Algunos hoteles limitan la cantidad de dispositivos que cada cliente puede conectar al Wi-Fi del hotel reconociendo sus direcciones MAC, y registran la dirección MAC del dispositivo cuando se conecta por primera vez. En este caso, puede clonar en el router la dirección MAC que su teléfono utiliza para conectarse al Wi-Fi del hotel, permitiendo que el router use esa dirección MAC para acceder al Wi-Fi del hotel.

1. Conecte su teléfono al Wi-Fi del hotel. Busque la dirección MAC que su teléfono utiliza para conectarse al Wi-Fi del hotel.

   Aquí tiene un ejemplo para iPhone, iOS 16.1.2: vaya a Settings -> Wi-Fi -> seleccione el Wi-Fi del hotel y encontrará la Wi-Fi Address. Anote esta dirección.

   ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

   En algunos modelos antiguos, la dirección MAC puede no estar disponible en la configuración de Wi-Fi. En ese caso, el dispositivo puede usar su dirección MAC real al conectarse a redes Wi-Fi públicas, que puede encontrarse en Settings > About de su teléfono, o "About Phone".

2. Conecte su teléfono u ordenador al router. Inicie sesión en el panel de administración web del router y, a continuación, clone o introduzca manualmente esta dirección MAC.

   **Para firmware v4.5 y anteriores**, seleccione NETWORK en el lado izquierdo -> MAC Address.

   Seleccione Manual Mode, introduzca la dirección MAC obtenida en el paso 1 y haga clic en Apply.

   ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

   **Para firmware v4.6 y superior**, seleccione INTERNET en el lado izquierdo -> sección Repeater y haga clic en Modify.

   ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

   En la ventana emergente, cambie MAC Mode a Clone, introduzca manualmente la dirección MAC y haga clic en Apply.

   ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. Puede ser necesario reiniciar el router para que los cambios surtan efecto.

---

### Método 4: Pedir ayuda al personal del hotel

Algunos hoteles tienen políticas de verificación muy estrictas para sus redes. Si ninguno de los métodos anteriores funciona, intente pedir al personal del hotel que agregue directamente la dirección MAC de su router, use la dirección MAC predeterminada de fábrica, no una aleatoria, a la lista blanca de la red del hotel.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
