# Dynamic DNS

Dynamic Domain Name Service（Dynamic DNS または DDNS）は、ドメイン名をネットワーク機器の動的IPアドレスに紐付けるためのサービスです。Dynamic DNS を使用すると、ルーターへリモートアクセスできます。この機能を利用するには、インターネットのパブリックIPアドレスが必要です。

## DDNSを有効にする

Web 管理画面の左側メニューで、**APPLICATIONS** -> **Dynamic DNS** に移動します。

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

**Enable DDNS** をオンにし、**Terms of Services & Privacy Policy** に同意してから、**Apply** をクリックします。

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

右下の **Security Settings** をクリックします。

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

ポップアップウィンドウで、利用したいリモートアクセスプロトコルが有効になっているか確認します。有効になっていない場合は、SYSTEM -> Security -> Remote Access Control に移動して有効にしてください。

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

必要なリモートアクセスプロトコルを有効にし、**Apply** をクリックします。

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

DNS サーバー間のレコード同期には、最大 10 分程度の遅延が発生する場合があります。そのため、有効化直後やパブリックIPアドレスが変更された直後は、DDNS ドメイン名ですぐにアクセスできないことがあります。

**Note**: DDNS と VPN Client を同時に有効にする場合は、**Services From GL.iNet Use VPN** が無効になっていることを確認してください。この機能は、VPN Dashboard の [VPN Client Options](vpn_dashboard_v4.8.md#tunnel-options) にあります。

## DDNSが機能しているか確認する

DDNS が機能しているかどうかは、DDNS テストツールを使用するか、コマンドで手動確認できます。

=== "Using the DDNS Test tool"

    Dynamic DNS ページで、**DDNS Test** をクリックします。

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    DDNS ドメインを名前解決して得られた IP アドレスが、ルーターの WAN IP と一致していることを確認してください。
    
    一致しない場合は、画面上部に黄色のメッセージが表示されます。これは、ルーターが NAT 配下にある可能性があり、上位ルーターでポートフォワーディングを設定する必要があることを示しています。

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Check it manually"

    1. 以下のように `nslookup` コマンドを使用して、ドメイン名と IP アドレスの対応を確認します。

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        上の画像にある "xxxxxxx.glddns.com" は、ご自身の Host Name に置き換えてください。
        
        上の画像の "8.8.8.8" は Google DNS です。そのまま使用するか、別の DNS に置き換えて Enter キーを押してください。

    2. 下の画像の "103.81.180.10" のようなパブリックIPアドレスが結果として表示された場合、DDNS ドメインがパブリックIPアドレスに正しく紐付けられていることを意味します。

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}
        
        ルーターに接続されている端末で、ブラウザから "what is my ip address" を検索するか、[What Is My IP Address](https://whatismyipaddress.com){target="_blank"} のようなサイトにアクセスしてください。そこでパブリックIPアドレスを確認できます。手順 1 と 2 で取得した 2 つの IP アドレスを比較し、同じであれば DDNS は有効です。異なる場合は有効になっていません。

    3. 下のように `** server can't find xxxxxxx.glddns.com: NXDOMAIN` というメッセージが表示された場合は、ドメインの名前解決に失敗しており、DDNS ドメインがパブリックIPアドレスに正しく紐付けられていないことを示します。

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## HTTPS リモートアクセス

!!! Note

    1. HTTPS リモートアクセスには **Public IP** アドレスが必要です。
    
        ご利用のインターネットサービスプロバイダー（ISP）からパブリックIPアドレスが割り当てられているか確認するには、[こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)をクリックしてください。
    
    2. ルーターが NAT 配下にある場合は、HTTPS アクセス用に上位ルーターでポート **443** のポートフォワーディングを設定してください。

以下の手順で、ルーターの HTTPS リモートアクセスを有効にします。

1. Dynamic DNS ページで、**Enable DDNS** をオンにし、**Terms of Services & Privacy Policy** に同意してから、**Apply** をクリックします。

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Web 管理画面で、SYSTEM -> Security -> Remote Access Control に移動します。

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. **HTTPS Remote Access** を有効にし、**Apply** をクリックします。

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

有効にすると、**HTTPS** 経由で DDNS ホスト名（例: `https://xxxxxxx.glddns.com`）を使用し、どこからでもルーターの管理画面にアクセスできるようになります。

ポートフォワーディングを設定している場合は、`https://xxxxxxx.glddns.com:external_port ` としてアクセスします（external_port は実際のポート番号に置き換えてください）。

**Note**: この機能では自己署名証明書を使用するため、下図のように DDNS ホスト名を使用して **HTTPS** でルーターの管理画面にアクセスすると、ブラウザに **Your connection is not private** と表示されます（下の例ではポート 8001 を使用しています）。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

HTTPS リモートアクセスを続行するには、下部の **Advanced** をクリックします。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

次に、**Proceed to xxxxxxx.glddns.com** をクリックして続行します。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

これで、DDNS ホスト名を使って HTTPS で Web 管理画面にアクセスできるようになります。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSH リモートアクセス

!!! Note

    1. SSH リモートアクセスには **Public IP** アドレスが必要です。
    
        ご利用のインターネットサービスプロバイダー（ISP）からパブリックIPアドレスが割り当てられているか確認するには、[こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)をクリックしてください。
    
    2. ルーターが NAT 配下にある場合は、SSH アクセス用に上位ルーターでポート **22** のポートフォワーディングを設定してください。

以下の手順で、ルーターの SSH リモートアクセスを有効にします。

1. Dynamic DNS ページで、**Enable DDNS** をオンにし、**Terms of Services & Privacy Policy** に同意してから、**Apply** をクリックします。

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Web 管理画面で、SYSTEM -> Security -> Remote Access Control に移動します。

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. **SSH Remote Access** を有効にし、**Apply** をクリックします。

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

有効にすると、**SSH** 経由で DDNS ホスト名（例: `ssh root@xxxxxxx.glddns.com`）を使用し、どこからでもルーターにアクセスできるようになります。

ポートフォワーディングを設定している場合は、`ssh root@xxxxxxx.glddns.com:external_port` としてアクセスします（external_port は実際のポート番号に置き換えてください）。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
