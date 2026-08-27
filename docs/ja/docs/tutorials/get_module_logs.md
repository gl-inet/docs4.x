# モジュールログを取得する方法

一部の GL.iNet ルーターには 3G/4G/5G モジュールが内蔵されています。ネットワーク接続が不安定な場合は、分析のためにモジュールログをエクスポートする必要があることがあります。

以下に、セルラーモジュールのログをエクスポートする手順を示します。

## 1. コンピューターをルーターに接続する

ノートPCをルーターの Wi-Fi に接続します（SSID とパスワードは本体底面ラベルで確認できます）。または、Ethernet ケーブルを使って、コンピューターの Ethernet ポートをルーターの LAN ポートに接続してください。

## 2. SSHでルーターにログインする

[こちら](ssh_log_in_to_the_router.md)を参照してください。

## 3. モジュールログを取得する

### GL-XE300/GL-X750/GL-X300B の場合

1. 次のコマンドを使用して GL.iNet サーバーから qlog を取得し、qlog ファイルの SHA256 が正しいことを確認します。

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

2. USB フラッシュドライブを挿入し、`df` コマンドでマウントパスを確認して控えておきます。

    私の USB フラッシュドライブのマウントパスは `/tmp/mountd/disk1_part1` です。

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. 次のコマンドでモジュールのデバッグモードを有効にします。

    ```
    gl_modem AT AT+QCFG="dbgctl",0
    ```

4. 次のコマンドで qlog を開始します。

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

    `/tmp/mountd/disk1_part1` は私の USB フラッシュドライブのパスです。実際にはご自身のパスに変更してください。

5. 次のコマンドでモジュールを再起動します。

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. 1～3分待ってから、次のコマンドで qlog を停止します。

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. USB フラッシュドライブ内にディレクトリが作成され、その中に複数のファイルが保存されます。これらは qlog で取得したデータであり、Quectel のツールでデコードする必要があります。これらのファイルを GL.iNet または Quectel の技術サポートへ送付してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 の場合

1. USB フラッシュドライブを挿入し、`df` コマンドでマウントパスを確認して控えておきます。

    私の USB フラッシュドライブのマウントパスは `/tmp/mountd/disk1_part1` です。

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. GL.iNet サーバーから qlog を取得し、qlog ファイルの SHA256 が正しいことを確認します。

    次のコマンドで qlog を取得します。

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

3. 次のコマンドで qlog を開始します。

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. 次のコマンドでモジュールを再起動します。

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. qlog でパケットを取得した後、次のコマンドで qlog を停止します。

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. USB フラッシュドライブ内にディレクトリが作成され、その中に複数のファイルが保存されます。これらは qlog で取得したデータであり、Quectel のツールでデコードする必要があります。これらのファイルを GL.iNet または Quectel の技術サポートへ送付してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
