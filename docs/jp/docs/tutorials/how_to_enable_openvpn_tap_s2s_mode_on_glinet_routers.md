# GL.iNetルーターでOpenVPN TAP-S2Sモードを有効にする方法

## 利用シナリオ

TAP-S2S モードを有効にすると、OpenVPN クライアント側のデバイスから OpenVPN サーバー側のデバイスへリモートアクセスでき、OpenVPN サーバー側のデバイスから OpenVPN クライアント側のデバイスへもリモートアクセスできます。ただし、TAP-S2S モードを有効にすると、OpenVPN クライアント側で設定した VPN ルールは適用されなくなります。

## TAP-S2S と TUN モード

ネットワークトポロジー

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2S モードと TUN モードは物理的な接続方法は同じですが、論理的な接続方法が異なります。違いは次のとおりです。

1. GL-X3000 の LAN 側デバイスが GL-MT6000 の管理画面にアクセスする場合、TAP-S2S モードでは仮想 IP を使用しませんが、TUN モードでは使用します。
2. GL-X3000 の LAN 側デバイスが GL-X3000 自身の管理画面にアクセスする場合、TAP-S2S モードでは仮想 IP を使用しますが、TUN モードでは使用しません。
3. GL-X3000 の LAN 側デバイスが GL-MT6000 の LAN 側にあるデバイスの IP アドレスを把握している場合、TAP-S2S モードでは直接リモートアクセスできますが、TUN モードでは追加設定を有効にしないと直接アクセスできません。
4. TAP-S2S モードでは、GL-X3000 は GL-MT6000 を経由してインターネットにアクセスする必要があります。一方、TUN モードでは、GL-X3000 は直接インターネットにアクセスできます。そのため、TAP-S2S モードでは GL-X3000 で設定した VPN ルールは適用されず、GL-MT6000 で設定した VPN ルールに従う必要があります。

## チュートリアル

まず、パブリック IP を持つルーター（ここでは GL-MT6000 とします）で OpenVPN Server を有効にし、デバイスモードを **TAP-S2S** に設定して **Apply** をクリックし、続いて **Export Client Configuration** をクリックします。

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

さらに、別のルーター（ここでは GL-X3000 とします）で OpenVPN Client を有効にし、上記の手順でダウンロードした設定ファイルをインポートして **Apply** をクリックし、その後この機能を有効にします。

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

この時点で、GL-X3000 ルーターの IP アドレスは変わります。GL-MT6000 の管理ダッシュボードにログインし、**Clients** を開くと、GL-X3000 の新しい IP アドレスを確認できます。

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

GL-MT6000 のネットワーク接続が失われた場合、OpenVPN Server を無効にした場合、または GL-X3000 で OpenVPN Client を無効にした場合、GL-X3000 の IP アドレスは元に戻ります。

注意事項:

- 両方のデバイスを v4.5 にアップグレードする必要があります。そうしないと接続できません。
- TAP-S2S は Global Proxy Mode でのみ動作し、OpenVPN を有効にすると自動的に調整されます。
- この機能を有効にすると、次の機能は使用できません: VPN server、Adguard Home、Parental Control、ZeroTier、Tailscale、Tor、Firewall、Multi-WAN、LAN、DNS、Network Mode、IPv6、MAC Address、Drop-in Gateway、IGMP Snooping など。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
