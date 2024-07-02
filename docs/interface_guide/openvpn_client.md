# GL.iNetルーターにOpenVPNクライアントをセットアップする方法

OpenVPNはオープンソースのVPNプロトコルであり、仮想プライベートネットワーク（VPN）技術を利用して、安全なサイト間接続またはポイント・ツー・ポイント接続を確立します。

OpenVPNよりもWireGuardの方がはるかに高速であるため、WireGuardをお勧めします。WireGuardクライアントのセットアップについては、 [こちら](wireguard_client.md)をご覧ください。

すでにプロバイダからOpenVPNサービスを契約しているが、設定ファイルの入手方法がわからない場合は、 [penVPNサービスプロバイダから設定ファイルを入手する](#get-configuration-files-from-openvpn-service-providers) を参照するか、プロバイダのサポートに問い合わせてください。

OpenVPNクライアントは、ウェブ管理パネルまたは [モバイルアプリ](../faq/mobile_app.md)から設定できます。

ウェブ管理パネルから設定する場合は、以下のガイドに従ってください。

左側 -> VPN -> OpenVPNクライアント

NordVPN メンバーシップをお持ちの場合は、**NordVPN** ボタンをクリックしてログインするか、**手動で追加** をクリックして OpenVPN プロファイルをアップロードします。

![openvpn client no initialized](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_no_initialized.png){class="glboxshadow"}

## NordVPN をセットアップする

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} は、速度とセキュリティの点でトップのオンライン VPN サービスです。

1. NordVPNのウェブアカウントにログインし、**サービス認証情報**を取得します。

    ![nordacc](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordacc.jpg){class="glboxshadow"}

    Nordダッシュボードにログイン後、左側のNordVPNをクリックし、**NordVPNを手動で設定**をクリックします。

    ![nordlogin](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordlogin.jpg){class="glboxshadow"}

    そうすると、サービスの認証情報が見つかります。

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn_service_credentials.png){class="glboxshadow"}

2. ステップ1で取得したNordVPNアカウントの**サービス認証情報**を入力し（注：ログインアカウントのメールアドレス/パスワードではありません）、**認証情報の保存とサーバーの取得**をクリックします。
   
    ![input nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/input_nordvpn_credential.png){class="glboxshadow"}

3. プロトコル、各ロケーションの最大サーバー数、ロケーションを選択し、**Apply**をクリックします。

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/select_nordvpn_servers.png){class="glboxshadow"}

    設定ファイルをダウンロードします。

    ![downloaded configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/downloaded_configs.png){class="glboxshadow"}

4. VPNダッシュボードに移動して接続を有効にします。

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/vpn_dashboard_to_connect.png){class="glboxshadow"}

    スイッチを切り替えて接続を有効にします。

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_connected.png){class="glboxshadow"}

5. サーバーを更新する

    NordVPNはいくつかのサーバーをメンテナンスまたはシャットダウンする可能性があり、それは接続を失敗させるので、利用可能な最新のサーバーを取得するために**サーバーを更新**することができます。

    ![update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/update_servers.png){class="glboxshadow"}

6. クレデンシャルの編集

    歯車のアイコンをクリックしてクレデンシャルを編集する。

    ![edit credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/edit_credential.png){class="glboxshadow"}

## OpenVPNクライアントのセットアップ

ファームウェア4. 0以降、OpenVPNプロファイルをグループ化して管理できるようになりました。同じグループ内にすべてのプロファイルが同じ認証情報で含まれていることを確認してください。例えば、あなたがExpressVPNユーザーなら、*expressvpn*というグループを追加し、あなたが望むExpressVPNのOpenVPNプロファイルをすべてこのグループにアップロードすることができます。他のOpenVPNサービスプロバイダについては、別のグループを作成してください。

次のステップでは、ExpressVPNを例にして説明します。

1. **手動で追加**をクリックします。

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_add_manually.png){class="glboxshadow"}

2. グループを作成します。

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/add_a_new_group.png){class="glboxshadow"}

3. expressvpnなど、わかりやすい名前を付けます。

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/set_new_group_name.png){class="glboxshadow"}

4. OpenVPN設定ファイルをアップロードし、クレデンシャルを入力し、**Apply**をクリックします。

    -  4種類の設定ファイルをサポート：

        1. ファイルには `askpass` 入力が必要です。

        2. ファイルには`ユーザー名`と`パスワード`の入力が必要です。

        3. ファイルには `ユーザー名`、`パスワード`、`askpass` の入力が必要です（v4.5以降）。
        
        4. ファイルは入力不要。

    ![upload profile](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/upload_profile_1.png){class="glboxshadow"}

    ![after upload profile](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/after_upload_profile.png){class="glboxshadow"}

5. 3つの点のアイコンをクリックして、プロファイルを開始/削除します。

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/start_the_profile.png){class="glboxshadow"}

6.  [VPNダッシュボード](vpn_dashboard.md) のページで接続状況を確認します。

    ![vpn dashboard page, openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/vpn_dashboard_openvpn_status.png){class="glboxshadow"}

## GL.iNetルーターにOpenVPNサーバーをセットアップする

GL.iNetルーターをOpenVPNサーバーに設定し、別のGL.iNetルーターをOpenVPNクライアントに設定することができます。OpenVPNサーバーのセットアップについては、 [こちら](openvpn_server.md)をご覧ください。

## OpenVPNサービスプロバイダから設定ファイルを入手する

私たちはさまざまなOpenVPNサービスプロバイダをテストしました。設定ファイルの入手方法がわからない場合は、以下の指示に従ってください。ただし、以下に記載されていない場合は、サービスプロバイダに問い合わせて設定ファイルを入手する必要があります。

OpenVPNの設定に問題がある場合は、 [support@glinet.biz](mailto:support@glinet.biz)に連絡するか、[このフォーラムの投稿](https://forum.gl-inet.com/t/openvpn-and-wireguard-compatibility-report/15621){target="_blank"}に報告してください。

??? "NordVPN"
    ### NordVPN

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **ログインの詳細を確認する**
    
        NordVPN サービスの認証情報は、NordVPN アカウントの認証情報（メールアドレスとパスワード）とは異なります。ルーターの手動 OpenVPN 設定方法を使用して VPN に接続するには、NordVPN サービス認証情報が必要です。

         [公式ウェブサイト](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}にログインし、Nord アカウント ダッシュボードに移動すると、サービス資格情報が表示されます。

        ![nordacc](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordacc.jpg){class="glboxshadow"}

        Nordダッシュボードにログイン後、左側のNordVPNをクリックし、**NordVPNを手動で設定**をクリックします。

        ![nordlogin](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordlogin.jpg){class="glboxshadow"}

        そうすると、サービスの認証情報が見つかります。

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn_service_credentials.png){class="glboxshadow"}

    2. **NordVPNサーバーの選択**

         [NordVPN推奨サーバーユーティリティはこちら](https://nordvpn.com/servers/tools/){target="_blank"}にアクセスしてください。それはあなたのネットワークに基づいてサーバーをお勧めします。UDPまたはTCP設定をダウンロードするには、**利用可能なプロトコルを表示**をクリックします。 Click [ こちら](../faq/openvpn_tcp_udp.md) をクリックして違いをご覧ください。

        ![nordvpn server utility](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/nordvpn/nordvpn_server_utility.png){class="glboxshadow"}

     すべてのサーバーのコンフィグは [ここから](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip)ダウンロードできます。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

    [参考リンク](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

     [モバイルアプリ](../faq/mobile_app.md) を使用してNordVPNを設定することもできます。

??? "ExpressVPN"
    ### ExpressVPN

    [公式ウェブサイト](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    [Expressvpn公式インストラクション](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}より引用。

    1.  [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} のウェブサイトにアクセスし、ExpressVPNの認証情報でログインします。

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        電子メールに送信された **確認コードを入力**してください。

    2.  "デバイスの設定" セクションで、**詳細**をクリックします。

    ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3.  **手動設定**をクリックしてください。

    ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. **ユーザー名**、**パスワード**、および **OpenVPN設定ファイル**のリストが表示されます。

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        .ovpnファイルをダウンロードする場所をクリックしてください。

        **このブラウザのウィンドウを開いておいてください**。この情報は後で設定する際に必要になります。

    [参考リンク](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "PIA (プライベート・インターネット・アクセス)"
    ### PIA

    [公式ウェブサイト](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    直接[ダウンロード](https://www.privateinternetaccess.com/openvpn/openvpn.zip) する。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

??? "CyberGhost"
    ### CyberGhost

    [公式ウェブサイト](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

     [CyberGhost公式インストラクション](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}より引用

    1. CyberGhost VPNオンラインアカウントにログインします。

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. 左側のメニューから"**VPN**"を選択し、"**Configure Device**"をクリックして、以下のようにサーバーの設定を作成します：

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. 次に、以下の説明に従ってサーバー構成を作成します

        * **プロトコル** : **OpenVPN**
        * **国** : ネイティブ・プロトコルの接続は1つのサーバーでしか使用できないため、サーフィンをしたい国を選択する必要があります。この国で使用されるサーバーは、CyberGhostによって自動的に選択されます。

        * **サーバーグループ** : サーバーグループと使用するOpenVPNプロトコル（UDPまたはTCP）を選択します。

        **OpenVPN UDP**はTCPバージョンよりも高速ですが、場合によってはダウンロードが途切れることがあります。これはデフォルトの設定です。
        
        **OpenVPN TCP**はUDPバージョンよりも安定した接続を可能にしますが、若干遅くなります。突然の接続切断など、接続に関する問題が繰り返し発生する場合は、このバージョンを選択してください。

        希望するパラメータを選択したら、**設定を保存**で保存します。

    4. 設定ダッシュボードで生成された **OpenVPN** 認証情報を表示するには、**設定を表示** をクリックします。

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. 接続設定の後、以下の点にご注意ください：

        * **サーバーグループ** : これは接続したい国（サーバー）のアドレスで、例えば'12345-1-ca.cg-dialup.net'。このアドレスは、前のステップで選択した国ごとに変わります。実際に使用する単一サーバーは、CyberGhostによって自動的に選択されます。
        * **ユーザー名** : このプロトコルで生成された専用のユーザー名です。これは通常のCyberGhostアカウントのユーザー名ではなく、手動設定でCyberGhostサーバーと認証するためだけに使用されます。GL.iNetルーターでOpenVPNをセットアップする際に必要となります。
        * **パスワード** : プロトコルを使用するためだけに生成されたパスワード。これは通常のCyberGhostアカウントのパスワードではなく、手動設定でCyberGhostサーバーと認証するためだけに使用されます。GL.iNetルーターでOpenVPNを設定する際に必要となります。

        完了したら、設定ファイルをダウンロードしてください。 *設定ファイルのダウンロード* クリックし、設定ファイルをコンピュータにダウンロードしてください。

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "PrivateVPN"
    ### PrivateVPN

    [公式ウェブサイト](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    直接[ダウンロード](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank} する。

    [こちら](https://privatevpn.com/client/PrivateVPN-TUN.zip)が公式ダウンロードリンクです。ルーターのインポート中にバグが発生したため、内部のファイル名に「Bogotá」という特殊文字が含まれています。ファイル名を変更し、上記のダウンロードリンクを提供しています。今後のバージョンではこのバグを修正する予定です。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

??? "Proton VPN"
    ### Proton VPN

    [公式ウェブサイト](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **プロトンVPNはWireGuardサービスを提供しており、WireGuardを使用することをお勧めします。[こちら](wireguard_client.md#wireguard-providers)をチェックアウト**

    1.  [プロトンVPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} アカウントにログインします。

    2. 左側の**ダウンロード**をクリックしてください。

    3. ルータープラットフォーム、プロトコルなどを選択し、設定ファイルをダウンロードする対象国を探します。

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. OpenVPNに接続するためのクレデンシャルは、プロトンウェブサイトのダッシュボードにログインするためのものではありません。**アカウント -> OpenVPN/IKEv2 ユーザー名**で確認できます。

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [公式ウェブサイト](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    直接[ダウンロード](https://d32d3g1fvkpl8y.cloudfront.net/heartbleed/router/Recommended-CA2.zip)する。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

    [参考リンク](https://support.purevpn.com/openvpn-files)

    GL.iNet ルーターは、PPTP を必要とするため、PureVPN の [専用 IP](https://www.purevpn.com/dedicated-ip){target="_blank"} 機能をサポートしていません。

??? "Surfshark"
    ### Surfshark

    [公式ウェブサイト](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}

    1. **ログインの詳細を確認する**

        Surfsharkサービスの認証情報は、Surfsharkアカウントの認証情報（メールアドレスとパスワード）とは異なります。ルーターの手動OpenVPN設定方法を使用してVPNに接続するには、Surfsharkサービス認証情報が必要です。

         [公式ウェブサイト](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"},  [このページ](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}に移動すると、手動接続に必要な詳細がすべて表示されます。

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Surfshark サーバーを選択する**

        **場所**タブを選択すると、すべての Surfshark サーバーが表示されます。

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        TCPかUDPを選択するよう求められます。[ここ](../faq/openvpn_tcp_udp.md) をクリックして違いを確認してください。

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    すべてのコンフィグは [こちら](https://api.surfshark.com/v1/server/configurations) から直接ダウンロードできます。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [公式ウェブサイト](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}アカウントでログインすると、VPNアカウントサマリーが表示されます。 アカウント設定案内をクリックします。

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. マニュアルセットアップのセクションを見つけ、手順に従って設定を行います。

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [公式ウェブサイト](https://www.ovpn.com/en?ref=glinet){target="_blank"}
    
    ログインして、下のメニューをクリックすれば、簡単にOpenVPNの設定ファイルを入手できます。

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    サーバーを選択し、ダウンロードします。

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    ユーザー名とパスワードは、OVPNにログインするときと同じです。

??? "AirVPN"
    ### AirVPN

    [公式ウェブサイト](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. AirVPNアカウントにログインします。

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. 左側で [Config Generator] を選択し、オペレーティング システムとして [Linux] を選択します。 次に、優先サーバーを選択します。

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. 設定ファイルのダウンロードページが表示されます。

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [公式ウェブサイト](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

     [Astrill 公式インストラクション](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}より引用。

    1. AstrillのOpenvpn設定ZIPを生成してダウンロードします。

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. OPENVPN_GUI のように 説明(Description) を入力します。

    3. 証明書に追加ボタンをクリックします。

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. OpenVPN証明書が追加されたら、ダウンロードボタンをクリックします。

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [公式ウェブサイト](https://www.bolehvpn.net/){target="_blank"}

     [ダッシュボード](https://users.bolehvpn.net/){target="_blank"}にログインし、構成ファイルをダウンロードして、 [Linux_iOS インライン](https://users.bolehvpn.net/download/inline/6){target="_blank"} 形式を選択します。 ダウンロードが完了したら、zip ファイルを解凍します。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

    [参考リンク](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [公式ウェブサイト](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    直接[ダウンロード](https://www.cactusvpn.com/downloads/){target="_blank"} します。

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [公式ウェブサイト](https://cryptostorm.is/){target="_blank"}

    直接[ダウンロード](https://cryptostorm.is/configs/ecc/){target="_blank"} します。

??? "FastestVPN"
    ### FastestVPN

    [公式ウェブサイト](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    OpenVPN TCPおよびUDP用のFastestVPN 設定ファイルのzipフォルダを [こちら](https://support.fastestvpn.com/download/openvpn-tcp-udp-config-files/)ダウンロードします。

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

    [参照リンク](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [公式ウェブサイト](https://www.finchvpn.com/){target="_blank"}

    1. FinchVPN アカウントにログインします。

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. ダウンロードページに移動し、FinchVPN OpenVPN Configの下にあるダウンロードをクリックします。

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Linuxを選択します。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. お好みに応じてプロトコルを選択してください。一般的には、最初の **Port 8484 over UDP** を 選択します。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. ファイルをダウンロードする前に、ユーザー名とパスワードを入力するボックスにチェックを入れてください。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [公式ウェブサイト](https://www.hideipvpn.com/){target="_blank"}

    1. HideIPVPN アカウントにログインします。

    2. 左側の「パッケージ」に移動し、パッケージをクリックしてアクティブであることを確認します。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. VPN タブには、ユーザー名とパスワードの VPN ログイン詳細が表示されます。これは、OpenVPN 接続時のログイン用です。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. 下にスクロールしてOpenVPN設定ファイルをダウンロードしてください。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [公式ウェブサイト](https://hide.me/?friend=glinet){target="_blank"}

    1. Hide.me アカウントにログインし、左側で サーバーの場所を見つけます。

    2. Windows用のOpenVPN設定をダウンロードします。

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [公式ウェブサイト](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    1. [https://www.hotspotshield.com/](https://www.hotspotshield.com/)にアクセスして、アカウントをクリックします。サインインを求められたらサインインしてください。

        ![ホットスポットシールド ログイン](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router)にアクセスします。

        「Select location」ドロップダウンメニューから、ルーターが使用する仮想ロケーションを選択します。次に「Download file」をクリックします。設定ファイル（config.ovpn）がコンピュータにダウンロードされます。OpenVPNクライアントをルーターに設定する際に、ユーザー名とパスワードを入力する必要があります。

        ![ホットスポットシールド リンクルーター](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [参考リンク](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [公式ウェブサイト](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - [ここ](https://configs.ipvanish.com/configs/configs.zip)からすべてのサーバーのすべての構成ファイルをダウンロードできます。これには、すべてのサーバー構成ファイル (.ovpn) と証明書ファイル (.crt) が含まれています。 .zipファイルは機種によっては少し大きい場合がありますので、使用しないサーバーの設定(.ovpn)を削除してください。

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    -  [ここ](https://www.ipvanish.com/software/configs/)個々のサーバー設定ファイルをダウンロードすることもできますが、ca.ipvanish.com.crtもダウンロードする必要があります。ルーターにアップロードする前に、ca.ipvanish.com.crt と .ovpn 設定ファイルを .zip アーカイブに圧縮する必要があります。

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [参照リンク](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [公式ウェブサイト](https://billing.ivacy.com/page/22852){target="_blank"}

    [OpenVPN UDP設定ファイルをダウンロードする](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivacy/IVACY_OpenVPN_Configs_UDP.zip)

    [OpenVPN TCP設定ファイルをダウンロードする](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivacy/IVACY_OpenVPN_Configs_TCP.zip)

    [参照リンク](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [公式ウェブサイト](https://www.ivpn.net/){target="_blank"}

    1. [OpenVPN設定ファイル](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip)をダウンロードする

    2. [IVPNクライアントエリア](https://www.ivpn.net/clientarea/login){target="_blank"}でアカウントIDを確認します。

    3. 設定ファイルをドラッグして新しい OpenVPN 設定を追加すると、ユーザー名とパスワードの入力を求められます。ユーザー名は、**ivpn**で始まるアカウントIDです。 パスワードには、**ivpn** などの任意のパスワードを使用できます。

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [参照リンク](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "OysterVPN"
    ### OysterVPN

    [公式ウェブサイト](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. [OysterVPNサーバーリストページ](https://support.oystervpn.com/server-list/){target="_blank}にアクセスし、**Download .ovpn file**をクリックして設定ファイルをダウンロードします。

        ![oystervpn .ovpnファイルをダウンロード](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. OpenVPN接続のためのユーザー名とパスワードは、OysterVPNにログインする際に使用するものと同じです。

    ヒント: zipファイルが大きすぎてアップロードできない場合、.zipファイル内のいくつかの.ovpnファイルを削除するか、単一の.ovpnファイルをアップロードすることができます。

??? "PrivadoVPN"
    ### PrivadoVPN

    [公式ウェブサイト](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    ログインするだけで、簡単に**VPN設定のダウンロード**を見つけることができます。

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    ヒント: zipファイルが大きすぎてアップロードできない場合は、.zipファイル内の.ovpnを削除するか、単一の.ovpnファイルをアップロードしてください。

??? "SaferVPN"
    ### SaferVPN

    [公式ウェブサイト](https://safervpn.com/?a_aid=563){target="_blank"}

    直接[ダウンロード](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup)する。

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [公式ウェブサイト](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPNにはWireGuardサービスがあり、WireGuardを使用することをお勧めします。 [ここ](wireguard_client.md#starvpn)でチェックアウトします。

    1. **StarVPNにアカウントを登録する**

         [料金プラン](https://www.starvpn.com/#pricing){target="_blank"} のオプションから、ニーズに合わせてVPNプランをお選びください。登録はチェックアウト時に行うか、[こちら](https://www.starvpn.com/dashboard/register.php){target="_blank"}から直接行うことができます。

    2. VPNログイン情報

        StarVPNメンバーエリア [ダッシュボード](https://www.starvpn.com/dashboard){target="_blank"}にログインします。 各スロットのVPNユーザー名とパスワードは、スロット管理セクションまたはダッシュボードエリアで確認できます。

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_edited-2.jpg){class="glboxshadow"}

        複数スロットの場合、VPN構成設定と認証情報は “スロットの管理” セクションにあります。

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_slots_edited-1024x355.jpeg){class="glboxshadow"}

    3. OpenVPNの設定ファイルをダウンロードする

        次のステップでは、OpenVPN ソフトウェアが接続先を認識するために必要な VPN サーバー構成ファイルをダウンロードする必要があります。 メンバーエリアのダッシュボードで構成ファイルをダウンロードします。

        ![download starvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/download-ovpn_edited.jpg){class="glboxshadow"}

        一部のGL.iNetルーターはIPv6またはDNS Leak Protectionをサポートしていないため、IPまたは接続エラーが発生する場合があります。ovpn設定ファイルを編集し、以下の簡単な作業でIPv6を無効にしてください。

        ![troubleshooting](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/troubleshooting.jpg){class="glboxshadow"}

??? "StreamVPN"

    [公式ウェブサイト](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} アカウントでログインすると、サブスクリプション情報が表示されます。 **インストールとガイド**をクリックします。

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2.  **VPNルーター**をクリックすると、`StreamVPN.zip`というzipアーカイブファイルがダウンロードされます。

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **注意:** 設定ファイル名は "Primary "を含んでいる場合のみ機能します。

??? "VPN.AC"
    ### VPN.AC

    [公式ウェブサイト](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [ダウンロード](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [公式ウェブサイト](https://www.vpngate.net/en/){target="_blank"}

    OpenVPN の設定ファイルは、 [VPN Gate website](https://www.vpngate.net/en/) に、サーバーの場所ごとにリストアップされています。

    1. **OpenVPN**列の下にあるOpenVPN 設定ファイルをクリックします。

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. ダウンロードページが表示されます。

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [公式ウェブサイト](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    情報は [VPN unlimited 公式インストラクション](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}より引用

    まずはユーザーオフィスにログインし、VPN Unlimitedサービスの管理をクリックし、いくつかの簡単な手順に従ってください：

    1. デバイスを選択する

        リストからデバイスを選ぶか、新しいデバイスを作成します。空きスロットがなくなった場合は、古いデバイスを削除するか、追加のスロットを購入してください。

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. 希望するサーバーの場所を選択する
    
        VPN Unlimited は、70以上のロケーションに400以上の多種多様なサーバーを提供しています。この場合、ドイツにしましょう。

    3. VPNプロトコルを選択する

        OpenVPNプロトコルを選択します。

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. 設定を作成する

        作成をクリックすると、VPN接続のセットアップに必要なすべてのデータが表示されます。

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPNはここでOpenVPNファイルを提供します: [OpenVPN ファイルはどこにありますか? - VyprVPN サポート](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    提供されたzipファイルには、.ovpnファイルを含む2つのフォルダが含まれています。一つはOpenVPN160と呼ばれるもの、もう一つはOpenVPN256と呼ばれるものです。zip ファイルから OpenVPN160 フォルダーを削除し、通常通り GL.iNet ルーターにアップロードしてください。

??? "ZoogVPN"
    ### ZoogVPN

    [公式ウェブサイト](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

     [公式サイト](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}にサインインし、 [OpenVPN設定ファイルページ](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}にアクセスすると、ここに全てのサーバーがあります。TCP列またはUDP列の設定ファイルをダウンロードしてください。

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    次に、 [GL.iNetルーターにOpenVPNクライアントをセットアップするガイド](#setup-openvpn-client)に従って、ユーザー名とパスワードは、ZoogVPNウェブサイトへのログインに使用するものと同じです。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
