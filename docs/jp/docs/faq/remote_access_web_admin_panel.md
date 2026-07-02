# GL.iNetルーターのWeb管理パネルにリモートアクセスする方法は？

次の方法は、ルーターの近くにいる間に事前設定を行う必要があります。

## 方法1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"}は、接続済みデバイスのリモート展開と管理を簡単にするためのプラットフォームです。GL.iNetルーターにリモートアクセスして管理するための簡単な方法を提供します。GL.iNetルーターをGoodCloudにバインドするだけで、いつでもどこからでもルーターのWeb管理パネルにリモートアクセスできます。

詳細については、[こちらのガイド](../interface_guide/cloud.md){target="_blank"}を参照してください。

## 方法2. VPN

ルーターに**パブリックIP**がある場合は、VPNトンネル経由でWeb管理パネルにリモートアクセスできます。この方法には高度な設定が含まれ、セットアップに追加の時間がかかる点に注意してください。

1. ルーターにパブリックIPがあることを確認します。[パブリックIPアドレスがあるかどうかを確認する方法は？](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. ルーターをWireGuard Serverとして設定します。詳細は[こちら](../interface_guide/wireguard_server.md){target="_blank"}を参照してください。

3. 後で使用するために、WireGuard Serverから設定ファイルをエクスポートします。

4. ルーターのWeb管理パネルで、**VPN** -> **WireGuard Server**に移動し、右上の**Options**をクリックします。**Allow Remote Access to the LAN Subnet**を有効にしてから、**Apply**をクリックします。

5. ルーターにリモートアクセスするために使用するデバイスを、設定ファイルを手動でインポートしてWireGuard Clientとして設定します。

    - WireGuard ClientがスマートフォンやノートPCなどの端末の場合は、[WireGuard Appをインストール](https://www.wireguard.com/install){target="_blank"}し、ファイルをインポートして接続を開始します。

    - WireGuard ClientがGL.iNetトラベルルーターなど別のGL.iNetルーターの場合は、[こちらのガイド](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"}を参照して設定ファイルをインポートし、接続を開始します。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
