# GoodPAS

**注意**: この機能はファームウェア v4.10 で導入され、AstroWarp から GoodPAS に名称変更されました。デバイスで古いファームウェアを使用している場合は、[AstroWarp](./astrowarp.md) を参照してください。

---

Web 管理パネルの左側で、**CLOUD SERVICES** -> **GoodPAS** に移動します。

GoodPAS は、GL.iNet ルーター SDK に統合された高度なリモートアクセスソリューションです。トラフィック難読化機能を内蔵した AmneziaWG プロトコルを採用し、いつでもどこでも信頼性の高いリモートアクセスを実現する、安定した安全な接続を提供します。

この機能を使うと、自宅ネットワークへシームレスにリモートアクセスできます。Web 管理パネルで動的アクセスコードを使ってデバイスを直接設定してペアリングでき、登録やログインなしで、旅行用ルーターと自宅ネットワークの安全な接続を数秒で確立できます。

**注意**:

1. GoodPAS を次の機能と同時に使用するとルーティング競合が発生する可能性があるため、同時使用は推奨されません: GoodCloud Site to Site、ZeroTier、Tailscale、Tor。

2. GoodPAS が有効な場合、Network Mode は使用できません。

## クイックセットアップ

次の例では、**Flint 3 (GL-BE9300)** と **Mango 2 (GL-MG1300)** を使用して GoodPAS ネットワークを設定します。

Flint 3 はホームルーター、Mango 2 は旅行用ルーターとして動作します。Mango 2 のネットワークトラフィックは Flint 3 に戻され、インターネットアクセスに使用されます。

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Flint 3 をインターネットに接続します。

    Flint 3 の Web 管理パネルにログインして INTERNET ページを開き、Ethernet、Repeater、Tethering、Cellular のいずれかの対応する方法でインターネットに接続します。

    以下の例では、Flint 3 ホームルーターが Ethernet ケーブルで ISP モデム（Hong Kong Broadband Network Ltd）に接続されています。

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Access Code を生成します。

    Flint 3 の Web 管理パネルで **CLOUD SERVICES** -> **GoodPAS** に移動し、**Use At Home** をクリックします。

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    Access Code が生成されます。あとで使用するため、このコードをコピーします。

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Mango 2 をインターネットに接続します。

    Mango 2 の Web 管理パネルにログインして INTERNET ページを開き、Ethernet、Repeater、Tethering、Cellular のいずれかの対応する方法でインターネットに接続します。

    以下の例では、Mango 2 旅行用ルーターが iPhone 17 のパーソナルホットスポットに接続されています（所在地は深圳で、中国聯通広東省ネットワークを使用）。

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Access Code を入力します。

    Mango 2 の Web 管理パネルで **CLOUD SERVICES** -> **GoodPAS** に移動し、**Use While Travelling** をクリックします。

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    手順 2 で取得した Access Code を入力します。

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    検証が完了するまで待ちます。

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    Flint 3 ホームルーターへの接続が完了します。これで、自宅ネットワーク経由で安全にインターネットを利用できます。

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    Flint 3 の Web 管理パネルにも、以下のように接続状態が表示されます。

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## 接続テスト

1. ノート PC またはスマートフォンを、Mango 2 旅行用ルーターの Wi-Fi に接続します。

2. ブラウザーを開き、[ipcheck.ing](https://ipcheck.ing/){target="_blank"} またはその他の IP アドレス確認サイトにアクセスします。

    Mango 2 のグローバル IP アドレスが表示され、Mango 2 が Flint 3 ホームルーター経由でインターネットにアクセスしていることを確認できます。

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Mango 2 で GoodPAS 接続を切断し、Web ページを再読み込みして IP 照会を再実行します。

    Mango 2 のグローバル IP アドレスが表示され、Mango 2 がローカルネットワーク経由でインターネットにアクセスしていることを確認できます。

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **Q: 動的アクセスコードの形式と有効期限を教えてください。**

    A: 数字と大文字を組み合わせた 8 文字のコードで、有効期限は 10 分です。

2. **Q: ホームルーター側で接続を終了すると、旅行用ルーターはどうなりますか。**

    A: 旅行用ルーターは切断され、ネットワークにアクセスできない保留状態になります。ホームルーター側で接続が再開されると、アクセスコードを再入力しなくても旅行用ルーターは自動的に再接続できます。

3. **Q: どのような場合に旅行用ルーターは保留状態になりますか。**

    A: ホームルーターが次のいずれかの状態になると、旅行用ルーターは保留状態になります。

    - GoodPAS 接続を終了した場合
    - インターネット接続を失った場合

4. **Q: 右上の Reset ボタンは何をしますか。**

    A: 認証済みのデバイスをすべて削除し、ルーターの役割を選び直すためのページに戻します。

5. **Q: ホームルーター側で GoodPAS をリセットすると、旅行用ルーターはどうなりますか。**

    A: ホームルーターをリセットすると、リモート接続中のデバイスは GoodPAS ネットワークから切断され、インターネットアクセスにはローカルネットワークを使用する状態に戻ります。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
