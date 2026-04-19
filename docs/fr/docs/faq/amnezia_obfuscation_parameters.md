# Paramètres d'obfuscation AmneziaWG

AmneziaWG est un protocole VPN basé sur WireGuard avec une obfuscation du trafic intégrée. Ses paramètres d'obfuscation contrôlent la manière dont le trafic est déguisé afin d'éviter sa détection par des contrôles réseau stricts. Vous trouverez ci-dessous un aperçu détaillé des différences entre les versions d'AmneziaWG, des paramètres d'obfuscation, de leurs contraintes et des réglages recommandés.

## AmneziaWG V2.0

Par rapport à AmneziaWG v1.0, la version v2.0 offre une obfuscation plus poussée en ajoutant de nouveaux paramètres (**S3~S4**) et en utilisant des en-têtes dynamiques pour les types de paquets (**H1~H4** sous forme de plages au lieu de valeurs fixes). En outre, AmneziaWG 2.0 prend en charge les paramètres **I1~I5**, qui envoient des paquets UDP formatés avant chaque négociation initiale afin de faire passer le trafic AmneziaWG pour un trafic ordinaire non VPN, ce qui permet de contourner efficacement l'inspection approfondie des paquets et d'améliorer la connectivité dans les réseaux restreints.

Ces améliorations rendent le trafic VPN plus difficile à détecter tout en conservant la vitesse élevée et la faible latence de WireGuard.

Voici comment identifier la version d'AmneziaWG :

- **V1.0** : pas de paramètres S3~S4 ; H1~H4 sont des entiers fixes uniques.
- **V2.0** : inclut les paramètres **S3~S4** ; **H1~H4** sont définis comme des plages numériques ; prend en charge les paramètres **I1~I5**.

**Remarque** : les paramètres I1-I5 ne sont pas générés automatiquement. Les utilisateurs peuvent les ajouter manuellement comme lignes supplémentaires dans le fichier de configuration VPN afin que le trafic AmneziaWG ressemble à d'autres protocoles courants, tels que QUIC ou WebRTC.

## Aperçu des paramètres

| Paramètre | Description | Contraintes | Généré automatiquement |
| --------- | ----------- | ----------- | ---------------------- |
| Jc | Nombre de paquets parasites avant que le client n'initie la négociation initiale (afin d'interférer avec la détection des caractéristiques du trafic) | 1~128 | 4~12 |
| Jmin | Taille minimale des paquets parasites aléatoires (octets) ; doit être configurée avec Jmax pour définir la taille des paquets parasites | 0 ≤ Jmin < Jmax < 1280 | 0 ≤ Jmin < Jmax < 1280 |
| Jmax | Taille maximale des paquets parasites aléatoires | 0 ≤ Jmin < Jmax < 1280 | 0 ≤ Jmin < Jmax < 1280 |
| S1 | Préfixes aléatoires pour les paquets Init | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Préfixes aléatoires pour les paquets Response | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Préfixes aléatoires pour les paquets Cookie | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Préfixes aléatoires pour les paquets Data | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | En-têtes dynamiques pour les types de paquets ; valeurs aléatoires (v1.0) ou plages (v2.0) | 5~2147483647 ; H1, H2, H3 et H4 doivent être différents | 5~2147483647 |
| I1~I5 | Paquets de signature pour l'imitation de protocole | bloc hexadécimal arbitraire | N/A |

Référence : [Documentation officielle d'AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

