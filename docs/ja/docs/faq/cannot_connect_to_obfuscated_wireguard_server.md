# 難読化された WireGuard サーバーに接続できない

VPN 難読化は、VPN トラフィックを通常のインターネットトラフィックのように見せる技術です。現在、一部の GL.iNet ルーターは AmneziaWG プロトコルに対応しており、トラフィック難読化を有効にした WireGuard サーバーを設定できます。

難読化された WireGuard サーバーへ接続できない場合は、以下の手順でトラブルシューティングしてください。

1. **各クライアントにインポートした WireGuard 設定が専用のものであることを確認します。**

    各クライアントには専用の peer 設定ファイルが必要です。複数のクライアントで同じ設定を共有すると、接続に失敗します。

    必要に応じて、**VPN** -> **WireGuard Server** -> **Profiles** に移動し、エクスポート済みプロファイルを確認します。

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **難読化パラメーターをクライアントが検証できることを確認します。**

    AmneziaWG プロトコルには下位互換性があります。WireGuard サーバーが AmneziaWG v1.0 のみをサポートしている場合でも、v2.0 をサポートするクライアントに設定ファイルをインポートすると検証に通ります。
        
    ただし、設定ファイルに AmneziaWG v2.0 の難読化パラメーターが含まれている場合は、WireGuard クライアントが AmneziaWG v2.0 をサポートしていることを確認してください。サポートしていない場合、パラメーター検証に失敗することがあります。

    !!! tip "AmneziaWG のバージョンを確認する方法"

        **V1.0**: S3-S4 パラメーターがなく、H1-H4 は単一の固定整数です。
        
        **V2.0**: 次のいずれかの条件を満たす場合は V2.0 です。
        
        - S3-S4 パラメーターを含む
        - H1-H4 が数値範囲として設定されている
        - カスタム I1-I5 パラメーターを含む。
        
        > 注意: I1-I5 は自動生成されません。ユーザーは設定ファイルに追加行として手動で記述し、AmneziaWG のトラフィックを QUIC や WebRTC などの一般的なプロトコルのように見せることができます。

    WireGuard クライアントが GL.iNet ルーターの場合は、以下の 2 つの方法で AmneziaWG バージョンを確認します。

    ??? note "Router Web Admin Panel で確認する"

        1. ルーターの Web Admin Panel にログインします。

        2. **VPN** -> **WireGuard Server** -> **Configuration** に移動し、難読化パラメータを確認します。設定に **S3-S4** と **H1-H4** が固定値ではなく可変範囲として含まれている場合、下図のようにルーターは AmneziaWG 2.0 を実行しています。

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            それ以外の場合は、下図のように AmneziaWG 1.0 を使用しています。

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "SSH コマンドで確認する"

        1. SSH でルーターにログインします。

        2. `opkg list|grep awg` を実行し、出力内の **kmod-amneziawg** パッケージのサフィックスを確認します。**2.0** と表示されている場合、下図のようにルーターは AmneziaWG 2.0 に対応しています。

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            それ以外の場合は、下図のように AmneziaWG 1.0 を実行しています。

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **難読化パラメータを調整します。**

    WireGuard サーバーで Jc、Jmin、Jmax などの [難読化パラメータ](amneziawg_obfuscation.md#parameter-overview) を手動設定している場合、誤った設定により handshake が失敗することがあります。

    これらの難読化パラメータを変更して再接続し、パラメータ不一致の問題を切り分けてください。テストのために、難読化設定をデフォルト値に戻すこともできます。

4. **公式 AmneziaWG App で接続をテストします。**

    比較テストを行います。公式 AmneziaWG App をインストールし、サーバーからエクスポートした元の設定ファイルをアプリにインポートして、接続を試します。

    - 公式アプリで接続できる場合、設定ファイルは有効です。問題は元のクライアントデバイス側にある可能性があります。ネットワーク接続を確認するか、サポートへお問い合わせください。

    - それでも接続できない場合、問題はルーター側のサーバー設定にあります。サーバー設定と難読化パラメータを確認してください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} までご連絡ください。
