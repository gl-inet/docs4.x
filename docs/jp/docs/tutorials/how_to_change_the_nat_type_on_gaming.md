# ゲームで NAT タイプを変更する方法

より良い NAT タイプを得るために、ルーターで UPnP を有効にするよう案内しているゲームメーカーは多くあります。しかし、UPnP は安全性の高いプロトコルではないことが知られています。

同じ目的は、DMZ またはポート転送を使って、より安全に実現できます。

## ゲーム機の IP アドレスを確認する

クライアント一覧に移動し、ゲーム機に割り当てられている IP アドレスを確認します。以降の設定ではこの IP アドレスを使用します。

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## 方法 1: DMZ

サイドバーの **Network > Port Forwarding** に移動し、ゲーム機の IP アドレスを指定して DMZ を有効にします。

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## 方法 2: ポート転送

サイドバーの **Network > Port Forwarding** に移動し、ゲーム機の IP アドレスを指定して必要なポートを追加します。

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

## Full Cone NAT

遅延を改善するため、**Network > NAT Settings** で Full Cone NAT を有効にできます。

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* この機能はファームウェア 4.5 以降で利用できます。

---

まだご不明な点がありますか？ [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
