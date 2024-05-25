# Quectelモジュールソフトウェアのアップグレード

## コンピュータをデバイスに接続

ラップトップのWi-Fiを使用してデバイスのSSIDに接続します（SSIDとWi-Fiパスワードはデバイスの底面ラベルに記載されています）。または、イーサネットケーブルを使用してデバイスのLANポートとコンピュータのイーサネットポートを接続します。

## SSHプロトコルを使用してデバイスにログイン

こちらのリンクを参照してください: [https://docs.gl-inet.com/router/en/3/tutorials/ssh/](https://docs.gl-inet.com/router/en/3/tutorials/ssh/)

### GL-MiFi/GL-XE300/GL-X750/GL-X300の場合

1. GL.iNetサーバーからQFirehoseを取得し、QFirehoseファイルのSHA256が正しいことを確認します

    以下のコマンドを使用してQFirehoseを取得します

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531-sha256-7383f4
    ```

    ``` 
    chmod 775 QFirehose-ar9531-sha256-7383f4  && sha256sum QFirehose-ar9531-sha256-7383f4
    ```

    ![ar9531_get_QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_get_QFirehose.png){class="glboxshadow"}

2. USBフラッシュディスクを挿入し、dfコマンドを使用してマウントパスを取得します。パスを覚えておいてください

    私のUSBフラッシュディスクのマウントパスは`/tmp/mountd/disk1_part1`です

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. Quectelモジュールソフトウェアを取得し、アップ圧縮します（例：EP06-A。他のモジュールソフトウェアの場合は、文書の最後の注意事項を参照してください）

    `/tmp/mountd/disk1_part1`は私のUSBフラッシュディスクのパスです。あなたのパスに変更する必要があります

    ```
    wget https://fw.gl-inet.com/tools/quectel_module_software/EP06ALAR02A08M4G_01.004.01.004.zip -P /tmp/mountd/disk1_part1/
    ```

    ![ar9531_get_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_get_quectel_module_software.png){class="glboxshadow"}

    ```
    unzip /tmp/mountd/disk1_part1/EP06ALAR02A08M4G_01.004.01.004.zip -d /tmp/mountd/disk1_part1/EP06ALAR02A08M4G_01.004.01.004
    ```

    ![ar9531_upcompress_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_upcompress_quectel_module_software.png){class="glboxshadow"}

  4. QFirehoseを使用してQuectelモジュールソフトウェアをアップグレード

    ```sh
    QFirehose-ar9531-sha256-7383f4 -f /tmp/mountd/disk1_part1/EP06ALAR02A08M4G_01.004.01.004
    ```

    ![ar9531_upgrade_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_upgrade_quectel_module_software.png){class="glboxshadow"}

5. 次のコマンドを使用してQuectelモジュールソフトウェアのバージョンを確認します。

    ```
    gl_modem AT AT+QGMR
    ```

    ![ar9531_check_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_check_quectel_module_software.png){class="glboxshadow"}

### GL-X3000/GL-XE3000の場合

1. GL.iNetサーバーからQFirehoseを取得し、QFirehoseファイルのSHA256が正しいことを確認します

    以下のコマンドを使用してQFirehoseを取得します

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-mtk7981a-sha256-c0b944
    ```

    ```
    chmod 775 QFirehose-mtk7981a-sha256-c0b944  && sha256sum QFirehose-mtk7981a-sha256-c0b944
    ```

    ![mtk7981a_get_QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_get_QFirehose.png){class="glboxshadow"}

2. Quectelモジュールソフトウェアを取得し、アップ圧縮します（例：RM520。他のモジュールソフトウェアの場合は、文書の最後の注意事項を参照してください）

    ```
    wget https://fw.gl-inet.com/tools/quectel_module_software/RM520NGLAAR01A07M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_get_quectel_module_software.png){class="glboxshadow"}

    ```
    unzip /RM520NGLAAR01A07M4G_01.201.01.201.zip -d /RM520NGLAAR01A07M4G_01.201.01.201
    ```

    ![mtk7981a_upcompress_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_upcompress_quectel_module_software.png){class="glboxshadow"}

3. QFirehoseを使用してQuectelモジュールソフトウェアをアップグレード

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR01A07M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_upgrade_quectel_module_software.png){class="glboxshadow"}

4. 次のコマンドを使用してQuectelモジュールのソフトウェアバージョンを確認します。

    ```
    echo 1 > /sys/devices/platform/11280000.pcie/pci0001:00/0001:00:00.0/0001:01:00.0/remove
    ```

    ```
    echo 1 > /sys/devices/platform/11280000.pcie/pci0001:00/0001:00:00.0/rescan
    ```

    ```
    gl_modem AT AT+QGMR
    ```

    ```
    rm /RM520NGLAAR01A07M4G_01.201.01.201* -rf
    ```

    ![mtk7981a_check_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_check_quectel_module_software.png){class="glboxshadow"}

### QuectelモジュールソフトウェアのダウンロードURL

EP06-A: [https://fw.gl-inet.com/tools/quectel_module_software/EP06ALAR02A08M4G_01.004.01.004.zip](https://fw.gl-inet.com/tools/quectel_module_software/EP06ALAR02A08M4G_01.004.01.004.zip)

RM520: [https://fw.gl-inet.com/tools/quectel_module_software/RM520NGLAAR01A07M4G_01.201.01.201.zip](https://fw.gl-inet.com/tools/quectel_module_software/RM520NGLAAR01A07M4G_01.201.01.201.zip)

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪問してください。
