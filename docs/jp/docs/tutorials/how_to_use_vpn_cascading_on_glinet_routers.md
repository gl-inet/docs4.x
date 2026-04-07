# GL.iNetルーターでVPN Cascadingを使う方法

## はじめに

VPN Cascading は、一部の文脈では「Double VPN」とも呼ばれますが、GL.iNetルーターでの動作は少し異なります。基本的な考え方は次のとおりです。

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1（ルーターをVPNサーバーとして使用）**: ルーターがVPNサーバーとして動作している場合、このサーバーに接続したクライアントは、デフォルトでルーターのISPネットワーク経由でインターネットにアクセスします。

**VPN 2（ルーターをVPNクライアントとして使用）**: ルーターはVPNクライアントとしても動作し、サードパーティのVPNサービスに接続します。

**VPN Cascading**: ルーターは VPN 1 のトンネルから VPN 2 のトンネルへトラフィックを転送します。これにより、VPN 1 経由でルーターに接続したデバイスは、ルーターのISPネットワークではなく、サードパーティのVPNサービス（VPN 2）経由でインターネットにアクセスできます。

## VPN Cascadingを有効にする方法

### ファームウェア v4.7 以前

1. まず、ルーターをVPNサーバーとして設定します。より高速に利用するには WireGuard プロトコルを推奨します。詳しくは[こちら](../interface_guide/wireguard_server.md){target="_blank"}をご覧ください。

2. ルーターから設定ファイルをエクスポートし、VPN経由でルーターに接続するクライアントデバイスへアップロードします。

3. ルーターをVPNクライアントとして設定し、サードパーティのVPNサービスに接続します。より高速に利用するには WireGuard プロトコルを推奨します。詳しくは[こちら](../interface_guide/wireguard_client.md){target="_blank"}をご覧ください。

4. 接続が完了すると、**VPN Dashboard** ページは次のように表示され、ルーターがVPNサーバーとVPNクライアントの両方として同時に設定されていることが分かります。

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    同じページの **VPN Server** セクションに移動し、**Global Options** をクリックします。

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    **VPN Cascading** を有効にして、**Apply** をクリックします。

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. これで VPN Cascading が有効になります。VPN経由でルーターに接続したデバイスは、ルーターのISPネットワークではなく、サードパーティのVPNサービス経由でインターネットにアクセスします。

### ファームウェア v4.8 以降

1. まず、ルーターをVPNサーバーとして設定します。より高速に利用するには WireGuard プロトコルを推奨します。詳しくは[こちら](../interface_guide/wireguard_server.md){target="_blank"}をご覧ください。

2. ルーターから設定ファイルをエクスポートし、VPN経由でルーターに接続するクライアントデバイスへアップロードします。

3. ルーターをVPNクライアントとして設定し、サードパーティのVPNサービスに接続します。より高速に利用するには WireGuard プロトコルを推奨します。詳しくは[こちら](../interface_guide/wireguard_client.md){target="_blank"}をご覧ください。

4. Web管理パネルで **VPN Dashboard** に移動し、現在のVPNモードに応じて以下の手順を選択してください。

    ??? "Global Mode"

        VPNモードが **Global Mode** の場合、VPNクライアントを有効にすると（下図のとおり）、VPN Cascading は自動的に有効になります。

        VPN経由でルーターに接続したデバイスは、ルーターのISPネットワークではなく、サードパーティのVPNサービス経由でインターネットにアクセスします。

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        VPNモードが **Policy Mode** の場合は、VPNトンネルルールを設定する必要があります。

        左側のグレーアウトされたボックスをクリックします。

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        このルールに適用するトラフィック送信元を選択します。VPN Cascading を有効にするには、**All Clients** を選択するか、**Specified Connection Types** を選択してから **WireGuard/OpenVPN Server** を選択してください。

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: すべてのLANデバイス、Drop-in Gateway 経由のデバイス、ゲストネットワークのデバイス、およびVPN経由でルーターに接続したデバイスが含まれます。

            すべてのデバイスのトラフィックに同じトンネルルールを適用したい場合は、**All Clients** を選択して **Apply** をクリックします。

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: 特定の方法でルーターに接続したデバイス（例: VPN経由で接続したデバイス）だけに、このトンネルルールを適用できます。

            ルーター上のVPNクライアントに、他のデバイスとは異なるルールを適用したい場合は、**WireGuard/OpenVPN Server** を選択して **Apply** をクリックします。

            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            これは **Policy Mode** におけるVPNトンネルルールの例です。

            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. これで VPN Cascading が有効になります。VPN経由でルーターに接続したデバイスは、ルーターのISPネットワークではなく、サードパーティのVPNサービス経由でインターネットにアクセスします。

6. **接続テスト**: VPN経由でルーターに接続したノートPCでブラウザを開き、[What Is My IP](https://whatismyipaddress.com/){target="_blank"} にアクセスしてパブリックIPを確認します。

    表示されたノートPCのIPアドレスがサードパーティVPNサーバーの地域（このガイドではブエノスアイレス）になっていれば、VPN Cascading が有効になっていることを示します。

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
