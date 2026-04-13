# GL.iNet ルーターで WireGuard クライアントを設定する

**Note**: このガイドはファームウェア v4.7 以降に適用されます。以前のバージョンについては [こちら](wireguard_client_v4.6.md) を参照してください。

---

WireGuard® は、最先端の暗号技術を利用した、非常にシンプルで高速かつモダンな VPN です。IPsec よりも高速・簡潔・軽量で使いやすいことを目指しており、OpenVPN よりも大幅に高いパフォーマンスを期待できます。

GL.iNet ルーターで WireGuard クライアントを設定するには、以下の動画を見るか、下記の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

開始前に、WireGuard の手動設定に対応した VPN サービスプロバイダーの有効な契約があることを確認してください。GL.iNet と互換性のある WireGuard プロバイダーは [こちら](https://www.gl-inet.com/solutions/vpn/){target="_blank"} で確認できます。

一般的には、契約している VPN サービスプロバイダーの公式サイトで設定ファイルを取得し、それをルーターにアップロードして WireGuard クライアントとして設定します。設定ファイルの取得方法が分からない場合は、[こちら](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) を参照するか、プロバイダーのサポートへお問い合わせください。

WireGuard クライアントは、Web 管理パネルまたは [モバイルアプリ](../faq/mobile_app.md) から設定できます。

- **モバイルアプリ** には、AzireVPN、Mullvad VPN、OVPN、StrongVPN、PIA VPN などの WireGuard サービスプロバイダーが一部統合されています。契約しているサービスのログイン情報を入力するだけで簡単に設定できます。アプリを開き、画面の案内に従って設定してください。

- **Web 管理パネル** では、一部の WireGuard サービスプロバイダーが統合されているだけでなく、手動設定の入口も用意されています。契約中の WireGuard サービスの認証情報を入力して素早く設定することも、設定ファイルを手動でアップロードして設定を完了することもできます。

以下では Web 管理パネルから設定する手順を説明します。該当する WireGuard サービスプロバイダーを選んで、目的の手順へ進んでください。

* [AzireVPN を設定する](#set-up-azirevpn)
* [Hide.me を設定する](#set-up-hideme)
* [IPVanish を設定する](#set-up-ipvanish)
* [Mullvad を設定する](#set-up-mullvad)
* [NordVPN を設定する](#set-up-nordvpn)
* [PIA (Private Internet Access) を設定する](#set-up-pia-private-internet-access)
* [PureVPN を設定する](#set-up-purevpn)
* [Surfshark を設定する](#set-up-surfshark)
* [WireGuard クライアントを手動で設定する（その他のプロバイダー向け）](#set-up-wireguard-client-manually-for-other-providers)

## AzireVPN を設定する {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} は、WireGuard のような安全でモダンかつ堅牢なトンネルを提供する、プライバシー重視の VPN サービスです。

Web 管理パネルまたはモバイルアプリを使って、GL.iNet ルーターで AzireVPN を設定する方法は以下の動画でも確認できます。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

または、以下の手順で Web 管理パネルから AzireVPN を設定できます。

Web 管理パネルで **VPN** -> **WireGuard Client** -> **AzireVPN** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. 契約を更新します。

    **Go Renew** をクリックすると、契約更新のために公式サイトへリダイレクトされます。

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Hide.me を設定する {#set-up-hideme}

[Official Website](https://www.hideipvpn.com/){target="_blank"}

Web 管理パネルで **VPN** -> **WireGuard Client** -> **Hide.me** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## IPVanish を設定する {#set-up-ipvanish}

[Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

Web 管理パネルで **VPN** -> **WireGuard Client** -> **IPVanish** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. サーバーを選択します。

    接続したいサーバーを選び、**Apply** をクリックします。

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Mullvad を設定する {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} は、オンラインでの行動、個人情報、位置情報のプライバシー保護を支援する VPN サービスです。

Web 管理パネルで **VPN** -> **WireGuard Client** -> **Mullvad** を開きます。

1. **Account** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. サーバーを選択します。

    接続したいサーバーを選び、**Apply** をクリックします。

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. 契約を更新します。

    **Go Renew** をクリックすると、契約更新のために公式サイトへリダイレクトされます。

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## NordVPN を設定する {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} は、速度とセキュリティを兼ね備えたオンライン VPN サービスです。

1. [こちら](https://my.nordaccount.com/){target="_blank"} をクリックして、NordVPN の Web アカウントにログインします。

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}

    Nord ダッシュボードにログインしたら、左側の NordVPN をクリックし、**Set up NordVPN manually** をクリックします。

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_dashboard.png){class="glboxshadow"}

    その後、**Access token** を確認できます。

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/manual_setup.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/generate_new_token.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/copy_access_token.png){class="glboxshadow"}

2. ルーターの Web 管理パネルにログインし、**VPN** -> **WireGuard Client** -> **NordVPN** を開きます。

    **Token** を入力して **Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. サーバーを選択します。

    接続したいサーバーを選び、**Apply** をクリックします。

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## PIA (Private Internet Access) を設定する {#set-up-pia-private-internet-access}

[Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

Web 管理パネルで **VPN** -> **WireGuard Client** -> **PIA** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. サーバーを選択します。

    接続したいサーバーを選び、**Apply** をクリックします。

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## PureVPN を設定する {#set-up-purevpn}

[Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

Web 管理パネルで **VPN** -> **WireGuard Client** -> **PureVPN** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    利用可能な設定ファイルがすべて生成されます。

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

4. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Surfshark を設定する {#set-up-surfshark}

[Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

Web 管理パネルで **VPN** -> **WireGuard Client** -> **Surfshark** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. サーバーを選択します。

    接続したいサーバーを選び、**Apply** をクリックします。

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. 公開鍵を更新します。

    VPN サーバーへ接続できない場合は、**Refresh** をクリックして公開鍵を更新できます。

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Windscribe を設定する {#set-up-windscribe}

[Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

Web 管理パネルで **VPN** -> **WireGuard Client** -> **Windscribe** を開きます。

1. **Username** と **Password** を入力し、**Save and Continue** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. サーバーを選択します。

    接続したいサーバーを選び、**Apply** をクリックします。

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    すると、選択したサーバーに対応する設定ファイル一覧が表示されます。

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. 接続を開始します。

    使用したいサーバーを選択し、右側の三点アイコンをクリックして接続を開始します。

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    接続されると、設定ファイルの横に緑色の点が表示されます。

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    VPN 接続の詳細は **VPN Dashboard** に表示されます。

    ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. サーバー一覧を更新します。

    **Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得でき、サーバーメンテナンスや停止による接続失敗を避けやすくなります。

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. 認証情報を編集、またはログアウトします。

    歯車アイコンをクリックすると、ログイン認証情報の編集やログアウトができます。

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. 公開鍵を更新します。

    VPN サーバーへ接続できない場合は、**Refresh** をクリックして公開鍵を更新できます。

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. すべて削除します。

    **Delete All** をクリックすると、すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も同時に削除するか選択できます。

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## WireGuard クライアントを手動で設定する（その他のプロバイダー向け） {#set-up-wireguard-client-manually-for-other-providers}

別の WireGuard サービスプロバイダーを利用している場合は、WireGuard 設定ファイルをダウンロードして、以下の手順で WireGuard Client を設定できます。設定ファイルのダウンロード方法が分からない場合は、[このガイド](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) を参照するか、プロバイダーのサポートへお問い合わせください。

Web 管理パネルで **VPN** -> **WireGuard Client** を開きます。

1. **Add Manually** をクリックします。

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. 左側のサイドバーにグループが作成されます。

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. グループに分かりやすい名前（例: azirevpn）を設定します。その後、設定ファイル（対応形式: zip、tar、gz、conf、txt）をアップロードするか、設定内容を手動で追加します。

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Upload a configuration file**

        アップロードエリアをクリックして WireGuard 設定ファイルをアップロードし、**Apply** をクリックします。

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Manually add configuration**

        アップロードエリア下部にある **Manually Add Configuration** をクリックします。

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        分かりやすい名前を付けて、設定内容をテキストボックスへ貼り付けます。その後 **Apply** をクリックします。

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        各項目を確認したい場合は Item mode に切り替えて設定内容を確認できます。その後 **Apply** をクリックします。

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. 右側の三点アイコンをクリックして接続を開始します。

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. 接続後は、**VPN Dashboard** ページで接続状態を確認できます。

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## GL.iNet ルーターで WireGuard サーバーを設定する

サードパーティーの VPN サービスを契約したくない場合は、GL.iNet ルーターを 2 台用意し、1 台を WireGuard サーバー、もう 1 台を WireGuard クライアントとして設定することもできます。

これは特に、自宅ネットワークの ISP がパブリック IP を提供しており、外出先から VPN 経由で自宅ネットワークへ安全に接続して、内部リソースへアクセスしたい場合に適しています。商用 VPN サービスを継続契約する費用や手間を省けます。

WireGuard サーバーの設定については、[こちら](wireguard_server.md) を参照してください。

---

WireGuard® は Jason A.Donenfeld の登録商標です。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
