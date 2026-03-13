# GL.iNetルー器でのWireGuardクライアントの設定方法（firmware v4.6で前）

!!! 注意

    このガイドはfirmware v4.6で前に基づいています 最も新バージョンを使用している場合 は、ここをご覧ください。

WireGuard® は **最も新の暗号化技術**を使用した、非常にシンプルで高速で最も新のVPNです。IPSecよりも速く、よりシンプルで軽量で有用なすることをwhileAvoidthe massive headacheを目のとしています。OpenVPNよりも大幅にパフォーマンスが高いことを意図しています。

プロバイダーからWireGuardサービスをすでに購入しているが、設定ファイルを取なければならないする方法がわからない場合は、プロバイダーからの設定ファイルの取なければならない、またはそのサポートにお問い合わせください。

Web管理パネルまたはモバイルアプリを介してWireGuardクライアントを設定できます。モバイルアプリには、AzireVPN、Mullvad VPN、OVPN、StrongVPN、PIA VPNなど、いくつかのWireGuardサービスプロバイダーがすでに統合されています。

Web管理パネル介して設定するには、以下のガイドに従ってください。

メンバーを持有している場合はAzireVPNまたはMullvadボタンをクリックしてログインするか、「手動で追加」をクリックしてWireGuardプロファイルをアップロードできます。

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## AzireVPNの設定

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} は、WireGuardなどの安全で現代ので堅牢なトンネルを 提供する隐私重視のVPNサービスすることです。

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. 「ユーザー名」と「パスワード」を入力し、「認証情報を保存してサーバーを取なければならない」をクリックします。各サーバーの設定ファイルが生成されます。

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. VPNダッシュボードに移動して接続を有効にします。

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    接続すると、ユーザーのIPアドレスと送受信されたバイト数が表示されます。

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. サーバーをアップデート

    AzireVPNは一部のサーバーを維持またはシャットダウンする場合があり、接続が失敗する可能性があります。「サーバーをアップデート」をクリックして利用可能な最も新サーバーを取なければならないできます。

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. 認証情報を編集

    歯車アイコンをクリックして認証情報を編集します。

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Mullvadの設定
