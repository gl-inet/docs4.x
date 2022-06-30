# 動的DNS

ダイナミックドメインネームサービス（Dynamic DNSまたはDDNS）は、ドメイン名をネットワークデバイスの動的なIPアドレスにマッピングするために使用されるサービスです。

ウェブ管理画面の左側 -> APPLICATIONS -> 動的 DNS

![ddns](https://static.gl-inet.com/docs/en/4/tutorials/ddns/ddns.png){class="glboxshadow"}.
　　　　　　　　　　　　　　
## DDNSを有効にする

利用規約とプライバシーポリシーのオプションである、**Enabled DDNS**にチェックを入れ、**Apply**ボタンをクリックします。通常、反映されるまでに数分かかります。

DDNSの更新頻度は、10分に1回です。

![enable ddns](https://static.gl-inet.com/docs/en/4/tutorials/ddns/enable_ddns.png){class="glboxshadow"}.

## DDNSが有効かどうかの確認

==="DDNSテストツールの使用"

   **DDNSテスト**をクリックします。

    ![ddns test](https://static.gl-inet.com/docs/en/4/tutorials/ddns/click_ddns_test.png){class="glboxshadow"} と表示される。

    以下のように、**Your DDNS is resolved as x.x.x.x** と表示されれば、DDNSが動作していることになります。言い換えれば、この**ホスト**名は、インターネットアクセスのためのルータの最終的な出口IPにマップされています。

    ![DDNSが動作した](https://static.gl-inet.com/docs/en/4/tutorials/ddns/ddns_test_resolved.png){class="glboxshadow"}。 
 ==="または手動で確認する"

    以下の2つのIPアドレスが同じかどうかを確認し、Yesの場合はDDNSが有効であり、そうでない場合は無効です。

    * ドメイン名とIPアドレスの対応表を得るには、以下のように `nslookup` コマンドを使用します。zw72cd7.glddns.com` を自分のホスト名に変更する必要があります。8.8.8.8`はGoogle DNSのため、他のDNSに変更することも可能です。

        `nslookup zw72cd7.glddns.com 8.8.8.8` を指定します。

        ![nslookup](https://static.gl-inet.com/docs/en/4/tutorials/ddns/nslookup.png){class="glboxshadow"}となります。

        上記の出力は、Host NameがIPアドレスにマップされたことを意味します。

    * ルーターに接続した電話やパソコンを使うか、Googleで**my ip address**と検索するか、[https://whatismyipaddress.com/](https://whatismyipaddress.com/){target="_blank"}などのサイトにアクセスしてみてください。

## HTTPリモートアクセス

この機能を使用するには、パブリックIPアドレスが必要です。インターネットプロバイダからパブリックIPアドレスが提供されているかどうかは、こちら(../how_to_check_if_isp_assigns_you_a_public_ip_address/)で確認することができます。

ルーターがNATの内側にある場合、上位のルーターでポートフォワーディングを設定する必要があるかもしれません。この場合、**80**番ポートを使用します。

![HTTP-Remote-Access](https://static.gl-inet.com/docs/en/4/tutorials/ddns/http_remote_access.png){class="glboxshadow"}.

上記の手順で、HTTPリモートアクセスを有効にしてください。

***HTTPは暗号化されていませんので、ご自身の責任でご利用ください。

HTTPリモートアクセスを有効にすると、DDNSのホスト名を**http**にすることで、どこでも管理パネルにアクセスできるようになります（例：`http://xxxxxxx.glddns.com`）。ポートフォワーディングを使用している場合は、http://xxxxxxx.glddns.com:YourExternalPort のようにアクセスする必要があります。

## HTTPSリモートアクセス

この機能を利用するには、パブリックIPアドレスが必要です。インターネットプロバイダからパブリックIPアドレスが提供されているかどうかは、こちら(../how_to_check_if_isp_assigns_you_a_public_ip_address/)で確認できます。

ルーターがNATの内側にある場合、上位のルーターでポートフォワーディングを設定する必要がある場合があります。この場合、**443**番ポートを使用します。

![HTTPSリモートアクセス](https://static.gl-inet.com/docs/en/4/tutorials/ddns/https_remote_access.png){class="glboxshadow"}を使用します。

HTTPSリモートアクセスを有効にすると、DDNSのホスト名を**https**にすることで、どこでも管理画面にアクセスできるようになります（例：`https://xxxxxxx.glddns.com`）。ポートフォワーディングを使用している場合は、「https://xxxxxxx.glddns.com:YourExternalPort」のようにアクセスします。

この機能は、自己署名証明書を使用するため、ブラウザは **Your connection is not private** と表示します。とりあえず、Chrome Androidでの使い方を紹介しますが、他のブラウザーも同様の手順です。スマホのWiFiをオフにして、4Gだけでインターネットにアクセスすることにします。

クロームを開き、アドレスバーにURLを入力します。ここでは例として`https://zw72cd7.glddns.com:8001`を使用します。下部の**Advanced**をクリックして続行します。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/en/4/tutorials/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"} をクリックします。

**Processed to xxxxxxx.glddns.com (unsafe)** をクリックし、次に進みます。

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/en/4/tutorials/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"} をクリックし、次へ進みます。

その後、Web Admin Panelにアクセスします。

この時、管理画面には、以下のような画面が表示されます。

## SSHリモートアクセス

この機能を使用するには、パブリックIPアドレスが必要です。インターネットプロバイダからパブリックIPアドレスが提供されているかどうかは、こちら(../how_to_check_if_isp_assigns_you_a_public_ip_address/)で確認することができます。

ルーターがNATの内側にある場合、上位のルーターでポートフォワーディングを設定する必要があるかもしれません。この場合、**22**番ポートを使用します。

![SSH-Remote-Access](https://static.gl-inet.com/docs/en/4/tutorials/ddns/ssh_remote_access.png){class="glboxshadow"}.

上記の手順で、SSHリモートアクセスを有効にすると、どこからでもルーターにsshでアクセスできるようになります。

SSHコマンドは以下のようになります。

`ssh root@xxxxxxx.glddns.com`

または 

`ssh root@xxxxxxx.glddns.com:YourExternalPort`
