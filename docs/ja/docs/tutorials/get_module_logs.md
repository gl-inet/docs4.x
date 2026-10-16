# qlogでモデムログを取得する方法

一部のGL.iNetルーターには、3G/4G/5Gモデムが内蔵されています。ネットワーク接続が不安定な場合は、分析のためにモデムログをエクスポートする必要があることがあります。

以下の手順で、セルラーモデムのログをエクスポートします。

## 1. コンピューターをルーターに接続する

ノートPCをルーターの Wi-Fi に接続します（SSID とパスワードは本体底面ラベルで確認できます）。または、Ethernet ケーブルを使って、コンピューターの Ethernet ポートをルーターの LAN ポートに接続してください。

## 2. SSHでルーターにログインする

[こちら](ssh_log_in_to_the_router.md)を参照してください。

## 3. モデムログを取得する

デバイスのモデルに対応する手順を選択してください。

### GL-E5800

1. USBメモリーを挿入し、`df -h` を実行してマウントパスを確認し、記録します。

    以下の例では、USBメモリーは `/tmp/mountd/disk1_part1` にマウントされています。

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. cfg設定ファイルをダウンロードします。

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. 次のコマンドを実行して、モデムログの取得を開始します。`/tmp/mountd/disk1_part1` は、USBメモリーの実際のマウントパスに置き換えてください。

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. モデムを再起動します。`<sim_slot>` は、現在有効なSIMカードスロットの番号（`1` または `2`）に置き換えてください。

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    たとえば、SIMカード **1** が有効な場合:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. 3分待ってから、次のコマンドを実行してqlogを停止します。

    ```
    diag_mdlog -k
    ```

6. USBメモリーにフォルダーが作成されます。このフォルダーにはqLogで取得したデータファイルが保存されており、デコードにはQuectelツールが必要です。これらのファイルをGL.iNetまたはQuectelのテクニカルサポートへ送信してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000

1. USBメモリーを挿入し、`df -h` を実行してマウントパスを確認し、記録します。

    以下の例では、USBメモリーは `/tmp/mountd/disk1_part1` にマウントされています。

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. cfg設定ファイルをダウンロードします。

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. qlogツールをダウンロードします。

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. 次のコマンドを実行してqlogを開始します。`/tmp/mountd/disk1_part1` は、USBメモリーの実際のマウントパスに置き換えてください。

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. モデムを再起動します。

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. 3分待ってから、次のコマンドを実行してqlogを停止します。

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. USBメモリーにフォルダーが作成されます。このフォルダーにはqLogで取得したデータファイルが保存されており、デコードにはQuectelツールが必要です。これらのファイルをGL.iNetまたはQuectelのテクニカルサポートへ送信してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B

1. USBメモリーを挿入し、`df -h` を実行してマウントパスを確認し、記録します。

    以下の例では、USBメモリーは `/tmp/mountd/disk1_part1` にマウントされています。

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. 次のコマンドを実行して、GL.iNetサーバーからqlogをダウンロードします。

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. 次のコマンドを実行して、モデムのデバッグモードを有効にします。

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. 次のコマンドを実行してqlogを開始します。`/tmp/mountd/disk1_part1` は、USBメモリーの実際のマウントパスに置き換えてください。

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. モデムを再起動します。

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. 3分待ってから、次のコマンドを実行してqlogを停止します。

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. USBメモリーにフォルダーが作成されます。このフォルダーにはqLogで取得したデータファイルが保存されており、デコードにはQuectelツールが必要です。これらのファイルをGL.iNetまたはQuectelのテクニカルサポートへ送信してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000

1. USBメモリーを挿入し、`df -h` を実行してマウントパスを確認し、記録します。

    以下の例では、USBメモリーは `/tmp/mountd/disk1_part1` にマウントされています。

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. 次のコマンドを実行して、GL.iNetサーバーからqlogをダウンロードします。

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. 次のコマンドを実行してqlogを開始します。`/tmp/mountd/disk1_part1` は、USBメモリーの実際のマウントパスに置き換えてください。

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. モデムを再起動します。

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. 3分待ってから、次のコマンドを実行してqlogを停止します。

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. USBメモリーにフォルダーが作成されます。このフォルダーにはqLogで取得したデータファイルが保存されており、デコードにはQuectelツールが必要です。これらのファイルをGL.iNetまたはQuectelのテクニカルサポートへ送信してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
