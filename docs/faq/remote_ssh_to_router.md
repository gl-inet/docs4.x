# GL.iNetルーター端末へのリモートSSH接続方法は？

- **方法 1**: ルーターのネットワークに [パブリックIP](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)がある場合、[WireGuard サーバー](../interface_guide/wireguard_server.md)をセットアップし、WireGuardを使用してルーターにSSH接続してください。パブリックIPをお持ちでない場合は、2と3の方法をお試しください。
- **方法 2**: [デバイスをGoodCloudにバインド](../interface_guide/cloud.md#setup)してください。 その後、 [GoodCloud Web サイト](https://www.goodcloud.xyz){target="_blank"}にログインすることで、[ルーターにリモートで SSH 接続](../interface_guide/cloud.md#remote-access-routers-terminal)できます。
- **方法 3**: リバース プロキシ ソリューションを使用するには、[AstroRelay](https://www.astrorelay.com/){target="_blank"}をお勧めします。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
