# パブリックIPアドレスを持っているか確認する方法

パブリックアドレスは、プライベート IP アドレスとは異なり、インターネットに接続された機器に割り当てられる一意の数値識別子です。Web サイトの公開、VPN サーバーの構築、各種オンラインサービスの提供には、パブリック IP アドレスが必要になります。通常はインターネットサービスプロバイダーが提供します。

自分がパブリック IP アドレスを持っているか分からない場合は、以下のいずれかの方法で確認できます。

**方法1: インターネットサービスプロバイダーへ直接問い合わせる**

**方法2: ルーター管理パネルとインターネット上で IP アドレスを確認する**

1. ルーターの管理パネルにログインします。
   - GL.iNet ルーターの場合は、ブラウザで `192.168.8.1` を開いてログインします。
   - 構成内に複数のルーターがある場合は、メインルーターの管理パネルにログインしてください。

2. ルーター管理パネルで WAN IP アドレスを確認します（例: `42.XXX.XX.`）。

![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}

3. ブラウザで `what is my ip` と検索します。

![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

2 つの IP アドレスが一致していれば、パブリック IP アドレスを持っています。

![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

パブリック IP アドレスを持っていない場合は、イントラネット貫通ツールの利用を検討してください。パブリック IP アドレスがなくても、Web サイト、VPN サーバー、各種サービスをインターネット上から利用可能にできます。

---

関連記事

- [GL.iNetルーターでWireGuardサーバーを設定する](../interface_guide/wireguard_server.md)
- [GL.iNetルーターでOpenVPNサーバーを設定する](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
