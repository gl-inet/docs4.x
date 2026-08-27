# GL.iNetルーターでSurfsharkのDedicated IPに接続する方法

この記事では、GL.iNet ルーターで Surfshark の Dedicated IP 接続を設定する手順を紹介します。

ここでは GL-AXT1800 を例に説明します。

1. Surfshark アカウントにログインし、**Dedicated IP** を選択します。

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/manualdip.jpg){class="glboxshadow"}

2. Dedicated IP セクションで **Settings** をクリックします。

    ![setting](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/setting.jpg){class="glboxshadow"}

3. プロトコル（WireGuard または OpenVPN）を選択し、手動接続用の設定ファイルをダウンロードします。

    ![protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/protocol.jpg){class="glboxshadow"}

    WireGuard 設定では、ダウンロードページに Server IP と Server Public Key が表示されます。以下を参照してください。

    ![loadwg](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/loadwg.jpg){class="glboxshadow"}

    OpenVPN 設定では、ダウンロードページに Server IP と認証情報（Username & Password）が表示されます。以下を参照し、後で使うために認証情報をコピーしてください。

    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/loadovpn.jpg){class="glboxshadow"}

4. 以下のリンクを参照して、設定ファイルを GL.iNet ルーターにアップロードします。必要に応じて認証情報を入力してください。

    - [WireGuard設定をアップロードする](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [OpenVPN設定をアップロードする](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
