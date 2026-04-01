# Comment utiliser WinSCP pour modifier des fichiers sur les routeurs GL.iNet

WinSCP est un outil pratique pour modifier, copier et télécharger des fichiers ou des répertoires sur le routeur. Vous pouvez transférer des fichiers entre un ordinateur local et votre routeur en utilisant les protocoles de transfert FTP, SCP, SFTP, WebDAV ou S3. Cet outil fonctionne sous le système d'exploitation Windows.

---

1. Téléchargez WinSCP [ici](https://winscp.net/eng/download.php){target="_blank"} et installez-le sur Windows.

2. Connectez-vous au routeur, puis lancez WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * File protocol : choisissez `SCP` comme protocole.
    * Host name : saisissez l’adresse IP du routeur. Si vous n’avez pas modifié l’IP de votre routeur, elle doit être `192.168.8.1`
    * Port number : `22`
    * Username & Password : saisissez `root` comme nom d’utilisateur, puis entrez votre mot de passe. 

    Cliquez ensuite sur le bouton `Login`.

3. Après la connexion, vous aurez un accès complet au routeur.

    Vous pouvez sélectionner, afficher, modifier ou transférer des fichiers et répertoires depuis ou vers le routeur.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Par exemple, si vous souhaitez modifier la configuration du pare-feu, vous pouvez accéder à /etc/config, trouver le fichier firewall, faire un clic droit dessus, puis choisir **Edit**.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Vous pouvez maintenant modifier librement le contenu du fichier. Veillez à ne pas dérégler les paramètres.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
