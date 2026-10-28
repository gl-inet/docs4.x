# AdGuard Home-DNS de VPN-tunnel laten omzeilen {#how-to-make-adguard-home-dns-bypass-the-vpn-tunnel}

VPN en AdGuard Home kunnen normaal gesproken gelijktijdig op GL.iNet-routers worden uitgevoerd. Er ontstaan geen problemen als AdGuard Home niet is ingesteld om DNS-verzoeken te verwerken.

Als je AdGuard Home echter configureert om al het DNS-verkeer te beheren en query’s door te sturen naar **openbare upstream DNS-servers**, kunnen deze query’s via de VPN-tunnel worden geleid, afhankelijk van je VPN-routeringsinstellingen. Als die servers niet via de tunnel bereikbaar zijn, kunnen LAN-clients die AdGuard Home voor DNS-resolutie gebruiken mogelijk geen domeinnamen omzetten.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home is ingeschakeld en verwerkt DNS-verzoeken)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(Instellingen voor upstream DNS in AdGuard Home)</small>

Om AdGuard Home te laten functioneren terwijl VPN actief is, kun je in LuCI een statische route toevoegen die upstream DNS-verkeer naar de normale WAN-gateway doorstuurt en de VPN-tunnel omzeilt. Volg de onderstaande stappen.

1. Meld je aan bij het webbeheerpaneel van je router en ga naar **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Meld je aan met hetzelfde beheerderswachtwoord.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. Ga in LuCI naar **Network** -> **Routing** en klik op **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Maak een nieuwe statische route voor je upstream DNS-adressen.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface: selecteer de fysieke WAN-interface **wan**.

    - Route type: behoud de standaardwaarde.

    - Target: `[Your Public Upstream DNS Server]/32`

        Je kunt `nslookup` gebruiken om het werkelijke IP-adres van je openbare upstream DNS-server te controleren.

    - Gateway: `[Your WAN Upstream Gateway IP]`

        Dit is meestal het IP-adres van je modem of ISP-gateway, zoals `192.168.0.1`. Je vindt dit op de internetstatuspagina van je router.

    Deze route zorgt ervoor dat de upstream DNS-query's van AdGuard Home de VPN-tunnel omzeilen en rechtstreeks via je WAN-verbinding gaan.

4. Sla de instellingen op en pas ze toe. AdGuard Home zal daarna DNS-namen weer normaal omzetten.

5. Test de upstream DNS-servers.

    Je kunt je upstream DNS-servers rechtstreeks in de AdGuard Home-interface controleren.

    Ga in het webbeheerpaneel van je router naar **APPLICATIONS** -> **AdGuard Home** en klik op **Settings Page** om het AdGuard Home-dashboard te openen.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    Ga in het AdGuard Home-dashboard naar **Settings** -> **DNS settings** -> **Upstream DNS servers** en klik op **Test upstreams**. De resultaten verschijnen aan de rechterkant.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Tip**: als je meer dan één DNS-server hebt en deze een combinatie van IP-adressen en domeinen gebruiken, kun je AdGuard DNS scheiden van VPN-DNS. Dit is mogelijk eenvoudiger dan een statische route gebruiken.

Meld je via SSH aan bij je GL.iNet-router en voer de volgende opdrachten uit om AdGuard Home te dwingen DNS-query's uitsluitend via de WAN-verbinding te verzenden.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
