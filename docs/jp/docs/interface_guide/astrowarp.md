# AstroWarp

!!! note

    このガイドでは、AstroWarpの新しいバージョンを紹介します。これは現に、それぞれ firmware v4.8.4 および v4.8.3 で **Flint 3 (GL-BE9300)** と **Slate 7 (GL-BE3600)** で利用可能です。

    彼のモデルについては、[こちら](https://docs.astrowarp.net/){target="_blank"} をご覧ください。

AstroWarp は GL.iNet ルーターに統合された高度なネットワーク機能です。登録やログインなしにホームネットワークへのシームレスなリモートアクセスを可能にします。組み込みのトラフィック難読化を持つ AmneziaWG プロトコルを使用し、接続を安定かつ安全に保ち、どこでも信頼できるリモートアクセスに最も適です。

ユーザーは GL.iNet ルーター管理パネルから直接 AstroWarp ネットワークを設定できます。アクセスキーを使用してルーターをペアリングするだけで、旅行用ルーターを数秒でホームネットワークに安全に接続できます。

**注意：**

1. ルーティングの競合が発生する可能性があるため、以下の機能と同時に AstroWarp を使用することは推奨されません：GoodCloud サイト間、ZeroTier、Tailscale、Tor。
2. AstroWarp が有効な場合、ネットワークモードは使用できません。

## クイックセットアップ

次の例では、**Flint 3 (GL-BE9300)** と **Slate 7 (GL-BE3600)** を使用して AstroWarp ネットワークを設定します。

Flint 3 はホームルーターとして機能し、Slate 7 は旅行用ルーターとして機能し、インターネットアクセスためにネットワークトラフィックを Flint 3 にルーティングします。

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**注意**：各 GL.iNet ルーターには AstroWarp ネットワーキング用に**月額 10GB の無料データ**が付属しています。AstroWarp ネットワーク内のデバイスはホームルーターのデータを使用してインターネットにアクセスできます。必要に応じて無制限データ用に AstroWarp+ プランにアップグレードできます。

1. Flint 3 を設定してインターネットに接続します。

    Flint 3 の Web 管理パネルにログインし、INTERNET ページに移動します。サポートされているインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用してインターネットに接続します。

    以下に示すように、Flint 3 ホームルーターはイーサネットケーブルで ISP モデム（Hong Kong Broadband Network Ltd）に接続されています。

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. アクセスコードを生成します。

    Flint 3 の Web 管理パネルで、CLOUD SERVICES -> AstroWarp に移動します。「から宅で使用」をクリックします。

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    **アクセスコード**が生成されます。このコードをコピーして、後で使用します。

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Slate 7 を設定してインターネットに接続します。

    Slate 7 の Web 管理パネルにログインし、INTERNET ページに移動します。サポートされているインターネット接続方法（Ethernet、Repeater、Tethering、Cellular）のいずれかを使用してインターネットに接続します。

    以下に示すように、Slate 7 旅行用ルーターは iPhone 15 Pro のパーソナルホットスポットに接続されています（深圳に位置し、中国聯通広東省ネットワークを使用）。
