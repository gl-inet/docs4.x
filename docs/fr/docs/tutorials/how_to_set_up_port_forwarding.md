# Comment configurer la redirection de port sur votre routeur principal

Si vous configurez un serveur (tel qu'un [serveur OpenVPN](how_to_set_up_openvpn_server.md) ou un [serveur WireGuard](build_your_own_wireguard_home_server_with_two_glinet_routers.md)) sur votre routeur GL.iNet et que celui-ci est connecté derrière un routeur principal, vous devrez configurer la redirection de port sur le routeur principal. Cela garantit que le serveur sera accessible correctement.

Notez que s'il existe d'autres routeurs entre le routeur principal et le routeur GL.iNet, vous devez configurer la redirection de port sur tous ces routeurs intermédiaires.

## Préparation

Avant de configurer la redirection de port, nous vous recommandons de **réserver une adresse IP statique** pour le routeur GL.iNet sur votre routeur principal. Cela garantit qu'une adresse IP fixe sera toujours attribuée au routeur GL.iNet.

Dans le cas contraire, si le routeur principal ou le routeur GL.iNet redémarre, le routeur principal pourrait attribuer une nouvelle adresse IP au routeur GL.iNet, ce qui entraînerait l'échec de la règle de redirection de port.

Ensuite, configurez la redirection de port pour le routeur GL.iNet sur votre routeur principal.

Les étapes de configuration de la redirection de port varient selon la marque et le modèle du routeur. Consultez la section appropriée ci-dessous.

## Utilisation d'un routeur GL.iNet comme routeur principal

Veuillez consulter [ce lien](../interface_guide/port_forwarding.md){target="_blank"}.

## Utilisation d'une autre marque de routeur comme routeur principal

!!! note "Veillez à saisir les informations suivantes lors de la configuration de la redirection de port"

    Lors de la configuration de la redirection de port, assurez-vous de fournir les informations suivantes. Notez que la terminologie peut varier selon les marques et les modèles de routeurs.
    
    * **External port/Internal port :** Saisissez le port que vous utilisez. Par exemple, les ports par défaut sont **1194** (pour les serveurs OpenVPN) et **51820** (pour les serveurs WireGuard).
    * **Protocol :** Choisissez **All** ou **UDP/TCP**.
    * **Internal IP** (ou indiqué comme **Host IP**) : saisissez l'adresse IP WAN de votre routeur secondaire ou sélectionnez votre routeur secondaire dans la liste déroulante si cette option est disponible.

Voici des instructions étape par étape pour configurer la redirection de port sur des marques et modèles courants de routeurs principaux.

Si la marque ou le modèle de votre routeur principal n'est pas répertorié ci-dessous, consultez la documentation de votre routeur ou contactez son équipe d'assistance pour obtenir de l'aide.

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link

* [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero

Consultez [ce lien](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys

Consultez [ce lien](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear

Consultez [ce lien](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

