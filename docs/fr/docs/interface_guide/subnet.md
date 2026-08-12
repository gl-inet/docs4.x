# Sous-réseau

**Note** : Cette page est actuellement disponible sur Flint 4 (GL-BE14000) et sera déployée sur d'autres modèles avec le firmware v4.10.

---

Sur le côté gauche du panneau d'administration Web, allez dans **NETWORK** -> **Subnet**.

Cette page regroupe la configuration de **LAN**, **Guest Network**, **IoT Network** et des **VLAN Networks** personnalisés dans une vue unifiée. Elle fournit une interface de gestion centralisée pour tous les paramètres liés aux sous-réseaux, ce qui vous permet de créer et gérer plusieurs sous-réseaux afin d'isoler différents types d'appareils ou de trafic.

## Réseau principal

**Main Network** est le réseau auquel votre appareil est connecté via le Wi-Fi principal ou via un câble Ethernet.

Dans Main Network, vous pouvez voir directement tous les états d'interface, le VLAN ID, l'adresse IP du routeur et la plage DHCP.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Cliquez sur **Edit** dans le coin inférieur droit pour configurer Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

La page de configuration comprend les paramètres de base, les paramètres du serveur DHCP et la réservation d'adresse.

### Paramètres de base

Vous pouvez définir le sous-réseau dans les plages d'adresses IPv4 privées : `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Il s'agit de l'adresse à saisir dans la barre d'adresse de votre navigateur pour accéder à la page d'administration du routeur.

    Par défaut, elle est définie sur **192.168.8.1**. Vous pouvez la modifier si elle entre en conflit avec votre réseau.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez aussi sélectionner **255.255.0.0** si vous avez besoin d'un sous-réseau plus grand avec plus d'adresses IP.

- **VLAN ID**

    Le VLAN ID par défaut de Main Network est **1** et ne peut pas être modifié.

- **AP Isolation**

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Ces appareils ne pourront pas communiquer avec les autres appareils du même réseau.

### Serveur DHCP

Le **DHCP Server** est activé par défaut. Le serveur DHCP attribue automatiquement des adresses IP et d'autres paramètres de communication à chaque appareil client.

Si le serveur DHCP est désactivé, vous devrez configurer manuellement les paramètres réseau des appareils clients. Cliquez [ici](../tutorials/manually_configure_static_ip.md) pour apprendre à configurer manuellement une IP statique.

Vous pouvez modifier les adresses IP de début et de fin selon vos besoins, par exemple si votre réseau s'agrandit ou se réduit, si des conflits d'adresses IP se produisent ou si la plage du masque de sous-réseau est modifiée.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Cliquez sur **Advanced** pour une configuration supplémentaire si nécessaire.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time** : période pendant laquelle une adresse IP attribuée par DHCP reste valide pour un appareil.

- **Gateway** : appareil qui route le trafic entre le réseau local et les réseaux externes tels qu'Internet.

- **DNS Server** : deux champs de serveur DNS sont disponibles pour configurer les résolveurs principal et secondaire.

    **Note** : le DNS principal est saisi dans le champ supérieur et le DNS secondaire dans le champ inférieur. Si le serveur principal n'est pas disponible, les appareils clients basculent automatiquement vers le résolveur secondaire, ce qui assure la continuité de la résolution des noms de domaine.

- **LPR Server** (Line Printer Remote Server) : service qui gère les travaux d'impression et permet aux appareils réseau d'envoyer des demandes d'impression à des imprimantes distantes. Plusieurs ports d'imprimante LPR peuvent être configurés.

### Réservation d'adresse

Lorsque vous spécifiez une adresse IP réservée pour un client dans le LAN, ce client reçoit toujours la même adresse IP chaque fois qu'il accède au serveur DHCP du routeur. Vous pouvez attribuer des adresses IP réservées aux ordinateurs ou serveurs qui nécessitent des paramètres IP permanents.

**Note :** Les clients configurés doivent se reconnecter au routeur pour que le paramètre prenne effet.

Cliquez sur **Add** pour réserver une IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

Une fenêtre contextuelle apparaît.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Sélectionnez **MAC** dans la liste déroulante. L'**IP** disponible correspondante est automatiquement renseignée. Vous pouvez aussi saisir un **hostname** et un **name** personnalisé pour faciliter l'identification. Cliquez ensuite sur **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

Après l'ajout d'une nouvelle réservation d'adresse IP, la page ci-dessous s'affiche, ce qui signifie que la configuration a réussi.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Réseau invité

**Guest Network** fournit un réseau Wi-Fi dédié aux visiteurs. Isolé du réseau principal, il renforce la sécurité tout en offrant un accès pratique à Internet.

**Note** : Certains modèles, par exemple GL-MT5000 et GL-MT2500/GL-MT2500A, ne disposent pas de fonction Wi-Fi ; les paramètres Guest Network ne sont donc pas disponibles dans leur panneau d'administration Web.

Dans Guest Network, vous pouvez voir directement l'état de l'interface, le VLAN ID, la passerelle et la plage DHCP.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Cliquez sur **Edit** dans le coin inférieur droit ; le panneau de configuration Guest Network s'ouvre sur le côté droit de la page.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

La page de configuration comprend les paramètres de base et les paramètres du serveur DHCP.

### Paramètres de base

Vous pouvez définir le sous-réseau dans les plages d'adresses IPv4 privées : `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/gest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    La **passerelle par défaut** de Guest Network est **192.168.9.1**. Si elle entre en conflit avec votre réseau local, remplacez-la par une autre adresse.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez aussi sélectionner **255.255.0.0** si vous avez besoin d'un sous-réseau plus grand avec plus d'adresses IP.

- **VLAN ID**

    Le VLAN ID par défaut de Guest Network est **9** et peut être modifié selon vos besoins.

- **AP Isolation**

    Cette fonction est disponible depuis le firmware v4.5.

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Ces appareils ne pourront pas communiquer avec les autres appareils du même réseau.

- **WAN Access Control**

    WAN Access Control gère l'accès du sous-réseau local aux réseaux côté WAN, y compris Internet et les autres sous-réseaux WAN.

    Trois modes de contrôle d'accès WAN sont disponibles :

    - **Unrestricted** : permet à ce sous-réseau d'accéder à Internet et aux autres sous-réseaux côté WAN sans restriction.

    - **Block WAN Subnet** : bloque l'accès aux autres sous-réseaux côté WAN. L'accès à Internet reste disponible.

    - **Block Internet Access** : bloque tout accès sortant, y compris Internet et les sous-réseaux côté WAN.

### Serveur DHCP

Le **DHCP Server** est activé par défaut. Le serveur DHCP attribue automatiquement des adresses IP et d'autres paramètres de communication à chaque appareil client.

Si le serveur DHCP est désactivé, vous devrez configurer manuellement les paramètres réseau des appareils clients. Cliquez [ici](../tutorials/manually_configure_static_ip.md) pour apprendre à configurer manuellement une IP statique.

Vous pouvez modifier les adresses IP de début et de fin selon vos besoins, par exemple si votre réseau s'agrandit ou se réduit, si des conflits d'adresses IP se produisent ou si la plage du masque de sous-réseau est modifiée.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Cliquez sur **Advanced** pour une configuration supplémentaire si nécessaire.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time** : période pendant laquelle une adresse IP attribuée par DHCP reste valide pour un appareil.

- **Gateway** : appareil qui route le trafic entre le réseau local et les réseaux externes tels qu'Internet.

- **DNS Server** : deux champs de serveur DNS sont disponibles pour configurer les résolveurs principal et secondaire.

    **Note** : le DNS principal est saisi dans le champ supérieur et le DNS secondaire dans le champ inférieur. Si le serveur principal n'est pas disponible, les appareils clients basculent automatiquement vers le résolveur secondaire, ce qui assure la continuité de la résolution des noms de domaine.

- **LPR Server** (Line Printer Remote Server) : service qui gère les travaux d'impression et permet aux appareils réseau d'envoyer des demandes d'impression à des imprimantes distantes. Plusieurs ports d'imprimante LPR peuvent être configurés.

## IoT Network

IoT Network crée un réseau Wi-Fi dédié aux appareils IoT. Isolé du réseau principal, il offre une meilleure compatibilité et une sécurité renforcée.

**Note** : Certains modèles, par exemple GL-MT5000 et GL-MT2500/GL-MT2500A, ne disposent pas de fonction Wi-Fi ; les paramètres IoT Network ne sont donc pas disponibles dans leur panneau d'administration Web.

Dans IoT Network, vous pouvez voir directement l'état de l'interface, le VLAN ID, la passerelle et la plage DHCP.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Cliquez sur **Edit** dans le coin inférieur droit ; le panneau de configuration IoT Network s'ouvre sur le côté droit de la page. Vous pouvez configurer Basic Settings et DHCP Server Settings dans ce panneau.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Paramètres de base

Vous pouvez définir le sous-réseau dans les plages d'adresses IPv4 privées : `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    La **passerelle par défaut** de IoT Network est **192.168.10.1**. Si elle entre en conflit avec votre réseau local, remplacez-la par une autre adresse.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez aussi sélectionner **255.255.0.0** si vous avez besoin d'un sous-réseau plus grand avec plus d'adresses IP.

- **VLAN ID**

    Le VLAN ID par défaut de IoT Network est **10** et peut être modifié selon vos besoins.

- **AP Isolation**

    Cette fonction est disponible depuis le firmware v4.5.

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Ces appareils ne pourront pas communiquer avec les autres appareils du même réseau.

- **WAN Access Control**

    WAN Access Control gère l'accès du sous-réseau local aux réseaux côté WAN, y compris Internet et les autres sous-réseaux WAN.

    Trois modes de contrôle d'accès WAN sont disponibles :

    - **Unrestricted** : permet à ce sous-réseau d'accéder à Internet et aux autres sous-réseaux côté WAN sans restriction.

    - **Block WAN Subnet** : bloque l'accès aux autres sous-réseaux côté WAN. L'accès à Internet reste disponible.

    - **Block Internet Access** : bloque tout accès sortant, y compris Internet et les sous-réseaux côté WAN.

### Serveur DHCP

Le **DHCP Server** est activé par défaut. Le serveur DHCP attribue automatiquement des adresses IP et d'autres paramètres de communication à chaque appareil client.

Si le serveur DHCP est désactivé, vous devrez configurer manuellement les paramètres réseau des appareils clients. Cliquez [ici](../tutorials/manually_configure_static_ip.md) pour apprendre à configurer manuellement une IP statique.

Vous pouvez modifier les adresses IP de début et de fin selon vos besoins, par exemple si votre réseau s'agrandit ou se réduit, si des conflits d'adresses IP se produisent ou si la plage du masque de sous-réseau est modifiée.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Cliquez sur **Advanced** pour une configuration supplémentaire si nécessaire.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time** : période pendant laquelle une adresse IP attribuée par DHCP reste valide pour un appareil.

- **Gateway** : appareil qui route le trafic entre le réseau local et les réseaux externes tels qu'Internet.

- **DNS Server** : deux champs de serveur DNS sont disponibles pour configurer les résolveurs principal et secondaire.

    **Note** : le DNS principal est saisi dans le champ supérieur et le DNS secondaire dans le champ inférieur. Si le serveur principal n'est pas disponible, les appareils clients basculent automatiquement vers le résolveur secondaire, ce qui assure la continuité de la résolution des noms de domaine.

- **LPR Server** (Line Printer Remote Server) : service qui gère les travaux d'impression et permet aux appareils réseau d'envoyer des demandes d'impression à des imprimantes distantes. Plusieurs ports d'imprimante LPR peuvent être configurés.

## VLAN Networks

En haut de la page principale, vous pouvez créer des **VLAN networks** supplémentaires selon vos besoins afin d'isoler différents types d'appareils ou le trafic des visiteurs.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Cliquez sur le bouton **+ Add** à droite de la page pour configurer un nouveau réseau.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Paramètres de base

Vous pouvez configurer les informations de base des **VLAN Networks** sur cette page.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Personnalisez le nom du sous-réseau nouvellement créé pour l'identifier.

- **Gateway**

    Configurez manuellement la passerelle du nouveau sous-réseau. Remplacez cette passerelle si elle entre en conflit avec votre segment LAN existant.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez aussi sélectionner **255.255.0.0** si vous avez besoin d'un sous-réseau plus grand avec plus d'adresses IP.

- **VLAN ID**

    Lorsque vous créez un sous-réseau, vous devez attribuer un VLAN ID compris entre **9** et **4000**. Évitez d'utiliser un VLAN ID déjà occupé afin d'éviter les conflits réseau.

- **AP Isolation**

    Cette fonction est disponible depuis le firmware v4.5.

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Ces appareils ne pourront pas communiquer avec les autres appareils du même réseau.

- **WAN Access Control**

    WAN Access Control gère l'accès du sous-réseau local aux réseaux côté WAN, y compris Internet et les autres sous-réseaux WAN.

    Trois modes de contrôle d'accès WAN sont disponibles :

    - **Unrestricted** : permet à ce sous-réseau d'accéder à Internet et aux autres sous-réseaux côté WAN sans restriction.

    - **Block WAN Subnet** : bloque l'accès aux autres sous-réseaux côté WAN. L'accès à Internet reste disponible.

    - **Block Internet Access** : bloque tout accès sortant, y compris Internet et les sous-réseaux côté WAN.

### Serveur DHCP

Le **DHCP Server** est activé par défaut. Le serveur DHCP attribue automatiquement des adresses IP et d'autres paramètres de communication à chaque appareil client.

Si le serveur DHCP est désactivé, vous devrez configurer manuellement les paramètres réseau des appareils clients. Cliquez [ici](../tutorials/manually_configure_static_ip.md) pour apprendre à configurer manuellement une IP statique.

Vous pouvez modifier les adresses IP de début et de fin selon vos besoins, par exemple si votre réseau s'agrandit ou se réduit, si des conflits d'adresses IP se produisent ou si la plage du masque de sous-réseau est modifiée.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Cliquez sur **Advanced** pour une configuration supplémentaire si nécessaire.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time** : période pendant laquelle une adresse IP attribuée par DHCP reste valide pour un appareil.

- **Gateway** : appareil qui route le trafic entre le réseau local et les réseaux externes tels qu'Internet.

- **DNS Server** : deux champs de serveur DNS sont disponibles pour configurer les résolveurs principal et secondaire.

    **Note** : le DNS principal est saisi dans le champ supérieur et le DNS secondaire dans le champ inférieur. Si le serveur principal n'est pas disponible, les appareils clients basculent automatiquement vers le résolveur secondaire, ce qui assure la continuité de la résolution des noms de domaine.

- **LPR Server** (Line Printer Remote Server) : service qui gère les travaux d'impression et permet aux appareils réseau d'envoyer des demandes d'impression à des imprimantes distantes. Plusieurs ports d'imprimante LPR peuvent être configurés.

Une fois configuré, le nouveau réseau VLAN apparaît sur la page actuelle avec les informations de sous-réseau.

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

