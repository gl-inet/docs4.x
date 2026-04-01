# Comment réparer le réseau ou réinitialiser aux paramètres d'usine ?

Tous les routeurs GL.iNet sont équipés d'un mécanisme physique de réinitialisation (soit un bouton Reset, soit un trou de réinitialisation). Appuyer sur le bouton ou utiliser le trou de réinitialisation produit le même effet : restaurer la connectivité réseau ou réinitialiser le routeur à ses paramètres d'usine.

Pour les modèles avec un trou de réinitialisation, utilisez une épingle, un trombone déplié ou un outil similaire pour effectuer l'opération.  

Assurez-vous que le routeur a complètement démarré avant d'effectuer une réinitialisation. **N'appuyez PAS** sur le bouton Reset immédiatement après la mise sous tension, car cela peut déclencher le mode failsafe U-Boot.

## Réparer le réseau

Maintenez le bouton Reset enfoncé pendant **4 secondes**, puis relâchez-le pour effectuer une réinitialisation logicielle, ce qui peut réparer votre réseau.

Cette opération redémarre l'interface réseau et restaure l'interface Internet à ses paramètres par défaut, tout en conservant les paramètres Wi-Fi, les paramètres VPN, les paramètres système, etc.

**Remarque** :

1. Si le Wi-Fi a été désactivé, une réinitialisation logicielle rétablira l'état activé par défaut du Wi-Fi.

2. Une réinitialisation logicielle peut également être utilisée pour passer rapidement du mode non-routeur au mode routeur.

## Réinitialiser aux paramètres d'usine {#reset-to-factory}

Regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jguDqBWP-Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Il existe deux façons de réinitialiser le firmware.

1. Utiliser le mécanisme physique de réinitialisation (bouton ou trou de réinitialisation).

    Maintenez le bouton Reset enfoncé (ou insérez une épingle dans le trou de réinitialisation) pendant **10 secondes**, puis relâchez-le pour réinitialiser le routeur aux paramètres d'usine. Toutes les données utilisateur seront effacées.

    **Remarque :** Si la réinitialisation d'usine ne fonctionne pas, vous devrez peut-être suivre le [tutoriel U-Boot](debrick.md) pour débricker votre routeur.

2. Réinitialiser le firmware dans le panneau d'administration Web.

    Connectez-vous au panneau d'administration Web de votre routeur, puis accédez à **SYSTEM -> Reset Firmware**. Cliquez sur le bouton pour réinitialiser le firmware.

    **Remarque :** Tous vos paramètres et données actuels seront perdus. Le processus prendra environ 2 minutes. N'éteignez PAS le routeur pendant ce processus.

    ![glinet reset firmware](https://static.gl-inet.com/docs/router/en/4/tutorials/reset_firmware/reset_firmware_4.8.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
