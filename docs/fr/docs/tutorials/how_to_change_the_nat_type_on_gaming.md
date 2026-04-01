# Comment modifier le type NAT pour les jeux

La plupart des éditeurs de jeux vous demanderont d'activer l'UPnP sur le routeur pour obtenir un meilleur type de NAT, mais des études montrent que l'UPnP est un protocole non sécurisé.

Vous pouvez obtenir le même résultat de manière plus sûre, soit grâce à la fonction DMZ, soit grâce à la redirection de ports.

## Vérifier l'adresse IP de votre appareil de jeu

Accédez à la liste des clients et vérifiez l'adresse IP attribuée à votre appareil de jeu. Vous devrez utiliser cette adresse IP dans la configuration ci-dessous.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Méthode 1 : DMZ

Dans la barre latérale **Network > Port Forwarding**, activez la DMZ avec l'adresse IP de votre appareil de jeu.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Méthode 2 : redirection de ports

Dans la barre latérale **Network > Port Forwarding**, ajoutez les ports nécessaires avec l'adresse IP de votre appareil de jeu.

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

## Full Cone NAT

Vous pouvez activer **Full Cone NAT** dans **Network > NAT Settings** pour améliorer la latence.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* Cette fonction est disponible à partir du firmware 4.5.

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
