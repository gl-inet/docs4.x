# Se connecter à Internet via un Wi‑Fi existant en mode Repeater

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Le mode Repeater permet de connecter le routeur à un autre réseau sans fil existant, par exemple lorsque vous utilisez le Wi‑Fi gratuit d'un hôtel ou d'un café.

Par défaut, il fonctionne en mode WISP (Wireless Internet Service Provider), ce qui signifie que le routeur crée son propre sous-réseau et agit comme pare-feu pour vous protéger du réseau public.

## Étapes de base

Connectez-vous au panneau d'administration web du routeur, accédez à la section **INTERNET** -> **Repeater**, puis cliquez sur **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Choisissez le réseau Wi‑Fi auquel vous souhaitez vous connecter dans la liste des réseaux disponibles.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**Remarque** : la page affiche les canaux Wi‑Fi pris en charge par votre routeur. Assurez-vous que le réseau Wi‑Fi auquel vous vous connectez utilise l'un de ces canaux ; sinon, il risque de ne pas apparaître dans la liste des réseaux disponibles.

Saisissez le bon mot de passe Wi‑Fi, puis cliquez sur **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Si le SSID Wi‑Fi auquel vous souhaitez vous connecter n'apparaît pas dans la liste Available Network, cliquez sur **Join Other Network** en haut à droite, puis saisissez manuellement le SSID Wi‑Fi et les autres informations requises. Reportez-vous [ici](#join-other-network) pour les étapes détaillées.

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Pour vous connecter à un hotspot public, par exemple dans un hôtel, un aéroport ou un centre commercial, consultez [Pour les hotspots publics](#for-public-hotspot).

Pour les autres paramètres, reportez-vous à [Paramètres avancés](#advanced-settings).

Après un court moment, si le mot de passe saisi est correct, la connexion sera établie.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Pour les hotspots publics {#for-public-hotspot}

Lorsque vous connectez le routeur à un hotspot public doté d'un portail captif, l'activation des fonctionnalités suivantes peut contribuer à améliorer le taux de réussite de la connexion.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    Cette fonctionnalité est disponible depuis la v4.6.

    Si cette option est activée, le routeur passera automatiquement en Login Mode for Public Hotspots lorsqu'il sera connecté avec succès à un hotspot mais pas à Internet. **Dans ce mode, certains services seront suspendus tandis que le mode DNS sera basculé sur automatique**, ce qui peut divulguer votre activité réseau au fournisseur du hotspot (par exemple un hôtel ou un centre commercial).

    Même si cette option n'est pas activée, le routeur vous invitera à entrer dans ce mode lorsqu'il détecte un portail captif sur le hotspot et que la connexion échoue.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    Si cette option est activée, le routeur se fera passer pour l'appareil client que vous utilisez pour accéder au panneau d'administration en imitant l'adresse MAC de cet appareil.

- **MAC Mode**

    Vous pouvez choisir l'adresse MAC que le routeur utilisera pour se connecter au hotspot public.

    - **Factory** : utilise l'adresse MAC d'origine attribuée en usine à l'appareil.

    - **Clone** : clone l'adresse MAC d'un appareil client pour la connexion. Si l'adresse MAC souhaitée n'est pas listée, saisissez manuellement celle que vous voulez cloner. 
    
        Remarque : de nombreux appareils modernes utilisent des adresses MAC aléatoires (souvent appelées Private Wi‑Fi Address ou random hardware address) lorsqu'ils se connectent aux réseaux Wi‑Fi. Pour cette raison, l'adresse MAC affichée ici peut ne pas correspondre à la véritable adresse MAC physique de l'appareil.
  
    - **Random** : génère automatiquement une adresse MAC aléatoire pour la connexion.

    Lorsque vous enregistrez la configuration réseau, le **MAC Mode** (y compris toute adresse MAC clonée ou aléatoire) est associé au SSID spécifique enregistré. Vous pouvez modifier manuellement ces paramètres pour chaque SSID à tout moment.

- **Auto Update MAC** : si cette option est activée, l'adresse MAC peut être mise à jour automatiquement.

## Paramètres avancés {#advanced-settings}

Lors de la connexion au réseau, quelques options supplémentaires sont disponibles.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember** : activez cette option pour mémoriser le réseau Wi‑Fi actuellement répété.

* **Lock BSSID** : lorsque cette option est activée, le routeur se connecte uniquement au point d'accès (AP) spécifique correspondant au BSSID sélectionné, même si d'autres AP partagent le même SSID.

* **Manually Set Static IP** : lorsque cette option est activée, vous pouvez configurer manuellement une adresse IPv4 fixe, un masque de sous-réseau, une passerelle et des serveurs DNS pour la connexion Repeater du routeur, au lieu d'obtenir automatiquement ces paramètres.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL** : TTL (Time To Live) définit la durée maximale pendant laquelle les paquets peuvent survivre dans le réseau et peut être ajusté selon les exigences de l'opérateur. Par défaut, le routeur transmet le TTL du paquet entrant de l'appareil client moins une unité. Si vous devez camoufler la connexion, vous pouvez définir ici une valeur fixe. Le TTL n'est valable que pour IPv4.

* **HL** : en IPv6, le champ HL (Hop Limit) sert à limiter le nombre de sauts de transmission des paquets de données sur le réseau, ce qui correspond au TTL en IPv4.

* **MTU** : la valeur par défaut est 1500.

## Options Repeater

Pour afficher les options Repeater, cliquez sur l'icône en forme d'engrenage en haut à droite de la section Repeater connectée.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**Pour le firmware v4.8**, la page Repeater Options s'affiche comme suit.

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**: 

    - **No Switching mode** : lorsque ce mode est activé, les autres réseaux enregistrés ne seront pas connectés automatiquement lorsque le Wi‑Fi actuel sera déconnecté.
  
    - **Auto Switching mode** : lorsque ce mode est activé, le routeur essaiera de se connecter à d'autres réseaux enregistrés lorsque le Wi‑Fi actuel sera déconnecté.
  
    - **Auto Switching Without Network** : lorsque ce mode est activé, le routeur n'analysera pas automatiquement les réseaux lorsqu'il est correctement connecté dans un mode autre que Repeater. Il essaiera uniquement de basculer automatiquement vers d'autres réseaux enregistrés lorsqu'il n'aura plus de réseau, ce qui permet d'éviter les pertes de paquets pendant les communications. 

- **Band Selection** : vous pouvez choisir parmi trois options : Auto, 5 GHz et 2.4 GHz.

    Si vous sélectionnez manuellement une bande, le routeur n'analysera ni ne se connectera à aucun Wi‑Fi utilisant une autre bande.

**Pour le firmware v4.7 et les versions antérieures**, la page Repeater Options s'affiche comme ci-dessous.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Networks**. Si cette option est activée, le routeur se connectera automatiquement à d'autres réseaux enregistrés lorsqu'il ne pourra plus se connecter au réseau Wi‑Fi actuel.

* **Band Selection**. Si vous sélectionnez manuellement une bande, le routeur n'analysera ni ne se connectera à aucun Wi‑Fi utilisant une autre bande.

## Gérer les réseaux connus

Pour supprimer un réseau connu, cliquez sur **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Ou cliquez sur **Connect** dans la section Repeater si aucun réseau n'est connecté.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Dans la section **Known Networks**, cliquez sur l'icône de corbeille pour supprimer un réseau connu, ou sur l'icône d'engrenage pour configurer le réseau.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Rejoindre un autre réseau {#join-other-network}

Si le SSID n'apparaît pas dans la liste Available Networks, ou si le SSID est masqué, vous pouvez cliquer sur **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Saisissez le SSID, sélectionnez **Security** et entrez le mot de passe (si nécessaire).

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

Pour les paramètres **Security**, deux ou trois options sont disponibles, selon le modèle.

* None, ce qui signifie qu'aucun mot de passe n'est requis.
* WPA/WPA2/WPA3, option courante prise en charge par presque tous les réseaux Wi‑Fi.
* WPA/WPA2/WPA3 Enterprise, qui nécessite Extensible Authentication Protocol (EAP) pour l'authentification. Un nom d'utilisateur et un mot de passe valides sont nécessaires pour se connecter (généralement sur des réseaux d'entreprise ou de campus).

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    Pour des instructions détaillées sur la répétition des réseaux EAP, cliquez [ici](../tutorials/eap.md){target="_blank"}.

## Reconnexion

Dans les cas suivants, le routeur essaiera automatiquement de se reconnecter au Wi‑Fi à intervalles réguliers. Vous pouvez désactiver cette fonction manuellement si nécessaire. En cas d'erreur de SSID ou de mot de passe, supprimez le réseau des Known Networks pour résoudre le problème.

1. SSID ou mot de passe incorrect saisi lors de la configuration de Repeater.

2. Déplacement hors de portée du routeur en amont après la connexion initiale.

3. Le routeur en amont modifie le SSID ou le mot de passe, ou restreint l'accès après la connexion.

Le processus de reconnexion comporte trois phases distinctes : phase d'attente, phase d'analyse et phase de connexion.

1. Phase d'attente : aucun problème ; le routeur attend que les conditions de reconnexion soient réunies.

2. Phase d'analyse : des pertes de paquets peuvent survenir sur la bande de fréquence analysée. Les nouveaux appareils peuvent rencontrer des problèmes de connexion. Pour les modèles GL-AXT1800/GL-AX1800, le Guest Wi‑Fi sera temporairement désactivé.

3. Phase de connexion : le Wi‑Fi principal sur la bande cible peut être interrompu pendant quelques secondes lors du rétablissement.

**Remarque** : les problèmes surviennent généralement pendant les phases d'analyse et de connexion.

## Dépannage

Lorsque le routeur est connecté à un réseau Wi‑Fi en mode Repeater, si Internet n'est pas disponible, un message jaune s'affiche comme ci-dessous.

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Pour résoudre ce problème :

1. Vérifiez que l'appareil en amont (c'est-à-dire le réseau Wi‑Fi auquel votre routeur est connecté) dispose d'un accès à Internet.

2. Accédez à la page [Multi-WAN](multi-wan.md) pour vérifier l'état de l'interface Repeater.

## DFS

Lors de la connexion à un Wi‑Fi 5G en amont, le Wi‑Fi du routeur suivra le Wi‑Fi en amont afin d'utiliser ou non le canal DFS.

* Si le Wi‑Fi en amont utilise un canal DFS et peut être analysé, le Wi‑Fi 5G du routeur utilisera le même canal.

* Le Wi‑Fi 5G du routeur basculera vers un canal non DFS si le Wi‑Fi en amont ne peut pas être analysé ou si la connexion échoue.

??? "Modèles pris en charge"

    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Modèles non pris en charge"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Articles connexes

- [Page Internet](internet.md)
- [Comment définir la priorité de chaque méthode d'accès à Internet ?](multi-wan.md)
- [Comment définir l'équilibrage de charge lorsque plusieurs méthodes d'accès à Internet sont utilisées en même temps ?](multi-wan.md)
- [Comment connaître les adresses MAC LAN et Wi‑Fi ?](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
