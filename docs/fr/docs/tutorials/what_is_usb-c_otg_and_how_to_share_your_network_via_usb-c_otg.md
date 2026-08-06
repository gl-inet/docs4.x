# Qu'est-ce que l'USB-C OTG et comment partager votre réseau via USB-C OTG

## USB OTG
**USB OTG** (On-The-Go) est une norme USB qui permet aux appareils compatibles, comme les routeurs, de basculer entre les rôles **Host** et **Device**. Elle permet la transmission directe de données et l'échange d'alimentation sans appareil hôte séparé.

Les deux modes suivants peuvent être sélectionnés via **USB OTG** :

- Lorsqu'un appareil passe en **mode Host** via USB OTG, il agit comme hôte USB, lance la transmission de données, fournit l'alimentation et contrôle toutes les opérations de lecture et d'écriture entre les deux appareils connectés.

- En **Device mode**, l'appareil sert de périphérique, reçoit l'alimentation de l'hôte et répond passivement à ses commandes, sans pouvoir initier la communication lui-même.

## Partage réseau via USB-C OTG sur Mudi 7

Le port USB-C compatible OTG du Mudi 7 fonctionne en mode **Device** ou **Host** afin de permettre un partage réseau flexible avec des appareils externes.

### Connexion à un ordinateur

La plupart des ordinateurs fonctionnent uniquement comme hôtes et ne prennent pas en charge OTG. Lorsqu'un ordinateur est connecté au routeur via USB, le routeur affiche une fenêtre de sélection de mode. Vous pouvez choisir n'importe quel mode ; le Mudi 7 négocie automatiquement le rôle. L'ordinateur le reconnaît ensuite comme un adaptateur USB pour un accès Internet direct, sans pilote supplémentaire.

### Connexion à un smartphone

- **Device Mode** : le Mudi 7 agit comme périphérique USB et partage son réseau avec le téléphone.

- **Host Mode** : lorsque vous activez USB Tethering sur le téléphone, celui-ci peut partager son réseau cellulaire avec le Mudi 7 via USB. Cette liaison USB peut servir d'interface WAN indépendante et permettre le Multi-WAN.

!!! Note

    1. Lorsque vous utilisez la fonction OTG du téléphone pour l'interconnexion, assurez-vous que le téléphone prend en charge OTG et utilisez un câble USB compatible avec les données. Les câbles de charge uniquement ne peuvent pas transmettre de signaux réseau.

    2. Lorsque Device Mode est activé, le téléphone n'affiche pas de notification de connexion réseau. Pour vérifier le fonctionnement, consultez l'état du réseau dans les réglages du téléphone ou effectuez un test de connectivité.

        Par exemple, si vous partagez le réseau du Mudi 7 avec un téléphone via **Device Mode** (par exemple, iPhone 17 Pro), vérifiez que Device Mode est actif en suivant les étapes ci-dessous.

        1. Utilisez un câble USB compatible OTG pour connecter le port USB 3.1 du Mudi 7 à votre iPhone 17 Pro.

        2. Sur le Mudi 7, sélectionnez **Device Mode**.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. Dans les réglages du téléphone, vous verrez que le Mudi 7 fournit un accès réseau au téléphone, comme indiqué dans la capture ci-dessous.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Vous avez encore des questions ? Visitez notre [Community Forum](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
