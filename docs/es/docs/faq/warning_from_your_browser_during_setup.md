# Advertencia de su navegador: Your Connection is not Private

Puede encontrarse con esta alerta del navegador si es la primera vez que configura su router GL.iNet: Your Connection is not Private.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Esta es una advertencia de seguridad estándar emitida por el navegador cuando detecta un sitio web sin un certificado SSL/TLS de confianza.

Los navegadores suelen estar diseñados para confiar en certificados emitidos por autoridades de certificación de terceros, CAs. Sin embargo, los routers GL.iNet usan certificados autofirmados, que no son emitidos por una CA. Por eso, los navegadores los marcan como inseguros y muestran esta advertencia.

## ¿Es seguro acceder a 192.168.8.1?

Damos prioridad a la seguridad de su red. Durante la configuración inicial, no necesita conexión a Internet, ya que el proceso es completamente local.

Cuando se conecta al Wi-Fi del router GL.iNet durante la configuración, puede ver **"Connected, No internet"**. Esto es normal, ya que el router funciona dentro de una red local independiente durante la configuración.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

Del mismo modo, la IP **192.168.8.1** es una dirección IP local privada asignada al propio router. Se usa para acceder al panel de administración local del dispositivo, no a un sitio web público.

Como la conexión es completamente local y no se requiere acceso a Internet durante la configuración, **no existe riesgo de filtración de privacidad**. Esto garantiza un entorno seguro y aislado para configurar su router.

## ¿Por qué sigo recibiendo una advertencia?

Los navegadores normalmente no distinguen entre una dirección IP predefinida para la configuración y un sitio web normal; tratan todas las direcciones IP como si fueran sitios web y esperan que las conexiones HTTPS estén protegidas con certificados SSL/TLS.

Los routers GL.iNet sí utilizan certificados SSL/TLS, pero son autofirmados y no emitidos por autoridades de certificación de terceros, CAs. Aunque acceder a esta IP es seguro, ya que está en una red local privada, el navegador sigue considerándola "insegura", por lo que muestra una alerta.

## ¿Qué puedo hacer con esta advertencia?

Haga clic en **Advanced** y luego en **Continue to 192.168.8.1**.

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Después será redirigido al panel de administración web.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## ¿Puedo añadir un certificado SSL en el router?

Sí, puede añadir su certificado SSL en los routers GL.iNet.

[Cómo añadir un certificado SSL](../faq/use_https_for_adh.md)

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
