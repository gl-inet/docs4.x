# Firmware v4.11 {#firmware-v411}

このリリースでは、ネットワーク品質の監視とセキュリティ評価を改善し、接続の問題や潜在的なセキュリティリスクを特定しやすくしています。また、DNS、QoS、SQM、データ統計を強化し、ネットワーク管理とトラフィック制御の柔軟性を高めています。

最新のファームウェアは、[ファームウェアダウンロードセンター](https://dl.gl-inet.com/){target="_blank"}から入手できます。

## ネットワーク品質 {#network-quality}

[ネットワーク品質](../interface_guide/network_quality.md)は、インターネット接続をリアルタイムで監視する新機能です。応答性、遅延、DNS のパフォーマンスを評価するとともに、接続の切断やパケット損失を検出し、帯域幅テストだけではわからないネットワークの不安定さや接続の問題を特定するのに役立ちます。

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## セキュリティスキャン {#security-scan}

[セキュリティスキャン](../interface_guide/security_scan.md)は、ルーターのセキュリティ設定を評価し、セキュリティスコア、リスク警告、最適化の提案を表示する新機能です。Wi-Fi セキュリティ、WAN ping、リモート SSH、ポート転送、DPI コンテンツ保護などを確認し、潜在的なセキュリティリスクの特定と対処を支援します。ページを開くとスキャンが自動的に開始されます。スコアアイコンをクリックすると、スキャンをリセットして再実行できます。

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## UPnP {#upnp}

[UPnP](../interface_guide/upnp.md) により、対応するLANデバイスやアプリケーションは、ポート転送を手動設定せずにポートマッピングを自動的に要求できます。オンラインゲーム、ピアツーピアのファイル共有、リモートアクセスの接続が簡単になります。UPnPページでは、有効なマッピングの表示、リースの残り時間の確認、必要に応じたマッピングの削除ができます。

![UPnP](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/upnp.png){class="glboxshadow"}

## DNS {#dns}

このリリースでは、WAN DNS、VPN DNS、Manual DNS を1つのページにまとめ、[DNS](../interface_guide/dns_v4.11.md) 設定を改善しています。接続タイプごとの DNS 状態を簡単に確認し、カスタム DNS サーバーを設定できます。また、手動 DNS 設定を VPN トンネルに適用するか、ルーター自体に適用するかを選択できます。

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md)（Quality of Service）には、WAN帯域幅向けの **Run Speedtest** オプションがあり、ダウンロード速度とアップロード速度を測定して対応する欄に自動入力します。このリリースでは、Application Priorityに加え、**Device Priority** と **Advanced QoS** の2つのスケジューリングポリシーが追加されています。

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: WAN が混雑しているときに、選択したローカルクライアントのネットワーク優先度を高くします。

- **Application Priority**: アプリケーションごとに優先度を設定すると、ルーターがそれに応じて帯域幅を割り当てます。

- **Advanced QoS**: 優先度の高いトラフィックに対して、高度な QoS ルールを作成します。

## SQM {#sqm}

[SQM](../interface_guide/sqm.md)（Smart Queue Management）には、WAN帯域幅向けの **Run Speedtest** オプションがあり、ダウンロード速度とアップロード速度を測定して対応する欄に自動入力します。**cake** と **fq_codel** の2つのキューイング方式を利用できます。

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: 全体的な遅延制御に最も優れた、インテリジェントな自動トラフィック整形です（推奨）。

    このキューイング方式では、新たに追加された **Cake Autorate** が、プローブのRTTに基づいて設定済みの帯域幅を動的に調整します。能動的な速度テストではなく軽量なpingを使用するため、帯域幅が変動するWAN接続に推奨されます。

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: 基本的な遅延低減を備えた、シンプルで効率的な公平キューイングです。

## データ統計 {#data-statistics}

[データ統計](../interface_guide/data_statistics.md)で、クライアントごとのトラフィック絞り込みが可能になりました。また、棒グラフや円グラフなどの新しい表示形式が追加されています。アプリのトラフィック統計を表示する際に、特定のクライアントを選択し、グラフの表示形式を切り替えることで、通信量をよりわかりやすく分析できます。

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
