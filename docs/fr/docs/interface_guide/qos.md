# QoS (Quality of Service)

QoS (Quality of Service) optimise l'allocation de bande passante en priorisant les activités critiques (par ex. appels vidéo, jeux) lors de la congestion du réseau, ce qui réduit la latence et améliore les performances globales du réseau. 

**Note** : 

1. Cette fonctionnalité est actuellement disponible uniquement sur **GL-MT5000 (Brume 3)**.

2. Cette fonctionnalité affecte le trafic qui traverse le routeur lorsqu'il agit comme passerelle (y compris le trafic des clients locaux et le trafic du VPN Client), mais pas le trafic entrant lorsque le routeur agit comme VPN Server.

---

Dans le panneau d'administration web, accédez à **FLOW CONTROL** > **QoS**. 

Définissez d'abord vos vitesses maximales d'envoi et de téléchargement (plage de saisie : 1 - 10000) pour l'ordonnancement du trafic. Faites-les correspondre à votre bande passante Internet réelle pour obtenir les meilleurs résultats.

Définissez ensuite les priorités des différentes applications, et le routeur allouera la bande passante en conséquence.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
