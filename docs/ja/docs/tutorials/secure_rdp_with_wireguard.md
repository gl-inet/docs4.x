# WireGuardで外部ネットワークからのRDPを保護する {#securing-rdp-from-an-external-network-with-wireguard}

外部ネットワークからPCへリモートアクセスしたい場合や、その逆を行いたい場合があります。最も安全な方法は、自分専用のWireGuardトンネルを使うことです。ポートフォワーディングを使ってパブリックIPアドレス経由でPCへ直接アクセスするよりも安全性が高くなります。トンネルを設定すれば、**Windows Remote Desktop** を使って、どこからでもPCにアクセスできます。

このチュートリアルでは、2台のGL.iNetルーターを例に、WireGuardネットワークでWindows RDPを保護する方法を説明します。

## トポロジー {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## 設定手順 {#setup-steps}

1. WireGuardネットワークを構築します。

    まず、2台のGL.iNetルーターでWireGuardサーバーとWireGuardクライアントを設定します。[2台のGL.iNetルーターでWireGuardサーバーを構築する方法](build_your_own_wireguard_home_server_with_two_glinet_routers.md)を参照してください。

2. WireGuardサーバーからクライアントLANへのアクセスを許可します。

    サーバーとクライアント間で双方向アクセスを可能にするには、まずサーバーからクライアントLANへのアクセスを許可します。[サーバーからWireGuardクライアントLANにアクセスする方法](wireguard_server_access_to_client_lan_side.md)を参照してください。

    手順はファームウェアのバージョンによって異なる場合があります。

3. WireGuardクライアントからサーバーLANへのアクセスを許可します。

    この手順はファームウェアのバージョンによって異なる場合があります。WireGuardクライアントとして設定したルーターのファームウェアバージョンを以下から選択してください。

    ??? note "ファームウェアv4.7以前の場合"

        WireGuardクライアントにログインし、**VPN** -> **VPN Dashboard** に移動します。**VPN Server** を探し、右側の歯車アイコンをクリックします。

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        ポップアップウィンドウで **Remote Access LAN** を有効にし、**Apply** をクリックします。

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "ファームウェアv4.8以降の場合"

        WireGuardクライアントにログインし、**VPN** -> **WireGuard Server** に移動します。右上の **Options** をクリックします。

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        ポップアップウィンドウで **Allow Remote Access to the LAN Subnet** を有効にし、**Apply** をクリックします。

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. アクセス先のコンピューターをVPNサーバーに接続し、そのLAN IPアドレスを確認します。

    以下の例では、サーバー側PCのIPアドレスは **192.168.29.123** です。

5. サーバー側PCにアクセスできるように設定します。

    サーバー側PCで **System Settings** を開き、**Remote Desktop** をクリックします。

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    **Remote Desktop** を有効にし、**Confirm** をクリックします。

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. クライアント側ノートPCからリモートアクセスします。

    検索バーで **Remote Desktop Connection** を検索します。

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    アプリを起動し、サーバー側PCのIPアドレス（例：**192.168.29.123**）を入力します。

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    サーバー側PCの認証情報を入力して接続します。

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    これでサーバー側PCをリモート操作できるようになります。

    逆方向に行いたい場合は、サーバー側PCとクライアント側ノートPCの手順を入れ替えてください。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
