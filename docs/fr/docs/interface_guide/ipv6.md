# IPv6

IPv6 (Internet Protocol version 6) est la dernière version du protocole Internet, conçue pour remplacer IPv4. Il offre un plus grand nombre d'adresses IP uniques, résout le problème d'épuisement des adresses IPv4 et prend en charge le nombre croissant d'appareils connectés dans le monde.

Dans la partie gauche du panneau d'administration web, accédez à **NETWORK** -> **IPv6**. 

Cette page vous permet d'activer et de configurer IPv6 sur votre routeur.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

Lorsque l'IPv6 est activé, les interfaces WAN telles qu'Ethernet obtiennent leur adresse IPv6 via DHCPv6. Vous pouvez également modifier manuellement l'adresse IPv6 sur la page des paramètres Ethernet.

**Remarque** : certaines fonctionnalités (par exemple le pare-feu, GoodCloud, OpenVPN DCO) ne prennent pas encore en charge IPv6. Si vous utilisez ces fonctionnalités et IPv6 en même temps, cela risque d'entraîner des problèmes de connectivité.

Activez **Enable IPv6**, sélectionnez le mode de votre réseau principal ainsi que la méthode d'acquisition du DNS, puis cliquez sur **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode** : quatre modes sont disponibles : **Native**, **Passthrough**, **NAT6** et **Static IPv6**.

- Native : ce mode convient lorsque le routeur obtient directement une adresse IPv6 publique et attribue automatiquement des adresses IPv6 aux appareils en ligne. Ce mode répond aux besoins d'accès IPv6 de la plupart des utilisateurs.

- Passthrough : ce mode convient lorsque les paquets IPv6 doivent être transmis directement, sans traitement ni conversion. Par exemple, certaines applications ou certains services réseau peuvent nécessiter de préserver intégralement le contenu des paquets IPv6 pour un traitement ou une analyse ultérieurs, notamment pour le débogage réseau ou l'analyse de sécurité.

- NAT6 : ce mode convient aux scénarios dans lesquels un routeur est utilisé comme passerelle de gestion pour attribuer des adresses IPv6 internes dynamiques à chaque appareil du réseau. Dans ce mode, les terminaux se connectent via un terminal de réseau optique (Optical Network Terminal) et obtiennent une adresse IPv6 du réseau local.

- Static IPv6 : ce mode convient aux appareils ou services nécessitant une adresse IPv6 fixe, comme les serveurs ou les imprimantes réseau. Il garantit que l'appareil utilise toujours la même adresse IPv6, ce qui facilite la gestion et l'accès.

**Méthode d'acquisition du DNS** : elle détermine comment le routeur obtient les adresses des serveurs DNS IPv6. Deux options sont disponibles : **Automatic** et **Manual**. 

- Automatic : le routeur obtiendra dynamiquement les adresses des serveurs DNS IPv6 (par exemple via DHCPv6).

- Manual : saisissez des adresses de serveurs DNS IPv6 personnalisées. Cependant, comme le DNS sert à résoudre les noms de domaine en adresses IP correspondantes, une configuration manuelle des serveurs DNS peut provoquer des échecs de résolution DNS. Utilisez cette option avec prudence.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
