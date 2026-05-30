# AstroWarp

**注意**: このガイドでは、AstroWarp の新バージョンを紹介します。

新しい AstroWarp は GL.iNet ルーター SDK に統合されており、トラフィック難読化を内蔵した AmneziaWG プロトコルを採用しています。これにより、安定かつ安全な接続を実現し、いつでもどこでも信頼性の高いリモートアクセスを提供します。

この機能により、自宅ネットワークへシームレスにリモートアクセスできます。Web Admin Panel からダイナミックアクセスコードを使ってデバイスを直接設定・ペアリングでき、登録やログインなしで、旅行用ルーターと自宅ネットワークの安全な接続を数秒で確立できます。

従来の AstroWarp は Web Admin Panel 上に表示されていましたが、リモートネットワーク接続を確立するには独立した AstroWarp プラットフォームが必要でした。従来版 AstroWarp のドキュメントについては、[こちら](https://docs.astrowarp.net/){target="_blank"} を参照してください。

**Note:**

1. GoodCloud Site to Site、ZeroTier、Tailscale、Tor のいずれかの機能と AstroWarp を同時に使用すると、ルーティングの競合が発生する可能性があるため、推奨されません。
2. AstroWarp を有効にすると、Network Mode は使用できません。

## 対応モデル

??? "対応モデル"

    これらのモデルは新しい AstroWarp に対応しています。従来版 AstroWarp の対応モデル一覧は、[こちら](https://docs.astrowarp.net/en/quick_start/){target="_blank"} をクリックして確認してください。

    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **注意**: ※印のモデルは、Beta ファームウェアで統合版 AstroWarp をサポートしています。

??? "非対応モデル"
    これらのデバイスは新しい AstroWarp には対応していませんが、一部のモデルは従来版 AstroWarp で引き続き利用できます。詳細は [こちら](https://docs.astrowarp.net/en/quick_start/){target="_blank"} を参照してください。

    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## クイックセットアップ

次の例では、**Flint 3 (GL-BE9300)** と **Slate 7 (GL-BE3600)** を使用して AstroWarp ネットワークを設定します。

Flint 3 はホームルーターとして動作し、Slate 7 は旅行用ルーターとして動作します。Slate 7 のネットワークトラフィックは Flint 3 に戻され、インターネットアクセスに利用されます。

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**注意**: 各 GL.iNet ルーターには、AstroWarp ネットワーク用として毎月 **10 GB の無料データ通信量** が付属しています。AstroWarp ネットワーク内のデバイスがインターネットへアクセスする際には、ホームルーター側のデータ通信量が使用されます。必要に応じて、無制限データの **AstroWarp+** プランにアップグレードできます。

1. Flint 3 をインターネットに接続します。

    Flint 3 の Web 管理パネルにログインし、**INTERNET** ページを開きます。対応している接続方法である Ethernet、Repeater、Tethering、Cellular のいずれかを使用してインターネットに接続します。

    以下の例では、Flint 3 のホームルーターが Ethernet ケーブルで ISP モデム（Hong Kong Broadband Network Ltd）に接続されています。

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Access Code を生成します。

    Flint 3 の Web 管理パネルで、**CLOUD SERVICES** -> **AstroWarp** に移動し、**Use At Home** をクリックします。

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    **Access Code** が生成されます。あとで使用するので、このコードをコピーしておいてください。

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Slate 7 をインターネットに接続します。

    Slate 7 の Web 管理パネルにログインし、**INTERNET** ページを開きます。対応している接続方法である Ethernet、Repeater、Tethering、Cellular のいずれかを使用してインターネットに接続します。

    以下の例では、Slate 7 の旅行用ルーターが iPhone 15 Pro のパーソナルホットスポットに接続されています（所在地は深圳で、中国聯通広東省ネットワークを使用）。

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Access Code を入力します。

    Slate 7 の Web 管理パネルで、**CLOUD SERVICES** -> **AstroWarp** に移動し、**Use While Travelling** をクリックします。

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    手順 2 で取得した Access Code を入力します。

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    検証が完了するまで待ちます。

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    その後、Flint 3 ホームルーターへの接続が正常に完了します。これで、自宅ネットワーク経由で安全にインターネットを利用できます。

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    Flint 3 側の Web 管理パネルにも、以下のように接続ステータスが表示されます。

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## 接続テスト

1. ノート PC またはスマートフォンを、Slate 7 旅行用ルーターの Wi-Fi に接続します。

2. ブラウザを開き、[ipcheck.ing](https://ipcheck.ing/){target="_blank"} またはその他の IP アドレス確認サイトにアクセスします。

    Flint 3 のグローバル IP アドレスが表示されれば、Slate 7 が Flint 3 ホームルーター経由でインターネットにアクセスしていることを示します。

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Slate 7 で AstroWarp 接続を切断し、その後 Web ページを再読み込みして IP 照会を再実行します。

    Slate 7 のグローバル IP アドレスが表示されれば、Slate 7 がローカルネットワーク経由でインターネットにアクセスしていることを示します。

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## プランのアップグレード

各 GL.iNet ルーターには、AstroWarp ネットワーク用として毎月 **10 GB の無料データ通信量** が付属しています。AstroWarp ネットワーク内のデバイスがインターネットへアクセスする際には、ホームルーター側のデータ通信量が使用されます。

必要に応じて、無制限データの **AstroWarp+** プランにアップグレードできます。

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

## FAQ

1. **Q: ダイナミックアクセスコードの形式と有効期限を教えてください。**

    A: 数字と大文字を組み合わせた 8 文字のコードで、有効期限は 10 分です。

2. **Q: ホームルーター側で接続を終了すると、旅行用ルーターはどうなりますか。**

    A: 旅行用ルーターは切断され、ネットワークにアクセスできない pending 状態になります。ホームルーター側で接続が再開されると、アクセスコードを再入力しなくても旅行用ルーターは自動的に再接続できます。

3. **Q: ホームルーター側で無料データがなくなったり、AstroWarp+ プランの期限が切れたりするとどうなりますか。**

    A: 旅行用ルーターはネットワークにアクセスできない pending 状態になり、ローカルネットワークへ自動的に切り替わることはありません。

4. **Q: どのような場合に旅行用ルーターは pending 状態になりますか。**

    A: ホームルーターが次のいずれかの条件に当てはまると、旅行用ルーターは pending 状態になります。

    - AstroWarp 接続を終了した場合
    - 無料データ通信量を使い切った場合
    - AstroWarp+ プランの有効期限に達した場合（該当する場合）
    - インターネット接続を失った場合

5. **Q: 右上の Reset ボタンは何をしますか。**

    A: 認証済みのデバイスをすべて削除し、ルーターの役割を選び直すためのロール選択ページに戻します。

6. **Q: ホームルーター側で AstroWarp をリセットすると、旅行用ルーターはどうなりますか。**

    A: ホームルーター側で AstroWarp をリセットすると、リモート接続されているデバイスは AstroWarp ネットワークから切断され、インターネット接続にはローカルネットワークへ戻ります。

7. **Q: ホームルーターを AstroWarp+ プランにアップグレードしたあと、まだ有効期間内に役割を旅行用ルーターへ切り替えた場合、残りの利用期間は保持されますか。**

    A: 残りの有効期間は保持されず、期限日になると失効します。不要な損失を避けるため、現在のプランが期限切れになってからデバイスの役割を切り替えてください。

8. **Q: ルーターの Web Admin Panel で新しい AstroWarp を有効にした場合、どうすれば無効にして従来版 AstroWarp に戻せますか。**

    A: ルーターの Web Admin Panel で **CLOUD SERVICES** -> **AstroWarp** に移動し、右上の **Reset** をクリックします。

    ![reset](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/reset.png){class="glboxshadow"}

    その後、クラウドアカウントで [astrowarp.net](https://my.astrowarp.net/#/login){target="_blank"} にログインします。ログイン後、**"+"** ボタンをクリックしてルーターを AstroWarp ネットワークに追加します。

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/add_device.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} にアクセスするか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} までお問い合わせください。
