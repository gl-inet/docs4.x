# GL.iNetルーターでOpenVPN TAP-S2Sモードを有効にする方法

## 利用シナリオ

TAP-S2Sモードを有効にすると、OpenVPNクライアント側のデバイスからOpenVPNサーバー側のデバイスへリモートアクセスできるようになり、OpenVPNサーバー側のデバイスからOpenVPNクライアント側のデバイスへもリモートアクセスできます。

ただし、TAP-S2Sモードを有効にすると、OpenVPNクライアント側で設定したVPNルールは有効になりません。

## TAP-S2S と TUN モードの違い

ネットワークトポロジー

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2SモードとTUNモードは物理的な接続方法は同じですが、論理的な接続方法が異なります。主な違いは以下のとおりです。

1. GL-X3000 のLAN側デバイスが GL-MT6000 の管理画面へアクセスする場合、TAP-S2Sモードでは仮想IPを使用しませんが、TUNモードでは仮想IPを使用します。
2. GL-X3000 のLAN側デバイスが GL-X3000 自身の管理画面へアクセスする場合、TAP-S2Sモードでは仮想IPを使用しますが、TUNモードでは使用しません。
3. GL-X3000 のLAN側デバイスが GL-MT6000 のLAN側デバイスのIPアドレスを把握している場合、TAP-S2Sモードでは直接リモートアクセスできますが、TUNモードでは追加設定を有効にしないと直接アクセスできません。
4. TAP-S2Sモードでは、GL-X3000 は GL-MT6000 を経由してインターネットへアクセスする必要があります。一方、TUNモードでは GL-X3000 から直接インターネットへアクセスできます。そのため、TAP-S2Sモードでは GL-X3000 側で設定したVPNルールは有効にならず、GL-MT6000 側で設定したVPNルールに従う必要があります。

## 手順

まず、パブリックIPアドレスを持つルーターを1台用意します。ここでは GL-MT6000 を例にします。このルーターで OpenVPN Server を有効にし、Device Mode を **TAP-S2S** に設定して **Apply** をクリックし、続いて **Export Client Configuration** をクリックします。

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

次に、別のルーターを1台用意します。ここでは GL-X3000 を例にします。このルーターで OpenVPN Client を有効にし、上の手順でダウンロードした設定ファイルをインポートして **Apply** をクリックし、その後クライアント機能を有効にします。

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

このとき、GL-X3000 ルーターのIPアドレスが変わります。GL-MT6000 の管理ダッシュボードにログインし、**Clients** を開くと、GL-X3000 の新しいIPアドレスを確認できます。

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

GL-MT6000 のネットワーク接続が切断された場合、OpenVPN Server を無効にした場合、または GL-X3000 で OpenVPN Client を無効にした場合は、GL-X3000 のIPアドレスは元に戻ります。

注意事項:

- 両方のデバイスを v4.5 以降へアップグレードする必要があります。そうでない場合、接続できません。
- TAP-S2S は Global Proxy Mode でのみ動作し、OpenVPN を有効にすると自動的に調整されます。
- この機能を有効にすると、以下の機能は使用できません。VPN Server、AdGuard Home、Parental Control、ZeroTier、Tailscale、Tor、Firewall、Multi-WAN、LAN、DNS、Network Mode、IPv6、MAC Address、Drop-in Gateway、IGMP Snooping など。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
