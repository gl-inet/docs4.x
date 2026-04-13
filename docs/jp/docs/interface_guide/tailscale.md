# Tailscale

Tailscale は、所有しているデバイスやアプリケーションに世界中のどこからでも、安全かつ簡単にアクセスできるようにするVPNサービスです。詳細については、[Tailscale公式サイト](https://tailscale.com/) を参照してください。

ファームウェア v4.2 以降で利用できる GL.iNetルーターのTailscale機能を使うと、ルーターをTailscaleの仮想ネットワークに参加させることができます。接続後は、ルーター本体だけでなく、WAN側およびLAN側のリソースにもリモートアクセスできます。

**注**:

1. Tailscale は WireGuard をベースとしているため、ルーティング競合を引き起こす可能性があります。OpenVPN Client、WireGuard Client、GoodCloud Site to Site、ZeroTier、AstroWarp と同時に使用することは推奨されません。

2. この機能は現在ベータ版であり、不具合が含まれる可能性があります。

3. GL.iNetルーターは **まだ exit node として利用できません**。

## 対応モデル

??? "対応モデル"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "非対応モデル"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Tailscaleネットワークを設定する

以下は GL-MT2500 を例にした手順です。

1. デバイスをバインドします。

    まずTailscaleアカウントを登録し、テスト用としてスマートフォンやノートPCなどのデバイスを1台または2台、Tailscaleアカウントにバインドしてください。

    バインド後、Tailscale Admin console でデバイスとその状態を確認できます。

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. GL.iNetルーターでTailscaleを有効にします。

    ルーターのWeb管理画面にログインし、**APPLICATIONS** -> **Tailscale** に移動します。

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Tailscale を有効にして、**Apply** をクリックします。

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

3. しばらくすると、画面に **Device Bind Link** が表示されます。Device Bind Link をクリックします。

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    ポップアップウィンドウにTailscaleのリンクが表示されるので、そのリンクをクリックしてTailscaleのWebサイトへ移動し、ログインします。

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    ログイン後、接続したいデバイスの確認画面が表示されます。**Connect** をクリックします。

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    接続に成功すると、自動的にTailscale Admin consoleへ移動します。GL-MT2500 のIPアドレスが `100.88.54.21` であることが確認でき、このIPを使ってルーターへアクセスできます。

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. 接続を確認します。

    同じTailscaleネットワークに接続されているデバイスでは、次の3つの方法で接続確認ができます。

    * ping コマンドを使用する

        ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

    * ルーターへSSH接続する

        ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

    * Web管理画面にアクセスする

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## WAN からのリモートアクセスを許可する

このオプションを有効にすると、デバイスのWAN側にあるリソースへTailscale仮想ネットワーク経由でアクセスできます。

たとえば、下図の構成でこの機能を有効にすると、`leo-phone` から `GL-AXT1800` のIPアドレス（`192.168.29.1`）へアクセスできます。これは、GL-AXT1800 が `GL-MT2500` の上位デバイスであり、後者が leo-phone と同じTailscaleネットワークに接続されているためです。

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

操作手順は次のとおりです。

1. ルーターのWeb管理画面にログインし、**APPLICATIONS** -> **Tailscale** に移動します。

    **Allow Remote Access WAN** を有効にして、**Apply** をクリックします。

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Tailscale Admin console を開くと、GL-MT2500 にサブネットがあることを示すアラートが表示されます。

    GL-MT2500 の右側にある三点アイコンをクリックし、**Edit route settings** を選択します。

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. サブネットルートを有効にします。

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. これで、他のデバイスから `GL-AXT1800` のIPアドレス（`192.168.29.1`）へアクセスできます。実際には、`192.168.29.0/24` サブネット内のすべてのデバイスへアクセスできます。

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## LAN へのリモートアクセスを許可する

このオプションを有効にすると、デバイスのLAN側にあるリソースへTailscale仮想ネットワーク経由でアクセスできます。

たとえば、下図の構成でこの機能を有効にすると、`leo-phone` から `Ubuntu` のIPアドレス（`192.168.8.110`）を使ってSSH接続できます。これは、`Ubuntu` が `GL-MT2500` の下位デバイスであり、後者が leo-phone と同じTailscaleネットワークに接続されているためです。

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

操作手順は次のとおりです。

1. ルーターのWeb管理画面にログインし、**APPLICATIONS** -> **Tailscale** に移動します。

    **Allow Remote Access LAN** を有効にして、**Apply** をクリックします。

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Tailscale Admin console を開くと、GL-MT2500 にサブネットがあることを示すアラートが表示されます。

    GL-MT2500 の右側にある三点アイコンをクリックし、**Edit route settings** を選択します。

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. サブネットルートを有効にします。

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. これで、他のデバイスから `Ubuntu` のIPアドレス（`192.168.8.110`）へ ping やSSH接続ができます。実際には、`192.168.8.0/24` サブネット内のすべてのデバイスへアクセスできます。

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## カスタム Exit Node

デフォルトでは、Tailscale はオーバーレイネットワークとして動作し、Tailscale を実行しているデバイス間の通信のみをルーティングします。Google のようなWebサイト閲覧時のような、通常のパブリックインターネットトラフィックは処理しません。

ただし、Tailscale にパブリックインターネットトラフィックもルーティングさせたい場面があります。たとえば、外出先や海外旅行中に、自国からしか利用できないオンラインサービス（銀行など）へアクセスしたい場合、自宅にあるパブリックIPを持つデスクトップPCを Exit node として設定し、同じ Tailnet 上にある他のデバイス（下図の GL-AXT1800 や GL-MT3000 など）のトラフィックをそこへ送るようにできます。これにより、すべてのパブリックインターネットトラフィックを Exit Node 経由で転送できます。

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

すべてのトラフィックを Exit Node 経由にすると、実質的にデフォルトルート（0.0.0.0/0, ::/0）を利用することになり、通常のVPN接続と似た動作になります。

要するに、Exit node は Tailnet 上のデバイスからの外向きインターネットトラフィックをルーティングする役割を持ち、事実上VPN Serverのように動作します。Exit node に接続すると、Tailscale以外のインターネットトラフィックはその設置場所から送信されているように見えるため、地域制限のあるコンテンツへのアクセスやオンラインプライバシーの強化に役立ちます。このトラフィック転送を担当するデバイスが "exit node" です。

**注**: ルーターのDNSサーバーがローカルネットワーク内でのみ到達可能なプライベートIPアドレスを使用している場合、Exit Node 使用時にインターネット接続を失うことがあります。この場合はルーターにログインし、**NETWORK** -> **DNS** に移動して、8.8.8.8 などのパブリックDNSサーバーを手動で設定してください。

---

以下の例では、GL.iNetルーター **GL-MT2500** と **Leo-Desktop** が同じ Tailnet 上にあります。Leo-Desktop を Exit Node として設定する手順は以下のとおりです。

1. Tailscale Admin console で GL-MT2500 のサブネットルートを有効にします。

    Tailscale Admin console で、GL-MT2500 の右側にある三点アイコンをクリックし、**Edit route settings** を選択します。

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    ポップアップウィンドウでサブネットルートを有効にします。

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Exit node として使いたいデバイス（この例では Leo-Desktop）で **Run exit node** を選択します。以下は Windows OS での例です。

    ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    次に **Yes** をクリックします。

    ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. Tailscale Admin console で、Leo-Desktop を Exit node として設定します。

    ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. GL-MT2500 の Web管理画面 にログインし、**APPLICATIONS** -> **Tailscale** に移動して **Custom Exit Nodes** を有効にします。更新ボタンをクリックし、ドロップダウンメニューから Leo-Desktop のIPアドレスを選択して、**Apply** をクリックします。

    ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    その後、ルーターに接続されたデバイスは Exit Node 経由でインターネットへアクセスするようになり、すべてのインターネットトラフィックが Exit Node の場所から送信されているように見えます。

参考情報: [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} までご連絡ください。
