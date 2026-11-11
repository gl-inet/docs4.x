# Obfuscation AmneziaWG {#amneziawg-obfuscation}

AmneziaWG est un protocole VPN basé sur WireGuard avec une obfuscation du trafic intégrée. Ses paramètres d'obfuscation contrôlent la manière dont le trafic est déguisé afin d’éviter sa détection par des mécanismes d’inspection réseau restrictive.

Vous trouverez ci-dessous une présentation détaillée d’AmneziaWG et de ses différentes versions.

## Pourquoi AmneziaWG ? {#why-amneziawg}

Le prédécesseur d’AmneziaWG, WireGuard, s’est imposé comme un protocole VPN rapide et fiable grâce à sa base de code compacte et à sa grande efficacité. Cependant, ses en-têtes de paquets fixes et ses tailles de paquets prévisibles créent une signature facilement reconnaissable. Les systèmes DPI peuvent identifier ces paquets sans difficulté et interrompre immédiatement les connexions, ce qui constitue un problème critique dans les pays où la censure d’Internet est stricte.

AmneziaWG conserve la simplicité architecturale et les hautes performances de l'implémentation WireGuard d'origine, tout en ajoutant un module d'obfuscation dédié qui masque les modèles du trafic VPN. Les particuliers comme les entreprises peuvent ainsi protéger leur vie privée en ligne et maintenir des connexions stables dans les environnements réseau restrictifs.

En bref :

- Il masque les caractéristiques VPN pour empêcher la détection par les FAI, les pare-feu ou l’inspection approfondie des paquets (DPI).
- Il fait apparaître votre connexion VPN comme du trafic web standard, améliorant la stabilité et le taux de réussite de la connexion dans les réseaux restreints.

## AmneziaWG V2.0 {#amneziawg-v20}

### Présentation {#amneziawg-v20-overview}

<font color="red">**Remarque** : AmneziaWG 2.0 est pris en charge sur les routeurs GL.iNet équipés du firmware v4.9.0 ou d’une version ultérieure.</font>

AmneziaWG 2.0 conserve les mécanismes d’obfuscation de la v1.0, à savoir la série de paquets parasites (**Jc**, **Jmin**, **Jmax**) et les préfixes aléatoires des paquets Init et Response (**S1–S2**). Les mécanismes suivants masquent les caractéristiques de la connexion qui restaient prévisibles :

* **S3–S4** : préfixes aléatoires pour les paquets Cookie et Data. La v1.0 ne remplissait que les paquets Init et Response. Les paquets Cookie faisaient donc exactement 64 octets et les paquets Data avaient exactement la longueur de leur charge utile.

* **H1–H4 sous forme de plages** : la valeur d’en-tête de chaque type de paquet est tirée d’une plage. À la réception, toute valeur comprise dans la plage est acceptée. Les quatre plages ne doivent pas se chevaucher.

* **I1–I5** : paquets UDP définis par l’utilisateur et envoyés avant chaque négociation. La session commence ainsi par un trafic qui ressemble à celui d’un protocole UDP courant plutôt qu’à une négociation WireGuard.

Ces améliorations rendent le trafic VPN plus difficile à détecter tout en conservant la vitesse élevée et la faible latence de WireGuard.

!!! Tip "Comment distinguer AmneziaWG 1.0 et 2.0 ?"

    **V1.0** : pas de paramètres S3-S4 ; H1-H4 sont des entiers fixes uniques.
    
    **V2.0** : il s’agit de la version V2.0 si l’une des conditions ci-dessous est remplie :
            
    - Inclut des paramètres S3-S4
    - H1-H4 sont définis comme des plages numériques
    - Inclut des paramètres I1-I5 personnalisés.
            
    > Remarque : I1-I5 ne sont pas générés automatiquement. Les utilisateurs peuvent les ajouter manuellement comme lignes supplémentaires dans le fichier de configuration afin que le trafic AmneziaWG ressemble à d’autres protocoles courants, tels que QUIC ou WebRTC.

### Paramètres {#amneziawg-v20-parameters}

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

Exemple de section d’obfuscation v2.0 :

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1318795025-1318795156
H2 = 1029272944-1029273095
H3 = 966737016-966737098
H4 = 282229905-429495047
```

Références : [Documentation officielle AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Présentation {#amneziawg-v31-overview}

<font color="red">**Remarque** : AmneziaWG 3.1 est pris en charge sur les routeurs GL.iNet équipés du firmware v4.11.1 ou d’une version ultérieure.</font>

AmneziaWG 3.1 conserve tous les mécanismes d’obfuscation de la v2.0 : les préfixes aléatoires pour chaque type de paquet (**S1–S4**), les en-têtes dynamiques (**H1–H4**), les paquets de signature envoyés avant la négociation (**I1–I5**) et la série de paquets parasites (**Jc**, **Jmin**, **Jmax**). Les mécanismes suivants compliquent l’identification du trafic par son empreinte.

- **Protection des en-têtes** : utilise ChaCha20 pour masquer les champs d’en-tête des paquets WireGuard qui resteraient autrement en clair.
- **Remplissage du contenu** : ajoute une quantité aléatoire de remplissage aux paquets de données de transport, dans la limite de l’espace disponible selon la MTU.
- **Temporisations personnalisées** : permet de configurer des valeurs ou des plages pour le renouvellement des clés, les nouvelles tentatives de négociation, les messages de maintien de connexion et d’autres opérations connexes. Les valeurs générées automatiquement sont recommandées sur le serveur et le client.
- **Ajouts aléatoires en fin de paquet** : ajoute un nombre variable d’octets aux paquets de négociation et de données de transport pour diversifier davantage leurs tailles.
- **Désactivation des réponses Cookie** : permet à un appareil de cesser d’envoyer les réponses Cookie de négociation tout en continuant à les recevoir et à traiter les autres étapes de la négociation.

### Paramètres {#amneziawg-v31-parameters}

Les paramètres suivants ont été introduits dans AmneziaWG V3.1.

| Paramètre | Description | Contraintes | Plage ou valeur GL.iNet |
| --------- | ----------- | ----------- | ----------- |
| `HeaderProtectionKey` | Protège à l’aide de ChaCha20 les champs d’en-tête qui resteraient autrement en clair | Exactement 32 octets. Si cette option est activée, S1, S2, S3 et S4 doivent tous être définis à une valeur ≥ 12. Combinaison recommandée : `H1=1`, `H2=2`, `H3=3`, `H4=4`. Le mécanisme d’en-têtes personnalisés est alors désactivé et la protection des en-têtes masque le type de message | Clé de 32 octets |
| `ContentPaddingAddition` | Ajoute aux paquets de données de transport un nombre d’octets tiré au hasard de la plage configurée pour chaque paquet | `range<uint16>`, 0–65535, min ≤ max ; `0` ou `0-0` désactive la fonction | 0–65535 (exemple : `10-50`) |
| `RekeyAfterTime` | Durée d’utilisation de la clé actuelle avant le lancement d’un renouvellement actif (en secondes) | `range<uint16>`, 0–65535, min ≤ max ; `0` ou `0-0` rétablit la valeur par défaut de WireGuard | 100–150 (valeur WireGuard par défaut : 120) |
| `RekeyTimeout` | Délai d’attente d’une réponse à une demande de négociation avant une nouvelle tentative (en secondes) | `range<uint16>`, 0–65535, min ≤ max ; `0` ou `0-0` rétablit la valeur par défaut de WireGuard | 4–7 (valeur WireGuard par défaut : 5) |
| `RejectAfterTime` | Délai sans réception de données avant le lancement d’une nouvelle négociation (en secondes) | `range<uint16>`, 0–65535, min ≤ max ; `0` ou `0-0` rétablit la valeur par défaut de WireGuard | 180–240 (valeur WireGuard par défaut : 180) |
| `KeepaliveTimeout` | Délai sans envoi de données avant l’envoi d’un message interne de maintien de connexion (en secondes) | `range<uint16>`, 0–65535, min ≤ max ; `0` ou `0-0` rétablit la valeur par défaut de WireGuard | 8–20 (valeur WireGuard par défaut : 10) |
| `MaxHandshakeAttempts` | Nombre maximal de nouvelles tentatives de négociation | `range<uint16>`, 0–65535, min ≤ max ; `0` ou `0-0` rétablit la valeur par défaut de WireGuard | 12–18 (valeur WireGuard par défaut : 18) |
| `RandomTrailers` | Ajoute un nombre variable d’octets à la fin des paquets : données aléatoires pour les paquets de négociation, zéros après le paquet IP interne pour les paquets de transport. La longueur ajoutée est choisie de façon à ne dépasser la MTU d’aucune des deux extrémités | `off` désactive la fonction. Lorsqu’elle est activée, il est recommandé de définir `S1 = S2 = S3 = S4` pour réduire le risque de mauvaise identification du type de paquet dû aux tailles aléatoires | `on` / `off` |
| `DisableCookies` | Empêche l’appareil local d’envoyer des réponses Cookie de négociation. La réception de ces réponses du pair et le reste de la négociation ne sont pas affectés | `off` désactive la fonction. S3 et H3 doivent rester valides, car ils peuvent encore servir à la réception | `on` / `off` |

**Remarques**

* Le routeur peut générer les plages de la dernière colonne. Les options `RandomTrailers` et `DisableCookies` se règlent sur chaque appareil.
* La valeur de `HeaderProtectionKey` doit être identique sur le client et le serveur.
* À l’exécution, toute temporisation hors des plages indiquées est remplacée par une valeur aléatoire comprise dans la plage. Une valeur personnalisée peut donc ne pas être appliquée telle quelle.
* `ContentPaddingAddition` et `S4` modifient la longueur des paquets de transport à des endroits différents. Les deux paramètres peuvent être utilisés ensemble.
* La protection des en-têtes et les valeurs `H` dynamiques peuvent coexister. `H1–H4` peuvent rester dynamiques, même si le réglage `1/2/3/4` est recommandé.

---

Exemple de section d’obfuscation v3.1 :

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

Références : [Documentation officielle AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Article connexe :

- [Comment configurer l'obfuscation VPN sur les routeurs GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
