# Mettre à niveau le firmware du module Quectel

## Préparation

1. Assurez-vous que votre routeur est configuré pour accéder à Internet.

2. Connectez un ordinateur de bureau ou portable au routeur via le Wi-Fi ou un câble Ethernet.

## Étapes de mise à niveau

### Pour GL-X3000/GL-XE3000

**Méthode 1. Mise à niveau via l’interface GL.iNet**

1. Téléchargez le firmware du module correspondant depuis le bas de ce tutoriel.

2. Connectez-vous au panneau d’administration Web de votre routeur, puis accédez à **SYSTEM** -> **Upgrade** -> **Modem Local Upgrade**, et téléversez le firmware du module (au format .zip).
    
    ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

**Méthode 2. Mise à niveau via SSH**

Prenons comme exemple la mise à niveau du module RM520N.

1. Connectez-vous à votre routeur en SSH. Veuillez consulter [ce lien](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

2. Saisissez la commande ci-dessous pour télécharger le firmware de module.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Saisissez la commande ci-dessous pour décompresser le firmware de module.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Mettez à niveau le firmware du module à l’aide de la commande QFirehose, comme indiqué ci-dessous.

    **Remarque** : remplacez "/RM520NGLAAR03A03M4G_01.201.01201" par le chemin réel du dossier du firmware de module.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Patientez quelques minutes. Une fois la mise à niveau terminée, le système affichera "Upgrade module successfully".

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Redémarrez votre routeur, puis reconnectez-vous à votre routeur en SSH.

7. Exécutez la commande suivante pour confirmer une nouvelle fois que la mise à niveau du module a réussi.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Pour GL-MiFi/GL-XE300/GL-X750/GL-E750

Prenons comme exemple la mise à niveau du module EM060K.

1. Préparez une clé USB. Téléchargez le firmware de module correspondant sur la clé USB depuis le bas de ce tutoriel, puis décompressez le fichier .zip et placez-le dans le répertoire racine de la clé USB.

2. Branchez la clé USB sur votre routeur. Consultez ensuite [ce lien](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) pour vous connecter à votre routeur en SSH.

3. Saisissez la commande `df - h` pour vérifier le chemin de montage de la clé USB, puis notez ce chemin.

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Saisissez la commande `ls -l` pour vérifier le dossier du firmware de module.

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Saisissez la commande ci-dessous pour récupérer QFirehose depuis le serveur GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Accordez-lui ensuite les autorisations d’exécution.

    ``` 
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Mettez à niveau le firmware du module à l’aide de la commande QFirehose, comme indiqué ci-dessous.

    **Remarque** : remplacez "/mnt/sdb1/EM060KGLAAR01A12M2GA" par le chemin réel du dossier du firmware de module.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Patientez quelques minutes. Une fois la mise à niveau terminée, le système affichera "Upgrade module successfully".

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Redémarrez votre routeur, puis reconnectez-vous à votre routeur en SSH.

9. Exécutez la commande suivante pour confirmer une nouvelle fois que la mise à niveau du module a réussi.

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## URL de téléchargement des firmwares de modules Quectel

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
