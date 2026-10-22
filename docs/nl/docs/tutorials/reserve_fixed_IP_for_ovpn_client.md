# How to reserve a fixed IP for OpenVPN client in a self built OpenVPN connection? {#how-to-reserve-a-fixed-ip-for-openvpn-client-in-a-self-built-openvpn-connection}

Deze handleiding laat zien hoe je een vast IP-adres reserveert voor een OpenVPN-client die met je server verbindt. Stel eerst een GL.iNet-router als OpenVPN-server in.

1. Meld je aan bij het webbeheerpaneel van de OpenVPN-server en ga links naar **VPN** -> **OpenVPN Server**.

    Noteer op het tabblad **Configuration** het **IPv4 subnet**, bijvoorbeeld 10.8.0.0/24, en stel Authentication Mode in op **Username and Password Only**.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Open het tabblad **Users** en maak een gebruikersnaam en wachtwoord.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. SSH log in to the router, run the following command to open the OpenVPN server configuration script file:

    `vi /lib/netifd/proto/openserver.sh`

    Controleer in het geopende bestand of de regel "*client-config-dir /etc/openvpn/ccd*" aanwezig is.

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    Voeg de regel anders handmatig toe, sla het bestand op en sluit het.

4. Go to `/etc/openvpn/`, add a ccd folder `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Ga naar `/etc/openvpn/ccd`, voeg het bestand "GLsupport" toe en voer `ifconfig-push 10.8.0.10 255.255.255.0` in. Sla het bestand op en sluit het.

    Verify the content by `cat GLsupport`

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Wanneer GLsupport met de OpenVPN-server verbindt, krijgt deze gebruiker het vaste IP-adres 10.8.0.10.

    - "255.255.255.0" is het subnetmasker. Je kunt dit vervangen door het subnetmasker van je OpenVPN-server.

    **Opmerking**: maak voor meerdere clients in stap 2 meerdere gebruikers aan. Herhaal stap 5 en voeg voor elke gebruiker, zoals user_1, user_2 en user_3, een bestand aan de map CCD toe met de opdracht "ifconfig-push", het vaste IP-adres en subnetmasker.

    For example, `ifconfig-push 10.8.0.20 255.255.255.0`, `ifconfig-push 10.8.0.30 255.255.255.0`, `ifconfig-push 10.8.0.40 255.255.255.0`

6. Test met je OVPN-client en controleer of Client Virtual IP (IPv4) het gereserveerde adres is.

    Als de OpenVPN-client een GL.iNet-router is, meld je je aan bij het webbeheerpaneel en controleer je op VPN Dashboard het Client Virtual IP (IPv4).

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(VPN Dashboard in firmware v4.7 and earlier)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(VPN Dashboard in firmware v4.8)</small>

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
