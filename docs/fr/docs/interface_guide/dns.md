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

### Automatic

Dans ce mode, le routeur utilisera automatiquement le serveur DNS fourni par l’appareil en amont (par exemple, le modem du FAI ou le routeur principal), ou les paramètres DNS correspondant à chaque interface réseau.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS

Veuillez suivre les instructions ci-dessous selon votre version du firmware.

!!! note "Pour le firmware v4.8 et antérieur"

    Quatre types de chiffrement sont disponibles : DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS et Oblivious DNS over HTTPS.

    Sélectionnez d’abord **Encryption Type**. Les autres options changeront en fonction de votre choix.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - **Pour DNS over TLS (DoT)**, choisissez un fournisseur DNS parmi **Control D**, **NextDNS** et **Cloudflare**.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - **Pour les trois autres options (DNSCrypt-Proxy, DNS over HTTPS et Oblivious DNS over HTTPS)**, sélectionnez au moins un serveur DNS depuis le dépôt.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

!!! note "Pour le firmware v4.9 et ultérieur"

    En plus de Control D, NextDNS et Cloudflare, davantage de fournisseurs DNS sont désormais disponibles pour le mode Encrypted DNS, notamment **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** et **OpenDNS**. Vous pouvez également spécifier manuellement un serveur DNS chiffré si nécessaire.

    Sélectionnez d’abord **DNS Provider**. Les autres options changeront en fonction de votre choix.

    ![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

    - Si vous sélectionnez un fournisseur DNS spécifique (par exemple NextDNS), choisissez un type de chiffrement parmi **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** et **DNS over QUIC (DoQ)**. Notez que DNS over QUIC (DoQ) a été introduit dans le firmware v4.9 et n’est disponible que lorsque vous utilisez Control D, NextDNS ou AdGuard DNS comme fournisseur DNS.

        ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

    - Si vous sélectionnez **Manual** comme fournisseur DNS, choisissez un type de chiffrement parmi **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** et **DNSCrypt**.

        ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

        Cliquez ensuite sur **Add a Server** pour ajouter au moins un serveur DNS. Vous pouvez saisir directement l’URL ou le format stamp du DNS chiffré. Pour une liste des serveurs publics, consultez [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

        ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Comparaison des types de chiffrement

1. **DNS over TLS (DoT)**

    Chiffre les requêtes DNS via un port TLS dédié. Il isole le trafic DNS du trafic web classique et reste facile à identifier pour les opérateurs réseau.

2. **DNS over HTTPS (DoH)**

    Transporte les données DNS dans le trafic HTTPS standard. Il mélange les requêtes DNS au trafic web normal pour une meilleure confidentialité et contourne les filtrages de trafic les plus simples.

3. **DNS over QUIC (DoQ)**

    Encapsule le DNS dans le protocole QUIC. Il offre une faible latence, une reconnexion rapide et des performances stables sur les réseaux instables.

4. **Oblivious DNS over HTTPS (ODoH)**

    Version améliorée de DoH. Il sépare l’adresse IP de l’utilisateur de ses requêtes DNS, empêchant à la fois le serveur et les fournisseurs de réseau de suivre votre activité de navigation.

5. **DNSCrypt**

    Protocole de chiffrement mature pour le DNS. Il authentifie et chiffre le trafic DNS, en mettant l’accent sur la protection contre la falsification et la compatibilité avec les environnements réseau plus anciens.

### Manual DNS

Dans ce mode, vous pouvez personnaliser le serveur DNS de votre routeur. Sélectionnez au moins un **DNS Server** pour votre routeur dans la liste déroulante.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy

Dans ce mode, le routeur acheminera toutes les requêtes DNS du LAN vers l’adresse du serveur proxy que vous indiquez (par exemple `8.8.8.8#53`). Cela peut être utile si vous exécutez un autre serveur DNS ou Pi-hole sur votre réseau.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Modifier Hosts

Vous pouvez cliquer sur le bouton **Edit Hosts** en haut à droite pour personnaliser les règles d’hôtes statiques.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

Le routeur applique ces règles d’hôtes en priorité lors de la résolution des requêtes des clients connectés.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
