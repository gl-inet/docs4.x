# FAQ de dépannage de la connexion Internet {#internet-connection-troubleshooting-faq}

## Q1. Que dois-je faire si je n'arrive pas à accéder à Internet ? {#q1-what-should-i-do-if-i-cannot-access-the-internet}

Suivez les étapes ci-dessous pour effectuer un dépannage de base.

1. Vérifiez la connexion physique.

    Assurez-vous que le câble Ethernet est correctement connecté entre le port WAN de votre routeur et l'appareil amont (par ex. modem, ONT ou prise Ethernet). Vérifiez les LED de l'appareil amont et assurez-vous qu'il y a bien une transmission active.

2. Redémarrez les appareils.

    Éteignez l'appareil amont (par ex. le modem) ainsi que votre routeur. Attendez 1 à 2 minutes. Rallumez ensuite d'abord le modem, attendez qu'il soit complètement en ligne, puis rallumez le routeur.

3. Vérifiez l'adresse IP WAN.

    Connectez-vous au panneau d'administration web de votre routeur et accédez à la section **INTERNET** -> **Ethernet**. S'il reste bloqué dans l'état de connexion, comme illustré ci-dessous, cela peut indiquer un problème de DHCP, un **MAC binding** ou la nécessité d'un VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Contactez votre FAI et vérifiez si vous avez besoin d'un **nom d'utilisateur PPPoE**, d'un **mot de passe PPPoE** et d'un **VLAN ID** pour accéder à Internet.

    Vérifiez également si votre FAI a déjà configuré un **MAC binding** sur votre modem/ONT.

## Q2. Quand dois-je cloner une adresse MAC ? {#q2-when-should-i-clone-a-mac-address}

Certains FAI associent votre connexion haut débit à l'adresse MAC du premier appareil connecté, généralement votre ancien routeur ou votre ordinateur. Lorsque vous remplacez votre routeur, il peut être nécessaire de cloner l'adresse MAC pour rétablir l'accès à Internet.

Suivez les étapes ci-dessous pour cloner une adresse MAC sur votre routeur GL.iNet.

1. Notez l'adresse MAC de votre ancien routeur (ou de l'ordinateur précédemment associé à votre accès haut débit).

2. Connectez-vous au panneau d'administration web de votre routeur et accédez à **NETWORK** -> **Ethernet Port** (nommé **Port Management** dans certaines versions du firmware). Réglez **MAC Mode** sur **Clone** ou **Manual**, saisissez manuellement l'adresse MAC, puis cliquez sur **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Redémarrez votre modem (c'est-à-dire l'appareil amont).

## Q3. Quand dois-je configurer un VLAN ID ? {#q3-when-do-i-need-to-configure-a-vlan-id}

Certains FAI exigent un balisage VLAN pour l'authentification Internet ou la séparation du trafic, en particulier avec les connexions fibre et IPTV. Contactez votre FAI et vérifiez si un VLAN ID est requis.

Suivez les étapes ci-dessous pour configurer le VLAN ID.

1. Connectez-vous à votre routeur et accédez à la section **INTERNET** -> **Ethernet**. Cliquez sur **Modify**.

2. Saisissez le VLAN ID fourni par votre FAI, puis cliquez sur **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## Q4. Et si cela ne fonctionne toujours pas ? {#q4-what-if-it-still-doesnt-work}

Si le problème persiste, essayez de connecter directement un PC ou un ordinateur portable à votre modem et vérifiez si vous avez accès à Internet.

Si vous n'avez pas accès à Internet, le problème peut venir de votre FAI. Contactez votre FAI pour obtenir une assistance supplémentaire.

Si vous avez accès à Internet, le problème peut être lié à la configuration de votre routeur. Contactez notre support technique à l'adresse [support@gl-inet.com](mailto:support@gl-inet.com) et fournissez les informations suivantes :

- Modèle du routeur
- Étapes de dépannage déjà effectuées
- Nom de votre FAI
- Toute autre information qui pourrait nous aider à vous assister

## Informations sur les FAI {#isp-information}

Vous trouverez ci-dessous des informations sur les FAI par région, compilées par GL.iNet à partir des retours clients, des forums et des ressources OpenWRT, à titre de référence uniquement.

| Pays/Région   | FAI   | Type de connexion | VLAN ID | Clonage MAC requis | Exigences supplémentaires |
| :------------ | :---- | :---------------- | :------ | :----------------- | :------------------------ |
| États-Unis | AT&T Fiber | DHCP (IP Passthrough) | N/A | Non | Activation d'IP Passthrough obligatoire ; contournement de l'authentification EAP nécessaire |
| États-Unis | Spectrum | DHCP | N/A | Oui (dans certaines zones) | Liaison MAC stricte (redémarrage du modem requis) |
| États-Unis | Verizon Fios | DHCP | N/A | Non | |
| États-Unis | Comcast Xfinity | DHCP | N/A | Oui (fréquent) | Redémarrage du modem obligatoire lors d'un changement de routeur (libération de la MAC) |
| États-Unis | Cox Communications | DHCP | N/A | Oui | Redémarrage du modem obligatoire lors d'un changement de routeur (libération de la MAC) |
| États-Unis | Frontier Fiber | DHCP | N/A | Non | |
| États-Unis | CenturyLink / Lumen | PPPoE | 201 | Non | Des VLAN sont requis dans certaines zones. |
| Canada | Bell Canada Fibe | PPPoE | 35 | Non | |
| Allemagne | Deutsche Telekom | PPPoE | 7 | Non | VLAN 7 obligatoire pour Internet ; identifiants PPPoE requis |
| Allemagne | Vodafone (Kabel) | DHCP | N/A | Oui (parfois) | Une liaison MAC peut s'appliquer ; redémarrez le modem après un changement de routeur |
| Allemagne | 1&1 / O2 (Telekom line) | PPPoE | 7 | Non | VLAN 7 obligatoire pour Internet |
| Allemagne | DNS:NET | PPPoE | 37 | Non | |
| Allemagne | o2(UGG) | PPPoE | 7 | Non | |
| Royaume-Uni | BT Broadband | PPPoE | 101 | Non | VLAN 101 requis ; identifiants de connexion PPPoE nécessaires |
| Royaume-Uni | Sky Broadband | DHCP (Option 61) | 101 | Non | Nécessite DHCP Option 61 (identifiant client) |
| Royaume-Uni | Virgin | DHCP | N/A | Oui | Le modem est en mode pont et nécessite le clonage MAC. |
| France | Orange | DHCP / PPPoE | 832 | Non | VLAN 832 requis ; une authentification Option 90 peut être nécessaire |
| France | Free (Freebox) | DHCP | N/A | Non | |
| France | Bouygues Telecom | DHCP | 100 | Oui | Cloner l'adresse MAC de la Bbox |
| Espagne | Movistar | PPPoE | 6 | Non | VLAN 6 (Internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Espagne | DIGI | PPPoE | 20 | Non | |
| Espagne | Orange | DHCP | 832/835 | Non | Les VLAN peuvent varier selon la région |
| Italie | TIM | PPPoE | 835 | Non | VLAN 835 requis |
| Italie | Aruba | PPPoE | 835 | Non | |
| Pays-Bas | KPN | DHCP | 6 | Non | VLAN 6 requis pour Internet |
| Pays-Bas | Tweak | DHCP | 34 | Oui | Cloner l'adresse MAC de l'Experia Box |
| Pays-Bas | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | Non | |
| Pays-Bas | Odido | DHCP | 300 | Non | |
| Belgique | EDPnet | PPPoE | 10 | Non | |
| Bosnie-Herzégovine | BH Telecom | PPPoE | 100 | Non | |
| Croatie | Terrakom | PPPoE | 905 | Non | |
| République tchèque | O2 | PPPoE | 848 | Non | |
| Chypre | Epic | PPPoE | 35 | Non | |
| Chypre | Cyta | PPPoE | 42 | Non | |
| Chypre | Cablenet | PPPoE | 42 | Non | |
| Chypre | Primetel | PPPoE | 42 | Non | |
| Pologne | Orange Polska | PPPoE | 35 | Non | VLAN 35 requis |
| Pologne | T-mobile | PPPoE | 35 | Non | |
| Irlande | Vodafone SIRO | PPPoE | 10 | Non | |
| Irlande | Pure Telecom | PPPoE | 10 | Non | |
| Autriche | A1 Telekom | PPPoE | 2 | Non | |
| Autriche | Fonira | PPPoE | 31 | Non | |
| Turquie | Turknet | PPPoE | 35 | Non | |
| Turquie | Turk Telekom | PPPoE | 35 | Non | |
| Turquie | Turkcell Superonline | PPPoE | N/A | Oui | |
| Turquie | Turksat Kablonet | DHCP/PPPoE | N/A | Non | |
| Grèce | Cosmote | PPPoE | 835 | Non | |
| Grèce | Nova | PPPoE | 835 | Oui | |
| Grèce | DEI/PPC | DHCP | 835 | Non | |
| Japon | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | Non | IPoE nécessite un routeur compatible MAP-E/DS-Lite |
| Japon | SoftBank Hikari | PPPoE / IPoE | N/A | Non | Le service IPoE de BBIX est couramment utilisé |
| Inde | Airtel | PPPoE / DHCP | N/A | Non | PPPoE requis dans certaines régions |
| Inde | JioFiber | DHCP | N/A | Non | ONT verrouillé dans de nombreux cas |
| Singapour | Singtel | PPPoE | 10 | Non | VLAN 10 requis ; IPTV sur un VLAN distinct |
| Singapour | StarHub | DHCP | N/A | Non | Connexion basée sur DHCP |
| Australie | NBN (divers FAI) | PPPoE / DHCP | 2 (courant) | Oui | VLAN 2 courant, mais dépend du FAI |
