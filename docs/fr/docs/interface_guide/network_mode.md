# Network Mode

Dans la partie gauche du panneau d'administration Web, allez dans **NETWORK** -> **Network Mode**.

Le mode réseau désigne les différents rôles et fonctions opérationnels qu'un routeur peut adopter pour répondre à divers besoins de déploiement réseau. Ces modes sont adaptés à des scénarios allant de la couverture Wi-Fi domestique aux réseaux d'entreprise à liens multiples, chaque mode activant ou désactivant certaines fonctionnalités du routeur afin d'optimiser les performances.

!!! note

    1. Lorsque vous modifiez le mode réseau du routeur, vous devrez peut-être reconnecter tous les appareils clients.
    
    2. **Lorsque votre routeur est en mode Access Point / WDS / Bridge, vous ne pourrez pas accéder au panneau d'administration Web en utilisant l'adresse IP LAN d'origine.** Vous devez à la place vous connecter au routeur en amont pour trouver l'adresse IP qu'il a attribuée à ce routeur, puis utiliser cette adresse IP pour accéder au panneau d'administration Web. Si vous n'avez pas accès au routeur en amont, maintenez le bouton de réinitialisation enfoncé pendant 4 secondes pour revenir au mode Router par défaut.

    3. **En mode Extender**, vous pouvez toujours accéder au panneau d'administration Web à l'aide de son adresse IP LAN d'origine.
    
    4. **En mode Non-Router, les fonctionnalités suivantes ne seront pas disponibles** : Access Control (Allowlist and Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Pour les modèles avec Wi-Fi

À l'exception de certains modèles spécifiques, la plupart des routeurs sans fil GL.iNet disposent de la fonctionnalité Wi-Fi.

Les modèles équipés du Wi-Fi prennent généralement en charge quatre modes réseau : Router, Access Point, Extender et WDS. Notez que certains modèles ne prennent pas en charge le mode WDS.

![network mode](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router** : il s'agit du mode de fonctionnement par défaut de la plupart des routeurs domestiques et de petit bureau, conçu pour créer un réseau local privé et agir comme une passerelle dédiée entre l'Internet public et les appareils connectés.

    En mode Router, l'appareil active les fonctions essentielles, notamment NAT, DHCP et un pare-feu intégré. Il se connecte à une liaison en amont, telle qu'une fibre haut débit, attribue automatiquement des adresses IP privées aux appareils connectés et assure la sécurité réseau de l'ensemble du réseau privé.
    
    ---

- **Access Point** : ce mode permet à un routeur de se connecter à un réseau filaire via un câble LAN et de diffuser des signaux sans fil, étendant ainsi la couverture Wi-Fi dans les grands espaces pour permettre à davantage d'appareils d'accéder au réseau.

    En mode Access Point, le routeur désactive ses fonctions NAT et DHCP et fonctionne uniquement comme émetteur de signal sans fil et comme commutateur, plutôt que comme passerelle autonome.

    Après être passé en mode Access Point, vous ne pourrez plus accéder au panneau d'administration Web en utilisant l'adresse IP LAN d'origine. Vous devez à la place vous connecter au routeur en amont pour trouver l'adresse IP qu'il a attribuée à cet AP, puis utiliser cette adresse IP pour accéder au panneau d'administration Web. Si vous n'avez pas accès au routeur en amont, maintenez le bouton de réinitialisation enfoncé pendant 4 secondes pour revenir au mode Router par défaut.

    ---

- **Extender** : ce mode est conçu pour étendre la couverture Wi-Fi d'un réseau sans fil existant et éliminer les zones mortes dans les endroits où la connectivité est faible.

    Il permet au routeur de recevoir sans fil les signaux du routeur principal, de les amplifier, puis de retransmettre le signal renforcé. Contrairement au mode Access Point, il ne nécessite aucune connexion filaire au routeur principal, mais il peut entraîner une division par deux de la bande passante, car l'appareil doit gérer simultanément la réception et la transmission du signal.

    En mode Extender, vous pourrez toujours accéder au panneau d'administration Web en utilisant son adresse IP LAN d'origine.

    ---

- **WDS** : le mode Wireless Distribution System (WDS) est similaire au mode Extender dans la mesure où il étend la couverture Wi-Fi sans fil, mais il prend en charge le pontage sans fil entre plusieurs routeurs compatibles. Il est recommandé pour étendre un réseau sans fil lorsque le routeur en amont dispose de la fonctionnalité WDS.
    
    Ce mode convient parfaitement à des scénarios tels que la couverture de bâtiments à plusieurs étages ou de petits campus de bureaux où plusieurs routeurs doivent fonctionner ensemble pour former un réseau sans fil unifié. Contrairement au mode Extender, qui transmet uniquement les signaux d'un routeur principal vers un seul répéteur, le mode WDS permet aux routeurs interconnectés d'émettre et de recevoir des signaux, assurant ainsi une couverture fluide sur des zones plus vastes avec plusieurs nœuds de signal.

    Après être passé en mode WDS, vous ne pourrez plus accéder au panneau d'administration Web en utilisant l'adresse IP LAN d'origine. Vous devez à la place vous connecter au routeur en amont pour trouver l'adresse IP qu'il a attribuée à ce routeur WDS, puis utiliser cette adresse IP pour accéder au panneau d'administration Web. Si vous n'avez pas accès au routeur en amont, maintenez le bouton de réinitialisation enfoncé pendant 4 secondes pour revenir au mode Router par défaut.

## Pour les modèles sans Wi-Fi

Le GL-MT2500/GL-MT2500A ne prend pas en charge les modes Access Point, Extender ni WDS, car il ne dispose pas de la fonctionnalité Wi-Fi. En revanche, il prend en charge les modes Router et Bridge.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router** : il s'agit du mode de fonctionnement par défaut de la plupart des routeurs domestiques et de petit bureau, conçu pour créer un réseau local privé (LAN) et agir comme une passerelle dédiée entre l'Internet public et les appareils connectés.

    En mode Router, l'appareil active les fonctions essentielles, notamment NAT, DHCP et un pare-feu intégré. Il se connecte à une liaison en amont, telle qu'une fibre haut débit, attribue automatiquement des adresses IP privées aux appareils connectés et assure la sécurité réseau de l'ensemble du réseau privé.
    
    ---

- **Bridge** : permet au routeur de se connecter à un réseau filaire et de fonctionner comme un pont entre les appareils du réseau. 

    Dans ce mode, le routeur fonctionne essentiellement comme un commutateur, en transférant les données entre les appareils connectés sans fournir de services NAT, pare-feu ni DHCP. Cela permet une communication fluide entre les appareils d'un même réseau, car il agit comme un simple point de connexion plutôt que comme une passerelle réseau.

    Après être passé en mode Bridge, vous ne pourrez plus accéder au panneau d'administration Web en utilisant l'adresse IP LAN d'origine. Vous devez à la place vous connecter au routeur en amont pour trouver l'adresse IP qu'il a attribuée à ce routeur Bridge, puis utiliser cette adresse IP pour accéder au panneau d'administration Web. Si vous n'avez pas accès au routeur en amont, maintenez le bouton de réinitialisation enfoncé pendant 4 secondes pour revenir au mode Router par défaut.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
