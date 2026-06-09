# Cómo hacer que el DNS de AdGuard Home evite el túnel VPN

Normalmente, la VPN y AdGuard Home pueden funcionar simultáneamente en los routers GL.iNet. No surgen problemas cuando AdGuard Home no está configurado para manejar las solicitudes DNS.

Sin embargo, si configura AdGuard Home para gestionar todo el tráfico DNS y reenviar consultas a **servidores DNS ascendentes públicos**, al activar la VPN se producirán fallos en la resolución DNS.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home habilitado y gestiona las solicitudes DNS)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(Configuración de DNS ascendente de AdGuard Home)</small>

De forma predeterminada, todo el tráfico saliente se enruta a través del túnel VPN. Esto obliga a que el tráfico DNS ascendente de AdGuard Home pase por la VPN, la cual no puede alcanzar sus servidores DNS ascendentes públicos. Como resultado, todos los clientes conectados no podrán resolver nombres de dominio.

Para mantener AdGuard Home funcional mientras la VPN está activa, puede añadir una ruta estática en LuCI para reenviar el tráfico DNS ascendente a la puerta de enlace WAN habitual y evitar el túnel VPN. Siga los pasos a continuación.

1. Inicie sesión en el Panel de Administración web de su router y vaya a **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Inicie sesión con la misma contraseña de administrador.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. En LuCI, navegue hasta **Network** -> **Routing**, luego haga clic en **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Cree una nueva ruta estática para sus direcciones DNS ascendentes.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface: seleccione la interfaz WAN física **wan**.
    
    - Route type: mantenga el valor predeterminado.
    
    - Target: `[Your Public Upstream DNS Server]/32`
    
        Puede usar `nslookup` para verificar la dirección IP real de su servidor DNS ascendente público.
    
    - Gateway: `[Your WAN Upstream Gateway IP]`
    
        Suele ser la dirección IP de su módem o puerta de enlace del ISP, como `192.168.0.1`. Encuéntrela en la página de estado de internet de su router.

    Esta ruta garantiza que las consultas DNS ascendentes de AdGuard Home eviten el túnel VPN y pasen directamente a través de su conexión WAN.

4. Guarde y aplique los ajustes. AdGuard Home reanudará entonces la resolución DNS normal.

5. Pruebe los servidores DNS ascendentes.

    Puede verificar sus servidores DNS ascendentes directamente en la interfaz de AdGuard Home.
    
    En el Panel de Administración web de su router, vaya a **APPLICATIONS** -> **AdGuard Home**, luego haga clic en **Settings Page** para abrir el panel de AdGuard Home.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    En el panel de AdGuard Home, vaya a **Settings** -> **DNS settings** -> **Upstream DNS servers** y haga clic en **Test upstreams**. Los resultados aparecerán a la derecha.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Consejo**: Si tiene más de un servidor DNS y son una combinación de IP y dominio, puede separar el DNS de AdGuard del DNS de la VPN, lo que podría ser más sencillo que usar una ruta estática.

Inicie sesión por SSH en su router GL.iNet y ejecute los siguientes comandos para forzar a que AdGuard Home envíe las consultas DNS solo a través de la WAN.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

¿Aún tiene preguntas? Visite nuestro [Foro Comunitario](https://forum.gl-inet.com){target="_blank"} o [Contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
