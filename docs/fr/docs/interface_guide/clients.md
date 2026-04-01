# Clients

Sur le côté gauche du panneau d’administration web, allez à **CLIENTS**.

La page Clients affiche, de gauche à droite, des informations sur les appareils connectés, notamment le nom de l’appareil, le type de connexion, l’adresse IP, l’adresse MAC, la vitesse et le trafic.

## Nom de l’appareil

La première colonne affiche le nom et le type de l’appareil, en fonction du nom d’hôte de l’appareil.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Pour modifier le nom et le type de l’appareil, cliquez sur l’icône à trois points dans la colonne Action, puis dans le menu déroulant, cliquez sur **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Type de connexion

L’icône bleue à droite du nom de l’appareil représente le type ou la méthode de connexion de l’appareil.

Elle indique comment l’appareil est connecté au réseau, que ce soit via le Wi-Fi ou un câble Ethernet.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## Adresse IP et MAC

La deuxième colonne répertorie les adresses IP et MAC de l’appareil connecté.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

De nombreux appareils utilisent des adresses MAC aléatoires. Si les appareils connectés utilisent des adresses MAC aléatoires, l’invite suivante s’affiche.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Note** : La règle utilisée ici est la suivante : si le deuxième caractère de l’adresse MAC est 2, 6, A ou E (sans tenir compte de la casse), elle est considérée comme une adresse MAC aléatoire. Toutefois, certains appareils peuvent utiliser une règle différente pour générer une adresse MAC aléatoire ; cette méthode de détection peut donc ne pas être exacte.

## Vitesse

La troisième colonne affiche la vitesse Internet de l’appareil connecté.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

La vitesse indiquée ici correspond à la vitesse moyenne sur 3 minutes.

- Si cette page reste ouverte pendant 10 secondes, la vitesse moyenne des 10 dernières secondes est affichée.
- Si cette page reste ouverte pendant 30 secondes, la vitesse moyenne des 30 dernières secondes est affichée.
- Si cette page reste ouverte pendant 60 secondes, la vitesse moyenne des 60 dernières secondes est affichée.
- Si cette page reste ouverte pendant 3 minutes, le débit moyen des 3 dernières minutes est affiché.
- Si cette page reste ouverte pendant 10 minutes, le débit moyen des 3 dernières minutes est affiché.

## Trafic

La quatrième colonne affiche le trafic Internet de l’appareil connecté.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## IP réservée

Dans la cinquième colonne, vous pouvez réserver une adresse IP pour un appareil connecté donné en un seul clic.

Cette fonctionnalité est disponible à partir de la v4.8.

Lorsque vous définissez une adresse IP réservée pour un client au sein du LAN, ce client reçoit toujours la même adresse IP à chaque connexion au serveur DHCP du routeur.

Vous pouvez attribuer des adresses IP réservées aux ordinateurs ou serveurs qui nécessitent une configuration IP permanente.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Liste de blocage {#blocklist}

Dans la sixième colonne, vous pouvez bloquer des appareils connectés spécifiques en un seul clic.

La règle de contrôle d’accès est **Blocklist** par défaut ; vous pouvez la basculer sur **Allowlist** depuis le haut de la page si nécessaire.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist** : les appareils dont les adresses MAC figurent dans la liste de blocage ne sont pas autorisés à se connecter à ce routeur.

- **Allowlist** : seuls les appareils avec des adresses MAC spécifiques sont autorisés à se connecter ; cette option convient aux appareils IoT et à la gestion de réseaux d’entreprise.

Pour créer une Blocklist, vous pouvez importer une liste de blocage au format Excel à **(1)**, ou saisir manuellement des adresses MAC à **(2)**.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Méthode 1. Importer des clients**

Dans la page Access Control, cliquez sur **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Cliquez sur **Download Import Template** pour télécharger une feuille XLS nommée "mac-template.csv".

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Ouvrez le fichier, ajoutez les adresses MAC, puis enregistrez-le.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Sélectionnez le fichier enregistré ou faites-le glisser dans la zone de téléversement.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Une fois le téléversement réussi, cliquez sur **Import** pour terminer l’importation par lot des adresses MAC.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Méthode 2. Saisie manuelle**

Dans la page Access Control, saisissez manuellement l’adresse MAC des appareils que vous souhaitez bloquer, puis cliquez sur **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Note** : Le blocage des clients repose sur l’adresse MAC de l’appareil. Si l’appareil bloqué utilise une adresse MAC différente lors d’une prochaine connexion, il pourra toujours se connecter au routeur.

## Tri

Le type de tri actuel s’affiche dans le coin supérieur droit, et vous pouvez le remplacer par un autre type de tri.

Le tri par défaut est le suivant :

- L’appareil utilisé actuellement est toujours affiché en haut.
- Dans la section des clients en ligne, plus l’appareil s’est connecté récemment, plus il apparaît haut dans la liste.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Action

### Détails du client

Si vous devez consulter les détails d’un appareil client, cliquez sur l’icône à trois points dans la colonne Action tout à droite, puis cliquez sur **View Details** dans le menu déroulant.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Vous pouvez voir toutes les informations concernant l’appareil client dans la sous-page ouverte, y compris toutes les adresses IPv6 de l’appareil le cas échéant.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modifier

Cliquez sur l’icône à trois points dans la colonne Action, puis dans le menu déroulant, cliquez sur **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Limiter la vitesse

Cliquez sur l’icône à trois points dans la colonne Action, puis dans le menu déroulant, cliquez sur **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Si une limitation de vitesse est appliquée à un client, les flèches montante et descendante de sa vitesse deviennent jaunes.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

Cliquez sur l’icône à trois points dans la colonne Action pour désactiver la limitation de vitesse.

### Utiliser un tunnel VPN

**Note** : Cette option est disponible à partir du firmware v4.8 et n’apparaît dans le menu Action que si une politique basée sur l’adresse MAC est configurée.

Ajoutez un client à la liste du tunnel VPN avec une politique basée sur l’adresse MAC. Si vous devez ajuster les tunnels plus en détail, allez dans le VPN Dashboard pour les gérer.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Supprimer les clients hors ligne

Dans la section des clients hors ligne, vous pouvez cliquer sur **Delete All** en haut à droite pour supprimer tous les clients hors ligne.

Si vous souhaitez supprimer un client spécifique, cliquez sur l’icône à trois points dans la colonne Action, puis dans le menu déroulant, cliquez sur **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
