# Récupérer les journaux du module

Certains routeurs GL.iNet sont équipés de modules 3G/4G/5G intégrés. Lorsque la connexion réseau est instable, il peut être nécessaire d'exporter le journal du module pour l'analyser.

Voici les étapes pour exporter le journal du module cellulaire.

## 1. Connecter votre ordinateur au routeur

Connectez un ordinateur portable au Wi-Fi du routeur (vous trouverez le SSID et le mot de passe sur l'étiquette située sous l'appareil), ou connectez le port Ethernet de votre ordinateur au port LAN du routeur à l'aide d'un câble Ethernet.

## 2. Se connecter au routeur en SSH

Veuillez consulter [ce lien](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Récupérer les journaux du module

### Pour GL-XE300/GL-X750/GL-X300B

1. Utilisez les commandes suivantes pour récupérer qlog depuis le serveur GL.iNet et vérifier que le SHA256 du fichier qlog est correct.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

2. Insérez une clé USB et utilisez la commande df pour obtenir le chemin de montage ; mémorisez ce chemin.

    Le chemin de montage de ma clé USB est `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. Utilisez la commande suivante pour activer le mode de débogage du module.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Utilisez la commande suivante pour démarrer qlog.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

    Ici, `/tmp/mountd/disk1_part1` correspond au chemin de ma clé USB ; vous devez le remplacer par votre propre chemin.

5. Utilisez la commande suivante pour redémarrer le modem.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Attendez 1 à 3 minutes, puis utilisez la commande suivante pour arrêter qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. Vous trouverez un dossier sur la clé USB contenant plusieurs fichiers. Il s'agit des données récupérées par qlog, qui doivent être décodées à l'aide d'un outil Quectel ; veuillez donc envoyer ces fichiers à l'assistance technique de GL.iNet ou de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### Pour GL-X3000/GL-XE3000

1. Insérez une clé USB et utilisez la commande df pour obtenir le chemin de montage ; mémorisez ce chemin.

    Le chemin de montage de ma clé USB est `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Récupérez qlog depuis le serveur GL.iNet et vérifiez que le SHA256 du fichier qlog est correct.

    Utilisez les commandes suivantes pour récupérer qlog
    
    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    
    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4  && sha256sum qlog-mtk7981a-sha256-78dda4 && sha256sum /etc/default_v15.cfg
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_get_qlog.png){class="glboxshadow"}

3. Utilisez la commande suivante pour démarrer qlog.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```
    
4. Utilisez la commande suivante pour redémarrer le modem.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Après avoir capturé les paquets avec qlog, utilisez la commande suivante pour arrêter qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. Vous trouverez un dossier sur la clé USB contenant plusieurs fichiers. Il s'agit des données récupérées par qlog, qui doivent être décodées à l'aide d'un outil Quectel ; veuillez donc envoyer ces fichiers à l'assistance technique de GL.iNet ou de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
