# VPN クライアントプロフィール

> このガイドはファームウェア v4.9 以降に適用されます。

Web Admin Panel の左側で、**VPN** -> **VPN Client Profile** に移動します。

ファームウェア v4.9 以降では、[OpenVPN Client](openvpn_client.md) と [WireGuard Client](wireguard_client.md) が 1 つの **VPN Client Profile** ページに統合され、より簡単に管理できるようになりました。レイアウトは多少調整されていますが、基本機能は変わっていません。必要に応じて個別ガイドも参照できます。

このページでは、統合済み VPN サービスの一部にログインして接続用プロファイルを簡単にダウンロードしたり、ほかの VPN プロバイダーの Web サイトからエクスポートした設定ファイルを手動でアップロードしたりできます。必要に応じて、右上で VPN プロトコルを切り替えることも可能です。

## WireGuard

WireGuard® は、最先端の暗号技術を利用した軽量・高性能なモダン VPN です。IPsec よりも高速で簡潔かつ実用的であり、OpenVPN よりも大幅に高いパフォーマンスを発揮します。

GL.iNet ルーターでは、以下の VPN プロバイダー向けに WireGuard の組み込みサポートを提供しています。契約が有効であれば、**VPN Client Profile** ページでサービス認証情報を入力するだけで素早く設定できます。

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

別の WireGuard サービスプロバイダーを利用している場合は、プロバイダーの Web サイトから設定ファイルをダウンロードし、**Add Manually** をクリックしてルーターへアップロードしてください。設定ファイルのダウンロード方法が分からない場合は、[こちら](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) を参照するか、プロバイダーのサポートへお問い合わせください。

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} を例に説明します。

1. **AzireVPN** をクリックします。

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. **Username** と **Password** を入力し、**Save and Continue** をクリックします。

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    利用可能なすべてのサーバーの設定ファイルが生成されます。

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. 実際の利用目的に応じて、以下の案内を参照してください。

    !!! note "Case 1. 接続中のすべてのクライアントに VPN 経由でインターネットアクセスさせたい場合、以下の手順を実行してください。"

        1. 使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. 接続されると、設定ファイルの横に緑色の点が表示されます。

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            これで VPN 接続が有効になり、このルーターに接続されているすべてのクライアントは、安全なインターネットアクセスのために VPN を利用します。

        3. （オプション）VPN 接続が予期せず失敗した場合に、ローカルネットワークのすべてのインターネットアクセスを自動的に遮断し、実際の IP アドレスやオンラインデータが漏洩するのを防ぎ、継続的なプライバシーとセキュリティを確保したい場合は、**VPN Dashboard** に移動して **Kill Switch** を有効にします。

            * 個々の VPN トンネルごとに Kill Switch を設定する方法については、[こちら](vpn_dashboard_v4.9.md#tunnel-options) を参照してください。

            * グローバル VPN 接続（拡張 Kill Switch）の Kill Switch を設定する方法については、[こちら](vpn_dashboard_v4.9.md#all-other-traffic) を参照してください。

    !!! note "Case 2. 代わりに VPN ポリシーをカスタマイズしたい場合は、以下の手順を実行してください。"

        1. 下部の **Go to Dashboard** をクリックします。

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. **VPN Dashboard** に移動して VPN ポリシーを設定します。詳細は [こちら](vpn_dashboard_v4.9.md#set-up-vpn-policy) を参照してください。

## OpenVPN

OpenVPN は、仮想プライベートネットワーク技術を用いて安全なサイトツーサイト接続またはポイントツーポイント接続を確立する、オープンソースの VPN プロトコルです。

GL.iNet ルーターでは、[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"} 向けに OpenVPN の組み込みサポートを提供しています。契約が有効であれば、**VPN Client Profile** ページでサービス認証情報を入力するだけで素早く設定できます。

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

別の OpenVPN サービスプロバイダーを利用している場合は、プロバイダーの Web サイトから設定ファイルをダウンロードし、**Add Manually** をクリックしてルーターへアップロードしてください。設定ファイルのダウンロード方法が分からない場合は、[こちら](openvpn_client.md#get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers) を参照するか、プロバイダーのサポートへお問い合わせください。

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

関連記事

- [VPN Dashboard（ファームウェア v4.9）](vpn_dashboard_v4.9.md)
- [GL.iNet ルーターで WireGuard クライアントを設定する](wireguard_client.md)
- [GL.iNet ルーターで OpenVPN クライアントを設定する](openvpn_client.md)

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
