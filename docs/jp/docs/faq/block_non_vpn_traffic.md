# すべての通信を VPN 経由にするには？

ルーター上のすべてのネットワークトラフィックを VPN 経由でルーティングし、VPN が切断されたときにはすべてのインターネット接続を遮断したい場合は、以下の手順に従って **VPN Kill Switch** を有効にしてください。

**注意**: **VPN Kill Switch** を有効にする前に、まず GL.iNet ルーターで VPN クライアントを設定してください。

## ファームウェア v4.7 以前

ルーターの Web 管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Client** に移動して、**Global Options** をクリックします。

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

**Block Non-VPN Traffic**（一部のファームウェアバージョンでは Kill Switch と表示されます）を有効にして、**Apply** をクリックします。

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**注意**: **Block Non-VPN Traffic** / **Kill Switch** が有効な場合、VPN が無効または切断されると、DNS リークを防ぐために、ルーターに接続されたすべてのデバイスのインターネットアクセスが制限されます。

## ファームウェア v4.8 以降

ファームウェア v4.8 では、**VPN Kill Switch** は 2 つのモードに分かれています。

- **Tunnel Kill Switch**: 対応する VPN トンネルが有効になると、デフォルトで有効になります。

- **Enhanced Kill Switch（Policy Mode）**: デフォルトでは無効で、上記の VPN トンネルやポリシーに一致しないすべてのトラフィックも引き続きインターネットへアクセスできるようにします。つまり、非 VPN トラフィックの通常のインターネットアクセスを維持します。

### Tunnel Kill Switch

ルーターの Web 管理パネルで、**VPN** -> **VPN Dashboard** に移動します。

ルーターを VPN クライアントとして設定している場合、この VPN トンネルの **Kill Switch** は、VPN が有効になるとデフォルトでオンになります。

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Global Mode)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Policy Mode)</small>

トンネル名の横にある歯車アイコンをクリックし、**Tunnel Options** を開きます。

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

このトンネルの **Kill Switch** はデフォルトで有効になっています。

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Enhanced Kill Switch

この機能は **Policy Mode** で利用できます。

ルーターの Web 管理パネルで、**VPN** -> **VPN Dashboard** に移動し、VPN モードを **Policy Mode** に切り替えます。次に、画面下部にある **All Other Traffic** セクションを探します。この表示は、ファームウェアバージョンによって若干異なる場合があります。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** は、上記の VPN トンネルやポリシーに一致しないトラフィック、または VPN 接続からフェイルオーバーしたトラフィックについて、通常のインターネットアクセスを確保するためのデフォルトトンネルです。このトンネルはデフォルトで有効になっており、**Enhanced Kill Switch** とは排他的な関係にあります。

**注意**: **All Other Traffic** を無効にすると、インターネットへは VPN 経由でのみアクセスできるようになります。一致しないすべてのトラフィックはブロックされます。この設定は、各トンネルごとの **Kill Switch** を上書きするものではありません。

---

まだご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
