# ¿Cómo resolver un conflicto de subred LAN?

Cuando conecta un cable Ethernet desde el router de casa al puerto WAN del router GL.iNet, a veces puede ver este mensaje:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Esto ocurre porque el router de su casa utiliza la misma IP LAN que el router GL.iNet, y esto se denomina conflicto de LAN.

Siga los pasos que se indican a continuación para cambiar la subred LAN.

## 1. Cambiar la subred LAN

Haga clic en el enlace **Change LAN Subnet** y será redirigido a la página de configuración **LAN**.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Cambie el número que aparece después del segundo punto, que por defecto es **8**, por otro número. Por ejemplo, 192.168.10.1, y luego haga clic en **Apply**.

Después del cambio, espere unos segundos. La página se actualizará y se redirigirá automáticamente a la nueva dirección IP, **192.168.10.1**. Verá que desaparece el aviso de conflicto de subred.

Si la página no se redirige, continúe con el siguiente paso.

## 2. Iniciar sesión con la nueva IP LAN

Introduzca manualmente la nueva IP LAN en la barra de direcciones y pulse Intro.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Inicie sesión con su contraseña de administrador y el aviso de conflicto de subred desaparecerá.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
