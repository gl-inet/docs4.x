# Dynamic DNS

Dynamic Domain Name Service, Dynamic DNS o DDNS, es un servicio que se usa para asociar un nombre de dominio a la dirección IP dinámica de un dispositivo de red. Con Dynamic DNS, puede acceder a su router de forma remota. Para esta función se requiere una dirección IP pública de Internet.

## Habilitar DDNS

En el lado izquierdo del panel de administración web, vaya a **APPLICATIONS** -> **Dynamic DNS**.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Active **Enable DDNS**, acepte los **Terms of Services & Privacy Policy** y luego haga clic en **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Haga clic en **Security Settings** en la esquina inferior derecha.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

En la ventana emergente, compruebe si está habilitado el protocolo de acceso remoto que desea aplicar. Si no lo está, vaya a SYSTEM -> Security -> Remote Access Control para habilitarlo.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Habilite el protocolo de acceso remoto que desee y haga clic en **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Puede haber un retraso de hasta 10 minutos en la sincronización de registros entre servidores DNS. Esto puede impedirle acceder mediante el nombre de dominio DDNS inmediatamente después de habilitarlo o cuando cambie su IP pública.

**Nota**: Si habilita DDNS y VPN Client al mismo tiempo, asegúrese de que **Services From GL.iNet Use VPN** esté deshabilitado. Esta función puede encontrarse en [VPN Client Options](vpn_dashboard.md#tunnel-options) dentro de VPN Dashboard.

## Comprobar si DDNS funciona

Puede comprobar si DDNS funciona usando la herramienta DDNS test o verificarlo manualmente con comandos.

=== "Usando la herramienta DDNS Test"

    En la página Dynamic DNS, haga clic en **DDNS Test**

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Asegúrese de que la dirección IP obtenida mediante la resolución del dominio DDNS coincide con la IP WAN del router.

    Si no coincide, aparecerá un aviso amarillo en la parte superior indicando que el router puede estar detrás de NAT y que necesita configurar port forwarding en el router superior.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Comprobarlo manualmente"

    1. Use el comando `nslookup` para obtener la correspondencia entre el nombre de dominio y la dirección IP, como se muestra a continuación.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        Sustituya `xxxxxxx.glddns.com` en la imagen anterior por su Host Name.

        `8.8.8.8` en la imagen anterior es el DNS de Google. Úselo o reemplácelo por otro DNS y luego pulse Enter.

    2. Si obtiene una dirección IP pública como resultado, por ejemplo, `103.81.180.10`, como en la imagen siguiente, esto indica que su dominio DDNS se ha asociado correctamente a una dirección IP pública.

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}

        En un dispositivo conectado al router, busque `what is my ip address` en un navegador o visite un sitio web como [What Is My IP Address](https://whatismyipaddress.com){target="_blank"}. Obtendrá su dirección IP pública. Compare las dos direcciones IP obtenidas en los pasos 1 y 2. Si son iguales, DDNS está funcionando; en caso contrario, no.

    3. Si recibe un mensaje `** server can't find xxxxxxx.glddns.com: NXDOMAIN`, como se muestra a continuación, esto indica que la resolución del dominio ha fallado y que su dominio DDNS no se ha asociado correctamente a una dirección IP pública.

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## Acceso remoto HTTPS

!!! Note

    1. Se requiere una dirección **Public IP** para el acceso remoto HTTPS.

        Haga clic [aquí](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) para comprobar si su proveedor de servicios de Internet, ISP, le asigna una dirección IP pública.

    2. Si su router está detrás de NAT, configure port forwarding, puerto **443**, en el router superior para el acceso HTTPS.

Siga los pasos que se indican a continuación para habilitar el acceso remoto HTTPS a su router.

1. En la página Dynamic DNS, active **Enable DDNS**, acepte los **Terms of Services & Privacy Policy** y luego haga clic en **Apply**.

   ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. En el panel de administración web, vaya a SYSTEM -> Security -> Remote Access Control.

   ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Habilite **HTTPS Remote Access** y haga clic en **Apply**.

   ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Una vez habilitado, podrá acceder al panel de administración del router desde cualquier lugar usando el nombre de host DDNS mediante **HTTPS**, por ejemplo, `https://xxxxxxx.glddns.com`.

Si se ha configurado port forwarding, acceda mediante `https://xxxxxxx.glddns.com:external_port`, sustituyendo `external_port` por el número de puerto real.

**Nota**: Esta función usa certificados autofirmados, por lo que los navegadores mostrarán **Your connection is not private** cuando acceda al panel de administración del router mediante el nombre de host DDNS a través de **HTTPS**, como se muestra a continuación, usando el puerto 8001 como ejemplo.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Para continuar con el acceso remoto HTTPS, haga clic en **Advanced** en la parte inferior.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Luego haga clic en **Proceed to xxxxxxx.glddns.com** para continuar.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

A continuación podrá acceder al panel de administración web usando el nombre de host DDNS mediante HTTPS.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## Acceso remoto SSH

!!! Note

    1. Se requiere una dirección **Public IP** para el acceso remoto SSH.

        Haga clic [aquí](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) para comprobar si su proveedor de servicios de Internet, ISP, le asigna una dirección IP pública.

    2. Si su router está detrás de NAT, configure port forwarding, puerto **22**, en el router superior para el acceso SSH.

Siga los pasos que se indican a continuación para habilitar el acceso remoto SSH a su router.

1. En la página Dynamic DNS, active **Enable DDNS**, acepte los **Terms of Services & Privacy Policy** y luego haga clic en **Apply**.

   ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. En el panel de administración web, vaya a SYSTEM -> Security -> Remote Access Control.

   ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Habilite **SSH Remote Access** y haga clic en **Apply**.

   ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Una vez habilitado, podrá acceder al panel de administración del router desde cualquier lugar usando el nombre de host DDNS mediante **SSH**, por ejemplo, `ssh root@xxxxxxx.glddns.com`.

Si se ha configurado port forwarding, acceda mediante `ssh root@xxxxxxx.glddns.com:external_port`, sustituyendo `external_port` por el número de puerto real.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
