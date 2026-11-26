# すべての通信を VPN 経由にするには？ {#how-to-let-all-data-go-through-vpn}

ルーター上のすべてのネットワークトラフィックを VPN 経由でルーティングし、VPN が切断されたときにはすべてのインターネット接続を遮断したい場合は、以下の手順に従って **VPN Kill Switch** を有効にしてください。

**注意**: **VPN Kill Switch** を有効にする前に、まず GL.iNet ルーターで VPN クライアントを設定してください。

## ファームウェア v4.7 以前 {#for-firmware-v47-or-earlier}

ルーターの Web 管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Client** に移動して、**Global Options** をクリックします。

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

**Block Non-VPN Traffic**（一部のファームウェアバージョンでは Kill Switch と表示されます）を有効にして、**Apply** をクリックします。

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**注意**: **Block Non-VPN Traffic** / **Kill Switch** が有効な場合、VPN が無効または切断されると、DNS リークを防ぐために、ルーターに接続されたすべてのデバイスのインターネットアクセスが制限されます。

## ファームウェア v4.8 {#for-firmware-v48}

ファームウェア v4.8 では、**VPN Kill Switch** は 2 つのモードに分かれています。

- **Tunnel Kill Switch**: 対応する VPN トンネルが有効になると、デフォルトで有効になります。

- **Enhanced Kill Switch（Policy Mode）**: デフォルトでは無効で、上記の VPN トンネルやポリシーに一致しないすべてのトラフィックも引き続きインターネットへアクセスできるようにします。つまり、非 VPN トラフィックの通常のインターネットアクセスを維持します。

### Tunnel Kill Switch {#tunnel-kill-switch}

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

### Enhanced Kill Switch {#enhanced-kill-switch}

この機能は **Policy Mode** で利用できます。

ルーターの Web 管理パネルで、**VPN** -> **VPN Dashboard** に移動し、VPN モードを **Policy Mode** に切り替えます。次に、画面下部にある **All Other Traffic** セクションを探します。この表示は、ファームウェアバージョンによって若干異なる場合があります。

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** はデフォルトのトンネルです。 上記の VPN トンネルやポリシーに一致しないトラフィックや、VPN のフェイルオーバーによってここに転送されたトラフィックは、通常どおりインターネットにアクセスできます。 このトンネルはデフォルトで有効です。無効にすると、VPN のフェイルオーバーで転送されるはずのトラフィックを含め、該当するトラフィックがすべてブロックされます。設定済みの VPN トンネルを通るトラフィックだけがインターネットにアクセスできます。保護の内容は **Enhanced Kill Switch** と同じです。

**All Other Traffic** **All Other Traffic** の設定は、各トンネルの個別のキルスイッチ設定を上書きしません。

## ファームウェア v4.9 以降 {#for-firmware-v49-and-above}

ファームウェア v4.9 以降では、**Tunnel Kill Switch** と **Enhanced Kill Switch** の 2 種類の VPN キルスイッチを使用できます。

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

ルーターの Web 管理パネルで、**VPN** -> **VPN Dashboard** に移動します。

ルーターを VPN クライアントとして設定している場合、この VPN トンネルの **Kill Switch** は、VPN が有効になるとデフォルトでオンになります。

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

トンネル名の横にある歯車アイコンをクリックし、**Tunnel Options** を開きます。

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

このトンネルの **Kill Switch** はデフォルトで有効になっています。

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Enhanced Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

ルーターの Web 管理パネルで、**VPN** -> **VPN Dashboard** に移動します。 続いて、右上の歯車アイコンをクリックします。

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

トラフィックポリシーには **Allow Non-VPN Traffic** と **Enhanced Kill Switch** の 2 つのオプションがあります。

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic**: デフォルトで有効です。 上記の VPN トンネルやポリシーに一致しないトラフィックや、VPN のフェイルオーバーによってここに転送されたトラフィックは、通常どおりインターネットにアクセスできます。

- **Enhanced Kill Switch**: 有効にすると、すべてのデバイスは VPN 経由でのみインターネットにアクセスできます。どの VPN トンネルにも一致しないトラフィックはブロックされます。この設定は、各トンネルの個別のキルスイッチ設定を上書きしません。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
