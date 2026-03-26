# DNS

Sur le côté gauche du panneau d’administration web, allez à **NETWORK** -> **DNS**.

Les paramètres DNS de votre routeur contrôlent la manière dont les noms de domaine sont traduits en adresses IP. Cette page vous permet d’utiliser automatiquement le ou les serveurs DNS obtenus depuis les appareils en amont, ou d’en définir de personnalisés, ainsi que de configurer les priorités DNS.

Si vous définissez un ou plusieurs serveurs DNS personnalisés, toutes les requêtes DNS seront résolues par ceux-ci au lieu des serveurs DNS obtenus via chaque interface réseau. Sinon, vous utiliserez les paramètres DNS configurés pour chaque interface.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** l’activation de cette option peut provoquer l’échec de la résolution DNS privée. Si votre réseau utilise un portail captif, désactivez cette option.

- **Override DNS Settings for All Clients:** si cette option est activée, votre routeur remplacera les paramètres DNS non chiffrés pour tous les clients.

- **Allow Custom DNS to Override VPN DNS:** si cette option est activée, une fois un DNS personnalisé défini, les paquets transmis via le tunnel VPN seront résolus à l’aide du DNS personnalisé au lieu des paramètres DNS fournis par les connexions VPN.

## Paramètres du serveur DNS

Il existe quatre modes : Automatic, Encrypted DNS, Manual DNS et DNS Proxy.

- **Automatic** : le routeur utilisera automatiquement le serveur DNS fourni par l’appareil en amont (par exemple le modem du FAI ou le routeur principal), ou les paramètres DNS correspondant à chaque interface réseau.

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS** : quatre types de chiffrement sont disponibles : DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS et Oblivious DNS over HTTPS.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - Pour DNS over TLS, sélectionnez un fournisseur DNS parmi Control D, NextDNS et Cloudflare.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - Pour les trois autres modes (DNSCrypt-Proxy, DNS over HTTPS et Oblivious DNS over HTTPS), sélectionnez au moins un DNS Server depuis le dépôt.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS** : sélectionnez au moins un DNS Server pour votre routeur dans la liste déroulante.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy** : le routeur acheminera toutes les requêtes DNS du LAN vers l’adresse du serveur proxy que vous indiquez (par exemple `8.8.8.8#53`). Cela peut être utile si vous exécutez un autre serveur DNS ou Pi-hole sur votre réseau.

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Modifier Hosts

Les requêtes des clients seront résolues en priorité à l’aide des règles DNS statiques que vous écrivez dans Hosts.

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
