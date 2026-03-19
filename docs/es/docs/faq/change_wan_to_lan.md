# Cambiar WAN a LAN

Puede cambiar el puerto WAN del router para que funcione como puerto LAN. Esto resulta especialmente útil cuando se usa el router en modo repetidor, donde el puerto WAN no es necesario. Al cambiar el puerto WAN a LAN, tendrá un puerto LAN adicional para ampliar la conectividad.

Siga los pasos que se indican a continuación para cambiar WAN a LAN.

## Para firmware 4.7 y superior

1. Deje el puerto WAN sin conectar.

2. Conecte un dispositivo al router y acceda al panel de administración web del router.

3. En el panel de administración web, vaya a la sección **INTERNET** -> **Ethernet** y haga clic en el icono de engranaje de la esquina superior derecha.

   ![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

   Se le dirigirá a la página **Port Management**, donde el estado del puerto WAN se muestra como usado para WAN.

   ![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Haga clic en **LAN** para cambiar las propiedades del puerto Ethernet y luego en **Apply**.

   ![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

   En la ventana emergente de advertencia, haga clic en **Apply** para confirmar.

   ![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

   **Nota**: El Wi-Fi puede desconectarse temporalmente durante este proceso. Vuelva a conectarse al router una vez finalizado.

5. De vuelta en la sección Ethernet, se mostrará que el puerto WAN ahora se usa como puerto LAN.

   ![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

   Puede volver a cambiarlo a WAN en la página **Port Management**, o pulsar el botón RESET durante 4 segundos para reiniciar la interfaz WAN.

## Para firmware 4.6 y anterior

1. Deje el puerto WAN sin conectar.

2. Conecte un dispositivo al router y acceda al panel de administración web.

3. En el panel de administración web, vaya a la sección **INTERNET** -> **Ethernet**, donde se mostrará que el estado del puerto WAN es **Using as WAN**. Haga clic en **Change to LAN**.

   ![internet page](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Haga clic en **Apply** para confirmar.

   ![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

   **Nota**: El Wi-Fi puede desconectarse temporalmente durante este proceso. Vuelva a conectarse al router una vez finalizado.

5. De vuelta en la sección Ethernet, se mostrará `Using as LAN`.

   ![using as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

   Puede revertir fácilmente la configuración repitiendo los pasos anteriores.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
