# Sans fil (firmware v4.9)

> Ce guide s'applique au firmware v4.9 et aux versions ultérieures. Pour les versions antérieures, veuillez cliquer [ici](wireless.md).

Dans le panneau d'administration web, accédez à **WIRELESS**.

La page Wireless vous permet de configurer différents réseaux Wi‑Fi, notamment le Wi‑Fi MLO (disponible sur certains modèles), le réseau principal, le réseau invité et le réseau IoT. Les bandes Wi‑Fi prises en charge varient selon le modèle.

## Multi-Link Operation (MLO)

??? "Modèles pris en charge"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Modèles non pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation) est l'une des fonctionnalités principales du Wi‑Fi 7 (802.11be). Elle est conçue pour améliorer les performances du réseau, réduire significativement la latence et renforcer la stabilité de la connexion en utilisant simultanément plusieurs bandes de fréquences, telles que 2.4 GHz, 5 GHz et 6 GHz.

Il est recommandé aux clients Wi‑Fi 7 de se connecter au Wi‑Fi MLO, qui améliore fortement le débit et la fiabilité du réseau grâce aux connexions multi-bandes.

Cliquez sur **Add** pour configurer un réseau Wi‑Fi MLO, puis sur **Apply**. Notez que les bandes Wi‑Fi disponibles varient selon le modèle.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band : sélectionnez au moins deux bandes radio.
- Wi-Fi Security : si la bande 6 GHz est sélectionnée, WPA3-SAE est la seule option disponible et recommandée. Elle fonctionne au mieux avec la plupart des appareils compatibles MLO.
- Enable Randomized BSSID : lorsque la bande 6 GHz est sélectionnée, le BSSID 6 GHz du Wi‑Fi MLO sera synchronisé avec le Wi‑Fi principal.

Une fois activé, la page s'affiche comme suit.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo3.png){class="glboxshadow"}

## Réseau principal

Le réseau principal est votre réseau Wi‑Fi principal. Il prend en charge la diffusion simultanée sur différentes bandes radio, toutes activées par défaut. Vous pouvez configurer des paramètres distincts pour chaque bande, comme le SSID Wi‑Fi, le mode de sécurité, le mot de passe, le BSSID aléatoire, la puissance TX, la bande passante et le canal.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main.png){class="glboxshadow"}

Cliquez sur l'icône d'engrenage à droite pour afficher ou modifier les paramètres Wi‑Fi de chaque bande. Notez que les bandes Wi‑Fi disponibles varient selon le modèle.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_2.4g.png){class="glboxshadow"}

## Réseau invité

Le réseau invité est un réseau Wi‑Fi dédié aux visiteurs, avec toutes les bandes désactivées par défaut. Vous pouvez activer et configurer les paramètres réseau de base pour chaque bande, comme le SSID Wi‑Fi, le mode de sécurité, le mot de passe et l'activation du BSSID aléatoire. 

Cliquez sur **Add** pour configurer un réseau Wi‑Fi invité, puis sur **Apply**. Notez que les bandes Wi‑Fi disponibles varient selon le modèle.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest2.png){class="glboxshadow"}

Une fois activé, la page s'affiche comme suit.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest3.png){class="glboxshadow"}

## Réseau IoT

Le réseau IoT est un réseau Wi‑Fi dédié aux appareils intelligents, avec toutes les bandes désactivées par défaut. Vous pouvez activer et configurer les paramètres réseau de base pour chaque bande, comme le SSID Wi‑Fi, le mode de sécurité, le mot de passe et l'activation du BSSID aléatoire.

Cliquez sur **Add** pour configurer un réseau Wi‑Fi IoT, puis sur **Apply**. Notez que ce réseau n'inclut pas la bande 6 GHz et que les bandes Wi‑Fi disponibles varient selon le modèle.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot2.png){class="glboxshadow"}

Une fois activé, la page s'affiche comme suit.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot3.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"}.
