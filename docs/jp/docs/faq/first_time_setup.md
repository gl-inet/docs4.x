# 初めてのセットアップ

GL.iNetルーターの初回セットアップは非常に似ています。ほとんどの機種にWi-Fiモジュールが搭載されていますが、Wi-Fiモジュールが搭載されていない机型もあります。そのため、以下の案内はWi-Fi モジュールの有無に基づい て2つのケースに分けられます。

* [Wi-Fi搭載モデルの場合](#for-models-that-have-wi-fi)
* [Wi-Fi非搭載モデルの場合](#for-models-that-dont-have-wi-fi)

## Wi-Fi搭載モデルの場合 {#for-models-that-have-wi-fi}

以下はGL-AXT1800（Slate AX）の例です。

パッケージに same 梱されている以下のものをご用意ください。

- GL-AXT1800
- 電源アダプタ
- イーサネットケーブル

以下のビデオガイドを見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>（このビデオでは、手顺がほとんどのルーター機種で同じため、异なるGL.iNetルーターを使用してセットアップを説明しています。）</small>

1. 電源オン

    TFカードを使用する場合は、ルーターの電源を入れる前に挿入してください。TFカードのホットスワップはサポートされていません。

    電源アダプターの一端をルーターに差し込み、もう一端をコンセントに差し込みます。自動的に電源が入ります。

2. ルーターに接続する

    イーサネットケーブルまたはWi-Fi経由でルーターに接続できます。

    * ケーブル経由で接続する

        パソコンをイーサネットケーブルでルーターのLANポートに接続します。

    * Wi-Fiで接続する

        Wi-Fi SSIDはルーターの底面ラベルに以下のフォーマットで印刷されています：

        **GL-AXT1800-XXX** または **GL-AXT1800-XXX-5G**

        デフォルトのWi-Fi KeyはSSIDの下にあります。

        パソコン、スマホ、タブレットでルーターのSSIDを検索し、Wi-Fi Keyを入力します。一部のモデルでWi-Fiパスワードがラベルに見つからない場合は、**goodlife**をお試しください。

        **ヒント:** 底面ラベルにあるQRコードにはデフォルトのWi-Fi情報が含まれています。スマートフォンのQRコードスキャン器でスキャンすることで素早く接続できます。

        **注意:** Wi-Fiに接続した後、すぐにインターネットにアクセスできない場合があります。インターネットにアクセスする前に、次の手順でネットワークを設定してください。

3. Web管理パネルにログインする

    ウェブブラウザ（Chrome、Edge、Safariを推奨）を開き、[http://192.168.8.1](http://192.168.8.1)にアクセスします。ウェブ管理パネルの初期セットアップが表示されます。

    ウェブ管理パネルにアクセスできない場合は、[こちら](cannot_access_web_admin_panel.md)をご確認ください。

    言語を選択し、**次へ**をクリックして続行します。

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    管理者パスワードを設定します。強力なパスワードを使用することをお勧めします。**適用**をクリックして続行します。

    **注意**: 初期化中にWi-Fiが切れる場合があります必らずずルーターに再接続してください。

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    初期セットアップの後、ルーターのウェブ管理パネルに入ります。

    ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. インターネットに接続する

    * [イーサネットケーブル経由でインターネットに接続する](../interface_guide/internet_ethernet.md)
    * [既存のWi-Fi経由でインターネットに接続する](../interface_guide/internet_repeater.md)
    * [USBテザリングでインターネットに接続する](../interface_guide/internet_tethering.md)
    * [USBモデム経由でインターネットに接続する](../interface_guide/internet_cellular.md)

## Wi-Fi非搭載モデルの場合 {#for-models-that-dont-have-wi-fi}

以下はGL-MT2500A（Brume 2）の例です。

1. 電源オン

    電源アダプターの一端をルーターに差し込み、もう一端をコンセントに差し込みます。ルーターは自動的に電源が入ります。

2. ルーターに接続する

    イーサネットケーブルまたはWi-Fi経由でルーターに接続できます。

    * イーサネットケーブルで直接接続

        パソコンをイーサネットケーブルでルーターのLANポートに接続します。この設定方法はシンプルで分かりやすいので推奨します。

    * 別のルーターのWi-Fiで接続

        GL-MT2500Aには内蔵Wi-Fiモジュールがないため、別のWi-Fi機能付きルーターを使用してGL-MT2500Aを初期化できます。

        * 方法1: 2台目のルーターをAP（Access Point）モードに設定し、GL-MT2500AのLANポートを2台目のルーターのWANポートに接続します。

        * 方法2: 2台目のルーターをデフォルトのルーターモードのままにし、192.168.8.1/24と競合しない別のルーターIPアドレス（例：192.168.10.1）を持っていることを確認し、GL-MT2500AのLANポートを2台目のルーターのWANポートに接続します。

        パソコンまたはスマートフォンを使って、2台目のルーターのWi-Fiに接続します。

        !!! 注意

            ここでいう2台目のルーターとは、GL.iNet GL-AXT1800、TP-LINK、Netgearなどの一般的なルーターです。ISP提供の光ネットワークターミナルまたはデバイスはこのシナリオでは動作しない場合があります。

3. Web管理パネルにアクセスする

    ウェブブラウザ（Chrome、Edge、Safariを推奨）を開き、[http://192.168.8.1](http://192.168.8.1)にアクセスします。ウェブ管理パネルの初期セットアップが表示されます。ウェブ管理パネルにアクセスできない場合は、[こちら](cannot_access_web_admin_panel.md)をご確認ください。

    言語を選択し、**次へ**をクリックして続行します。

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    管理者パスワードを設定します。強力なパスワードを使用することをお勧めします。**送信**をクリックして続行します。

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    初期セットアップの後、ルーターのウェブ管理パネルに入ります。

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. インターネットに接続する

    * [イーサネットケーブル経由でインターネットに接続する](../interface_guide/internet_ethernet.md)
    * [USBテザリングでインターネットに接続する](../interface_guide/internet_tethering.md)
    * [USBモデム経由でインターネットに接続する](../interface_guide/internet_cellular.md)

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
