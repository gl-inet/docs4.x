# VPN ダッシュボード

**注意**: このガイドはファームウェアv4.8に基づいています。旧バージョンについては、[こちら](vpn_dashboard_v4.7.md)を参照してください。

---

Web管理パネルの左側で、**VPN** -> **VPNダッシュボード** に移動します。

VPNダッシュボードでは、トンネルルール、サーバーアドレス、トラフィック統計、クライアント仮想IP、接続ログなどのVPN接続情報を確認でき、VPNキルスイッチ、IPマスカレーディング、MTUなどの詳細設定も行えます。

また、複数のVPN接続を有効にして、マルチトンネル構成に対応することもできます。

## セットアップウィザード

左上の本のアイコンをクリックし、VPNセットアップウィザードに従ってVPN設定をすばやく完了します。

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**注意**: VPNセットアップウィザードは、AzireVPN、Hide.me、IPVanish、Mullvad、NordVPN、PIA、Surfshark などの統合VPNサービス専用です。その他のVPNサービスを利用する場合は、ウィザードをスキップして [OpenVPNクライアント](openvpn_client.md){target="\_blank"} または [WireGuardクライアント](wireguard_client.md){target="\_blank"} で手動設定してください。

ここでは **Hide.me** を例に説明します。Hide.me の認証情報でログインしてください。

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

VPNサーバーを選択し、**適用** をクリックします。ここで選ぶサーバーが、このVPNトンネル経由で接続される先になります。公開IPアドレスは、選択したサーバーの所在地からアクセスしているように見えます。

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

接続は自動的に開始されます。接続に成功したらVPNダッシュボードへ移動し、VPNトンネルが有効になっていることを確認できます。

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

現在使用中のVPNプロトコル（例: WireGuard）、設定ファイル、サーバーアドレス、サーバーの待受ポート、トラフィック統計、クライアント仮想IPが表示されます。右下では接続ログも確認できます。

接続されているすべてのクライアントは、このVPNトンネル経由でインターネットにアクセスします。

VPNポリシーを設定したい場合は、[ポリシーモード](#policy-mode)を参照してください。

## VPNモード

VPNダッシュボード右上のボタンからVPNモードを切り替えます。

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

利用できるモードは **グローバルモード** と **ポリシーモード** の2つです。

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### グローバルモード

このモードでは、すべてのトラフィックがVPNトンネル経由でルーティングされ、アクティブにできるVPNクライアントインスタンスは1つだけです。

すべてのクライアントトラフィックを単一のVPNサーバー経由でルーティングしたい場合に適しています。例えば、ネットワーク全体の保護を統一したい場合や、特定地域向けコンテンツにアクセスしたい場合などです。

以下の例では、ルーターはWireGuardプロトコルを使ってオーストラリアのサーバーに接続しています。接続されたクライアントのすべてのトラフィックは、このVPNトンネル経由でルーティングされます。

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### ポリシーモード

このモードでは、ルーターは複数のVPNサーバーに接続でき、クライアントや通信先ごとにルーティングルールをカスタマイズできます。

複数のVPNサーバーを使い分けて、トラフィックの種類や宛先ごとに経路を変えたい場合に適しています。

VPNモードを **ポリシーモード** に切り替え、**適用** をクリックします。

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

切り替え後、VPNがまだ有効でない場合、ページには **プライマリートンネル**、**トンネルの追加**、**その他のすべてのトラフィック** の3つのセクションが表示されます。

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

各セクションの詳細は以下を参照してください。

- [プライマリートンネル](#primary-tunnel)
- [トンネルの追加](#add-tunnel)
- [その他のすべてのトラフィック](#all-other-traffic)

#### プライマリートンネル

プライマリートンネルは、ポリシーモードであらかじめ用意されているトンネルです。最も高い優先度を持ち、トンネルが複数ある場合は[トンネル優先度](#tunnel-priority)を変更できます。

このトンネルでは、次の3つの要素を設定してトンネルルールをカスタマイズできます。

1.  **From**: トラフィックの送信元、つまりこのトンネル経由でルーティングする対象です。

    グレーアウトされたボックスをクリックして送信元を選択します。

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}
    - **すべてのクライアント**: すべてのデバイスからのトラフィックがこのルールに一致します。

      ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **指定された接続タイプ**: 指定した接続タイプ（例: LANサブネット、Drop-in Gateway、ゲストネットワーク）からのトラフィックがこのルールに一致します。

      ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

      このルーターでOpenVPNサーバーまたはWireGuardサーバーを有効にしている場合は、指定された接続タイプの下に追加オプションが表示されます。これは[VPNカスケード](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md)で便利です。

      ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **指定されたデバイス**: 指定したデバイス（MACアドレスで識別）からのトラフィックがこのルールに一致します。

      ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **指定デバイスを除外**: 指定したデバイス（MACアドレスで識別）からのトラフィックはこのルールに一致しません。

      ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2.  **To**: トラフィックの宛先です。

    グレーアウトされたボックスをクリックして宛先を選択します。

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}
    - **すべてのターゲット**: このルールに一致するトラフィックはすべての宛先へルーティングされます。

      ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **指定されたドメイン / IPリスト**: 指定したドメインまたはIPアドレス宛てのトラフィックがこのルールに一致します。内容は手動で入力します。

      ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

      または、**Input Mode** を Manual から Subscription URL に切り替えて、URLを入力することもできます。

      ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

      !!! 注意

            - Subscription URL を選択すると、URL内のドメイン名またはIPアドレスは毎日自動更新されます。

            - 正しいURLを入力してください。URLの検証により、ドメイン名またはIPアドレスの有効性を確認できます。詳細は[こちら](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}をご覧ください。

    - **指定されたドメイン / IPリストを除外**: このルールに一致するトラフィックは、指定したドメインまたはIPアドレスにはルーティングされません。内容は手動で入力します。

      ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

      または、**Input Mode** を Manual から Subscription URL に切り替えて、URLを入力することもできます。

      ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

      !!! 注意

            - Subscription URL を選択すると、URL内のドメイン名またはIPアドレスは毎日自動更新されます。

            - 正しいURLを入力してください。URLの検証により、ドメイン名またはIPアドレスの有効性を確認できます。詳細は[こちら](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}をご覧ください。

3.  **Via**: トラフィックをどの経路でルーティングするか、つまりVPNを使うかどうかを表します。

    グレーアウトされたボックスをクリックしてルーティング方法を選択します。

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}
    - **VPNを使用**: このルールに一致するトラフィックは、VPN経由で選択した宛先にルーティングされます。

      まずルーターをVPNクライアントとして設定する必要があります。[VPNセットアップウィザード](#vpn-setup-wizard)を使うか、左側メニューの OpenVPN Client / WireGuard Client から手動設定してください。

      VPNクライアント設定が完了したら、このトンネルで使用するVPN設定ファイルを選択し、**Apply** をクリックします。

      ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **VPNを使用しない**: このルールに一致するトラフィックは、VPNではなくローカルWAN経由で選択した宛先へルーティングされます。

      ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4.  送信元、宛先、ルーティング方法を選択すれば、プライマリートンネルの設定は完了です。

以下の例では、プライマリートンネルのルールは「すべてのクライアントがVPNを使用して、指定したドメインにアクセスする」です。トラフィックはオーストラリアのサーバーを経由し、このトンネルから選択したインターネットドメインへ出ていきます。

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**注意**: セキュリティのため、トンネルを有効にする前に [その他のすべてのトラフィック](#all-other-traffic) と [トンネルオプション](#tunnel-options) も確認してください。

#### トンネルの追加

複数のVPNインスタンス用に追加トンネルを作成するには、プライマリートンネルの下にある **トンネルの追加** をクリックし、カスタムルールを設定します。

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

トンネル名を設定します。

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

VPNダッシュボードに新しいトンネルが追加されます。

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

必要に応じてさらにトンネルを追加できます。作成できるトンネルは最大5個です（プリセットのプライマリートンネルを含む）。

送信元、宛先、ルーティング方法を設定してトンネルルールをカスタマイズしてください。詳細は [プライマリートンネル](#primary-tunnel) を参照してください。

**注意**: セキュリティのため、トンネルを有効にする前に [その他のすべてのトラフィック](#all-other-traffic) と [トンネルオプション](#tunnel-options) も確認してください。

#### その他のすべてのトラフィック

ポリシーモードでは、あらかじめ有効になっているトンネルがVPNダッシュボードの下部に表示されます。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

このトンネルは、上記のVPNトンネルグループに一致しないトラフィックがインターネットへアクセスできるかどうかを制御します。VPNを経由しないトラフィックでも通常どおり通信できるよう、デフォルトで有効になっています。

- 有効な場合、一致しないトラフィックも引き続きインターネットへアクセスできます。

  ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- 無効な場合、VPN経由でルーティングされたトラフィックだけがインターネットへアクセスできます。非VPNトラフィックと、VPN接続からフェイルオーバーしたトラフィックはすべてブロックされます。この設定は、各VPNトンネル個別のキルスイッチを上書きするものではありません。

  ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### トンネル優先度

デフォルトでは、プリセットのプライマリートンネルが最優先で、その次に手動で追加したトンネル、最後にローカルWAN経由の接続性を維持するための **その他のすべてのトラフィック** トンネルが続きます。

優先度を変更するには、上部の情報バーにある **Modify Priority** をクリックするか、各トンネル左上の優先度ラベル（例: Priority 1 / Priority 2）をクリックします。

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

右側の三本線アイコンをドラッグして順序を変更し、**Apply** をクリックします。

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは以下の順序でトラフィックをルーティングします。**

1. トラフィックはまず最優先のトンネルルールに一致するかを確認します。一致した場合はそのトンネルを通ります。一致しない場合は次の優先度のトンネルを試し、最終的に **その他のすべてのトラフィック** トンネルまで判定を続けます。

2. VPNトンネルが予期せず切断された場合、このトンネルの **キルスイッチ** が有効かどうかに応じて、次の優先度のトンネルへフェイルオーバーするかが決まります。
   - キルスイッチが有効な場合、トラフィックはブロックされ、次の優先度のトンネルにはフェイルオーバーしません。
   - キルスイッチが無効な場合、トラフィックは次の優先度のトンネルへフェイルオーバーし、そのトンネルルールへの一致を試みます。

3. **その他のすべてのトラフィック** トンネルはデフォルトで有効になっており、VPNトンネルに一致しないトラフィックでもインターネットへアクセスできるようにします。
   - 有効な場合、一致しないトラフィックやフェイルオーバートラフィックはローカルWAN経由でルーティングされます。
   - 無効な場合、キルスイッチが強化され、IPリーク防止のため通常のインターネットアクセスがブロックされます。

#### トンネルオプション

各VPNトンネルでは、VPNキルスイッチ、IPマスカレーディング、MTUなどの詳細設定を行えます。

トンネル名の横にある歯車アイコンをクリックし、**Options** を選択します。

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、このVPNトンネルに一致するトラフィックは、VPN接続が予期せず切断された場合にブロックされます。無効にすると、そのトラフィックは次の優先度のトンネル、またはローカルWANへフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスはVPNトンネル経由で通信します。これらのサービスは通常デバイスの実IPアドレスを必要とするため、この設定はデフォルトで無効です。

- **Allow Remote Access the LAN Subnet**: 有効にすると、VPN経由でこのルーターおよびLAN内デバイスへリモートアクセスできます。VPNサーバー側で、LANサブネットへの戻りルートが通知されている必要があります。

- **IP Masquerading**: 有効にすると、LANクライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモート側がLANサブネットを認識しているSite-to-Site構成の場合にのみ無効にしてください。

- **MTU**: ここで設定したMTU値は、設定ファイル内のMTU設定を上書きします。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご利用ください。
