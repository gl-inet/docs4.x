# Comment capturer les journaux du modem avec qlog

Certains routeurs GL.iNet disposent de modems 3G/4G/5G intégrés. Lorsque la connexion réseau est instable, il peut être nécessaire d’exporter les journaux du modem pour les analyser.

Voici les étapes permettant d’exporter les journaux du modem cellulaire.

## 1. Connecter votre ordinateur au routeur

Connectez un ordinateur portable au Wi-Fi du routeur (vous trouverez le SSID et le mot de passe sur l'étiquette située sous l'appareil), ou connectez le port Ethernet de votre ordinateur au port LAN du routeur à l'aide d'un câble Ethernet.

## 2. Se connecter au routeur en SSH

Veuillez consulter [ce lien](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Obtenir les journaux du modem

Sélectionnez les étapes correspondant au modèle de votre appareil.

### GL-E5800

1. Insérez une clé USB, puis exécutez `df -h` pour obtenir son chemin de montage et notez-le.

    Dans l’exemple suivant, la clé USB est montée sur `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Téléchargez le fichier de configuration cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Exécutez la commande suivante pour démarrer la capture des journaux du modem. Remplacez `/tmp/mountd/disk1_part1` par le chemin de montage réel de votre clé USB.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Redémarrez le modem. Remplacez `<sim_slot>` par le numéro de l’emplacement de la carte SIM actuellement active (`1` ou `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Par exemple, si la carte SIM **1** est active :

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Patientez 3 minutes, puis exécutez la commande suivante pour arrêter qlog.

    ```
    diag_mdlog -k
    ```

6. Vous trouverez sur la clé USB un dossier contenant les données capturées par qLog. Ces fichiers nécessitent l’outil Quectel pour être décodés. Envoyez-les au support technique de GL.iNet ou de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000

1. Insérez une clé USB, puis exécutez `df -h` pour obtenir son chemin de montage et notez-le.

    Dans l’exemple suivant, la clé USB est montée sur `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Téléchargez le fichier de configuration cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Téléchargez l’outil qlog.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Exécutez la commande suivante pour démarrer qlog. Remplacez `/tmp/mountd/disk1_part1` par le chemin de montage réel de votre clé USB.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Redémarrez le modem.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Patientez 3 minutes, puis exécutez la commande suivante pour arrêter qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Vous trouverez sur la clé USB un dossier contenant les données capturées par qLog. Ces fichiers nécessitent l’outil Quectel pour être décodés. Envoyez-les au support technique de GL.iNet ou de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B

1. Insérez une clé USB, puis exécutez `df -h` pour obtenir son chemin de montage et notez-le.

    Dans l’exemple suivant, la clé USB est montée sur `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Exécutez les commandes suivantes pour télécharger qlog depuis le serveur GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Exécutez la commande suivante pour activer le mode de débogage du modem.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Exécutez la commande suivante pour démarrer qlog. Remplacez `/tmp/mountd/disk1_part1` par le chemin de montage réel de votre clé USB.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Redémarrez le modem.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Patientez 3 minutes, puis exécutez la commande suivante pour arrêter qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Vous trouverez sur la clé USB un dossier contenant les données capturées par qLog. Ces fichiers nécessitent l’outil Quectel pour être décodés. Envoyez-les au support technique de GL.iNet ou de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000

1. Insérez une clé USB, puis exécutez `df -h` pour obtenir son chemin de montage et notez-le.

    Dans l’exemple suivant, la clé USB est montée sur `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Exécutez les commandes suivantes pour télécharger qlog depuis le serveur GL.iNet.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Exécutez la commande suivante pour démarrer qlog. Remplacez `/tmp/mountd/disk1_part1` par le chemin de montage réel de votre clé USB.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Redémarrez le modem.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Patientez 3 minutes, puis exécutez la commande suivante pour arrêter qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. Vous trouverez sur la clé USB un dossier contenant les données capturées par qLog. Ces fichiers nécessitent l’outil Quectel pour être décodés. Envoyez-les au support technique de GL.iNet ou de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
