# Quectelモジュールファームウェアをアップグレードする方法

## 事前準備

1. ルーターがインターネットへ接続できる状態であることを確認します。

2. コンピューターまたはノートPCを、Wi-Fiまたはイーサネットケーブルでルーターへ接続します。

## アップグレード手順

### GL-X3000 / GL-XE3000 の場合

**方法1: GL.iNet GUI からアップグレードする**

1. このチュートリアルの末尾から、対応するモジュールファームウェアをダウンロードします。

2. ルーターの Web 管理画面にログインし、**SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** に移動して、モジュールファームウェア（`.zip` 形式）をアップロードします。

   ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

**方法2: SSH からアップグレードする**

ここでは RM520N モジュールのアップグレードを例に説明します。

1. SSHでルーターへログインします。[こちら](ssh_log_in_to_the_router.md)を参照してください。

2. 次のコマンドでモジュールファームウェアをダウンロードします。

   ```
   wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
   ```

   ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. 次のコマンドでモジュールファームウェアを展開します。

   ```
   unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
   ```

   ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. 次のように QFirehose コマンドを使ってモジュールファームウェアをアップグレードします。

   **Note**: `"/RM520NGLAAR03A03M4G_01.201.01.201"` は実際のモジュールファームウェアフォルダーのパスに置き換えてください。

   ```
   QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
   ```

   ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. 数分待ちます。アップグレードが完了すると、システムに `Upgrade module successfully` と表示されます。

   ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. ルーターを再起動し、再度SSHでルーターへログインします。

7. 次のコマンドを実行し、モジュールのアップグレードが正常に完了したか再確認します。

   ```
   gl_modem -B 0001:01:00.0 AT AT+QGMR
   ```

   ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### GL-MiFi / GL-XE300 / GL-X750 / GL-E750 の場合

ここでは EM060K モジュールのアップグレードを例に説明します。

1. USBメモリを用意します。このチュートリアルの末尾から対応するモジュールファームウェアをUSBメモリにダウンロードし、`.zip` ファイルを展開してUSBドライブのルートディレクトリへ配置します。

2. USBメモリをルーターに接続します。その後、[こちら](ssh_log_in_to_the_router.md)を参照してSSHでルーターへログインします。

3. `df - h` コマンドを入力し、USBドライブのマウントパスを確認して控えます。

   ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. `ls -l` コマンドを入力し、モジュールファームウェアのフォルダー名を確認します。

   ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. 次のコマンドでGL.iNetサーバーからQFirehoseを取得します。

   ```
   cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
   ```

   続いて、実行権限を付与します。

   ```
   chmod 775 /usr/bin/QFirehose-ar9531
   ```

   ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. 次のように QFirehose コマンドを使ってモジュールファームウェアをアップグレードします。

   **Note**: `"/mnt/sdb1/EM060KGLAAR01A12M2GA"` は実際のモジュールファームウェアフォルダーのパスに置き換えてください。

   ```
   /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
   ```

   ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. 数分待ちます。アップグレードが完了すると、システムに `Upgrade module successfully` と表示されます。

   ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. ルーターを再起動し、再度SSHでルーターへログインします。

9. 次のコマンドを実行し、モジュールのアップグレードが正常に完了したか再確認します。

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

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
