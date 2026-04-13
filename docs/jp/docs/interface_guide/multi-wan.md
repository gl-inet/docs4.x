# マルチWAN

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Web Admin Panel の左側で、**NETWORK** -> **Multi-WAN** に移動します。

ルーターに複数のインターネット接続方法を設定できます。ある接続方法が利用できなくなった場合、短時間で自動的に別の接続方法へ切り替えられます。また、複数の接続方法を同時に使い、一定の比率で新しい接続を割り当てることもできます。

GL.iNet ルーターは、[Ethernet](internet_ethernet.md)、[Repeater](internet_repeater.md)、[Tethering](internet_tethering.md)、[Cellular](internet_cellular.md) など、複数の方法でインターネットへ接続できます。

!!! Note

    1. Wi-Fi 機能のないモデル（例: GL-MT2500/GL-MT2500A）は、Ethernet、Tethering、Cellular のみをサポートします。

    2. USB ポートのないモデル（例: GL-B3000）は、Ethernet と Repeater のみをサポートします。

    3. 一部モデルは [Dual-Ethernet WAN](dual-ethernet_wan.md) をサポートしており、UI 上に追加の Ethernet インターフェースが表示されます。

## インターフェース状態追跡

GL.iNet ルーターは最大 5 つの仮想ネットワークインターフェースをサポートしますが、実際の数はモデルによって異なります。たとえば GL-MT6000 には **Ethernet 1**、**Ethernet 2**、**Repeater**、**Tethering**、**Cellular** があり、それぞれがソフトウェア定義された異なる役割を持ちます。

ルーターは **ping** コマンド（v4.3 以前では **httping** も利用可能）を使って宛先 IP への接続状態を追跡し、そのインターフェースが利用可能かどうかを判断します。

インターフェースが利用可能な場合、左側に緑色の点が表示され、利用できない場合は灰色になります。

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### ステータストラッキング設定

歯車アイコンをクリックすると、各ネットワークインターフェースの状態追跡設定を開けます。

以下は Ethernet インターフェースの状態追跡設定の例で、ほかのインターフェースも同様です。

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: デフォルトで有効です。無効にすると、ルーターはインターフェースの物理状態（例: ネットワークケーブルが挿さっているかどうか）だけで利用可否を判断します。

- **Detection Mode**: この機能は v4.5 では Low Data Mode として導入され、v4.7 で Detection Mode に名称変更されました。Normal Mode、Low Data Mode、Strict Mode の 3 つがあります。

    Normal Mode がデフォルトです。Low Data Mode はインターフェースのネットワーク異常が発生したときのみ追跡を行い、Strict Mode は public IP への検出コマンド結果だけに基づいてインターフェース状態を判定します。

    データ通信量に制限がある場合は Low Data Mode を使えます。ただし、ネットワーク切断後の再接続が Normal Mode よりわずかに遅くなることがあり、デフォルトでは Cellular インターフェースのみがオンになります。

- **Track Command**: ping コマンドを使って宛先 IP への接続状態を追跡し、インターフェースが利用可能かどうかを判断します。ファームウェア v4.3 以前では httping も使用できます。

- **IPv4 Track IP**: ここで IPv4 Track IP をカスタマイズできます。

!!! Note

    v4.3 などの古いファームウェアでは、**Track Interval**、**Change to Failure Condition**、**Change to Available Condition** などの設定がありました。これらは v4.5 以降で廃止され、Detection Mode と Sensitivity Options に置き換えられています。

### 感度オプション

この機能は v4.5 以降で利用できます。

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

この感度設定は、インターネット状態を検出する時間間隔を決定します。

- ネットワークが安定していて、動画視聴、ライブ配信、ゲームなどの用途では、切断時に素早く切り替えられるよう高感度を推奨します。
- ネットワークが不安定で、キャッシュされるファイルをダウンロードしているような用途では、頻繁な切り替えや接続失敗を防ぐため低感度を推奨します。

**Tips**: 高感度へ切り替えるとネットワーク切断が発生する場合があります。慎重に調整してください。

## Multi-WAN の方式

方式は **Failover** と **Load Balance** の 2 つです。複数の WAN 接続がある場合、デフォルトでは Failover が有効になります。

**Failover** と **Load Balance** は排他的であり、同時には使用できません。

### Failover

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

各インターフェースの優先順位を設定できます。使用中のインターフェースに障害が発生すると、ルーターは利用可能なインターフェースのうち最も優先順位の高いものへ自動的に切り替えます。

たとえば、ルーターに **Ethernet** と **Repeater** の 2 種類のインターネット接続が設定され、Ethernet の優先順位が 1、Repeater の優先順位が 2 である場合、より優先順位の高い Ethernet が使われます。Ethernet ケーブルを抜くと Ethernet インターフェースは利用不可になり、ルーターは自動的に Repeater インターフェースへ切り替えてインターネットへ接続します。

その後 Ethernet 接続が復旧すると、優先順位が高いため、ルーターは自動的に Ethernet へ戻ります。

### 負荷分散

複数のネットワークインターフェースを同時に使い、ルーター全体の帯域を増やします。

ここで設定する load ratio は各ネットワークインターフェース間の比率であり、システムはその比率に基づいて新しい接続を各インターフェースへ割り当てます。

たとえば、ルーターが 4 つのネットワーク（Ethernet、Repeater、Tethering、Cellular）に同時接続され、4 つすべてのインターフェースがインターネット利用可能な場合、Load Balance を有効にして `1:1:1:1` に設定すると、4 つのインターフェースへ新しい接続が均等に割り当てられます。

load ratio はカスタマイズも可能です。たとえば Ethernet が 200 Mbps、Repeater の Wi-Fi が 100 Mbps、Tethering と Cellular が未接続の場合、Ethernet を 2、Repeater を 1、Tethering/Cellular を 0 に設定できます。するとシステムは `2:1` の比率で新しい接続を割り当て、Ethernet インターフェースが Repeater の約 2 倍の接続を処理します。Failover mode と比べると、利用可能なインターフェースへ負荷を分散することで全体のスループット効率を高められます。

**Note:** 既存の接続やトラフィックが load ratio と正確に一致することは保証されません。長時間使用するほど、この比率に近づきます。

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

## 使用シナリオ

* 店舗のレジシステムは有線でインターネットへ接続し、ネットワークケーブルが使えない場合の予備回線として、近隣店舗の Wi-Fi への Repeater 接続（または SIM カードを挿入して Cellular を有効化）を使用することで、モバイル決済が止まるのを防げます。

* ルーターを公衆 Wi-Fi に Repeater 接続していて速度が十分でない場合は、Mobile Tethering を同時に使って Load Balance を行い、全体の帯域を改善できます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
