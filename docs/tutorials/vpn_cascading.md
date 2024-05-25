# VPNカスケーディング

## VPNカスケーディングの仕組み

VPNカスケーディングは、さまざまなシナリオでダブルVPNとも呼ばれます。ただし、GL.iNetのVPNカスケーディングは少し異なる場合があります。以下の図を参考にしてください。

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/vpn_cascading.png){class="glboxshadow"}

**VPN 1**: ルーターがVPNサーバーとして使用されます。このサーバーに接続されたクライアントは、デフォルトでルーターのISPネットワークを使用してインターネットに接続します。

**VPN 2**: ルーターがサードパーティのVPNサービスへのVPNクライアントとして使用されます。

**VPNカスケーディング**: VPN1トンネルのデータをVPN2トンネルに転送することができます。これにより、VPN1に接続されたラップトップ、デスクトップ、スマートフォン（エンドデバイス）は、これらのエンドデバイスに他の設定を行うことなく、サードパーティのVPNサービスに接続されます。

## VPNカスケーディングを有効にする方法

以下の図は、ルーターでOpenVPNとWireguardサーバーが有効になっており、OpenVPNプロトコルを介してNordVPNに接続している状態を示しています。

![gl.inet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/vpn_dashboard.png){class="glboxshadow"}

VPNサーバーセクションの**Global Options**でVPNカスケーディングを有効にすることができます。

![gl.inet enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

## VPNポリシーはVPNカスケーディングに影響しますか？

* ポリシーはVPNカスケーディングに影響しません

    **Global Proxy**、**ターゲットドメインやIPに基づく**、**クライアントデバイスに基づく**、**VLANに基づく**などのVPNポリシーは、VPNカスケーディングに影響しません。これらのポリシーは、ルーターのサブネット内に物理的に接続されたデバイスにのみ影響します。

    ![gl.inet vpn dashboard, vpn policy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/modify_vpn_policy_mode_1.png){class="glboxshadow"}

* ポリシーはVPNカスケーディングに影響します

    **自動検出**や**カスタマイズされたルーティングルール**を使用する場合、VPN構成に付属するルーティングルールや設定したルールは、ルーターのデータルーティング方法に影響するため、VPNカスケーディングが機能しない場合があります。

    ![gl.inet vpn dashboard, vpn policy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/modify_vpn_policy_mode_2.png){class="glboxshadow"}

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪問してください。