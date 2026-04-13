# VPN Dashboard (Firmware v4.9)

**Note**: このガイドはファームウェア v4.9 を基準にしています。以前のバージョンについては [こちら](vpn_dashboard.md) を参照してください。

---

Web Admin Panel の左側で、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboard では、ルーティングルール、接続中のサーバー、トラフィック統計、クライアント仮想 IP、接続ログなどの VPN 接続情報を確認できるほか、VPN Kill Switch、IP Masquerading、MTU などの詳細設定も行えます。

ファームウェア v4.8 と比較して、v4.9 の VPN Dashboard には次の改善があります。

1. **1 つのトンネルグループ内で複数のプロファイルを選択し、優先度を設定できます。** トンネルは、優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。

2. **各トンネルグループは独立して動作し、グループ間ではフェイルオーバーしません。** 1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と All Other Traffic トンネルの状態に基づいて、ローカル WAN へ切り替えるかどうかを判断します。

## はじめに {#getting-started}

このページを初めて開いたとき、まだトンネルが作成されていない場合は、以下のような画面が表示されます。**Add VPN Tunnel** をクリックして開始します。

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**VPN Client Profile** ページに移動し、VPN プロバイダーを選択してログインします。

ここに表示される VPN プロバイダーは、GL.iNet ルーターの Web Admin Panel に統合されています。有効なサブスクリプションがあれば、認証情報を入力するだけでログインし、VPN 接続用の設定ファイルを取得できます。

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

他の VPN プロバイダーを利用している場合や、独自の VPN 設定をアップロードしたい場合は、**Add Manually** をクリックして設定ファイルをアップロードしてください。

ここでは **PureVPN** を例に説明します。PureVPN をクリックし、有効な認証情報でログインします。

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

VPN プロファイルの一覧が表示されます。VPN サービスプロバイダーによっては、一覧が表示される前に VPN プロトコルや希望するサーバー / 都市を選択する必要がある場合があります。

続いて、下部の **Go to Dashboard** をクリックします。VPN Dashboard に移動し、VPN トンネルの追加と VPN ポリシーの設定を行います。

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

??? "VPN ポリシーとは？"

    VPN ポリシーは、ネットワークトラフィックを VPN トンネル経由でどのようにルーティングするかを定義します。どのトラフィックを VPN 経由で宛先へ送るか、どのトラフィックをローカル WAN 経由で直接インターネットへ出すかを決定します。

    これにより、すべてのクライアントまたは特定のデバイスについて、指定した Web サイトやインターネット全体へのアクセスを VPN 接続経由にでき、柔軟で安全なネットワーク管理を実現できます。

VPN Dashboard では、セットアップウィザードに従って VPN ポリシーを設定します。VPN プロファイル、クライアント送信元、トラフィック宛先を順に選択してください。

1. **VPN プロファイルを選択します。**

    統合 VPN サービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

    ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカル WAN へ切り替えるかどうかを判断します。

2. **クライアント送信元を選択します。**

    選択肢は 4 つあります。

    - **All Clients**: 選択すると、すべてのデバイスからのトラフィックがこのルールに一致します。
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: 選択すると、指定した接続タイプ（例: LAN subnet、Drop-in Gateway、Guest Network）からのトラフィックがこのルールに一致します。
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: 選択すると、指定したデバイス（MAC アドレスで識別）からのトラフィックがこのルールに一致します。
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: 選択すると、指定したデバイス（MAC アドレスで識別）からのトラフィックはこのルールに一致しません。
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

3. **トラフィック宛先を選択します。**

    選択肢は 3 つあります。

    - **All Targets**: 選択すると、このルールに一致するトラフィックはすべての宛先へルーティングされます。
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは指定したドメインまたは IP アドレスへルーティングされます。内容は手動で入力する必要があります。
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは、指定したドメインまたは IP アドレスへルーティングされません。内容は手動で入力する必要があります。
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

## 利用シナリオ

参考として、以下に 2 つのシナリオを手順付きで示します。

### シナリオ 1

**目的:**

1. このルーターに接続された特定のデバイスだけが VPN 経由でインターネットへアクセスし、それ以外のデバイスはローカル WAN 経由でアクセスするようにします。

2. 選択したデバイスは VPN 接続のみを使用する必要があります。VPN が予期せず切断された場合、DNS リークや IP 追跡を防ぐため、それらのデバイスのインターネットアクセスはブロックされます。

**以下の手順で VPN ポリシーを設定してください。**

1. VPN プロファイルを選択します。

    統合 VPN サービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

    ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![scenario 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカル WAN へ切り替えるかどうかを判断します。

2. クライアント送信元を選択します。

    **Specified Devices** タブをクリックし、VPN を使用するデバイスを選択して **Apply** をクリックします。

    ![scenario 1 select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

3. トラフィック宛先を選択します。

    **All Targets** タブをクリックして宛先に設定し、**Apply** をクリックします。

    ![scenario 1 select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. VPN Dashboard に移動すると、VPN トンネルが追加されています。

    ![scenario 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

5. このトンネルの **Kill Switch** が有効になっていることを確認してください。VPN が予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNS リークや IP 追跡を防ぐためにブロックされます。

    ![scenario 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

    ![scenario 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

6. **Allow Non-VPN Traffic** が有効になっていることを確認してください。これはデフォルトで有効で、VPN トンネルに一致しないトラフィックでもローカル WAN 経由でインターネットへアクセスできるようにするための設定です。

    ![scenario 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

7. 中央のボタンをクリックして、このトンネルを有効にします。

    ![scenario 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

8. 接続が完了すると、VPN ポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想 IP アドレスなどの VPN 接続情報が表示されます。

    ![scenario 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

    これで、指定した 2 台のデバイスだけが VPN 経由でインターネットへアクセスします。VPN が予期せず切断された場合、それらのデバイスのインターネットアクセスは DNS リークや IP 追跡を防ぐためにブロックされます。それ以外のデバイスはローカル WAN 経由でインターネットへアクセスします。

### シナリオ 2

**目的:**

1. すべてのデバイスは、特定のソーシャルメディアおよびストリーミングサービスのドメインにアクセスするときは **VPN Tunnel 1** を使用し、それ以外のすべてのインターネットアクセスには **VPN Tunnel 2** を使用します。

2. VPN トンネルが予期せず切断された場合、DNS リークや IP 追跡を防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

**以下の手順で VPN ポリシーを設定してください。**

1. Tunnel 1 用の VPN プロファイルを選択します。

    ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![scenario 2 select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカル WAN へ切り替えるかどうかを判断します。

2. クライアント送信元を選択します。

    **All Clients** タブをクリックし、Tunnel 1 の client source に設定して **Apply** をクリックします。

    ![scenario 2 select source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. トラフィック宛先を選択します。

    **Specified Domain / IP List** タブをクリックし、以下のように一般的なソーシャルメディアおよびストリーミングサービスのドメインを入力して **Apply** をクリックします。

    ![scenario 2 select target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

4. VPN Dashboard に移動すると、Tunnel 1 が追加されています。

    ![scenario 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

5. Tunnel 1 の **Kill Switch** が有効になっていることを確認してください。VPN が予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNS リークや IP 追跡を防ぐためにブロックされます。

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

6. **Add New Tunnel** をクリックして Tunnel 2 を追加します。

    ![scenario 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

7. Tunnel 2 用の VPN プロファイルを選択します。

    ここでも [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。1 つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![scenario 2 select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1 つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカル WAN へ切り替えるかどうかを判断します。

8. クライアント送信元を選択します。

    **All Clients** タブをクリックし、Tunnel 2 の client source に設定して **Apply** をクリックします。

    ![scenario 2 select source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. トラフィック宛先を選択します。

    **All Targets** タブをクリックし、Tunnel 2 の宛先に設定して **Apply** をクリックします。

    ![scenario 2 select target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

10. VPN Dashboard に移動すると、Tunnel 2 が追加されています。

    ![scenario 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

11. Tunnel 2 の **Kill Switch** が有効になっていることを確認してください。VPN が予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNS リークや IP 追跡を防ぐためにブロックされます。

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

12. 右上の歯車アイコンをクリックし、**Enhanced Kill Switch** を有効にします。これにより、すべてのトラフィックが VPN 経由でのみインターネットへアクセスするようになります。

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

13. 中央のボタンをクリックして、Tunnel 1 と Tunnel 2 を有効にします。

    ![scenario 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

14. 接続が完了すると、VPN ポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想 IP アドレスなどの VPN 接続情報が表示されます。

    ![scenario 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

    これで、指定したドメインへアクセスするときはすべてのデバイスが **VPN Tunnel 1** を使用し、それ以外のインターネットアクセスには **VPN Tunnel 2** を使用します。VPN トンネルが予期せず切断された場合、すべてのデバイスのインターネットアクセスは DNS リークや IP 追跡を防ぐためにブロックされます。

## All Other Traffic {#all-other-traffic}

右上の歯車アイコンをクリックすると、VPN トンネルに一致しないトラフィックの扱いを設定できます。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

このポリシーは、どの VPN トンネルグループにも一致しないトラフィックがインターネットへアクセスできるかどうかを制御します。選択肢は **Allow Non-VPN Traffic** と **Enhanced Kill Switch** の 2 つです。

- **Allow Non-VPN Traffic**: 非 VPN トラフィックでも通常どおりインターネットへアクセスできるよう、デフォルトで有効になっています。

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: すべてのデバイスに対して、インターネットアクセスを VPN 経由に限定します。VPN トンネルに一致しないトラフィックはすべてブロックされます。このグローバル設定は、各 VPN トンネルに設定された個別の Kill Switch を上書きしません。

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## トンネル優先度 {#tunnel-priority}

トンネル優先度を調整するには、トンネルグループの歯車アイコンをクリックし、**Priority** を選択します。

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

右側の三本線アイコンをドラッグしてトンネルの順序を変更し、**Apply** をクリックします。

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは次のルールに従ってトラフィックをルーティングします。**

1. まず最優先のトンネルルールへの一致を試みます。一致した場合はそのトンネル経由でルーティングされ、一致しない場合は次の優先度のトンネルを順に試します。

2. 各トンネルグループは独立して動作します。いったんトンネルルールに一致したトラフィックは、そのトンネル経由でルーティングされ、トンネルグループ間でフェイルオーバーは行われません。

3. 各トンネルグループ内では複数のプロファイルを選択でき、トンネル内フェイルオーバーを有効にできます。トンネルグループ内で最優先のプロファイルが停止した場合、トンネルは自動的に次順位のプロファイルで接続を試みます。

4. VPN トンネルが予期せず切断された場合、このトンネルの **Kill Switch** が有効かどうかに応じて、トラフィックを All Other Traffic トンネルへフェイルオーバーするかどうかが決まります。

    - Kill Switch が有効な場合、トラフィックはブロックされ、All Other Traffic トンネルへはフェイルオーバーしません。
    - Kill Switch が無効な場合、トラフィックは All Other Traffic トンネルへフェイルオーバーします。

5. **All Other Traffic** では、VPN トンネルに一致しないトラフィックがインターネットへアクセスできるかどうかを、モードによって制御します。

    - **Allow Non-VPN Traffic**: デフォルトで有効で、VPN トンネルに一致しないトラフィックでもローカル WAN 経由でインターネットへアクセスできます。

    - **Enhanced Kill Switch**: すべてのデバイスに対して、インターネットアクセスを VPN 経由に限定します。VPN トンネルに一致しないトラフィックはすべてブロックされます。このグローバル設定は、各 VPN トンネルに設定された個別の Kill Switch を上書きしません。つまり、Kill Switch をさらに強化し、通常のインターネットアクセスもブロックすることで IP リークを防ぎます。

## トンネルオプション {#tunnel-options}

各 VPN トンネルでは、VPN Kill Switch、IP Masquerading、MTU などの詳細設定を行えます。

トンネルグループの歯車アイコンをクリックし、**Options** を選択します。

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、この VPN トンネルに一致するトラフィックは、VPN 接続が予期せず切断された場合にブロックされます。無効にすると、そのトラフィックは **All Other Traffic** トンネルへフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスは VPN トンネル経由でパケットを送信します。これらのサービスは通常デバイスの実 IP アドレスを必要とするため、このオプションはデフォルトで無効です。

- **Allow Remote Access to the LAN Subnet**: 有効にすると、VPN 経由でこのルーターおよび LAN 内デバイスにリモートアクセスできます。VPN サーバー側で、その LAN サブネットへの戻りルートが通知されている必要があります。

- **IP Masquerading**: 有効にすると、LAN クライアントの送信元 IP アドレスはルーターの VPN トンネル IP に書き換えられます。リモートピアが LAN サブネットを認識している Site-to-Site 構成の場合にのみ無効にしてください。

- **MTU**: ここで設定した MTU 値は、設定ファイル内の MTU 設定を上書きします。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
