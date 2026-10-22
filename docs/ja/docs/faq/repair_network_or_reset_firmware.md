# ネットワークを修復する方法、または工場出荷時の設定にリセットする方法 {#how-to-repair-network-or-factory-reset}

すべてのGL.iNetルーターには、物理的なリセット機構（リセットボタンまたはピン穴）が備わっています。ボタンを押す場合もピン穴を押す場合も効果は同じで、ネットワーク接続の修復、またはルーターの工場出荷時設定へのリセットを行えます。

ピン穴があるモデルでは、ピン、伸ばしたクリップ、または同様の道具を使用して操作してください。

リセットを実行する前に、ルーターが完全に起動していることを確認してください。電源投入直後にリセットボタンを**押さないでください**。U-Bootフェイルセーフモードが起動する可能性があります。

## ネットワークの修復 {#repair-network}

リセットボタンを**4秒間**押し続けてから放すと、ネットワークを修復するソフトリセットを実行できます。

この操作は、ネットワークインターフェースを再起動し、インターネットインターフェースをデフォルト設定にリセットしますが、Wi-Fi設定、VPN設定、システム設定などは保持されます。

**注意**：

1. Wi-Fiが無効になっている場合、ソフトリセットでWi-Fiがデフォルトの有効状態に復元されます。

2. ソフトリセットは、ルーターモード以外のモードからルーターモードへすばやく切り替える場合にも使用できます。

## 工場出荷状態に戻す {#reset-to-factory}

**タッチスクリーンのないモデル**では、リセットボタンまたは Web 管理パネルの 2 つの方法でファームウェアをリセットできます。このビデオを見るか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/jguDqBWP-Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. 物理的なリセット機構（ボタンまたはピン穴）を使用する

    リセットボタン（またはピン穴にピンを差し込む）を**10秒間**押し続けてから放すと、ルーターが工場出荷時の設定にリセットされます。すべてのユーザーデータがクリアされます。

    **注意：**工場出荷時設定へのリセットで解決しない場合は、[U-Bootチュートリアル](debrick.md)に従ってルーターをデブリックする必要がある場合があります。

2. Web 管理パネルでファームウェアをリセットする

    ルーターの Web 管理パネルにログインし、SYSTEM -> Reset Firmware に移動します。ボタンをクリックしてファームウェアをリセットします。

    **注意：**現在のすべての設定とデータが失われます。処理には約2分かかります。処理中はルーターの電源を絶対に切らないでください。

    ![glinet reset firmware](https://static.gl-inet.com/docs/router/en/4/faq/repair_network_or_reset_firmware/reset_firmware_4.8.png){class="glboxshadow"}

**タッチスクリーン搭載モデル**では、タッチスクリーン、リセットボタン、Web 管理パネルの 3 つの方法でファームウェアをリセットできます。

次の動画では、Mudi 7（GL-E5800）を使ってこれらの方法を紹介しています。同じ手順は、すべてのタッチスクリーン搭載モデルに適用されます。

<iframe width="560" height="315" src="https://www.youtube.com/embed/3Kx_StIFLqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
<small></small>

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
