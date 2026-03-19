# ¿Por qué aparece un mensaje en la prueba de DDNS?

Cuando ejecuta la prueba de DDNS en la página Dynamic DNS, puede aparecer un mensaje como el siguiente.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

No es un mensaje de **Warning** ni de **Error**, sino un recordatorio que indica el estado de la red de su router.

Este resultado suele reflejar la posición del router dentro de la red. Por ejemplo, si su router GL.iNet está configurado como router secundario en su red doméstica, aparecerá este mensaje.

No desaparecerá aunque haya configurado el reenvío de puertos en su router principal; esto simplemente indica que el router está detrás de NAT.

Si necesita exponer servicios a través de NAT, por ejemplo, para acceso remoto, se requieren configuraciones adicionales.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
