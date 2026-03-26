# SQM (Smart Queue Management)

Le SQM (Smart Queue Management) gère intelligemment le trafic réseau de votre routeur afin de réduire la latence et le « bufferbloat », pour des jeux en ligne et des appels vocaux plus fluides.

**Remarque** :

1. Cette fonctionnalité est actuellement disponible uniquement sur **GL-MT5000 (Brume 3)**.

2. Elle affecte le trafic qui traverse le routeur lorsqu'il agit comme passerelle (y compris le trafic des clients locaux et le trafic du client VPN), mais pas le trafic entrant lorsque le routeur agit comme serveur VPN.

3. Comme le SQM consomme des ressources, il convient surtout aux réseaux à faible bande passante ou congestionnés. Son activation sur des connexions très rapides peut réduire le débit maximal.

---

Dans la partie gauche du panneau d'administration web, accédez à **FLOW CONTROL** -> **SQM**.

Définissez d'abord vos vitesses maximales d'envoi et de téléchargement (plage de saisie : 1 à 10000) pour l'ordonnancement du trafic. Faites-les correspondre à votre bande passante réelle pour obtenir les meilleurs résultats.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

Pour **Queue Rule**, deux options sont disponibles :

- **cake** : façonnage intelligent et automatique du trafic avec un excellent contrôle global de la latence (recommandé).

- **fq_codel** : file d'attente équitable simple et efficace avec une réduction de latence de base.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
