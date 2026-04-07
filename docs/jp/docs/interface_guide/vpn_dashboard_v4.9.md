# VPN Dashboard (Firmware v4.9)

**注意**: このガイドはファームウェア v4.9 を基準にしています。以前のバージョンについては [こちら](vpn_dashboard.md) を参照してください。

---

Web管理パネルの左側で、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboard では、ルーティングルール、接続中のサーバー、トラフィック統計、クライアント仮想IP、接続ログなどのVPN接続情報を確認できるほか、VPNキルスイッチ、IPマスカレーディング、MTU などの詳細設定も行えます。

ファームウェア v4.8 と比較して、v4.9 の VPN Dashboard には次の改善があります。

1. **1つのトンネルグループ内で複数のプロファイルを選択し、優先度を設定できます。** トンネルは、優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。

2. **各トンネルグループは独立して動作し、グループ間ではフェイルオーバーしません。** 1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と All Other Traffic トンネルの状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

## はじめに {#getting-started}

このページを初めて開いたとき、まだトンネルが作成されていない場合は、以下のような画面が表示されます。**Add VPN Tunnel** をクリックして開始します。

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**VPNプロバイダーを選択** します。ここに表示されるVPNプロバイダーは、GL.iNet ルーターの Web管理パネルに統合されています。有効なサブスクリプションがあれば、認証情報を入力するだけでログインし、VPN接続用の設定ファイルを取得できます。

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

他のVPNプロバイダーを利用している場合や、独自のVPN設定をアップロードしたい場合は、**VPN Client Profile** に移動して手動で設定してください。

ここでは **Hide.me** を例に説明します。Hide.me の認証情報でログインします。

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**VPNサーバーを選択** します。ここで選択したサーバーが、このVPNトンネル経由で接続する先になります。公開IPアドレスは、選択したサーバーの所在地からアクセスしているように見えます。**Apply** をクリックします。

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

自動的に接続が開始されます。**Done** をクリックします。

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

VPN Dashboard に移動すると、VPN Tunnel 1 が有効になり、接続済みであることを確認できます。

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**この例では、このルーターに接続されているすべてのクライアントが、このVPNトンネル経由でインターネットにアクセスします。**

VPNポリシーを設定する場合は、[VPNポリシー](#vpn-policy) を参照してください。

**All Other Traffic** は、VPN Dashboard の下部に表示される、あらかじめ有効なトンネルです。詳細は [こちら](#all-other-traffic) を参照してください。

## トンネル詳細 {#tunnel-details}

VPN Dashboard では、各VPNトンネルが下図のように表示されます。ルーティングルール、接続中のサーバー、トラフィック統計、サーバーアドレス、待受ポート、クライアント仮想IP、接続ログなどの詳細な情報を確認できます。トンネルグループ上部では、VPNトンネルの有効化・無効化やトンネル設定の変更も行えます。

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## VPNポリシー {#vpn-policy}

VPNポリシーでは、ネットワークトラフィックをVPNトンネル経由でどのようにルーティングするかを定義します。どのトラフィックをVPN経由でトラフィック宛先へ送るか、どのトラフィックをローカルWAN経由で直接インターネットへ出すかを決定します。

これにより、すべてのクライアントまたは特定のデバイスについて、指定したWebサイトやインターネット全体へのアクセスをVPN接続経由にでき、柔軟で安全なネットワーク管理を実現できます。

### クイックセットアップ

VPN Dashboard で **Add New Tunnel** をクリックするか、既存のVPNトンネルの中央部分をクリックします。

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

その後、セットアップウィザードに従って、VPNプロファイル、トラフィック送信元、トラフィック宛先を選択し、VPNポリシーを設定します。

1. **VPNプロファイルを選択します。**

    統合VPNサービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

    [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイルの一覧が表示されます。1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整してください。

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **注意**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) トンネルの状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

2. **クライアント送信元を選択します。**

    選択肢は4つあります。

    - **All Clients**: 選択すると、すべてのデバイスからのトラフィックがこのルールに一致します。
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: 選択すると、指定した接続タイプ（例: LAN subnet、Drop-in Gateway、Guest Network）からのトラフィックがこのルールに一致します。
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: 選択すると、指定したデバイス（MACアドレスで識別）からのトラフィックがこのルールに一致します。
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: 選択すると、指定したデバイス（MACアドレスで識別）からのトラフィックはこのルールに一致しません。
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **トラフィック宛先を選択します。**

    選択肢は3つあります。

    - **All Targets**: 選択すると、このルールに一致するトラフィックはすべての宛先へルーティングされます。
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは指定したドメインまたはIPアドレスへルーティングされます。内容は手動で入力する必要があります。
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは、指定したドメインまたはIPアドレスへルーティングされません。内容は手動で入力する必要があります。
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### 利用シナリオ

参考として、以下に2つのシナリオを手順付きで示します。

**シナリオ 1**

**目的:**

1. このルーターに接続された特定のデバイスだけがVPN経由でインターネットへアクセスし、それ以外のデバイスはローカルWAN経由でアクセスするようにします。

2. 選択したデバイスはVPN接続のみを使用する必要があります。VPNが予期せず切断された場合、DNSリークやIP追跡を防ぐため、それらのデバイスのインターネットアクセスはブロックされます。

**以下の手順でVPNポリシーを設定してください。**

1. VPNプロファイルを選択します。

    統合VPNサービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

    [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイルの一覧が表示されます。

    ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

    1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

    **注意**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) トンネルの状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

2. クライアント送信元として **Specified Devices** を選択し、VPNを使用するデバイスを選んで **Apply** をクリックします。

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. トラフィック宛先として **All Targets** を選択し、**Apply** をクリックします。

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. VPN Dashboard に戻ると、VPNトンネルが追加されています。

    ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. このトンネルの **Kill Switch** が有効になっていることを確認してください。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNSリークやIP追跡を防ぐためにブロックされます。

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}

6. **All Other Traffic** が有効で、モードが **Allow Non-VPN Traffic** になっていることを確認してください。これにより、上記のVPNトンネルに一致しないトラフィックでもローカルWAN経由でインターネットへアクセスできます。

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. スイッチを切り替えて、このトンネルを有効にします。

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. 接続が完了すると、VPNポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想IPアドレスなどのVPN接続情報が表示されます。

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

    これで、指定した2台のデバイスだけがVPN経由でインターネットへアクセスします。VPNが予期せず切断された場合、それらのデバイスのインターネットアクセスはDNSリークやIP追跡を防ぐためにブロックされます。それ以外のデバイスはローカルWAN経由でインターネットへアクセスします。

**シナリオ 2**

**目的:**

1. すべてのデバイスは、特定のソーシャルメディアおよびストリーミングサービスのドメインにアクセスするときは **VPN Tunnel 1** を使用し、それ以外のすべてのインターネットアクセスには **VPN Tunnel 2** を使用します。

2. VPNトンネルが予期せず切断された場合、DNSリークやIP追跡を防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

**以下の手順でVPNポリシーを設定してください。**

1. Tunnel 1 用のVPNプロファイルを選択します。

    統合VPNサービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

    [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイルの一覧が表示されます。

    ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}

    1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

    **注意**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) トンネルの状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

2. Tunnel 1 のクライアント送信元として **All Clients** を選択し、**Apply** をクリックします。

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Tunnel 1 のトラフィック宛先として **Specified Domain / IP List** を選択します。下図のように、一般的なソーシャルメディアおよびストリーミングサービスのドメインを入力して **Apply** をクリックします。

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. VPN Dashboard に戻ると、Tunnel 1 が追加されています。

    ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Tunnel 1 の **Kill Switch** が有効になっていることを確認してください。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNSリークやIP追跡を防ぐためにブロックされます。

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}

6. **Add New Tunnel** をクリックして Tunnel 2 を追加します。

    ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Tunnel 2 用のVPNプロファイルを選択します。

    統合VPNサービスの認証情報でログインしているか、設定ファイルをアップロードしている場合、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** に移動し、認証情報でログインするか設定ファイルを手動でアップロードしてください。

    [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイルの一覧が表示されます。

    ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}

    1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

    ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

    **注意**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続が確立されるまで順に切り替えます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) トンネルの状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

8. Tunnel 2 のクライアント送信元として **All Clients** を選択し、**Apply** をクリックします。

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Tunnel 2 のトラフィック宛先として **All Targets** を選択し、**Apply** をクリックします。

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. VPN Dashboard に戻ると、Tunnel 2 が追加されています。

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Tunnel 2 の **Kill Switch** が有効になっていることを確認してください。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNSリークやIP追跡を防ぐためにブロックされます。

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. **All Other Traffic** を無効にし、モードが **Enhanced Kill Switch** になっていることを確認してください。これにより、すべてのトラフィックがVPN経由でのみインターネットへアクセスするようになります。

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. スイッチを切り替えて、Tunnel 1 と Tunnel 2 を有効にします。

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. 接続が完了すると、VPNポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想IPアドレスなどのVPN接続情報が表示されます。

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    これで、指定したドメインへアクセスするときはすべてのデバイスが **VPN Tunnel 1** を使用し、それ以外のインターネットアクセスには **VPN Tunnel 2** を使用します。VPNトンネルが予期せず切断された場合、すべてのデバイスのインターネットアクセスはDNSリークやIP追跡を防ぐためにブロックされます。

## その他のすべてのトラフィック {#all-other-traffic}

このオプションは、上記のVPNトンネルグループのいずれにも一致しないトラフィックがインターネットへアクセスできるかどうかを制御します。VPN経由でルーティングされないトラフィックでも通常どおりインターネットへアクセスできるよう、デフォルトで有効になっています。

有効な場合、一致しないトラフィックも引き続きインターネットへアクセスできます。

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

無効な場合、VPN経由でルーティングされたトラフィックだけがインターネットへアクセスできます。非VPNトラフィックと、VPN接続からフェイルオーバーしたトラフィックはすべてブロックされます。この設定は、各VPNトンネルの個別の Kill Switch を上書きしません。

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## トンネル優先度 {#tunnel-priority}

トンネル優先度を調整するには、トンネルグループの歯車アイコンをクリックし、**Sort** を選択します。

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

右側の三本線アイコンをクリックしたままドラッグしてトンネルの順序を変更し、**Apply** をクリックします。

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは次のルールに従ってトラフィックをルーティングします。**

1. まず最優先のトンネルルールへの一致を試みます。一致した場合はそのトンネル経由でルーティングされ、一致しない場合は次の優先度のトンネルを順に試します。

2. 各トンネルグループは独立して動作します。いったんトンネルルールに一致したトラフィックは、そのトンネル経由でルーティングされ、トンネルグループ間でフェイルオーバーは行われません。

3. 各トンネルグループ内では複数のプロファイルを選択でき、トンネル内フェイルオーバーを有効にできます。トンネルグループ内で最優先のプロファイルが停止した場合、トンネルは自動的に次順位のプロファイルで接続を試みます。

4. VPNトンネルが予期せず切断された場合、このトンネルの **Kill Switch** が有効かどうかに応じて、トラフィックを All Other Traffic トンネルへフェイルオーバーするかどうかが決まります。

    - Kill Switch が有効な場合、トラフィックはブロックされ、All Other Traffic トンネルへはフェイルオーバーしません。
    - Kill Switch が無効な場合、トラフィックは All Other Traffic トンネルへフェイルオーバーします。

5. **All Other Traffic** トンネルはデフォルトで有効になっており、VPNトンネルに一致しないトラフィックでもインターネットへアクセスできるようになっています。

    - 有効な場合、一致しないトラフィックやフェイルオーバートラフィックはローカルWAN経由でルーティングされます。
    - 無効な場合、キルスイッチが強化され、IPリークを防ぐため通常のインターネットアクセスがブロックされます。

## トンネルオプション {#tunnel-options}

各VPNトンネルでは、VPNキルスイッチ、IPマスカレーディング、MTU などの詳細設定を行えます。

トンネルグループの歯車アイコンをクリックし、**Options** を選択します。

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、このVPNトンネルに一致するトラフィックは、VPN接続が予期せず切断された場合にブロックされます。無効にすると、そのトラフィックは **All Other Traffic** トンネルへフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスはVPNトンネル経由でパケットを送信します。これらのサービスは通常デバイスの実IPアドレスを必要とするため、このオプションはデフォルトで無効です。

- **Allow Remote Access to the LAN Subnet**: 有効にすると、VPN経由でこのルーターおよびLAN内デバイスにリモートアクセスできます。VPNサーバー側で、そのLANサブネットへの戻りルートが通知されている必要があります。

- **IP Masquerading**: 有効にすると、LANクライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモートピアがLANサブネットを認識している Site-to-Site 構成の場合にのみ無効にしてください。

- **MTU**: ここで設定したMTU値は、設定ファイル内のMTU設定を上書きします。

---

まだご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
