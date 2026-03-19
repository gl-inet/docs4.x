# El módem USB no funciona correctamente en el router GL.iNet

Algunos routers GL.iNet tienen puertos USB, por lo que los usuarios pueden conectar un módem USB para configurar el acceso a Internet e incluso implementar escenarios Multi-WAN si lo combinan con otros accesos a Internet.

Sin embargo, puede ocurrir que algunos módems USB, como el ZTE F50 Mobile Wi-Fi Hotspot, no funcionen con normalidad en el router, provocando cortes frecuentes de la red.

Esto puede deberse a un problema de compatibilidad entre el puerto USB del router, normalmente USB 3.0, y la red Wi-Fi 2.4G, lo que hace que el módem USB se desconecte constantemente y no pueda acceder a Internet con normalidad.

Para resolver este problema, puede cambiar la especificación del puerto USB de USB 3.0 a USB 2.0.

Acceda al panel de administración de su router GL.iNet y vaya a **SYSTEM -> Overview -> External Storage**.

Verá una opción llamada USB Protocol Switch.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Cámbiela a USB 2.0. Aparecerá un mensaje como el que se muestra a continuación. Haga clic en Switch para continuar.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Cuando el protocolo USB aparezca como USB 2.0, significará que el cambio se ha realizado correctamente.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Después de eso, compruebe si la conexión a Internet mejora.

---

Artículos relacionados

- [Compatible Modems](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
