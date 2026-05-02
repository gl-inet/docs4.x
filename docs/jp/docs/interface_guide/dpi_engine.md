# DPI Engine

DPI（Deep Packet Inspection）は、インテリジェントなネットワーク管理を支える中核技術です。従来のルーターが送信元アドレスと宛先アドレスの識別にとどまるのに対し、DPI はパケットのペイロードを詳細に解析し、シグネチャライブラリとの照合によってアプリケーションや Web サイトを正確に識別できます。これにより、よりきめ細かなトラフィック分類と制御が可能になります。

GL.iNet の DPI Engine はルーター上でローカルに動作し、プライバシーを保ちながら高度なネットワーク管理を実現します。トラフィック統計、コンテンツフィルター、QoS をまとめて利用でき、包括的なトラフィック制御を行えます。

[Netify](https://www.netify.ai/){target="_blank"} と統合された GL.iNet DPI は、効率的に展開できる軽量な組み込みプラグインを採用しています。Netify のオンライン更新シグネチャデータベースにより、より正確で効率的なネットワーク制御が可能です。

**注**:

1. ルーターが Drop-in Gateway モードのときは、DPI 機能（Data Statistics、Content Filter、QoS を含む）および SQM は動作しません。

2. DPI を有効にすると、安定したパフォーマンスを確保するため **Network Acceleration** は自動的に無効になります。

## 対応モデル

!!! note "対応モデル"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## クイックセットアップ

Web管理画面の左側で、**FLOW CONTROL** -> **DPI Engine** に移動し、**Enable DPI Engine** をクリックします。

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

ポップアップウィンドウで Terms of Service & Privacy Policy を確認して同意し、**Apply** をクリックします。

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

ルーターがシステム処理を行うまでしばらく待ちます。この間に **Network Acceleration** が無効になり、**Data Statistics** と **Content Filter** が有効になります。

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

有効化が完了したら、**Done** をクリックします。

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

続いて **DPI Engine Version Center** に移動し、DPI Program version と Database version を確認できます。

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**注**: このページにはコアシステムの状態指標のみが表示されます。実際のトラフィック処理は、関連機能を有効にしたあとに開始されます。

## データベースのアップグレード

新しいデータベースバージョンが利用可能な場合は、**Upgrade** をクリックするだけで更新できます。

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
