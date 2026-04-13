# QoS (Quality of Service)

La QoS (Quality of Service) optimise l’allocation de la bande passante en donnant la priorité aux activités critiques (par ex. appels vidéo, jeux en ligne) lors de la congestion du réseau, ce qui réduit la latence et améliore les performances globales du réseau.

**Remarque** : cette fonctionnalité affecte le trafic qui traverse le routeur lorsqu’il agit comme passerelle (y compris le trafic des clients locaux et du client VPN), mais pas le trafic entrant lorsque le routeur agit comme serveur VPN.

## Modèles pris en charge

!!! note "Modèles pris en charge"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configuration rapide

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **QoS**.

Activez l’interrupteur pour activer la QoS ; la page s’affichera comme ci-dessous.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

Définissez ensuite vos vitesses maximales d’envoi et de téléchargement (plage de saisie : 1 - 10000) pour l’ordonnancement du trafic. Faites-les correspondre à votre bande passante Internet réelle pour obtenir les meilleurs résultats.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Remarque** : les valeurs saisies dans le champ sont en **Mbps** (mégabits par seconde). L’équivalent en **MB/s** (mégaoctets par seconde) s’affiche à titre indicatif.

Définissez ensuite les priorités pour les différentes applications. Le routeur allouera la bande passante en conséquence.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## Personnaliser la priorité des applications

Pour personnaliser la priorité des applications, sélectionnez **Customize** puis cliquez sur **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, toutes les catégories sont définies par défaut sur **Medium Priority**.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Faites glisser les catégories pour ajuster leur priorité selon vos besoins, puis cliquez sur **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
