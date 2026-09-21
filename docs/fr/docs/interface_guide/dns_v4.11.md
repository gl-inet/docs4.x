# DNS

**Remarque** : le contenu de cette page a été introduit pour la première fois dans le firmware v4.11.

Si votre appareil utilise une autre version du firmware, utilisez le sélecteur ci-dessous pour accéder au guide correspondant.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 et versions antérieures](dns.md)

</div>

---

Dans le menu latéral gauche du panneau d'administration Web, accédez à **DNS**.

Les paramètres DNS du routeur déterminent comment les noms de domaine sont traduits en adresses IP. Cette page permet d'utiliser les serveurs DNS obtenus automatiquement auprès des appareils en amont ou de définir des serveurs personnalisés. Vous pouvez également configurer les options DNS et modifier les règles d'hôtes statiques.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

Par défaut, les requêtes DNS du trafic correspondant à la stratégie VPN utilisent les serveurs DNS fournis par le tunnel VPN. Les autres requêtes DNS utilisent les serveurs obtenus à partir de l'interface WAN active. Si vous définissez des serveurs DNS personnalisés, vous pouvez les appliquer aux tunnels VPN, au routeur lui-même ou aux deux. Lorsque ces options sont activées, les requêtes DNS comprises dans le périmètre choisi sont résolues par les serveurs indiqués plutôt que par ceux obtenus depuis les interfaces réseau concernées. Si aucun serveur personnalisé n'est défini, le routeur utilise les serveurs DNS obtenus depuis les interfaces réseau concernées.

## DNS WAN

WAN DNS affiche les serveurs DNS récupérés depuis chaque liaison montante WAN, notamment Ethernet, Repeater, Tethering et Cellular.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Lorsqu'une liaison WAN est active, les adresses de ses serveurs DNS apparaissent à droite, comme illustré ci-dessous.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## DNS VPN

VPN DNS affiche les serveurs DNS obtenus depuis chaque tunnel VPN actif.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Lorsqu'un tunnel VPN est actif, les requêtes DNS du trafic VPN suivent la configuration VPN DNS, comme illustré ci-dessous.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## DNS manuel

Manual DNS prend en charge deux types de configuration : **Static DNS** et **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels** : si cette option est activée, le DNS manuel personnalisé est utilisé pour les paquets passant par le tunnel VPN à la place des paramètres DNS du VPN.

- **Apply Manual DNS to Router Itself** : cette option est activée par défaut. Lorsqu'elle est activée, les services intégrés du routeur (tels que GoodCloud) appliquent les paramètres DNS manuels personnalisés.

### DNS statique

Static DNS permet de saisir manuellement des adresses de serveurs DNS IPv4 ou IPv6. Vous pouvez saisir directement les adresses ou sélectionner des serveurs DNS publics prédéfinis dans la liste déroulante.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Vous pouvez saisir jusqu'à quatre adresses de serveurs DNS. Cliquez sur **Apply** pour enregistrer les modifications.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### DNS chiffré

Le mode Encrypted DNS prend en charge plusieurs fournisseurs DNS, notamment Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS et OpenDNS. Vous pouvez également spécifier manuellement un serveur DNS chiffré si nécessaire.

Sélectionnez d'abord le DNS Provider. Les autres options changent en fonction de votre sélection.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Si vous sélectionnez un fournisseur DNS précis (par exemple NextDNS), choisissez un type de chiffrement parmi DNS over TLS (DoT), DNS over HTTPS (DoH) et DNS over QUIC (DoQ). DNS over QUIC (DoQ) a été introduit dans le firmware v4.9 et n'est disponible que lorsque Control D, NextDNS ou AdGuard DNS est utilisé comme fournisseur.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Si vous sélectionnez Manual comme fournisseur DNS, choisissez un type de chiffrement parmi DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS et DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Cliquez ensuite sur **Add a Server** pour ajouter au moins un serveur DNS. Vous pouvez saisir directement l'URL ou le format stamp du DNS chiffré. Pour consulter la liste des serveurs publics, reportez-vous à [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Comparaison des types de chiffrement"

    1. **DNS over TLS (DoT)**

        Chiffre les requêtes DNS via un port TLS dédié. Le trafic DNS est ainsi isolé du trafic Web ordinaire et peut être facilement identifié par les opérateurs réseau.

    2. **DNS over HTTPS (DoH)**

        Transmet les données DNS dans le trafic HTTPS standard. Les requêtes DNS se confondent avec le trafic Web normal, ce qui assure une forte confidentialité et contourne les filtres de trafic simples.

    3. **DNS over QUIC (DoQ)**

        Encapsule DNS dans le protocole QUIC. Il offre une faible latence, une reconnexion rapide et des performances stables sur les réseaux instables.

    4. **Oblivious DNS over HTTPS (ODoH)**

        Version améliorée de DoH. Elle sépare l'adresse IP de l'utilisateur des requêtes DNS, empêchant le serveur et les fournisseurs réseau de suivre l'activité de navigation.

    5. **DNSCrypt**

        Protocole de chiffrement DNS mature. Il authentifie et chiffre le trafic DNS en privilégiant la protection contre la falsification et la compatibilité avec les anciens environnements réseau.

## Options DNS

Cliquez sur **Options** dans l'angle supérieur droit pour configurer les paramètres DNS avancés.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Vous pouvez activer ou désactiver ces options selon vos besoins.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection** : l'activation de cette option peut faire échouer les recherches DNS privées. Si votre réseau utilise un portail captif, désactivez cette option.

- **Override DNS Settings of All Clients** : lorsque cette option est activée, le routeur remplace les paramètres DNS non chiffrés de tous les clients.

## Modifier les hôtes

Cliquez sur **Edit Hosts** dans l'angle supérieur droit pour personnaliser les règles d'hôtes statiques.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

Le routeur donne la priorité à ces règles d'hôtes lors de la résolution des requêtes des clients connectés.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
