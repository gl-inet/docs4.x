So lassen Sie AdGuard Home DNS den VPN-Tunnel umgehen

Normalerweise können VPN und AdGuard Home gleichzeitig auf GL.iNet-Routern betrieben werden. Keine Probleme treten auf, solange AdGuard Home nicht für die Verarbeitung von DNS-Anfragen konfiguriert ist.

Wenn Sie AdGuard Home jedoch so einrichten, dass es den gesamten DNS-Datenverkehr verwaltet und Anfragen an **öffentliche Upstream-DNS-Server** weiterleitet, führt die Aktivierung des VPN zu DNS-Auflösungsfehlern.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/adguard_dns_failure/adguardhome.png){class="glboxshadow" width="660"}
<br><small>(AdGuard Home aktiviert und verarbeitet DNS-Anfragen)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/adguard_dns_failure/adguard_dns.png){class="glboxshadow" width="600"}
<br><small>(AdGuard Home DNS-Einstellungen)</small>

Standardmäßig wird der gesamte ausgehende Datenverkehr über den VPN-Tunnel geleitet. Dadurch wird der Upstream-DNS-Datenverkehr von AdGuard Home auf den VPN-Tunnel gezwungen, der Ihre öffentlichen Upstream-DNS-Server nicht erreichen kann. Infolgedessen können alle verbundenen Clients keine Domänennamen auflösen.

Damit AdGuard Home weiterhin funktioniert, während das VPN aktiv ist, können Sie in LuCI eine statische Route hinzufügen, um den Upstream-DNS-Datenverkehr an das reguläre WAN-Gateway weiterzuleiten und den VPN-Tunnel zu umgehen. Gehen Sie folgendermaßen vor:

1. Melden Sie sich im Web-Admin-Panel Ihres Routers an und gehen Sie zu **SYSTEM** -> **Advanced Settings** ->** Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/adguard_dns_failure/luci_login1.png){class="glboxshadow"}

    Melden Sie sich mit demselben Administrator-Passwort an.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/adguard_dns_failure/luci_login2.png){class="glboxshadow"}

2. Navigieren Sie in LuCI zu **Network** -> **Routing** und klicken Sie auf **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/adguard_dns_failure/routing1.png){class="glboxshadow"}

3. Erstellen Sie eine neue statische Route für Ihre Upstream-DNS-Adressen.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/adguard_dns_failure/routing2.jpg){class="glboxshadow"}

    - Schnittstelle: Wählen Sie die physische WAN-Schnittstelle **wan**.
    
    - Routentyp: Behalten Sie den Standardwert bei.
    
    - Ziel: `[Ihre öffentliche Upstream-DNS-Server-IP]/32`
    
        Verwenden Sie `nslookup`, um die tatsächliche IP-Adresse Ihres öffentlichen Upstream-DNS-Servers zu überprüfen.
    
    - Gateway: `[IP Ihres WAN-Upstream-Gateways]`
    
        Dies ist normalerweise die IP-Adresse Ihres Modems oder ISP-Gateways, z. B. `192.168.0.1`. Sie finden sie auf der Internet-Statusseite Ihres Routers.

    Diese Route stellt sicher, dass die Upstream-DNS-Abfragen von AdGuard Home den VPN-Tunnel umgehen und direkt über Ihre WAN-Verbindung laufen.

4. Speichern und wenden Sie die Einstellungen an. AdGuard Home wird dann die normale DNS-Auflösung wieder aufnehmen.

---

**Tipp**: Wenn Sie mehrere DNS-Server haben, die aus einer Mischung von IP- und Domänenadressen bestehen, können Sie die AdGuard-DNS von der VPN-DNS trennen. Das ist möglicherweise einfacher als die Verwendung einer statischen Route. 

Melden Sie sich per SSH an Ihrem GL.iNet-Router an und führen Sie die folgenden Befehle aus, um AdGuard Home zu zwingen, DNS-Anfragen ausschließlich über das WAN zu senden.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
