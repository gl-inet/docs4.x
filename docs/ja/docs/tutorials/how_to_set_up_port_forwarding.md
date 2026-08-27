# メインルーターでポートフォワーディングを設定する方法

GL.iNetルーターでサーバー（たとえば [OpenVPNサーバー](how_to_set_up_openvpn_server.md) や [WireGuardサーバー](build_your_own_wireguard_home_server_with_two_glinet_routers.md)）を設定しており、そのルーターがメインルーターに接続されている場合は、メインルーターでポートフォワーディングを設定する必要があります。これにより、サーバーに正しくアクセスできるようになります。

メインルーターとGL.iNetルーターの間に他のルーターがある場合は、それらすべての上流ルーターでもポートフォワーディングを設定する必要があります。

## 準備

ポートフォワーディングを設定する前に、メインルーターでGL.iNetルーターの**固定IPアドレス予約**を行うことを推奨します。これにより、GL.iNetルーターには常に固定のIPアドレスが割り当てられます。

そうしないと、メインルーターまたはGL.iNetルーターの再起動時に、メインルーターがGL.iNetルーターへ新しいIPアドレスを割り当て、ポートフォワーディングのルールが機能しなくなる可能性があります。

次に、GL.iNetルーター向けにメインルーターでポートフォワーディングを設定してください。

ポートフォワーディングの設定手順は、ルーターのブランドやモデルによって異なります。以下の該当セクションを参照してください。

## GL.iNetルーターをメインルーターとして使用する場合

[こちらのリンク](../interface_guide/port_forwarding.md){target="_blank"}を参照してください。

## 他社製ルーターをメインルーターとして使用する場合

!!! note "ポートフォワーディング設定時に以下の情報を入力してください"

    ポートフォワーディングを設定する際は、以下の情報を入力してください。なお、項目名はルーターのブランドやモデルによって異なる場合があります。

    * **External port/Internal port:** 使用するポートを入力します。たとえば、デフォルトのポートは **1194**（OpenVPNサーバー用）と **51820**（WireGuardサーバー用）です。
    * **Protocol:** **All** または **UDP/TCP** を選択します。
    * **Internal IP**（または **Host IP** と表示される場合があります）: セカンダリルーターのWAN IPアドレスを入力するか、利用可能であればドロップダウンからセカンダリルーターを選択します。

以下は、一般的なメインルーターブランドやモデルでポートフォワーディングを設定するための手順です。

メインルーターのブランドまたはモデルが以下にない場合は、ルーターのマニュアルを参照するか、サポートチームへお問い合わせください。

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link

* [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero

[こちらのリンク](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}を参照してください。

### Linksys

[こちらのリンク](https://support.linksys.com/kb/article/318-en/){target="_blank"}を参照してください。

### Netgear

[こちらのリンク](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}を参照してください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
