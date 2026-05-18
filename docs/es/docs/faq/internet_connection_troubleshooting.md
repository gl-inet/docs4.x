# Preguntas frecuentes sobre la solución de problemas de conexión a Internet

## P1. ¿Qué debo hacer si no puedo acceder a Internet?

Siga los pasos siguientes para realizar una solución de problemas básica.

1. Compruebe la conexión física.

    Asegúrese de que el cable Ethernet esté bien conectado entre el puerto WAN del router y el dispositivo aguas arriba (por ejemplo, módem, ONT o toma Ethernet). Compruebe los LED del dispositivo aguas arriba y verifique que haya transmisión activa.

2. Reinicie los dispositivos.

    Apague el dispositivo aguas arriba (por ejemplo, el módem) y su router. Espere de 1 a 2 minutos. Después, encienda primero el módem, espere a que esté completamente en línea y luego encienda el router.

3. Compruebe la dirección IP WAN.

    Inicie sesión en el panel de administración web del router y vaya a **INTERNET** -> **Ethernet**. Si se queda en estado de conexión, como se muestra a continuación, el problema puede deberse a DHCP, a la vinculación MAC o a que se requiera una VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Póngase en contacto con su ISP y confirme si necesita **nombre de usuario PPPoE**, **contraseña PPPoE** e **ID de VLAN** para acceder a Internet.

    Al mismo tiempo, verifique si su ISP había configurado previamente la **vinculación MAC** en su módem/ONT.

## P2. ¿Cuándo debo clonar una dirección MAC?

Algunos ISP vinculan su conexión de banda ancha a la dirección MAC del primer dispositivo conectado, normalmente su antiguo router u ordenador. Cuando sustituye el router, tendrá que clonar esa dirección MAC para restaurar el acceso a Internet.

Siga los pasos siguientes para clonar una dirección MAC en su router GL.iNet.

1. Anote la dirección MAC de su router anterior (o del ordenador que estaba vinculado previamente a su banda ancha).

2. Inicie sesión en el panel de administración web del router y vaya a **NETWORK** -> **Ethernet Port** (llamado **Port Management** en algunas versiones de firmware). Configure **MAC Mode** en **Clone** o **Manual**, introduzca manualmente la dirección MAC y, a continuación, haga clic en **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Reinicie el módem (es decir, el dispositivo aguas arriba).

## P3. ¿Cuándo necesito configurar un ID de VLAN?

Algunos ISP requieren etiquetado VLAN para la autenticación de Internet o la separación del tráfico, especialmente en conexiones de fibra e IPTV. Póngase en contacto con su ISP y confirme si se requiere un ID de VLAN.

Siga los pasos siguientes para configurar el ID de VLAN.

1. Inicie sesión en su router y vaya a **INTERNET** -> **Ethernet**. Haga clic en **Modify**.

2. Introduzca el ID de VLAN proporcionado por su ISP y, a continuación, haga clic en **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## P4. ¿Qué ocurre si sigue sin funcionar?

Si el problema persiste, intente conectar un PC o portátil directamente a su módem y compruebe si tiene acceso a Internet.

Si no tiene acceso a Internet, es posible que el problema esté en su ISP. Póngase en contacto con su ISP para obtener más ayuda.

Si sí tiene acceso a Internet, el problema puede estar relacionado con la configuración de su router. Póngase en contacto con nuestro soporte técnico en [support@gl-inet.com](mailto:support@gl-inet.com) y proporcione la siguiente información:

- Modelo del router
- Pasos de solución de problemas que ya ha probado
- Nombre de su ISP
- Cualquier otra información que crea que puede ayudarnos a asistirle

## Información de ISP

A continuación se muestra información de ISP por región recopilada por GL.iNet a partir de comentarios de clientes, foros y recursos de OpenWrt, solo como referencia.

| País/Región | ISP | Tipo de conexión | ID de VLAN | ¿Requiere clonación MAC? | Requisitos adicionales |
| :---------- | :-- | :--------------- | :--------- | :----------------------- | :--------------------- |
| Estados Unidos | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | Debe habilitar IP Passthrough; se requiere omitir la autenticación EAP |
| Estados Unidos | Spectrum | DHCP | N/A | Sí (en algunas zonas) | Vinculación MAC estricta (requiere reiniciar el módem) |
| Estados Unidos | Verizon Fios | DHCP | N/A | No | |
| Estados Unidos | Comcast Xfinity | DHCP | N/A | Sí (habitual) | Debe reiniciar el módem al cambiar de router (MAC release) |
| Estados Unidos | Cox Communications | DHCP | N/A | Sí | Debe reiniciar el módem al cambiar de router (MAC release) |
| Estados Unidos | Frontier Fiber | DHCP | N/A | No | |
| Estados Unidos | CenturyLink / Lumen | PPPoE | 201 | No | Se requieren VLAN en determinadas zonas |
| Canadá | Bell Canada Fibe | PPPoE | 35 | No | |
| Alemania | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 obligatoria para Internet; se requieren credenciales PPPoE |
| Alemania | Vodafone (Kabel) | DHCP | N/A | Sí (a veces) | Puede aplicarse vinculación MAC; reinicie el módem después de cambiar de router |
| Alemania | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 obligatoria para Internet |
| Alemania | DNS:NET | PPPoE | 37 | No | |
| Alemania | o2(UGG) | PPPoE | 7 | No | |
| Reino Unido | BT Broadband | PPPoE | 101 | No | VLAN 101 obligatoria; se requiere inicio de sesión PPPoE |
| Reino Unido | Sky Broadband | DHCP (Option 61) | 101 | No | Requiere DHCP Option 61 (identificador de cliente) |
| Reino Unido | Virgin | DHCP | N/A | Sí | El módem está en modo bridge y requiere clonación MAC |
| Francia | Orange | DHCP / PPPoE | 832 | No | VLAN 832 obligatoria; puede requerir autenticación Option 90 |
| Francia | Free (Freebox) | DHCP | N/A | No | |
| Francia | Bouygues Telecom | DHCP | 100 | Sí | Clonar la MAC del Bbox |
| España | Movistar | PPPoE | 6 | No | VLAN 6 (Internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| España | DIGI | PPPoE | 20 | No | |
| España | Orange | DHCP | 832/835 | No | Las VLAN pueden variar según la región |
| Italia | TIM | PPPoE | 835 | No | VLAN 835 obligatoria |
| Italia | Aruba | PPPoE | 835 | No | |
| Países Bajos | KPN | DHCP | 6 | No | VLAN 6 obligatoria para Internet |
| Países Bajos | Tweak | DHCP | 34 | Sí | Clonación de la MAC de Experia Box |
| Países Bajos | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Países Bajos | Odido | DHCP | 300 | No | |
| Bélgica | EDPnet | PPPoE | 10 | No | |
| Bosnia y Herzegovina | BH Telecom | PPPoE | 100 | No | |
| Croacia | Terrakom | PPPoE | 905 | No | |
| República Checa | O2 | PPPoE | 848 | No | |
| Chipre | Epic | PPPoE | 35 | No | |
| Chipre | Cyta | PPPoE | 42 | No | |
| Chipre | Cablenet | PPPoE | 42 | No | |
| Chipre | Primetel | PPPoE | 42 | No | |
| Polonia | Orange Polska | PPPoE | 35 | No | VLAN 35 obligatoria |
| Polonia | T-mobile | PPPoE | 35 | No | |
| Irlanda | Vodafone SIRO | PPPoE | 10 | No | |
| Irlanda | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Türkiye | Turknet | PPPoE | 35 | No | |
| Türkiye | Turk Telekom | PPPoE | 35 | No | |
| Türkiye | Turkcell Superonline | PPPoE | N/A | Sí | |
| Türkiye | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Grecia | Cosmote | PPPoE | 835 | No | |
| Grecia | Nova | PPPoE | 835 | Sí | |
| Grecia | DEI/PPC | DHCP | 835 | No | |
| Japón | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE requiere un router compatible con MAP-E/DS-Lite |
| Japón | SoftBank Hikari | PPPoE / IPoE | N/A | No | Se usa con frecuencia el servicio BBIX IPoE |
| India | Airtel | PPPoE / DHCP | N/A | No | Algunas regiones requieren PPPoE |
| India | JioFiber | DHCP | N/A | No | ONT bloqueado en muchos casos |
| Singapur | Singtel | PPPoE | 10 | No | VLAN 10 obligatoria; IPTV en VLAN separada |
| Singapur | StarHub | DHCP | N/A | No | Conexión basada en DHCP |
| Australia | NBN (varios ISP) | PPPoE / DHCP | 2 (habitual) | Sí | VLAN 2 habitual, pero depende del ISP |
