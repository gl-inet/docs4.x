---
title: Comprendre la couverture Wi-Fi, les points d'accès et la puissance d'émission
---

# Comprendre la couverture Wi-Fi, les points d'accès et la puissance d'émission

De nombreux utilisateurs supposent qu'augmenter la puissance d'émission d'un routeur améliore toujours la couverture et les performances Wi-Fi.

Même si une puissance d'émission plus élevée augmente généralement la couverture d'un routeur unique, la puissance maximale n'est pas toujours idéale dans les réseaux comportant plusieurs points d'accès (AP), des nœuds mesh ou des déploiements Wi-Fi d'entreprise.

Comprendre les cellules de couverture, le roaming, la planification des canaux et la puissance d'émission peut aider à améliorer les performances sans fil.

## Routeur unique ou plusieurs points d'accès

### Routeur unique

Si vous n'avez qu'un seul routeur assurant la couverture Wi-Fi :

- Une puissance d'émission plus élevée augmente généralement la couverture.
- Les appareils clients peuvent maintenir une connexion utilisable à plus grande distance.
- Réduire la puissance d'émission diminue normalement le signal reçu et le rapport signal/bruit (SNR) en liaison descendante.

Pour la plupart des utilisateurs avec un seul routeur, il est recommandé de laisser la puissance d'émission sur son réglage par défaut ou automatique.

Réduire la puissance d'émission de votre routeur ne réduit pas l'énergie RF transmise par les réseaux Wi-Fi voisins. Leurs routeurs et AP continuent d'émettre à la même puissance.

### Plusieurs points d'accès

Lorsque plusieurs AP sont déployés, l'objectif n'est pas nécessairement de maximiser la zone de couverture de chaque AP.

L'objectif est plutôt de créer plusieurs cellules de couverture plus petites et bien définies, qui ne se chevauchent que suffisamment pour fournir une couverture continue et un roaming fiable.

Le bon emplacement des AP, la puissance d'émission et le choix des canaux sont tous importants.

## Chevauchement des cellules de couverture

Si chaque AP émet à la puissance maximale, leurs zones de couverture peuvent se chevaucher excessivement.

Un appareil client peut rester connecté à un AP éloigné même lorsqu'un AP plus proche fournit un signal plus fort. On parle couramment de **sticky client**.

Un client connecté au mauvais AP peut subir :

- Un SNR plus faible
- Des débits de modulation et de codage plus faibles
- Davantage de retransmissions
- Un débit réduit
- Une latence accrue

Réduire la puissance d'émission des AP peut réduire la taille des cellules de couverture et encourager les appareils clients à roamer plus tôt.

## Comprendre le roaming des clients

Dans la plupart des réseaux Wi-Fi, c'est l'appareil client qui décide quand roamer.

Le routeur ou l'AP peut fournir une assistance au roaming, mais le téléphone, l'ordinateur portable, la tablette ou un autre client prend normalement la décision finale de quitter un AP et de se connecter à un autre.

Les différents appareils clients utilisent des seuils et des algorithmes de roaming différents. Un appareil peut donc rester connecté à un AP tant qu'il considère la connexion comme utilisable, même lorsqu'un autre AP offre un signal plus fort.

Réduire le chevauchement excessif de couverture peut aider les clients à prendre de meilleures décisions de roaming.

## Réutilisation spatiale

Le Wi-Fi est un support partagé.

Avant de transmettre, les appareils Wi-Fi écoutent pour déterminer si le canal est déjà utilisé. Si des AP utilisant le même canal peuvent s'entendre sur une grande zone, ils peuvent passer plus de temps à attendre que le canal soit disponible.

Cela réduit le temps d'antenne utilisable et le débit global.

Une réduction appropriée de la puissance d'émission peut permettre à des AP utilisant le même canal dans différentes zones physiques de fonctionner plus indépendamment. C'est ce qu'on appelle la **réutilisation spatiale**.

La réutilisation spatiale ne signifie pas que la réduction de la puissance d'émission de votre AP réduit les interférences transmises par les réseaux voisins. Des cellules de couverture correctement dimensionnées peuvent plutôt réduire la contention inutile et permettre la réutilisation du même canal dans des zones suffisamment séparées.

## Planification des canaux

La puissance d'émission et le choix des canaux doivent être considérés ensemble.

### 2,4 GHz

La bande 2,4 GHz comporte relativement peu de canaux qui ne se chevauchent pas.

Dans de nombreuses régions réglementaires, les canaux 1, 6 et 11 sont couramment utilisés avec une largeur de canal de 20 MHz.

Dans la mesure du possible, les AP proches doivent utiliser des canaux différents qui ne se chevauchent pas.

### 5 GHz et 6 GHz

Les bandes 5 GHz et 6 GHz offrent davantage de canaux disponibles, ce qui facilite l'attribution de canaux différents aux AP proches.

L'utilisation de canaux qui ne se chevauchent pas réduit la contention co-canal, même si un chevauchement excessif de couverture peut encore affecter le comportement de roaming.

Les canaux disponibles dépendent du modèle de routeur, du pays ou de la région, de la largeur de canal et de la réglementation locale.

## AP câblés et réseaux mesh

### Points d'accès câblés

Une connexion Ethernet câblée entre le routeur principal et les AP supplémentaires est généralement le déploiement à privilégier.

Comme la connexion câblée transporte le trafic de backhaul, la puissance d'émission Wi-Fi peut être ajustée principalement pour la couverture des clients, le roaming et la réutilisation spatiale.

### Mesh avec backhaul câblé

Les nœuds mesh utilisant un backhaul câblé peuvent être optimisés de manière similaire aux AP câblés.

La puissance d'émission peut être ajustée pour réduire le chevauchement excessif des cellules tout en maintenant une couverture continue.

### Mesh avec backhaul sans fil

Dans un déploiement mesh sans fil, les radios Wi-Fi peuvent également transporter le trafic entre les nœuds mesh.

Réduire trop fortement la puissance d'émission peut affaiblir la connexion de backhaul sans fil et réduire les performances globales.

Lorsque vous utilisez un backhaul sans fil, assurez-vous que les nœuds mesh conservent une connexion forte et stable entre eux.

## Exemple de déploiement multi-AP

Prenons deux routeurs GL.iNet connectés par Ethernet :

- Le routeur principal fournit les services de routage, DHCP, NAT et pare-feu.
- Le second routeur fonctionne en mode Access Point.
- Les deux appareils diffusent le même nom de réseau Wi-Fi et les mêmes paramètres de sécurité.
- Les AP proches utilisent des canaux différents qui ne se chevauchent pas.
- La puissance d'émission est ajustée afin que les cellules de couverture se chevauchent suffisamment pour le roaming, mais pas excessivement.

La puissance d'émission idéale dépend des matériaux du bâtiment, de l'emplacement des AP, des appareils clients, des réseaux Wi-Fi voisins et de la zone de couverture souhaitée.

Il n'existe pas de valeur de puissance d'émission unique correcte pour tous les déploiements.

## Idées reçues courantes

### La puissance maximale fournit toujours le meilleur Wi-Fi

La puissance maximale fournit généralement la plus grande zone de couverture, mais elle peut créer un chevauchement excessif et un mauvais comportement de roaming dans les déploiements multi-AP.

### Une puissance d'émission plus faible réduit les interférences entrantes

Réduire la puissance d'émission de votre AP réduit le signal généré par votre propre AP. Cela ne réduit pas la puissance transmise par les routeurs ou AP voisins.

### Une puissance d'émission plus faible rend le récepteur de l'AP plus sensible

La puissance d'émission et la sensibilité du récepteur sont des caractéristiques distinctes. Réduire la puissance d'émission n'améliore pas en soi la capacité de l'AP à recevoir les transmissions des clients.

### Les appareils clients se connectent toujours à l'AP le plus proche

Les appareils clients sélectionnent normalement les AP et roament entre eux à l'aide de leurs propres algorithmes internes. Ils peuvent rester connectés à un AP plus éloigné même lorsqu'un AP plus proche est disponible.

## Points de départ recommandés

| Déploiement | Recommandation |
| --- | --- |
| Routeur unique | Laissez la puissance d'émission sur son réglage par défaut ou automatique. |
| Deux AP câblés ou plus | Utilisez des canaux qui ne se chevauchent pas et ajustez la puissance d'émission pour réduire le chevauchement excessif. |
| Mesh avec backhaul câblé | Optimisez les cellules de couverture pour un roaming fiable. |
| Mesh avec backhaul sans fil | Évitez de réduire la puissance au point d'affaiblir la connexion de backhaul. |

Après les changements, testez les performances à plusieurs emplacements et vérifiez :

- La puissance du signal
- Le débit montant et descendant
- La latence
- Le roaming entre AP
- La qualité du backhaul sans fil, le cas échéant

Modifiez un seul réglage à la fois afin de pouvoir mesurer précisément son effet.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com) ou [contactez-nous](https://www.gl-inet.com/contact-us/).
