# GoodCloud site à site

## Présentation

La fonctionnalité **Site to Site** de GoodCloud permet à des bureaux situés à différents endroits d'établir des connexions sécurisées entre eux via Internet. Elle étend le réseau de l'entreprise afin de rendre les ressources informatiques d'un site accessibles aux employés d'autres sites du réseau.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scénario 1** : des dizaines de succursales appartenant à la même entreprise doivent être intégrées dans un réseau privé unifié, afin de permettre un partage fluide des ressources entre tous les sites.

**Scénario 2** : lorsque deux entreprises qui collaborent étroitement ont besoin d'un environnement de travail commun, le réseau site à site facilite cette collaboration dans un cadre partagé et sécurisé.

**Scénario 3** : pour les familles disposant de caméras IP, le site à site permet l'accès à distance à l'appareil lorsque les membres sont absents du domicile, pour une surveillance simple depuis n'importe où.

## Conditions

1. Au moins deux routeurs GL.iNet sont nécessaires pour créer un réseau site à site.

2. Au moins un routeur doit disposer d'une adresse IP publique afin de pouvoir être défini comme nœud principal. [Vérifiez si votre FAI vous attribue une adresse IP publique](how_to_check_if_isp_assigns_you_a_public_ip_address.md). 

    Il est préférable d'utiliser comme nœud principal un routeur offrant de bonnes performances et le meilleur débit réseau.

3. Il n'est **PAS** recommandé d'utiliser **Site to Site** pendant que les nœuds secondaires utilisent également un client VPN / Tailscale / ZeroTier / AstroWarp, car cela peut rendre la configuration réseau particulièrement complexe.

## Créer un réseau site à site

1. Associez vos routeurs à votre compte GoodCloud. [Comment faire](../interface_guide/cloud.md/#setup-your-goodcloud-account) ?

2. Connectez-vous à [GoodCloud](https://www.goodcloud.xyz/#/login), puis accédez à **Site to Site** dans la barre latérale gauche. Cliquez sur **Create Network** en haut à droite.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Cochez la case à gauche pour sélectionner au moins deux appareils.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}
    
    Les appareils sélectionnés s'afficheront dans la partie inférieure de la page. 

    Le port par défaut de Site to Site est **51830**. Si vous souhaitez utiliser un autre port, cliquez sur **Advanced** en bas à gauche pour le modifier. Cliquez ensuite sur **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Un réseau site à site peut comporter jusqu'à 10 appareils afin de garantir des performances stables.

4. Donnez un nom à votre réseau, puis cliquez sur **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Le test **Node Usability Testing** démarre pour vérifier si un appareil peut être défini comme **Main Node**.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Si aucun appareil ne peut être utilisé comme **Main Node**, assurez-vous que :

    - au moins un routeur dispose d'une adresse IP publique, statique ou dynamique ;
    - le port est ouvert. Le port par défaut de Site to Site est 51830. Vous pouvez également le modifier puis réessayer ;
    - si le routeur que vous souhaitez définir comme **Main Node** est derrière un NAT, vous devrez peut-être configurer une redirection de port.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Si plusieurs appareils peuvent être définis comme **Main Node**, choisissez-en un pour continuer. Nous vous recommandons de sélectionner comme **Main Node** le routeur offrant de bonnes performances et le meilleur débit réseau.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Si un seul appareil peut être défini comme **Main Node**, la page de détails de **Site to Site** s'ouvrira directement.

6. Le réseau est désactivé par défaut. Assurez-vous que les adresses IP LAN de tous les nœuds ne sont pas en conflit. Cliquez sur l'icône en forme d'engrenage pour modifier l'adresse IP LAN si nécessaire, puis cliquez sur **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Attendez quelques minutes. Lorsque la ligne en pointillés devient continue, cela signifie que le réseau site à site a été établi avec succès.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Tester la connexion site à site

1. Connectez votre PC ou votre smartphone à l'un des nœuds de ce réseau site à site.

2. Ouvrez un navigateur Web pour accéder à l'adresse IP LAN d'un autre nœud. Si vous pouvez accéder à la page de connexion, cela signifie que la connexion entre ces deux nœuds fonctionne.

## Routes et autres options

Par défaut, chaque nœud peut accéder au LAN des autres nœuds. Pour des raisons de sécurité, nous recommandons de n'ouvrir que les adresses IP des services spécifiques.

Par exemple, il existe un serveur A (172.30.97.100) dans le sous-réseau du nœud 1. Si vous souhaitez que les autres nœuds puissent accéder uniquement au service A du nœud 1, vous pouvez le configurer comme suit :

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Vous pouvez également ajouter les routes parentes des nœuds.

Chaque nœud secondaire établit un tunnel chiffré vers le nœud principal. Si vous souhaitez modifier l'adresse IP du sous-réseau du tunnel, cliquez sur **IP Address Range** pour la modifier.

L'application d'une modification de la plage d'adresses IP entraînera une déconnexion du réseau pendant quelques minutes.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
