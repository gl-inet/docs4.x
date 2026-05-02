# SQM (Smart Queue Management)

Le SQM (Smart Queue Management) gère intelligemment le trafic réseau de votre routeur afin de réduire la latence et le « bufferbloat », pour des jeux en ligne et des appels vocaux plus fluides.

**Remarque** :

1. Cette fonctionnalité affecte le trafic qui traverse le routeur lorsqu’il agit comme passerelle (y compris le trafic des clients locaux et du client VPN), mais pas le trafic entrant lorsque le routeur agit comme serveur VPN.

2. Comme le SQM consomme beaucoup de ressources, il convient surtout aux réseaux à faible bande passante ou congestionnés. Son activation sur des connexions très rapides peut réduire le débit maximal.
3. Le SQM ne prend pas effet lorsque le routeur est en mode Drop-in Gateway.
4. Le SQM et la QoS ne peuvent pas être activés simultanément.
5. Le SQM ne peut pas fonctionner avec Network Acceleration. L’activation du SQM désactivera automatiquement Network Acceleration afin de garantir des performances stables.

## Modèles pris en charge

!!! note "Modèles pris en charge"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configuration rapide

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **SQM**.

Activez l’interrupteur pour activer le SQM, puis définissez vos vitesses maximales d’envoi et de téléchargement (plage de saisie : 1 - 10000) pour l’ordonnancement du trafic. Faites-les correspondre à votre bande passante Internet réelle pour obtenir les meilleurs résultats.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Remarque** : les valeurs saisies dans le champ sont en **Mbps** (mégabits par seconde). L’équivalent en **MB/s** (mégaoctets par seconde) s’affiche à titre indicatif.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Pour **Queue Rule**, deux options sont disponibles :

- **cake** : mise en forme intelligente et automatique du trafic avec un excellent contrôle global de la latence (recommandé).

- **fq_codel** : file d’attente équitable simple et efficace avec une réduction de latence de base.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
