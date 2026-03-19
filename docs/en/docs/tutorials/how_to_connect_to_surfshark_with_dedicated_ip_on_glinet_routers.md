# How to connect to Surfshark with a dedicated IP on GL.iNet routers?

This article introduces the steps to set up a Surfshark connection with a dedicated IP on GL.iNet routers.

We use the GL-AXT1800 as an example.

1. Log in to your Surfshark account, then select **Dedicated IP**.

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){calss="glboxshadow"}

2. Under the Dedicated IP section, click **Settings**.

    ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){calss="glboxshadow"}

3. Select a protocol (WireGuard or OpenVPN) and download configuration files for manual connection.

    ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){calss="glboxshadow"}
    
    For WireGuard configuration, the download page displays the Server IP and Server Public Key, as shown below.
    
    ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){calss="glboxshadow"}

    For OpenVPN configuration, the download page displays the Server IP and credentials (Username & Password), as shown below. Copy the credentials for later use.
    
    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){calss="glboxshadow"}

4. Refer to the links below to upload the configuration files to your GL.iNet router. Enter the credentials if required.

    - [Upload Wireguard configuration](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [Upload OpenVPN configuration](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.