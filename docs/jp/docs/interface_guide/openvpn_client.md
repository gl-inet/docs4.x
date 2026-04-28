# GL.iNet ルーターで OpenVPN クライアントを設定する {#setup-openvpn-client}

OpenVPN は、仮想プライベートネットワーク技術を用いて安全な site-to-site 接続または point-to-point 接続を確立する、オープンソースの VPN プロトコルです。

GL.iNet ルーターで OpenVPN クライアントを設定するには、以下の動画を見るか、下記の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

開始前に、OpenVPN の手動設定に対応した VPN サービスプロバイダーの有効な契約があることを確認してください。GL.iNet と互換性のある OpenVPN プロバイダーは [こちら](https://www.gl-inet.com/solutions/vpn/){target="_blank"} で確認できます。

一般的には、契約している VPN サービスプロバイダーの公式サイトで設定ファイルを取得し、それをルーターへアップロードして OpenVPN クライアントとして設定します。設定ファイルの取得方法が分からない場合は、[こちら](#get-configuration-files-from-openvpn-service-providers) を参照するか、プロバイダーのサポートへお問い合わせください。

OpenVPN クライアントは、Web 管理パネルまたは [モバイルアプリ](../faq/mobile_app.md) から設定できます。以下では Web 管理パネルから設定する手順を説明します。

---

Web 管理パネルで **VPN** -> **OpenVPN Client** を開きます。

NordVPN を契約している場合は **NordVPN** をクリックしてログインします。それ以外の場合は **Add Manually** をクリックして OpenVPN 設定ファイルをアップロードします。

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## NordVPN を設定する {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} は、速度とセキュリティに優れた人気のオンライン VPN サービスです。

GL.iNet ルーターの管理パネルには NordVPN のクイック設定が統合されています。ルーターの Web 管理パネルまたはモバイルアプリに NordVPN Dashboard で取得したアカウント認証情報を入力することで、すべての NordVPN サーバーの設定ファイルをオンラインで取得でき、手動でファイルをアップロードする必要がありません。

1. [こちら](https://my.nordaccount.com/){target="_blank"} から NordVPN の Web アカウントへログインします。

    ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

    ログイン後、Nord Dashboard の左側メニューで **NordVPN** をクリックし、**Set up NordVPN manually** をクリックします。

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    **service credentials** が表示されます。取得するには、まずメールアドレスの確認を完了し、その後コピーしておいてください。

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. ルーターの Web 管理パネルにログインし、**VPN** -> **OpenVPN Client** -> **NordVPN** を開きます。

    手順 1 で取得した **service credentials** を入力し（Nord アカウントのメールアドレス/パスワードでは **ありません**）、**Save and Continue** をクリックします。

    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. プロトコル、各ロケーションの最大サーバー数、ロケーションを選択し、**Apply** をクリックします。

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

    設定ファイルがダウンロードされます。

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. 接続されると、設定ファイルの横に緑色の点が表示されます。

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. 認証情報を編集します。

    歯車アイコンをクリックしてログイン認証情報を編集します。

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. すべてのファイルを削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除できます。

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## OpenVPN クライアントを手動で設定する（その他のプロバイダー向け） {#set-up-openvpn-client-manually-for-other-providers}

ご利用の OpenVPN サービスプロバイダーが管理パネルに統合されていない場合は、まず契約中のプロバイダーの公式サイトで設定ファイルを取得してください。その後、ルーターへアップロードして OpenVPN クライアントを設定します。

以下では [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} を例に説明します。

1. Private Internet Access の公式サイトから設定ファイルをダウンロードします。

2. ルーターの Web 管理パネルにログインし、**VPN** -> **OpenVPN Client** を開いて **Add Manually** をクリックします。

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. 左側のサイドバーにグループが作成されます。

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. グループに分かりやすい名前（例: private internet access）を付けます。

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. OpenVPN 設定ファイルをアップロードします。必要に応じて認証情報を入力し、**Apply** をクリックします。

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}

    - 認証に使用される認証情報には 4 種類あります。

        1. 認証なし

        2. ユーザー名とパスワードのみ

        3. パスフレーズのみ

        4. ユーザー名、パスワード、パスフレーズ

    アップロード後、設定ファイルが表示されます。

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. 右側の三点アイコンをクリックして接続を開始します。

    ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. 接続されると、設定ファイルの横に緑色の点が表示されます。

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## GL.iNet ルーターで OpenVPN サーバーを設定する

GL.iNet ルーターが 2 台ある場合は、1 台を OpenVPN サーバー（パブリック IP が必要）、もう 1 台を OpenVPN クライアントとして設定できます。これにより、サードパーティーの VPN サービスを契約しなくても、自分専用の VPN 接続を構築できます。

OpenVPN サーバーの設定方法は [こちら](openvpn_server.md) を参照してください。

## OpenVPN サービスプロバイダーから設定ファイルを取得する {#get-configuration-files-from-openvpn-service-providers}

30 以上の OpenVPN サービスプロバイダーをテストし、設定ファイル取得手順をまとめています。設定ファイルの取得方法が分からない場合は、以下を参照してください。

契約しているサービスプロバイダーが以下にない場合は、プロバイダーのサポートへお問い合わせください。

??? "NordVPN"
    ### NordVPN

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **NordVPN アカウントにログインする**

        [公式サイト](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} にログインし、Nord Account Dashboard を開くと、service credentials を確認できます。

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        Nord Dashboard にログイン後、左側の NordVPN をクリックし、**Set up NordVPN manually** をクリックします。

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        **Service credentials** を確認し、設定アップロードに使う場合に備えてコピーしておきます。

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **NordVPN サーバーを選んで設定ファイルをダウンロードする**

        **Server recommendation** タブを開くと、ネットワークに基づいて推奨サーバーが表示され、ダウンロード可能なプロトコルも確認できます。**Get setup configuration** をクリックして進みます。

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        ポップアップウィンドウで **OpenVPN** を選択し、UDP または TCP の設定をダウンロードします。

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    すべてのサーバー設定は [こちら](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip) からダウンロードできます。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    [モバイルアプリ](../faq/mobile_app.md) を使って NordVPN を設定することもできます。

??? "AirVPN"
    ### AirVPN

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. AirVPN アカウントにログインします。

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. 左側で Config Generator を選び、OS として Linux を選択します。その後、利用したいサーバーを選択します。

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. 設定ファイルのダウンロードページが表示されます。

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    情報は [Astrill 公式手順](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"} を参照しています。

    1. Astrill の OpenVPN 設定 ZIP を生成してダウンロードします。

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. `OPENVPN_GUI` のような Description を入力します。

    3. **ADD to my certificates** ボタンをクリックします。

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. OpenVPN 証明書が追加されたら、**Download** をクリックします。

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

    [Dashboard](https://users.bolehvpn.net/){target="_blank"} にログインし、設定ファイルをダウンロードして [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"} 形式を選択します。ダウンロード後に zip ファイルを展開してください。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [こちら](https://www.cactusvpn.com/downloads/){target="_blank"} から直接ダウンロードします。

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [こちら](https://cryptostorm.is/configs/ecc/){target="_blank"} から直接ダウンロードします。

??? "CyberGhost"
    ### CyberGhost

    [Official Website](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    情報は [CyberGhost 公式手順](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"} を参照しています。

    1. CyberGhost VPN のオンラインアカウントにログインします。

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. 左側メニューから "**VPN**" を選択し、"**Configure Device**" をクリックして、以下のようにサーバー設定を作成します。

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. 次の内容でサーバー設定を作成します。

        * **Protocol** : **OpenVPN**
        * **Country** : ネイティブプロトコル接続は 1 台のサーバーでのみ使用できるため、接続元にしたい国を選択します。その国で使うサーバーは CyberGhost が自動的に選択します。
        * **Server group** : 使用するサーバーグループと OpenVPN プロトコル（UDP または TCP）を選択します。

        **OpenVPN UDP** は TCP より高速ですが、環境によってはダウンロードが途切れる場合があります。これがデフォルト設定です。

        **OpenVPN TCP** は UDP より安定しやすい一方で、速度はやや低下します。突然切断されるなど接続問題が繰り返し発生する場合はこちらを選択してください。

        希望する項目を選択したら、**Save Configuration** で保存します。

    4. 設定ダッシュボードで生成された **OpenVPN** 認証情報を見るには、**View Configuration** をクリックします。

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. 接続設定後は、次の情報を控えてください。

        * **Server Group** : 接続先の国（サーバー）のアドレスです。例: `12345-1-ca.cg-dialup.net`。このアドレスは前の手順で選択した国ごとに変わります。実際に使われる個別サーバーは CyberGhost が自動で選択します。
        * **Username** : このプロトコル専用に生成されるユーザー名です。通常の CyberGhost アカウントのユーザー名ではありません。手動設定で CyberGhost サーバーへ認証するためだけに使用します。GL.iNet ルーターで OpenVPN を設定する際に必要です。
        * **Password** : このプロトコル専用に生成されるパスワードです。通常の CyberGhost アカウントのパスワードではありません。手動設定で CyberGhost サーバーへ認証するためだけに使用します。GL.iNet ルーターで OpenVPN を設定する際に必要です。

        完了したら設定ファイルをダウンロードします。*Download Configuration* をクリックして、設定ファイルを PC に保存してください。

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN

    [Official Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    情報は [ExpressVPN 公式手順](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"} を参照しています。

    1. [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} のサイトへアクセスし、ExpressVPN の認証情報でログインします。

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        メールで送信された **verification code** を入力します。

    2. "Set up your devices" セクションで **More** をクリックします。

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. **Manual Configuration** をクリックします。

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. **username**、**password**、および **OpenVPN configuration files** の一覧が表示されます。

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        利用したいロケーションをクリックして `.ovpn` ファイルをダウンロードします。

        **このブラウザウィンドウは閉じずに残しておいてください**。後で設定時にこの情報が必要です。

    [Refer link](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    OpenVPN TCP/UDP 用の FastestVPN 設定ファイル（ZIP ファイル）は [こちら](https://support.fastestvpn.com/download/fastestvpn_ovpn/) からダウンロードできます。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. FinchVPN アカウントにログインします。

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Download ページを開き、FinchVPN OpenVPN Config の下にある Download をクリックします。

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Linux を選択します。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. 好みのプロトコルを選択します。通常は最初の **Port 8484 over UDP** を選べば問題ありません。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. ファイルをダウンロードする前に、ユーザー名とパスワードを含めるチェックボックスをオンにしてください。

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. HideIPVPN アカウントにログインします。

    2. 左側の Package を開き、契約中のパッケージをクリックして有効であることを確認します。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. VPN タブには、OpenVPN 接続時に使用するユーザー名とパスワードの VPN Login Details が表示されます。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. 下へスクロールして OpenVPN 設定ファイルをダウンロードします。

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Hide.me アカウントにログインし、左側で Server Locations を見つけます。

    2. Windows 用の OpenVPN Configuration をダウンロードします。

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [Official Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Note: Hotspot Shield のルーター用設定ファイルは現在提供・サポートされていません。以下の手順は、すでにファイルを保持している方向けの参考情報です。**

    1. [https://www.hotspotshield.com/](https://www.hotspotshield.com/) を開き、Account をクリックします。必要に応じてサインインしてください。

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router) を開きます。

        Select location のドロップダウンから、ルーターで使用する仮想ロケーションを選びます。その後 "Download file" をクリックすると、設定ファイル（`config.ovpn`）が PC にダウンロードされます。ルーターで OpenVPN クライアントを設定する際に、ユーザー名とパスワードの入力が必要です。

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Refer link](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - [こちら](https://configs.ipvanish.com/configs/configs.zip) から全サーバーの設定ファイルをまとめてダウンロードできます。zip にはサーバー設定ファイル（`.ovpn`）と証明書ファイル（`.crt`）が含まれます。機種によっては zip がやや大きい場合があるため、使わないサーバーの `.ovpn` を削除してください。

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - [こちら](https://www.ipvanish.com/software/configs/) から個別のサーバー設定ファイルをダウンロードすることもできますが、**ca.ipvanish.com.crt** もあわせてダウンロードする必要があります。ルーターへアップロードする前に、**ca.ipvanish.com.crt** と `.ovpn` 設定ファイルを zip アーカイブにまとめてください。

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    Ivacy で OpenVPN クライアントを設定するには、次の情報が必要です。

    - "Download Configuration" 画面に表示される、OpenVPN 手動設定用のユーザー名
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - パスワード（Ivacy アカウントへのサインインに使うものと同じ）
    - OpenVPN 設定ファイル

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. [OpenVPN 設定ファイル](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip) をダウンロードします。

    2. [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"} で Account ID を確認します。

    3. 設定ファイルを Add a New OpenVPN Configuration にドラッグすると、User Name と Password の入力を求められます。User Name には **ivpn** で始まる Account ID を入力し、Password には **ivpn** など任意の文字列を入力できます。

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad"
    ### Mullvad

    [Official Website](https://mullvad.net/en){target="_blank"}

    1. [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"} のサイトへアクセスし、Mullvad の認証情報でログインします。

    2. OpenVPN Configuration を選択します。

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. **Linux** を選択し、サーバーロケーションを選びます。

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    ログインするだけで、以下のメニューから簡単に OpenVPN 設定ファイルを取得できます。

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    サーバーを選択してダウンロードします。

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    ユーザー名とパスワードは、OVPN へのログインに使用するものと同じです。

??? "OysterVPN"
    ### OysterVPN

    [Official Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. [OysterVPN サーバー一覧ページ](https://support.oystervpn.com/server-list/){target="_blank"} にアクセスし、**Download .ovpn file** をクリックして設定ファイルをダウンロードします。

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. OpenVPN 接続用のユーザー名とパスワードは、OysterVPN へのログインに使うものと同じです。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

??? "PIA (Private Internet Access)"
    ### PIA

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [こちら](https://www.privateinternetaccess.com/openvpn/openvpn.zip) から直接ダウンロードします。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

??? "PrivadoVPN"
    ### PrivadoVPN

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    ログインすると、**Download VPN Configuration** を簡単に見つけられます。

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

??? "PrivateVPN"
    ### PrivateVPN

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [こちら](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank"} から直接ダウンロードします。

    [Here](https://privatevpn.com/client/PrivateVPN-TUN.zip) は公式ダウンロードリンクです。ルーターへのインポート時の不具合により、zip 内のファイル名に `Bogotá` という特殊文字が含まれていたため、名前を変更したファイルを上記リンクで提供しています。今後のバージョンで修正予定です。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

??? "Proton VPN"
    ### Proton VPN

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN は WireGuard サービスも提供しているため、WireGuard の利用を推奨します。[こちら](wireguard_client.md#wireguard-providers) を参照してください。**

    1. [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} のアカウントへログインします。

    2. 左側の **Download** をクリックします。

    3. Router プラットフォームやプロトコルなどを選択し、設定ファイルをダウンロードしたい国を探します。

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. OpenVPN 接続用の認証情報は、Proton サイトのダッシュボードにログインするものとは異なります。**Account -> OpenVPN/IKEv2 username** で確認できます。

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    PureVPN で OpenVPN クライアントを設定するには、OpenVPN 用ユーザー名、パスワード、設定ファイルが必要です。これらは PureVPN アカウントで確認できます。

    1. [PureVPN アカウントにサインインします。](https://my.purevpn.com/)
    2. 左側サイドバーで **Subscriptions** をクリックします。
    3. 下へスクロールして OpenVPN 用ユーザー名とパスワードを確認します。
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. 左側サイドバーで **Manual Configuration** をクリックします。
    5. VPN ロケーションを選択し、**Download** をクリックして設定ファイルをダウンロードします。

    [Refer link](https://support.purevpn.com/openvpn-files)

    GL.iNet ルーターは PureVPN の [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"} 機能をサポートしていません。これは PPTP を必要とするためです。

??? "SaferVPN"
    ### SaferVPN

    [Official Website](https://safervpn.com/?a_aid=563){target="_blank"}

    [こちら](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup) をクリックして設定ファイルを直接ダウンロードします。

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN は OpenVPN と WireGuard の両方を提供しています。通常は OpenVPN より WireGuard の方が高速なため、WireGuard の利用を推奨します。[こちら](wireguard_client.md#starvpn) を参照してください。

    OpenVPN を使いたい場合は、以下の手順で設定ファイルをダウンロードしてください。

    1. **StarVPN アカウントを登録する**

        [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} で自分に合った VPN プランを選択します。登録は checkout 時、または直接 [こちら](https://www.starvpn.com/dashboard/register.php){target="_blank"} から行えます。

    2. **OpenVPN Configuration をダウンロードする**

        StarVPN の member area [dashboard](https://www.starvpn.com/dashboard){target="_blank"} にログインします。Dashboard の **VPN Configuration** セクションで **OpenVPN Config** をクリックします。GL.iNet ルーターへファイルをアップロードするときに認証に必要となるため、OVPN 用のユーザー名とパスワードを控えておいてください。

        ![download starvpn ovpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/ovpnconfigdl.png){class="glboxshadow"}

        UDP または TCP を選択して設定ファイルをダウンロードします。

        ![select udp or tcp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/udp_tcp.png){class="glboxshadow"}

    3. **設定ファイルを編集する**

        一部の GL.iNet ルーターは IPv6 をサポートしていません。互換性や接続の問題を避けるため、`.ovpn` 設定ファイルを開いて、以下のように IPv6 関連の内容を削除してください。

        ![remove ipv6](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/remove_ipv6.png){class="glboxshadow"}

??? "StreamVPN"
    ### StreamVPN

    [Official Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} アカウントでログインすると、契約情報が表示されます。**Install & Guides** をクリックします。

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. **VPN Router** をクリックすると、`StreamVPN.zip` という zip アーカイブがダウンロードされます。

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Note:** ファイル名に "Primary" を含む設定ファイルのみ動作します。

??? "StrongVPN"
    ### StrongVPN

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} アカウントでログインすると VPN Accounts Summary が表示されます。**Account Setup Instructions** をクリックします。

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Manual setup セクションを見つけ、手順に従って設定を取得します。

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **ログイン情報を確認する**

        Surfshark の service credentials は、通常の Surfshark アカウント認証情報（メールアドレスとパスワード）とは異なります。ルーターで手動 OpenVPN 設定を行うには、Surfshark service credentials が必要です。

        [公式サイト](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} にログインし、[このページ](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"} を開くと、手動接続に必要な情報を確認できます。

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Surfshark サーバーを選択する**

        **Locations** タブを選択すると、Surfshark サーバーの一覧が表示されます。

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        TCP または UDP を選ぶよう求められます。違いは [こちら](../faq/openvpn_tcp_udp.md) を参照してください。

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}

    すべての設定は [こちら](https://api.surfshark.com/v1/server/configurations) から直接ダウンロードできます。

    ヒント: ZIP ファイルが大きすぎてアップロードできない場合は、`.zip` ファイルから一部の `.ovpn` ファイルを削除するか、単一の `.ovpn` ファイルをアップロードしてください。

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [こちら](https://vpn.ac/ovpn/) からダウンロードします。

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    OpenVPN 設定ファイルは [VPN Gate website](https://www.vpngate.net/en/) にサーバーロケーションごとに掲載されています。

    1. **OpenVPN** 列にある OpenVPN Config file をクリックします。

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. ダウンロードページが表示されます。

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    情報は [VPN unlimited 公式手順](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"} を参照しています。

    User Office にログインし、VPN Unlimited サービスの **Manage** をクリックして、以下の簡単な手順に従います。

    1. デバイスを選択する

        リストからデバイスを選ぶか、新しいデバイスを作成します。空きスロットが足りない場合は、古いデバイスを削除するか追加スロットを購入してください。

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. 希望するサーバーロケーションを選択する

        VPN Unlimited は 70 以上のロケーションに 400 以上の多彩なサーバーを提供しています。この例では Germany を選択します。

    3. VPN プロトコルを選択する

        OpenVPN を選択します。

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. 設定を作成する

        Generate をクリックすると、VPN 接続の設定に必要な情報がすべて表示されます。

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPN の OpenVPN ファイルは [こちら](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"} から取得できます。

    提供される zip には `.ovpn` ファイルを含む 2 つのフォルダー（OpenVPN160 と OpenVPN256）が入っています。zip から OpenVPN160 フォルダーを削除し、通常どおり GL.iNet ルーターへアップロードしてください。

??? "Windscribe"
    ### Windscribe

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. [こちら](https://windscribe.com/login?auth_required){target="_blank"} から Windscribe の会員アカウントへログインし、[OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"} を開きます。

    2. 使用したいサーバーロケーション、プロトコル（UDP/TCP）、ポート（例: 1194）、OpenVPN バージョン（通常は新しいもの）を選択し、**Download Config** をクリックします。すると `.ovpn` ファイルがローカルデバイスにダウンロードされます。

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. 同じページで **Get Credentials** をクリックすると、対応する認証情報が表示されます。これは後でルーターの Web 管理パネルで設定ファイルをアップロードして認証する際に使用します。認証情報をコピーするか、このページを開いたままにしてください。

    4. その後、[こちらのガイド](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers) に従って続行してください。

??? "ZoogVPN"
    ### ZoogVPN

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    [公式サイト](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"} にサインインし、[OpenVPN configuration files page](https://app.zoogvpn.com/setup/configuration-files){target="_blank"} を開くと、すべてのサーバー一覧が表示されます。TCP 列または UDP 列から設定ファイルをダウンロードしてください。

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    その後、[GL.iNet ルーターで OpenVPN クライアントを設定するガイド](#setup-openvpn-client) に従って続行してください。ユーザー名とパスワードは ZoogVPN サイトへのログインに使用するものと同じです。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
