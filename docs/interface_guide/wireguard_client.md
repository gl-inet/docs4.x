# GL.iNetルーターでのWireGuardクライアントの設定方法

WireGuard®は、**最先端の暗号技術**を利用した、非常にシンプルで高速かつ最新のVPNです。これは、IPSecよりも[高速](https://www.wireguard.com/performance/){target="_blank"}、シンプル、効率的で使いやすく、複雑な問題を回避することを目的としています。また、OpenVPNよりも著しく高性能であることを意図しています。

すでにプロバイダーからWireGuardサービスを購入しているが、設定ファイルの取得方法がわからない場合は、[WireGuardサービスプロバイダーから設定ファイルを取得する](#get-configuration-files-from-wireguard-service-providers)を参照するか、そのサポートに問い合わせてください。

Web管理パネルまたは[モバイルアプリ](../faq/mobile_app.md)を介してWireGuardクライアントを設定できます。モバイルアプリには、AzireVPN、Mullvad VPN、OVPN、StrongVPN、PIA VPNなどのいくつかのWireGuardサービスプロバイダーが統合されています。

Web管理パネルを介して設定する場合は、以下のガイドに従ってください。

AzireVPNまたはMullvadのメンバーシップがある場合は、**AzireVPN**または**Mullvad**ボタンをクリックしてログインするか、**手動で追加**をクリックしてWireGuardプロファイルをアップロードしてください。

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/wireguard_client_no_initialized.png){class="glboxshadow"}

## AzireVPNの設定

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}は、WireGuardのような安全で最新かつ堅牢なトンネルを提供するプライバシー志向のVPNサービスです。

![azirevpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/azirevpn.png){class="glboxshadow"}

1. **ユーザー名**と**パスワード**を入力し、**認証情報の保存とサーバー取得**をクリックします。これにより、各サーバーの設定ファイルが生成されます。

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/azirevpn_generated_profiles.png){class="glboxshadow"}

2. VPNダッシュボードに移動して接続を有効にします。

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    接続すると、ユーザーのIPアドレスと送受信されたバイト数が表示されます。

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. サーバーの更新

    AzireVPNはサーバーのメンテナンスやシャットダウンを行うことがあり、接続が失敗することがあります。**サーバーを更新する**をクリックして、最新の利用可能なサーバーを取得できます。

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/azirevpn_update_servers.png){class="glboxshadow"}

4. 認証情報の編集

    歯車アイコンをクリックして認証情報を編集します。

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/azirevpn_edit_credential.png){class="glboxshadow"}

## Mullvadの設定

[Mullvad](https://mullvad.net/){target="_blank"}は、オンライン活動、身元、位置情報をプライベートに保つVPNサービスです。

ファームウェア4.xには、Mullvad WireGuardサービスが統合されています。

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/mullvad.png){class="glboxshadow"}

1. **アカウント**を入力し、**認証情報の保存とサーバー取得**をクリックします。

    Mullvadアカウント番号は、「1000 0000 0000 0000」から「9999 9999 9999 9999」の範囲の16桁の10進数です。

    ロケーションを選択するダイアログが表示されます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/mullvad_select_servers.png){class="glboxshadow"}

    選択したロケーションサーバーの設定ファイルが生成されます。
    
    **パブリックキー**は、Mullvadサーバーに送信するWireGuardの公開鍵です。同時に最大5つの鍵を持つことができ、WireGuard鍵は[Mullvadのページ](https://mullvad.net/en/account/#/ports){target="_blank"}で管理できます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/mullvad_generated_profiles.png){class="glboxshadow"}

2. VPNダッシュボードに移動して接続を有効にします。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    接続すると、ユーザーのIPアドレスと送受信されたバイト数が表示されます。

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. サーバーの更新

    Mullvadはサーバーのメンテナンスやシャットダウンを行うことがあり、接続が失敗することがあります。**サーバーを更新する**をクリックして、最新の利用可能なサーバーを取得できます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/mullvad_update_servers.png){class="glboxshadow"}

4. 認証情報の編集

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/mullvad_edit_credential.png){class="glboxshadow"}

5. アカウント情報の削除

    **削除**をクリックすると、アカウントの認証情報、秘密鍵、公開鍵、および設定ファイルが**ルーターから**削除されます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/wgclient_delete_all.png){class="glboxshadow"}

6. 削除

    すべての設定ファイルをワンクリックで削除し、秘密鍵と公開鍵も削除するかどうかを確認するプロンプトを表示します。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/wgclient_delete_all_configuration_file.png){class="glboxshadow"}


## WireGuardクライアントの設定
ファームウェア4.0以降では、WireGuardプロファイルを管理するためのグループ化機能が追加されました。

1. **手動で追加**をクリックします。

    ![追加手動で](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. グループが作成されます。

    ![新しいグループを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/add_a_new_group.png){class="glboxshadow"}

3. グループに「azirevpn」などの説明的な名前を付けます。次に、設定ファイルをアップロードするか、手動で設定を追加するかを選択できます。

    ![新しいグループ名を設定](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **設定ファイルをアップロード**

        WireGuard設定ファイルをアップロードし、**適用**をクリックします。

        ![プロファイルをアップロード](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/upload_profile.png){class="glboxshadow"}

        ![プロファイルアップロード後](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **手動で設定を追加**、これはWireGuard設定を貼り付けるか、各項目を入力したい場合に使用します。

        ![テキストでWireGuardを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        説明的な名前を付け、設定を貼り付けて**適用**をクリックして続行します。

        ![テキストでWireGuardを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        または、各項目を入力して設定を追加することもできます。**アイテムモード**をクリックします。

        ![項目モードでWireGuardを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![項目モードでWireGuardを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. プロファイルの開始 / 編集 / 削除を行うには、三点リーダーのアイコンをクリックします。

    ![プロファイルを開始](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/start_the_profile.png){class="glboxshadow"}

5. 接続ステータスを確認するには、[VPNダッシュボード](vpn_dashboard.md)ページに移動します。

    ![VPNダッシュボードページ](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## GL.iNetルーターでWireGuardサーバーを設定する

GL.iNetルーターをWireGuardサーバーとして設定し、別のGL.iNetルーターをWireGuardクライアントとして設定することができます。WireGuardサーバーの設定については、[こちら](wireguard_server.md)をご参照ください。

## WireGuardサービスプロバイダーから設定ファイルを取得する
??? "AzireVPN"
    ### AzireVPN

    [公式ウェブサイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. [AzireVPN公式ウェブサイト](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}にアクセスしてログインし、次に[WireGuard設定ジェネレーター](https://www.azirevpn.com/cfg/wireguard){target="_blank"}にアクセスします。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. IPオプションで**IPv4**を選択します。次に、**設定をダウンロードする**をクリックします。

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. 次に、[ガイド](#setup-wireguard-client)に従って続行します。

    4. [モバイルアプリ](../faq/mobile_app.md)を使用してAzireVPNを設定することもできます。

??? "Mullvad"
    ### Mullvad

    [公式ウェブサイト](https://mullvad.net/){target="_blank"}

    1. [Mullvad公式ウェブサイト](https://mullvad.net/){target="_blank"}にアクセスしてログインし、次に[WireGuard設定ファイルジェネレーター](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}にアクセスします。

    2. 次に、[ガイド](#setup-wireguard-client)に従って続行します。

    3. [モバイルアプリ](../faq/mobile_app.md)を使用してMullvadを設定することもできます。

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [公式ウェブサイト](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    公式ウェブサイトからWireGuardの設定をダウンロードすることはできません。PIA VPNを設定するには、[モバイルアプリ](../faq/mobile_app.md)を使用してください。

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "AirVPN"
    ### AirVPN

    [公式ウェブサイト](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank}を利用している場合、ウェブサイトにサインインし、[クライアントエリア](https://airvpn.org/client/){target="_blank"}に移動し、[設定ジェネレーター](https://airvpn.org/generator/){target="_blank}をクリックします。

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. 設定ジェネレーターのページで、プロトコルセクションのWireGuardを選択します。

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. サーバーを選択し、ページの下部までスクロールして**生成**ボタンをクリックします。設定ファイルがダウンロードされます。

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_client/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. 次に、[ガイド](#setup-wireguard-client)に従って続行します。
    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

??? "Astrill"
    ### Astrill

    [公式ウェブサイト](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}を使用している場合は、ログインしてから[このページ](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"}にアクセスしてWireGuardの設定を生成してください。

    その後、[ガイド](#set-up-wireguard-client)に従って続行してください。

??? "Hide.me VPN"
    ### Hide.me VPN

    [公式ウェブサイト](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPNは、GL.iNetルーターでWireGuardサービスを簡単に使用できる方法を提供します。

    1. ルーターに[SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}で接続します。

    2. 以下のインストールURLをコピーし、ターミナルに貼り付けてEnterを押します。（右クリックで貼り付け）

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. インストールが開始され、ユーザー名とパスワードが求められます。パスワードを入力または貼り付ける際、ターミナルには何も表示されませんが、入力後にEnterを押してください。

    4. 完了後、Web管理パネルに移動すると、hide.me VPNグループが作成され、既に設定ファイルが含まれています。他の設定ファイルと同様に接続してください。

    **注意:** Hide.me VPN設定ファイル内のキーは、接続前に再生成され、切断後は無効になるため、この設定ファイルを他のデバイスにコピーしても接続できません。

    [参照リンク](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "IVPN"
    ### IVPN

    [公式ウェブサイト](https://www.ivpn.net/){target="_blank"}

    [IVPN](https://www.ivpn.net/){target="_blank"}を使用している場合、WireGuard設定を手動で生成する必要があります。OSに基づいたガイドに従ってください。

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    その後、[ガイド](#setup-wireguard-client)に従って続行してください。

??? "NVPN"
    ### NVPN

    [公式ウェブサイト](https://www.nvpn.net/){target="_blank"}

    設定を作成するために[こちらのガイド](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"}に従ってください。

    その後、[ガイド](#setup-wireguard-client)に従って続行してください。
    ??? "OVPN"
    ### OVPN

    [公式ウェブサイト](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"}にログインし、以下のメニューからWireGuard設定ファイルを取得します。

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. **WireGuardキーの生成**をクリックし、希望するサーバーを選択してから設定をダウンロードします。

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. テキスト編集ソフトウェアで設定ファイルを開き、その内容をコピーします。

        設定にはIPv6の内容が含まれている場合がありますが、GL.iNetルーターはIPv6を十分にサポートしていないため、IPv6の内容を削除してください。以下の例では、ハイライトされた内容がIPv6の内容です。

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}
    
    4. その後、[ガイド](#setup-wireguard-client)に従って続行してください。

    5. [モバイルアプリ](../faq/mobile_app.md)を使用してOVPNを設定することもできます。

??? "PrivateVPN"
    ### PrivateVPN

    [公式ウェブサイト](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. ログインしてから[コントロールパネル](https://privatevpn.com/control-panel){target="_blank"}にアクセスします。
    
        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. サーバーを選択します。
    
        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. **GENERATE CONFIG**をクリックし、設定をコピーします。
    
        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. その後、[ガイド](#setup-wireguard-client)に従って続行してください。

??? "Proton VPN"
    ### Proton VPN

    [公式ウェブサイト](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}を使用している場合は、[こちらのガイド](https://protonvpn.com/support/wireguard-configurations/){target="_blank"}に従ってWireGuard設定ファイルを生成してください。

    その後、[ガイド](#setup-wireguard-client)に従って続行してください。

??? "PureVPN"
    ### PureVPN

    [公式ウェブサイト](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    [ここ](https://support.purevpn.com/setup-wireguard-on-linux){target="_blank"}のガイドに従って、WireGuard設定ファイルを取得してください。

    **注意**: プロファイルをダウンロードしたら、30分以内にファイルをコピーして接続をアクティブにしてください。そうしないと、設定が期限切れとなり、新しい設定ファイルを再ダウンロードする必要があります。

??? "SpiderVPN"
    ### SpiderVPN

    [公式ウェブサイト](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff)にログインし、VPN設定を取得するセクションを見つけます。手順に従って設定を取得してください。

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. VPN設定をダウンロードします。

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. その後、[ガイド](#setup-wireguard-client)に従って続行してください。

??? "StarVPN"
    ### StarVPN

    [公式ウェブサイト](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **StarVPNアカウントを登録する**

        [価格プラン](https://www.starvpn.com/#pricing){target="_blank}のオプションを確認し、ニーズに合ったVPNプランを選択します。チェックアウト時に登録するか、直接[こちら](https://www.starvpn.com/dashboard/register.php){target="_blank"}で登録できます。

    2. **WireGuard設定をダウンロードする**

        StarVPNメンバーエリアの[ダッシュボード](https://www.starvpn.com/dashboard){target="_blank"}にログインします。WireGuard設定をクリックして設定ファイルをダウンロードします。各スロットにはユニークなWireGuard設定ファイルが含まれています。

        ![starvpn download wireguard config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/download-config_edited.jpg){class="glboxshadow"}

    3. 設定にはIPv6の内容が含まれている場合がありますが、GL.iNetルーターはIPv6を十分にサポートしていないため、IPv6の内容を削除してください。

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/starvpn_wireguard_configuration_remove_ipv6.jpg){class="glboxshadow"}

    4. その後、[ガイド](#setup-wireguard-client)に従って続行してください。

    [参考リンク](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [公式ウェブサイト](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}を使用している場合は、[https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}にサインインします。
    
    2. ドロップダウンメニューからロケーションを選択し、**GENERATE**をクリックして、ダウンロードされたテキストファイルを開きます。
    
        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. その後、[ガイド](#setup-wireguard-client)に従って続行してください。

    4. [モバイルアプリ](../faq/mobile_app.md)を使用してStrongVPNを設定することもできます。

??? "Surfshark"
    ### Surfshark

    [公式サイト](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}

    1. [Surfshark](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}を使用している場合は、ログインして、この[ページ](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}にアクセスし、**ルーター**をクリックし、**WireGuard**を選択します。

        ![サーフシャーク ワイヤーガード マニュアル設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. 次のウィンドウで、**キー・ペアを持っていない**を選択します。

        ![サーフシャーク ワイヤーガード マニュアル設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. **新しいキー・ペアを生成する**を選択します。

        ![サーフシャーク ワイヤーガード マニュアル設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. キーが生成されると、**場所を選択する**を選択します。

        ![サーフシャーク ワイヤーガード マニュアル設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. 最後に、設定したい場所を選択し、その場所の横にある**ダウンロード**ボタンをクリックします。

        ![サーフシャーク ワイヤーガード マニュアル設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    [参照リンク](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [公式サイト](https://trust.zone/){target="_blank"}

    1. [https://trust.zone/setup](https://trust.zone/setup)にアクセスしてログインします。
    
    2. WireGuardセクションまでスクロールし、使用するポートを選択して、特定のサーバーの設定ファイルまたは全設定ファイルのzipファイルをダウンロードします。

    3. その後、[ガイド](#setup-wireguard-client)に従って続行します。

??? "VPN.AC"
    ### VPN.AC

    [公式ウェブサイト](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}を使用している場合は、コントロールパネルにログインし、「サービス」メニューからWireGuardマネージャーを見つけます。
    
        ![VPN.AC WireGuard マネージャー](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. 設定を作成し、ダウンロードします。
    
        ![VPN.AC WireGuard プロファイル作成](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. その後、[ガイド](#setup-wireguard-client)に従って続行します。

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [公式ウェブサイト](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}を使用している場合は、[ユーザーオフィス](https://my.keepsolid.com/){target="_blank"}にサインインし、VPN Unlimited® アプリケーションを選択して、**管理**をクリックします。
    
        ![VPN Unlimited 設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}
    
    2. **デバイス**のフィールドを押して、**新しいデバイスを手動で作成...**をクリックし、カスタム名（例：WireGuard）を設定します。**サーバー**の適切な場所を選択し、ドロップダウンメニューから**WireGuard**®プロトコルを選択して、**生成**をクリックします。
    
        ![VPN Unlimited 設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}
    
    3. 設定パラメータがテキスト形式で表示されます。
    
        ![VPN Unlimited 設定](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        設定を以下のように組み合わせます。

        <p>
        [Interface]</br>
        PrivateKey = <i>ユーザーオフィスからPrivateKeyを貼り付け</i></br>
        ListenPort = <i>ListenPortの詳細を貼り付け</i></br>
        Address = <i>Address情報を貼り付け</i></br>
        DNS = <i>ユーザーオフィスからDNSの詳細を貼り付け</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>ユーザーオフィスからPublicKeyを貼り付け</i></br>
        PresharedKey = <i>PresharedKeyの詳細を貼り付け</i></br>
        AllowedIPs = <i>AllowedIPsの詳細を貼り付け</i></br>
        Endpoint = <i>Endpoint情報を貼り付け</i></br>
        </p>

    4. その後、[ガイド](#setup-wireguard-client)に従って続行します。
 
    [参考リンク 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [参考リンク 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}
    
??? "Windscribe"
    ### Windscribe

    [公式ウェブサイト](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    ログインしてから、[WireGuard設定ジェネレータ](https://windscribe.com/getconfig/wireguard){target="_blank"}にアクセスします。使用したい場所とポートを選択し、「設定をダウンロード」をクリックします。

    ![Windscribe WireGuard設定ジェネレータ](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    その後、[ガイド](#setup-wireguard-client)に従って続行します。

??? "12VPX"
    ### 12VPX

    [公式ウェブサイト](https://12vpx.com/?aff=1174){target="_blank"}

    [12VPX](https://12vpx.com/?aff=1174){target="_blank"}を使用している場合は、ログインしてから[このページ](https://12vpx.com/setup/wireguard){target="_blank"}にアクセスします。すべてのサーバーの設定が表示されます。

    その後、[ガイド](#setup-wireguard-client)に従って続行します。

---

WireGuard®はJason A.Donenfeldの登録商標です。

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}にアクセスしてください。