# GL.iNetルーターでSurfsharkのDedicated IPに接続する方法

この記事では、Surfshark の Dedicated IP を設定する手順を説明します。

ここでは GL-AXT1800 を例にしています。

1. Surfshark アカウントにログインし、**Dedicated IP** を選択します。

   ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){calss="glboxshadow"}

2. Dedicated IP セクションで **Settings** をクリックします。

   ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){calss="glboxshadow"}

3. **Select a protocol (WireGuard or OpenVPN) and download** をクリックし、手動接続用の設定ファイルをダウンロードします。

   ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){calss="glboxshadow"}

   WireGuard を選んだ場合のダウンロードページは次のとおりです。

   ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){calss="glboxshadow"}

   OpenVPN を選んだ場合のダウンロードページは次のとおりです。

   ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){calss="glboxshadow"}

   後で使うために **credentials** をコピーしておいてください。

4. 以下のリンクを参照して、設定ファイルを GL.iNet ルーターにアップロードします。

   必要に応じて credentials を入力してください。
   - [WireGuard設定をアップロードする](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/#set-up-other-providersvia-configuration-files)

   - [OpenVPN設定をアップロードする](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/#set-up-openvpn-client)

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
