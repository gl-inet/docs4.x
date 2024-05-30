# 2つのGL.iNetルーターで自分のWireGuardホームサーバーを構築する方法

この記事では、ホームルーターをWireGuard VPNサーバーとして設定し、トラベルルータをWireGuard VPNクライアントとして接続する方法を紹介します。これにより、どこにいてもトラベルルータを使用して自宅のIPアドレスを使用できます。

ここでは、GL-MT6000を例として使用してホームサイトでWireGuard VPNサーバーを実行しますが、無線機能が不要な場合はMT2500などの他のモデルも使用できます。トラベルルータとしてはGL-MT3000を例として使用しますが、他のモデルも使用能です。

## なぜ自分のWireGuardホームサーバーを構築する必要があるのか

1. インターネットアドレスとして自宅のIPアドレスを使用し、自宅にいるように振る舞うことができます。
2. サードパーティのVPNサービスと比較して月額料金が不要です。
3. 暗号化されたVPNトンネルを介してすべてのインターネットトラフィックを自宅のネットワークにルーティングし、プライバシーを保護します。
4. 内部リソースとローカルのストリーミングに簡単にアクセスできます。

## トポロジー

![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

## パブリックIPアドレスを持っているか確認する

まず、GL-MT6000がWAN側にパブリックIPアドレスを持っていることを確認する必要があります。そうでないと、トラベルルータが旅行中にVPN接続を確立できません。

パブリックIPアドレスを持っているか確認するには、ウェブブラウザを開き、アドレスバーに[ip.gs](https://ip.gs){target="_blank"}と入力してください。

![myip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/myip.jpg){class="glboxshadow"}

パブリックIPアドレスが表示され、ISPからのWAN IPと一致すれば、パブリックIPアドレスが付与されています。

もしパブリックIPアドレスを持っていない場合、以下の方法を参考にしてください。

1. メインルーターがある場合、ログインしてISPからパブリックIPを取得しているか確認してください。
2. ISPにパブリックIPアドレスを提供してもらうよう依頼できるかもしれませんが、追加料金が発生する場合があります。
3. 上記の方法がどちらも機能しない場合（例: CGNATにいる場合）、[Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md)などのリバースプロキシ方法を利用できます。

??? "メインルーターとしてTP-Linkを使用する場合"

    ### GL-MT6000を上位ルーターに接続する

    自宅のルーターのWiFiまたはLANに接続し、ウェブ管理パネルにログインします。ISPから取得したIPアドレスを確認します。ここで確認できるのはパブリックIP **42.200.00.00**です。

    **例: TP-Linkルーター**

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.jpg){class="glboxshadow"}

    ### メインルーターでポートフォワーディングを設定する

    1. メインルーターのウェブコントロールページにログインします。
    2. ポートフォワーディングの機能がどこにあるかを確認します。異なるブランドでは異なる名前で呼ばれることがあります。
    3. GL-MT6000に割り当てられたIPアドレスを確認します。

    **例: TP-Linkルーター**
    
    1. 「Advanced」に移動し、「仮想サーバー」をクリックして、「追加」をクリックします。
    2. 内部IP（デバイスIP）：GL-MT6000に割り当てられたIPアドレスで、TP-Linkのクライアントリストで確認できます。
    3. 外部/内部ポート：両方とも「51820」と入力してください。
    4. プロトコル： 「All」または「UDP」または「TCP/UDP」を選択できます。

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

??? "GL.iNetをメインルーターとして使用する場合"
    ### GL-MT6000をISPモデムに直接接続する

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.jpg){class="glboxshadow"}

    IPアドレスにパブリックIPが表示され、ポートフォワーディングを行う**必要はありません**。

## GL-MT6000でWireGuardサーバーを設定する

### DDNSを有効にする（オプション）

パブリック静的IPがなく、パブリック動的IPのみを持っている場合は、DDNS機能を有効にします。

管理パネルに移動 > アプリケーション > ダイナミックDNS を選択し、スライドして有効にします。

![serverddns](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/serverddns.jpg){class="glboxshadow"}

以下のボックスにチェックを入れ、**適用する**をクリックします。

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/ddnsapply.jpg){class="glboxshadow"}

次にWireGuard VPNサーバーに移動し、リッスンポートが51820であることを確認して「適用する」をクリックします。

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgsever.jpg){class="glboxshadow"}

## 構成を生成する

**プロフィール**をクリックし、クライアントを**追加**すると、自動的にクライアント構成が生成されます。**四角いアイコン**（ポイント2）をクリックし、DDNSドメインを使用するようにスライドします。（ポイント3、動的IPのみの場合はオプション）。

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

WireGuardの[モバイルアプリ](https://www.wireguard.com/install/)を使用してQRコードをスキャンし、サーバーをテストします。詳細は[こちら](../interface_guide/wireguard_server.md/#to-check-if-wireguard-server-is-working-properly)をクリックしてください。

## クライアントインストール用のテキスト形式の構成を出力します

**構成ファイル**をクリックして構成をテキスト形式に変更します。テキストをクライアント用にコピーするか、ダウンロードして保存し、後でクライアントにドラッグします。

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## GL-MT3000でWireGuardクライアントを設定する

### LAN IPを変更する
管理パネルにログインし、サイドバーの**ネットワーク**に移動してLAN IPを変更します。

[LAN IPを変更する](../interface_guide/lan.md)

### 設定を追加する

WireGuardクライアントに移動し、**手動で追加**をクリックします。

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient1.jpg){class="glboxshadow"}

接続の名前を作成し、この前ダウンロードした設定をドラッグするか、**構成を手動で追加する**をクリックします。

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient2.jpg){class="glboxshadow"}

設定テキストを貼り付け、それからサーバーに接続できます。

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient3.jpg){class="glboxshadow"}

## GL-MT3000をGL-MT6000サーバーに接続する

作成した名前をクリックすると、読み込んだ設定が表示されるので、**スタート**をクリックします。

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgstart.jpg){class="glboxshadow"}

クライアントがホームパブリックIPでサーバーに接続されていることがわかります。

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

GL-MT6000のVPNダッシュボードに戻ると、クライアントが接続されていることも確認できます。

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon.jpg){class="glboxshadow"}

## 旅行中に問題が発生した場合にリモートでルーターを管理するためにGoodCloudを使用する

サーバーが停電やその他の理由でダウンすることがあります。サーバーのアクセシビリティを維持するために、GoodCloudにもバインドしてください。

---

関連記事

- [GoodCloud](../interface_guide/cloud.md)