# Se connecter à Internet via un câble Ethernet

Connectez le routeur à un réseau haut débit au moyen d'un câble Ethernet branché sur le port WAN. En général, il obtient automatiquement une adresse IP (DHCP). Les utilisateurs peuvent également configurer manuellement une IP statique ou PPPoE. Cette méthode offre une grande stabilité et un débit élevé, ce qui la rend idéale pour les environnements domestiques et professionnels disposant d'un accès haut débit fixe.

Suivez les étapes ci-dessous pour connecter votre routeur à Internet via un câble Ethernet.

1. Connectez le port WAN de votre routeur à l'appareil en amont (par exemple un modem FAI, un routeur, un commutateur réseau ou une prise Ethernet) à l'aide d'un câble Ethernet. 

2. Connectez-vous au panneau d'administration web du routeur, puis accédez à la section **INTERNET** -> **Ethernet**. 

    Si la connexion aboutit, la section Ethernet affichera les détails du réseau, notamment le protocole, l'adresse IP, la passerelle et le serveur DNS.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Conseil** : avant de brancher le câble Ethernet sur le port WAN du routeur, vous pouvez cliquer sur **Change to LAN** pour [définir le port WAN comme port LAN](../faq/change_wan_to_lan.md). Cela est utile lorsque vous utilisez le routeur comme [Repeater](internet_repeater.md), car le port WAN physique reste inactif. Vous pouvez ainsi réaffecter ce port WAN inutilisé en port LAN et disposer d'un port LAN supplémentaire.

## Protocole

Trois types de protocoles sont disponibles : DHCP, Static et PPPoE. Cliquez sur **Modify** pour en changer.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP est le protocole par défaut et le plus courant. Il attribue automatiquement des adresses IP et d'autres paramètres de communication aux équipements réseau via une architecture client-serveur sur les réseaux IP.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static est nécessaire si votre FAI (Internet Service Provider) fournit une adresse IP fixe, ou si vous souhaitez configurer manuellement les informations réseau, telles que l'adresse IP, la passerelle et le masque de sous-réseau.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE est un protocole utilisé par la plupart des FAI. En général, ils fournissent un modem ainsi qu'un nom d'utilisateur et un mot de passe, nécessaires pour configurer l'accès à Internet.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Avancé

Outre les paramètres essentiels, certains paramètres avancés facultatifs sont également disponibles pour les trois protocoles ci-dessus.

* **VLAN ID** : ce paramètre n'est requis que si le serveur du fournisseur impose à l'interface d'utiliser un ID VLAN tagué spécifique.

* **TTL** : TTL (Time To Live) définit la durée maximale pendant laquelle les paquets peuvent survivre dans le réseau. Par défaut, le routeur décrémente de 1 le TTL des paquets entrants provenant des appareils clients avant de les transférer. Si vous devez le forcer, vous pouvez définir ici une valeur fixe. Le paramètre TTL n'est valable que pour IPv4.

* **HL** : en IPv6, le champ HL (Hop Limit) limite le nombre de sauts de transmission des paquets de données sur le réseau. Il correspond à l'équivalent du TTL en IPv4.

* **MTU** : la valeur MTU par défaut est de 1500 octets.

## Port Ethernet

Cliquez sur l'icône en forme d'engrenage en haut à droite pour accéder à [Port Ethernet](ethernet_port.md).

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

La page **WAN** affiche le rôle du port (c'est-à-dire son utilisation en WAN ou en LAN), le mode MAC et l'adresse MAC, ainsi que la vitesse négociée du port réseau. 

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

La page **LAN** affiche le rôle du port et la vitesse négociée du port réseau.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

Veuillez consulter ce [lien](ethernet_port.md) pour plus de détails. 

## Dépannage

Si un câble Ethernet est branché sur le port WAN mais qu'Internet n'est pas disponible, un message jaune s'affichera comme ci-dessous.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Pour résoudre ce problème :

1. Vérifiez que l'appareil en amont dispose bien d'un accès à Internet.

2. Accédez à la page [Multi-WAN](multi-wan.md) pour vérifier l'état de l'interface Ethernet.

---

Articles connexes

- [Page Internet](internet.md)
- [Comment définir la priorité de chaque méthode d'accès à Internet ?](multi-wan.md)
- [Comment définir l'équilibrage de charge lorsque plusieurs méthodes d'accès à Internet sont utilisées en même temps ?](multi-wan.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
