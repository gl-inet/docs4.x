# How to reserve fixed IP for OpenVPN client in a self built OpenVPN connection?

If you have successfully set up your OpenVPN server using a GL.iNet router, this tutorial will show you how to reserve a fixed IP for your OpenVPN client connecting to your server.

1. Log in to the web admin panel of your OpenVPN server, from the left sidebar, navigate to **VPN** -> **OpenVPN Server**.

    In the **Configuration** tab, note down the **IPv4 subnet**, and switch the Authentication Mode to **Username and Password Only**. For example, the following shows that the IPv4 subnet is 10.8.0.0/24.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Turn to **Users** tab, create a username and password. As shown below, a username "GLsupport" has been created as an example.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. SSH log in to the router, run the following command to open the OpenVPN server configuration script file:

    `vi /etc/lib/netifd/proto/openserver.sh`

    In the opened file, check if the line "*client-config-dir /etc/openvpn/ccd*" exists in the script. 

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    If not, add it manually, then save and exit the file (in the vi editor, press the **Esc** key, then enter **:wq** and press Enter).

4. Go to `/etc/openvpn/`, add a ccd folder `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Add a file "GLsupport", followed by `ifconfig-push 10.8.0.10 255.255.255.0`

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Replace the "GLsupport" with the username you created in Step 2.
    
    - Replace the "10.8.0.10" with the fixed IP you want to reserve for your ovpn client, ensuring this fixed IP is within the IPv4 subnet of your OpenVPN server. 
    
    - The "255.255.255.0" is the subnet mask and you can replace it with your OpenVPN server subnet mask.

    **Note**: If you want to fix IP addresses for multiple OpenVPN clients, please create multiple usernames and passwords in Step 2, then repeat Step 5, add files to the CCD folder in the order of users, such as user_1, user_2, user_3, followed by the "ifconfig push" command and their corresponding fixed IP and subnet mask. 
    
    For example, `ipconfig-push 10.8.0.31 225.225.225.0`, `ipconfig-push 10.8.0.32 225.225.225.0`, `ipconfig-push 10.8.0.33 225.225.225.0`

6. At last, test with your OVPN client and check if the Client Virtual IP (IPv4) is the reserved one you set. 

    For example, if your OpenVPN client is a GL.iNet router, you can log in to the OpenVPN client router’s web admin panel, navigate to OpenVPN Client, and verify the Client Virtual IP (IPv4).

    ![test 1](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/test_e.g.1.png){class="glboxshadow"}

    ![test 2](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/test_e.g.2.png){class="glboxshadow"}

    ![test 3](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/test_e.g.3.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.