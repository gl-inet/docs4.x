# GL.iNet ルーターで VPN カスケードを使う方法

## はじめに

VPN カスケードは、文脈によっては「Double VPN」と呼ばれることがありますが、GL.iNet ルーターでは少し意味合いが異なります。基本的な考え方は次のとおりです。

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1（ルーターを VPN サーバーとして使用）**: ルーターが VPN サーバーとして動作している場合、このサーバーに接続したクライアントは、デフォルトではルーターの ISP ネットワーク経由でインターネットにアクセスします。

**VPN 2（ルーターを VPN クライアントとして使用）**: ルーターは VPN クライアントとしても動作し、第三者の VPN サービスに接続します。

**VPN カスケード**: ルーターは VPN 1 のトンネルから VPN 2 のトンネルへトラフィックを転送します。これにより、VPN 1 経由でルーターに接続したデバイスは、ルーターの ISP ネットワークではなく、第三者の VPN サービス（VPN 2）経由でインターネットにアクセスできるようになります。

## VPN カスケードを有効にする方法

### ファームウェア v4.7 以前

1. まず、ルーターを VPN サーバーとして設定します。より高速に利用するため、WireGuard プロトコルを推奨します。詳しくは [こちら](../interface_guide/wireguard_server.md){target="\_blank"} をご覧ください。

2. ルーターから設定ファイルをエクスポートし、VPN 経由でルーターに接続するクライアントデバイスへアップロードします。

3. ルーターを VPN クライアントとして設定し、第三者の VPN サービスに接続します。より高速に利用するため、WireGuard プロトコルを推奨します。詳しくは [こちら](../interface_guide/wireguard_client.md){target="\_blank"} をご覧ください。

4. 接続が完了すると、**VPN Dashboard** ページは以下のように表示され、ルーターが VPN サーバーと VPN クライアントの両方として設定されていることが分かります。

   ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

   同じページの **VPN Server** セクションに移動し、**Global Options** をクリックします。

   ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

   **VPN Cascading** を有効にして、**Apply** をクリックします。

   ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. これで VPN カスケードが有効になります。VPN 経由でルーターに接続したデバイスは、ルーターの ISP ネットワークではなく、第三者の VPN サービス経由でインターネットにアクセスします。

### ファームウェア v4.8 以降

1.  まず、ルーターを VPN サーバーとして設定します。より高速に利用するため、WireGuard プロトコルを推奨します。詳しくは [こちら](../interface_guide/wireguard_server.md){target="\_blank"} をご覧ください。

2.  ルーターから設定ファイルをエクスポートし、VPN 経由でルーターに接続するクライアントデバイスへアップロードします。

3.  ルーターを VPN クライアントとして設定し、第三者の VPN サービスに接続します。より高速に利用するため、WireGuard プロトコルを推奨します。詳しくは [こちら](../interface_guide/wireguard_client.md){target="\_blank"} をご覧ください。

4.  Web 管理パネルで **VPN Dashboard** に移動し、現在の VPN モードに応じて以下の手順を選択してください。

    ??? "Global Mode"

        VPN モードが **Global Mode** の場合、VPN クライアントを有効にすると（下図のとおり）、VPN カスケードは自動的に有効になります。

        VPN 経由でルーターに接続したデバイスは、ルーターの ISP ネットワークではなく、第三者の VPN サービス経由でインターネットにアクセスします。

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        VPN モードが **Policy Mode** の場合は、VPN トンネルルールを設定する必要があります。

        左側のグレーアウトされたボックスをクリックします。

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        このルールに適用するトラフィック送信元を選択します。VPN カスケードを有効にするには、**All Clients** を選択するか、**Specified Connection Types** を選択してから **WireGuard/OpenVPN Server** を選びます。

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: これには、すべての LAN デバイス、Drop-in Gateway 経由のデバイス、ゲストネットワークのデバイス、および VPN 経由でルーターに接続したデバイスが含まれます。

            すべてのデバイスのトラフィックに同じトンネルルールを適用したい場合は、**All Clients** を選択して **Apply** をクリックします。

            ![all clients](https://static.gl.inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: 特定の接続方法でルーターに接続したデバイス（例: VPN 経由で接続したデバイス）だけに、このトンネルルールを適用できます。

            ルーターに接続している他のデバイスとは異なるルールを VPN クライアントに適用したい場合は、**WireGuard/OpenVPN Server** を選択して **Apply** をクリックします。

            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            以下は、**Policy Mode** における VPN トンネルルールの例です。

            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5.  これで VPN カスケードが有効になります。VPN 経由でルーターに接続したデバイスは、ルーターの ISP ネットワークではなく、第三者の VPN サービス経由でインターネットにアクセスします。

6.  **接続テスト**: VPN 経由でルーターに接続したノート PC でブラウザを開き、[What Is My IP](https://whatismyipaddress.com/){target="\_blank"} にアクセスしてパブリック IP を確認します。

    表示された IP アドレスの所在地が第三者 VPN サーバーの所在地（この例ではブエノスアイレス）になっていれば、VPN カスケードが有効になっていることを示します。

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
