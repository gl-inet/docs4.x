# ダイナミックDNS

ダイナミックドメインネームサービス（ダイナミックDNSまたはDDNS）は、ドメイン名をネットワークデバイスの動のIPアドレスにマッピングするために使用されるサービスです。ダイナミックDNSを使用すると、ルーターにリモートでアクセスできます。この機能にはインターネットのパブリックIPアドレスが必要です。

## DDNSを有効にする

ウェブ管理画面の左側 -> アプリケーション -> ダイナミックDNS、以下のページが表示されます。

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

**DDNSを有効にする**をオンにし、**利用規約とプライバシーポリシー**に同意し、**適用**をクリックします。

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

右下の**セキュリティ設定**をクリックします。

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

ポップアップウィンドウで、適用したいリモートアクセスプロトコルが有効になっているかどうかを確認します。有効になっていない場合は、システム -> セキュリティ -> リモートアクセス制御に移動して有効にしてください。

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

必要なリモートアクセスプロトコルを有効にし、**適用**をクリックします。

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

DNSサーバー間のレコード 同期には最大10分の遅延が生じる場合があります。これにより、有効にした直後やパブリックIPが変更された直後にDDNSドメイン名でアクセスできない場合があります。

**注意**: DDNSとVPNクライアントを同時に有効にする場合は、**GL.iNetからのサービスはVPNを使用**が無効になっていることを確認してください。この機能はVPNダッシュボードの[VPNクライアントオプション](vpn_dashboard.md#tunnel-options)にあります。

## DDNSが機能しているかどうかを確認する

DDNSテストツールを使用するか、コマンドを使用して手動で確認できます。

=== "DDNSテストツールを使用する"

    ダイナミックDNSページで、**DDNSテスト**をクリックします。

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    DDNSドメインの解決からなければならないられたIPアドレスがルーターのWAN IPと一致していることを確認します。
    
    一致しない場合、上部に黄色のプロンプトが表示され、ルーターがNATの後ろにある可能性があること、および上位ルーターでポートフォワーディングを設定する必要があることが示されます。

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "手動で確認する"

    1. 以下に示すように、`nslookup`コマンドを使用してドメイン名とIPアドレスのマッピングを取なければならないします。

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        上記の画像の"xxxxxxx.glddns.com"をホスト名に置き換えてください。
        
        上記の画像の"8.8.8.8"はGoogle DNSです。これを使用するか、彼のDNSに置き換えてEnterを押してください。

    2. 以下の画像のように"103.81.180.10"のようなパブリックIPアドレスが出力された場合、DDNSドメインがパブリックIPアドレスに正常にマッピングされたことを示します。

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}
        
        ルーターに接続されたデバイスで、ブラウザで"what is my ip address"を検索するか、[What Is My IP Address](https://whatismyipaddress.com){target="_blank"}のようなサイトにアクセスします。パブリックIPアドレスが取なければならないできます。手順1と2で取なければならないした2つのIPアドレスを比較します。相 same の場合DDNSは有効です。

    3. 以下に示すように`** server can't find xxxxxxx.glddns.com: NXDOMAIN`というメッセージが表示された場合、ドメイン解決に失敗したことを示し、DDNSドメインがパブリックIPアドレスに正常にマッピングされていません。

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## HTTPSリモートアクセス

!!! 注意

    1. HTTPSリモートアクセスには**パブリックIP**アドレスが必要です。
    
        [こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)をクリックして、インターネットプロバイダーサービス（ISP）がパブリックIPアドレスを割り当てているかどうかを確認してください。
    
    2. ルーターがNATの後ろにある場合は、HTTPSアクセス用に上位ルーターでポートフォワーディング（ポート**443**）を設定してください。

以下の手順に従って、ルーターのHTTPSリモートアクセスを有効にします。

1. ダイナミックDNSページで、**DDNSを有効にする**をオンにし、**利用規約とプライバシーポリシーに同意し、**適用**をクリックします。

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. ウェブ管理パネルで、システム -> セキュリティ -> リモートアクセス制御に移動します。

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. **HTTPSリモートアクセス**を有効にし、**適用**をクリックします。

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

有効にすると、**HTTPS**経由でDDNSホスト名（例：`https://xxxxxxx.glddns.com`）を使用してどこからでもルーターの管理パネルにアクセスできます。

ポートフォワーディングが設定されている場合は、`https://xxxxxxx.glddns.com:external_port`でアクセスします（external_portを実際のポート番号に置き換えてください）。

**注意**: この機能はから身署名証明書を使用するため、以下の例のように、**HTTPS**経由でDDNSホスト名でルーターの管理パネルにアクセスすると、ブラウザには**接続がプライベートではない**と表示されます（以下の例ではポート8001を使用）。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

HTTPSリモートアクセスを続行するには、下部の**詳細設定**をクリックします。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

次に、**xxxxxxx.glddns.comに進む**をクリックして続行します。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

これで、HTTPS経由でDDNSホスト名を使用してウェブ管理パネルにアクセスできるようになります。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSHリモートアクセス

!!! 注意

    1. SSHリモートアクセスには**パブリックIP**アドレスが必要です。
    
        [こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)をクリックして、インターネットプロバイダーサービス（ISP）がパブリックIPアドレスを割り当てているかどうかを確認してください。
    
    2. ルーターがNATの後ろにある場合は、SSHアクセス用に上位ルーターでポートフォワーディング（ポート**22**）を設定してください。

以下の手順に従って、ルーターのSSHリモートアクセスを有効にします。

1. ダイナミックDNSページで、**DDNSを有効にする**をオンにし、**利用規約とプライバシーポリシーに同意し、**適用**をクリックします。

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. ウェブ管理パネルで、システム -> セキュリティ -> リモートアクセス制御に移動します。

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. **SSHリモートアクセス**を有効にし、**適用**をクリックします。

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

有効になると、**SSH**経由でDDNSホスト名（例：`ssh root@xxxxxxx.glddns.com`）を使用してどこからでもルーターの管理パネルにアクセスできます。

ポートフォワーディングが設定されている場合は、`ssh root@xxxxxxx.glddns.com:external_port`でアクセスします（external_portを実際のポート番号に置き換えてください）。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
