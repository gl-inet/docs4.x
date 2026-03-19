# ゲームでNATタイプを変更する方法

多くのゲームメーカーは、より良い NAT タイプを得るためにルーターで UPnP を有効にするよう案内しています。しかし、UPnP は安全性の低いプロトコルであることが知られています。

より安全な方法として、DMZ またはポート転送を使って同じ目的を達成できます。

## ゲーム機のIPアドレスを確認する

クライアント一覧を開き、ゲーム機に割り当てられている IP アドレスを確認します。以下の設定ではこの IP アドレスを使います。

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## 方法1: DMZ

サイドバーで **Network > Port Forwarding** に移動し、ゲーム機の IP アドレスを指定して DMZ を有効にします。

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## 方法2: ポート転送

サイドバーで **Network > Port Forwarding** に移動し、ゲーム機の IP アドレスに対して必要なポートを追加します。

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

例: PS5 のポート

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox のポート

UDP 88, 3074

TCP 3074

ゲームによっては別のポートを転送する必要がある場合があります。詳しくは以下のサイトを参照してください。

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT

遅延を改善したい場合は、**Network > NAT Settings** で Full Cone NAT を有効にできます。

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

- この機能はファームウェア 4.5 以降で利用できます。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
