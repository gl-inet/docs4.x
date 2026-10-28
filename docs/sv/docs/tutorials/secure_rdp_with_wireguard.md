# Skydda RDP från ett externt nätverk med WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

Du kan behöva fjärransluta till en dator från ett externt nätverk eller i motsatt riktning. Ett säkert sätt är att använda en egen WireGuard-tunnel. Det ger bättre säkerhet än portvidarebefordran och direkt åtkomst till datorn via den offentliga IP-adressen. När tunneln har konfigurerats kan du använda **Windows Remote Desktop** för att komma åt datorn varifrån som helst.

Guiden använder två GL.iNet-routrar som exempel för att visa hur Windows RDP skyddas via ett WireGuard-nätverk.

## Topologi {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Konfigurationssteg {#setup-steps}

1. Skapa WireGuard-nätverket.

    Konfigurera först en egen WireGuard-server och WireGuard-klient med två GL.iNet-routrar. Se [Bygg en egen WireGuard-server med två GL.iNet-routrar](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Tillåt WireGuard-servern att komma åt klientens LAN.

    För att möjliggöra dubbelriktad åtkomst mellan servern och klienten måste du först tillåta servern att komma åt klientens LAN-sida. Se [Öppna WireGuard-klientens LAN-sida från servern](wireguard_server_access_to_client_lan_side.md).

    Stegen kan variera mellan firmwareversioner.

3. Tillåt WireGuard-klienten att komma åt serverns LAN.

    Steget kan variera mellan firmwareversioner. Välj firmwareversionen för routern som används som WireGuard-klient nedan.

    ??? note "För firmware v4.7 och tidigare"

        Logga in på WireGuard-klienten och gå till **VPN** -> **VPN Dashboard**. Leta reda på **VPN Server** och klicka på kugghjulsikonen till höger.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        Aktivera **Remote Access LAN** i dialogrutan och klicka på **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "För firmware v4.8 och senare"

        Logga in på WireGuard-klienten och gå till **VPN** -> **WireGuard Server**. Klicka på **Options** i det övre högra hörnet.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        Aktivera **Allow Remote Access to the LAN Subnet** i dialogrutan och klicka på **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Anslut datorn som ska fjärranslutas till VPN-servern och ta reda på dess LAN-IP-adress.

    I följande exempel är IP-adressen för datorn på serversidan **192.168.29.123**.

5. Konfigurera datorn på serversidan för fjärråtkomst.

    Gå till **System Settings** på datorn på serversidan och klicka på **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Aktivera **Remote Desktop** och klicka på **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Fjärranslut från den bärbara datorn på klientsidan.

    Sök efter **Remote Desktop Connection** i sökfältet.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Starta appen och ange IP-adressen för datorn på serversidan, till exempel **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Ange inloggningsuppgifterna för datorn på serversidan för att ansluta.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Du kan nu fjärrstyra datorn på serversidan.

    Om du vill ansluta i motsatt riktning byter du plats på stegen för datorn på serversidan och den bärbara datorn på klientsidan.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
