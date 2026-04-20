# ネットワークモード

Web Admin Panel の左側で、**NETWORK** -> **Network Mode** に移動します。

Network mode とは、さまざまなネットワーク構成に対応するためにルーターが担う動作役割や機能を指します。各モードは、家庭での Wi-Fi エリア拡張から企業向けの複数回線構成まで、用途に応じて特定の機能を有効または無効にし、最適な動作を実現します。

!!! note

    1. ルーターのネットワークモードを変更すると、すべてのクライアントデバイスを再接続する必要がある場合があります。
    2. **ルーターが Access Point / WDS / Bridge mode のときは、元の LAN IP アドレスでは Web Admin Panel にアクセスできません。** 上位ルーターにログインして、このルーターに割り当てられた IP アドレスを確認し、その IP アドレスで Web Admin Panel にアクセスしてください。上位ルーターにアクセスできない場合は、リセットボタンを 4 秒間長押ししてデフォルトの Router mode に戻してください。
    3. **Non-Router mode では、次の機能は利用できません**: Access Control (Allowlist and Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Wi-Fi搭載モデルの場合

特定のモデルを除き、多くの GL.iNet ワイヤレスルーターには Wi-Fi 機能があります。

Wi-Fi 機能を持つモデルでは、通常 Router、Access Point、Extender、WDS の 4 つのネットワークモードを利用できます。ただし、一部モデルは WDS mode をサポートしていません。

![network mode](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: 家庭や小規模オフィス向けルーターで一般的なデフォルト動作モードです。プライベート LAN を構築し、インターネットと接続デバイスの間の専用ゲートウェイとして機能します。

    Router mode では、NAT、DHCP、内蔵ファイアウォールなどの基本機能が有効になります。光回線などの上位回線に接続し、接続デバイスへプライベート IP アドレスを自動割り当てしながら、ネットワーク全体の保護を行います。

    ---

- **Access Point**: LAN ケーブルで有線ネットワークへ接続し、無線信号をブロードキャストして Wi-Fi カバレッジを拡張するモードです。

    Access Point mode では、NAT と DHCP は無効になり、単独のゲートウェイではなく、無線アクセスポイント兼スイッチとして動作します。

    Access Point mode に切り替えると、元の LAN IP アドレスでは Web Admin Panel にアクセスできません。上位ルーターにログインして、この AP に割り当てられた IP アドレスを確認し、その IP アドレスでアクセスしてください。上位ルーターにアクセスできない場合は、リセットボタンを 4 秒間長押ししてデフォルトの Router mode に戻してください。

    ---

- **Extender**: 既存の無線ネットワークの Wi-Fi カバレッジを拡張し、電波の届きにくい場所を補うためのモードです。

    ルーターがメインルーターの無線信号を受信し、それを増幅して再送信します。Access Point mode と異なり有線接続は不要ですが、受信と送信を同時に行うため、帯域が半減する場合があります。

    Extender mode では、元の LAN IP アドレスを使って引き続き Web Admin Panel にアクセスできます。

    ---

- **WDS**: Wireless Distribution System（WDS）mode は、無線で Wi-Fi カバレッジを拡張する点では Extender mode と似ていますが、対応ルーター同士の無線ブリッジ接続をサポートします。上位ルーターが WDS 機能を持つ場合に推奨されます。

    複数階建ての建物や小規模オフィスで、複数のルーターを連携させて 1 つの無線ネットワークを構成したい場合に適しています。1 台のメインルーターから単一の中継機へ信号を送る Extender mode と異なり、WDS mode では接続されたルーター同士が送受信の両方を行えるため、より広い範囲をシームレスにカバーできます。

    WDS mode に切り替えると、元の LAN IP アドレスでは Web Admin Panel にアクセスできません。上位ルーターにログインして、この WDS ルーターに割り当てられた IP アドレスを確認し、その IP アドレスでアクセスしてください。上位ルーターにアクセスできない場合は、リセットボタンを 4 秒間長押ししてデフォルトの Router mode に戻してください。

## Wi-Fi非搭載モデルの場合

GL-MT2500/GL-MT2500A は Wi-Fi 機能がないため、Access Point、Extender、WDS mode は利用できません。その代わりに Router mode と Bridge mode をサポートします。

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: 家庭や小規模オフィス向けルーターで一般的なデフォルト動作モードです。プライベート LAN を構築し、インターネットと接続デバイスの間の専用ゲートウェイとして機能します。

    Router mode では、NAT、DHCP、内蔵ファイアウォールなどの基本機能が有効になります。光回線などの上位回線に接続し、接続デバイスへプライベート IP アドレスを自動割り当てしながら、ネットワーク全体の保護を行います。

    ---

- **Bridge**: ルーターを有線ネットワークへ接続し、ネットワークデバイス間のブリッジとして動作させます。

    このモードでは、ルーターは実質的にスイッチとして動作し、NAT、ファイアウォール、DHCP を行わずに接続デバイス間でデータを転送します。ネットワークゲートウェイではなく単純な接続ポイントとして動作することで、同一ネットワーク上のデバイス同士のシームレスな通信を可能にします。

    Bridge mode に切り替えると、元の LAN IP アドレスでは Web Admin Panel にアクセスできません。上位ルーターにログインして、この Bridge ルーターに割り当てられた IP アドレスを確認し、その IP アドレスでアクセスしてください。上位ルーターにアクセスできない場合は、リセットボタンを 4 秒間長押ししてデフォルトの Router mode に戻してください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
