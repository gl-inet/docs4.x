# パブリックIPアドレスを持っているか確認する方法

パブリックアドレスは、プライベートIPアドレスとは異なり、インターネットに接続されたデバイスに割り当てられる一意の数値識別子です。ウェブサイトをホストしたり、VPNサーバーを設定したり、オンラインサービスを提供したりする場合は、パブリックIPアドレスが必要です。通常、インターネットサービスプロバイダーが提供します。

パブリックIPアドレスを持っているかどうか確かでない場合は、以下の方法で確認できます。

**方法1: インターネットサービスプロバイダーに直接問い合わせる**

**方法2: ルーター管理パネルとインターネットでIPアドレスを確認する**

1. ルーターの管理パネルにサインインします。
    * GL.iNetルーターの場合、ウェブブラウザに「192.168.8.1」と入力してサインインします。
    * セットアップに複数のルーターがある場合は、プライマリールーターの管理パネルにサインインします。
2. ルーター管理パネルでIPアドレスを確認します（例：42.XXX.XX.）
![IPアドレスを確認](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. ウェブブラウザで「私のIPは何ですか？」と検索します。
![私のIPは何ですか？](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

もし二つのIPアドレスが一致すれば、パブリックIPアドレスを持っています。
![二つのIPアドレスが一致](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

もしパブリックIPアドレスを持っていない場合は、イントラネットペネトレーションツールを使用することを検討できます。これにより、パブリックIPアドレスがなくても、ウェブサイト、VPNサーバー、サービスをインターネット上でアクセス可能にすることができます。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com)をご覧ください。