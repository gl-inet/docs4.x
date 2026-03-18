# WireGuardサービスプロバイダーから設定ファイルを取得する方法

??? "AzireVPN" ### AzireVPN

    [公式サイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. [AzireVPN公式サイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}にアクセスしてログインし、[WireGuard Configuration Generator](https://www.azirevpn.com/cfg/wireguard){target="_blank"}を開きます。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. IP オプションで **IPv4** を選択し、**Download Configuration** をクリックします。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-azirevpn)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使って AzireVPN を設定することもできます。

??? "Hide.me VPN" ### Hide.me VPN

    [公式サイト](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN は、GL.iNet ルーターで WireGuard を簡単に利用する方法を提供しています。

    1. ルーターへ [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"} で接続します。

    2. 以下のインストール URL をコピーし、ターミナルに貼り付けて Enter キーを押します。右クリックで貼り付けできます。

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. インストールが開始されると、ユーザー名とパスワードの入力を求められます。パスワードを入力または貼り付けてもターミナル上には表示されませんが、そのまま Enter キーを押してください。

    4. 完了したら Web 管理パネルを開きます。すでに設定ファイル付きの `hide.me VPN` グループが作成されているので、ほかの設定ファイルと同様に接続してください。

    **Note:** Hide.me VPN の設定ファイル内のキーは接続前に毎回再生成され、切断後は無効になります。そのため、この設定ファイルを別の機器へコピーしても正常には接続できません。

    [参考リンク](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad" ### Mullvad

    [公式サイト](https://mullvad.net/){target="_blank"}

    1. [Mullvad公式サイト](https://mullvad.net/){target="_blank"}にアクセスしてログインし、[WireGuard configuration file generator](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}を開きます。

    2. 次に[このガイド](../interface_guide/wireguard_client.md/#set-up-mullvad)に従って続行してください。

    3. [モバイルアプリ](../faq/mobile_app.md)を使って Mullvad を設定することもできます。

??? "PIA (Private Internet Access)" ### PIA (Private Internet Access)

    [公式サイト](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Web サイトからは WireGuard 設定をダウンロードできません。[モバイルアプリ](../faq/mobile_app.md)を使って PIA VPN を設定してください。

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark" ### Surfshark

    [公式サイト](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} を利用している場合は、ログイン後に[このページ](https://my.surfshark.com/vpn/manual-setup/router)を開き、**Router** をクリックして **WireGuard** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. 次の画面で **I don't have a key pair** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. **Generate a new key pair** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. キーが生成されたら、**Choose a location** を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. 最後に、設定したいロケーションを選び、ロケーション横の **download** ボタンをクリックします。設定ファイルをダウンロードできます。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-surfshark)に従って続行してください。

    [参考リンク](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN" ### AirVPN

    [公式サイト](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"} を利用している場合は、Web サイトにログインし、[Client Area](https://airvpn.org/client/){target="_blank"} を開いてから [Config Generator](https://airvpn.org/generator/){target="_blank"} をクリックします。

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Config Generator ページの Protocols セクションで WireGuard を選択します。

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. サーバーを選択し、ページ下部までスクロールして **Generate** をクリックします。設定ファイルがダウンロードされます。

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "Astrill" ### Astrill

    [公式サイト](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"} を利用している場合は、ログイン後に [このページ](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} を開き、WireGuard 設定を生成します。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "IVPN" ### IVPN

    [公式サイト](https://www.ivpn.net/){target="_blank"}

    [IVPN](https://www.ivpn.net/){target="_blank"} を利用している場合は、WireGuard 設定を手動で生成する必要があります。使用している OS に応じたガイドに従ってください。

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "NVPN" ### NVPN

    [公式サイト](https://www.nvpn.net/){target="_blank"}

    [こちら](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows) のガイドに従って設定を作成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "OVPN" ### OVPN

    [公式サイト](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} にログインし、以下のメニューから WireGuard 設定ファイルを取得します。

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. **Generate WireGuard keys** をクリックし、希望するサーバーを選んで設定をダウンロードします。

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. テキストエディターで設定ファイルを開き、内容をコピーします。

        設定ファイルには IPv6 の記述が含まれる場合がありますが、GL.iNet ルーターでは IPv6 のサポートが十分でないため、IPv6 関連の記述は削除してください。下の例では、ハイライトされている部分が IPv6 の記述です。

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    5. [モバイルアプリ](../faq/mobile_app.md)を使って OVPN を設定することもできます。

??? "PrivateVPN" ### PrivateVPN

    [公式サイト](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. ログインしてから [コントロールパネル](https://privatevpn.com/control-panel){target="_blank"} にアクセスします。

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. サーバーを選択します。

        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. **GENERATE CONFIG** をクリックし、設定内容をコピーします。

        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "PrivadoVPN" ### PrivadoVPN

    [公式サイト](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    PrivadoVPN の Web サイトにアクセスしてログインします。

    ダッシュボードで手動設定セクションを見つけ、WireGuard をクリックします。接続したいサーバーを選択し、**Download Configuration** をクリックします。

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "Proton VPN" ### Proton VPN

    [公式サイト](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} を利用している場合は、[こちら](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} のガイドに従って WireGuard 設定ファイルを生成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "PureVPN" ### PureVPN

    [公式サイト](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    [このガイド](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} を参照するか、以下の手順で WireGuard 設定ファイルを手動取得してください。

    1. [メンバーエリア](https://my.puremember.com/){target="_blank"}にログインし、**Manual Configuration**をクリックします。

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn1.png){class="glboxshadow"}

    2. Member Area から WireGuard 設定ファイルをダウンロードします。

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn2.png){class="glboxshadow"}

    **Note**: プロファイルをダウンロードした後は、30 分以内にファイルをコピーして接続を有効化してください。期限を過ぎると設定が失効し、再度ダウンロードが必要になります。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    [参考リンク](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN" ### SpiderVPN

    [公式サイト](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"} にログインし、VPN 設定を取得するセクションを見つけて、案内に従って設定を取得します。

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. VPN 設定をダウンロードします。

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "StarVPN" ### StarVPN

    [公式サイト](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **StarVPN アカウントを登録する**

        [料金プラン](https://www.starvpn.com/#pricing){target="_blank"}ページで、自分に合った VPN プランを選択します。決済時に登録するか、直接[こちら](https://www.starvpn.com/dashboard/register.php){target="_blank"}から登録できます。

    2. **WireGuard 設定をダウンロードする**

        StarVPN のメンバーエリア [dashboard](https://www.starvpn.com/dashboard){target="_blank"} にログインします。`Wireguard Config` をクリックして設定ファイルをダウンロードします。各スロットには固有の WireGuard 設定ファイルが含まれます。

        ![starvpn download wireguard config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/download-config_edited.jpg){class="glboxshadow"}

    3. 設定ファイルに IPv6 の記述が含まれている場合があります。GL.iNet ルーターでは IPv6 のサポートが十分でないため、IPv6 関連の記述を削除してください。

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/starvpn_wireguard_configuration_remove_ipv6.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    [参考リンク](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}

??? "StrongVPN" ### StrongVPN

    [公式サイト](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} を利用している場合は、[https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"} にログインします。

    2. ドロップダウンメニューからロケーションを選択し、**GENERATE** をクリックして、ダウンロードしたテキストファイルを開きます。

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使って StrongVPN を設定することもできます。

??? "TRUST.ZONE" ### TRUST.ZONE

    [公式サイト](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. [https://trust.zone/setup](https://trust.zone/setup){target="_blank"} にアクセスしてログインします。

    2. WireGuard セクションまでスクロールし、希望するポートを選択して、特定サーバーの設定またはすべての設定を含む zip ファイルをダウンロードします。

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "VPN.AC" ### VPN.AC

    [公式サイト](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"} を利用している場合は、コントロールパネルにログインし、`Services` メニューから `WireGuard Manager` を開きます。

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. 設定を作成してダウンロードします。

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "VPN Unlimited(KeepSolid)" ### VPN Unlimited(KeepSolid)

    [公式サイト](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"} を利用している場合は、[User Office](https://my.keepsolid.com/){target="_blank"} にログインし、VPN Unlimited アプリケーションを選択して **Manage** をクリックします。

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}

    2. **Device** の下にあるフィールドをクリックし、**Manually create a new device...** を選択します。カスタム名（例: WireGuard）を設定し、適切な **Server** ロケーションを選び、ドロップダウンから **WireGuard** プロトコルを選択して **Generate** をクリックします。

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}

    3. 設定パラメータが以下のようなテキスト形式で表示されます。

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        以下の形式で設定を組み立てます。

        <p>
        [Interface]</br>
        PrivateKey = <i>User Office から PrivateKey を貼り付け</i></br>
        ListenPort = <i>ListenPort の値を貼り付け</i></br>
        Address = <i>Address の値を貼り付け</i></br>
        DNS = <i>User Office から DNS の値を貼り付け</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>User Office から PublicKey を貼り付け</i></br>
        PresharedKey = <i>PresharedKey の値を貼り付け</i></br>
        AllowedIPs = <i>AllowedIPs の値を貼り付け</i></br>
        Endpoint = <i>Endpoint の値を貼り付け</i></br>
        </p>

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    [参考リンク1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [参考リンク2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe" ### Windscribe

    [公式サイト](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. [こちら](https://windscribe.com/login?auth_required){target="_blank"} から Windscribe アカウントにログインし、[WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"} を開きます。

    2. 利用したいサーバーロケーションとポートを選択し、**Download Config** をクリックします。

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. [このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "12VPX" ### 12VPX

    [公式サイト](https://12vpx.com/?aff=1174){target="_blank"}

    [12VPX](https://12vpx.com/?aff=1174){target="_blank"} を利用している場合は、ログイン後に [このページ](https://12vpx.com/setup/wireguard){target="_blank"} を開くと、すべてのサーバー設定が表示されます。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
