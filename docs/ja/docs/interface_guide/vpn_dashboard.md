# VPN Dashboard {#vpn-dashboard}

このページの内容は、ファームウェア v4.9.x 以降に基づいています。デバイスで別のファームウェアバージョンを使用している場合は、以下のセレクターで該当するガイドに切り替えてください。

<div class="gl-link-select" data-label="ファームウェアバージョン" data-placeholder="ファームウェア v4.9 以降" markdown="1">

- [ファームウェア v4.7 以前](vpn_dashboard_v4.7.md)
- [ファームウェア v4.8](vpn_dashboard_v4.8.md)

</div>

---

Web Admin Panel の左側で、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboard では、ルーティングルール、接続中のサーバー、トラフィック統計、クライアント仮想 IP、接続ログなどの VPN 接続情報を確認できるほか、VPN キルスイッチ、IP マスカレーディング、MTU などの詳細設定も行えます。

ファームウェア v4.8 と比較して、v4.9 の VPN Dashboard には次の改善があります。

1. **1 つのトンネルグループ内で複数のプロファイルを選択し、優先度を設定できます。** トンネルは、優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。

2. **各トンネルグループは独立して動作し、グループ間ではフェイルオーバーしません。** 1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムはトンネルのキルスイッチと All Other Traffic トンネルの状態に基づいて、ローカル WAN へ切り替えるかどうかを判断します。

## VPN プロファイルをアップロードする {#upload-vpn-profile}

このページを初めて開いたとき、まだトンネルが作成されていない場合は、以下のような画面が表示されます。**Add VPN Tunnel** をクリックして開始します。

![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

**VPN Client Profile** ページに移動します。VPN プロバイダーを選択してログインしてください。

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. 上の画像に表示されている VPN プロバイダーは、GL.iNet ルーターの Web Admin Panel に統合されています。有効なサブスクリプションがあれば、認証情報を入力するだけですぐにログインし、VPN 接続用の設定ファイルを取得できます。
    
    2. 他の VPN プロバイダーを契約している場合や、独自の VPN 設定をアップロードしたい場合は、**Add Manually** をクリックして設定ファイルをアップロードしてください。

ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例に説明します。PureVPN をクリックし、有効な認証情報でログインします。

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

VPN プロファイルの一覧が表示されます。VPN サービスプロバイダーによっては、一覧が表示される前に VPN プロトコルや希望するサーバー / 都市を選択する必要がある場合があります。

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

下部の **Go to Dashboard** をクリックします。VPN Dashboard に移動し、VPN トンネルの追加と VPN ポリシーの設定を行います。

## VPN トンネルを追加する {#add-vpn-tunnel}

### 基本手順 {#general-steps}

以下の手順で VPN トンネルを追加し、VPN ポリシーを設定します。必要に応じて [設定例](#case-reference) を参照してください。

1. VPN Dashboard で **Add VPN Tunnel** をクリックします。右側に VPN セットアップウィザードが表示されます。

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. VPN プロファイルを選択します。

    1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整してから、**Next** をクリックします。

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **注意**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは [トンネルオプション](#tunnel-options) と [その他のすべてのトラフィック](#all-other-traffic) の設定にあるキルスイッチの状態に基づいて、ルーターのローカルネットワーク（WAN）へ切り替えるかどうかを判断します。

3. クライアント送信元を選択し、**Next** をクリックします。

    選択肢は 4 つあります。

    - **All Clients**: 選択すると、すべてのデバイスからのトラフィックがこのルールに一致します。
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: 選択すると、指定した接続タイプ（例: LAN サブネット、Drop-in Gateway、ゲストネットワーク）からのトラフィックがこのルールに一致します。
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: 選択すると、指定したデバイス（MAC アドレスで識別）からのトラフィックがこのルールに一致します。
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: 選択すると、指定したデバイス（MAC アドレスで識別）からのトラフィックはこのルールに一致しません。
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. トラフィック宛先を選択し、**Apply** をクリックします。

    選択肢は 3 つあります。

    - **All Targets**: 選択すると、このルールに一致するトラフィックはすべての宛先へルーティングされます。
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは指定したドメインまたは IP アドレスへルーティングされます。内容は手動で入力する必要があります。
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは、指定したドメインまたは IP アドレスへルーティングされません。内容は手動で入力する必要があります。
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. VPN トンネルが追加され、**VPN Dashboard** に移動します。必要に応じて、さらに VPN トンネルを追加してください。

    安全のため、VPN トンネルを有効にする前に、[その他のすべてのトラフィック](#all-other-traffic) と [トンネルオプション](#tunnel-options) で **Kill Switch** の状態を確認してください。

### 設定例 {#case-reference}

参考として、代表的な VPN ポリシーの設定例を 2 つ、手順付きで示します。

??? note "ケース 1: 指定したデバイスのみを VPN 経由でルーティングする"

    **要件:**

    1. このルーターに接続された特定のデバイスだけが VPN 経由でインターネットへアクセスし、それ以外のデバイスはローカル WAN 経由でインターネットへアクセスします。

    2. 選択したデバイスは VPN 接続のみを使用する必要があります。VPN が予期せず切断された場合、DNS リークや IP 追跡を防ぐため、それらのデバイスのインターネットアクセスはブロックされます。

    **設定手順:**

    1. VPN プロファイルを選択します。

        統合 VPN サービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

        ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

        ![case 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. クライアント送信元を選択します。

        **Specified Devices** タブをクリックし、VPN を使用するデバイスを選択して **Next** をクリックします。

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. トラフィック宛先を選択します。

        **All Targets** タブをクリックしてトラフィック宛先に設定し、**Apply** をクリックします。

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. VPN Dashboard に移動します。以下のように、VPN トンネルが追加されています。

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. このトンネルの **Kill Switch** が有効になっていることを確認してください。VPN が予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNS リークや IP 追跡を防ぐためにブロックされます。

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}
        
    6. **Allow Non-VPN Traffic** が有効になっていることを確認してください。これはデフォルトで有効になっており、VPN トンネルに一致しないトラフィックでもローカル WAN 経由でインターネットへアクセスできるようにします。

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. 中央のボタンをクリックして、このトンネルを有効にします。

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. 接続が完了すると、VPN ポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想 IP アドレスなどの VPN 接続情報が表示されます。

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        これで、指定した 2 台のデバイスだけが VPN 経由でインターネットへアクセスします。VPN が予期せず切断された場合、DNS リークや IP 追跡を防ぐため、それらのデバイスのインターネットアクセスはブロックされます。それ以外のデバイスはローカル WAN 経由でインターネットへアクセスします。

??? note "ケース 2: 特定の Web サイトへのアクセスはすべてのデバイスで VPN 1 を経由させ、残りのトラフィックはすべて VPN 2 を経由させる"

    **要件:**

    1. すべてのデバイスは、特定のソーシャルメディアおよびストリーミングサービスのドメインにアクセスするときは **VPN Tunnel 1** を使用し、それ以外のすべてのインターネットアクセスには **VPN Tunnel 2** を使用します。

    2. VPN トンネルが予期せず切断された場合、DNS リークや IP 追跡を防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

    **設定手順:**

    1. Tunnel 1 用の VPN プロファイルを選択します。

        統合 VPN サービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。
        
        ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整してから、**Next** をクリックします。

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. クライアント送信元を選択します。

        **All Clients** タブをクリックして Tunnel 1 のクライアント送信元に設定し、**Next** をクリックします。

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. トラフィック宛先を選択します。

        **Specified Domain / IP List** タブをクリックし、以下のように一般的なソーシャルメディアおよびストリーミングサービスのドメインを入力して、**Apply** をクリックします。

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. VPN Dashboard に移動します。VPN Tunnel 1 が追加されています。

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Tunnel 1 の **Kill Switch** が有効になっていることを確認してください。VPN が予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNS リークや IP 追跡を防ぐためにブロックされます。

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}
        
    6. **Add New Tunnel** をクリックして Tunnel 2 を追加します。

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Tunnel 2 用の VPN プロファイルを選択します。

        ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. クライアント送信元を選択します。

        **All Clients** タブをクリックして Tunnel 2 のクライアント送信元に設定し、**Next** をクリックします。

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. トラフィック宛先を選択します。

        **All Targets** タブをクリックして Tunnel 2 のトラフィック宛先に設定し、**Apply** をクリックします。

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. VPN Dashboard に移動します。VPN Tunnel 2 が追加されています。

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Tunnel 2 の **Kill Switch** が有効になっていることを確認してください。VPN が予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNS リークや IP 追跡を防ぐためにブロックされます。

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. 右上の歯車アイコンをクリックし、**Enhanced Kill Switch** を有効にします。これにより、すべてのトラフィックは VPN 経由でのみインターネットへアクセスするようになります。

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. 中央のボタンをクリックして、Tunnel 1 と Tunnel 2 を有効にします。

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. 接続が完了すると、VPN ポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想 IP アドレスなどの VPN 接続情報が表示されます。

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        これで、指定したドメインへアクセスするときはすべてのデバイスが **VPN Tunnel 1** を使用し、それ以外のインターネットアクセスには **VPN Tunnel 2** を使用します。VPN トンネルが予期せず切断された場合、DNS リークや IP 追跡を防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

## キルスイッチ {#kill-switch}

!!! Tip "キルスイッチとは？"

    VPN キルスイッチは、VPN 接続に障害が発生したときに、トラフィックが暗号化されていないインターネット接続へ切り替わるのを防ぐのに役立ちます。

    個別のトンネルで **Kill Switch** を有効にすると、そのトンネルの接続に障害が発生した場合、そのトンネルに割り当てられたトラフィックのインターネットアクセスがブロックされます。その他のトラフィックには **All Other Traffic** の設定が適用されます。

    **Enhanced Kill Switch** は、どの VPN トンネルにも一致しないインターネットトラフィックをブロックします。各トンネルの **Kill Switch** 設定を上書きすることはありません。

ファームウェア v4.8 以降、GL.iNet ルーターでは、グローバル VPN 接続のキルスイッチと、個々の VPN トンネルのキルスイッチを設定できます。

- グローバル VPN 接続のキルスイッチ（Enhanced Kill Switch）を設定するには、[その他のすべてのトラフィック](#all-other-traffic) を参照してください。

- 個々の VPN トンネルのキルスイッチを設定するには、[トンネルオプション](#tunnel-options) を参照してください。

## その他のすべてのトラフィック {#all-other-traffic}

右上の歯車アイコンをクリックすると、VPN トンネルに一致しないトラフィックのポリシーを設定できます。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

このポリシーは、どの VPN トンネルグループにも一致しないトラフィックがインターネットへアクセスできるかどうかを制御します。選択肢は **Allow Non-VPN Traffic** と **Enhanced Kill Switch** の 2 つです。

- **Allow Non-VPN Traffic**: 非 VPN トラフィックが通常どおりインターネットへアクセスできるよう、デフォルトで有効になっています。

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: すべてのデバイスに VPN 経由でのインターネットアクセスを強制します。VPN トンネルに一致しないトラフィックはすべてブロックされます。このグローバル設定は、個々の VPN トンネルに設定されたキルスイッチを上書きしません。

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## トンネルオプション {#tunnel-options}

各 VPN トンネルでは、VPN キルスイッチ、IP マスカレーディング、MTU などの詳細設定を行えます。

トンネルグループの歯車アイコンをクリックし、**Options** を選択します。

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、VPN 接続が予期せず切断された場合に、この VPN トンネルに一致するトラフィックはブロックされます。無効にすると、そのトラフィックは **All Other Traffic** トンネルへフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスは VPN トンネル経由でパケットを送信します。これらのサービスは通常、正しく動作するためにデバイスの実 IP アドレスを必要とするため、このオプションはデフォルトで無効です。

- **Allow Remote Access to the LAN Subnet**: 有効にすると、VPN 経由でこのルーターおよびその LAN デバイスへのリモートアクセスが許可されます。VPN サーバーが、その LAN サブネットへの戻りルートをアドバタイズしている必要があります。

- **IP Masquerading**: 有効にすると、LAN クライアントの送信元 IP アドレスはルーターの VPN トンネル IP に書き換えられます。リモートピアがお使いの LAN サブネットを認識しているサイトツーサイト構成の場合にのみ、無効にしてください。

- **MTU**: トンネルに設定した MTU 値は、設定ファイル内の MTU 設定を上書きします。

## トンネル優先度 {#tunnel-priority}

トンネル優先度を調整するには、トンネルグループの歯車アイコンをクリックし、**Priority** を選択します。

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

右側の三本線アイコンを長押ししてドラッグし、トンネルの順序を変更してから **Apply** をクリックします。

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは次のルールに従ってトラフィックをルーティングします。**

1. トラフィックは、まず最も優先度の高いトンネルのルールへの一致を試みます。一致した場合はそのトンネル経由でルーティングされ、一致しない場合は次の優先度のトンネルを試し、以降も同様に続きます。

2. 各トンネルグループは独立して動作します。いったんトンネルのルールに一致したトラフィックは、そのトンネル経由でルーティングされ、トンネルグループ間でのフェイルオーバーは行われません。

3. 各トンネルグループ内で複数のプロファイルを選択すると、トンネル内フェイルオーバーが有効になります。トンネルグループ内で最も優先度の高いプロファイルがダウンした場合、トンネルは自動的に 2 番目に優先度の高いプロファイルで接続し、以降も同様に続きます。

4. VPN トンネルが予期せず切断された場合、このトンネルの **Kill Switch** が有効かどうかに基づいて、トラフィックを All Other Traffic トンネルへフェイルオーバーするかどうかが決まります。

    - キルスイッチが有効な場合、トラフィックはブロックされ、All Other Traffic トンネルへはフェイルオーバーしません。
    - キルスイッチが無効な場合、トラフィックは All Other Traffic トンネルへフェイルオーバーします。

5. **All Other Traffic** トンネルでは、モードによって、VPN トンネルに一致しないトラフィックがインターネットへアクセスできるかどうかが決まります。

    - **Allow Non-VPN Traffic**: デフォルトで有効になっており、VPN トンネルに一致しないトラフィックでもローカル WAN 経由でインターネットへアクセスできるようにします。

    - **Enhanced Kill Switch**: すべてのデバイスに VPN 経由でのインターネットアクセスを強制します。VPN トンネルに一致しないトラフィックはすべてブロックされます。このグローバル設定は、個々の VPN トンネルに設定されたキルスイッチを上書きしません。つまり、キルスイッチを強化し、通常のインターネットアクセスをブロックすることで IP リークを防ぎます。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
