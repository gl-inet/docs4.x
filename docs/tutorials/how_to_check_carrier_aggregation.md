# セルラールーターのキャリアアグリゲーションステータスを確認する方法

キャリアアグリゲーションは、複数のネットワークバンドを組み合わせて、セルラー接続の帯域幅と速度を向上させる技術です。GL.iNetの携帯ルーターでは、ルーター管理パネルからキャリアアグリゲーションのステータスを確認できます：

| ルーターモデル                  | サポート   |
| :----------------------------- | :-------: |
| Spitz AX (GL-X3000)            | √         |
| Puli AX (GL-XE3000)            | √         |
| Mudi V2 (GL-E750V2)            | √         |
| Mudi (GL-E750)                 | √         |
| Spitz (GL-X750)                | √         |
| Collie (GL-X300B)              | √         |
| Puli (GL-XE300)                | √         |
| Cirrus (GL-AP1300LTE)          | √         |

（キャリアアグリゲーションはルーター管理パネル内で有効にすることはできません。この機能はGL.iNetではなく、SIMキャリアによって提供されます。）

キャリアアグリゲーションのステータスを確認するには、次の手順に従います：

1. SIMカードをルーターに挿入していることを確認してください。
2. ウェブブラウザのアドレスバーに「192.168.8.1」と入力し、サインインします。
3. 右側のアイコンをクリックします。
    ![アイコンをクリック](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/cellular-click-icon-right.png){class="glboxshadow"}
4. **ATコマンドフィールド**に「**AT+QCAINFO**」と入力します。
5. **送信**をクリックします。

キャリアアグリゲーションが有効な場合、リストに複数のネットワークバンドが表示されます。

![ATCINFO](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-information.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com)をご覧ください。