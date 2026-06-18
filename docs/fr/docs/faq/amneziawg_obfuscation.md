# Obfuscation AmneziaWG

AmneziaWG est un protocole VPN basé sur WireGuard avec une obfuscation du trafic intégrée. Ses paramètres d'obfuscation contrôlent la manière dont le trafic est déguisé afin d’éviter sa détection par des mécanismes d’inspection réseau restrictive.

Vous trouverez ci-dessous une analyse détaillée d’AmneziaWG, des différences entre les versions, de la prise en charge sur les routeurs GL.iNet et un aperçu des paramètres.

## Pourquoi AmneziaWG ?

Le prédécesseur d’AmneziaWG, WireGuard, s’est imposé comme un protocole VPN rapide et fiable grâce à sa base de code compacte et à sa grande efficacité. Cependant, ses en-têtes de paquets fixes et ses tailles de paquets prévisibles créent une signature facilement reconnaissable. Les systèmes DPI peuvent identifier ces paquets sans difficulté et interrompre immédiatement les connexions, ce qui constitue un problème critique dans les pays où la censure d’Internet est stricte.

AmneziaWG reprend la simplicité architecturale et les hautes performances de l’implémentation d’origine, tout en supprimant les signatures réseau identifiables qui rendent WireGuard facile à détecter par les systèmes d’inspection approfondie des paquets (DPI).

En bref :

- Il masque les caractéristiques VPN pour empêcher la détection par les FAI, les pare-feu ou l’inspection approfondie des paquets (DPI).
- Il fait apparaître votre connexion VPN comme du trafic web standard, améliorant la stabilité et le taux de réussite de la connexion dans les réseaux restreints.

## AmneziaWG V2.0

Par rapport à AmneziaWG v1.0, la version v2.0 offre une obfuscation plus poussée en ajoutant de nouveaux paramètres (**S3~S4**) et en utilisant des en-têtes dynamiques pour les types de paquets (**H1~H4** sous forme de plages au lieu de valeurs fixes). En outre, AmneziaWG 2.0 prend en charge les paramètres **I1~I5**, qui envoient des paquets UDP formatés avant chaque négociation initiale afin de faire passer le trafic AmneziaWG pour un trafic ordinaire non VPN, ce qui permet de contourner efficacement l’inspection approfondie des paquets et d’améliorer la connectivité dans les réseaux restreints.

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

Ces améliorations rendent le trafic VPN plus difficile à détecter tout en conservant la vitesse élevée et la faible latence de WireGuard.

Voici comment identifier la version d’AmneziaWG :

- **V1.0** : pas de paramètres S3~S4 ; H1~H4 sont des entiers fixes uniques.
- **V2.0** : inclut les paramètres **S3~S4** ; **H1~H4** sont définis comme des plages numériques ; prend en charge les paramètres **I1~I5**.

> Remarque : Les paramètres I1-I5 ne sont pas générés automatiquement. Les utilisateurs peuvent les ajouter manuellement comme lignes supplémentaires dans le fichier de configuration VPN afin que le trafic AmneziaWG ressemble à d’autres protocoles courants, tels que QUIC ou WebRTC.

## AmneziaWG sur les routeurs GL.iNet

Actuellement, plusieurs routeurs GL.iNet (par exemple, Brume 3, Flint 3, Flint 2 et Beryl AX) prennent en charge le protocole AmneziaWG dans certaines versions de firmware. La prise en charge officielle complète sera disponible dans le firmware version 4.9 et se déploiera progressivement sur d’autres modèles.

Pour configurer l’obfuscation VPN sur les routeurs GL.iNet, veuillez vous référer à [cet article](../tutorials/vpn_obfuscation.md).

## Aperçu des paramètres

| Paramètre | Description | Contraintes | Généré automatiquement |
| --------- | ----------- | ----------- | ---------------------- |
| Jc | Nombre de paquets parasites avant que le client n’initie la négociation initiale (afin d’interférer avec la détection des caractéristiques du trafic) | 1~128 | 4~12 |
| Jmin | Taille minimale des paquets parasites aléatoires (octets) ; doit être configurée avec Jmax pour définir la taille des paquets parasites | 0 ≤ Jmin < Jmax < 1280 | 0 ≤ Jmin < Jmax < 1280 |
| Jmax | Taille maximale des paquets parasites aléatoires | 0 ≤ Jmin < Jmax < 1280 | 0 ≤ Jmin < Jmax < 1280 |
| S1 | Préfixes aléatoires pour les paquets Init | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Préfixes aléatoires pour les paquets Response | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Préfixes aléatoires pour les paquets Cookie | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Préfixes aléatoires pour les paquets Data | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | En-têtes dynamiques pour les types de paquets ; valeurs aléatoires (v1.0) ou plages (v2.0) | 5~2147483647 ; H1, H2, H3 et H4 doivent être différents | 5~2147483647 |
| I1~I5 | Paquets de signature pour l’imitation de protocole | bloc hexadécimal arbitraire | N/A |

Références : [Documentation officielle AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Article connexe :

- [Comment configurer l’obfuscation VPN sur les routeurs GL.iNet](../tutorials/vpn_obfuscation.md){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
