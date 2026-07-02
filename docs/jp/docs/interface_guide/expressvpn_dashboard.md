# ExpressVPN Dashboard

> **Note:** このガイドは、GL.iNet x ExpressVPN共同ブランドルーター **Fortify** にのみ適用されます。

[ExpressVPN](https://www.expressvpn.com/){target="_blank"}は、オンラインプライバシーの保護、インターネット接続の安全性向上、グローバルコンテンツへのアクセスを目的とした、世界有数のプレミアムVPNサービスです。高速通信、強力な暗号化、100か国以上のサーバーへのアクセスを提供します。ストリーミング、プライベートなブラウジング、公共Wi-Fiでのデータ保護など、ExpressVPNは高速で安全な利用体験を提供します。

**Fortify**は、GL.iNetとExpressVPNが共同でリリースした共同ブランドルーターです。各製品には、1年間のExpressVPN無料サブスクリプションが付属しています。ユーザーはルーターのWeb管理パネルから直接サブスクリプションを引き換え、アカウントを紐付けることができます。アクティベーション後、ルーターを通過するすべてのトラフィックはExpressVPNの高速ネットワークと強力な暗号化を利用し、ネットワーク接続全体とオンラインプライバシーを保護します。

このガイドでは、ルーターのWeb管理パネル内で12か月のExpressVPNプランを引き換える手順を説明します。また、利用シーンや要件に応じてVPNポリシーをカスタマイズし、暗号化された安全で高速なインターネット接続を利用する方法も説明します。

## はじめに

### ExpressVPNプランを引き換える

FortifyのWeb管理パネルにログインし、**VPN** -> **VPN Client Profile**に移動します。

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/2-vpn_client_profile.png){class="glboxshadow"}

**Terms of Service**と**Privacy Policy**を読み、同意してから**Get Started**をクリックします。

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/2-get_started.png){class="glboxshadow"}

**Claim 12-Month Plan**をクリックします。

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/2-claim_plan.png){class="glboxshadow"}

ポップアップウィンドウで**Order ID**を入力します。このルーターをGL.iNet Storeで購入した場合は、**Order Email**も必要です。その後、**Continue to ExpressVPN**をクリックします。

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/3-amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/3-store_order_email.png){class="glboxshadow"}

ExpressVPN Checkoutにリダイレクトされます。右側に引き換えコードが適用され、追加料金なしで12か月のサブスクリプションが有効になります。

上部にメールアドレスを入力し、初回期間終了後もVPNアクセスを継続できるよう支払い方法を追加します。その後、**Subscribe with Card**をクリックします。

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/4-expressvpn_checkout1.png){class="glboxshadow"}

**Activation Link**がメールアドレスに送信されます。受信トレイを開き、手順に従ってExpressVPNアカウントを有効化します。

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/4-expressvpn_checkout2.png){class="glboxshadow"}

メール内のアクティベーションリンクをクリックし、パスワードを作成してアカウントを有効化します。

![create password](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/5-create_password(1).png){class="glboxshadow"}

アカウントが正常に有効化されました。FortifyルーターのWeb管理パネルに戻り、VPNトンネルを追加してください。

![my account](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/7-my_account(1).png){class="glboxshadow"}

### VPNトンネルを追加する

以下の手順に従ってVPNトンネルを追加し、VPNポリシーを設定します。必要に応じて[ケースリファレンス](#case-reference)を参照してください。

1. FortifyのWeb管理パネルにログインし、**VPN** -> **ExpressVPN Dashboard**に移動します。**Add VPN Tunnel**をクリックします。

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. VPNプロファイルを選択し、**Next**をクリックします。

    ExpressVPNプロファイルの一覧が表示されます。1つまたは複数のプロファイルを選択し、必要に応じて右側で優先順位を調整します。

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        複数のプロファイルを選択した場合、トンネルは接続が確立されるまで優先順位に従って各プロファイルで接続を試みます。1つのトンネル内のすべてのプロファイルが接続に失敗した場合、システムは[トンネルオプション](#tunnel-options)と[All Other Traffic](#all-other-traffic)設定のKill Switchの状態に基づいて、ルーターのローカルネットワーク（WAN）へ切り替えるかどうかを判断します。

3. クライアント送信元を選択し、**Next**をクリックします。

    4つのオプションがあります。

    - **All Clients**: 選択すると、すべてのデバイスからのトラフィックがこのルールに一致します。
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types**: 選択すると、指定した接続タイプ（LANサブネット、Drop-in Gateway、ゲストネットワークなど）からのトラフィックがこのルールに一致します。
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices**: 選択すると、指定したデバイス（MACアドレスで識別）からのトラフィックがこのルールに一致します。
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: 選択すると、指定したデバイス（MACアドレスで識別）からのトラフィックはこのルールに一致しません。
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. 宛先を選択し、**Apply**をクリックします。

    3つのオプションがあります。

    - **All Targets**: 選択すると、このルールに一致するトラフィックはすべての宛先へルーティングされます。
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは指定したドメインまたはIPアドレスへルーティングされます。手動で入力する必要があります。
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: 選択すると、このルールに一致するトラフィックは指定したドメインまたはIPアドレスへルーティングされません。手動で入力する必要があります。
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. VPNトンネルが正常に追加されました。**ExpressVPN Dashboard**に移動します。必要に応じてVPNトンネルを追加してください。

### ケースリファレンス {#case-reference}

参考として、2つの代表的な設定ケースと手順を示します。

**ケース1**: 指定したデバイスのみをVPN経由でルーティングする。

<u>要件</u>:

1. このルーターに接続された特定のデバイスのみがVPN経由でインターネットにアクセスします。他のすべてのデバイスはローカルWAN経由でインターネットにアクセスします。

2. 選択したデバイスはVPN接続のみを使用する必要があります。VPNが予期せず切断された場合、DNSリークとIPトラッキングを防ぐため、これらのデバイスのインターネットアクセスはブロックされます。

<u>設定手順</u>:

1. VPNプロファイルを選択します。

    1つまたは複数のプロファイルを選択し、必要に応じて右側で優先順位を調整してから、**Next**をクリックします。

    ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

2. クライアント送信元を選択します。

    **Specified Devices**タブをクリックし、VPNを使用するデバイスを選択してから**Next**をクリックします。

    ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

3. 宛先を選択します。

    **All Targets**タブをクリックし、トラフィック宛先として設定してから**Apply**をクリックします。

    ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

4. ExpressVPN Dashboardに移動します。以下のようにVPNトンネルが正常に追加されました。

    ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

5. このトンネルの**Kill Switch**が有効になっていることを確認します。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNSリークとIPトラッキングを防ぐためにブロックされます。

    ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

    ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}
    
6. **Allow Non-VPN Traffic**が有効になっていることを確認します。これはデフォルトで有効になっており、VPNトンネルに一致しないトラフィックがローカルWANネットワーク経由で引き続きインターネットにアクセスできるようにします。

    ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

7. 中央のボタンをクリックして、このトンネルを有効化します。

    ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

8. 接続後、ページにはVPN接続の詳細（VPNポリシー、クライアント仮想IP、サーバーアドレス、待受ポート、トラフィック統計など）が表示されます。

    ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

    これで、指定した2台のデバイスのみがVPN経由でインターネットにアクセスします。VPNが予期せず切断された場合、DNSリークとIPトラッキングを防ぐため、これらのデバイスのインターネットアクセスはブロックされます。他のすべてのデバイスはローカルWANネットワーク経由でインターネットにアクセスします。

**ケース2**: 特定のWebサイトへのアクセスはすべてのデバイスでVPN 1を使用し、残りのインターネットトラフィックはVPN 2を使用する。

<u>要件</u>:

1. すべてのデバイスは、特定のSNSおよびストリーミングサービスのWebサイトへアクセスするときにVPN Tunnel 1を使用し、その他すべてのインターネットアクセスにはVPN Tunnel 2を使用します。

2. VPNトンネルが予期せず切断された場合、DNSリークとIPトラッキングを防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

<u>設定手順</u>:

1. Tunnel 1のVPNプロファイルを選択します。

    1つまたは複数のプロファイルを選択し、必要に応じて右側で優先順位を調整してから、**Next**をクリックします。

    ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

2. クライアント送信元を選択します。

    **All Clients**タブをクリックし、Tunnel 1のクライアント送信元として設定してから**Next**をクリックします。

    ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

3. 宛先を選択します。

    **Specified Domain / IP List**タブをクリックし、以下のように特定のSNSおよびストリーミングサービスのドメインを入力してから、**Apply**をクリックします。

    ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

4. ExpressVPN Dashboardに移動します。VPN Tunnel 1が正常に追加されました。

    ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

5. Tunnel 1の**Kill Switch**が有効になっていることを確認します。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNSリークとIPトラッキングを防ぐためにブロックされます。

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}
    
6. **Add New Tunnel**をクリックしてTunnel 2を追加します。

    ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

7. Tunnel 2のVPNプロファイルを選択します。

    1つまたは複数のプロファイルを選択し、必要に応じて右側で優先順位を調整してから、**Next**をクリックします。

    ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

8. クライアント送信元を選択します。

    **All Clients**タブをクリックし、Tunnel 2のクライアント送信元として設定してから**Next**をクリックします。

    ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

9. 宛先を選択します。

    **All Targets**タブをクリックし、Tunnel 2のトラフィック宛先として設定してから**Apply**をクリックします。

    ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

10. VPN Dashboardに移動します。VPN Tunnel 2が正常に追加されました。

    ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

11. Tunnel 2の**Kill Switch**が有効になっていることを確認します。VPNが予期せず切断された場合、このトンネルに一致するトラフィックのインターネットアクセスは、DNSリークとIPトラッキングを防ぐためにブロックされます。

    ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

    ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

12. 右上の歯車アイコンをクリックし、**Enhanced Kill Switch**を有効にして**Apply**をクリックします。これにより、すべてのトラフィックがVPN経由でインターネットにアクセスする必要があります。

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

13. 中央のボタンをクリックしてTunnel 1とTunnel 2を有効化します。

    ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

14. 接続後、ページにはVPN接続の詳細（VPNポリシー、クライアント仮想IP、サーバーアドレス、待受ポート、トラフィック統計など）が表示されます。

    ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

    これで、すべてのデバイスは指定したドメインへアクセスするときに**VPN Tunnel 1**を使用し、その他すべてのインターネットアクセスには**VPN Tunnel 2**を使用します。VPNトンネルが予期せず切断された場合、DNSリークとIPトラッキングを防ぐため、すべてのデバイスのインターネットアクセスはブロックされます。

## Kill Switch

Kill SwitchはVPN接続のセキュリティ機能です。VPN接続が予期せず切断された場合、ローカルネットワークのすべてのインターネットアクセスを自動的に遮断し、実際のIPアドレスやオンラインデータの露出を防ぎ、継続的なプライバシーとセキュリティを確保します。この機能は、公共ネットワークの利用、機密データの処理、実際のIPアドレスの非表示など、安全で匿名性の高いインターネットアクセスを維持する場合に特に役立ちます。

有効にすると、VPNトンネルを迂回しようとするクライアントトラフィックをブロックし、DNS設定の問題、予期しない切断、直接IPリクエストなどによって発生するVPNリークを防ぎます。

Fortifyは、グローバルVPN接続と個別のVPNトンネルの両方でKill Switch設定をサポートしています。

- グローバルVPN接続（Enhanced Kill Switch）のKill Switchを設定するには、[All Other Traffic](#all-other-traffic)を参照してください。

- 個別のVPNトンネルごとにKill Switchを設定するには、[トンネルオプション](#tunnel-options)を参照してください。

## All Other Traffic

右上の歯車アイコンをクリックして、VPNトンネルに一致しないトラフィックのポリシーを設定します。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

このポリシーは、VPNトンネルグループのいずれにも一致しないトラフィックがインターネットにアクセスできるかどうかを制御します。利用可能なオプションは**Allow Non-VPN Traffic**と**Enhanced Kill Switch**の2つです。

- **Allow Non-VPN Traffic**: 非VPNトラフィックの通常のインターネットアクセスを確保するため、デフォルトで有効になっています。

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: すべてのデバイスにVPN経由でのインターネットアクセスを強制します。VPNトンネルに一致しないトラフィックはブロックされます。このグローバル設定は、個別のVPNトンネルに設定されたKill Switchを上書きしません。

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## トンネルオプション {#tunnel-options}

各VPNトンネルに対して、VPN Kill Switch、IPマスカレーディング、MTUなどの詳細設定を構成できます。

トンネルグループ内の歯車アイコンをクリックし、**Options**を選択します。

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: 有効にすると、VPN接続が予期せず失敗した場合、このVPNトンネルに一致するトラフィックはブロックされます。無効にすると、そのトラフィックは**All Other Traffic**トンネルへフェイルオーバーします。

- **Services from GL.iNet Use VPN**: 有効にすると、GoodCloud、DDNS、rttyサービスはVPNトンネル経由でパケットを送信します。このオプションはデフォルトで無効です。これらのサービスは通常、正常に動作するためにデバイスの実IPアドレスを必要とするためです。

- **Allow Remote Access to the LAN Subnet**: 有効にすると、VPN経由でこのルーターおよびLANデバイスへのリモートアクセスが許可されます。VPNサーバーが自身のLANサブネットへの戻りルートを広告する必要があります。

- **IP Masquerading**: 有効にすると、LANクライアントの送信元IPアドレスはルーターのVPNトンネルIPに書き換えられます。リモートピアがLANサブネットを認識しているサイトツーサイト構成の場合のみ無効にしてください。

- **MTU**: トンネルに設定したMTU値は、設定ファイル内のMTU設定を上書きします。

## トンネル優先順位

トンネルの優先順位を調整するには、トンネルグループ内の歯車アイコンをクリックし、**Priority**を選択します。

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

右側の三本線アイコンをクリックしたままドラッグしてトンネルの順序を変更し、**Apply**をクリックします。

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

**複数のトンネルが有効な場合、ルーターは次のルールに従ってトラフィックをルーティングします**:

1. トラフィックはまず、最も優先順位の高いトンネルルールとの一致を試みます。一致した場合はそのトンネル経由でルーティングされ、一致しない場合は次の優先順位のトンネルを試し、以降同様に処理します。

2. 各トンネルグループは独立して動作します。トラフィックがトンネルルールに一致すると、そのトンネル経由でルーティングされ、トンネルグループ間でフェイルオーバーしません。

3. 各トンネルグループ内で複数のプロファイルを選択すると、トンネル内フェイルオーバーを有効にできます。トンネルグループ内で最も優先順位の高いプロファイルがダウンした場合、トンネルは次に優先順位の高いプロファイルを使用して自動的に接続します。

4. VPNトンネルが予期せず切断された場合、システムはこのトンネルの**Kill Switch**が有効かどうかに基づいて、トラフィックをAll Other Trafficトンネルへフェイルオーバーするかどうかを判断します。

    - Kill Switchが有効な場合、トラフィックはブロックされ、All Other Trafficトンネルへフェイルオーバーしません。
    - Kill Switchが無効な場合、トラフィックはAll Other Trafficトンネルへフェイルオーバーします。

5. **All Other Traffic**トンネルでは、VPNトンネルに一致しないトラフィックがインターネットにアクセスできるかどうかを、モードによって決定します。

    - **Allow Non-VPN Traffic**: VPNトンネルに一致しないトラフィックがローカルWAN経由で引き続きインターネットにアクセスできるよう、デフォルトで有効になっています。

    - **Enhanced Kill Switch**: すべてのデバイスにVPN経由でのインターネットアクセスを強制します。VPNトンネルに一致しないトラフィックはブロックされます。このグローバル設定は、個別のVPNトンネルに設定されたKill Switchを上書きしません。つまり、Kill Switchを強化し、通常のインターネットアクセスをブロックしてIPリークを防ぎます。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
