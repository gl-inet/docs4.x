# Firmware v4.11

このリリースでは、ネットワーク品質の監視とセキュリティ評価を改善し、接続の問題や潜在的なセキュリティリスクを特定しやすくしています。また、Mesh、GL.iNet アカウント、VLAN の新機能に加え、DNS、SQM、QoS、通信統計も大幅に強化されています。

最新のファームウェアは、[ファームウェアダウンロードセンター](https://dl.gl-inet.com/){target="_blank"}から入手できます。

## ネットワーク品質

[ネットワーク品質](../interface_guide/network_quality.md)は、インターネット接続をリアルタイムで監視する新機能です。応答性、遅延、DNS のパフォーマンスを評価するとともに、接続の切断やパケット損失を検出し、帯域幅テストだけではわからないネットワークの不安定さや接続の問題を特定するのに役立ちます。

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## セキュリティスキャン

[セキュリティスキャン](../interface_guide/security_scan.md)は、ルーターのセキュリティ設定を評価し、セキュリティスコア、リスク警告、最適化の提案を表示する新機能です。Wi-Fi セキュリティ、WAN ping、リモート SSH、ポート転送、DPI コンテンツ保護などを確認し、潜在的なセキュリティリスクの特定と対処を支援します。ページを開くとスキャンが自動的に開始されます。スコアアイコンをクリックすると、スキャンをリセットして再実行できます。

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## Mesh

[Mesh](../interface_guide/mesh.md)は、Wi-Fi EasyMesh™ 標準に基づく機能で、家全体の Wi-Fi カバー範囲を広げ、シームレスなローミングを実現します。複数の GL.iNet ルーターがある場合は、1台をメインルーター、残りをメッシュノードとして設定することで、家の中を移動しても Wi-Fi をシームレスに利用できます。

**注意**: この機能は一部のモデルで先行して提供され、ファームウェア v4.11 で対応モデルが拡大されました。

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/mesh.png){class="glboxshadow"}

## GL.iNet アカウント

[GL.iNet アカウント](../interface_guide/glinet_account.md)を使用すると、デバイスとクラウドサービスに統一されたアカウントでアクセスできます。1つの GL.iNet アカウントで GoodCloud と GL.iNet アプリを利用でき、ネットワークやデバイスをより便利に管理できます。また、GoodPAS を使用すると、トラベルルーターとホームネットワークの間に安全な接続をすばやく確立でき、外出先からシームレスにリモートアクセスできます。

**注意**: この機能は一部のモデルで先行して提供され、ファームウェア v4.11 で対応モデルが拡大されました。

![GL.iNet Account](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/glinet_account.png){class="glboxshadow"}

## GoodPAS

[GoodPAS](../interface_guide/goodpas.md)は、トラフィック難読化機能を内蔵した AmneziaWG プロトコルに基づくリモートアクセスソリューションです。登録やログインを行わずに、動的なアクセスコードを使用してトラベルルーターをホームネットワークに安全に接続できます。

**注意**: この機能は一部のモデルで先行して提供され、ファームウェア v4.11 で対応モデルが拡大されました。

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodpas.png){class="glboxshadow"}

## GoodCloud

[GoodCloud](../interface_guide/cloud.md)を使用すると、GL.iNet ルーターにリモートアクセスし、一元管理できます。複数のデバイスの一括管理、ネットワーク設定の展開、ファームウェアの更新に加え、ルーターの Web 管理パネルや SSH ターミナルにもリモートでアクセスできます。

**注意**: この機能は一部のモデルで先行して提供され、ファームウェア v4.11 で対応モデルが拡大されました。

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodcloud.png){class="glboxshadow"}

## Ethernet Port

[Ethernet Port](../interface_guide/ethernet_port_v4.10.md) ページには、ルーターのすべてのインターフェースが表示されます。各インターフェースの接続状態を確認し、イーサネットポートの役割（WAN または LAN）を管理できます。また、MAC アドレス、ネゴシエート速度、現在のリンク状態などのポート情報も確認できます。さらに、作成したサブネットに物理インターフェースを割り当てることができます。

**注意**: この機能は一部のモデルで先行して提供され、ファームウェア v4.11 で対応モデルが拡大されました。

次の図は、Flint 3（GL-BE9300）の Ethernet Port ページです。

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/ethernet_port.png){class="glboxshadow"}

## DNS

このリリースでは、WAN DNS、VPN DNS、Manual DNS を1つのページにまとめ、[DNS](../interface_guide/dns_v4.11.md) 設定を改善しています。接続タイプごとの DNS 状態を簡単に確認し、カスタム DNS サーバーを設定できます。また、手動 DNS 設定を VPN トンネルに適用するか、ルーター自体に適用するかを選択できます。

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns_v4.11.png){class="glboxshadow"}

## QoS

このファームウェアでは、[QoS](../interface_guide/qos.md)（Quality of Service）が強化されています。WAN 帯域幅向けに **Run Speedtest** が追加され、WAN のダウンロード帯域幅とアップロード帯域幅を測定して、対応する欄に自動入力できます。新たに追加された **Device Priority** と **Advanced QoS** を含む、3種類のスケジューリングポリシーを利用できます。

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: WAN が混雑しているときに、選択したローカルクライアントのネットワーク優先度を高くします。

- **Application Priority**: アプリケーションごとに優先度を設定すると、ルーターがそれに応じて帯域幅を割り当てます。

- **Advanced QoS**: 優先度の高いトラフィックに対して、高度な QoS ルールを作成します。

## SQM

[SQM](../interface_guide/sqm.md)（Smart Queue Management）には、WAN 帯域幅向けの **Run Speedtest** オプションが用意されており、ダウンロード速度とアップロード速度を測定して、対応する欄に自動入力します。**cake** キュー規律では、新たに追加された **Cake Autorate** が、プローブの RTT に基づいて設定済みの帯域幅を動的に調整します。能動的な速度テストではなく軽量な ping を使用するため、帯域幅が変動する WAN 接続に推奨されます。

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_v4.11.png){class="glboxshadow" width=600}

![cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/cake_autorate.png){class="glboxshadow" width=600}

## データ統計

[データ統計](../interface_guide/data_statistics.md)で、クライアントごとのトラフィック絞り込みが可能になりました。また、棒グラフや円グラフなどの新しい表示形式が追加されています。アプリのトラフィック統計を表示する際に、特定のクライアントを選択し、グラフの表示形式を切り替えることで、通信量をよりわかりやすく分析できます。

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
