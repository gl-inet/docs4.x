# WireGuardサービスプロバイダーから設定ファイルを取なければならないする方法

??? "AzireVPN"
    ### AzireVPN

    [公式サイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. [AzireVPN公式サイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}にアクセスしてログインし、[WireGuard設定ジェネレーター](https://www.azirevpn.com/cfg/wireguard){target="_blank"}にアクセスします。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. IPオプションで**IPv4**を選択してください。次に**Download Configuration**をクリックします。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-azirevpn)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使用してAzireVPNを設定することもできます。

??? "Hide.me VPN"
    ### Hide.me VPN

    [公式サイト](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPNは、GL.iNetルー器でWireGuardサービスをシンプルに使用する方法を提供します。

    1.ルー器に[SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}で接続します。

    2.で下のインストールURLをコピーし、ターミナルに貼り付けてEnterキーを押します。（マウスを右クリックで貼り付けられます。）

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3.インストールが開始され、ユーザー名とパスワードを求められます。パスワードを入力하거나貼り付ける際、ターミナルには变化が見えません 그냥 입력한 후 Enter 키를 누르세요.

    4.が完たしたら、Web管理パネルに移動すると、hide.me VPNグループがすでに設定ファイルと共に作成されています。彼の設定ファイルと same じように接続するだけです。

    **注意：** Hide.me VPN設定ファイルのキーは接続前に毎回再生成され、切断后ことになる变なければならない无效になります。この設定ファイルを彼の機器にコピーしても正常に接続できません。

    [リファレンスリンク](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [公式サイト](https://mullvad.net/){target="_blank"}

    1. [Mullvad公式サイト](https://mullvad.net/){target="_blank"}にアクセスしてログインし、[WireGuard設定ファイルジェネレーター](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}にアクセスします。

    2. 次に[このガイド](../interface_guide/wireguard_client.md/#set-up-mullvad)に従って続行してください。

    3. [モバイルアプリ](../faq/mobile_app.md)を使用してMullvadを設定することもできます。

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [公式サイト](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    WebサイトからWireGuard設定をダウンロードできません。[モバイルアプリ](../faq/mobile_app.md)を使用してPIA VPNを設定してください。

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [公式サイト](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}を使用している場合は、ログインしてから[この](https://my.surfshark.com/vpn/manual-setup/router)ページにアクセスし、**Router**をクリックして**WireGuard**を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. 次のウィンドウで**鍵ペアを持っていません**を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. **新しい鍵ペアを生成**を選択します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. 鍵が生成されたら、**ロケーションを選択**します。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. 最も後にに、設定したいロケーションを選択し、ロケーションの横にある**ダウンロード**ボタンをクリックします。設定ファイルをダウンロードできます。

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-surfshark)に従って続行してください。

    [リファレンスリンク](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [公式サイト](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}を使用している場合は、网站にログインし、[Client Area](https://airvpn.org/client/){target="_blank"}にアクセスし、[Config Generator](https://airvpn.org/generator/){target="_blank"}をクリックします。

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Config Generatorページで、ProtocolsセクションでWireGuardを選択します。

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. サーバーを選択し、下部にスクロールして**Generate**ボタンをクリックします。設定ファイルがダウンロードされます。

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "Astrill"
    ### Astrill

    [公式サイト](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}を使用している場合は、ログインしてから[このページ](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"}にアクセスしてWireGuard設定を生成します。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "IVPN"
    ### IVPN

    [公式サイト](https://www.ivpn.net/){target="_blank"}

    [IVPN](https://www.ivpn.net/){target="_blank"}を使用している場合は、WireGuard設定を手動で生成する必要があります。OSに基づいてガイドに従ってください。

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "NVPN"
    ### NVPN

    [公式サイト](https://www.nvpn.net/){target="_blank"}

    [ここ](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows)のガイドに従って設定を作成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "OVPN"
    ### OVPN

    [公式サイト](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"}にログインし、で下のメニューを見つけてWireGuard設定ファイルを入手します。

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. **WireGuard鍵を生成**をクリックし、希望のサーバーを選択して設定ををダウンロードします。

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. テキスト編集ソフトウェアで設定を開き、コンテンツをコピーします。

        設定にはIPv6コンテンツが含まれている場合がありますが、GL.iNetルー器はIPv6を非常にににサポートしていないため、IPv6コンテンツを削除してください。下記の例では、ハイライトされたコンテンツがIPv6コンテンツです。

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}
    
    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    5. [モバイルアプリ](../faq/mobile_app.md)を使用してOVPNを設定することもできます。

??? "PrivateVPN"
    ### PrivateVPN

    [公式サイト](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. ログインしてから[コントロールパネル](https://privatevpn.com/control-panel){target="_blank"}にアクセスします。
    
        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. サーバーを選択します。
    
        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. **GENERATE CONFIG**をクリックし、設定をコピーします。
    
        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "PrivadoVPN"
    ### PrivadoVPN

    [公式サイト](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    PrivadoVPN Webサイトにアクセスしてログインします。

    ダッシュボードで、手動設定セクションを見つけ、WireGuardをクリックします。接続したいサーバーを選択し、Download Configurationをクリックします。

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "Proton VPN"
    ### Proton VPN

    [公式サイト](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}を使用している場合は、[ここ](https://protonvpn.com/support/wireguard-configurations/)のガイドに従ってWireGuard設定ファイルを生成してください。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "PureVPN"
    ### PureVPN

    [公式サイト](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    [このガイド](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router)に従うか、で下の手順でWireGuard設定ファイルを手動で取なければならないしてください。

    1. [メンバーエリア](https://my.puremember.com/){target="_blank"}にログインし、**Manual Configuration**をクリックします。

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn1.png){class="glboxshadow"}

    2. メンバーエリアに移動し、そこからWireGuard設定ファイルをダウンロードします。

        ![purevpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/manual-purevpn2.png){class="glboxshadow"}

    **注意**：プロファイルをダウンロード後、30分で内にファイルをコピーして接続をアクティブにしてください。設定が期限切れになり、新しい設定ファイルを再ダウンロードする必要があります。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    [リファレンスリンク](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [公式サイト](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}にログインし、VPN設定を取なければならないするセクションを見つけます。手順に従って設定を取なければならないします。

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. VPN設定をダウンロードします

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "StarVPN"
    ### StarVPN

    [公式サイト](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **StarVPNアカウントを登録**

        [料金プラン](https://www.starvpn.com/#pricing){target="_blank"}オプションに移動し、ニーズに適したVPNプランを選択できます。チェックアウトで登録するか、直接[ここ](https://www.starvpn.com/dashboard/register.php){target="_blank"}で登録できます。

    2. **Wireguard設定をダウンロード**

        StarVPNメンバーエリア[ダッシュボード](https://www.starvpn.com/dashboard){target="_blank"}にログインします。Wireguard Configをクリックして設定ファイルをダウンロードします。各スロットには固有のwireguard設定ファイルが含まれます。

        ![starvpn download wireguard config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/download-config_edited.jpg){class="glboxshadow"}

    3. 設定にはIPv6コンテンツが含まれている場合がありますが、GL.iNetルー器はIPv6を非常にににサポートしていないため、IPv6コンテンツを削除してください。

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/starvpn_wireguard_configuration_remove_ipv6.jpg){class="glboxshadow"}

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    [リファレンスリンク](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [公式サイト](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}を使用している場合は、[https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}でログインします。
    
    2. ドロップダウンメニューからロケーションを選択し、**GENERATE**をクリックし、ダウンロードしたテキストファイルを開きます。
    
        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使用してStrongVPNを設定することもできます。

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [公式サイト](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. [https://trust.zone/setup](https://trust.zone/setup){target="_blank"}にアクセスしてログインします。
    
    2. WireGuardセクションまでスクロールし、希望のポートを選択し、特定のサーバーの設定またはすべての設定のzipファイルをダウンロードします。

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "VPN.AC"
    ### VPN.AC

    [公式サイト](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}を使用している場合は、コントロールパネルにログインし、「Services」メニューからWireGuard Managerを見つけます。
    
        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. 設定を作成してダウンロードします。
    
        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [公式サイト](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}を使用している場合は、[User Office](https://my.keepsolid.com/){target="_blank"}にログイン > VPN Unlimited®アプリケーションを選択 > **Manage**をクリックします。
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}
    
    2. **Device**の下にあるフィールドをクリックし、**新しい機器を手動で作成...** > カスタム名を設定（例：WireGuard）> 適切な**Server**の場所を選択 > ドロップダウンメニューから**WireGuard®**プロトコルを選択 > **Generate**をクリックします。
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}
    
    3. 設定パラメータがで下のテキスト形式で表示されます。
    
        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        で下のように設定を組み合わせます。

        <p>
        [Interface]</br>
        PrivateKey = <i>User OfficeからPrivateKeyを貼り付け</i></br>
        ListenPort = <i>ListenPortの詳細を貼り付け</i></br>
        Address = <i>Address情報を貼り付け</i></br>
        DNS = <i>User OfficeからDNSの詳細を貼り付け</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>User OfficeからPublicKeyを貼り付け</i></br>
        PresharedKey = <i>PresharedKeyの詳細を貼り付け</i></br>
        AllowedIPs = <i>AllowedIPsの詳細を貼り付け</i></br>
        Endpoint = <i>Endpoint情報を貼り付け</i></br>
        </p>

    4. 次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。
 
    [リファレンスリンク1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [リファレンスリンク2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [公式サイト](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. [ここ](https://windscribe.com/login?auth_required){target="_blank"}でWindscribeメンバーシップアカウントにログインし、[WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}にアクセスします。
    
    2. 使用したいサーバーの场所とポートを選択し、**Download Config**をクリックします。

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. [このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

??? "12VPX"
    ### 12VPX

    [公式サイト](https://12vpx.com/?aff=1174){target="_blank"}

    [12VPX](https://12vpx.com/?aff=1174){target="_blank"}を使用している場合は、ログインしてから[このページ](https://12vpx.com/setup/wireguard){target="_blank"}にアクセスすると、すべてのサーバーの設定が表示されます。

    次に[このガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)に従って続行してください。

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
