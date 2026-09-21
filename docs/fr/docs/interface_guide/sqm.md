# SQM (Smart Queue Management)

**Remarque** : cette fonction a été introduite dans le firmware v4.9. Certains modèles, tels que Mango 2 (GL-MG1300), ne prennent pas en charge le SQM en raison d’une mémoire insuffisante, même lorsqu’ils exécutent le firmware v4.9 ou une version ultérieure.

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **SQM**.

Le SQM (Smart Queue Management) gère intelligemment le trafic réseau de votre routeur afin de réduire la latence et le « bufferbloat », pour des jeux en ligne et des appels vocaux plus fluides.

**Remarque** :

1. Cette fonctionnalité affecte uniquement le trafic qui traverse le routeur lorsqu’il fonctionne comme passerelle, y compris le trafic des clients locaux et le trafic du client VPN. Elle ne s’applique pas au trafic entrant lorsque le routeur agit comme serveur VPN.

2. Comme le SQM consomme beaucoup de ressources, il convient surtout aux réseaux à faible bande passante ou congestionnés. Son activation sur des connexions très rapides peut réduire le débit maximal.
3. Le SQM ne prend pas effet lorsque le routeur est en mode Drop-in Gateway.
4. Le SQM et la QoS ne peuvent pas être activés simultanément.
5. Le SQM ne peut pas fonctionner avec Network Acceleration. L’activation du SQM désactivera automatiquement Network Acceleration afin de garantir des performances stables.

## Pour le firmware v4.11 et les versions ultérieures

Activez l’interrupteur pour activer le SQM, puis effectuez la configuration en suivant les étapes ci-dessous.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Saisissez manuellement les débits montant et descendant du WAN (plage de saisie : 1 - 10000), ou cliquez sur **Run Speedtest** pour les mesurer et remplir automatiquement les champs. Une connexion Internet active est nécessaire pour exécuter le test de débit.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Remarque** : les valeurs saisies sont exprimées en **Mbps** (mégabits par seconde). L’équivalent en **MB/s** (mégaoctets par seconde) est affiché à titre indicatif.

2. **Queue Discipline**

    Sélectionnez une règle de mise en file d’attente pour gérer le trafic et réduire la latence lorsque le réseau est sollicité.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake** : mise en forme intelligente et automatique du trafic avec un excellent contrôle global de la latence (recommandé).

        Lorsque **cake** est sélectionné comme discipline de file d’attente, **Cake Autorate** est disponible en option.

        Cake Autorate est un outil de mise en forme piloté par la latence qui réduit ou augmente la bande passante CAKE en temps réel selon le RTT des sondes. Aucun test de débit actif n’est exécuté ; seuls des pings légers sont utilisés. Cette fonction est recommandée lorsque la bande passante WAN fluctue et n’est pas nécessaire sur les liaisons stables.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Remarque** : Cake Autorate génère en permanence un trafic de sonde en arrière-plan. Tenez compte de cette consommation de données supplémentaire si vous utilisez une connexion facturée à l’usage.

        Les paramètres par défaut conviennent à la plupart des connexions. Ne modifiez les paramètres suivants que si vous comprenez leur effet sur Cake Autorate. Si nécessaire, cliquez sur **Reset to Default** pour restaurer les paramètres de sonde et de seuil par défaut.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses** : liste d’adresses IP séparées par des virgules, utilisées pour mesurer la qualité du réseau.

        - **Probe Interval** : des intervalles plus courts permettent une réponse plus rapide, mais consomment davantage de ressources processeur.

        - **Concurrent Probes** : le nombre de sondes simultanées ne doit pas dépasser le nombre de serveurs de sonde ; des valeurs plus élevées augmentent la charge du processeur.

        - **Idle Detection Threshold** : lorsque le débit tombe sous cette valeur, la connexion est considérée comme inactive. Cette valeur ne doit pas dépasser 25 % de la limite de débit configurée.

        - **Download Latency Threshold** : lorsque la latence de téléchargement dépasse ce seuil, la bande passante est réduite.

        - **Upload Latency Threshold** : lorsque la latence d’envoi dépasse ce seuil, la bande passante est réduite.

    - **fq_codel** : file d’attente équitable simple et efficace avec une réduction de latence de base.

## Pour les firmwares v4.9 à v4.10

Activez l’interrupteur pour activer le SQM, puis définissez vos vitesses maximales d’envoi et de téléchargement (plage de saisie : 1 - 10000) pour l’ordonnancement du trafic. Faites-les correspondre à votre bande passante Internet réelle pour obtenir les meilleurs résultats.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Remarque** : les valeurs saisies dans le champ sont en **Mbps** (mégabits par seconde). L’équivalent en **MB/s** (mégaoctets par seconde) s’affiche à titre indicatif.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Pour **Queue Rule**, deux options sont disponibles :

- **cake** : mise en forme intelligente et automatique du trafic avec un excellent contrôle global de la latence (recommandé).

- **fq_codel** : file d’attente équitable simple et efficace avec une réduction de latence de base.

!!! Tip

    La QoS permet de définir la priorité des applications, le routeur attribuant la bande passante en conséquence, tandis que le SQM permet de sélectionner une règle de file d’attente.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
