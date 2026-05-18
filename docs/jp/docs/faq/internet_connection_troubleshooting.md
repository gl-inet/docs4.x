# インターネット接続のトラブルシューティングFAQ

## Q1. インターネットに接続できない場合はどうすればよいですか？

基本的なトラブルシューティングとして、以下の手順をお試しください。

1. 物理接続を確認します。

    ルーターの WAN ポートと上位側デバイス（モデム、ONT、Ethernet ジャックなど）の間で、Ethernet ケーブルがしっかり接続されていることを確認してください。上位側デバイスのLEDも確認し、通信が行われていることを確認します。

2. デバイスを再起動します。

    上位側デバイス（モデムなど）とルーターの電源を切ります。1〜2分待ってから、先にモデムの電源を入れ、完全にオンラインになったことを確認してからルーターの電源を入れてください。

3. WAN IPアドレスを確認します。

    ルーターの Web 管理パネルにログインし、**INTERNET** -> **Ethernet** セクションに移動します。下図のように接続中のまま止まっている場合は、DHCP の問題、MAC バインディング、または VLAN ID の設定が必要な可能性があります。

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    ISP に連絡し、インターネット接続に **PPPoE username**、**PPPoE password**、**VLAN ID** が必要か確認してください。

    あわせて、ISP が以前にモデム / ONT に **MAC binding** を設定していないかも確認してください。

## Q2. MACアドレスをクローンするのはどのような場合ですか？

一部の ISP では、回線接続を最初に接続したデバイス（通常は以前使っていたルーターまたはPC）の MAC アドレスに紐付けています。ルーターを交換した場合、インターネット接続を復旧するには MAC アドレスのクローンが必要になります。

GL.iNet ルーターに MAC アドレスをクローンする手順は以下のとおりです。

1. 以前使っていたルーター（または回線に紐付けられていたPC）の MAC アドレスを控えます。

2. ルーターの Web 管理パネルにログインし、**NETWORK** -> **Ethernet Port**（一部のファームウェアでは **Port Management**）に移動します。**MAC Mode** を **Clone** または **Manual** に設定し、MAC アドレスを手動で入力して **Apply** をクリックします。

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. モデム（上位側デバイス）を再起動します。

## Q3. VLAN ID の設定が必要なのはどのような場合ですか？

一部の ISP では、特に光回線や IPTV 接続で、インターネット認証やトラフィック分離のために VLAN タグが必要です。VLAN ID が必要かどうかは ISP に確認してください。

VLAN ID を設定する手順は以下のとおりです。

1. ルーターにログインし、**INTERNET** -> **Ethernet** セクションに移動して **Modify** をクリックします。

2. ISP から提供された VLAN ID を入力し、**Apply** をクリックします。

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## Q4. それでも動作しない場合はどうすればよいですか？

問題が解決しない場合は、PC またはノートPC をモデムに直接接続し、インターネットへアクセスできるか確認してください。

インターネットへアクセスできない場合は、問題が ISP 側にある可能性があります。詳細は ISP にお問い合わせください。

インターネットへアクセスできる場合は、ルーターの設定に問題がある可能性があります。[support@gl-inet.com](mailto:support@gl-inet.com) まで以下の情報を添えて技術サポートへご連絡ください。

- ルーターモデル
- すでに試したトラブルシューティング手順
- ご利用の ISP 名
- そのほか、問題解決に役立つと思われる情報

## ISP information

以下は、GL.iNet がお客様からのフィードバック、フォーラム、OpenWRT の情報をもとにまとめた地域別 ISP 情報です。参考情報としてご利用ください。

| Country/Region   | ISP   | Connection Type | VLAN ID | MAC Clone Required | Additional Requirements |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| United States    | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | Must enable IP Passthrough; EAP authentication bypass needed |
| United States | Spectrum | DHCP | N/A | Yes (in some areas) | Strong MAC binding (modem reboot required) |
| United States | Verizon Fios | DHCP | N/A | No | |
| United States | Comcast Xfinity | DHCP | N/A | Yes (common) | Must reboot modem when changing router (MAC release) |
| United States | Cox Communications | DHCP | N/A | Yes | Must reboot modem when changing router (MAC release) |
| United States | Frontier Fiber | DHCP | N/A | No | |
| United States | CenturyLink / Lumen | PPPoE | 201 | No | VLANs are required in certain areas. |
| Canada | Bell Canada Fibe | PPPoE | 35 | No | |
| Germany | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 mandatory for internet; PPPoE credentials required |
| Germany | Vodafone (Kabel) | DHCP | N/A | Yes (sometimes) | MAC binding may apply; reboot modem after router change |
| Germany | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 mandatory for internet |
| Germany | DNS:NET | PPPoE | 37 | No | |
| Germany | o2(UGG) | PPPoE | 7 | No | |
| United Kingdom | BT Broadband | PPPoE | 101 | No | VLAN 101 required; PPPoE login needed |
| United Kingdom | Sky Broadband | DHCP (Option 61) | 101 | No | Requires DHCP Option 61 (client identifier) |
| United Kingdom | Virgin | DHCP | N/A | Yes | The modem is in bridged mode and requires MAC cloning. |
| France | Orange | DHCP / PPPoE | 832 | No | VLAN 832 required; may require Option 90 authentication |
| France | Free (Freebox) | DHCP | N/A | No | |
| France | Bouygues Telecom | DHCP | 100 | Yes | Clone Bbox MAC |
| Spain | Movistar | PPPoE | 6 | No | VLAN 6 (internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spain | DIGI | PPPoE | 20 | No | |
| Spain | Orange | DHCP | 832/835 | No | VLANs may vary by region |
| Italy | TIM | PPPoE | 835 | No | VLAN 835 required |
| Italy | Aruba | PPPoE | 835 | No | |
| Netherlands | KPN | DHCP | 6 | No | VLAN 6 required for internet |
| Netherlands | Tweak | DHCP | 34 | Yes | Cloning Experia Box MAC |
| Netherlands | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Netherlands | Odido | DHCP | 300 | No | |
| Belgium | EDPnet | PPPoE | 10 | No | |
| Bosnia and Herzegovina | BH Telecom | PPPoE | 100 | No | |
| Croatia | Terrakom | PPPoE | 905 | No | |
| Czech Republic | O2 | PPPoE | 848 | No | |
| Cyprus | Epic | PPPoE | 35 | No | |
| Cyprus | Cyta | PPPoE | 42 | No | |
| Cyprus | Cablenet | PPPoE | 42 | No | |
| Cyprus | Primetel | PPPoE | 42 | No | |
| Poland | Orange Polska | PPPoE | 35 | No | VLAN 35 required |
| Poland | T-mobile | PPPoE | 35 | No | |
| Ireland | Vodafone SIRO | PPPoE | 10 | No | |
| Ireland | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Türkiye | Turknet | PPPoE | 35 | No | |
| Türkiye | Turk Telekom | PPPoE | 35 | No | |
| Türkiye | Turkcell Superonline | PPPoE | N/A | Yes | |
| Türkiye | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Greece | Cosmote | PPPoE | 835 | No | |
| Greece | Nova | PPPoE | 835 | Yes | |
| Greece | DEI/PPC | DHCP | 835 | No | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE requires MAP-E/DS-Lite compatible router |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | No | BBIX IPoE service commonly used |
| India | Airtel | PPPoE / DHCP | N/A | No | Some regions require PPPoE |
| India | JioFiber | DHCP | N/A | No | Locked ONT in many cases |
| Singapore | Singtel | PPPoE | 10 | No | VLAN 10 required; IPTV separate VLAN |
| Singapore | StarHub | DHCP | N/A | No | DHCP-based connection |
| Australia | NBN (various ISPs) | PPPoE / DHCP | 2 (common) | Yes | VLAN 2 common but ISP-dependent |
