# GL.iNetルーターのWeb Admin Panelにリモートアクセスする方法は？

- **方法１**: If your router's network has a　もしあなたのルーターのネットワークに [public IP](../how_to_check_if_isp_assigns_you_a_public_ip_address)がある場合, please set up a [WireGuard Server](../wireguard_server)をセットアップし WireGuardを使ってルーターのWeb管理パネルにアクセスしてください。　パブリックIPをお持ちでない方は、方法２と方法３をお試しください。
- **方法２**: Please [bind your device to GoodCloud](../cloud/#setup), then you can [access the router's web Admin Panel remotely](../cloud/#remote-access-web-admin-panel) by logging into the [GoodCloud website](https://www.goodcloud.xyz){target="_blank"}.
- **方法３**: To use a reverse proxy solution, we suggest [AstroRelay](https://www.astrorelay.com/){target="_blank"}.