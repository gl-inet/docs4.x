# Quectelモジュールのファームウェアをアップグレードする

## 準備

1. ルーターがインターネットにアクセスできるよう設定されていることを確認します。

2. コンピューターまたはノートPCをWi-FiまたはEthernetケーブルでルーターに接続します。

## アップグレード手順

### GL-X3000 / GL-XE3000 の場合

**方法1. GL.iNet GUIからアップグレードする**

1. このチュートリアルの末尾から、対応するモジュールファームウェアをダウンロードします。

2. ルーターのWeb管理パネルにログインし、**SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** に移動して、モジュールファームウェア（.zip形式）をアップロードします。

    ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

**方法2. SSH経由でアップグレードする**

ここでは RM520N モジュールのアップグレードを例にします。

1. ルーターへSSHログインします。詳細は[このリンク](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/)を参照してください。

2. 以下のコマンドを入力してモジュールファームウェアをダウンロードします。

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. 以下のコマンドを入力してモジュールファームウェアを解凍します。

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. 以下のように、QFirehose コマンドを使ってモジュールファームウェアをアップグレードします。

    **Note**: "/RM520NGLAAR03A03M4G_01.201.01201" は、実際のモジュールファームウェアフォルダーパスに置き換えてください。

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. 数分待ちます。アップグレードが完了すると、システムに "Upgrade module successfully" と表示されます。

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. ルーターを再起動し、再度SSHログインします。

7. 次のコマンドを実行して、モジュールのアップグレードが成功したか最終確認します。

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### GL-MiFi / GL-XE300 / GL-X750 / GL-E750 の場合

ここでは EM060K モジュールのアップグレードを例にします。

1. USBメモリを用意します。このチュートリアルの末尾から対応するモジュールファームウェアをUSBメモリにダウンロードし、.zip ファイルを解凍してUSBドライブのルートディレクトリに配置します。

2. USBメモリをルーターに挿します。その後、[このリンク](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/)を参照してルーターへSSHログインします。

3. `df - h` コマンドを入力してUSBドライブのマウントパスを確認し、そのパスを控えます。

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. `ls -l` コマンドを入力してモジュールファームウェアのフォルダーを確認します。

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. 以下のコマンドを入力して、GL.iNetサーバーから QFirehose を取得します。

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    その後、実行権限を付与します。

    ```
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. 以下のように、QFirehose コマンドを使ってモジュールファームウェアをアップグレードします。

    **Note**: "/mnt/sdb1/EM060KGLAAR01A12M2GA" は、実際のモジュールファームウェアフォルダーパスに置き換えてください。

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. 数分待ちます。アップグレードが完了すると、システムに "Upgrade module successfully" と表示されます。

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. ルーターを再起動し、再度SSHログインします。

9. 次のコマンドを実行して、モジュールのアップグレードが成功したか最終確認します。

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## QuectelモジュールファームウェアのダウンロードURL

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
