# LAN

Dans la partie gauche du panneau d'administration web, accédez à **NETWORK** -> **LAN**.

Le LAN est le réseau auquel votre appareil est connecté lorsqu'il utilise le Wi‑Fi principal ou un câble Ethernet.

Il comprend les paramètres de base, les paramètres du serveur DHCP et la réservation d'adresses.

## Paramètres de base

Vous pouvez définir le sous-réseau dans les plages d'adresses privées IPv4 suivantes : `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    Il s'agit de l'adresse à saisir dans la barre d'adresse de votre navigateur pour accéder à la page d'administration du routeur. 
    
    Par défaut, elle est définie sur **192.168.8.1**. Vous pouvez la modifier en cas de conflit avec votre réseau.

- **Netmask**
    
    La valeur par défaut est **255.255.255.0**. Vous pouvez également sélectionner **255.255.0.0** si vous avez besoin d'un sous-réseau plus grand avec davantage d'adresses IP.

- **AP Isolation**

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Ces appareils ne pourront pas communiquer avec les autres appareils du même réseau.

## Serveur DHCP

Le **DHCP Server** est activé par défaut. Le serveur DHCP attribue automatiquement à chaque appareil client une adresse IP et d'autres paramètres de communication.

Si le serveur DHCP est désactivé, vous devrez configurer manuellement les paramètres réseau des appareils clients. Cliquez [ici](../tutorials/manually_configure_static_ip.md) pour apprendre à configurer manuellement une adresse IP statique.

Vous pouvez modifier les adresses IP de début et de fin selon vos besoins — par exemple si votre réseau s'agrandit ou se réduit, si des conflits d'adresses IP surviennent ou si la plage du masque de sous-réseau est modifiée.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Cliquez sur **Advanced** pour effectuer une configuration supplémentaire si nécessaire.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time** : durée pendant laquelle une adresse IP attribuée par DHCP reste valide pour un appareil.

- **Gateway** : appareil qui achemine le trafic entre le réseau local et les réseaux externes tels qu'Internet.

- **DNS Server 1** : serveur principal qui traduit les noms de domaine en adresses IP.

- **DNS Server 2** : serveur secondaire utilisé pour la résolution des noms de domaine si le serveur DNS principal n'est pas disponible.

- **LPR Server** : (Line Printer Remote Server) service qui gère les tâches d'impression et permet aux appareils du réseau d'envoyer des demandes d'impression à des imprimantes distantes. Plusieurs ports d'imprimante LPR peuvent être configurés.

## Réservation d'adresses

Lorsque vous attribuez une adresse IP réservée à un client dans le LAN, ce client reçoit toujours la même adresse IP à chaque fois qu'il accède au serveur DHCP du routeur. Vous pouvez attribuer des adresses IP réservées aux ordinateurs ou aux serveurs qui nécessitent des paramètres IP permanents.

**Remarque :** les clients configurés doivent se reconnecter au routeur pour que la modification prenne effet.

Cliquez sur **Add** pour réserver une adresse IP.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

Une fenêtre contextuelle s'affiche.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Sélectionnez l'adresse **MAC** dans la liste déroulante ; l'adresse **IP** correspondant à la MAC sélectionnée sera remplie automatiquement. Donnez-lui un nom explicite, puis cliquez sur **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

Après avoir ajouté une nouvelle réservation d'adresse IP, la page affichée ci-dessous indique que la configuration a bien été effectuée.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
