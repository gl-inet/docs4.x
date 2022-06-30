# GL.iNetルータにOpenVPNサーバをセットアップする。

OpenVPNは、仮想プライベートネットワーク（VPN）技術を利用して、サイト間またはポイント・ツー・ポイント接続を安全に確立するオープンソースのVPNプロトコルです。

GL.iNetのルーターには、OpenVPNクライアントとサーバーがプリインストールされています。

OpenVPNよりもWireGuardの方が高速に接続できるため、WireGuardをお勧めします。WireGuardサーバーのセットアップについては、以下を参照してください。 [here](../wireguard_server).

---

## インターネットサービスプロバイダからパブリックIPアドレスが割り当てられていることを確認する

インターネットサービスプロバイダからパブリックIPアドレスが割り当てられているかどうかご確認ください。 [here](../how_to_check_if_isp_assigns_you_a_public_ip_address).

**できない場合、OpenVPN Server に接続できません。**

別の方法として、リバース・プロキシ・ソリューションを使用することもできます。　 [AstroRelay](https://www.astrorelay.com/){target="_blank"}.お勧めします

## ネットワークトポロジー

* GL.iNetルーターがネットワークのメインルーターである場合、これは簡単です、 [next step](#setup-openvpn-server)に移動してください。.
* すでにメインルーターがあり、GL.iNetルーターがメインルーターの下にある場合、メインルーターにポートフォワーディングの設定が必要な場合があります。
* すでにメインルーターがある場合、GL.iNetルーターはその数段下にあるため、それぞれのレベルでポートフォワーディングを設定する必要があります。

## OpenVPNサーバーのセットアップ

1.　**Generate Configuration**をクリックしてください (初回のみ）

    ![openvpn server generate configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_generate_config.png){class="glboxshadow"}

2. コンフィギュレーションを適用します。

    ![openvpn server configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_configuration.png){class="glboxshadow"}

    設定を変更する必要がない場合は、 ページ下部の**Export Client Configuration**を直接クリックしてください。 設定を変更した場合は、 **Apply** ボタンをクリックして続行してください。

    * **Protocol:** UDP or TCP. To find out what the difference is, check out [this tutorial](../openvpn_tcp_udp/).

    * **Authentication Mode:** There are three options **Only Certificate**, **Only Username/Password**, **Username/Password and Certificate**. 
    
        For **Username/Password** and **Username/Password and Certificate** options, they need add user(s). Then, if a OpenVPN client connect to this server, it need to input the username and password.

        ![openvpn server users](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_users.png){class="glboxshadow"}

        Created a user.

        ![openvpn server add a user](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_add_a_user.png){class="glboxshadow"}

        For **Only Certificate** and **Username/Password and Certificate**, the router will automatically generate a server and client certificate-key, and write into the configuration file when generating the client configuration file.

        Please check [here](#advanced-configuration) for **Advanced Configuration**.

3. Export Client Configuration

    Clicking the **Export Client Configuration** button at the bottom or applying the modified configuration will pop up this dialog.

    If your network's public IP changes from time to time, you can enable [DDNS](../ddns/) by using DDNS domain in the configuration. Click **Download** to export the configuration for further setup.

    ![openvpn server configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_export_client_configuration.png){class="glboxshadow"}

4. Start OpenVPN server

    Click the **Start** button in the upper right corner on OpenVPN Server page to start the server. Then go to [VPN Dashboard page](../vpn_dashboard#vpn-server) to check its status and other settings.

    ![start openvpn server](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/start_openvpn_server.png){class="glboxshadow"}

## To check if OpenVPN Server is working properly

To check if OpenVPN Server is working properly, we can use another device connected to another network and use the OpenVPN configuration we exported earlier, to connect and see whether it connects properly and whether the IP address is the IP of OpenVPN Server.

The simpliest way is to use a cell phone with [OpenVPN official client app](https://openvpn.net/vpn-client/){target="_blank"} installed, turn off its Wi-Fi connection, and only connect to Internet via 3G/4G/5G. Then open the OpenVPN app, import the OpenVPN configuration we previously exported. Enable the connection, check if the phone has Internet access and whether its IP address is the IP of your OpenVPN Server.

When importing the configuration file to the OpenVPN app, it may has a reminder as below, please click **CONTINUE** as the certificate is already included in the configuration file.

![openvpn app select certificate](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow"}

There are several common reasons cause failed:

* The Internet Service Provider doesn't assign you a public IP address, please check [here](#make-sure-internet-service-provider-assigns-you-a-public-ip-address).
* You may need setup port forwarding, please check [here](#network-topology).
* The port you are using for OpenVPN Server is blocked by the Internet Service Provider, change to another port, or contact the Internet Service Provider.
* Some countries/regions may block the VPN connection.

## Advanced Configuration

![openvpn server advancd configuration](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_server/openvpn_server_advanced_configuration.png){class="glboxshadow"}

## OpenVPN Client App

We can use another GL.iNet router as OpenVPN Client, or use their official app on other devices with various OS.

- Please refer to OpenVPN Official Website: [https://openvpn.net/vpn-client/](https://openvpn.net/vpn-client/){target="_blank"}