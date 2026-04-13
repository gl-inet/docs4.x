# 2台のGL.iNetルーターで独自のWireGuardホームサーバーを構築する方法

この記事では、自宅のルーターをWireGuard VPNサーバーとして設定し、旅行用ルーターをWireGuard VPNクライアントとしてリモート接続する方法を紹介します。これにより、どこにいても旅行用ルーターで自宅のIPアドレスを利用できます。

以下の動画を見るか、その下の手順を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>（この動画では、VPN設定の例として GL-MT5000 (Brume 3) と GL-MT3600BE (Beryl 7) を使用しています。）</small>

以下の手順では、GL-MT6000 (Flint 2) と GL-MT3000 (Beryl AX) を例に説明します。

- GL-MT6000 は自宅用ルーターとして使用し、WireGuard VPNサーバーとして設定します。無線機能が不要な場合は、セキュリティゲートウェイ GL-MT2500 やその他のモデルも選択肢になります。

- GL-MT3000 は旅行用ルーターとして使用し、自宅のVPNサーバーにリモート接続する WireGuard VPNクライアントとして設定します。

## 独自のWireGuardホームサーバーを構築する理由

1. 自宅のIPアドレスをインターネット上のアドレスとして使えるため、自宅からアクセスしているように見せられます。
2. サードパーティーのVPNサービスのような月額料金は不要です。
3. すべてのインターネットトラフィックを暗号化されたVPNトンネル経由で自宅ネットワークにルーティングし、プライバシーを保護できます。
4. 自宅内のリソースやローカルストリーミングに簡単にアクセスできます。

## 準備

### パブリックIPがあるか確認する

まず、GL-MT6000 の WAN 側にパブリックIPアドレスがあることを確認してください。そうでない場合、旅行中に旅行用ルーターからVPN接続を確立できません。

パブリックIPアドレスを確認するには、Webブラウザーを開き、アドレスバーに [what is my ip](https://whatismyipaddress.com/){target="_blank"} と入力します。

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

パブリックIPアドレスが表示されます。その値が ISP が GL-MT6000 に割り当てた WAN IP と一致していれば、パブリックIPアドレスを利用しています。

パブリックIPアドレスがない場合は、以下を参考にしてください。

1. メインルーターがある場合は、その管理画面にログインし、ISP からパブリックIPを取得しているか確認します。
2. ISP にパブリックIPアドレスの提供を依頼します。追加料金が必要な場合があります。
3. 上記の2つが利用できない場合、たとえば CGNAT 環境では、[Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md) のようなリバースプロキシ方式を利用できます。あるいは、SDWAN ソリューションの [AstroWarp](https://www.astrowarp.net/){target="_blank"} を試すこともできます。

### Port Forwarding が必要か確認する

??? "GL.iNet as Main Router"

    GL.iNetルーターが Ethernet ケーブルで ISP モデムに直接接続されている場合、その GL.iNetルーターはメインルーターです。

    **GL.iNetルーターが ISP モデムに直接接続されているか確認する方法**

    手順:

    1. GL.iNet 管理画面にログインします。

    2. 左側のサイドバーで INTERNET を選択し、トポロジーと接続の詳細を確認します。

        Ethernet で直接接続されている場合は、「Ethernet」というセクションに Protocol、IP address、Gateway などの情報が表示されます。

        以下の画像では、マークされた IP Address が、この GL.iNetルーターに対して ISP が割り当てた WAN IP です。

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        この WAN IP はパブリックIPアドレスです。つまり、この GL.iNetルーターはメインルーターとして動作しており、**Port Forwarding を設定する必要はありません**。

        この GL.iNetルーターを WireGuard Server として設定し、旅行用ルーターを WireGuard Client として接続するだけで、両者の間に VPNトンネルが構築されます。

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet as Sub-Router"

    GL.iNetルーターが NAT 配下にある場合は、メインルーター側で GL.iNetルーター向けに **Port Forwarding** を設定します。

    Topology

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    例: 自宅のメインルーターが TP-Link ルーターの場合。

    自宅ルーターの Wi-Fi または LAN に接続して Web 管理画面にログインします。ISP から取得している WAN IP アドレスを確認してください。下の画像では、パブリックIP が **42.200.00.00** であることが分かります。

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Port Forwarding を設定する前に、メインルーター側で GL.iNetルーターの IP アドレスを予約し、固定IPを割り当てることを推奨します。** そうしないと、メインルーターまたは GL.iNetルーターの再起動後に別の IP アドレスが割り当てられ、ポートフォワーディングルールが機能しなくなる場合があります。

    その後、メインルーター側で GL.iNetルーター向けの Port Forwarding を設定します。

    1. 「Advanced」に移動して「virtual Server」をクリックし、「Add」をクリックします。

    2. Internal IP (Device IP): GL.iNet Router に割り当てられている IP アドレスです。TP-Link のクライアント一覧で確認できます。

    3. External/Internal port:  両方とも "51820" を入力してください。

    4. Protocol:  "All"、"UDP"、または "TCP/UDP" を選択できます。

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **参考: [Port Forward](how_to_set_up_port_forwarding.md) の例**

## WireGuardサーバーを設定する

### DDNS を有効にする（任意）

固定パブリックIPアドレスではなく、動的パブリックIPアドレスのみを使っている場合は、DDNS 機能を有効にしてください。

GL-MT6000 の Web 管理画面にログインし、**APPLICATIONS** -> **Dynamic DNS** に移動します。**Enable DDNS** のスイッチをオンにします。

**Terms of Service & Privacy Policy** にチェックを入れ、**Apply** をクリックします。

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

続いて **WireGuard Server** -> Configuration タブに移動し、Listen Port が 51820 であることを確認して **Apply** をクリックします。

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### 設定を生成する

同じページで、Configuration タブの横にある **Profiles** タブをクリックし、**Add** をクリックします（下図の 1）。

クライアント設定が自動的に生成されます。**forward icon** をクリックします（下図の 2）。

ポップアップウィンドウで DDNS Domain を有効にする場合は、スライドしてオンにします（下図の 3）。これは任意設定であり、動的パブリックIPを使用している場合のみ有効にしてください。

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

その後、WireGuard の [mobile app](https://www.wireguard.com/install/){target="_blank"} で QR を読み取り、サーバーをテストできます。詳細は [こちら](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly) を参照してください。

また、VPNクライアント接続用にテキスト形式の設定をエクスポートすることもできます。

**Configuration File** タブをクリックして、設定表示を QR コードからテキスト形式に切り替えます。

クライアント用のテキストをコピーするか、Download ボタンをクリックして後で使えるよう保存します。

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## WireGuardクライアントを設定する

### LAN IP を変更する

このチュートリアルでは GL-MT6000 と GL-MT3000 を例に使用していますが、どちらのデフォルト LAN IP も **192.168.8.1** です。競合を避けるため、どちらか一方を別の LAN IP に変更する必要があります。

ここでは、GL-MT3000（WireGuard クライアント）の LAN IP を変更する手順を説明します。

GL-MT3000 の Web 管理画面にログインし、左側のサイドバーで **NETWORK** -> **LAN** に移動して LAN IP を変更します。たとえば、デフォルトの 192.168.8.1 を `192.168.10.1` に変更できます。

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

LAN インターフェースの詳細については [こちら](../interface_guide/lan.md) を参照してください。

### 設定を追加する

GL-MT3000 の Web 管理画面で **VPN** -> **WireGuard Client** に移動し、**Add Manually** をクリックします。

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

左側でグループを作成して名前を設定し、右側で設定ファイルを選択してアップロードするか、アップロードボックスにドラッグします。

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

ファイルの検証が完了したら、**Apply** をクリックします。

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

また、**Manually Add Configuration** をクリックして設定テキストを貼り付け、**Apply** をクリックすることもできます。

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

アップロードが成功すると、設定ファイルが WireGuard Client ページに表示されます。

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### 接続を開始する

三点アイコンをクリックし、**Start** をクリックします。

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

数分待ちます。正常に接続されると、緑色のドットが点灯します。

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

**VPN Dashboard** を開くと、クライアントが自宅のパブリックIPでサーバーに接続していることが分かります。ページ表示はファームウェアのバージョンによって多少異なる場合があります。

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

GL-MT6000（WireGuard サーバー）の Web 管理画面に戻り、**VPN** -> **WireGuard Server** に移動します（ファームウェア v4.7 以前を使用している場合は **VPN** -> **VPN Dashboard** に移動します）。クライアントが接続されていることを示す接続状態も確認できます。

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>（FW v4.8 の WireGuard Server ページ）</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>（FW v4.7 以前の VPN Dashboard ページ）</small>

## 外出前にリモートVPNトラブル対応の準備をする

旅行中に予期しない問題が発生した場合に備えて、VPN のリモートトラブルシューティング用に、両方のルーターを事前に GoodCloud アカウントへバインドしておくことをおすすめします。

停電などによりサーバーが停止することがあります。サーバーへのアクセス性を維持するためにも、GL.iNet GoodCloud にバインドしてください。

---

関連記事

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
