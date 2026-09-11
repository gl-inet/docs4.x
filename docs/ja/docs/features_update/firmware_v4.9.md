# Firmware v4.9

このリリースでは、より精密なネットワーク制御、改善されたトラフィック管理、強化されたネットワークセキュリティ、刷新されたユーザーインターフェースに重点を置き、全体的なユーザー体験の向上を目指しています。

最新のファームウェアは [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"} から入手できます。

## Flow Control

Flow Control は、ネットワークトラフィックを正確に識別、監視、制御、フィルタリングする中核的なネットワーク管理モジュールです。ネットワークリソースの割り当てを効率的に最適化し、帯域幅の混雑を解消し、ネットワークアクセス動作を標準化することで、よりスムーズで安全、かつ制御しやすいネットワーク環境を提供します。ファームウェア v4.9 では、このモジュールに複数の実用的な機能が統合され、包括的なトラフィック管理が可能になりました。

Flow Control モジュールには、DPI Engine、Data Statistics、Content Filter、QoS、SQM、Parental Control が含まれます。

### DPI Engine

送信元アドレスと宛先アドレスのみを識別する従来のルーターとは異なり、DPI（Deep Packet Inspection）はパケットのペイロードを詳細に分析し、特徴照合ライブラリを使用してアプリケーションや Web サイトを正確に識別します。これにより、きめ細かなトラフィック分類と制御が可能になります。

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics

Data Statistics は、アプリケーションやプロトコル別のネットワーク使用状況を確認できる、直感的なトラフィックダッシュボードを提供します。1 時間、1 日、7 日の履歴推移の表示、使用量ランキング、デバイスごとのトラフィック監視、不要なアプリのワンクリックブロックに対応しています。

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter

Content Filter は、DPI 分類を利用したインテリジェントなオンライン安全機能です。有害な Web サイトや悪意のある Web サイトを自動的にブロックしてネットワークを安全に保つほか、特定のアプリ、ドメイン、IP アドレスをブロックするカスタムルールにも対応しています。

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS

QoS（Quality of Service）は、ネットワーク混雑時にビデオ通話やゲームなどの重要な通信を優先し、帯域幅の割り当てを最適化します。これにより、遅延を抑え、ネットワーク全体のパフォーマンスを向上させます。

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM（Smart Queue Management）は、ルーターのネットワークトラフィックをインテリジェントに管理して遅延と「バッファブロート」を最小限に抑え、ゲームや音声通話をよりスムーズにします。

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control

以前は **Applications** メニューに分類されていたこの機能は、ファームウェア v4.9 で **Flow Control** メニューに移動しました。アップグレードされた DPI Engine により、不適切なアプリケーションやネットワークコンテンツを正確に識別してブロックし、トラフィックに基づく、より高度で精密なアクセス制限を実現します。

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

ファームウェア v4.9 では、VPN モジュールの基盤となるルーティングロジックと操作インターフェースが全面的に改善されました。潜在的なルーティング競合を解消し、設定ロジックを簡素化して、操作性を向上させています。

主な変更点は次のとおりです。

### 独立した VPN トンネル

各 VPN トンネルは、グループ間でフェイルオーバーしない独立したグループとして動作します。ネットワークトラフィックが特定の VPN グループに一致すると、現在のトンネルに障害が発生しても他の VPN グループへ自動的に切り替わらないため、安定した予測可能なトラフィックルーティングが維持されます。

**注意**: ファームウェア v4.9 では従来の「Not Use VPN」ポリシーが削除され、冗長な設定をなくすことで、複数の複雑なトンネルルールによるルーティング競合を回避します。

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### VPN プロファイルのフェイルオーバー

1 つの VPN トンネルグループに複数の設定プロファイルを登録できます。同じグループ内で各プロファイルの優先順位を設定でき、1 つのプロファイルに障害が発生した場合はグループ内で自動的にフェイルオーバーして、VPN 接続を維持します。

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### 再設計されたダッシュボード

VPN Dashboard は、より直感的なレイアウトに全面的に再設計されました。トンネルの状態、接続の詳細、設定項目が見やすく表示され、日常の操作と管理を効率化します。また、新しいアーキテクチャでは、トラフィックを常に保護するために、すべての VPN トンネルでキルスイッチがデフォルトで有効になります。

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

ファームウェア v4.9 では、複数の新しいトラフィック難読化パラメータを備えた AmneziaWG 2.0 プロトコルが正式に導入されました。アップグレードされたプロトコルは、DPI やその他のトラフィック識別システムによる検出を効果的に回避し、接続の秘匿性と耐干渉性を大幅に向上させます。これにより、ネットワーク制限のある地域や複雑なネットワーク環境でも、安定した信頼性の高い VPN 接続を確立できます。

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## IoT ネットワーク

ファームウェア v4.9 では、IoT スマートデバイス専用の独立した Wi-Fi ネットワークを作成できます。メインネットワークから物理的および論理的に分離することで、IoT デバイスがメインネットワークにアクセスすることによるネットワークリソースの消費やセキュリティリスクを回避します。この改善により、さまざまなスマート IoT クライアントとの互換性が広がり、ホームネットワーク全体のセキュリティが強化されます。

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL（Access Control List）は、接続プロトコル、デバイスの IP アドレス、ポートに基づいて内部および外部のネットワークトラフィックを管理するカスタムアクセスルールを作成できる、中核的なネットワークセキュリティ管理機能です。特定のネットワークアクセス動作を許可またはブロックするための精密な権限制御に対応しています。複数の ACL ルールが競合した場合、システムは優先度の高いルールを自動的に実行し、ポリシーを正確に適用します。

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

Port Forwarding との主な違いは役割です。ACL はデバイスとトラフィックのアクセス権限を制御するネットワークセキュリティ管理に重点を置きます。一方、Port Forwarding はネットワークリソースのリダイレクトに使用され、外部ネットワークトラフィックを指定したローカル端末へ転送して、ローカルネットワークサービスへのリモートアクセスを実現します。

## Wireless UI

Wireless UI は、整理されたレイアウトと統一されたビジュアルスタイルで全面的に再設計されました。操作の複雑さが軽減され、インターフェース全体のシンプルさと使いやすさが大きく向上しています。

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## 暗号化 DNS

暗号化 DNS は、DoH、DoT、DoQ など、より多くの暗号化プロトコルに対応しました。同時に、より多くの公式 DNS サービスプロバイダーが統合され、カスタム暗号化 DNS サーバーの手動設定も追加されました。これにより、安全なドメイン解決に関する多様なニーズに対応できます。

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node

GL.iNet ルーターは、Tailscale Exit Node として動作できるようになりました。Tailnet 内のデバイスから送信されるすべてのインターネットトラフィックをルーターのパブリック IP アドレス経由でルーティングでき、Tailscale ネットワーク全体で統一された安全なネットワーク出口管理を実現します。詳しくは[こちら](../interface_guide/tailscale.md#run-exit-node)を参照してください。

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

ご不明な点がありましたら、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} ください。
