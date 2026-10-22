# Sans fil (firmware v4.8 et versions antérieures) {#wireless-firmware-v48-and-earlier}

Le contenu de cette page est basé sur la version de firmware v4.8.x et les versions antérieures. Si votre appareil utilise une autre version de firmware, utilisez le sélecteur ci-dessous pour passer au guide correspondant.

<div class="gl-link-select" data-label="Version du firmware" data-placeholder="Firmware v4.8 et versions antérieures" markdown="1">

- [Firmware v4.9 et versions ultérieures](wireless.md)

</div>

---


Sur le côté gauche du panneau d’administration web, accédez à **WIRELESS**.

La page Wireless permet de configurer des réseaux Wi‑Fi distincts, notamment en 2.4 GHz, 5 GHz, 6 GHz et en Wi‑Fi MLO (la disponibilité varie selon le modèle). Chaque bande peut être configurée en Main Wi‑Fi ou Guest Wi‑Fi pour une gestion sans fil plus flexible.

**Note** : Certains modèles ne prennent pas en charge le Wi-Fi 5 GHz, comme le GL-MT300N-V2 (Mango) et le GL-X300B (Collie) ; certains n’ont pas de fonction Wi‑Fi, comme le GL-MT5000 (Brume 3) et le GL-MT2500/GL-MT2500A (Brume 2).

## Wi-Fi MLO {#mlo-wi-fi}

| Modèles pris en charge          |           |
| :----------------------------- | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)       | √         |
| Beryl 7 (GL-MT3600BE)          | √         |
| Flint 3e (GL-BE6500)           | √         |
| Flint 3 (GL-BE9300)            | √         |
| Slate 7 (GL-BE3600)            | √         |

Le MLO (Multi-Link Operation) est l’une des fonctionnalités essentielles du Wi-Fi 7 (802.11be). Il est conçu pour améliorer les performances du réseau, réduire sensiblement la latence et renforcer la stabilité de la connexion en utilisant simultanément plusieurs bandes de fréquences, comme 2.4 GHz, 5 GHz et 6 GHz.

Cliquez sur les onglets ci-dessous pour en savoir plus sur les paramètres de Main Wi-Fi MLO et de Guest Wi-Fi MLO.

=== "Wi-Fi MLO"

    Main Wi-Fi MLO vous permet de configurer plusieurs paramètres, notamment l’activation/la désactivation du Wi-Fi, la sélection des bandes radio (au moins deux), l’activation/la désactivation du BSSID aléatoire, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe Wi-Fi et de la visibilité du SSID.

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - Si les bandes radio du Wi-Fi MLO incluent le 6 GHz, le BSSID du Wi-Fi MLO se synchronisera lorsque le BSSID du Wi-Fi 6GHz changera.

    - La sécurité Wi-Fi par défaut du Wi-Fi MLO est WPA3-SAE, qui convient à la plupart des appareils prenant en charge le MLO.

=== "Guest Wi-Fi MLO"

    Guest Wi-Fi MLO vous permet de configurer des paramètres simplifiés, notamment l’activation/la désactivation du Wi-Fi, la sélection des bandes radio (au moins deux), la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe et de la visibilité du SSID.

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## Wi-Fi 6 GHz {#6-ghz-wi-fi}

| Modèles pris en charge          |           |
| :----------------------------- | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)       | √         |
| Mudi 7 (GL-E5800)              | √         |
| Flint 3 (GL-BE9300)            | √         |

Le Wi-Fi 6 GHz offre une connectivité sans fil plus rapide et plus stable, avec moins de congestion que les bandes 2.4 GHz et 5 GHz.

Cliquez sur les onglets ci-dessous pour en savoir plus sur les paramètres de Main Wi-Fi 6 GHz et de Guest Wi-Fi 6 GHz.

=== "Wi-Fi 6 GHz"

    Main Wi-Fi 6 GHz vous permet de configurer plusieurs paramètres, notamment l’activation/la désactivation du Wi-Fi, le réglage de la puissance TX, l’activation/la désactivation du BSSID aléatoire, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe Wi-Fi, de la visibilité du SSID, du mode Wi-Fi, de la bande passante et du canal.

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - Activer PSC : lorsque PSC (Preferred Scanning Channel) est activé, seuls les canaux offrant une meilleure connectivité seront réservés afin de garantir la connexion des appareils 6 GHz.

=== "Guest Wi-Fi 6 GHz"

    Guest Wi-Fi 6 GHz vous permet de configurer des paramètres simplifiés, notamment l’activation/la désactivation du Wi-Fi, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe et de la visibilité du SSID.

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## Wi-Fi 5 GHz {#5-ghz-wi-fi}

Cliquez sur les onglets ci-dessous pour en savoir plus sur les paramètres de Main Wi-Fi 5 GHz et de Guest Wi-Fi 5 GHz.

=== "Wi-Fi 5 GHz"

    Main Wi-Fi 5 GHz vous permet de configurer plusieurs paramètres, notamment l’activation/la désactivation du Wi-Fi, le réglage de la puissance TX, l’activation/la désactivation du BSSID aléatoire, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe Wi-Fi, de la visibilité du SSID, du mode Wi-Fi, de la bande passante et du canal.

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "Guest Wi-Fi 5 GHz"

    Guest Wi-Fi 5 GHz vous permet de configurer des paramètres simplifiés, notamment l’activation/la désactivation du Wi-Fi, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe et de la visibilité du SSID.

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## Wi-Fi 2.4 GHz {#24-ghz-wi-fi}

Cliquez sur les onglets ci-dessous pour en savoir plus sur les paramètres de Main Wi-Fi 2.4 GHz et de Guest Wi-Fi 2.4 GHz.

=== "Wi-Fi 2.4 GHz"

    Main Wi-Fi 2.4 GHz vous permet de configurer plusieurs paramètres, notamment l’activation/la désactivation du Wi-Fi, le réglage de la puissance TX, l’activation/la désactivation du BSSID aléatoire, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe Wi-Fi, de la visibilité du SSID, du mode Wi-Fi, de la bande passante et du canal.

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "Guest Wi-Fi 2.4 GHz"

    Guest Wi-Fi 2.4 GHz vous permet de configurer des paramètres simplifiés, notamment l’activation/la désactivation du Wi-Fi, la définition du nom du Wi-Fi (SSID), de la sécurité Wi-Fi, du mot de passe et de la visibilité du SSID.

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Paramètres Wi-Fi généraux {#general-wi-fi-settings}

* Survolez l’icône du code QR à côté du SSID Wi-Fi pour afficher son code QR Wi‑Fi. Vous pouvez le scanner avec votre téléphone ou votre tablette afin de vous connecter rapidement au réseau Wi‑Fi correspondant.

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID** : activée par défaut, cette fonctionnalité empêche le suivi du routeur via un BSSID fixe. Consultez [Randomized BSSID](#randomized-bssid) pour en savoir plus.

* **Bandwidth** et **Channel** ne peuvent pas être modifiés lorsque le routeur agit comme [répéteur](internet_repeater.md), car ils suivent ceux du réseau répété.

* Lorsque **Channel** est défini sur **Auto**, le Wi-Fi du routeur ne bascule pas automatiquement vers un canal DFS.

* Lorsque vous basculez **Channel** d’un canal non-DFS vers un canal DFS, un avertissement s’affiche comme ci-dessous.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* Lorsque **Bandwidth** est défini sur **160 MHz** (disponible uniquement sur certains modèles), le Wi-Fi utilisera toujours un canal DFS, même si vous choisissez un canal non-DFS ou Auto pour les paramètres de Channel.

## BSSID aléatoire {#randomized-bssid}

Randomized BSSID est une fonctionnalité de confidentialité disponible depuis le firmware v4.6 et activée par défaut. Elle empêche la localisation et le suivi de votre routeur au moyen d’un BSSID Wi-Fi fixe (l’adresse MAC de l’interface sans fil du routeur).

**Pourquoi un BSSID fixe présente un risque pour la confidentialité**

Les systèmes d’exploitation mobiles (comme Android et iOS) utilisent le positionnement Wi-Fi fondé sur des données collaboratives pour fournir des services de localisation :

1. Les appareils clients (téléphones et ordinateurs portables) transmettent régulièrement les BSSID qu’ils détectent, ainsi que leur propre position GPS, au serveur du fournisseur du système d’exploitation ou du fabricant de l’appareil.

2. Les fournisseurs regroupent ces données dans une base mondiale associant chaque BSSID à une position.

3. Tout appareil dont le Wi-Fi est activé, même sans GPS, peut interroger cette base pour estimer sa position à partir des BSSID environnants.

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

Un routeur avec un BSSID fixe agit ainsi comme une balise de localisation : il peut être géolocalisé à distance et ses déplacements (par exemple lorsque vous l’emportez en voyage) peuvent être suivis dans le temps. Des attaquants peuvent également interroger ces bases pour localiser des routeurs ou les identifier à partir des informations du fabricant (OUI) contenues dans le BSSID.

**Comment Randomized BSSID vous protège**

Lorsque cette fonctionnalité est activée, le routeur génère un BSSID aléatoire et le renouvelle à chaque démarrage. Puisque le BSSID change régulièrement, il ne peut plus être associé à une position fixe dans les bases des fournisseurs, ce qui rompt l’association entre BSSID et position utilisée pour le suivi.

| État | Comportement |
| ----------------- | ---------------------- |
| Activé (par défaut) | Un nouveau BSSID aléatoire est généré à chaque démarrage |
| Désactivé | Le routeur utilise son adresse MAC réelle d’usine comme BSSID |

**Remarques** :

1. Le BSSID ne change qu’au redémarrage du routeur ; il reste identique pendant une session en cours.
2. Pour le Wi-Fi invité, le BSSID reste identique à celui du Wi-Fi principal sur la même bande de fréquence.
3. Si les bandes du Wi-Fi MLO incluent 6 GHz, son BSSID se synchronise avec celui du Wi-Fi 6 GHz.
4. Randomized BSSID bloque le suivi via le BSSID du routeur, mais n’empêche pas les appareils clients de transmettre leur propre position. Il ne constitue pas une solution de confidentialité complète : le SSID, le canal et les caractéristiques du signal restent observables.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"}.
