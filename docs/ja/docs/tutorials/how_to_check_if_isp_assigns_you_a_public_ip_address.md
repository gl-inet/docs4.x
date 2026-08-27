# パブリック IP アドレスを持っているか確認する方法

パブリック IP アドレスは、プライベート IP アドレスとは異なり、インターネットに接続されたデバイスに割り当てられる一意の数値識別子です。Web サイトを公開したり、VPN サーバーを設定したり、各種オンラインサービスを提供したりするには、パブリック IP アドレスが必要です。通常はインターネットサービスプロバイダーがこれを提供します。

自分がパブリック IP アドレスを持っているかどうかわからない場合は、以下のいずれかの方法で確認してください。

**方法 1: インターネットサービスプロバイダーに直接問い合わせる**

**方法 2: ルーターの管理画面とインターネット上で IP アドレスを確認する**

1. ルーターの管理画面にログインします。
    * GL.iNet ルーターの場合は、Web ブラウザで `192.168.8.1` を開いてサインインします。
    * 構成内に複数のルーターがある場合は、メインルーターの管理画面にログインします。
2. ルーターの管理画面で WAN IP アドレスを確認します（例: `42.XXX.XX.`）。
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. Web ブラウザで `what is my ip` を検索します。
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

2 つの IP アドレスが一致していれば、パブリック IP アドレスを持っています。
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

パブリック IP アドレスを持っていない場合は、イントラネット貫通ツールの利用を検討してください。パブリック IP アドレスがなくても、Web サイト、VPN サーバー、各種サービスをインターネット上から利用できるようになります。

---

関連記事

- [GL.iNet ルーターで WireGuard サーバーを設定する](../interface_guide/wireguard_server.md)
- [GL.iNet ルーターで OpenVPN サーバーを設定する](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

まだご不明な点がありますか？ [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
