# Qualité du réseau

**Remarque** : cette fonctionnalité a été introduite dans le firmware v4.11.

---

Dans le menu latéral gauche du panneau d'administration Web, accédez à **FLOW CONTROL** -> **Network Quality**.

Le tableau de bord Network Quality surveille la qualité de votre connexion Internet en temps réel. Il évalue la réactivité, la latence et les performances DNS tout en détectant les interruptions de connexion et les pertes de paquets. Ces mesures vous aident à identifier les problèmes d'instabilité et de connectivité que les seuls tests de bande passante peuvent ne pas révéler.

Sur cette page, vous pouvez évaluer votre connexion Internet à l'aide du Network Quality Score et lancer des tests de débit locaux si nécessaire.

**Remarque** :

1. Le GL.iNet Network Quality Score global est calculé selon la formule pondérée suivante :

    `Overall Score = Response Score × 60% + Reliable Score × 40%`.

2. Speedtest est un test de débit local exécuté sur le routeur et soumis aux règles de limitation de débit de fonctionnalités telles que SQM et QoS.

## Network Quality Score

Cette section affiche le Network Quality Score global, calculé à partir du Response Score et du Reliable Score. Vous pouvez consulter chaque score séparément. Le panneau affiche également des mesures associées, notamment la latence, la gigue et la perte de paquets, ainsi que les débits descendants et montants en temps réel en Ko/s. Par défaut, le tableau de bord utilise `google.com` comme cible des tests de connectivité Internet et de résolution DNS.

Cliquez sur l'icône des paramètres pour configurer les cibles de test.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Vous pouvez sélectionner les cibles des tests Internet Reachability et DNS Resolution parmi Baidu, Tencent, Alibaba, Google, Microsoft ou Cloudflare. Vous pouvez également saisir manuellement un domaine personnalisé.

Les cibles configurées servent à exécuter les tests de connectivité et DNS et à calculer le Network Quality Score.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target** : permet de tester la connectivité Internet et de mesurer la latence de bout en bout (cible ping Hop2).

- **DNS Resolution Target** : domaine résolu lors des requêtes DNS. Les enregistrements A (IPv4) et AAAA (IPv6) sont tous deux interrogés.

## Speedtest

Ce test de débit intégré utilise Cloudflare Speed Test pour mesurer les débits descendant et montant, la latence du ping et le bufferbloat. Des graphiques de débit en temps réel sont affichés pendant le test.

Cliquez sur **Run Speedtest** pour lancer le test.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Une fois le test terminé, la page affiche les résultats.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
