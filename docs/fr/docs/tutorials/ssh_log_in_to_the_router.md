# Connexion SSH au routeur

Secure Shell (SSH) est un protocole réseau cryptographique permettant d’exploiter des services réseau de manière sécurisée sur un réseau non sécurisé. Son application la plus connue est la connexion à distance aux systèmes informatiques. Il peut parfois être nécessaire de disposer d’outils de base pour se connecter à un serveur en SSH. Ce guide explique comment se connecter en SSH aux routeurs GL.iNet.

---

## Pour les utilisateurs Windows

Il existe plusieurs façons d’accéder au terminal du routeur sous Windows, notamment via Windows Cmd, PowerShell, Bitvise ou PuTTY.

### Utilisation de Windows Cmd

1. Ouvrez l’invite de commandes

    Appuyez sur **Win** + **R** (touche Windows + touche R) pour ouvrir la boîte Exécuter. Saisissez **cmd** puis appuyez sur Entrée.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Une fenêtre noire d’invite de commandes s’ouvrira.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Connectez-vous au routeur

    Dans la fenêtre d’invite de commandes, saisissez `ssh root@192.168.8.1` puis appuyez sur Entrée.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Remarque** : `192.168.8.1` est l’adresse IP par défaut du routeur. Si vous l’avez modifiée auparavant, utilisez votre adresse IP personnalisée.

    Saisissez ensuite le mot de passe administrateur de votre routeur, puis appuyez sur Entrée. **Pour des raisons de sécurité, le mot de passe ne s’affiche pas à l’écran**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Si le mot de passe est correct, vous vous connecterez au routeur avec succès.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Dépannage"

    1. **Erreur : Connection timed out**
    
        Assurez-vous que votre appareil (par exemple un ordinateur portable) est connecté au routeur. Reconnectez-vous au Wi-Fi du routeur ou à son port LAN, puis réessayez.

    2. **Erreur : Permission denied**

        Assurez-vous de saisir le bon mot de passe administrateur. Si vous l’avez oublié, réinitialisez le routeur en maintenant le bouton RESET enfoncé pendant 10 secondes.

### Utilisation de PowerShell

1. Ouvrez Windows PowerShell

    Cliquez sur l’icône de recherche dans la barre des tâches, saisissez **PowerShell**, sélectionnez **Windows PowerShell** et exécutez-le en tant qu’administrateur.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Connectez-vous au routeur

    Dans la fenêtre PowerShell, saisissez `ssh root@192.168.8.1` puis appuyez sur Entrée.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Remarque** : `192.168.8.1` est l’adresse IP par défaut du routeur. Si vous l’avez modifiée auparavant, utilisez votre adresse IP personnalisée.

    Le système vous demandera de confirmer la connexion. Saisissez `yes` puis appuyez sur Entrée.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Le système vous demandera ensuite de saisir le mot de passe administrateur du routeur. Entrez le bon mot de passe administrateur, puis appuyez sur Entrée. **Pour des raisons de sécurité, le mot de passe ne s’affiche pas à l’écran**.
    
    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}
    
    Vous serez alors connecté avec succès au terminal de votre routeur.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Dépannage"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Cela se produit si la clé de sécurité du routeur a changé (par exemple après une réinitialisation d’usine ou une mise à jour du firmware), ou si vous vous êtes déjà connecté à un autre routeur, ce qui entraîne l’échec de la vérification de la clé d’hôte.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Pour résoudre le problème, ouvrez l’Explorateur de fichiers, accédez à `C:\Users\Administrator\.ssh`, puis trouvez un fichier nommé **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Double-cliquez sur le fichier known_hosts et ouvrez-le avec le Bloc-notes.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Supprimez l’entrée correspondant à l’adresse IP du routeur (par ex. `192.168.8.1`), puis enregistrez le fichier. Quittez l’Explorateur de fichiers.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        De retour dans PowerShell, utilisez la commande `ssh root@192.168.8.1` pour vous reconnecter au routeur. Il vous demandera de confirmer la connexion. Saisissez `yes` puis appuyez sur Entrée, puis saisissez le mot de passe de connexion du routeur. Vous serez alors connecté avec succès au terminal de votre routeur.

    2. **Que faire si j'ai modifié le port SSH du routeur ?**
    
        Si vous avez modifié le port SSH du routeur, indiquez le port via le paramètre `-p` lors de l’utilisation de la commande ssh. Par exemple :
        
        ``ssh -p [nouveau numéro de port] [nom d'utilisateur]@[adresse IP du routeur]``

### Utilisation de Bitvise

Regardez cette vidéo pour vous connecter à votre routeur via Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Utilisation de PuTTY

1. Téléchargez PuTTY

    Téléchargez la dernière version de PuTTY [ici](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Installez PuTTY

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Lancez PuTTY

    Cliquez sur **PuTTY** depuis le menu Démarrer.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    La fenêtre de configuration suivante s’affichera.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Saisissez `192.168.8.1` dans Host Name (or IP address), laissez Port sur la valeur par défaut `22`, puis sélectionnez `SSH` comme type de connexion.

    Saisissez `Your Session` dans les sessions enregistrées, puis cliquez sur `Save`.

    Cliquez ensuite sur `Open` en bas de la fenêtre.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    Une alerte de sécurité s’affichera comme ci-dessous ; cliquez sur `Yes`.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Saisissez ensuite votre mot de passe administrateur. **Pour des raisons de sécurité, le mot de passe ne s’affiche pas à l’écran**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    Lorsque vous voyez l’image ci-dessus, cela signifie que vous êtes connecté au routeur en SSH avec succès.

---

## Pour les utilisateurs Linux/Mac

La procédure est globalement la même sous Linux et macOS. Nous utilisons ci-dessous Ubuntu comme exemple.

### Utilisation d’Ubuntu

1. Lancez le terminal.

    Démarrez Ubuntu. Double-cliquez sur l’icône Terminal pour lancer le terminal.
    
    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Connectez-vous au routeur.

    Saisissez la commande de connexion SSH : `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    Le système vous demandera de confirmer la connexion. Saisissez `yes` puis appuyez sur Entrée.

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Saisissez ensuite le mot de passe administrateur de votre routeur. **Pour des raisons de sécurité, le mot de passe ne s’affiche pas à l’écran**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    Lorsque vous voyez l’image ci-dessus, cela signifie que vous vous êtes connecté au routeur avec succès.

??? "Dépannage"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Cela se produit si la clé de sécurité du routeur a changé (par exemple après une réinitialisation d’usine ou une mise à jour du firmware), ou si vous vous êtes déjà connecté à un autre routeur, ce qui entraîne l’échec de la vérification de la clé d’hôte.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Si cela se produit, exécutez la commande dans la zone rouge ci-dessus. Veuillez copier la commande exacte affichée dans votre terminal.

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Essayez ensuite de vous reconnecter.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**
    
        Vous pouvez rencontrer cette erreur lors de la connexion. Cette erreur est due à une modification du package Openssh à partir de la version 8.8. Pour la corriger, ouvrez le fichier **~/.ssh/config** avec un éditeur de texte (par exemple Nano ou Vim) et ajoutez les lignes suivantes :

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Assurez-vous de modifier l’IP de l’hôte si elle n’est pas celle par défaut.

        Pour plus d’informations sur ce problème, veuillez consulter [ce sujet](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
