# 初めてのセットアップ

GL.iNetルーターの初回セットアップ手順は、どのモデルでもほぼ同じです。ほとんどのモデルにはWi-Fiモジュールが搭載されていますが、一部のモデルには搭載されていません。

そのため、以下の手順はWi-Fiモジュールの有無に応じて2つのケースに分けています。

* [Wi-Fi搭載モデルの場合](#for-models-that-have-wi-fi)
* [Wi-Fi非搭載モデルの場合](#for-models-that-dont-have-wi-fi)

## Wi-Fi搭載モデルの場合 {#for-models-that-have-wi-fi}

以下の手順では、GL-MT3000（Beryl AX）を例として使用します。

パッケージに同梱されている以下のものを準備してください。

- ルーター GL-MT3000（Beryl AX）
- 電源アダプター
- イーサネットケーブル

以下のビデオガイドを見るか、下記の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. **電源を入れる**

    電源アダプターの一端をルーターに接続し、もう一端をコンセントに差し込みます。ルーターは自動的に起動します。
    
    一部のモデル（Slate AXなど）にはTFカードスロットが搭載されています。TFカードを使用する場合は、ルーターの電源を入れる前にカードを挿入してください。TFカードのホットスワップはサポートされていません。

2. **ルーターに接続する**

    デバイス（スマートフォン、ノートパソコン、パソコンなど）をイーサネットケーブルまたはWi-Fiでルーターに接続します。

    * Ethernetで接続する: デバイスをイーサネットケーブルでルーターのLANポートに接続します。

    * Wi-Fiで接続する: ルーター底面のラベルでWi-Fi SSIDとWi-Fi Keyを確認します。デバイスでルーターのSSIDを検索し、Wi-Fi Keyを入力します。

        !!! tip
        
            1. 底面ラベルのQRコードには、デフォルトのWi-Fi情報が含まれています。QRコードスキャナーで読み取ると、すばやく接続できます。
            2. 一部の古いモデルでラベルにWi-Fi Keyが記載されていない場合は、"goodlife" を試してください。
        
    Wi-Fiに接続しても、すぐにインターネットへアクセスできない場合があります。インターネットへアクセスする前に、次の手順に従ってネットワークを設定してください。

3. **Web管理パネルにログインする**

    Webブラウザ（互換性のためChrome、Edge、Safariを推奨）を開き、[http://192.168.8.1](http://192.168.8.1)にアクセスします。GL.iNetのログインページに移動します。Web管理パネルにアクセスできない場合は、トラブルシューティングとして[こちら](cannot_access_web_admin_panel.md)をクリックしてください。

    管理者パスワードを設定し、**Next**をクリックします。

    ![mt3000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_password.png){class="glboxshadow"}

    Wi-Fiを設定します。Wi-Fi情報を変更した場合は、更新後のWi-Fiに再接続してから**Next**をクリックしてください。

    ![mt3000 set up wifi](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_set_up_wifi.png){class="glboxshadow"}

    ルーターの初期化が完了するまで待ちます。

    ![mt3000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_initializing.png){class="glboxshadow"}

    その後、ルーターのWeb管理パネルにアクセスできます。

    ![mt3000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_panel.png){class="glboxshadow"}

4. **インターネットに接続する**

    * [イーサネットケーブル経由でインターネットに接続する](../interface_guide/internet_ethernet.md)
    * [既存のWi-Fi経由でインターネットに接続する](../interface_guide/internet_repeater.md)
    * [USBテザリングでインターネットに接続する](../interface_guide/internet_tethering.md)
    * [USBモデム経由でインターネットに接続する](../interface_guide/internet_cellular.md)

## Wi-Fi非搭載モデルの場合 {#for-models-that-dont-have-wi-fi}

以下の手順では、GL-MT5000（Brume 3）を例として使用します。

1. **電源を入れる**

    電源アダプターの一端をルーターに接続し、もう一端をコンセントに差し込みます。ルーターは自動的に起動します。

2. **ルーターに接続する**

    デバイス（ノートパソコン、パソコンなど）をイーサネットケーブルでルーターのLANポートに接続します。

3. **Web管理パネルにログインする**

    Webブラウザ（互換性のためChrome、Edge、Safariを推奨）を開き、[http://192.168.8.1](http://192.168.8.1)にアクセスします。GL.iNetのログインページに移動します。Web管理パネルにアクセスできない場合は、トラブルシューティングとして[こちら](cannot_access_web_admin_panel.md)をクリックしてください。

    管理者パスワードを設定し、**Next**をクリックします。

    ![mt5000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_password.png){class="glboxshadow"}

    ルーターの初期化が完了するまで待ちます。

    ![mt5000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_initializing.png){class="glboxshadow"}

    その後、ルーターのWeb管理パネルにアクセスできます。

    ![mt5000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_panel.png){class="glboxshadow"}

4. **インターネットに接続する**

    * [イーサネットケーブル経由でインターネットに接続する](../interface_guide/internet_ethernet.md)
    * [USBテザリングでインターネットに接続する](../interface_guide/internet_tethering.md)
    * [USBモデム経由でインターネットに接続する](../interface_guide/internet_cellular.md)

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
