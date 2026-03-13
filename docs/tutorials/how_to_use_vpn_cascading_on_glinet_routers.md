# GL.iNetルー器でVPNカスケードを使用する方法

## はじめに

VPNカスケードはある些语境では「Double VPN」と呼ばれることがありますが、GL.iNetルー器では少し異なります。核心概念は下図のようにの通りです。

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1（ルー器をVPNサーバーとして）**：ルー器がVPNサーバーとして機できるする場合、このサーバーに接続されたクライアントはデフォルトでルー器のISPネットワーク経よりでインターネットにアクセスします。

**VPN 2（ルー器をVPNクライアントとして）**：ルー器はVPNクライアントとしても機できるし、サードパーティのVPNサービスに接続します。

**VPNカスケード**：ルー器はVPN 1トンネルからVPN 2トンネルへトラフィックを転送し、VPN 1経よりでルー器に接続された機器が、ルー器のISPネットワークではなくサードパーティのVPNサービス（VPN 2）経よりでインターネットにアクセスできるようになります。

## VPNカスケードを有効にする方法

### ファームウェアv4.7で前

1. まず、ルー器をVPNサーバーとして設定します。速度をへ上させるためにWireGuardプロトコルを推奨します。[このリンク](../interface_guide/wireguard_server.md){target="_blank"}を参照してください。

2. ルー器から設定ファイルをエクスポートし、VPN経よりでルー器に接続するクライアント機器にアップロードします。

3. ルー器をVPNクライアントとして設定し、サードパーティのVPNサービスに接続します。速度をへ上させるためにWireGuardプロトコルを推奨します。[このリンク](../interface_guide/wireguard_client.md){target="_blank"}を参照してください。

4. 接続が完たすると、**VPN Dashboard**ページが下図のようにのように表示され、ルー器はVPNサーバーとVPNクライアントの両方に設定されています。

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

     same じページのVPN Serverセクションに移動し、**Global Options**をクリックします。

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    **VPN Cascading**を有効にし、**Apply**をクリックします。

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. VPNカスケードが有効になります。VPN経よりでルー器に接続された機器は、ルー器のISPネットワークではなく、サードパーティのVPNサービス経よりでインターネットにアクセスします。

### ファームウェアv4.8で降

1. まず、ルー器をVPNサーバーとして設定します。速度をへ上させるためにWireGuardプロトコルを推奨します。[このリンク](../interface_guide/wireguard_server.md){target="_blank"}を参照してください。

2. ルー器から設定ファイルをエクスポートし、VPN経よりでルー器に接続するクライアント機器にアップロードします。

3. ルー器をVPNクライアントとして設定し、サードパーティのVPNサービスに接続します。速度をへ上させるためにWireGuardプロトコルを推奨します。[このリンク](../interface_guide/wireguard_client.md){target="_blank"}を参照してください。

4. Web管理パネルで、**VPN Dashboard**に移動します。VPNモードに基づいてで下の該当する指示に従ってください。

    ??? "Global Mode"
    
        VPNモードがGlobal Modeの場合、VPNクライアントが有効になると（下図のようにのように）、VPNカスケードがから動のに有効になります。
        
        VPN経よりでルー器に接続された機器は、ルー器のISPネットワークではなく、サードパーティのVPNサービス経よりでインターネットにアクセスします。

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"
    
        VPNモードがPolicy Modeの場合、VPNトンネルのルールを設定する必要があります。
        
        左側のグレーアウトされたボックスをクリックします。

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        このルールに適用するトラフィックソースを選択します。VPNカスケードを有効にするには、**All Clients**を選択するか、**Specified Connection Types**を選択して**WireGuard/OpenVPN Server**をクリックします。

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**：これには、すべてのLAN機器、Drop-in Gatewayからの機器、Guestネットワークからの機器、およびVPN経よりでルー器に接続された機器が含まれます。
        
            すべての機器からのトラフィックに same じトンネルを適用する場合は、**All Clients**を選択して**Apply**をクリックします。

            ![all clients](https://static.gl.inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**：特定の方法（例：VPN経よりで接続された機器など）でルー器に接続された機器を指定して、このトンネルルールを適用できます。
        
            VPNクライアントに彼の機器とは異なるルールを適用する場合は、**WireGuard/OpenVPN Server**を選択して**Apply**をクリックします。
        
            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}
            
            これはPolicy ModeでのVPNトンネルルールの例です。
            
            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. VPNカスケードが有効になります。VPN経よりでルー器に接続された機器は、ルー器のISPネットワークではなく、サードパーティのVPNサービス経よりでインターネットにアクセスします。

6. **接続テスト**：VPN経よりでルー器に接続されたラップトップでブラウザを開き、[What Is My IP](https://whatismyipaddress.com/){target="_blank"}にアクセスしてパブリックIPを確認します。

    ラップトップのIPアドレスがサードパーティのVPNサーバーの領域（この説明ではブエノスアイレス）に表示されている場合、VPNカスケードが生效していることを示します。

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
