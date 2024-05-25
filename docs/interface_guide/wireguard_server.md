
# GL.iNet ルーターで WireGuard サーバーを設定

WireGuard® は、**最先端の暗号技術** を利用した非常にシンプルで高速かつ最新の VPN です。IPSec よりも [高速](https://www.wireguard.com/performance/){target="_blank"} で [シンプル](https://www.wireguard.com/quickstart/){target="_blank"}、効率的、より使いやすいことを目指しています。また、OpenVPN よりもはるかに高性能であることを意図しています。

---

## インターネットサービスプロバイダーがパブリック IP アドレスを割り当てることを確認

インターネットサービスプロバイダーがパブリック IP アドレスを割り当てるかどうか [こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) で確認してください。

**割り当てられていない場合、WireGuard サーバーに接続することはできません。**

代替方法としてリバースプロキシソリューションを使用することができます。私たちは [AstroRelay](https://www.astrorelay.com/){target="_blank"} を提案します。チュートリアルは [こちら](../tutorials/how_to_set_up_wireguard_server_via_astrorelay.md) をご覧ください。

## ネットワークトポロジー

* GL.iNet ルーターがネットワークのメインルーターである場合、次のステップに進むだけです。
* 既にメインルーターが存在する場合、GL.iNet ルーターがメインルーターの下にあるため、メインルーターでポートフォワーディングを設定する必要があります。
* 既にメインルーターが存在し、GL.iNet ルーターがいくつかのレベル下にある場合、各レベルでポートフォワーディングを設定する必要があります。

## WireGuard サーバーの設定

Web 管理パネルにアクセスし、左側のメニューから -> VPN -> WireGuard サーバー を選択します。

1. **構成を生成** をクリックします（初回のみ）。

    ![wireguard server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_generate_configuration.png){class="glboxshadow"}

2. 構成を適用

    デフォルトの構成はほとんどの場合に適しています。上位ルーターのゲートウェイと IPv4 アドレスが競合する場合、修正後に **適用** ボタンをクリックします。例えば、**10.1.0.1/24** に変更することができます。**/24** を忘れずに追加してください。そうしないとクライアントが接続できません。

    ![wireguard server apply configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_apply_configuration.png){class="glboxshadow"}

    例えば、Xfinity ルーターを使用している場合、ルーターの IP は WireGuard サーバーの IP と同じになるため、上記の変更を行う必要があります。
    
    ![xfinitygateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    **キーを手動で設定** する場合。

    ![wireguard server set key manually](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_set_key_manually.png){class="glboxshadow"}

3. プロファイルを追加

    **プロファイル**タブに切り替え、**追加**ボタンをクリックしてデバイスのプロファイルを生成します。

    ![wireguard server profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profiles.png){class="glboxshadow"}

    説明的な名前を入力します。

    ![wireguard server profile setting](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profile_setting.png){class="glboxshadow"}
    
    **詳細設定**は高度な設定用です。

    ![wireguard server profile advanced setting](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profile_setting_more.png){class="glboxshadow"}

    **適用**をクリックして続行します。これによりプロファイルが生成されます。
    
    ![download wireguard client configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_wireguard_client_configuration.png){class="glboxshadow"}

    ネットワークのパブリックIPが時々変わる場合は、[DDNS](ddns.md)を有効にし、設定でDDNSドメインを使用してください。

    **ダウンロード**をクリックしてプロファイルを保存します。

4. WireGuardサーバーの起動

    右上隅の**スタート**ボタンをクリックしてWireGuardサーバーを起動します。VPNダッシュボードページに移動して、状態と他の設定を確認します。

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wireguard_server.png){class="glboxshadow"}

### WireGuardサーバーが正常に動作しているか確認するには

多くの人はサーバーが起動しているのを見て、接続されていると誤解します。サーバーは、間違ったポートやアドレスを転送しても起動することがあります。

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgconnected.jpg){class="glboxshadow"}

WireGuardサーバーが正常に動作しているか確認するには、別のネットワークに接続された別のデバイスを使用し、この前にエクスポートしたWireGuard構成を使用して接続し、正しく接続されているか、IPアドレスがWireGuardサーバーのIPアドレスであるかを確認します。

最も簡単な方法は、[WireGuard公式クライアントアプリ](https://www.wireguard.com/install){target="_blank"}をインストールした携帯電話を使用し、Wi-Fi接続をオフにして、3G/4G/5G経由でのみインターネットに接続することです。次にWireGuardアプリを開き、QRコードからWireGuard構成をインポートします。接続を有効にし、携帯電話がインターネットアクセスを持ち、そのIPアドレスがWireGuardサーバーのIPアドレスであるかを確認します。

失敗の原因はいくつかあります：

* インターネットサービスプロバイダーがパブリックIPアドレスを割り当てていない、 [こちら](#make-sure-internet-service-provider-assigns-you-a-public-ip-address)を確認してください。
* ポートフォワーディングの設定が必要な場合があります、 [こちら](#network-topology)を確認してください。
* WireGuardサーバー用に使用しているポートがインターネットサービスプロバイダーによってブロックされている、別のポートに変更するか、インターネットサービスプロバイダーに連絡してください。
* 一部の国/地域ではVPN接続がブロックされることがあります。

## WireGuardクライアントアプリ

別の GL.iNet ルーターを WireGuard クライアントとして使用したり、さまざまな OS を備えた他のデバイスで公式アプリを使用したりすることができます。

- WireGuard公式ウェブサイトを参照してください: [https://www.wireguard.com/install](https://www.wireguard.com/install){target="_blank"}

---

WireGuard®はJason A.Donenfeldの登録商標です。

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}にアクセスしてください。