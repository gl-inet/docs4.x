# OpenVPN Client

OpenVPN is an open-source VPN protocol that makes use of virtual private network (VPN) techniques to establish safe site-to-site or point-to-point connections. 

GL.iNet routers have pre-installed OpenVPN Client and Server.

We recommend WireGuard over OpenVPN because it is much faster. For setup a WireGuard Client, please check out [here](../wireguard_client).

If you have already bought OpenVPN service from a provider, but you don't know how to get the configuration file, please refer to [get configuration file from VPN service providers](#get-configuration-files-from-vpn-service-providers).

You can setup OpenVPN Client via web Admin Panel and [mobile app](../mobile_app). For the mobile app, it has already integrated NordVPN.

## Setup NordVPN

From firmware 4.0, it has integrated NordVPN OpenVPN service.

1. Input your credential, then click **Save Credentials & Get Servers**

    ![input nordvpn credential](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/input_nordvpn_credential.png)

2. Select protocol, max server count of each location, locations, then click **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/select_nordvpn_servers.png)

    It will download configuration files.

    ![downloaded configuration files](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/downloaded_configs.png)

3. Connection

    Go to VPN Dashboard to enable the connection.

    ![vpn dashboard page](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/vpn_dashboard_to_connect.png)

    Toggle the switch to enable the connection.

    ![openvpn connected](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/openvpn_connected.png)

4. Update servers

    NordVPN may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![update servers](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/update_servers.png)

5. Edit credential

    Click the cog icon to edit the credential.

    ![edit credential](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/edit_credential.png)

## Setup OpenVPN client

As of frimware 4.0, it brings grouping to manage OpenVPN profiles. Please make sure all the profiles in the same group with the same credentials. For example, if you are ExpressVPN user, you can add a group named expressvpn, then upload all the ExpressVPN OpenVPN profiles you wanted to this group. For another OpenVPN service provider, please create another group.

Next steps, we will use ExpressVPN as an example.

1. Add a new group

    ![add a new group](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/add_a_new_group.png)

    ![set the new group name](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/set_new_group_name.png)

2. Give the group a descriptive name, for example expressvpn.

    ![set the new group name](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/set_new_group_name_2.png)

3. Upload your OpenVPN configuration file, then input the credential, click **Apply**.

    ![upload profile](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/upload_profile.png)

    ![after upload profile](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/after_upload_profile.png)

4. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard page](https://static.gl-inet.com/docs/en/4/tutorials/openvpn_client/vpndashboard_to_connect_expressvpn.png)

## Setup OpenVPN server by GL.iNet router

You can get a GL.iNet router to set as OpenVPN server, and get another GL.iNet router to set as OpenVPN client. For setup OpenVPN server, please check out [here](../openvpn_server).

## Get configuration files from VPN service providers
