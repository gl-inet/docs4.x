# FAQ de dépannage de la connexion Internet

## Q1. Que dois-je faire si je n'arrive pas à accéder à Internet ?

Suivez les étapes ci-dessous pour effectuer un dépannage de base.

1. Vérifiez la connexion physique.

    Assurez-vous que le câble Ethernet est correctement connecté entre le port WAN de votre routeur et l'appareil amont (par ex. modem, ONT ou prise Ethernet). Vérifiez les LED de l'appareil amont et assurez-vous qu'il y a bien une transmission active.

2. Redémarrez les appareils.

    Éteignez l'appareil amont (par ex. le modem) ainsi que votre routeur. Attendez 1 à 2 minutes. Rallumez ensuite d'abord le modem, attendez qu'il soit complètement en ligne, puis rallumez le routeur.

3. Vérifiez l'adresse IP WAN.

    Connectez-vous au panneau d'administration web de votre routeur et accédez à la section **INTERNET** -> **Ethernet**. S'il reste bloqué sur l'état de connexion, comme illustré ci-dessous, cela peut indiquer un problème de DHCP, un **MAC binding** ou la nécessité d'un VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Contactez votre FAI et vérifiez si vous avez besoin d'un **nom d'utilisateur PPPoE**, d'un **mot de passe PPPoE** et d'un **VLAN ID** pour accéder à Internet.

    Vérifiez également si votre FAI a déjà configuré un **MAC binding** sur votre modem/ONT.

## Q2. Quand dois-je cloner une adresse MAC ?

Certains FAI associent votre connexion haut débit à l'adresse MAC du premier appareil connecté, généralement votre ancien routeur ou votre ordinateur. Lorsque vous remplacez votre routeur, il peut être nécessaire de cloner l'adresse MAC pour rétablir l'accès à Internet.

Suivez les étapes ci-dessous pour cloner une adresse MAC sur votre routeur GL.iNet.

1. Notez l'adresse MAC de votre ancien routeur (ou de l'ordinateur précédemment associé à votre accès haut débit).

2. Connectez-vous au panneau d'administration web de votre routeur et accédez à **NETWORK** -> **Ethernet Port** (nommé **Port Management** dans certaines versions du firmware). Réglez **MAC Mode** sur **Clone** ou **Manual**, saisissez manuellement l'adresse MAC, puis cliquez sur **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Redémarrez votre modem (c'est-à-dire l'appareil amont).

## Q3. Quand dois-je configurer un VLAN ID ?

Certains FAI exigent un balisage VLAN pour l'authentification Internet ou la séparation du trafic, en particulier avec les connexions fibre et IPTV. Contactez votre FAI et vérifiez si un VLAN ID est requis.

Suivez les étapes ci-dessous pour configurer le VLAN ID.

1. Connectez-vous à votre routeur et accédez à la section **INTERNET** -> **Ethernet**. Cliquez sur **Modify**.

2. Saisissez le VLAN ID fourni par votre FAI, puis cliquez sur **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## Q4. Et si cela ne fonctionne toujours pas ?

Si le problème persiste, essayez de connecter directement un PC ou un ordinateur portable à votre modem et vérifiez si vous avez accès à Internet.

Si vous n'avez pas accès à Internet, le problème peut venir de votre FAI. Contactez votre FAI pour obtenir une assistance supplémentaire.

Si vous avez accès à Internet, le problème peut être lié à la configuration de votre routeur. Contactez notre support technique à l'adresse [support@gl-inet.com](mailto:support@gl-inet.com) et fournissez les informations suivantes :

- Modèle du routeur
- Étapes de dépannage déjà effectuées
- Nom de votre FAI
- Toute autre information qui pourrait nous aider à vous assister

## Informations sur les FAI

Vous trouverez ci-dessous des informations sur les FAI par région, compilées par GL.iNet à partir des retours clients, des forums et des ressources OpenWRT, à titre de référence uniquement.

| Pays/Région   | FAI   | Type de connexion | VLAN ID | Clonage MAC requis | Exigences supplémentaires |
| :------------ | :---- | :---------------- | :------ | :----------------- | :------------------------ |
| United States    | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | Must enable IP Passthrough; EAP authentication bypass needed |
| United States | Spectrum | DHCP | N/A | Yes (in some areas) | Strong MAC binding (modem reboot required) |
| United States | Verizon Fios | DHCP | N/A | No | |
| United States | Comcast Xfinity | DHCP | N/A | Yes (common) | Must reboot modem when changing router (MAC release) |
| United States | Cox Communications | DHCP | N/A | Yes | Must reboot modem when changing router (MAC release) |
| United States | Frontier Fiber | DHCP | N/A | No | |
| United States | CenturyLink / Lumen | PPPoE | 201 | No | VLANs are required in certain areas. |
| Canada | Bell Canada Fibe | PPPoE | 35 | No | |
| Germany | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 mandatory for internet; PPPoE credentials required |
| Germany | Vodafone (Kabel) | DHCP | N/A | Yes (sometimes) | MAC binding may apply; reboot modem after router change |
| Germany | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 mandatory for internet |
| Germany | DNS:NET | PPPoE | 37 | No | |
| Germany | o2(UGG) | PPPoE | 7 | No | |
| United Kingdom | BT Broadband | PPPoE | 101 | No | VLAN 101 required; PPPoE login needed |
| United Kingdom | Sky Broadband | DHCP (Option 61) | 101 | No | Requires DHCP Option 61 (client identifier) |
| United Kingdom | Virgin | DHCP | N/A | Yes | The modem is in bridged mode and requires MAC cloning. |
| France | Orange | DHCP / PPPoE | 832 | No | VLAN 832 required; may require Option 90 authentication |
| France | Free (Freebox) | DHCP | N/A | No | |
| France | Bouygues Telecom | DHCP | 100 | Yes | Clone Bbox MAC |
| Spain | Movistar | PPPoE | 6 | No | VLAN 6 (internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spain | DIGI | PPPoE | 20 | No | |
| Spain | Orange | DHCP | 832/835 | No | VLANs may vary by region |
| Italy | TIM | PPPoE | 835 | No | VLAN 835 required |
| Italy | Aruba | PPPoE | 835 | No | |
| Netherlands | KPN | DHCP | 6 | No | VLAN 6 required for internet |
| Netherlands | Tweak | DHCP | 34 | Yes | Cloning Experia Box MAC |
| Netherlands | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Netherlands | Odido | DHCP | 300 | No | |
| Belgium | EDPnet | PPPoE | 10 | No | |
| Bosnia and Herzegovina | BH Telecom | PPPoE | 100 | No | |
| Croatia | Terrakom | PPPoE | 905 | No | |
| Czech Republic | O2 | PPPoE | 848 | No | |
| Cyprus | Epic | PPPoE | 35 | No | |
| Cyprus | Cyta | PPPoE | 42 | No | |
| Cyprus | Cablenet | PPPoE | 42 | No | |
| Cyprus | Primetel | PPPoE | 42 | No | |
| Poland | Orange Polska | PPPoE | 35 | No | VLAN 35 required |
| Poland | T-mobile | PPPoE | 35 | No | |
| Ireland | Vodafone SIRO | PPPoE | 10 | No | |
| Ireland | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Türkiye | Turknet | PPPoE | 35 | No | |
| Türkiye | Turk Telekom | PPPoE | 35 | No | |
| Türkiye | Turkcell Superonline | PPPoE | N/A | Yes | |
| Türkiye | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Greece | Cosmote | PPPoE | 835 | No | |
| Greece | Nova | PPPoE | 835 | Yes | |
| Greece | DEI/PPC | DHCP | 835 | No | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE requires MAP-E/DS-Lite compatible router |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | No | BBIX IPoE service commonly used |
| India | Airtel | PPPoE / DHCP | N/A | No | Some regions require PPPoE |
| India | JioFiber | DHCP | N/A | No | Locked ONT in many cases |
| Singapore | Singtel | PPPoE | 10 | No | VLAN 10 required; IPTV separate VLAN |
| Singapore | StarHub | DHCP | N/A | No | DHCP-based connection |
| Australia | NBN (various ISPs) | PPPoE / DHCP | 2 (common) | Yes | VLAN 2 common but ISP-dependent |
