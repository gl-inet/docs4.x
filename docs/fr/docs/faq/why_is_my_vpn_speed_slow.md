# Pourquoi la vitesse de mon VPN est-elle plus lente que prévu ?

Si vous avez constaté que la vitesse de votre connexion VPN est inférieure à la vitesse théorique maximale (testée dans un réseau local idéal), c'est tout à fait normal en conditions réelles.

Les VPN sont conçus pour privilégier la sécurité et la confidentialité, ce qui a naturellement un impact sur la vitesse. Dans des conditions réseau habituelles, il est normal que la vitesse d'un VPN se situe entre 30 % et 50 % de la vitesse maximale annoncée. Cet écart s'explique par plusieurs facteurs qui influencent les performances. Ils sont détaillés ci-dessous, avec quelques conseils pour optimiser votre expérience.

**Remarque** : les méthodes ci-dessous peuvent aider à améliorer la vitesse du VPN, mais elles ne garantissent pas d'atteindre la vitesse annoncée, car les performances réelles dépendent de plusieurs facteurs.

## Vitesse du CPU du routeur

Le VPN chiffre vos données pour protéger votre vie privée, ce qui ajoute un traitement supplémentaire. Ce chiffrement et ce déchiffrement peuvent ralentir votre connexion. Choisissez un routeur doté d'un processeur plus rapide pour améliorer la vitesse de votre VPN.

Nous avons indiqué les vitesses de test VPN de tous les modèles sur notre [page produit](https://www.gl-inet.com/products/). Veuillez toutefois noter les points suivants :

* Les tests sont effectués sur un réseau local. Les vitesses réelles peuvent varier selon votre configuration réseau.
* Les vitesses OpenVPN et WireGuard seront plus faibles lorsque le routeur est utilisé comme serveur. Les résultats ci-dessus correspondent au mode client.

## Distance du serveur

Si le serveur VPN est éloigné de votre emplacement physique, les données doivent parcourir une plus grande distance, ce qui entraîne une latence plus élevée et des vitesses plus faibles.

L'exemple ci-dessous montre les vitesses côté client lors de connexions à différents emplacements de serveur au même moment de la journée.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Charge du serveur

Si de nombreux utilisateurs sont connectés au même serveur VPN, celui-ci peut être saturé, ce qui ralentit la vitesse pour tout le monde.

## Vitesse d'envoi du serveur

Si vous utilisez un tunnel VPN privé, la vitesse d'envoi du fournisseur d'accès Internet (FAI) du côté serveur sera le facteur limitant pour la vitesse de téléchargement du côté client, car le client VPN télécharge les données via le serveur.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Différences entre protocoles

Les protocoles VPN tels qu'OpenVPN et WireGuard diffèrent en matière de sécurité et de vitesse. Certains peuvent être plus lents en raison de leur méthode de chiffrement.

## Limitation par le FAI

Certains fournisseurs d'accès Internet (FAI) peuvent limiter la vitesse des utilisateurs qui utilisent un VPN, surtout s'ils soupçonnent une forte consommation de données. Cela est particulièrement fréquent dans certains pays en développement ou dans de petites villes où de nombreux utilisateurs partagent une infrastructure Internet limitée.

## DNS

Certains fournisseurs d'accès Internet (FAI) peuvent ne pas résoudre correctement les domaines VPN. Essayez d'utiliser [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) dans les paramètres **Network** de votre routeur.

## MTU

Certains fournisseurs d'accès Internet (FAI), en particulier les opérateurs mobiles, peuvent limiter la taille des paquets de données. Essayez de modifier la MTU par défaut de 1420 à 1380 ou 1280 dans **VPN Client Options**.

Pour le firmware v4.8 et supérieur, veuillez consulter [ici](../interface_guide/vpn_dashboard.md/#tunnel-options).

Pour le firmware v4.7 et antérieur, veuillez consulter [ici](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
