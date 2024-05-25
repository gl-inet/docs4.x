# モジュールログの取得

一部のGL.iNetルーターには、内蔵の3G、4G、または5Gモジュールが搭載されています。ネットワーク接続がスムーズでない場合、モジュールのログをエクスポートして分析する必要があるかもしれません。以下にその手順を示します。

## デバイスにコンピュータを接続する

ラップトップのWi-Fiを使用してデバイスのSSIDに接続します（SSIDとWi-Fiパスワードはデバイスの底面ラベルに記載されています）、またはイーサネットケーブルを使用してデバイスのLANポートとコンピュータのイーサネットポートに接続します。

## SSHプロトコルを使用してデバイスにログインする

こちらのリンクを参照してください: [https://docs.gl-inet.com/router/en/3/tutorials/ssh/](https://docs.gl-inet.com/router/en/3/tutorials/ssh/)

## GL-XE300/GL-X750/GL-X300の場合

### GL.iNetサーバーからqlogを取得し、qlogファイルのSHA256が正しいことを確認する

以下のコマンドを使用してqlogを取得します

```
cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
```

```
chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
```

![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

### qlogの使用

1. USBフラッシュディスクを挿入し、dfコマンドを使用してマウントパスを取得し、そのパスを覚えておきます

    私のUSBフラッシュディスクのマウントパスは `/tmp/mountd/disk1_part1` です

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. 以下のコマンドを使用してモジュールデバッグモードを開きます

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

3. 以下のコマンドを使用してqlogを起動します

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

    `/tmp/mountd/disk1_part1` は私のUSBフラッシュディスクです。パスはご自身のパスに変更してください。

4. 以下のコマンドを使用してモデルを再起動します。

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

5. 1〜3分待ち、以下のコマンドを使用してqlogを停止します

    ```
    killall qlog*
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

6. USBフラッシュディスクにディレクトリが見つかり、その中にいくつかのファイルが存在します。これらのファイルはqlogの取得データであり、Quectelツールを使用してデコードする必要があります。これらのファイルをGL.iNetまたはQuectelの技術サポートに送信してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

## GL-X3000/GL-XE3000の場合

1. USBフラッシュディスクを挿入し、dfコマンドを使用してマウントパスを取得し、そのパスを覚えておきます

    私のUSBフラッシュディスクのマウントパスは `/tmp/mountd/disk1_part1` です

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. GL.iNetサーバーからqlogを取得し、qlogファイルのsha256が正しいことを確認する

    以下のコマンドを使用してqlogを取得します
    
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

3. 以下のコマンドを使用してqlogを起動します

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

4. qlogでパケットをキャプチャした後、以下のコマンドを使用してqlogを停止します

    ```
    killall qlog*
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

5. USBフラッシュディスクにディレクトリが見つかり、その中にいくつかのファイルが存在します。これらのファイルはqlogの取得データであり、Quectelツールを使用してデコードする必要があります。これらのファイルをGL.iNetまたはQuectelの技術サポートに送信してください。

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
