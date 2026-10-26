# Ansluta till Surfshark med en dedikerad IP-adress på GL.iNet-routrar {#how-to-connect-to-surfshark-with-a-dedicated-ip-on-glinet-routers}

Artikeln beskriver hur du konfigurerar en Surfshark-anslutning med en dedikerad IP-adress på GL.iNet-routrar.

Vi använder GL-AXT1800 som exempel.

1. Logga in på ditt Surfshark-konto och välj **Dedicated IP**.

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/manualdip.jpg){class="glboxshadow"}

2. Klicka på **Settings** under avsnittet Dedicated IP.

    ![setting](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/setting.jpg){class="glboxshadow"}

3. Välj ett protokoll (WireGuard eller OpenVPN) och ladda ned konfigurationsfilerna för manuell anslutning.

    ![protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/protocol.jpg){class="glboxshadow"}

    För WireGuard-konfigurationen visar nedladdningssidan Server IP och Server Public Key enligt nedan.

    ![loadwg](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/loadwg.jpg){class="glboxshadow"}

    För OpenVPN-konfigurationen visar nedladdningssidan Server IP och inloggningsuppgifterna (Username & Password) enligt nedan. Kopiera inloggningsuppgifterna för senare användning.

    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/loadovpn.jpg){class="glboxshadow"}

4. Följ länkarna nedan för att ladda upp konfigurationsfilerna till GL.iNet-routern. Ange inloggningsuppgifterna om det krävs.

    - [Ladda upp WireGuard-konfigurationen](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [Ladda upp OpenVPN-konfigurationen](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
