# GL.iNetルーターにOpenVPNクライアントを設定する方法

OpenVPNは、仮想プライベートネットワーク（VPN）技術を利用して、安全なsite-to-siteまたはpoint-to-point 接続を確立するオープンソースのVPNプロトコルである。

GL.iNetのルーターには、OpenVPNクライアントとサーバーがプリインストールされています。

OpenVPNよりもWireGuardの方が高速なので、そちらをお勧めします。 WireGuardクライアントをセットアップする場合、 [こちらをご覧ください。](../wireguard_client).

すでにプロバイダーからOpenVPNサービスを購入しているが、設定ファイルを取得する方法がわからない場合、 こちらをご参照ください。 [OpenVPNサービスプロバイダから設定ファイルを取得する](#get-configuration-files-from-openvpn-service-providers) 、またはサポートにお問い合わせください。

OpenVPN Clientは、Web Admin Panelと [モバイルアプリ](../mobile_app)から設定することができます。 モバイル アプリの場合、NordVPN は既に統合されています。

## NordVPNをセットアップする

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} は、スピードとセキュリティのトップのオンラインVPNサービスです。

ファームウェア 4.0.0 から、NordVPN OpenVPN サービスが統合されました。

web Admin Panelにアクセスし、左側の「VPN」→「OpenVPN Client」をクリックします。

1. NordVPN アカウントのサービス認証情報を入力します。そして **Save Credentials & Get Servers**をクリックしてください。

    ??? "NordVPNサービスの認証情報はどこにあるか。"

        NordVPNサービスの認証情報は、Nord Accountのダッシュボードで確認することができます。

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn_service_credentials.png){class="glboxshadow"}

    ![input nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/input_nordvpn_credential.png){class="glboxshadow"}

2. プロトコル、各ロケーションの最大サーバー数、ロケーションを選択し、 **Apply**をクリックします。

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/select_nordvpn_servers.png){class="glboxshadow"}

    設定ファイルをダウンロードします。

    ![downloaded configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/downloaded_configs.png){class="glboxshadow"}

3. VPN ダッシュボードに移動し、接続を有効にします。

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/vpn_dashboard_to_connect.png){class="glboxshadow"}

    スイッチを切り替えて接続を有効にします。

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_connected.png){class="glboxshadow"}

4. サーバーの更新

    NordVPNは一部のサーバーをメンテナンスまたはシャットダウンすることがあり、その場合、接続に失敗することになります。**Update Servers** で利用可能な最新のサーバーを取得できます。

    ![update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/update_servers.png){class="glboxshadow"}

5. クレデンシャルの編集

    歯車アイコンをクリックして、クレデンシャルを編集します。

    ![edit credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/edit_credential.png){class="glboxshadow"}

## OpenVPNクライアントをセットアップする

frimware 4.0では、OpenVPNプロファイルをグループ化して管理することができるようになりました。 すべてのプロファイルが同じグループにあり、同じ認証情報を持っていることをご確認ください。たとえば、ExpressVPN ユーザーの場合、*expressvpn*という名前のグループを追加してから、必要なすべての ExpressVPN OpenVPN プロファイルをこのグループにアップロードできます。他のOpenVPNサービスプロバイダを利用する場合は、別のグループを作成してください。

次のステップでは、ExpressVPNを例として説明します。

1. ウェブ管理パネルにアクセスし、左側の「VPN」→「OpenVPN Client」をクリックします。

2. 新しいグループを追加する

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/add_a_new_group.png){class="glboxshadow"}

3. グループには expressvpn などのわかりやすい名前をつけます。

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/set_new_group_name.png){class="glboxshadow"}

4. OpenVPN設定ファイルをアップロードし、クレデンシャルを入力します。そして**Apply**をクリックします。

    ![upload profile](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/upload_profile.png){class="glboxshadow"}

    ![after upload profile](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/after_upload_profile.png){class="glboxshadow"}

5. VPN Dashboardに移動して接続を有効にします。

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/vpn_dashboard_to_connect_expressvpn.png){class="glboxshadow"}

## GL.iNet ルーターに OpenVPN サーバーをセットアップする

一つのGL.iNetルーターをOpenVPNサーバーに、もう一つののGL.iNetルーターをOpenVPNクライアントに設定することができます。OpenVPNサーバーの設定方法は、[ここ](../openvpn_server)をご参照してください。　 

## OpenVPNサービスプロバイダから設定ファイルを取得する

さまざまな OpenVPN サービス プロバイダーをテストしました。したがって、設定ファイルを取得する方法がわからない場合は、次の手順に従ってください。 ただし、以下に記載されていない場合は、サービスプロバイダに連絡して設定ファイルを入手する必要があります。

OpenVPNの設定に問題がある場合、[support@gl-inet.com](mailto:support@gl-inet.com)までご連絡ください。または[this forum post](https://forum.gl-inet.com/t/openvpn-and-wireguard-compatibility-report/15621){target="_blank"}で報告してください。

おすすめ:

<div id="nordvpn"></div>

??? "NordVPN"

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    OpenVPNクライアントの設定ファイルをダウンロードします。[NordVPN recommended server utility here](https://nordvpn.com/servers/tools/){target="_blank"}に入ることをおすすめします。これは、ネットワーク上のサーバーベースをお勧めします。**Show available protocols** をクリックし、UDP または TCP ファイルをダウンロードします。

    ![nordvpn server utility](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/nordvpn/nordvpn_server_utility.png){class="glboxshadow"}

    もちろん、すべてのサーバーの設定ファイルをダウンロードすることができます。 [ここ](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip)をクリックください。

    ヒント：ZIPファイルが大きすぎてアップロードできない場合は、.zipファイル内の一部の.ovpnを削除するか、単一の.ovpnファイルをアップロードすることができます。

    [参考リンク](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    NordVPNの設定には、[モバイルアプリ](../mobile_app)を使用することもできます。

<div id="pia"></div>

??? "PIA (Private Internet Access)"

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [ダウンロード](https://www.privateinternetaccess.com/openvpn/openvpn.zip) directly.

<div id="surfshark"></div>

??? "Surfshark"

    [Official Website](https://get.surfshark.net/aff_c?offer_id=6&aff_id=1400){target="_blank"}

    ログインして直接[ダウンロード](https://api.surfshark.com/v1/server/configurations)する、または [ガイド](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-)をお読みください。

<div id="purevpn"></div>

??? "PureVPN"

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    [ダウンロード](https://d32d3g1fvkpl8y.cloudfront.net/heartbleed/router/Recommended-CA2.zip) directly.

    [参考リンク](https://support.purevpn.com/openvpn-files)

<div id="torguard"></div>

??? "TorGuard"

    [Official Website](https://torguard.net/aff.php?aff=3040){target="_blank"}

    1.[TorGuard](https://torguard.net/aff.php?aff=3040){target="_blank"}を使用する場合、コントロールパネルにログインし、**Tools** メニューから **Config Generator**  を見つけてください。 **VPN Server** およびその他のオプションを選択します。**Generate Config** をクリックすると、設定ファイルが自動的にダウンロードされます。

        ![Generate ovpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/torguard/torguard_menu.jpg){class="glboxshadow"}

    2. OpenVPN 接続のユーザー名とパスワードは、コントロールパネルのログインとは異なります。VPNユーザー名とパスワードは下記からご確認いただけます。

        ![torguard vpn username vpn password](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/torguard/torguard_vpnusername_vpnpassword.png){class="glboxshadow"}

<div id="privatevpn"></div>

??? "PrivateVPN"

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://privatevpn.com/client/PrivateVPN-TUN.zip) directly.

<div id="protonvpn"></div>

??? "Proton VPN"

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPNはWireGuardサービスを持っているので、WireGuardの利用をお勧めします。チェックアウトは[こちら](../wireguard_client/#wireguard-providers)**.

    1. [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} アカウントにログインします。

    2. 左側の**Download**をクリックします。

    3. Router platform, protocolなどを選択し、対象国を見つけて設定ファイルをダウンロードします。

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. OpenVPN接続用のクレデンシャルは、Protonサイトのダッシュボードにログインするものではありません。**Account -> OpenVPN/IKEv2 username**で確認できます。

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

<div id="expressvpn"></div>

??? "ExpressVPN"

    [Official Website](https://www.xvbelink.com/?a_fid=glinet){target="_blank"}

    [Expressvpn official instruction](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}より引用

    1. [ExpressVPN](https://www.xvbelink.com/?a_fid=glinet){rel="sponsored" target="_blank"} Webサイトにアクセスし、ExpressVPNの認証情報でログインください。

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        メールに記載されている**認証コードを入力** してください。

    2. 右側には、**OpenVPN** がすでに選択されているので、 **ユーザ名**、**パスワード**、および**OpenVPN設定ファイル**のリストが表示されます。

        ![](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-manual-configuation-openvpn.jpg){class="glboxshadow"}

        .ovpnファイルをダウンロードする場所をクリックします。

        **このブラウザのウィンドウを開いたままにしておく**。この情報は、後で設定する際に必要となります。

その他:

<div id="airvpn"></div>

??? "AirVPN"

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. AirVPNアカウントにログインします。

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. 左側のConfig Generatorを選択し、オペレーティング システムとしてLinuxを選択します。次に、優先サーバーを選択します。

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. 設定ファイルのダウンロードページが表示されます。

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

<div id="astrill"></div>

??? "Astrill"

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    [Astrill official instruction](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}より引用

    1. Astrill Openvpn設定用ZIPファイルを生成し、ダウンロードする

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. OPENVPN_GUIのようなDescriptionを入力します。

    3. ADD to my certificatesボタンをクリックします。

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. OpenVPN 証明書が追加されたら、ダウンロードボタンをクリックします。

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

<div id="bolevpn"></div>

??? "bolehvpn"

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

   [Dashboard](https://users.bolehvpn.net/){target="_blank"}にログインします。 設定ファイルをダウンロードし、 [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"} 形式を選択します。ダウンロード完了後、zipファイルを解凍してください。

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

<div id="cactusvpn"></div>

??? "CactusVPN"

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Download](https://www.cactusvpn.com/downloads/){target="_blank"} directly.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

<div id="cryptostorm"></div>

??? "Cryptostorm"

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [Download](https://cryptostorm.is/configs/ecc/){target="_blank"} directly.

<div id="cyberghost"></div>

??? "CyberGhost"

    [Official Website](https://support.cyberghostvpn.com/hc/en-us){target="_blank"}

    [CyberGhost official instruction](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers?fbclid=IwAR0_IicBlnNzVqlKh0mAHFyM6uvsGgBQooYfMyJ0bHgb13Eidn8KhXnd6Y0){target="_blank"}より引用

    1. CyberGhost VPN のオンラインアカウントにログインします。

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. **My Devices**をクリック  > **Other**をクリック > **Configure new device**を選択します。

        ![config new device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.png){class="glboxshadow"}

    3. 新しい画面では、 **Server configuration** タブで、必要なパラメータを設定することができます。 DD-WRTルーターにOpenVPNを設定するために、プロトコルドロップダウンメニューから「OpenVPN」を選択します。以下で説明するように、目的の国とサーバー グループも定義する必要があります。

        ![server configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.png){class="glboxshadow"}

        - プロトコル: ルーター構成の場合は、OpenVPN を選択してください。
    

        - Country:ネイティブ プロトコル接続は 1 つのサーバーでしか使用できないため、サーフィンをしたい国を選択する必要があります。この国で使用されるサーバーは、CyberGhost によって自動的に選択されます。

        - サーバーグループ：サーバーグループと使用するOpenVPNプロトコル（UDPまたはTCP）を選択します。

            UDPはTCPバージョンよりも高速化を可能にしますが、場合によってはダウンロードを中断する可能性があります。これがデフォルト設定です。

            TCPは、UDPバージョンよりも安定した接続が可能ですが、若干速度が遅くなります。突然の切断など、接続の問題が繰り返し発生する場合は、このバージョンを選択します。

        設定した後、**Save and download configuration**で保存してください。

<div id="fastestvpn"></div>

??? "FastestVPN"

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    OpenVPN TCP/UDP用のFastestVPN Config Filesのzipフォルダのダウンロードは[こちら](https://support.fastestvpn.com/download/openvpn-tcp-udp-config-files/)

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

<div id="finchvpn"></div>

??? "FinchVPN"

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. FinchVPNアカウントにログインします。

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. ダウンロードページに移動し、FinchVPN OpenVPN Configの下にある「Download」をクリックします。

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Linuxを選択します。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. お好みに応じてプロトコルを選択してください。一般的には、一番目の**Port 8484 over UDP** を選択すればよいでしょう。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. ファイルをダウンロードする前に、ユーザー名とパスワードを入力するボックスにチェックマークを入れることを忘れないでください。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

<div id="hideipvpn"></div>

??? "HideIPVPN"

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. HideIPVPN のアカウントにログインします。

    2. 左側の「パッケージ」をクリックし、パッケージをクリックして、パッケージが有効になっていることを確認します。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. VPNタブには、VPNログインの詳細として、ユーザー名とパスワードがありますが、これはOpenVPN接続時にログインするためのものです。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. 下にスクロールすると、OpenVPNの設定ファイルをダウンロードできます。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

<div id="hidemevpn"></div>

??? "Hide.me VPN"

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Hide.me アカウントにログインし、左側で「Server Locations」を見つけます。

    2. OpenVPN設定ファイル（Windows版）をダウンロードします。

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

<div id="hidemyass"></div>

??? "HideMyAss"

    [Official Website](https://click.hmavpn.com/aff_c?offer_id=1&aff_id=861){target="_blank"}

    [Download](https://vpn.hidemyass.com/vpn-config/vpn-configs.zip)

<div id="ipvanish"></div>

??? "IPVANISH"

    [Official Website](https://www.ipvanish.com/){target="_blank"}

    [ここ](https://www.ipvanish.com/software/configs/configs.zip)からすべてのサーバーのすべての設定ファイルをダウンロードできます。次に、この **config.zip** を Web 管理パネルのOpenVPN クライアントにアップロードする必要があります。

    You can also download individual server configuration files [here](https://www.ipvanish.com/software/configs/), but you will need to download **ca.ipvanish.com.crt** as well. Before uploading to the router, you need to compress the **ca.ipvanish.com.crt** and .ovpn configuration files into a .zip archive and upload them.

    ![ipvanish](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_download_openvpn_configs.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

<div id="ivacy"></div>

??? "IVACY"

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    [Download OpenVPN UDP Configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivacy/IVACY_OpenVPN_Configs_UDP.zip)

    [Download OpenVPN TCP Configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivacy/IVACY_OpenVPN_Configs_TCP.zip)

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

<div id="ivpn"></div>

??? "IVPN"

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Download the [OpenVPN config files](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Find the Account ID on [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. When drag the config file to Add a New OpenVPN Configuration, you will be asked to enter User Name and Password. The User Name is your Account ID that begins with letters **ivpn**. The password can be anything, like **ivpn**

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html)

<div id="ovpn"></div>

??? "OVPN"

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}
    
    Just login, then you can easy get the OpenVPN configurations file by click the menu below.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Choose the server and download.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    The username and password are the same you login OVPN.

<div id="safervpn"></div>

??? "SaferVPN"

    [Official Website](https://safervpn.com/?a_aid=563){target="_blank"}

    [Download](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup) directly.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

<div id="starvpn"></div>

??? "StarVPN"

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN has WireGuard service, we recommend to use WireGuard, checkout [here](../wireguard_client/#starvpn).

    1. **Register an account with StarVPN**

        Head on over to their [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} options and choose a VPN plan that suits your needs. You can register on checkout or directly [here](https://www.starvpn.com/dashboard/register.php){target="_blank"}

    2. VPN Login Information

        Log into the StarVPN member area [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. You can find your VPN username and password for each slot in the Manage Slots Section or dashboard area.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_edited-2.jpg){class="glboxshadow"}

        For multiple slots, the VPN configuration settings and credentials can be located in the “Manage Slots” section.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_slots_edited-1024x355.jpeg){class="glboxshadow"}

    3. Download OpenVPN Configuration File

        The next step, you must download the VPN server configuration files necessary so that the OpenVPN Software knows where to connect to.   Download the configuration file in the members area dashboard.

        ![download starvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/download-ovpn_edited.jpg){class="glboxshadow"}

        Some GL.iNet routers do not support IPv6 or DNS Leak Protection, as a result you may experience an IP or connection error. Edit the ovpn configuration file and disable IPv6 by performing these simple tasks.

        ![troubleshooting](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/troubleshooting.jpg){class="glboxshadow"}

<div id="strongvpn"></div>

??? "StrongVPN"

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Login with your [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} account and then you will be able to see VPN Accounts Summary. Click Account Setup Instructions”.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Find the Manual setup section, follow the steps to get configuration.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

<div id="vpnac"></div>

??? "VPN.AC"

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

<div id="vpngate"></div>

??? "VPNGate"

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    The OpenVPN configuration files are listed on the [VPN Gate website](https://www.vpngate.net/en/) according to the server location.

    1. Click OpenVPN Config file under the column **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. You will see the download page.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

<div id="vpnunlimited"></div>

??? "VPN Unlimited(KeepSolid)"

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Information quoted from [VPN unlimited official instruction](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Start out by logging in to your User Office, press Manage for the VPN Unlimited service, and follow a few simple steps:

    1. Select a device

        Pick a device from the list or create a new one. If you are out of free slots, delete an old device or buy extra slots.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Choose the desired server location
    
        VPN Unlimited offers a large variety of servers, namely 400+ in 70+ locations. In this case, let it be Germany.

    3. Select the VPN protocol

        selece OpenVPN protocol.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Create a configuration

        Press Generate and you will get all the data required to set up a VPN connection.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

<div id="vyprvpn"></div>

??? "VyprVPN"

    VyprVPN offers the OpenVPN files here: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    The provided zip file contains two folders with the .ovpn files. One called OpenVPN160 one OpenVPN256. Just delete the OpenVPN160 folder from the zip file then upload it to GL.iNet router as usual.

<div id="wevpn"></div>

??? "Wevpn"

    [Official Website](https://www.wevpn.com/aff/glinet){target="_blank"}

    1. Access the Members Area to make a custom config using the Config Generator.

        ![wevpn manual configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/wevpn/wevpn_manual_configuration_generator.jpg){class="glboxshadow"}

    2. Choose the Protocal to UDP or TCP, the OpenVPN version, and the location. Then to download the configuration.

<div id="zoogvpn"></div>

??? "ZoogVPN"

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Sign in its [official website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}, then access the [OpenVPN configuration files page](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}, you will find all the servers here. Download the configuration file in the TCP column or UDP column.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Then follow the [guide to setup OpenVPN Client on GL.iNet router](#setup-openvpn-client), the username and password are the same as the ones used to log into ZoogVPN website.