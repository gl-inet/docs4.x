# GL.iNetルー器でSurfsharkのDedicated IPに接続する方法

このでは、SurfsharkのDedicated IPを設定する手順を紹介します。

ここではGL-AXT1800を例にとって説明します。

1. Surfsharkアカウントにログインし、**Dedicated IP**を選択します。

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){calss="glboxshadow"}

2. Dedicated IPセクションで、**Settings**をクリックします。

    ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){calss="glboxshadow"}

3. **プロトコル（WireGuardまたはOpenVPN）を選択してダウンロード**し、手動接続用の設定ファイルをダウンロードします。

    ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){calss="glboxshadow"}
    
    WireGuard設定の場合、ダウンロードページは下図のようにの通りです。
    
    ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){calss="glboxshadow"}

    OpenVPN設定の場合、ダウンロードページは下図のようにの通りです。
    
    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){calss="glboxshadow"}

    後で使用するために**認証情報**をコピーします。

4. で下のリンクを参照して、設定ファイルをGL.iNetルー器にアップロードします。

    必要な場合は認証情報を入力します。

    - [Wireguard設定をアップロード](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/#set-up-other-providersvia-configuration-files)

    - [OpenVPN設定をアップロード](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/#set-up-openvpn-client)

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
