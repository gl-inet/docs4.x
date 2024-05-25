# OpenVPN, TAP-S2S vs Tun

## 使用シナリオ

TAP-S2Sモードを有効にすると、OpenVPNクライアントデバイスはリモートでOpenVPNサーバーデバイスにアクセスでき、OpenVPNサーバーデバイスもリモートでOpenVPNクライアントデバイスにアクセスできます。ただし、TAP-S2Sモードを有効にすると、OpenVPNクライアント自身が設定したVPNルールは有効になりません。

## ネットワークトポロジー

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2SとTUNモードは物理的な接続方法は同じですが、論理的な接続方法が異なります。以下はその違いです：

1. GL-X3000のLAN側のデバイスがGL-MT6000の管理バックエンドにアクセスする場合、TAP-S2Sモードでは仮想IPを使用しませんが、TUNモードでは使用します。
2. GL-X3000のLAN側のデバイスがGL-X3000の管理バックエンドにアクセスする場合、TAP-S2Sモードでは仮想IPを使用しますが、TUNモードでは使用しません。
3. GL-X3000のLAN側デバイスがGL-MT6000のLAN側デバイスのIPアドレスを知っている場合、TAP-S2Sモードでは直接リモートアクセスが可能ですが、TUNモードでは追加設定を有効にしないと直接アクセスできません。
4. TAP-S2Sモードでは、GL-X3000はインターネットにアクセスするためにGL-MT6000を経由する必要がありますが、TUNモードではGL-X3000が直接インターネットにアクセスできます。したがって、TAP-S2Sモードでは、GL-X3000が設定したVPNルールは有効にならず、GL-MT6000が設定したVPNルールに従う必要があります。

## チュートリアル

まず、パブリックIPを持つルーター（GL-MT6000と仮定）を使用してOpenVPNサーバーを開き、デバイスモードを**TAP-S2S**に設定し、適用をクリックしてから**クライアント設定のエクスポート**をクリックします。

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

次に、パブリックIPを持つルーター（GL-X3000と仮定）を使用してOpenVPNクライアントを開き、上記の手順でダウンロードした設定ファイルをインポートし、適用をクリックしてから機能を有効にします。

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

この時点で、GL-X3000ルーターのIPアドレスが変更されます。GL-MT6000の管理ダッシュボードにログインし、**クライアント**を開いて、GL-X3000の新しいIPアドレスを見つけます。

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials_new/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

もしGL-MT6000がネットワーク接続を失った場合、またはOpenVPNサーバーをオフにした場合、もしくはGL-X3000がOpenVPNクライアントをオフにした場合、GL-X3000のIPアドレスは元に戻ります。

注意点：

- 両方のデバイスはバージョンv4.5にアップグレードされている必要があり、そうでないと接続できません。
- TAP-S2Sはグローバルプロキシモードでのみ動作し、OpenVPNがオンになると自動的に調整されます。
- この機能を有効にすると、以下の機能は使用できなくなります: VPNサーバー、Adguard Home、ペアレンタルコントロール、ZeroTier、Tailscale、Tor、ファイアウォール、マルチWAN、LAN、DNS、ネットワークモード、IPv6、MACアドレス、ドロップインゲートウェイ、IGMPスヌーピングなど。

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。