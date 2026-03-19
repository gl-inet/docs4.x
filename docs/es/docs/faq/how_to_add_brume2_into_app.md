# ¿Cómo añadir Brume 2 a la aplicación móvil GL.iNet?

Puede añadir su Brume 2, GL-MT2500 o GL-MT2500A, a la aplicación móvil GL.iNet incluso si no tiene función Wi-Fi. Puede configurarlo como router principal o como router secundario.

Los siguientes métodos también son aplicables a Brume, GL-MV1000.

## Brume 2 como router secundario

**Topología**

Aquí usamos Slate AX, GL-AXT1800, como router principal y Brume 2, GL-MT2500, como router secundario.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Inicie sesión en el panel de administración web de su Brume 2, vaya a **SYSTEM** -> **Security** -> **Open Ports on Router** y abra el puerto **80**.

   ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

   Para algunos modelos antiguos, vaya a **Firewall** -> **Open Ports on Router** y abra el puerto **80**.

   ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Inicie sesión en el router principal y anote la **WAN IP** de Brume 2.

   ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Conecte un teléfono al Wi-Fi de su router principal.

   ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

4. Inicie la aplicación GL.iNet y haga clic en **Add New Device**.

   ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

5. Luego haga clic en **Initialized Devices**.

   ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.PNG){class="glboxshadow gl-50-desktop"}

6. Introduzca la WAN IP que encontró anteriormente en el router principal.

   ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.PNG){class="glboxshadow gl-50-desktop"}

7. Introduzca la contraseña de inicio de sesión de Brume 2.

   ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

   Ahora su Brume 2 aparecerá en la aplicación móvil GL.iNet.

   ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

## Brume 2 como router principal

**Topología**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Inicie sesión en su router secundario, que en este caso es GL-AXT1800, y configúrelo en modo Access Point.

   ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Conecte un teléfono al Wi-Fi de su router secundario.

   ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

3. Inicie la aplicación GL.iNet y haga clic en **Add New Device**.

   ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

4. Seleccione su router principal.

   ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.PNG){class="glboxshadow gl-50-desktop"}

5. Haga clic en **Next**.

   ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.PNG){class="glboxshadow gl-50-desktop"}

6. Si sigue conectado al Wi-Fi del router secundario, simplemente espere. Si no, vuelva a conectarse al Wi-Fi del router secundario.

   ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.PNG){class="glboxshadow gl-50-desktop"}

7. Introduzca la contraseña de inicio de sesión de Brume 2.

   ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

   Ahora su Brume 2 aparecerá en la aplicación móvil GL.iNet.

   ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
