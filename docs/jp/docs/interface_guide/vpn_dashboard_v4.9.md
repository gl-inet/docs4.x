# VPN Dashboard（ファームウェア v4.9）

**Note**: このガイドはファームウェア v4.9 を基準にしています。旧バージョンについては [こちら](vpn_dashboard.md) を参照してください。

---

Web管理パネルの左側で、**VPN** -> **VPN Dashboard** に移動します。

VPN Dashboardでは、ルーティングルール、接続中のサーバー、トラフィック統計、クライアント仮想IP、接続ログなどのVPN接続情報を確認できるほか、Kill Switch、IP Masquerading、MTU などの詳細設定も行えます。

ファームウェアv4.8と比べて、v4.9のVPNダッシュボードには以下の改善があります。

1. **1つのトンネルグループ内で複数のプロファイルを選択し、その優先度を設定できるようになりました。** トンネルは優先度順に各プロファイルで接続を試み、接続に成功した時点で確立されます。

2. **各トンネルグループは独立して動作し、グループ間でフェイルオーバーしません。** 1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と **All Other Traffic** の状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

## はじめに

このページを初めて開いた時点でトンネルがまだ作成されていない場合、以下のように表示されます。**Add VPN Tunnel** をクリックして開始します。

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**VPNプロバイダーを選択** してください。ここに表示されるVPNプロバイダーは、GL.iNetルーターのWeb管理パネルに統合されています。有効なサブスクリプションがあれば、認証情報を入力するだけでログインし、VPN接続用の設定ファイルを取得できます。

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

他のVPNプロバイダーを利用している場合や、自分のVPN設定ファイルをアップロードしたい場合は、**VPN Client Profile** で手動設定してください。

ここでは **Hide.me** を例に説明します。Hide.me の認証情報でログインします。

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**VPNサーバーを選択** します。ここで選ぶサーバーが、このVPNトンネル経由で接続される先になります。公開IPアドレスは、選択したサーバーの所在地からアクセスしているように見えます。**Apply** をクリックしてください。

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

接続は自動的に開始されます。**Done** をクリックします。

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

VPN Dashboard へ移動すると、VPN Tunnel 1 が有効になり、接続済みであることを確認できます。

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**この例では、このルーターに接続されたすべてのクライアントがこのVPNトンネル経由でインターネットにアクセスします。**

VPNポリシーを設定したい場合は、[VPNポリシー](#vpn-policy)を参照してください。

**All Other Traffic** は、VPN Dashboard の下部に表示される、あらかじめ有効なトンネルです。詳細は[こちら](#all-other-traffic)を参照してください。

## トンネル詳細

VPN Dashboard では、各VPNトンネルが以下のように表示されます。ルーティングルール、接続中のサーバー、トラフィック統計、サーバーアドレス、待受ポート、クライアント仮想IP、接続ログなど、詳細な情報を確認できます。トンネルグループ上部では、VPNトンネルの有効化または無効化、および設定変更が可能です。

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## VPNポリシー

VPNポリシーでは、ネットワークトラフィックをVPNトンネル経由でどのようにルーティングするかを定義します。どの通信をVPN経由でトラフィック宛先へ送るか、どの通信をローカルWAN経由で直接インターネットへ出すかを決められます。

これにより、すべてのクライアントまたは特定のデバイスについて、指定したWebサイトやインターネット全体へのアクセスをVPN経由にするなど、柔軟で安全なネットワーク管理が可能になります。

### クイックセットアップ

VPN Dashboard で **Add New Tunnel** をクリックするか、既存のVPNトンネルの中央部分をクリックします。

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

その後、セットアップウィザードに従って、VPNプロファイル、トラフィック送信元、トラフィック宛先を選択し、VPNポリシーを設定します。

1. **VPNプロファイルを選択します。**

   統合VPNサービスの認証情報でログインしている場合、または設定ファイルをアップロード済みの場合は、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** でログインするか、設定ファイルをアップロードしてください。

   ここでは [Hide.me](https://hide.me/en/?friend=glinet){target="\_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイル一覧が表示されます。1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整してください。

   ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

   **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続に成功した時点で確立されます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

2. **トラフィック送信元を選択します。**

   選べるオプションは4つあります。
   - **All Clients**: すべてのデバイスからのトラフィックがこのルールに一致します。
     ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

   - **Specified Connection Types**: 指定した接続タイプ（例: LANサブネット、Drop-in Gateway、ゲストネットワーク）からのトラフィックがこのルールに一致します。
     ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

   - **Specified Devices**: 指定したデバイス（MACアドレスで識別）からのトラフィックがこのルールに一致します。
     ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

   - **Exclude Specified Devices**: 指定したデバイス（MACアドレスで識別）からのトラフィックはこのルールに一致しません。
     ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **トラフィック宛先を選択します。**

   選べるオプションは3つあります。
   - **All Targets**: このルールに一致するトラフィックは、すべての宛先へルーティングされます。
     ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

   - **Specified Domain / IP List**: このルールに一致するトラフィックは、指定したドメインまたはIPアドレスへルーティングされます。内容は手動で入力します。
     ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

   - **Exclude specified Domain / IP List**: このルールに一致するトラフィックは、指定したドメインまたはIPアドレスへはルーティングされません。内容は手動で入力します。
     ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### 利用シナリオ

以下に、参考用として2つのシナリオを手順付きで示します。

**シナリオ 1**

**目的:**

1. このルーターに接続された特定のデバイスのみがVPN経由でインターネットへアクセスし、それ以外のデバイスはローカルWAN経由でアクセスするようにします。

2. 選択したデバイスはVPN接続のみを使用する必要があります。VPNが予期せず切断された場合、DNSリークやIP追跡を防ぐため、それらのデバイスのインターネットアクセスはブロックされます。

**以下の手順でVPNポリシーを設定してください。**

1. VPNプロファイルを選択します。

   統合VPNサービスの認証情報でログインしている場合、または設定ファイルをアップロード済みの場合は、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** でログインするか、設定ファイルをアップロードしてください。

   ここでは [Hide.me](https://hide.me/en/?friend=glinet){target="\_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイル一覧が表示されます。

   ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

   1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

   ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

   **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続に成功した時点で確立されます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

2. トラフィック送信元として **Specified Devices** を選択し、VPNを利用させるデバイスを選んで **Apply** をクリックします。

   ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. トラフィック宛先として **All Targets** を選択し、**Apply** をクリックします。

   ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. VPN Dashboard へ戻ると、新しいVPNトンネルが追加されています。

   ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. このトンネルの **Kill Switch** が有効になっていることを確認してください。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスはDNSリークやIP追跡を防ぐためにブロックされます。

   ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

   ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}

6. **All Other Traffic** が有効で、モードが **Allow Non-VPN Traffic** になっていることを確認してください。これにより、上記のVPNトンネルに一致しないトラフィックはローカルWAN経由でインターネットへアクセスできます。

   ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. スイッチを切り替えて、このトンネルを有効にします。

   ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. 接続が完了すると、VPNポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想IPアドレスなどの情報が表示されます。

   ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

   これで、指定した2台のデバイスだけがVPN経由でインターネットにアクセスし、VPNが予期せず切断された場合にはそれらのデバイスの通信がブロックされます。それ以外のデバイスはローカルWAN経由で通信します。

**シナリオ 2**

**目的:**

1. すべてのデバイスは、特定のソーシャルメディアおよびストリーミングサービスのドメインにアクセスする際には **VPNトンネル1** を使用し、それ以外のすべてのインターネットアクセスには **VPNトンネル2** を使用します。

2. VPNトンネルが予期せず切断された場合、DNSリークやIP追跡を防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

**以下の手順でVPNポリシーを設定してください。**

1. トンネル1用のVPNプロファイルを選択します。

   統合VPNサービスの認証情報でログインしている場合、または設定ファイルをアップロード済みの場合は、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** でログインするか、設定ファイルをアップロードしてください。

   ここでは [Hide.me](https://hide.me/en/?friend=glinet){target="\_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイル一覧が表示されます。

   ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}

   1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

   ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

   **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続に成功した時点で確立されます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

2. トンネル1の送信元として **All Clients** を選択し、**Apply** をクリックします。

   ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. トンネル1の宛先として **Specified Domain / IP List** を選択し、一般的なソーシャルメディアおよびストリーミングサービスのドメインを入力して、**Apply** をクリックします。

   ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. VPN Dashboard へ戻ると、Tunnel 1 が追加されています。

   ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Tunnel 1 の **Kill Switch** が有効になっていることを確認してください。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスはDNSリークやIP追跡を防ぐためにブロックされます。

   ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

   ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}

6. **Add New Tunnel** をクリックして、Tunnel 2 を追加します。

   ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. トンネル2用のVPNプロファイルを選択します。

   統合VPNサービスの認証情報でログインしている場合、または設定ファイルをアップロード済みの場合は、利用可能なプロファイルがここに表示されます。まだ何もない場合は、**VPN Client Profile** でログインするか、設定ファイルをアップロードしてください。

   ここでは [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="\_blank"} を例にします。サービス認証情報でログインすると、VPNプロファイル一覧が表示されます。

   ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}

   1つまたは複数のプロファイルを選択し、必要に応じて右側で優先度を調整します。

   ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

   **Note**: 複数のプロファイルを選択した場合、トンネルは優先度順に各プロファイルで接続を試み、接続に成功した時点で確立されます。1つのトンネル内のすべてのプロファイルで接続に失敗した場合、システムは Tunnel Kill Switch と [All Other Traffic](#all-other-traffic) の状態に基づいて、ローカルWANへ切り替えるかどうかを判断します。

8. トンネル2の送信元として **All Clients** を選択し、**Apply** をクリックします。

   ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. トンネル2の宛先として **All Targets** を選択し、**Apply** をクリックします。

   ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. VPN Dashboard へ戻ると、Tunnel 2 が追加されています。

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Tunnel 2 の **Kill Switch** が有効になっていることを確認してください。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスはDNSリークやIP追跡を防ぐためにブロックされます。

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. **All Other Traffic** を無効にし、モードが **Enhanced Kill Switch** になっていることを確認してください。これにより、すべてのトラフィックがVPN経由でのみインターネットへアクセスするようになります。

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. スイッチを切り替えて、トンネル1とトンネル2を有効にします。

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. 接続が完了すると、VPNポリシー、トラフィック統計、サーバーアドレス、待受ポート、仮想IPアドレスなどの情報が表示されます。

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    これで、指定したドメインへのアクセス時はすべてのデバイスが **VPNトンネル1** を使用し、それ以外のインターネットアクセスでは **VPNトンネル2** を使用します。VPNトンネルが予期せず切断された場合、すべてのデバイスの通信はDNSリークやIP追跡を防ぐためにブロックされます。

## その他のすべてのトラフィック

このオプションは、上記のVPNトンネルグループに一致しないトラフィックがインターネットへアクセスできるかどうかを制御します。VPNを経由しないトラフィックでも通常どおり通信できるよう、デフォルトで有効になっています。

有効な場合、一致しないトラフィックも引き続きインターネットへアクセスできます。

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

無効な場合、VPN経由でルーティングされたトラフィックだけがインターネットへアクセスできます。非VPNトラフィックと、VPN接続からフェイルオーバーしたトラフィックはすべてブロックされます。この設定は、各VPNトンネル個別のキルスイッチを上書きするものではありません。

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## トンネル優先度

トンネル優先度を変更するには、トンネルグループの歯車アイコンをクリックし、**Sort** を選択します。

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

右側の三本線アイコンをドラッグしてトンネルの順序を変更し、**Apply** をクリックします。

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは以下のルールに従ってトラフィックをルーティングします。**

1. トラフィックはまず最優先のトンネルルールに一致するかを確認します。一致した場合はそのトンネルを通ります。一致しない場合は次の優先度のトンネルを試します。

2. 各トンネルグループは独立して動作します。いったんトンネルルールに一致したトラフィックは、そのトンネルを経由してルーティングされ、トンネルグループ間でフェイルオーバーは行われません。

3. 各トンネルグループでは複数のプロファイルを選択でき、トンネル内フェイルオーバーを有効にできます。最優先のプロファイルがダウンした場合、トンネルは自動的に次順位のプロファイルで接続を試みます。

4. VPNトンネルが予期せず切断された場合、このトンネルの **Kill Switch** が有効かどうかに応じて、**All Other Traffic** へフェイルオーバーするかが決まります。
   - Kill Switch が有効な場合、トラフィックはブロックされ、**All Other Traffic** へはフェイルオーバーしません。
   - Kill Switch が無効な場合、トラフィックは **All Other Traffic** へフェイルオーバーします。

5. **All Other Traffic** はデフォルトで有効になっており、VPNトンネルに一致しないトラフィックでもインターネットへアクセスできるようにします。
   - 有効な場合、一致しないトラフィックやフェイルオーバートラフィックはローカルWAN経由でルーティングされます。
   - 無効な場合、キルスイッチが強化され、IPリーク防止のため通常のインターネットアクセスがブロックされます。

## トンネルオプション

各VPNトンネルでは、Kill Switch、IP Masquerading、MTU などの詳細設定を行えます。

トンネルグループの歯車アイコンをクリックし、**Options** を選択します。

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、このVPNトンネルに一致するトラフィックは、VPN接続が予期せず切断された場合にブロックされます。無効にすると、そのトラフィックは **All Other Traffic** へフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rtty の各サービスはVPNトンネル経由で通信します。これらのサービスは通常デバイスの実IPアドレスを必要とするため、この設定はデフォルトで無効です。

- **Allow Remote Access to the LAN Subnet**: 有効にすると、VPN経由でこのルーターおよびLAN内デバイスへリモートアクセスできます。VPNサーバー側で、LANサブネットへの戻りルートが通知されている必要があります。

- **IP Masquerading**: 有効にすると、LANクライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモート側がLANサブネットを認識しているSite-to-Site構成の場合にのみ無効にしてください。

- **MTU**: ここで設定したMTU値は、設定ファイル内のMTU設定を上書きします。

---

まだご質問がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
