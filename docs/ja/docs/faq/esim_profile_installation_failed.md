# eSIMプロファイルのインストールに失敗した場合はどうすればよいですか？

GL.iNet ルーターで eSIM プロファイルを追加しようとしてインストールに失敗した場合は、以下のトラブルシューティング手順を確認してください。

1. ルーターがインターネットに接続されていることを確認します。

    ルーターが正常にインターネットへ接続されていることを確認してください。ネットワークが不安定だと、eSIM プロファイルのアップロードに影響し、取得やインストールに失敗する場合があります。

    可能であれば、スマートフォンのホットスポットや公衆 Wi-Fi など別のネットワークにルーターを接続し、その後もう一度 eSIM プロファイルをアップロードして試してください。

2. DNS 設定を変更します。

    インターネットが正常に動作している場合は、ルーターの Web 管理パネルにログインし、**NETWORK** -> **DNS** に移動します。

    DNS Mode を **Manual DNS** に切り替え、Google DNS (`8.8.8.8`, `8.8.4.4`) や Cloudflare DNS (`1.1.1.1`, `1.0.0.1`) など、別のパブリック DNS サーバーを設定して試してください。

    **Apply** をクリックして変更を保存し、その後もう一度 eSIM プロファイルをアップロードしてください。

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. AdGuard Home を無効にします。

    ルーターで AdGuard Home が利用可能かつ有効になっている場合は、無効にしてから eSIM プロファイルのインストールを再度試してください。

4. eSIM プロファイルが利用可能か確認します。

    この eSIM プロファイルまたは QR コードが、すでに別のデバイスで有効化またはインストールされていないか確認してください。

    ほとんどの eSIM プロファイルは 1 回しかインストールできず、複数デバイスで有効化できません。可能であれば、現在の eSIM プロファイルがまだ利用可能か、eSIM サービスプロバイダーに確認してください。eSIM の QR コードまたはアクティベーションコードが期限切れの場合は、新しいものを再発行してもらってから、もう一度アップロードしてください。

5. アクティベーションコードを確認します。

    正しい形式の QR コードでは、**LPA:** で始まるアクティベーションコードが表示されます。ただし、標準外の QR コードでは LPA プレフィックスなしの生のコードしか表示されない場合があります。その場合は、**Install** をクリックする前に、コードの先頭へ手動で `LPA:` を追加してください。

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. 確認コードが必要かどうか確認します。

    Smarty eSIM など、一部の eSIM プロファイルではインストール中に確認コードの入力が必要です。eSIM パッケージまたはインストールガイドを確認し、確認コードが必要かどうかを確認してください。必要な場合は、正しいコードを入力してください。

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. 上記の手順で解決しない場合は、**eSIM Management** ページから eSIM ログをエクスポートしてください。

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    その後、以下の重要情報とあわせて [support@gl-inet.com](mailto:support@gl-inet.com) へ送信し、追加サポートを依頼してください。

    - 発生している問題
    - すでに試したトラブルシューティング方法
    - ご利用の eSIM プロバイダー

---
