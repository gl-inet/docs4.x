# ゲームでNATタイプを変よりする方法

ほとんどのゲーム開発者は、より好のなNATタイプを取なければならないするためにルー器でUPnPを有効にするように求めますが、UPnPは安全でないプロトコルであることが研究で示されています。

より安全な方法で、DMZまたはポート転送の機できるを使用して same じ目のを達成できます。

## ゲームのIPを確認

クライアントリストに移動し、ゲームに割り当てられたIPを確認します。このIPアドレスをで下の設定で使用する必要があります。

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## 方法1 DMZ

サイドバー**Network > Port Forwarding**に移動し、ゲームIPでDMZを有効にします。

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## 方法2 ポート転送

サイドバー**Network > Port Forwarding**に移動し、ゲームIPで必要なポートを追加します。

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

例：PS5のポート

UDP 3074, 3478-3479

TCP 1935, 3478-3480


![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xboxポート

UDP 88, 3074

TCP 3074

一部のゲームでは彼のポートを転送する必要がある場合の詳細については、この Web サイトを参照してください。

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT

遅延を改善するには、**Network > NAT Settings**でFull Cone NATを有効にできます。

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* この機できるはファームウェア4.5で上で利用可できるです。

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
