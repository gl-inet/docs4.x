# WireGuardサービスプロバイダーから設定ファイルを取得する方法 {#how-to-get-configuration-files-from-wireguard-service-providers}

??? "AzireVPN"
    ### AzireVPN {#azirevpn}

    [公式サイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. [AzireVPN公式サイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} にアクセスしてログインし、[WireGuard Configuration generator](https://www.azirevpn.com/cfg/wireguard){target="_blank"} を開きます。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. IP オプションで **IPv4** を選択し、**Download Configuration** をクリックします。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-azirevpn)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使って AzireVPN を設定することもできます。

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [公式サイト](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN は、GL.iNet ルーターで WireGuard サービスを簡単に利用できる方法を提供しています。

    1. [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"} でルーターに接続します。

    2. 以下のインストール URL をコピーしてターミナルに貼り付け、Enter キーを押します。（右クリックで貼り付けできます。）

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. インストールが開始されると、ユーザー名とパスワードの入力を求められます。パスワードを入力または貼り付けてもターミナル上には表示されませんが、そのまま Enter キーを押してください。

    4. 完了したら Web 管理パネルに移動すると、設定ファイルがすでに入った hide.me VPN グループが作成されていることが分かります。ほかの設定ファイルと同じように接続するだけです。

    **注意:** Hide.me VPN の設定ファイル内のキーは接続のたびに再生成され、切断後は無効になります。そのため、この設定ファイルを他のデバイスにコピーしても正常に接続できません。

    参考: [hide.me VPN for Routers - GitHub](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad {#mullvad}

    [公式サイト](https://mullvad.net/){target="_blank"}

    1. [Mullvad公式サイト](https://mullvad.net/){target="_blank"} にアクセスしてログインし、[WireGuard configuration file generator](https://mullvad.net/en/account/#/wireguard-config){target="_blank"} を開きます。

    2. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-mullvad)に従って続行してください。

    3. [モバイルアプリ](../faq/mobile_app.md)を使って Mullvad を設定することもできます。

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access) {#pia-private-internet-access}

    [公式サイト](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Web サイトから WireGuard 設定をダウンロードできないため、[モバイルアプリ](../faq/mobile_app.md)を使って PIA VPN を設定してください。

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark {#surfshark}

    [公式サイト](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} を利用している場合は、ログインしてから[このページ](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}を開き、**Router** をクリックして **WireGuard** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. 次の画面で **I don't have a key pair** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. **Generate a new key pair** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. キーが生成されたら、**Choose a location** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. 最後に、設定したいロケーションを選び、そのロケーションの横にある **download** ボタンをクリックします。設定ファイルをダウンロードできます。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-surfshark)に従って続行してください。

??? "AirVPN"
    ### AirVPN {#airvpn}

    [公式サイト](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"} を利用している場合は、Web サイトにサインインし、[Client Area](https://airvpn.org/client/){target="_blank"} に移動して [Config Generator](https://airvpn.org/generator/){target="_blank"} をクリックします。

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Config Generator ページで、Protocols セクションから WireGuard を選択します。

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. サーバーを選択し、ページの最後までスクロールして **Generate** ボタンをクリックします。設定ファイルがダウンロードされます。

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "Astrill"
    ### Astrill {#astrill}

    [公式サイト](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"} を利用している場合は、ログインしてから[このページ](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"}を開き、WireGuard 設定を生成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "IVPN"
    ### IVPN {#ivpn}

    [公式サイト](https://www.ivpn.net/){target="_blank"}

    [IVPN](https://www.ivpn.net/){target="_blank"} を利用している場合は、WireGuard 設定を手動で生成する必要があります。お使いの OS に対応するガイドに従ってください。

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "NVPN"
    ### NVPN {#nvpn}

    [公式サイト](https://www.nvpn.net/){target="_blank"}

    [こちら](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"}のガイドに従って設定を作成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "OVPN"
    ### OVPN {#ovpn}

    [公式サイト](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} にログインし、以下のメニューから WireGuard 設定ファイルを取得します。

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. **Generate WireGuard keys** をクリックし、希望するサーバーを選択してから設定をダウンロードします。

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. テキストエディターで設定ファイルを開き、内容をコピーします。

        設定ファイルに IPv6 アドレスが含まれている場合があります。互換性や接続の問題を避けるため、.conf ファイルを開いて IPv6 アドレスを削除してください。下図のハイライト部分が IPv6 の内容です。

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    5. [モバイルアプリ](../faq/mobile_app.md)を使って OVPN を設定することもできます。

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [公式サイト](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. ログインしてから [Control panel](https://privatevpn.com/control-panel){target="_blank"} にアクセスします。

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. サーバーを選択します。

        ![select a server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. **GENERATE CONFIG** をクリックし、設定内容をコピーします。

        ![generate config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [公式サイト](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    PrivadoVPN の Web サイトにアクセスしてログインします。

    ダッシュボードで Manual Configuration セクションを見つけて WireGuard をクリックします。接続したいサーバーを選択し、**Download Configuration** をクリックします。

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [公式サイト](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} を利用している場合は、[こちら](https://protonvpn.com/support/wireguard-configurations/){target="_blank"}のガイドに従って WireGuard 設定ファイルを生成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "PureVPN"
    ### PureVPN {#purevpn}

    [公式サイト](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    PureVPN の設定ファイルを手動で取得するには、[このガイド](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}または以下の手順を参照してください。

    1. [PureVPN Member Area](https://my.puremember.com/){target="_blank"} にアカウントでログインします。ログイン後、左側メニューで **Manual Configuration** をクリックします。

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. 接続先の都市を選択し、右側の **Download** をクリックします。

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. ポップアップウィンドウで、プロトコルとして **WireGuard** を選択します。

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. デバイスタイプとして **Linux** を選択し、**Generate Configuration** をクリックします。設定ファイルがローカルデバイスにダウンロードされます。

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

        **注**: WireGuard 設定は 30 分で期限切れになります。有効期間内に接続を有効化してください。期限を過ぎた場合は、新しい設定を生成する必要があります。

    5. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って設定を完了してください。

    参考: [How to set up PureVPN on GL.iNet router](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN {#spidervpn}

    [公式サイト](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) にログインし、VPN 設定を取得するセクションを見つけて、案内に従って設定を取得します。

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. VPN 設定をダウンロードします。

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "StarVPN"
    ### StarVPN {#starvpn}

    [公式サイト](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **StarVPNアカウントを登録する**

        [料金プラン](https://www.starvpn.com/#pricing){target="_blank"}のページにアクセスし、ニーズに合った VPN プランを選択します。購入手続き時に登録することも、直接[こちら](https://www.starvpn.com/dashboard/register.php){target="_blank"}から登録することもできます。

    2. **WireGuard設定をダウンロードする**

        StarVPN のメンバーエリア [dashboard](https://www.starvpn.com/dashboard){target="_blank"} にログインします。**WireGuard Config** をクリックして設定ファイルをダウンロードします。各スロットには固有の WireGuard 設定ファイルが含まれます。

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/wgconfigdl.png){class="glboxshadow"}

        **ヒント**: AmneziaWG の難読化技術を使いたい場合は、**AmneziaWG Config** をクリックして設定ファイルをダウンロードしてください。各スロットには固有の AmneziaWG 設定ファイルが含まれます。

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **設定ファイルを編集する（任意）**

        設定ファイルに IPv6 アドレスが含まれている場合があります。互換性や接続性の問題を避けるため、以下のように .conf ファイルを開いて IPv6 アドレスを削除してください。

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って、設定ファイルを GL.iNet ルーターにアップロードしてください。

    参考リンク:

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [公式サイト](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} を利用している場合は、[https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"} にサインインします。

    2. ドロップダウンメニューからロケーションを選択し、**GENERATE** をクリックして、ダウンロードしたテキストファイルを開きます。

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使って StrongVPN を設定することもできます。

??? "TRUST.ZONE"
    ### TRUST.ZONE {#trustzone}

    [公式サイト](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. [https://trust.zone/setup](https://trust.zone/setup) にアクセスしてログインします。

    2. WireGuard セクションまでスクロールし、希望するポートを選択してから、特定サーバーの設定ファイルまたはすべての設定をまとめた zip ファイルをダウンロードします。

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [公式サイト](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"} を利用している場合は、コントロールパネルにログインし、"Services" メニューから WireGuard Manager を見つけます。

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. 設定を作成してダウンロードします。

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "VPN Safe"
    ### VPN Safe {#vpn-safe}

    [公式サイト](https://secure.vpnsafe.net/aff.php?aff=6){target="_blank"}

    1. **VPN Safe Dashboard** にログインし、有効な VPN サービスをクリックします。

        ![vpnsafe1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnsafe/vpnsafe1.jpg){class="glboxshadow"}

    2. 製品の詳細ページを下にスクロールして **WireGuard Configuration** を見つけます。

        ![vpnsafe2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnsafe/vpnsafe2.jpg){class="glboxshadow"}

    3. VPN Safe の WireGuard 設定は、必要な設定数に応じて次の 2 つの方法でダウンロードできます。

        - 設定を 1 つダウンロードする場合は、ドロップダウンリストから接続先のサーバーを選択し、**Download Config** をクリックします。WireGuard アプリで右側の QR コードをスキャンして、すばやく接続することもできます。

            ![vpnsafe3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnsafe/vpnsafe3.jpg){class="glboxshadow"}

            ![vpnsafe4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnsafe/vpnsafe4.jpg){class="glboxshadow"}

        - すべての設定をダウンロードする場合は、**Download All** をクリックして ZIP ファイルを取得します。解凍すると、利用可能なすべての設定ファイルが得られます。

            ![vpnsafe5](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnsafe/vpnsafe5.jpg){class="glboxshadow"}

    4. 続いて[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って設定を続けます。

    参考: [How to Add a VPN Safe WireGuard Config to a GL.iNet Router](https://www.youtube.com/watch?v=W-ycLZPeygA&list=PLY3TuHSEidyQ&index=12){target="_blank"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [公式サイト](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"} を利用している場合は、[User Office](https://my.keepsolid.com/){target="_blank"} にサインインし、VPN Unlimited® アプリケーションを選択して **Manage** をクリックします。

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/01.jpg){class="glboxshadow"}

    2. **Device** の下のフィールドを押して **Manually create a new device…** をクリックし、カスタム名（例: WireGuard）を設定します。適切な **Server** ロケーションを選び、ドロップダウンメニューから **WireGuard**® プロトコルを選択して **Generate** をクリックします。

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/02.jpg){class="glboxshadow"}

    3. すると、設定パラメーターが以下のようなテキスト形式で表示されます。

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/03.jpg){class="glboxshadow"}

        以下のように設定を組み立ててください。

        <p>
        [Interface]<br>
        PrivateKey = <i>User Office から PrivateKey を貼り付け</i><br>
        ListenPort = <i>ListenPort の内容を貼り付け</i><br>
        Address = <i>Address の情報を貼り付け</i><br>
        DNS = <i>User Office から DNS の内容を貼り付け</i><br>
        <br>
        [Peer]<br>
        PublicKey = <i>User Office から PublicKey を貼り付け</i><br>
        PresharedKey = <i>PresharedKey の内容を貼り付け</i><br>
        AllowedIPs = <i>AllowedIPs の内容を貼り付け</i><br>
        Endpoint = <i>Endpoint の情報を貼り付け</i><br>
        </p>

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    参考: [How to Configure WireGuard Client on GLiNet Router](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

??? "Windscribe"
    ### Windscribe {#windscribe}

    [公式サイト](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. [こちら](https://windscribe.com/login?auth_required){target="_blank"}から Windscribe のメンバーアカウントにログインし、[WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"} を開きます。

    2. 使用したいサーバーロケーションとポートを選択し、**Download Config** をクリックします。

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. [このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "X-VPN"
    ### X-VPN {#x-vpn}

    [公式サイト](https://xvpn.io/go?aff_id=nk5bu995){target="_blank"}

    X-VPNはファームウェアv4.11以降のGL.iNetルーターに統合されています。

    ファームウェアv4.11以降では、ログイントークンを使ってGL.iNet Web管理パネルからX-VPNへ直接ログインできます。詳しくは[こちら](../interface_guide/wireguard_client.md#set-up-x-vpn)を参照してください。

    ファームウェアがv4.11より前の場合、またはX-VPN設定ファイルを手動でダウンロードする場合は、次の手順に従います。

    1. X-VPNに[ログイン](https://xvpn.io/login){target="_blank"}し、**VPN** -> **VPN on Router**に移動します。

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn1.png){class="glboxshadow"}

    2. 右側の **Step 1** で、プロトコルとして **WireGuard** を選択します。

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn2.png){class="glboxshadow"}

    3. **Step 2** で希望する **Region** と **State/City** を選択し、**Search** ボタンをクリックします。

        ![xvpn wg config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn3.png){class="glboxshadow"}

    4. 検索結果でダウンロードボタンをクリックし、必要なサーバーの設定ファイルを取得します。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "12VPX"
    ### 12VPX {#12vpx}

    [公式サイト](https://12vpx.com/?aff=1174){target="_blank"}

    [12VPX](https://12vpx.com/?aff=1174){target="_blank"} を利用している場合は、ログインしてから[このページ](https://12vpx.com/setup/wireguard){target="_blank"}を開くと、すべてのサーバーの設定が表示されます。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
