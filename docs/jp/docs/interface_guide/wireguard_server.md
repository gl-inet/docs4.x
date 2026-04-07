# GL.iNet ルーターで WireGuard サーバーを設定する

WireGuard® は、最先端の暗号技術を利用した、非常にシンプルで高速かつモダンな VPN です。IPSec よりも高速・簡潔・軽量で使いやすいことを目指しており、OpenVPN よりも大幅に高いパフォーマンスを期待できます。

GL.iNet ルーターで WireGuard サーバーを設定するには、以下の動画を見るか、下記の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## パブリック IP アドレスがあることを確認する {#make-sure-you-have-a-public-ip-address}

インターネットサービスプロバイダーからパブリック IP アドレスが割り当てられているかどうかは、[こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) で確認してください。

**割り当てられていない場合、このルーターを WireGuard Server として設定することはできません。**

代替手段:

1. メインルーターがある場合は、そのルーターにログインして、ISP からパブリック IP を取得しているか確認します。
2. ISP にパブリック IP アドレスの提供を依頼します。追加料金が発生する場合があります。
3. 上記 2 つの方法が使えない場合（ネットワークが CGNAT 配下にある場合など）は、SD-WAN ソリューション [AstroWarp](https://www.astrowarp.net/){target="_blank"} の利用をご検討ください。

## ポートフォワーディングが必要か確認する {#confirm-if-port-forwarding-is-required}

**Network Topology**

??? "GL.iNet がメインルーターの場合"

    * GL.iNet ルーターがネットワークのメインルーターであれば、ポートフォワーディングは不要です。[次の手順](#set-up-wireguard-server) に進んでください。

??? "GL.iNet がサブルーターの場合"

    * すでにメインルーターがあり、GL.iNet ルーターをサブルーターとして使用している場合は、メインルーター側で [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) を設定する必要があります。

    * すでにメインルーターがあり、GL.iNet ルーターがさらに下位階層にある場合は、途中の各ルーターで [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) を設定してください。

## WireGuard サーバーを設定する {#set-up-wireguard-server}

Web 管理パネルにログインし、**VPN** -> **WireGuard Server** を開きます。

1. **Generate Configuration** をクリックします（VPN サーバー初回設定時のみ）。

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. 設定を確認します。

    多くの環境では、以下のようにデフォルト設定のままで利用できます。上位ルーターのゲートウェイと競合していなければ、IPv4 アドレスを変更する必要はありません。

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    （GL.iNet では IPv6 はデフォルトで無効です。IPv6 アドレスを使いたい場合は、ルーターで IPv6 を有効にしてください。）

    もし IPv4 アドレスが上位ルーターのゲートウェイと競合している場合は、**10.1.0.1/24** など別のアドレスに変更し、**Apply** をクリックします。接続問題を避けるため、`/24` の CIDR 表記を必ず含めてください。

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    たとえば、GL.iNet ルーターの上位に Xfinity ルーターがある場合、Xfinity ルーターの IP が 10.0.0.1 となり、GL.iNet ルーターを WireGuard サーバーとして設定したときの WireGuard Server のトンネル IP と競合することがあります。その場合は上記の変更が必要です。

    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. プロファイルを追加します。

    **Profiles** タブに切り替え、**Add** ボタンをクリックしてデバイス用のプロファイルを生成します。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    分かりやすい名前を設定し、**Apply** をクリックして続行します。

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    詳細設定が必要な場合は **Set More** をクリックします。その後 **Apply** をクリックして続行します。

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "必要に応じてルートルールを追加する"

        通常、ルートルールを追加する必要はありません。

        サーバー側から WireGuard クライアントの LAN 内デバイスへアクセスしたい場合は、**WireGuard Server** ページの **Route Rules** タブでルートルールを設定してください。詳しくは [こちら](../tutorials/wireguard_server_access_to_client_lan_side.md) を参照してください。

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        それ以外の場合は、手順 4 に進んでクライアント設定をダウンロードしてください。

4. 設定をダウンロードします。

    プロファイルを追加して適用すると、設定ファイルが QR コード、プレーンテキスト、`.conf` ファイルの 3 形式で生成されます。使いやすい方法で設定ファイルを取得してください。

    - **QR code**: WireGuard App をインストールしたエンドデバイス（スマートフォン、タブレット、ノート PC など）に適しています。特定のデバイスを WireGuard クライアントとして設定したい場合は、WireGuard App を開いて QR コードをスキャンするだけで、設定が自動的にインポートされます。

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: プレーンテキスト形式では設定内容を確認でき、そのままコピー＆ペーストして WireGuard App や GL.iNet ルーターへ手動設定できます。

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: **Download** をクリックすると、`.conf` ファイルをローカルデバイスへ保存できます。WireGuard App や GL.iNet ルーターへ直接アップロードできるため便利です。

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    必要に応じて、サーバーアドレスとしてパブリック IP、DDNS ドメイン、現在の WAN IP のいずれかを指定できます。この機能はファームウェア v4.8 以降で利用可能です。変更すると、設定ファイル内のサーバーアドレスも同時に更新されます。

    たとえば、ネットワークのパブリック IP が頻繁に変わる場合は、[DDNS](ddns.md) を有効にし、DDNS ドメインをサーバーアドレスとして使うことを推奨します。

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5. WireGuard サーバーを起動します。

    右上の **Start** ボタンをクリックして WireGuard サーバーを起動します。

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    接続状態は同じページに表示されます。

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## WireGuard サーバーが正常に動作しているか確認する

### サーバー状態を確認する

ファームウェア v4.8 以降では、**WireGuard Server** ページでサーバー接続状態を確認できます。

アップロード/ダウンロードのトラフィック統計とオンラインの接続デバイス数が表示されていれば、WireGuard サーバーは動作しており、WireGuard クライアントが接続されています。

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

トラフィックが 0、クライアント数も 0 と表示されている場合は、WireGuard クライアントが接続していません。

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

ファームウェア v4.7 以前では、**VPN Dashboard** ページでサーバー接続状態を確認してください。

### クライアント側の IP を確認する

サーバーへの接続が成功しているか確認するには、先ほどエクスポートした WireGuard 設定を別ネットワーク上のデバイス（サーバーと同じローカルネットワークではないデバイス）にインポートします。その後 Web ブラウザで自身の IP アドレスと位置情報を確認し、インターネットサービスプロバイダーの IP ではなく VPN サーバーの IP と位置情報が表示されれば、VPN 接続は成功です。

最も簡単なのは、公式の [WireGuard App](https://www.wireguard.com/install){target="_blank"} をインストールしたスマートフォンを使う方法です。まずスマートフォンの Wi-Fi を無効にし、モバイルデータ通信（4G/5G）のみでインターネットに接続します。次に WireGuard App を開いて設定ファイルをインポートし、接続を開始します。スマートフォンがインターネットへ接続できるか、また IP アドレスが WireGuard Server の IP と一致するか確認してください。

接続に失敗する主な原因は次のとおりです。

* インターネットサービスプロバイダーからパブリック IP アドレスが割り当てられていない。[こちら](#make-sure-you-have-a-public-ip-address) を確認してください。
* ポートフォワーディングの設定が必要な場合がある。[こちら](#confirm-if-port-forwarding-is-required) を確認してください。
* WireGuard Server で使用しているポートがインターネットサービスプロバイダーによってブロックされている。別のポートに変更するか、ISP に問い合わせてください。
* 一部の国や地域では VPN 接続がブロックされる場合があります。

## WireGuard App のインストール

[WireGuard 公式サイト](https://www.wireguard.com/install){target="_blank"} から WireGuard App をダウンロードしてください。

---

WireGuard® は Jason A.Donenfeld の登録商標です。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
