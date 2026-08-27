# セルラールーターでキャリアアグリゲーションの状態を確認する方法

キャリアアグリゲーションは、複数のネットワークバンドを組み合わせることで、セルラー接続の帯域幅を広げ、通信速度を向上させる機能です。

この機能は SIM キャリア側のサポートに依存するため、ルーターの Web 管理画面で有効化することはできません。

ただし、ルーターの Web 管理画面で AT コマンドを使うことで、キャリアアグリゲーションの状態を確認できます。

!!! note "対応モデル"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

以下の手順でキャリアアグリゲーションの状態を確認してください。

1. ルーターに SIM カードを挿入します。
2. Web ブラウザを開き、アドレスバーに `192.168.8.1` と入力してログインします。
3. **INTERNET** -> **Cellular** セクションに移動し、右上の三点アイコンをクリックして **Modem AT Command** をクリックします。

    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. ポップアップウィンドウで **AT+QCAINFO** を入力し、**Send** をクリックします。

    キャリアアグリゲーションが有効な場合は、一覧に複数のネットワークバンドが表示されます。

    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

まだご不明な点がありますか？ [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
