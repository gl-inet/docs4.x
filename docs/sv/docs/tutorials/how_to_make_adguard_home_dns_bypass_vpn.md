# Låt AdGuard Home DNS kringgå VPN-tunneln {#how-to-make-adguard-home-dns-bypass-the-vpn-tunnel}

VPN och AdGuard Home kan normalt köras samtidigt på GL.iNet-routrar. Inga problem uppstår när AdGuard Home inte är inställt på att hantera DNS-förfrågningar.

Om du däremot konfigurerar AdGuard Home för att hantera all DNS-trafik och vidarebefordra frågor till **public upstream DNS servers** leder aktivering av VPN till fel vid DNS-uppslagning.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home är aktiverat och hanterar DNS-förfrågningar)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(AdGuard Homes inställningar för uppströms DNS)</small>

Som standard dirigeras all utgående trafik genom VPN-tunneln. Det tvingar AdGuard Homes uppströms DNS-trafik genom VPN, där den inte kan nå de offentliga uppströms DNS-servrarna. Därför kan inga anslutna klienter slå upp domännamn.

För att AdGuard Home ska fortsätta fungera när VPN är aktivt kan du lägga till en statisk rutt i LuCI som vidarebefordrar uppströms DNS-trafik till den vanliga WAN-gatewayen och kringgår VPN-tunneln. Följ stegen nedan.

1. Logga in på routerns webbadministrationspanel och gå till **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Logga in med samma administratörslösenord.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. Gå till **Network** -> **Routing** i LuCI och klicka sedan på **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Skapa en ny statisk rutt för adresserna till de uppströms DNS-servrarna.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface: Välj det fysiska WAN-gränssnittet **wan**.

    - Route type: Behåll standardvärdet.

    - Target: `[Your Public Upstream DNS Server]/32`

        Du kan använda `nslookup` för att verifiera den faktiska IP-adressen för den offentliga uppströms DNS-servern.

    - Gateway: `[Your WAN Upstream Gateway IP]`

        Det är vanligtvis IP-adressen för modemet eller internetleverantörens gateway, till exempel `192.168.0.1`. Du hittar den på routerns sida för internetstatus.

    Rutten gör att AdGuard Homes uppströms DNS-frågor kringgår VPN-tunneln och går direkt via WAN-anslutningen.

4. Spara och tillämpa inställningarna. AdGuard Home återupptar sedan normal DNS-uppslagning.

5. Testa de uppströms DNS-servrarna.

    Du kan verifiera de uppströms DNS-servrarna direkt i AdGuard Home-gränssnittet.

    Gå till **APPLICATIONS** -> **AdGuard Home** i routerns webbadministrationspanel och klicka sedan på **Settings Page** för att öppna AdGuard Home-instrumentpanelen.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    Gå till **Settings** -> **DNS settings** -> **Upstream DNS servers** på AdGuard Home-instrumentpanelen och klicka på **Test upstreams**. Resultaten visas till höger.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Tips:** Om du har flera DNS-servrar som består av en blandning av IP-adresser och domäner kan du skilja AdGuard DNS från VPN DNS. Det kan vara enklare än att använda en statisk rutt.

Logga in på GL.iNet-routern via SSH och kör följande kommandon för att tvinga AdGuard Home att endast skicka DNS-frågor via WAN.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
