# 初めてのセットアップ

GL.iNetルーターの初回セットアップは非常に似ています。ほとんどの機種にWi-Fiモジュールが搭載されていますが、Wi-Fiモジュールが搭載されていない機種もありますので、Wi-Fiモジュールの有無で2つのケースに分けて説明します。

* [Wi-Fi搭載モデルの場合](#for-models-that-have-wi-fi)
* [Wi-Fi非搭載モデルの場合](#for-models-that-dont-have-wi-fi)

## Wi-Fi搭載モデルの場合

以下はGL-AXT1800（Slate AX）の例です。

パッケージに同梱されている以下のものをご用意ください。

GL-AXT1800, 電源アダプタ, イーサネットケーブル。

ビデオガイドがあります。

<iframe width="560" height="315" src="https://www.youtube.com/embed/f7DYULL6ZSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. 電源オン

    TF カードを使用する場合は、ルーターの電源を入れる前に挿入してください。 TF カードのホットプラグはサポートされていません。

    電源アダプターの一端をルーターに差し込み、もう一端をコンセントに差し込みます。 自動的に電源が入ります。

2. ルーターに接続する

    イーサネットケーブルまたはWi-Fi経由でルーターに接続できます。

    * ケーブル経由で接続する

        パソコンをイーサネットケーブルでルーターのLANポートに接続します。

    * Wi-Fiで接続する

        SSIDはルーターの底面ラベルに以下のフォーマットで印刷されています：

        **GL-AXT1800-XXX** or **GL-AXT1800-XXX-5G**

        パソコン/スマホ/タブレットでルーターのSSIDを検索し、WiFiパスワードを入力します。WiFiパスワードはルーター背面のラベルに記載されています。WiFiパスワードがラベルに記載されていないモデルもあるかもしれませんが、デフォルトのパスワード**goodlife**をお試しください。

        **ヒント:** GL-AXT1800 の背面にあるラベルの QR コードには Wi-Fi 接続情報が記載されており、携帯電話の QR コード スキャン ツールを使用してすぐに接続できます。

        **注意:** 現時点では、WiFi に接続した後はインターネットにアクセスできません。インターネットにアクセスするには、次の手順で管理者パスワードを設定する必要があります。

3. Web 管理パネルにアクセスする

    ウェブブラウザ（Chrome、Edge、Safariを推奨）を開き、[http://192.168.8.1](http://192.168.8.1)サイトにアクセスします。ウェブ管理パネルの初期セットアップが表示されます。ウェブ管理パネルにアクセスできない場合は、[こちら](cannot_access_web_admin_panel.md)をご確認ください。　

   言語を選択し、**次へ** をクリックして続行します。

　　![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

　　　管理者パスワードを設定します。強力なパスワードを使用することをお勧めします。 [**送信**] をクリックして続行します。

　　**注意**: 初期化中にWi-Fiが切れる場合がありますので、必ずルーターに再接続してください。

　　![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password.png){class="glboxshadow"}

　　初期セットアップの後、ルータのウェブ管理パネルに入ります。

　　![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. インターネットに接続する

    * [イーサネットケーブル経由でインターネットに接続する](../interface_guide/internet_ethernet.md)
    * [既存の Wi-Fi 経由でインターネットに接続する](../interface_guide/internet_repeater.md)
    * [USBテザリングでインターネットに接続する](../interface_guide/internet_tethering.md)
    * [USBモデム経由でインターネットに接続する](../interface_guide/internet_cellular.md)

## Wi-Fi非搭載モデルの場合

こちらはGL-MT2500A(Brume 2)の例です。

1. 電源オン

    電源アダプターの一端をルーターに差し込み、もう一端をコンセントに差し込みます。 自動的に電源が入ります。

2. ルーターに接続する

    イーサネットケーブルまたはWi-Fi経由でルーターに接続できます。

    * ケーブル経由で接続する

        パソコンをイーサネットケーブルでルーターのLANポートに接続します。

    * 別のルーターでWi-Fi接続

    　　GL-MT2500AにはWi-Fiモジュールが搭載されていないため、別のルーターを使用してGL-MT2500Aを初期化することができます。

    　　* 方法　1, 2台目のルーターがAP(Access Point)モードに設定されている場合は、GL-MT2500AのLANポートと2台目のルーターのWANポートを接続してください。

    　　* 方法　2, 2台目のルーターがデフォルトのルーターモードで、192.168.8.1/24と競合しない別のルーターIPアドレス、例えば192.168.10.1を持っている場合、GL-MT2500AのLANポートを2台目のルーターのWANポートに接続します。

    　　パソコンまたはスマートフォンを使って、2台目のルーターのWi-Fiに接続します。

3. ウェブ管理パネルにアクセスする

    Web ブラウザを開きます (Chrome、Edge、Safari をお勧めします)。[http://192.168.8.1](http://192.168.8.1)にアクセスしてください。Web 管理パネルの初期設定に移動します。Web管理パネルにアクセスできない場合は[こちら](cannot_access_web_admin_panel.md)をご確認ください。

    言語を選択し、**次へ** をクリックして続行します。

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    管理者パスワードを設定します。強力なパスワードを使用することをお勧めします。 [**送信**] をクリックして続行します。

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    初期セットアップ後、ルーターの Web 管理パネルに入ります。

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. インターネットに接続する

    * [イーサネットケーブル経由でインターネットに接続する](../interface_guide/internet_ethernet.md)
    * [USBテザリングでインターネットに接続する](../interface_guide/internet_tethering.md)
    * [USBモデム経由でインターネットに接続する](../interface_guide/internet_cellular.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
