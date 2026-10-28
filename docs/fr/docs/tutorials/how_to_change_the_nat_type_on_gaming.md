# Comment modifier le type NAT pour les jeux {#how-to-change-the-nat-type-on-gaming}

Certains développeurs de jeux recommandent d’activer UPnP sur votre routeur pour obtenir un meilleur type de NAT. Cependant, UPnP présente des risques de sécurité potentiels.

Vous pouvez configurer la DMZ ou la redirection de ports sur votre routeur pour obtenir le même résultat. Avant d’activer l’une de ces fonctions, assurez-vous de comprendre son fonctionnement et les risques de sécurité associés.

## Vérifier l'adresse IP de votre appareil de jeu {#check-your-game-ip}

Connectez-vous d’abord à votre routeur. Accédez à la liste des clients et vérifiez l'adresse IP attribuée à votre appareil de jeu. Vous devrez utiliser cette adresse IP dans la configuration ci-dessous.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Méthode 1 : DMZ {#method-1-dmz}

Dans la barre latérale **Network** -> **Port Forwarding**, activez la DMZ avec l'adresse IP de votre appareil de jeu.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Méthode 2 : redirection de ports {#method-2-port-forward}

Dans la barre latérale **Network** -> **Port Forwarding**, ajoutez les ports nécessaires avec l'adresse IP de votre appareil de jeu.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Exemple : ports pour PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480


![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Ports pour Xbox

UDP 88, 3074

TCP 3074

Certains jeux peuvent nécessiter la redirection d'autres ports ; consultez ce site Web pour plus de détails.

[Redirection de ports pour différents jeux](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

Vous pouvez activer Full Cone NAT pour améliorer la latence. Cette fonction est disponible depuis le firmware v4.5.

Accédez à **Network** -> **NAT Settings**, activez **Full Cone NAT** si nécessaire, puis cliquez sur **Apply**.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
