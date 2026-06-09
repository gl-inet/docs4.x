# Comment faire en sorte que le DNS d'AdGuard Home contourne le tunnel VPN

Normalement, VPN et AdGuard Home peuvent fonctionner simultanément sur les routeurs GL.iNet. Aucun problème ne survient lorsque AdGuard Home n'est pas configuré pour gérer les requêtes DNS.

Cependant, si vous configurez AdGuard Home pour gérer tout le trafic DNS et transférer les requêtes vers des **serveurs DNS publics en amont**, l'activation du VPN provoquera des échecs de résolution DNS.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home activé et gère les requêtes DNS)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(Paramètres DNS en amont d'AdGuard Home)</small>

Par défaut, tout le trafic sortant est acheminé via le tunnel VPN. Cela force le trafic DNS en amont d'AdGuard Home à passer par le VPN, qui ne peut pas atteindre vos serveurs DNS publics en amont. En conséquence, tous les clients connectés ne pourront pas résoudre les noms de domaine.

Pour qu'AdGuard Home reste fonctionnel lorsque le VPN est actif, vous pouvez ajouter une route statique dans LuCI pour acheminer le trafic DNS en amont vers la passerelle WAN habituelle en contournant le tunnel VPN. Suivez les étapes ci-dessous.

1. Connectez-vous au panneau d'administration Web de votre routeur et accédez à **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Connectez-vous avec le même mot de passe d'administration.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. Dans LuCI, accédez à **Network** -> **Routing**, puis cliquez sur **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Créez une nouvelle route statique pour vos adresses DNS en amont.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface : Sélectionnez l'interface WAN physique **wan**.
    
    - Route type : Conservez la valeur par défaut.
    
    - Target : `[Your Public Upstream DNS Server]/32`
    
        Vous pouvez utiliser `nslookup` pour vérifier l'adresse IP réelle de votre serveur DNS public en amont.
    
    - Gateway : `[Your WAN Upstream Gateway IP]`
    
        Il s'agit généralement de l'adresse IP de votre modem ou de la passerelle de votre FAI, par exemple `192.168.0.1`. Vous la trouverez sur la page d'état Internet de votre routeur.

    Cette route garantit que les requêtes DNS en amont d'AdGuard Home contournent le tunnel VPN et passent directement par votre connexion WAN.

4. Enregistrez et appliquez les paramètres. AdGuard Home reprendra alors la résolution DNS normale.

5. Testez les serveurs DNS en amont.

    Vous pouvez vérifier vos serveurs DNS en amont directement dans l’interface AdGuard Home.
    
    Dans le panneau d’administration Web de votre routeur, accédez à **APPLICATIONS** -> **AdGuard Home**, puis cliquez sur **Settings Page** pour ouvrir le tableau de bord d’AdGuard Home.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    Dans le tableau de bord d’AdGuard Home, accédez à **Settings** -> **DNS settings** -> **Upstream DNS servers** et cliquez sur **Test upstreams**. Les résultats apparaîtront sur la droite.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Astuce** : Si vous disposez de plusieurs serveurs DNS et qu'ils sont un mélange d'adresses IP et de noms de domaine, vous pouvez séparer le DNS d'AdGuard du DNS VPN, ce qui peut être plus simple que d'utiliser une route statique.

Connectez-vous en SSH à votre routeur GL.iNet et exécutez les commandes suivantes pour forcer AdGuard Home à envoyer les requêtes DNS uniquement via la WAN.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# Pour restaurer :
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
