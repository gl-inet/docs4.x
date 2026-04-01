# macOS ne peut pas écrire sur un partage Samba

Lorsqu'un périphérique de stockage formaté en exFAT est utilisé pour un partage Samba, certains appareils macOS peuvent rencontrer l'une des erreurs suivantes lorsqu'ils tentent d'écrire des fichiers sur le partage.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Essayez de résoudre ce problème à l'aide des méthodes suivantes.

1. **Vérifier les autorisations du partage Samba.**

    Assurez-vous que le partage Samba est configuré avec un accès en écriture. Connectez-vous au panneau d'administration Web de votre routeur et vérifiez que le dossier partagé a les autorisations "Read/Write" activées pour votre compte utilisateur.

2. **Utiliser la commande `cp -X file-name` pour copier le fichier.**

    Comme Finder ajoute automatiquement des attributs étendus (par exemple, des resource forks et des métadonnées) pendant les transferts, ce qui peut entrer en conflit avec la gestion par Samba d'un stockage exFAT, essayez d'utiliser la commande **cp -X file-name** pour copier le fichier.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Ou utilisez la commande **cp -rX folder-name** pour copier le dossier.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Redémarrer votre Mac.**

    Cliquez sur le menu Apple, puis sur Restart. Si le problème persiste, éteignez l'appareil, déconnectez tous les périphériques externes, attendez 30 secondes, puis redémarrez.

4. **Renommer le fichier.**

    Faites un clic droit sur le fichier et cliquez sur Rename. Utilisez des noms simples et évitez les caractères spéciaux comme !@# ou les espaces.

5. **Reconnecter le périphérique de stockage.**

    Si vous utilisez un disque externe, par exemple un disque USB, éjectez-le d'abord avant de le débrancher, attendez 10 secondes, puis rebranchez-le. Vous pouvez aussi essayer un autre port USB.

6. **Réparer les erreurs du disque avec First Aid.**

    Des données corrompues sur le disque peuvent provoquer des échecs d'écriture. Vous pouvez utiliser Utilitaire de disque de macOS pour corriger le problème.
    
    1. Ouvrez Finder -> Applications -> Utilities -> Disk Utility.
    2. Sélectionnez le lecteur/périphérique de stockage (local ou externe) dans la barre latérale gauche.
    3. Cliquez sur First Aid -> Run. Attendez la fin du processus.

7. **Ajuster le système de fichiers ou formater le disque.**

    Si vous utilisez un disque formaté en exFAT, des problèmes de compatibilité avec Samba peuvent se produire sous macOS. Vous pouvez essayer les méthodes suivantes.
    
    - **Formater en FAT32** (pour les disques externes, avec compatibilité multiplateforme)
    
        1. Sauvegardez d'abord les données du disque (le formatage efface tous les fichiers).
        2. Ouvrez Disk Utility -> sélectionnez le disque -> Erase.
        3. Choisissez "MS-DOS (FAT)" (FAT32) comme format -> cliquez sur Erase.

    - **Formater en ext4**
    
        !!! Note
        
            ext4 est principalement pris en charge par les systèmes Linux. Après un formatage en ext4, le périphérique de stockage peut devenir incompatible avec les systèmes d'exploitation Windows, ce qui peut entraîner des problèmes tels que l'impossibilité de reconnaître le lecteur ou d'y écrire depuis des appareils Windows.
        
        1. Sauvegardez toutes les données du disque, car le formatage les effacera.
        2. Utilisez un outil comme Disk Utility ou un système Linux pour formater le disque en ext4.

8. **Mettre à jour macOS et vider les caches.**

    Un logiciel obsolète ou des caches corrompus peuvent provoquer des conflits. Accédez à System Settings -> General -> Software Update et installez la dernière version, puis videz les caches système.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
