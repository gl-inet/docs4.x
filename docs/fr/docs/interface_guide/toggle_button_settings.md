# Paramètres du bouton à bascule

Les paramètres du bouton à bascule vous permettent d’assigner des fonctions spécifiques à l’interrupteur physique de votre routeur (également appelé sélecteur de mode sur certains modèles) pour un accès et un contrôle rapides, avec des raccourcis pratiques pour les opérations courantes.

Vous pouvez personnaliser le comportement de cet interrupteur dans le panneau d’administration web.

## Modèles pris en charge

??? "Modèles pris en charge"
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-MT1300 (Beryl)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-E750V2 (Mudi V2)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)

??? "Modèles non pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Configuration

Dans la partie gauche du panneau d’administration web, accédez à **SYSTEM** -> **Toggle Button Settings**.

![toggle button settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings.jpg){class="glboxshadow"}

Avant le firmware v4.8, cinq options permettaient de personnaliser la fonction du bouton à bascule :

- No Function
- AdGuard Home
- OpenVPN Client
- Tor
- WireGuard Client

Depuis le firmware v4.8, d’autres options ont été ajoutées : Repeater, Wi‑Fi et LED. Les utilisateurs peuvent ainsi personnaliser l’interrupteur selon leurs besoins.

- No Function
- Repeater
- Wi-Fi (Main/Guest Wi-Fi)
- VPN
- Tor
- AdGuard Home
- LED

![toggle button 4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_4.8.png){class="glboxshadow"}

Lors de l’application des paramètres, vous pouvez décider d’activer ou non immédiatement la fonctionnalité choisie selon la position ON/OFF (gauche/droite) du bouton à bascule.

**Remarque** : après le redémarrage de l’appareil, le système appliquera automatiquement l’état de la fonctionnalité en fonction de la position du bouton à bascule.

Par exemple, si vous configurez **WireGuard Client** pour qu’il soit contrôlé par le bouton à bascule : lorsque l’interrupteur est à gauche (**ON**), le client WireGuard démarre automatiquement ; lorsqu’il est à droite (**OFF**), le client WireGuard reste désactivé.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
