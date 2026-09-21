# ネットワーク品質

**注**：この機能はファームウェアv4.11で導入されました。

---

Web管理画面の左側で、**FLOW CONTROL** -> **Network Quality**に移動します。

ネットワーク品質ダッシュボードは、インターネット接続の品質をリアルタイムで監視します。応答性、遅延、DNSパフォーマンスを評価し、接続の切断やパケット損失を検出します。これらの指標は、帯域幅テストだけではわからないネットワークの不安定性や接続の問題を特定するのに役立ちます。

このページでは、ネットワーク品質スコアを使用してインターネット接続を評価し、必要に応じてローカル速度テストを実行できます。

**注**：

1. GL.iNetネットワーク品質の総合スコアは、次の加重式で算出されます。

    `総合スコア = 応答スコア × 60% + 信頼性スコア × 40%`

2. Speedtestはルーター上で実行されるローカル速度テストであり、SQMやQoSなどの機能による速度制限ルールの影響を受けます。

## ネットワーク品質スコア

このセクションには、応答スコアと信頼性スコアから算出された総合ネットワーク品質スコアが表示されます。各スコアを個別に確認できます。パネルには、遅延、ジッター、パケット損失などの関連指標に加え、リアルタイムのダウンロード速度とアップロード速度（KB/s）も表示されます。デフォルトでは、インターネット接続確認とDNS解決テストの対象として`google.com`が使用されます。

設定アイコンをクリックして、プローブ対象を設定します。

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

インターネット到達性とDNS解決のプローブ対象として、Baidu、Tencent、Alibaba、Google、Microsoft、Cloudflareを選択できます。カスタムドメインを手動で入力することもできます。

設定した対象は、接続テストとDNSテストの実行、およびネットワーク品質スコアの算出に使用されます。

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**：インターネット接続の確認とエンドツーエンド遅延の測定（Hop2 ping対象）に使用されます。

- **DNS Resolution Target**：DNSルックアップのプローブ時に解決されるドメインです。A（IPv4）レコードとAAAA（IPv6）レコードの両方が照会されます。

## Speedtest

この内蔵速度テストでは、Cloudflare Speed Testを使用して、ダウンロード速度、アップロード速度、ping遅延、バッファブロートを測定します。テスト中はリアルタイムの速度グラフが表示されます。

**Run Speedtest**をクリックして速度テストを開始します。

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

テストが完了すると、結果がページに表示されます。

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
