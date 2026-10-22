# DDNSテストでメッセージが表示されるのはなぜですか？ {#why-do-i-get-a-message-from-ddns-test}

ダイナミックDNSページでDDNSテストを実行すると、以下のメッセージが表示される場合があります。

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**（DDNSドメインの名前解決で得られたIPアドレスが、デバイスのWAN IPと一致しません。）

**"You need an Internet Public IP address to use Dynamic DNS."**（ダイナミックDNSを使用するには、インターネットのパブリックIPアドレスが必要です。）

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

これは**警告**（Warning）や**エラー**（Error）のメッセージではなく、ルーターのネットワーク状態を知らせるための通知です。

この結果は通常、ネットワーク内でのルーターの位置を反映しています。例えば、GL.iNetルーターがホームネットワークでセカンダリールーターとして設定されている場合、このメッセージが表示されます。

このメッセージは、プライマリールーターでポートフォワーディングを設定しても消えません。これは単に、ルーターがNATの内側にあることを示しています。

NATを越えてサービスを公開する必要がある場合（リモートアクセスなど）は、追加の設定が必要です。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
