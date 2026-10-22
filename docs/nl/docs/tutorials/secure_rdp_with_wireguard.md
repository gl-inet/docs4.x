# RDP vanaf een extern netwerk beveiligen met WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

Mogelijk wil je vanaf een extern netwerk toegang krijgen tot je pc, of omgekeerd. De veiligste manier is via je eigen WireGuard-tunnel. Dit is veiliger dan port forwarding en rechtstreekse toegang tot je pc via je openbare IP-adres. Nadat je de tunnel hebt ingesteld, kun je met **Windows Remote Desktop** overal toegang krijgen tot je pc.

In deze handleiding gebruiken we twee GL.iNet-routers als voorbeeld om te laten zien hoe je Windows RDP via een WireGuard-netwerk beveiligt.

## Topologie {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Configuratiestappen {#setup-steps}

1. Bouw je WireGuard-netwerk.

    Stel eerst je eigen WireGuard-server en WireGuard-client in met twee GL.iNet-routers. Zie [Je eigen WireGuard-server bouwen met twee GL.iNet-routers](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Geef je WireGuard-server toegang tot het LAN van de client.

    Sta eerst toe dat de server toegang heeft tot de LAN-zijde van de client om toegang in beide richtingen tussen server en client mogelijk te maken. Zie [Toegang krijgen tot de LAN-zijde van een WireGuard-client vanaf de server](wireguard_server_access_to_client_lan_side.md).

    De stappen kunnen per firmwareversie verschillen.

3. Geef je WireGuard-client toegang tot het LAN van de server.

    Deze stap kan per firmwareversie verschillen. Selecteer hieronder ter referentie de firmwareversie van de router die je als WireGuard-client hebt ingesteld.

    ??? note "Voor firmware v4.7 en ouder"

        Meld je aan bij je WireGuard-client en ga naar **VPN** -> **VPN Dashboard**. Zoek **VPN Server** en klik rechts op het tandwielpictogram.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        Schakel in het pop-upvenster **Remote Access LAN** in en klik op **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Voor firmware v4.8 en nieuwer"

        Meld je aan bij je WireGuard-client en ga naar **VPN** -> **WireGuard Server**. Klik rechtsboven op **Options**.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        Schakel in het pop-upvenster **Allow Remote Access to the LAN Subnet** in en klik op **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Verbind de computer waartoe je toegang wilt met de VPN-server en zoek het LAN-IP-adres.

    In het volgende voorbeeld is het IP-adres van de pc aan de serverzijde **192.168.29.123**.

5. Configureer de pc aan de serverzijde zodat deze toegankelijk is.

    Ga op de pc aan de serverzijde naar **System Settings** en klik op **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Schakel **Remote Desktop** in en klik op **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Maak op afstand verbinding vanaf de laptop aan de clientzijde.

    Zoek in de zoekbalk naar **Remote Desktop Connection**.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Start de app en voer het IP-adres van de pc aan de serverzijde in, bijvoorbeeld **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Voer de aanmeldgegevens van je pc aan de serverzijde in om verbinding te maken.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Je kunt de pc aan de serverzijde nu op afstand bedienen.

    Wil je dit in de omgekeerde richting doen, verwissel dan de stappen voor de pc aan de serverzijde en de laptop aan de clientzijde.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
