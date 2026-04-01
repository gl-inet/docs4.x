# Réseau invité

Les paramètres du réseau invité sont séparés de [LAN](lan.md) depuis le firmware v4.5.

Dans le panneau d'administration web, accédez à **NETWORK** -> **Guest Network**. 

Cette page comprend les paramètres de base du réseau invité et les paramètres du serveur DHCP.

## Paramètres de base

Vous pouvez définir le sous-réseau dans les plages d'adresses privées IPv4 suivantes : `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

Vous pouvez configurer un réseau séparé et isolé, conçu pour les utilisateurs temporaires, afin de fournir un accès limité et une sécurité renforcée grâce à sa séparation du réseau principal.

**Note**: Certains modèles (par exemple GL-MT5000, GL-MT2500/GL-MT2500A) ne prennent pas en charge le Wi-Fi ; les paramètres du réseau invité ne sont donc pas disponibles dans leur panneau d'administration web.

- **Gateway**

    La **passerelle par défaut** du réseau invité est **192.168.9.1**. Si elle entre en conflit avec votre réseau local, remplacez-la par une autre adresse.

- **Netmask**
    
    La valeur par défaut est **255.255.255.0**. Vous pouvez également sélectionner **255.255.0.0** si vous avez besoin d'un sous-réseau plus large avec davantage d'adresses IP.

- **AP Isolation**

    Cette fonctionnalité est disponible depuis le firmware v4.5.

    Elle permet d'isoler les appareils clients dans un segment réseau distinct. Ces appareils ne pourront pas communiquer avec les autres appareils du même réseau.

- **Block WAN Subnets**

    Cette fonctionnalité est disponible depuis le firmware v4.8.

    Lorsqu'elle est activée, le réseau invité ne peut pas accéder au réseau amont ni à son sous-réseau.

## Serveur DHCP

Si le réseau invité est activé, le serveur DHCP est activé par défaut.

Le serveur DHCP attribue automatiquement des adresses IP et d'autres paramètres de communication à chaque appareil client connecté au réseau invité. Si le serveur DHCP est désactivé, vous devrez configurer manuellement les paramètres réseau des appareils clients. Cliquez [ici](../tutorials/manually_configure_static_ip.md) pour savoir comment configurer manuellement une adresse IP statique.

Vous pouvez modifier les adresses IP de début et de fin selon vos besoins, par exemple si votre réseau s'agrandit ou se réduit, en cas de conflit d'adresses IP, ou si la plage du masque de sous-réseau est modifiée.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Cliquez sur **Advanced** pour effectuer une configuration supplémentaire si nécessaire.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time** : durée pendant laquelle une adresse IP attribuée par DHCP reste valide pour un appareil.

- **Gateway** : appareil qui route le trafic entre le réseau invité et les réseaux externes tels qu'Internet.

- **DNS Server 1** : serveur principal qui traduit les noms de domaine en adresses IP.

- **DNS Server 2** : serveur secondaire utilisé pour la résolution des noms de domaine si le serveur DNS principal est indisponible.

- **LPR Server** : (Line Printer Remote Server) service qui gère les travaux d'impression et permet aux appareils du réseau d'envoyer des demandes d'impression à des imprimantes distantes. Plusieurs ports d'imprimante LPR peuvent être configurés.

---

Articles connexes :

- [Comment configurer un réseau Wi-Fi invité sur les routeurs GL.iNet](../tutorials/how_to_set_up_a_guest_network.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
