# GL.iNetルー器でOpenVPN TAP-S2Sモードを有効にする方法

## 使用シナリオ

TAP-S2Sモードを有効にすると、OpenVPNクライアント機器はリモートでOpenVPNサーバー機器にアクセスでき、OpenVPNサーバー機器もリモートでOpenVPNクライアント機器にアクセスできます。ただし欠時は、TAP-S2Sモードを有効にするとOpenVPNクライアントから身が設定したVPNルールが有効にならないことです。

## TAP-S2S vs TUNモード

ネットワーク構成

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2SとTUNモードは物理のな接続方法は同じですが、論理の接続方法は異なります。違いは以下の通りです：

1. GL-X3000 LAN側の機器がGL-MT6000の管理バックエンドにアクセスする際、TAP-S2SモードはバーチャルIPを使用し，TUNモードは使用しません。
2. GL-X3000 LAN側の機器がGL-X3000の管理バックエンドにアクセスする際、TAP-S2SモードはバーチャルIPを使用し，TUNモードは使用しません。
3. GL-X3000 LAN側の機器がGL-MT6000 LAN側の機器のIPアドレスを知っている場合、TAP-S2Sモードは直接リモートアクセスできますが、TUNモードは追加設定を有効にしないと直接アクセスできません。
4. TAP-S2Sモードでは、GL-X3000はGL-MT6000を経よりしてインターネットにアクセスする必要がありますが、TUNモードではGL-X3000は直接インターネットにアクセスできます。したがって、TAP-S2Sモードでは、GL-X3000に設定されたVPNルールは有効にならず、GL-MT6000に設定されたVPNルールに従う必要があります。

## チュートリアル

まず、パブリックIPを持つルー器（GL-MT6000と仮定）を使用してOpenVPNサーバーを開き、機器モードを**TAP-S2S**に設定し、**Apply**をクリックしてから**Export Client Configuration**をクリックします。

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

また、パブリックIPを持つルー器（GL-X3000と仮定）を使用してOpenVPNクライアントを開き、上記の手順でダウンロードした設定ファイルをインポートし、**Apply**をクリックしてから機能を有効にします。

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

このとき、GL-X3000ルー器のIPアドレスが变よりされます。GL-MT6000管理ダッシュボードにログインし、**Clients**を開いて、GL-X3000の新しいIPアドレスを見つけることができます。

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

GL-MT6000がネットワーク接続を失ったか OpenVPNサーバーをオフにした場合、またはGL-X3000がOpenVPNクライアントをオフにした場合、GL-X3000のIPアドレスが復元されます。

注意時：

- 両方の機器をv4.5で上にアップグレードする必要があります。でない場合、接続できません；
- TAP-S2SはGlobal Proxy Modeでのみ機能し、OpenVPNに伴い 自動的に調整されます.
- この機能を有効にすると、以下の機能を使用できません：VPNサーバー、Adguard Home、 Parental Control、ZeroTier、Tailscale、Tor、Firewall、Multi-WAN、LAN、DNS、Network Mode、IPv6、MAC Address、Drop-in Gateway、IGMP Snoopingなど。

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
