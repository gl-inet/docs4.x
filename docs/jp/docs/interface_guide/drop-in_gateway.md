# ドロップインゲートウェイ

Web Admin Panel の左側で、**NETWORK** -> **Drop-in Gateway** に移動します。

Drop-in Gateway は、既存のプライマリルーターを置き換えたり再設定したりせずに、機能を拡張できる仕組みです。GL.iNet ルーターをプライマリルーターに Ethernet ケーブルで接続することで、既存のネットワーク構成に次のような高度な機能を追加できます。

- AdGuard Home で広告をフィルタリングする
- VPN クライアントを有効にする
- 暗号化 DNS を使用する

十分なメモリを搭載した高性能ルーターまたはセキュリティゲートウェイ（例: GL-MT2500、GL-MT5000）の使用を推奨します。必要に応じて、追加のトラフィック転送・制御ツールをインストールしてください。

## ネットワークトポロジー

Drop-in Gateway は中間ネットワークとして動作し、クライアントデバイスからのトラフィックを GL.iNet ルーターで処理した後、プライマリルーター経由で送信します。この過程では、既存のネットワーク設定（SSID やパスワードなど）を維持して接続済みデバイスの継続利用を可能にしつつ、必要に応じてすべての、または特定のクライアントデバイスのトラフィックを管理できます。

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

上の図には、灰色の線と、3 つの矢印および番号が付いた緑色の線の 2 種類があります。

1. **灰色の線** は物理的な接続構成を示しています。クライアントデバイス（例: コンピューター、ノート PC）はプライマリルーターに接続され、プライマリルーターの LAN ポートは Ethernet ケーブルで Drop-in Gateway を有効にした GL.iNet ルーターの WAN ポートに接続されます。

2. **緑色の線** は、Drop-in Gateway が有効なときのデータ転送経路を順番に示しています。番号付きの矢印はトラフィックの流れを表します。

    1. クライアントデバイスからのトラフィックは、まずプライマリルーターへ送られます。

    2. プライマリルーターは、そのトラフィックを GL.iNet ルーターへ転送して処理させます（例: 広告フィルタリング、VPN 暗号化）。

    3. 処理後のトラフィックはプライマリルーターへ戻され、最終的に元のクライアントデバイスへ届けられるか、インターネットへ送信されます。

## セットアップ

用途に応じて 2 つの展開方法があります。すべてのクライアントデバイスを Drop-in Gateway 経由にする方法と、特定のクライアントデバイスだけを Drop-in Gateway 経由にする方法です。

以下の例では、プライマリルーターのゲートウェイアドレスを `192.168.1.1` としています。

### すべてのデバイスを Drop-in Gateway 経由にする {all-devices-managed-by-the-drop-in-gateway}

1. プライマリルーターの LAN ポートを、GL.iNet ルーターの WAN ポートへ Ethernet ケーブルで接続します。

2. GL.iNet ルーターの Web Admin Panel にログインし、Drop-in Gateway を有効にします。対応する設定パラメーターが自動生成されます。

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** は、プライマリルーターが動的に割り当てた GL.iNet ルーターの WAN IP アドレスです。この WAN IP は [INTERNET](internet_ethernet.md) ページの Ethernet セクションで確認できます。

    - **Gateway** と **DNS Server 1** の欄には、デフォルトでプライマリルーターの IP アドレスが自動入力されます。これらの値が正しくない場合は、必要に応じて手動で調整してください。

    ここで表示される IP アドレスは後の手順で使用するため、控えておいてください。

    最初の設定方法を選択し、**Apply** をクリックします。

3. プライマリルーターの Web 管理画面にログインします。

    ??? "GL.iNet"

        プライマリルーターが GL.iNet 製で、ファームウェア v4.2 以降の場合は、以下の手順に従ってください。

        Web Admin Panel -> NETWORK -> LAN -> DHCP Server -> Advanced に移動します。

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        DHCP Gateway に手順 2 の IP Address（例: `192.168.1.23`）を入力し、**Apply** をクリックします。

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        プライマリルーターが TP-Link の場合は、以下の手順に従ってください（TP-LINK Archer C3150 を例にしています）。

        TP-Link の管理画面にログインし、**Advanced** -> **Network** -> **DHCP Server** に移動して、**DHCP** を無効にします。

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        その後、**Save** をクリックします。

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        プライマリルーターが Linksys の場合は、以下の手順に従ってください（Linksys WHW01 を例にしています）。

        Linksys の管理画面にログインし、**Router Settings** -> **Connectivity** に移動します。

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        **Local Network** タブをクリックし、**DHCP Server** を無効にして **OK** をクリックします。

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        警告が表示されるので、**OK** をクリックします。

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        プライマリルーターの管理画面で DHCP Server を無効にしてください。必要に応じて、各メーカーのユーザーマニュアルやサポート情報を参照してください。

4. GL.iNet ルーターに戻り、必要に応じて [AdGuard Home](adguardhome.md)、[encrypted DNS](dns.md)、[WireGuard Client](wireguard_client.md)、[OpenVPN Client](openvpn_client.md) などを設定します。

### 特定のデバイスのみを Drop-in Gateway 経由にする {some-devices-managed-by-the-drop-in-gateway}

1. プライマリルーターの LAN ポートを、GL.iNet ルーターの WAN ポートへ Ethernet ケーブルで接続します。

2. GL.iNet ルーターの Web Admin Panel にログインし、Drop-in Gateway を有効にします。対応する設定パラメーターが自動生成されます。

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** は、プライマリルーターが動的に割り当てた GL.iNet ルーターの WAN IP アドレスです。この WAN IP は [INTERNET](internet_ethernet.md) ページの Ethernet セクションで確認できます。

    - **Gateway** と **DNS Server 1** の欄には、デフォルトでプライマリルーターの IP アドレスが自動入力されます。これらの値が正しくない場合は、必要に応じて手動で調整してください。

    ここで表示される IP アドレスは後の手順で使用するため、控えておいてください。

    2 番目の設定方法を選択し、**Apply** をクリックします。

3. Drop-in Gateway を使用したいデバイスで、Gateway と DNS を Drop-in Gateway ページに表示されている IP Address に設定します。

    ??? "Windows"

        Windows 11 を例に説明します。Windows 10 でもほぼ同様です。PC がプライマリルーターに接続されていることを確認してください。ここでは PC がネットワークケーブルでプライマリルーターに接続されている前提ですが、Wi-Fi 接続でも設定方法はほぼ同じです。

        1. 設定を開きます。

        2. **Network & Internet** をクリックします。

        3. **Ethernet** タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. この PC の IP アドレスを確認し、"IP assignment" セクションで **Edit** ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. **Manual** を選択し、**IPv4** のトグルをオンにします。

        6. **IP address** には手順 4 で確認した IP アドレスを設定し、**Subnet mask** は `255.255.255.0`、**Gateway** と **Preferred DNS** はどちらも Drop-in Gateway ページの IP アドレスに設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. **Save** ボタンをクリックします。

    ??? "Android"

        Samsung S21 を例に説明します。スマートフォンがプライマリルーターに接続されていることを確認してください。

        1. 設定を開き、Connections をタップします。

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Wi-Fi をタップします。

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. 現在接続している SSID の歯車アイコンをタップします。

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. **View more** をタップします。

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. **IP settings** をタップし、**Static** を選択します。

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. **Gateway** と **DNS 1** を Drop-in Gateway ページに表示されている IP アドレスに設定し、**Save** をタップします。

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        iPhone 8 の iOS 16.3 を例に説明します。スマートフォンがプライマリルーターに接続されていることを確認してください。

        1. 設定を開き、Wi-Fi をタップします。

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. SSID をタップします。

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. 下へスクロールすると、**Configure IP** が **Automatic** になっています。次の手順で使うため、**IP Address** と **Subnet Mask** を控えておきます。

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. **Configure IP** を **Manual** に変更し、**IP Address** と **Subnet Mask** を前の手順で確認した値に設定します。**Router** には Drop-in Gateway ページに表示される IP アドレスを入力し、**Save** をタップします。

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. **Configure DNS** をタップして **Manual** に変更します。**Add Server** をタップし、DNS サーバーの IP アドレスとして Drop-in Gateway ページに表示される IP アドレスを入力して、**Save** をタップします。

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. GL.iNet ルーターの Web Admin Panel に戻り、必要に応じて [AdGuard Home](adguardhome.md)、[encrypted DNS](dns.md)、[WireGuard Client](wireguard_client.md)、[OpenVPN Client](openvpn_client.md) などを設定します。

## 注意事項

1. Drop-in Gateway を有効にすると、ネットワーク遅延は増加します。

2. Drop-in Gateway を有効にすると、選択された LAN デバイス間のデータ転送も Drop-in Gateway を経由します。そのため、プライマリルーターと Drop-in Gateway 間の帯域幅が LAN 全体の帯域幅に影響します。

---

Related Article:

- [How to set up drop-in gateway on a GL.iNet router](../tutorials/how_to_set_up_drop_in_gateway.md)

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
