# Configuración inicial

La configuración inicial de los routers GL.iNet es muy similar. La mayoría de los modelos tienen un módulo Wi-Fi, mientras que algunos no.

Por ello, la siguiente guía se divide en dos casos según la presencia o no de un módulo Wi-Fi.

- [Para modelos que tienen Wi-Fi](#para-modelos-que-tienen-wi-fi)
- [Para modelos que no tienen Wi-Fi](#para-modelos-que-no-tienen-wi-fi)

## Para modelos que tienen Wi-Fi

Aquí se utiliza como ejemplo el GL-AXT1800, Slate AX.

Prepare los siguientes elementos incluidos en el paquete.

- GL-AXT1800
- Un adaptador de corriente
- Un cable Ethernet

Vea esta guía en vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>Este vídeo utiliza un router GL.iNet diferente para demostrar la configuración, ya que los pasos son los mismos para la mayoría de los modelos de router.</small>

1. Encendido

   Si desea usar una tarjeta TF, insértela antes de encender el router. No se admite el intercambio en caliente de tarjetas TF.

   Conecte un extremo del adaptador de corriente al router y el otro a una toma de corriente. El router se encenderá automáticamente.

2. Conectarse al router

   Puede conectarse al router mediante cable Ethernet o por Wi-Fi.
   - Conexión por cable

     Conecte su ordenador al puerto LAN del router mediante un cable Ethernet.

   - Conexión por Wi-Fi

     El SSID de Wi-Fi está impreso en la etiqueta inferior del router en alguno de los siguientes formatos:

     **GL-AXT1800-XXX** o **GL-AXT1800-XXX-5G**

     La Wi-Fi Key predeterminada se encuentra debajo del SSID.

     Busque el SSID del router en su ordenador, teléfono o tableta e introduzca la Wi-Fi Key. En algunos modelos, si la contraseña Wi-Fi no aparece en la etiqueta, pruebe con "**goodlife**".

     **Consejo:** El código QR de la etiqueta inferior contiene la información Wi-Fi predeterminada. Puede conectarse rápidamente escaneándolo con el lector de códigos QR de su teléfono.

     **Nota:** Después de conectarse al Wi-Fi, es posible que no tenga acceso inmediato a Internet. Siga el siguiente paso para configurar primero su red antes de acceder a Internet.

3. Iniciar sesión en el panel de administración web

   Abra un navegador web, recomendamos Chrome, Edge o Safari, y visite [http://192.168.8.1](http://192.168.8.1). Será dirigido a la configuración inicial del panel de administración web.

   Si no puede acceder al panel de administración web, consulte [aquí](cannot_access_web_admin_panel.md).

   Elija un idioma y haga clic en **Next** para continuar.

   ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

   Configure la contraseña de administrador. Recomendamos usar una contraseña segura. Haga clic en **Apply** para continuar.

   **Nota**: El Wi-Fi puede apagarse durante la inicialización. Asegúrese de volver a conectarse al router.

   ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

   Después de la configuración inicial, entrará en el panel de administración web del router.

   ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. Conectarse a Internet
   - [Conectarse a Internet mediante un cable Ethernet](../interface_guide/internet_ethernet.md)
   - [Conectarse a Internet mediante una red Wi-Fi existente](../interface_guide/internet_repeater.md)
   - [Conectarse a Internet mediante USB tethering](../interface_guide/internet_tethering.md)
   - [Conectarse a Internet mediante un módem USB](../interface_guide/internet_cellular.md)

## Para modelos que no tienen Wi-Fi

Aquí se utiliza como ejemplo el GL-MT2500A, Brume 2.

1.  Encendido

    Conecte un extremo del adaptador de corriente al router y el otro a una toma de corriente. El router se encenderá automáticamente.

2.  Conectarse al router

    Podemos conectarnos al router mediante un cable Ethernet o mediante Wi-Fi.
    - Conexión directa mediante cable Ethernet

      Conecte su ordenador al puerto LAN del router mediante un cable Ethernet. Este es el método de configuración recomendado porque es simple y directo.

    - Conexión mediante el Wi-Fi de otro router

      Como el GL-MT2500A no tiene un módulo Wi-Fi integrado, podemos usar otro router con capacidad Wi-Fi para inicializar el GL-MT2500A.
      - Método 1: Configure el segundo router en modo AP, Access Point, y luego conecte el puerto LAN del GL-MT2500A al puerto WAN del segundo router.

      - Método 2: Mantenga el segundo router en el modo router predeterminado, pero con una dirección IP distinta que no entre en conflicto con 192.168.8.1/24, por ejemplo, 192.168.10.1. Luego conecte el puerto LAN del GL-MT2500A al puerto WAN del segundo router.

      Use su ordenador o teléfono inteligente para conectarse al Wi-Fi del segundo router.

      !!! Note

            El segundo router mencionado aquí es un router normal, como GL.iNet GL-AXT1800, TP-LINK o Netgear. En este escenario, es posible que no funcionen módems, terminales de red óptica ni dispositivos proporcionados por los ISP.

3.  Acceder al panel de administración web

    Abra un navegador web, recomendamos Chrome, Edge o Safari, y visite [http://192.168.8.1](http://192.168.8.1). Será dirigido a la configuración inicial del panel de administración web. Si no puede acceder al panel de administración web, consulte [aquí](cannot_access_web_admin_panel.md).

    Elija un idioma y haga clic en **Next** para continuar.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Configure la contraseña de administrador. Recomendamos usar una contraseña segura. Haga clic en **Submit** para continuar.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Después de la configuración inicial, entrará en el panel de administración web del router.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4.  Conectarse a Internet
    - [Conectarse a Internet mediante un cable Ethernet](../interface_guide/internet_ethernet.md)
    - [Conectarse a Internet mediante USB tethering](../interface_guide/internet_tethering.md)
    - [Conectarse a Internet mediante un módem USB](../interface_guide/internet_cellular.md)

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
