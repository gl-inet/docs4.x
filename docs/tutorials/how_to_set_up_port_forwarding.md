# プライマリルーターでポート転送を設定する方法

GL.iNetルーターでサーバー（[OpenVPNサーバー](https://docs.gl-inet.com/router/en/4/tutorials/build_your_own_openvpn_home_server_with_two_glrouter/)や[WireGuardサーバー](https://docs.gl-inet.com/router/en/4/tutorials/build_your_own_wireguard_home_server_with_two_glinet_routers/)など）を設定し、それがプライマリルーターに接続されている場合、プライマリルーターでポート転送を設定する必要があります。こうすることで、サーバーが適切にアクセス可能になります。（プライマリルーターとGL.iNetルーターの間に他のルーターがある場合、これらの前のすべてのルーターでポート転送を設定する必要があります。）

ポート転送を設定する手順は、ルーターのブランドとモデルにより異なります。以下のセクションで該当するものを参照してください。

## GL.iNetルーターをプライマリルーターとして使用する場合

プライマリルーターがGL.iNetルーターの場合、以下の手順でポート転送を設定します。

1. Webブラウザで、ルーター管理パネルのURL（例：`192.168.8.1`）を入力し、サインインします。
2. 左側のサイドバーで、**Network** > **Firewall** をクリックします。
3. **Port Forwards** タブで、**Add** をクリックします。
4. 次の情報を入力します：
    * **Name:** ルールの任意の名前を入力します。
    * **Protocol:** そのままにします。
    * **External Zone:** そのままにします。
    * **External Port:** 使用するポートを入力します。例：デフォルトのポートは**1194**（OpenVPNサーバー用）および**51820**（WireGuardサーバー用）です。
    * **Internal Zone:** そのままにします。
    * **Internal IP:** ポートを転送するルーターを選択します。
    * **Internal Port:** 使用するポートを入力します。例：デフォルトのポートは**1194**（OpenVPNサーバー用）および**51820**（WireGuardサーバー用）です。
5. **Apply** をクリックします。

## 他のブランドのルーターをプライマリルーターとして使用する場合

!!! note "ポート転送を設定する際に次の情報を入力してください："

    ルーターのブランドやモデルによって、ポート転送を設定する際に提供する情報の名前が異なります。一般的には、ルーターのポート転送画面に次の情報を入力してください：
    
    * **External port/Internal port:** 使用するポートを入力します。例：デフォルトのポートは**1194**（OpenVPNサーバー用）および**51820**（WireGuardサーバー用）です。
    * **Protocol:** **All** または **UDP/TCP** を選択します。
    * **Internal IP**（または **Host IP** と表示されることもあります）：セカンダリルーターのWAN IPアドレスを入力するか、ドロップダウンからセカンダリルーターを選択します。

以下は、プライマリルーターとして特定のブランドやモデルのルーターでポート転送を設定するための手順です：

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/)
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/)
* [Pace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/)

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.xfinity.com/support/articles/set-up-port-forwarding-xfinity-xfi)

### Eero

[これらの手順を参照してください。](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding)

### リンクシス

[これらの指示を参照してください。](https://www.tp-link.com/us/support/faq/1379/)

### ネットギア

[これらの指示を参照してください。](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router)

### TP-Link

[これらの指示を参照してください。](https://www.tp-link.com/us/support/faq/1379/)

上記にリストされていない特定のルーターブランドまたはモデルについて支援が必要な場合は、ルーターの製造元またはGL.iNetサポートチームにメールでお問い合わせください：[support@glinet.biz](mailto:support@glinet.biz)。

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。