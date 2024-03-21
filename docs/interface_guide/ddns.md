# ダイナミックDNS

ダイナミックドメインネームサービス（ダイナミックDNSまたはDDNS）は、ドメイン名をネットワークデバイスの動的IPアドレスにマッピングするために使用されるサービスです。

ウェブ管理画面の左側 -> アプリケーション -> ダイナミックDNS

![ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/ddns.png){class="glboxshadow"}

## DDNSを有効にする

利用規約とプライバシーポリシーの**DDNSを有効にする**トグルをオンにして、**適用**ボタンをクリックします。通常、有効になるまで数分かかります。

DDNS の更新頻度は 10 分に 1 回です。

![enable ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/enable_ddns.png){class="glboxshadow"}

**注意**: DDNS と VPN クライアントを同時に使用する場合は、 [VPN クライアントのグローバル オプション](vpn_dashboard.md#global-options-of-vpn-client)で**GL.iNetからのサービスはVPNを使用しません**を有効にしてください。

## DDNS が有効かどうかを確認する

=== "DDNSテストツールを使用する"

    **DDNS Test**をクリックしてください。

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/click_ddns_test.png){class="glboxshadow"}

    以下のように、**あなたのDDNSはx.x.x.xとして解決されました**と表示された場合、DDNSが機能することを示しています。言い換えれば、この**ホスト名**は、インターネットアクセスのためのルーターの最終的な出口IPにマッピングされています。

    ![ddns works](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/ddns_test_resolved.png){class="glboxshadow"}

=== "または手動で確認する"

    以下の 2 つの IP アドレスが同じかどうかを確認し、同じであれば DDNS が有効であり、そうでなければ無効です。

    * 以下に示すように `nslookup` コマンドを使用して、ドメイン名と IP アドレス間のマッピングを取得します。 `zw72cd7.glddns.com` をホスト名に変更する必要があります。 `8.8.8.8` はGoogle DNSですが、他のDNSに変更することもできます。

        `nslookup zw72cd7.glddns.com 8.8.8.8`

        ![nslookup](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/nslookup.png){class="glboxshadow"}

        上記の出力は、ホスト名が IP アドレスにマップされたことを意味します。

    * ルーターに接続されたスマホや PC を使用して、Google で **my ip address** を検索するか、[https://whatismyipaddress.com/](https://whatismyipaddress.com/){target="_blank"}のようなサイトにアクセスします。

## HTTPリモートアクセス

この機能にはパブリック IP アドレスが必要です。 インターネット プロバイダー サービスがパブリック IP アドレスを割り当てているかどうかを確認するには[こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)をご確認ください。

ルーターがNATの後ろにある場合、上位のルーターでポートフォワーディングを設定する必要があるかもしれません。ポート番号**80**を使用します。

![HTTP-Remote-Access](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/http_remote_access.png){class="glboxshadow"}

上記の手順に従って、HTTPリモートアクセスを有効にします。

***HTTPは暗号化されていませんので、ご自身の責任においてご利用ください。***

HTTPリモートアクセスを有効にすると、DDNSホスト名の**http**でどこからでも管理パネルにアクセスできます。 e.g. `http://xxxxxxx.glddns.com`. ポートフォワーディングを使用する場合は、 `http://xxxxxxx.glddns.com:YourExternalPort`のようにアクセスする必要があります。

## HTTPS リモート アクセス

この機能にはパブリックIPアドレスが必要です。 インターネットプロバイダーからパブリックIPアドレスが割り当てられているかどうかを確認するには、 [こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)を確認してください。

ルーターがNATの後ろにある場合、上位のルーターでポートフォワーディングを設定する必要があるかもしれません。 **443**ポートを使用します。

![HTTPS-Remote-Access](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access.png){class="glboxshadow"}

HTTPS リモート アクセスを有効にすると、DDNS ホスト名 **https** を使用してどこからでも管理パネルにアクセスできるようになります。e.g. `https://xxxxxxx.glddns.com`.ポートフォワーディングを使用する場合は、 `https://xxxxxxx.glddns.com:YourExternalPort`のようにアクセスする必要があります。

この機能は自己署名証明書を使用するため、ブラウザには **接続がプライベートではない**ことが表示されます。Android Chrome で使用する方法を説明します。他のブラウザでも同様のプロセスです。 スマホのWiFi をオフにし、インターネットへのアクセスには 4G のみを使用します。

Chromeを開き、アドレスバーにURLを入力します。例として `https://zw72cd7.glddns.com:8001`を使用します。下にある**Advanced**をクリックしてください。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

 **xxxxxx.glddns.com に処理されました (安全ではありません)** をクリックして続行します。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

次に、Web 管理パネルにアクセスします。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSHリモートアクセス

この機能にはパブリックIPアドレスが必要です。 インターネットプロバイダーからパブリックIPアドレスが割り当てられているかどうかを確認するには、 [こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)を確認してください。

ルーターがNATの後ろにある場合、上位のルーターでポートフォワーディングを設定する必要があるかもしれません。 **22**ポートを使用します。

![SSH-Remote-Access](https://static.gl-inet.com/docs/router/en/4/tutorials/ddns/ssh_remote_access.png){class="glboxshadow"}

上記の手順に従って SSH リモート アクセスを有効にします。そうすれば、どこでもルーターにsshできるようになります。

SSH コマンドは以下のようになります。

`ssh root@xxxxxxx.glddns.com`

または

`ssh root@xxxxxxx.glddns.com:YourExternalPort`

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
