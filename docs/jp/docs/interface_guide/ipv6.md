# IPv6

IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。より大きな一意の IP アドレス空間を提供し、IPv4 のアドレス枯渇問題を解決しながら、世界的に増加する接続デバイスを支えます。

Web Admin Panel の左側で、**NETWORK** -> **IPv6** に移動します。

このページでは、ルーターで IPv6 を有効にして設定できます。

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

IPv6 を有効にすると、Ethernet などの WAN インターフェースは DHCPv6 経由で IPv6 アドレスを取得します。Ethernet の設定ページで IPv6 アドレスを手動変更することもできます。

**Note**: 一部の機能（例: firewall、GoodCloud、OpenVPN DCO）はまだ IPv6 をサポートしていません。これらの機能と IPv6 を同時に使用すると、接続問題が発生する可能性があります。

**Enable IPv6** をオンにし、メインネットワークのモードと DNS acquisition method を選択して、**Apply** をクリックします。

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: 4 つのモードが利用できます。**Native**、**Passthrough**、**NAT6**、**Static IPv6** です。

- Native: ルーターが直接パブリック IPv6 アドレスを取得し、接続中のデバイスへ IPv6 アドレスを自動的に割り当てる場合に適したモードです。ほとんどのユーザーの IPv6 利用に対応できます。

- Passthrough: IPv6 パケットを処理や変換を行わず、そのまま通過させる必要がある場合に適したモードです。たとえば、一部のネットワークアプリケーションやサービスでは、後続の処理や解析のために IPv6 パケットの内容を完全に保持する必要があり、ネットワークのデバッグやセキュリティ解析で利用されます。

- NAT6: ルーターを管理ゲートウェイとして使用し、ネットワーク上の各デバイスへ動的な内部 IPv6 アドレスを割り当てるシナリオに適したモードです。このモードでは、端末デバイスは Optical Network Terminal を経由して接続し、ローカルネットワークの IPv6 アドレスを取得します。

- Static IPv6: サーバーやネットワークプリンターなど、固定 IPv6 アドレスが必要なデバイスやサービスに適したモードです。常に同じ IPv6 アドレスを使用するため、管理とアクセスがしやすくなります。

**DNS acquisition method**: ルーターが IPv6 DNS サーバーアドレスをどのように取得するかを決めます。**Automatic** と **Manual** の 2 つがあります。

- Automatic: ルーターは IPv6 DNS サーバーアドレスを動的に取得します（例: DHCPv6 経由）。

- Manual: カスタム IPv6 DNS サーバーアドレスを入力します。ただし、DNS はドメイン名を対応する IP アドレスへ解決するために使われるため、手動設定によって DNS ルックアップに失敗する場合があります。慎重に使用してください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
