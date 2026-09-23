# アップグレード

Web管理パネルの左側で、**SYSTEM** -> **Upgrade** に移動すると、ルーターのファームウェアを更新できます。

一部のセルラーモデルでは、必要に応じてモジュールバージョンもアップグレードできます。

!!! Note

    アップグレード中は電源を入れたままにしてください。ルーターの電源を **切らないでください**。アップグレード後、デバイスは自動的に再起動します。これには数分かかる場合があります。

## ファームウェアアップグレード

### オンラインアップグレード

ここで現在のファームウェアバージョンを確認できます。

![upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/online_upgrade.png){class="glboxshadow"}

- **Accept Preview Plan**

    有効にすると、正式版の公開前に新機能を試してフィードバックを送信できます。これらのアップグレードは安定していない場合があります。


**Note**: オンラインアップグレード時に **Download Failed** と表示された場合は、**SYSTEM** -> **Time Zone** に移動し、タイムゾーンのエラーを修正してください（ブラウザと同期）。

![online download failed](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/online_download_failed.jpg){class="glboxshadow" width="360"}

![time zone](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/time_zone.png){class="glboxshadow"}

### ローカルアップグレード

ファームウェアファイルを選択するか、ドラッグ&ドロップしてアップグレードできます。ファームウェアは [download center](https://dl.gl-inet.com){target="_blank"} からダウンロードできます。

![local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/local_upgrade.png){class="glboxshadow"}

アップロード後、ファームウェアの検証が行われます。

![local upgrade uploaded](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/local_upgrade_uploaded.png){class="glboxshadow"}

- **Keep Settings:** このオプションを有効にすると、現在の設定が保持され、アップグレード完了後にユーザーがインストールしたパッケージの再インストールを求められます。ファームウェアをダウングレードするときは、このオプションをチェックしないでください。

**Install** をクリックしてアップグレードします。

## モデムアップグレード

GL.iNet のセルラールーターでは、Web管理パネルからセルラーモデムのファームウェアをアップグレードできます。

セルラーネットワークが接続できない、または不安定な場合は、セルラーモジュールのアップグレードを試すことができます。モデムのアップグレードを実行する前に、まず技術サポートへ連絡してトラブルシューティングすることをおすすめします。

### オンラインアップグレード

ここで現在のセルラーモデムのバージョンを確認できます。ルーターがインターネットに接続されていれば、メーカーのサーバーから最新のセルラーモデムバージョンを自動で確認し、更新作業を簡単に行えます。

![modem online upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_online_upgrade.png){class="glboxshadow"}

### ローカルアップグレード

必要に応じて、コンピューターからモデムのファームウェアファイルを手動でアップロードしてセルラーモデムを更新できます。

![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

## DPIオンラインアップグレード

DPIオンラインアップグレードは、DPIエンジンとシグネチャデータベースを確認して更新し、データ統計、コンテンツフィルター、その他のDPI関連機能でトラフィックを正確に識別できるようにします。

**注**：この機能はファームウェアv4.11で導入されました。

![dpi online upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/dpi_online_upgrade.png){class="glboxshadow" width=700}

---

ご不明な点がありましたら、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
