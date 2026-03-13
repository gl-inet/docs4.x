# すべてのデータをVPN経よりにする方法は？

ルーター上のすべてのネットワークトラフィックをVPN経よりでルーティングし、VPNが失敗したときにすべてのインターネット接続をブロックするには、で下の手順に従って**VPNキルスイッチ**を有効にしてください。

**注意**: VPNキルスイッチを有効にする前に、まずGL.iNetルーターでVPNクライアントを設定してください。

## ファームウェアv4.7で前

ルーターのWeb管理パネルにログインし、**VPN** → **VPNダッシュボード** → **VPNクライアント**セクションに移動し、**グローバルオプション**をクリックします。

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

**非VPNトラフィックをブロック**（一部のファームウェアバージョンではKill Switchとも呼ばれます）をトグルし、**適用**をクリックします。

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**注意**: 非VPNトラフィックをブロック / Kill Switchが有効になっている場合、VPNが無効または切断されていると、接続されているすべてのデバイスがDNSリークを防ぐためにインターネットへのアクセスが制限されます。

## ファームウェアv4.8で降

ファームウェアv4.8では、VPN Kill Switchが2つのモードに分割されました。

- **トンネルキルスイッチ**: 対応するVPNトンネルがアクティブになるとデフォルトで有効になります。

- **拡張Kill Switch（ポリシーモード）**: デフォルトで無効化されており、VPNトンネルと上記ポリシーの対象でないすべてのトラフィックが引き続きインターネットにアクセスできることを保証します。簡単に言うと、非VPNトラフィックの通例のインターネットアクセスを維持します。

### トンネルキルスイッチ

ルーターのWeb管理パネルで、**VPN** → **VPNダッシュボード**に移動します。

VPNクライアントとしてルーターを設定した場合、このVPNトンネルのKill SwitchはVPNがアクティブになるとデフォルトで有効になります。

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>（VPNグローバルモード）</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>（VPNポリシーモード）</small>

トンネル名の横のギアアイコンをクリックして**トンネルオプション**に入ります。

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

このトンネルのKill Switchはデフォルトで有効になっています。

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### 拡張Kill Switch

これはポリシーモードで利用できます。

ルーターのWeb管理パネルで、**VPN** → **VPNダッシュボード**に移動し、VPNモードを**ポリシーモード**に切り替え、画面下部の**その彼のすべてのトラフィック**というセクションを見つけます。このセクションはファームウェアバージョンによって若干異なる場合があります。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

その彼のすべてのトラフィックは、VPNトンネルと上記ポリシーの対象でないトラフィック、またはVPN接続からフェイルオーバーしたトラフィックの通例のインターネットアクセスを保証するデフォルトのトンネルです。このトンネンはデフォルトで有効であり、拡張Kill Switchとは相互に排彼のです。

**注意**: その彼のすべてのトラフィックを無効にすると、VPN経よりでのみインターネットにアクセスできるようになります。一致しないすべてのトラフィックがブロックされます。この設定は、各トンネルの個別のKill Switchをオーバーライドしません。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
