# LAN {#lan}

**Remarque** : Ce guide s’applique aux appareils équipés du firmware v4.11 ou d’une version ultérieure. Si votre appareil utilise une autre version du firmware, sélectionnez le guide correspondant ci-dessous.

<div class="gl-link-select" data-label="Version du firmware" data-placeholder="Firmware v4.11 et versions ultérieures" markdown="1">

- [Firmware v4.9 et versions antérieures](lan.md)

</div>

---

Dans le menu de gauche du panneau d’administration Web, accédez à **NETWORK** -> **LAN**.

Cette page regroupe les paramètres du réseau principal (**Main Network**), du réseau invité (**Guest Network**), du réseau IoT (**IoT Network**) et des réseaux VLAN personnalisés (**VLAN Networks**). Vous pouvez créer et gérer plusieurs sous-réseaux pour isoler différents types d’appareils ou de trafic.

## Réseau principal {#main-network}

Votre appareil se connecte au réseau principal par le Wi-Fi principal ou par un câble Ethernet.

La section **Main Network** affiche l’état de toutes les interfaces, l’identifiant VLAN, l’adresse IP du routeur et la plage d’adresses DHCP.

![Vue d’ensemble du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Cliquez sur **Edit** dans le coin inférieur droit pour configurer le réseau principal.

![Configuration du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

La page de configuration contient les paramètres de base, les paramètres du serveur DHCP et les réservations d’adresses IP.

### Paramètres de base {#basic-settings}

Vous pouvez définir le sous-réseau dans l’une des plages d’adresses IPv4 privées suivantes : `192.168.0.0/16`, `172.16.0.0/12` et `10.0.0.0/8`.

![Paramètres de base du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Saisissez cette adresse dans la barre d’adresse de votre navigateur pour accéder au panneau d’administration du routeur.

    L’adresse par défaut est **192.168.8.1**. Vous pouvez la modifier si elle entre en conflit avec votre réseau.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez sélectionner **255.255.0.0** si vous avez besoin d’un sous-réseau plus grand offrant davantage d’adresses IP.

- **VLAN ID**

    L’identifiant VLAN du réseau principal est fixé à **1**.

- **AP Isolation**

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Les appareils ainsi isolés ne peuvent plus communiquer avec les autres appareils du même réseau.

    **Remarque** : L’isolation des clients s’applique uniquement aux appareils connectés en Wi-Fi.

### Serveur DHCP {#dhcp-server}

Le serveur DHCP (**DHCP Server**) est activé par défaut. Il attribue automatiquement une adresse IP et d’autres paramètres réseau à chaque appareil client.

Si le serveur DHCP est désactivé, vous devez configurer manuellement les paramètres réseau des appareils clients. Consultez le guide pour [configurer manuellement une adresse IP statique](../tutorials/manually_configure_static_ip.md).

Vous pouvez modifier les adresses IP de début et de fin de la plage DHCP, par exemple si la taille du réseau change, si des conflits d’adresses IP surviennent ou si le masque de sous-réseau change.

![Paramètres DHCP de base du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Cliquez sur **Advanced** pour accéder aux paramètres avancés.

![Accès aux paramètres DHCP avancés du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Paramètres DHCP avancés du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indique la durée de validité de l’adresse IP attribuée à un appareil par DHCP.

- **Gateway** désigne l’appareil qui achemine le trafic entre le réseau local et les réseaux externes comme Internet.

- **DNS Server 1** indique le serveur DNS principal, qui traduit les noms de domaine en adresses IP.

- **DNS Server 2** indique le serveur DNS secondaire, qui résout les noms de domaine lorsque le serveur principal est indisponible.

- **LPR Server** (Line Printer Remote Server) est un service qui gère les travaux d’impression et permet aux appareils du réseau d’envoyer des demandes d’impression à des imprimantes distantes. Vous pouvez configurer plusieurs ports d’impression LPR.

### Réservation d’adresses IP {#address-reservation}

Lorsqu’une adresse IP est réservée à un client du réseau local, le serveur DHCP du routeur lui attribue cette même adresse à chaque demande. Vous pouvez réserver une adresse IP aux ordinateurs ou aux serveurs qui nécessitent une configuration IP permanente.

**Remarque** : Les appareils clients concernés doivent se reconnecter au routeur pour que la réservation prenne effet.

Cliquez sur **Add** pour réserver une adresse IP.

![Liste des réservations d’adresses IP du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Une fenêtre s’ouvre.

![Fenêtre d’ajout d’une réservation d’adresse IP du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Sélectionnez une adresse **MAC** dans la liste déroulante. Le champ **IP** se remplit automatiquement avec l’adresse disponible correspondante. Vous pouvez saisir un nom d’hôte et un nom personnalisé pour identifier facilement l’appareil. Cliquez ensuite sur **Submit**.

![Exemple de réservation d’adresse IP du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

La nouvelle réservation d’adresse IP apparaît sur la page, comme illustré ci-dessous.

![Nouvelle réservation d’adresse IP du réseau principal](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Réseau invité {#guest-network}

Le réseau invité offre aux visiteurs un accès à Internet via un réseau Wi-Fi dédié. Il est isolé du réseau principal pour renforcer la sécurité.

**Remarque** : Certains modèles, dont les GL-MT5000 et GL-MT2500/GL-MT2500A, ne disposent pas du Wi-Fi. Les paramètres du réseau invité sont donc indisponibles dans leur panneau d’administration Web.

La section **Guest Network** affiche l’état de l’interface, l’identifiant VLAN, la passerelle et la plage d’adresses DHCP.

![Vue d’ensemble du réseau invité](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Cliquez sur **Edit** dans le coin inférieur droit pour ouvrir le panneau de configuration du réseau invité à droite de la page.

![Configuration du réseau invité](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

La page de configuration contient les paramètres de base et les paramètres du serveur DHCP.

### Paramètres de base {#guest-network-basic-settings}

Vous pouvez définir le sous-réseau dans l’une des plages d’adresses IPv4 privées suivantes : `192.168.0.0/16`, `172.16.0.0/12` et `10.0.0.0/8`.

![Paramètres de base du réseau invité](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    La **passerelle par défaut** du réseau invité est **192.168.9.1**. Si cette adresse entre en conflit avec votre réseau local, choisissez-en une autre.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez sélectionner **255.255.0.0** si vous avez besoin d’un sous-réseau plus grand offrant davantage d’adresses IP.

- **VLAN ID**

    L’identifiant VLAN par défaut du réseau invité est **9**. Vous pouvez le modifier selon vos besoins.

- **Associated LAN Ports**

    Sélectionnez les ports LAN à associer à ce sous-réseau. Les appareils reliés par câble à ces ports rejoindront ce réseau.

- **AP Isolation**

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Les appareils ainsi isolés ne peuvent plus communiquer avec les autres appareils du même réseau.

    **Remarque** : L’isolation des clients s’applique uniquement aux appareils connectés en Wi-Fi.

- **WAN Access Control**

    L’option **WAN Access Control** contrôle l’accès du sous-réseau local à Internet et aux autres sous-réseaux côté WAN.

    Trois modes de contrôle d’accès WAN sont disponibles.

    - **Unrestricted** autorise ce sous-réseau à accéder sans restriction à Internet et aux autres sous-réseaux côté WAN.

    - **Block WAN Subnet** bloque l’accès aux autres sous-réseaux côté WAN. L’accès à Internet reste disponible.

    - **Block Internet Access** bloque tout accès sortant, y compris l’accès à Internet et aux sous-réseaux côté WAN.

### Serveur DHCP {#guest-network-dhcp-server}

Le serveur DHCP (**DHCP Server**) est activé par défaut. Il attribue automatiquement une adresse IP et d’autres paramètres réseau à chaque appareil client.

Si le serveur DHCP est désactivé, vous devez configurer manuellement les paramètres réseau des appareils clients. Consultez le guide pour [configurer manuellement une adresse IP statique](../tutorials/manually_configure_static_ip.md).

Vous pouvez modifier les adresses IP de début et de fin de la plage DHCP, par exemple si la taille du réseau change, si des conflits d’adresses IP surviennent ou si le masque de sous-réseau change.

![Paramètres DHCP de base du réseau invité](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Cliquez sur **Advanced** pour accéder aux paramètres avancés.

![Accès aux paramètres DHCP avancés du réseau invité](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Paramètres DHCP avancés du réseau invité](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indique la durée de validité de l’adresse IP attribuée à un appareil par DHCP.

- **Gateway** désigne l’appareil qui achemine le trafic entre le réseau local et les réseaux externes comme Internet.

- **DNS Server 1** indique le serveur DNS principal, qui traduit les noms de domaine en adresses IP.

- **DNS Server 2** indique le serveur DNS secondaire, qui résout les noms de domaine lorsque le serveur principal est indisponible.

- **LPR Server** (Line Printer Remote Server) est un service qui gère les travaux d’impression et permet aux appareils du réseau d’envoyer des demandes d’impression à des imprimantes distantes. Vous pouvez configurer plusieurs ports d’impression LPR.

## Réseau IoT {#iot-network}

Le réseau IoT fournit un réseau Wi-Fi dédié aux objets connectés. Il est isolé du réseau principal et offre une meilleure compatibilité ainsi qu’une sécurité renforcée.

**Remarque** : Certains modèles, dont les GL-MT5000 et GL-MT2500/GL-MT2500A, ne disposent pas du Wi-Fi. Les paramètres du réseau IoT sont donc indisponibles dans leur panneau d’administration Web.

La section **IoT Network** affiche l’état de l’interface, l’identifiant VLAN, la passerelle et la plage d’adresses DHCP.

![Vue d’ensemble du réseau IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Cliquez sur **Edit** dans le coin inférieur droit pour ouvrir le panneau de configuration du réseau IoT à droite de la page. Vous pouvez y modifier les paramètres de base et les paramètres du serveur DHCP.

![Configuration du réseau IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Paramètres de base {#iot-network-basic-settings}

Vous pouvez définir le sous-réseau dans l’une des plages d’adresses IPv4 privées suivantes : `192.168.0.0/16`, `172.16.0.0/12` et `10.0.0.0/8`.

![Paramètres de base du réseau IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    La **passerelle par défaut** du réseau IoT est **192.168.10.1**. Si cette adresse entre en conflit avec votre réseau local, choisissez-en une autre.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez sélectionner **255.255.0.0** si vous avez besoin d’un sous-réseau plus grand offrant davantage d’adresses IP.

- **VLAN ID**

    L’identifiant VLAN par défaut du réseau IoT est **10**. Vous pouvez le modifier selon vos besoins.

- **Associated LAN Ports**

    Sélectionnez les ports LAN à associer à ce sous-réseau. Les appareils reliés par câble à ces ports rejoindront ce réseau.

- **AP Isolation**

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Les appareils ainsi isolés ne peuvent plus communiquer avec les autres appareils du même réseau.

    **Remarque** : L’isolation des clients s’applique uniquement aux appareils connectés en Wi-Fi.

- **WAN Access Control**

    L’option **WAN Access Control** contrôle l’accès du sous-réseau local à Internet et aux autres sous-réseaux côté WAN.

    Trois modes de contrôle d’accès WAN sont disponibles.

    - **Unrestricted** autorise ce sous-réseau à accéder sans restriction à Internet et aux autres sous-réseaux côté WAN.

    - **Block WAN Subnet** bloque l’accès aux autres sous-réseaux côté WAN. L’accès à Internet reste disponible.

    - **Block Internet Access** bloque tout accès sortant, y compris l’accès à Internet et aux sous-réseaux côté WAN.

### Serveur DHCP {#iot-network-dhcp-server}

Le serveur DHCP (**DHCP Server**) est activé par défaut. Il attribue automatiquement une adresse IP et d’autres paramètres réseau à chaque appareil client.

Si le serveur DHCP est désactivé, vous devez configurer manuellement les paramètres réseau des appareils clients. Consultez le guide pour [configurer manuellement une adresse IP statique](../tutorials/manually_configure_static_ip.md).

Vous pouvez modifier les adresses IP de début et de fin de la plage DHCP, par exemple si la taille du réseau change, si des conflits d’adresses IP surviennent ou si le masque de sous-réseau change.

![Paramètres DHCP de base du réseau IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Cliquez sur **Advanced** pour accéder aux paramètres avancés.

![Accès aux paramètres DHCP avancés du réseau IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Paramètres DHCP avancés du réseau IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indique la durée de validité de l’adresse IP attribuée à un appareil par DHCP.

- **Gateway** désigne l’appareil qui achemine le trafic entre le réseau local et les réseaux externes comme Internet.

- **DNS Server 1** indique le serveur DNS principal, qui traduit les noms de domaine en adresses IP.

- **DNS Server 2** indique le serveur DNS secondaire, qui résout les noms de domaine lorsque le serveur principal est indisponible.

- **LPR Server** (Line Printer Remote Server) est un service qui gère les travaux d’impression et permet aux appareils du réseau d’envoyer des demandes d’impression à des imprimantes distantes. Vous pouvez configurer plusieurs ports d’impression LPR.

## Réseaux VLAN {#vlan-networks}

En haut de la page principale, vous pouvez créer d’autres réseaux VLAN pour isoler différents types d’appareils ou le trafic des visiteurs.

![Vue d’ensemble des réseaux VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Cliquez sur **+ Add** à droite de la page pour configurer un nouveau réseau.

![Configuration des réseaux VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Paramètres de base {#vlan-networks-basic-settings}

Cette page permet de configurer les paramètres de base des réseaux VLAN.

![Paramètres de base des réseaux VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Attribuez un nom au nouveau sous-réseau pour l’identifier.

- **Gateway**

    Configurez manuellement la passerelle du nouveau sous-réseau. Modifiez son adresse si elle entre en conflit avec le segment LAN existant.

- **Netmask**

    La valeur par défaut est **255.255.255.0**. Vous pouvez sélectionner **255.255.0.0** si vous avez besoin d’un sous-réseau plus grand offrant davantage d’adresses IP.

- **VLAN ID**

    Lors de la création d’un sous-réseau, vous devez lui attribuer un identifiant VLAN compris entre **9** et **4000**. Choisissez un identifiant disponible pour éviter les conflits réseau.

- **Associated LAN Ports**

    Sélectionnez les ports LAN à associer à ce sous-réseau. Les appareils reliés par câble à ces ports rejoindront ce réseau.

- **AP Isolation**

    Vous pouvez isoler les appareils clients dans un segment réseau distinct. Les appareils ainsi isolés ne peuvent plus communiquer avec les autres appareils du même réseau.

    **Remarque** : L’isolation des clients s’applique uniquement aux appareils connectés en Wi-Fi.

- **WAN Access Control**

    L’option **WAN Access Control** contrôle l’accès du sous-réseau local à Internet et aux autres sous-réseaux côté WAN.

    Trois modes de contrôle d’accès WAN sont disponibles.

    - **Unrestricted** autorise ce sous-réseau à accéder sans restriction à Internet et aux autres sous-réseaux côté WAN.

    - **Block WAN Subnet** bloque l’accès aux autres sous-réseaux côté WAN. L’accès à Internet reste disponible.

    - **Block Internet Access** bloque tout accès sortant, y compris l’accès à Internet et aux sous-réseaux côté WAN.

### Serveur DHCP {#vlan-networks-dhcp-server}

Le serveur DHCP (**DHCP Server**) est activé par défaut. Il attribue automatiquement une adresse IP et d’autres paramètres réseau à chaque appareil client.

Si le serveur DHCP est désactivé, vous devez configurer manuellement les paramètres réseau des appareils clients. Consultez le guide pour [configurer manuellement une adresse IP statique](../tutorials/manually_configure_static_ip.md).

Vous pouvez modifier les adresses IP de début et de fin de la plage DHCP, par exemple si la taille du réseau change, si des conflits d’adresses IP surviennent ou si le masque de sous-réseau change.

![Paramètres DHCP de base des réseaux VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Cliquez sur **Advanced** pour accéder aux paramètres avancés.

![Accès aux paramètres DHCP avancés des réseaux VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![Paramètres DHCP avancés des réseaux VLAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indique la durée de validité de l’adresse IP attribuée à un appareil par DHCP.

- **Gateway** désigne l’appareil qui achemine le trafic entre le réseau local et les réseaux externes comme Internet.

- **DNS Server 1** indique le serveur DNS principal, qui traduit les noms de domaine en adresses IP.

- **DNS Server 2** indique le serveur DNS secondaire, qui résout les noms de domaine lorsque le serveur principal est indisponible.

- **LPR Server** (Line Printer Remote Server) est un service qui gère les travaux d’impression et permet aux appareils du réseau d’envoyer des demandes d’impression à des imprimantes distantes. Vous pouvez configurer plusieurs ports d’impression LPR.

Une fois configuré, le nouveau réseau VLAN s’affiche sur la page avec les informations de son sous-réseau.

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
