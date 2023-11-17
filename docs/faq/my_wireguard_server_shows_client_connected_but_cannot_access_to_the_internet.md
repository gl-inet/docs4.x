# My WireGuard Server Shows Client connected but cannot access to the internet

1. Your main router gateway IP is conflict with the WireGuard Server Virtual IP.

    Please see point 2 of [set up Wiregaurd Server](../interface_guide/wireguard_server.md/#setup-wireguard-server)

2. If you are using two GL-iNet Routers as the server and client, please change the LAN IP of either one.

    Change the [LAN IP](../interface_guide/lan.md)

3. You ISP cannot resolve your DNS. Please change the DNS on the configuration to **8.8.8.8** or **8.8.4.4**.

    ![dns8888](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/dns8888.jpg){class='glboxshadow'}

4. You have changed the Server Virtual IP yourself but you didn't put the **/24** and make it become **xx.x.x.x/24**.

    Please see point 2 of [set up Wiregaurd Server](../interface_guide/wireguard_server.md/#setup-wireguard-server)