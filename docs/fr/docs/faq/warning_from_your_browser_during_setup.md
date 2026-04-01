# Avertissement de votre navigateur : "Your Connection is not Private"

Vous pouvez voir cette alerte du navigateur lors de la première configuration de votre routeur GL.iNet : **Your Connection is not Private**.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Il s'agit d'un avertissement de sécurité standard affiché par le navigateur lorsqu'il détecte un site sans certificat SSL/TLS approuvé.

Les navigateurs sont généralement conçus pour faire confiance aux certificats délivrés par des autorités de certification tierces (CA). Or, les routeurs GL.iNet utilisent des certificats auto-signés, qui ne sont pas délivrés par des CA. Les navigateurs les considèrent donc comme non fiables et affichent cet avertissement.

## Est-il sûr d'ouvrir 192.168.8.1 ?

La sécurité de votre réseau est notre priorité. Lors de la configuration initiale, vous n'avez pas besoin d'une connexion Internet, car tout le processus s'effectue localement.

Lorsque vous vous connectez au Wi-Fi du routeur GL.iNet pendant la configuration, vous pouvez voir **"Connected, No internet"**. C'est normal, car le routeur fonctionne comme un réseau local autonome pendant la configuration.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

De même, l'adresse IP **192.168.8.1** est une adresse IP locale privée attribuée au routeur lui-même. Elle sert à accéder au panneau d'administration local de l'appareil, et non à un site web public.

Comme la connexion est entièrement locale et qu'aucun accès à Internet n'est nécessaire pendant la configuration, il n'y a **aucun risque de fuite de confidentialité**. Vous bénéficiez ainsi d'un environnement isolé et sécurisé pour configurer votre routeur.

## Pourquoi cet avertissement apparaît-il quand même ?

Les navigateurs ne font généralement pas la distinction entre une adresse IP prédéfinie de configuration et un site web classique ; ils traitent toutes les adresses IP comme des sites web et s'attendent à ce que les connexions HTTPS soient sécurisées par des certificats SSL/TLS.

Les routeurs GL.iNet utilisent bien des certificats SSL/TLS, mais ceux-ci sont auto-signés et ne sont pas délivrés par des autorités de certification tierces (CA). Même si l'accès à cette adresse IP est sûr (car il s'effectue sur un réseau local privé), le navigateur la considère malgré tout comme « non sécurisée », d'où l'apparition de l'alerte.

## Que faire face à cet avertissement ?

Veuillez cliquer sur **Advanced**, puis sur **Continue to 192.168.8.1**.

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Vous serez alors redirigé vers le panneau d'administration web.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Puis-je ajouter un certificat SSL sur le routeur ?

Oui, vous pouvez ajouter votre propre certificat SSL sur les routeurs GL.iNet.

[Comment ajouter un certificat SSL](../faq/use_https_for_adh.md)

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

