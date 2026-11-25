# 2台のGL.iNetルーターで独自のWireGuardホームサーバーを構築する方法 {#build-your-own-wireguard-home-server-with-two-glinet-routers}

この記事では、自宅のルーターをWireGuard VPNサーバーとして設定し、トラベルルーターをWireGuard VPNクライアントとしてリモート接続する方法を紹介します。これにより、どこにいてもトラベルルーターで自宅のIPアドレスを利用できます。

以下の動画を見るか、その下の手順を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>（この動画では、VPN設定の例として GL-MT5000 (Brume 3) と GL-MT3600BE (Beryl 7) を使用しています。）</small>

以下の手順では、GL-MT6000 (Flint 2) と GL-MT3000 (Beryl AX) を例に説明します。

- GL-MT6000 は自宅用ルーターとして使用し、WireGuard VPNサーバーとして設定します。無線機能が不要な場合は、セキュリティゲートウェイ GL-MT2500 やその他のモデルも選択肢になります。

- GL-MT3000 はトラベルルーターとして使用し、自宅のVPNサーバーにリモート接続する WireGuard VPNクライアントとして設定します。

## 独自のWireGuardホームサーバーを構築する理由 {#why-build-your-own-wireguard-home-server}

1. 自宅回線のパブリックIPアドレスを使用することで、インターネット上では自宅から通信しているように見えます。
2. サードパーティーのVPNサービスにかかる月額料金を節約できます。
3. すべてのインターネット通信を暗号化トンネル経由で自宅のネットワークに送ることで、プライバシーを保護できます。
4. 外出先から自宅のデバイスや地域のストリーミングサービスにアクセスできます。

## 準備 {#preparations}

### パブリックIPがあるか確認する {#check-if-you-have-a-public-ip}

まず、GL-MT6000 の WAN 側にパブリックIPアドレスがあることを確認してください。そうでない場合、旅行中にトラベルルーターからVPN接続を確立できません。

パブリックIPアドレスを確認するには、Webブラウザーを開き、アドレスバーに [what is my ip](https://whatismyipaddress.com/){target="_blank"} と入力します。

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

パブリックIPアドレスが表示されます。その値が ISP が GL-MT6000 に割り当てた WAN IP と一致していれば、パブリックIPアドレスを利用しています。

パブリックIPアドレスがない場合は、以下を参考にしてください。

1. メインルーターがある場合は、その管理パネルにログインし、ISP からパブリックIPを取得しているか確認します。
2. ISP にパブリックIPアドレスの提供を依頼します。追加料金が必要な場合があります。
3. 上記 2 つの方法が使えない場合（ネットワークが CGNAT 配下にある場合など）は、SD-WAN ソリューション [AstroWarp](../interface_guide/astrowarp.md){target="_blank"} の利用をご検討ください。

### ポートフォワーディングが必要か確認する {#check-if-port-forwarding-is-required}

??? "GL.iNet ルーターがメインルーターの場合"

    GL.iNetルーターが Ethernet ケーブルで ISP モデムに直接接続されている場合、その GL.iNetルーターはメインルーターです。

    **GL.iNetルーターが ISP モデムに直接接続されているか確認する方法**

    GL.iNetのWeb管理パネルにログインします。左側のサイドバーで **INTERNET** を選択し、ネットワーク構成と接続の詳細を確認します。

    Ethernet で直接接続されている場合は、「Ethernet」というセクションに Protocol、IP address、Gateway などの情報が表示されます。

    以下の画像では、マークされた IP Address が、この GL.iNetルーターに対して ISP が割り当てた WAN IP です。

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    この WAN IP はパブリックIPアドレスです。つまり、この GL.iNetルーターはメインルーターとして動作しており、**Port Forwarding を設定する必要はありません**。

    この GL.iNetルーターを WireGuard Server として設定し、トラベルルーターを WireGuard Client として接続するだけで、両者の間に VPNトンネルが構築されます。

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet ルーターがサブルーターの場合"

    GL.iNetルーターが NAT 配下にある場合は、メインルーター側で GL.iNetルーター向けに **Port Forwarding** を設定します。

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    例: 自宅のメインルーターが TP-Link ルーターの場合。

    自宅ルーターの Wi-Fi または LAN に接続して Web 管理パネルにログインします。ISP から取得している WAN IP アドレスを確認してください。下の画像では、パブリックIP が **42.200.00.00** であることが分かります。

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Port Forwarding を設定する前に、メインルーター側で GL.iNetルーターの IP アドレスを予約し、固定IPを割り当てることを推奨します。** そうしないと、メインルーターまたは GL.iNetルーターの再起動後に別の IP アドレスが割り当てられ、ポートフォワーディングルールが機能しなくなる場合があります。

    その後、メインルーター側で GL.iNetルーター向けの Port Forwarding を設定します。

    1. 「Advanced」に移動して「virtual Server」をクリックし、「Add」をクリックします。

    2. Internal IP (Device IP): GL.iNet Router に割り当てられている IP アドレスです。TP-Link のクライアント一覧で確認できます。

    3. External/Internal port:  両方とも "51820" を入力してください。

    4. Protocol:  "All"、"UDP"、または "TCP/UDP" を選択できます。

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **その他の[ポートフォワーディング](how_to_set_up_port_forwarding.md)の例**

## WireGuardサーバーを設定する {#set-up-wireguard-server}

1. Web管理パネルにログインし、**VPN** -> **WireGuard Server** に移動します。VPNサーバーを初めて設定するときは、**Generate Configuration** をクリックします。

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. 設定を確認します。

    通常は、以下のデフォルト設定のまま使用できます。

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address** は、WireGuardサーバーのトンネルIPアドレスです。上位ルーターのゲートウェイと競合しない場合は、変更する必要はありません。

        競合する場合は、**10.1.0.1/24** など別のアドレスに変更し、**Apply** をクリックします。接続の問題を防ぐため、CIDR表記の「/24」も入力してください。

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        たとえば、上位にあるXfinityルーターのIPアドレスが10.0.0.1の場合、一部のGL.iNetルーターをWireGuardサーバーとして設定すると、トンネルIPアドレスが競合することがあります。トンネルIPアドレスは、競合する場合にのみ変更してください。

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**：GL.iNetルーターでは、IPv6はデフォルトで無効です。IPv6アドレスを使用する場合は、ルーターで [IPv6](../interface_guide/ipv6.md) を有効にします。

    - **Listen Port**：WireGuardサーバーは、デフォルトでUDPポート `51820` で待ち受けます。このポートを変更する場合、ポートフォワーディングを使用していれば、上位ルーターのルールを変更してサーバーの新しい待受ポートに転送します。各クライアントプロファイルの `Endpoint` には、転送元となる外部ポートを指定します。サーバーに直接接続できる場合は、サーバーの待受ポートを指定します。

    - **Enable Obfuscation**：このオプションを有効にすると、VPNサーバーはAmneziaWGプロトコルでVPNトラフィックを難読化します。通常はデフォルト設定を使用し、各パラメーターの意味を理解している場合にのみ変更してください。

        - [GL.iNetルーターのAmneziaWG難読化](../faq/amneziawg_obfuscation.md)
        - [GL.iNetルーターでVPN難読化を設定する方法](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. プロファイルを追加します。

    **Profiles** タブに切り替え、**Add** をクリックしてデバイスのプロファイルを作成します。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    分かりやすい名前を入力し、**Apply** をクリックします。

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    詳細設定が必要な場合は、**Set More** をクリックします。設定後、**Apply** をクリックします。

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "必要に応じてルーティングルールを追加する"

        通常は、ルーティングルールを追加する必要はありません。

        サーバーからWireGuardクライアントのLAN内にあるデバイスにアクセスするには、**WireGuard Server** ページの **Route Rules** タブでルーティングルールを設定します。詳しくは、[クライアント側のLANにアクセスする手順](../tutorials/wireguard_server_access_to_client_lan_side.md)を参照してください。

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        ルーティングルールを設定しない場合は、手順4に進んでクライアント設定をダウンロードしてください。

4. 設定をダウンロードします。

    プロファイルを追加して **Apply** をクリックすると、設定をQRコード、プレーンテキスト、またはダウンロード可能な `.conf` ファイルとして取得できます。

    - **QRコード**：WireGuardアプリでQRコードを読み取って、標準のWireGuardプロファイルをインポートします。難読化を有効にした場合は、AmneziaWGアプリまたはAmneziaWG難読化に対応したクライアントを使用してください。

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **プレーンテキスト**：設定内容を確認したり、コピーしてWireGuardアプリやGL.iNetルーターなどで手動設定に使用したりできます。

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.confファイル**：**Download** をクリックしてファイルをデバイスに保存します。このファイルはWireGuardアプリやGL.iNetルーターに直接アップロードできます。

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    ファームウェアv4.8以降では、必要に応じて、サーバーアドレスとしてパブリックIPアドレス、DDNSドメイン、または現在のWAN IPアドレスを選択できます。選択を変更すると、設定ファイル内のサーバーアドレスも更新されます。

    たとえば、ネットワークのパブリックIPアドレスが頻繁に変わる場合は、[DDNS](../interface_guide/ddns.md) を有効にし、DDNSドメインをサーバーアドレスに指定します。

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. 右上の **Start** をクリックしてWireGuardサーバーを起動します。同じページに接続状態が表示されます。

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## WireGuardクライアントを設定する {#set-up-wireguard-client}

### LAN IP を変更する {#change-the-lan-ip}

このチュートリアルでは GL-MT6000 と GL-MT3000 を例に使用していますが、どちらのデフォルト LAN IP も **192.168.8.1** です。競合を避けるため、どちらか一方を別の LAN IP に変更する必要があります。

ここでは、WireGuardクライアントとして使用するGL-MT3000のLAN IPアドレスを変更します。

GL-MT3000のWeb管理パネルにログインし、**NETWORK** -> **LAN** に移動します。たとえば、LAN IPアドレスをデフォルトの192.168.8.1から `192.168.20.1` に変更できます。

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### 設定を追加する {#add-the-configuration}

GL-MT3000 の Web 管理パネルで **VPN** -> **WireGuard Client** に移動し、**Add Manually** をクリックします。

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

### 接続を開始する {#start-the-connection}

三点アイコンをクリックし、**Start** をクリックします。

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

数分待ちます。正常に接続されると、緑色のドットが点灯します。

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

**VPN Dashboard** を開くと、クライアントが自宅のパブリックIPでサーバーに接続していることが分かります。ページ表示はファームウェアのバージョンによって多少異なる場合があります。

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

GL-MT6000（WireGuard サーバー）の Web 管理パネルに戻り、**VPN** -> **WireGuard Server** に移動します（ファームウェア v4.7 以前を使用している場合は **VPN** -> **VPN Dashboard** に移動します）。クライアントが接続されていることを示す接続状態も確認できます。

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>（FW v4.8 の WireGuard Server ページ）</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>（FW v4.7 以前の VPN Dashboard ページ）</small>

## 外出前にリモートVPNトラブル対応の準備をする {#prep-for-remote-vpn-fixes-ahead}

旅行前に、両方のルーターを GoodCloud アカウントにバインドしてください。設定やその他のネットワークの問題で VPN 接続が失敗した場合に、リモートでトラブルシューティングできます。リモートアクセスは、ルーターの電源が入っていて、インターネットに接続されている場合にのみ機能します。

---

関連記事

- [GL.iNetルーターでWireGuardサーバーを設定する](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
