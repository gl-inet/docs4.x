# GL.iNetルーターにWireGuard Serverをセットアップする。

WireGuard®は、非常にシンプルでありながら高速な最新のVPNで、以下のような特徴を備えています。 **最先端暗号技術**.   [faster](https://www.wireguard.com/performance/){target="_blank"}を目指しています , [simpler](https://www.wireguard.com/quickstart/){target="_blank"}, IPSecよりも無駄がなく、便利でありながら、膨大な頭痛の種を回避することができます。OpenVPNよりもかなり高性能になる予定です。

GL.iNetルーターには、WireGuardサーバーとクライアントがプリインストールされています。
---

## インターネットサービスプロバイダからパブリックIPアドレスが割り当てられていることを確認してください

インターネットサービスプロバイダからパブリックIPアドレスが割り当てられているかどうかご確認ください。 [here](../how_to_check_if_isp_assigns_you_a_public_ip_address).

**「いいえ」の場合、WireGaurd Serverへの接続ができません。**

別の方法として、リバース・プロキシ・ソリューションを使用することもできます。　 [AstroRelay](https://www.astrorelay.com/){target="_blank"}お勧めします

## ネットワークトポロジー

* GL.iNetルーターがネットワークのメインルーターである場合は、簡単ですので、次のステップに進んでください。
* すでにメインルーターがあり、GL.iNetルーターがメインルーターの下にある場合、メインルーターにポートフォワーディングの設定が必要な場合があります。
* すでにメインルーターがある場合、GL.iNetルーターはその数段下にあるため、それぞれのレベルでポートフォワードの設定をする必要があります。

## WireGuardサーバーのセットアップ

左側にあるWeb Admin Panelにアクセスします。 -> VPN -> WireGuard Server.

1. **Generate Configuration** をクリックします（初回のみ）。

    ![wireguard server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_generate_configuration.png){class="glboxshadow"}

2. Apply the configuration

    The default configuration works for most cases. Also modify it according to your network situation, click the **Apply** button after modification.

    ![wireguard server apply configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_apply_configuration.png){class="glboxshadow"}

    For **Set Key Manually**.

    ![wireguard server set key manually](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_set_key_manually.png){class="glboxshadow"}

3. Add a profile

    Switch to **Profiles** tab, generate a profile for your device by click the **Add** button.

    ![wireguard server profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profiles.png){class="glboxshadow"}

    Enter a descriptive name.

    ![wireguard server profile setting](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profile_setting.png){class="glboxshadow"}
    
    **Set More** is for advanced settings.

    ![wireguard server profile advanced setting](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wireguard_server_profile_setting_more.png){class="glboxshadow"}

    Click **Apply** to continue. It will generate a profile.
    
    ![download wireguard client configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_wireguard_client_configuration.png){class="glboxshadow"}

    If your network's public IP changes from time to time, you can enable [DDNS](../ddns/), then using DDNS domain in the configuration.

    Click **Download** to save the profile.

4. Start WireGuard server

    Click the **Start** button in the upper right corner to start WireGuard server. Go to VPN Dashboard page to check its status and other settings.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wireguard_server.png){class="glboxshadow"}

### To check if WireGuard Server is working properly

To check if WireGaurd Server is working properly, we can use another device connected to another network and use the WireGuard configuration we exported earlier to connect and see whether it connects properly and whether the IP address is the IP of WireGuard Server.

The simpliest way is to use a cell phone with [WireGuard official client app](https://www.wireguard.com/install){target="_blank"} installed, turn off its Wi-Fi connection, and only connect to Internet via 3G/4G/5G. Then open the WireGaurd app, import the WireGaurd configuration from QR code. Enable the connection, check if the phone has Internet access and whether its IP address is the IP of your WireGuard Server.

There are several common reasons cause failed:

* The Internet Service Provider doesn't assign you a public IP address, please check [here](#make-sure-internet-service-provider-assigns-you-a-public-ip-address).
* You may need setup port forwarding, please check [here](#network-topology).
* The port you are using for WireGuard Server is blocked by the Internet Service Provider, change to another port, or contact the Internet Service Provider.
* Some countries/regions may block the VPN connection.

## WireGuard Client App

We can use another GL.iNet router as WireGuard Client, or use their official app on other devices with various OS.

- Please refer to WireGuard Official Website: [https://www.wireguard.com/install](https://www.wireguard.com/install){target="_blank"}