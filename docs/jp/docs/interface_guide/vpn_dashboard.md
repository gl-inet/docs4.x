# VPN Dashboard

**注意**: このガイドはファームウェア v4.8 を基準にしています。以前のバージョンについては [こちら](vpn_dashboard_v4.7.md) を参照してください。

---

Web管理パネルの左側で、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboard では、トンネルルール、サーバーアドレス、トラフィック統計、クライアント仮想IP、接続ログなどのVPN接続情報を確認できるほか、VPNキルスイッチ、IPマスカレーディング、MTU などの詳細設定も行えます。

マルチトンネル構成のために、複数のVPN接続を有効にすることもできます。

## セットアップウィザード {#setup-wizard}

左上の本のアイコンをクリックし、VPN Setup Wizard に従ってVPN設定をすばやく完了します。

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**注意**: VPN Setup Wizard は、AzireVPN、Hide.me、IPVanish、Mullvad、NordVPN、PIA、Surfshark を含む統合VPNサービス専用です。その他のVPNサービスを利用する場合は、ウィザードをスキップし、[OpenVPN Client](openvpn_client.md){target="_blank"} または [WireGuard Client](wireguard_client.md){target="_blank"} に移動して手動でVPNを設定してください。

ここでは **Hide.me** を例に説明します。Hide.me の認証情報でログインします。

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

VPNサーバーを選択して **Apply** をクリックします。ここで選択したサーバーが、このVPNトンネル経由で接続する先になります。公開IPアドレスは、選択したサーバーの所在地からアクセスしているように見えます。

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

自動的に接続が開始されます。接続に成功したら VPN Dashboard に移動し、VPNトンネルが有効になっていることを確認できます。

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

現在使用中のVPNプロトコル（例: WireGuard）、設定ファイル、サーバーアドレス、サーバー待受ポート、トラフィック統計、クライアント仮想IP が表示されます。右下では接続ログも確認できます。

接続済みのすべてのクライアントは、このVPNトンネル経由でインターネットにアクセスします。

VPNポリシーを設定する場合は、[ポリシーモード](#policy-mode) を参照してください。

## VPNモード

VPN Dashboard で、右上のボタンをクリックしてVPNモードを切り替えます。

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

利用できるモードは **Global Mode** と **Policy Mode** の2つです。

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### グローバルモード {#global-mode}

このモードでは、すべてのトラフィックがVPNトンネル経由でルーティングされ、有効にできるVPNクライアントインスタンスは1つだけです。

統一的なネットワークセキュリティを確保したい場合や、地域限定コンテンツへアクセスしたい場合など、すべてのクライアントトラフィックを1台のVPNサーバー経由でルーティングする用途に適しています。

次の例では、ルーターは WireGuard プロトコルを使ってオーストラリアのサーバーへ接続しています。接続されたクライアントのすべてのトラフィックは、このVPNトンネル経由でルーティングされます。

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### ポリシーモード {#policy-mode}

このモードでは、ルーターは複数のVPNサーバーに接続でき、クライアントやトラフィック宛先ごとにルーティングルールをカスタマイズできます。

複数のVPNサーバーを使って異なるトラフィックを異なる宛先へ振り分けるような、柔軟なトラフィック管理が必要な用途に適しています。

VPN Mode を Policy Mode に切り替えて、**Apply** をクリックします。

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

切り替え後、VPNが有効になっていない場合、ページには Primary Tunnel、Add Tunnel、All Other Traffic の3つのセクションが表示されます。

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

各セクションをクリックすると、詳細を確認できます。

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### プライマリートンネル {#primary-tunnel}

Primary Tunnel は、Policy Mode における<u>プリセット</u>のトンネルです。最優先で使用され、複数のトンネルがある場合は [tunnel priority](#tunnel-priority) を変更できます。

このトンネルでは、次の3つの要素を設定してトンネルルールをカスタマイズできます。

1. **From**: トラフィック送信元、つまりこのトンネル経由でルーティングするトラフィックを指定します。

    グレー表示のボックスをクリックして、トラフィック送信元を選択します。

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients**: 選択すると、すべてのデバイスからのトラフィックがこのルールに一致します。

        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: 選択すると、指定した接続タイプ（例: LAN subnet、Drop-in Gateway、Guest Network）からのトラフィックがこのルールに一致します。

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        このルーターで OpenVPN server または WireGuard server を有効にしている場合、Specified Connection Types の下にさらに多くの選択肢が表示されます。これは [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md) で便利です。

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: 選択すると、指定したデバイス（MACアドレスで識別）からのトラフィックがこのルールに一致します。

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: 選択すると、指定したデバイス（MACアドレスで識別）からのトラフィックはこのルールに **一致しません**。

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: トラフィック宛先を指定します。

    グレー表示のボックスをクリックして、トラフィック宛先を選択します。

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: 選択すると、このルールに一致するトラフィックはすべての宛先へルーティングされます。

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは指定したドメインまたはIPアドレスへルーティングされます。内容は手動で入力する必要があります。

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        または、**Input Mode** を Manual から Subscription URL に切り替え、URL Link を入力します。

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Subscribe URL を選択すると、そのURL内のドメイン名またはIPが毎日自動的に更新されます。

            - 正しいURLを入力してください。URL detection により、ドメイン名またはIPアドレスの有効性が検証されます。[詳細はこちら](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは、指定したドメインまたはIPアドレスへ **ルーティングされません**。内容は手動で入力する必要があります。

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        または、**Input Mode** を Manual から Subscription URL に切り替え、URL Link を入力します。

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Subscribe URL を選択すると、そのURL内のドメイン名またはIPが毎日自動的に更新されます。

            - 正しいURLを入力してください。URL detection により、ドメイン名またはIPアドレスの有効性が検証されます。[詳細はこちら](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: トラフィックのルーティング方法、つまりVPNを使用するかどうかを指定します。

    グレー表示のボックスをクリックして、ルーティング方法を選択します。

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: 選択すると、このルールに一致するトラフィックはVPN経由で選択した宛先へルーティングされます。

        まず、ルーターをVPNクライアントとして設定する必要があります。[VPN Setup Wizard](#setup-wizard) を使ってすばやく設定を完了するか、左側のサイドバーで OpenVPN Client / WireGuard Client に移動して手動で設定してください。

        ルーターをVPNクライアントとして設定したら、このトンネルで使用するVPN設定ファイルを選択して **Apply** をクリックします。

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: 選択すると、このルールに一致するトラフィックはVPNではなくローカルWAN経由で選択した宛先へルーティングされます。

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. トラフィック送信元、宛先、ルーティング方法を選択すると、Primary Tunnel ルールの設定は完了です。

次の例では、Primary Tunnel のルールは「すべてのクライアントがVPNを使用して指定ドメインへアクセスする」です。トラフィックはオーストラリアのサーバーを経由し、このトンネルから選択したインターネットドメインへ出ていきます。

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Note**: セキュリティ確保のため、トンネルを有効にする前に [All Other Traffic](#all-other-traffic) と [Tunnel Options](#tunnel-options) で他の設定も確認してください。

#### トンネルを追加 {#add-tunnel}

複数のVPNインスタンス用に追加トンネルを作成するには、Primary Tunnel の下にある **Add Tunnel** をクリックし、カスタムルールを設定します。

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

トンネル名を入力します。

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

VPN Dashboard にもう1つトンネルが追加されます。

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

必要に応じてさらにトンネルを追加できます。作成できるのは最大5つのトンネルです（プリセットの Primary Tunnel を含む）。

トラフィック送信元、宛先、ルーティング方法を設定してトンネルルールをカスタマイズしてください。詳細は [Primary Tunnel](#primary-tunnel) を参照してください。

**Note**: セキュリティ確保のため、トンネルを有効にする前に [All Other Traffic](#all-other-traffic) と [Tunnel Options](#tunnel-options) で他の設定も確認してください。

#### その他のすべてのトラフィック {#all-other-traffic}

Policy Mode では、VPN Dashboard の下部に<u>あらかじめ有効になっている</u>トンネルが表示されます。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

このトンネルは、上記のVPNトンネルグループのいずれにも一致しないトラフィックがインターネットへアクセスできるかどうかを制御します。VPN経由でルーティングされないトラフィックでも通常どおりインターネットへアクセスできるよう、デフォルトで有効になっています。

- 有効な場合、一致しないトラフィックも引き続きインターネットへアクセスできます。

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- 無効な場合、VPN経由でルーティングされたトラフィックだけがインターネットへアクセスできます。非VPNトラフィックと、VPN接続からフェイルオーバーしたトラフィックはすべてブロックされます。この設定は、各VPNトンネルの個別のキルスイッチを上書きしません。

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### トンネル優先度 {#tunnel-priority}

デフォルトでは、プリセットの Primary Tunnel が最優先で、その次に手動で追加したトンネル（ある場合）が続き、最後にローカルネットワーク接続（ローカルWAN経由）を確保するための All Other Traffic トンネルが続きます。

トンネル優先度を変更するには、上部の情報バーで **Modify Priority** をクリックするか、任意のトンネル左上にある **priority label**（例: Priority 1 / Priority 2）をクリックします。

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

右側の三本線アイコンを長押ししてトンネルの順序を変更し、**Apply** をクリックします。

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは次の順序でトラフィックをルーティングします。**

1. まず最優先のトンネルルールへの一致を試みます。一致した場合はそのトンネルを経由してルーティングされ、一致しない場合は次の優先度のトンネルを順に試し、最後に "All Other Traffic" トンネルまで判定します。

2. VPNトンネルが予期せず切断された場合、このトンネルの **Kill Switch** が有効かどうかに応じて、次順位のトンネルへトラフィックをフェイルオーバーするかどうかが決まります。

    - Kill Switch が有効な場合、トラフィックはブロックされ、次順位のトンネルへはフェイルオーバーしません。
    - Kill Switch が無効な場合、トラフィックは次順位のトンネルへフェイルオーバーし、そのトンネルルールへの一致を試みます。

3. **All Other Traffic** トンネルはデフォルトで有効になっており、VPNトンネルに一致しないトラフィックでもインターネットへアクセスできるようになっています。

    - 有効な場合、一致しないトラフィックやフェイルオーバートラフィックはローカルWAN経由でルーティングされます。
    - 無効な場合、キルスイッチが強化され、IPリークを防ぐため通常のインターネットアクセスがブロックされます。

#### トンネルオプション {#tunnel-options}

各VPNトンネルでは、VPNキルスイッチ、IPマスカレーディング、MTU などの詳細設定を行えます。

トンネル名の横にある歯車アイコンをクリックし、**Options** を選択します。

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、このVPNトンネルに一致するトラフィックは、VPN接続が予期せず切断された場合にブロックされます。無効にすると、そのトラフィックは次順位のトンネルまたはローカルWANへフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスはVPNトンネル経由でパケットを送信します。これらのサービスは通常デバイスの実IPアドレスを必要とするため、このオプションはデフォルトで無効です。

- **Allow Remote Access the LAN Subnet**: 有効にすると、VPN経由でこのルーターおよびそのLANデバイスにリモートアクセスできます。VPNサーバー側で、そのLANサブネットへの戻りルートが通知されている必要があります。

- **IP Masquerading**: 有効にすると、LANクライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモートピアがLANサブネットを認識している Site-to-Site 構成の場合にのみ無効にしてください。

- **MTU**: ここで設定したMTU値は、設定ファイル内のMTU設定を上書きします。

---

まだご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
