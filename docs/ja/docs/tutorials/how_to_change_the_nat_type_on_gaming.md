# ゲームで NAT タイプを変更する方法 {#how-to-change-the-nat-type-on-gaming}

一部のゲーム開発者は、NAT タイプを改善するためにルーターで UPnP を有効にすることを推奨しています。ただし、UPnP には潜在的なセキュリティリスクがあります。

ルーターで DMZ またはポート転送を設定することでも同じ目的を達成できます。どちらの機能も、有効にする前に仕組みと関連するセキュリティリスクを理解してください。

## ゲーム機の IP アドレスを確認する {#check-your-game-ip}

まず、ルーターにログインしてください。クライアント一覧に移動し、ゲーム機に割り当てられている IP アドレスを確認します。以降の設定ではこの IP アドレスを使用します。

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## 方法 1: DMZ {#method-1-dmz}

サイドバーの **Network** -> **Port Forwarding** に移動し、ゲーム機の IP アドレスを指定して DMZ を有効にします。

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## 方法 2: ポート転送 {#method-2-port-forward}

サイドバーの **Network** -> **Port Forwarding** に移動し、ゲーム機の IP アドレスを指定して必要なポートを追加します。

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

例: PS5 のポート

UDP 3074, 3478-3479

TCP 1935, 3478-3480


![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox のポート

UDP 88, 3074

TCP 3074

ゲームによっては、別のポートを転送する必要がある場合があります。詳しくは、以下のサイトを参照してください。

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

遅延を改善するために Full Cone NAT を有効にできます。この機能はファームウェア v4.5 以降で利用できます。

**Network** -> **NAT Settings** に移動し、必要に応じて **Full Cone NAT** を有効にして、**Apply** をクリックしてください。

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
