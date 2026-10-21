# Hur fjärransluter jag till webbadministrationspanelen på en GL.iNet-router? {#how-to-remotely-access-the-web-admin-panel-of-a-glinet-router}

Följande metoder måste konfigureras i förväg medan du fortfarande befinner dig fysiskt intill routern.

## Metod 1. GoodCloud {#method-1-goodcloud}

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} är en plattform som förenklar fjärrdistribution och hantering av anslutna enheter. Den gör det enkelt att fjärransluta till och hantera GL.iNet-routrar. Koppla din GL.iNet-router till GoodCloud. Därefter kan du fjärransluta till routerns webbadministrationspanel när och var som helst.

Mer information finns i [den här guiden](../interface_guide/cloud.md){target="_blank"}.

## Metod 2. VPN {#method-2-vpn}

Om routern har en **offentlig IP-adress** kan du fjärransluta till webbadministrationspanelen via en VPN-tunnel. Observera att den här metoden kräver avancerad konfiguration och tar extra tid att konfigurera.

1. Kontrollera att routern har en offentlig IP-adress. [Hur kontrollerar jag om min internetleverantör har tilldelat mig en offentlig IP-adress?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Konfigurera routern som WireGuard-server. Mer information finns [här](../interface_guide/wireguard_server.md){target="_blank"}.

3. Exportera en konfigurationsfil från WireGuard-servern för senare användning.

4. Gå till **VPN** -> **WireGuard Server** i routerns webbadministrationspanel och klicka på **Options** i det övre högra hörnet. Aktivera **Allow Remote Access to the LAN Subnet** och klicka sedan på **Apply**.

5. Konfigurera enheten som du vill fjärransluta från som WireGuard-klient genom att importera konfigurationsfilen manuellt.

    - Om WireGuard-klienten är en slutenhet, till exempel en smarttelefon eller bärbar dator, [installerar du WireGuard-appen](https://www.wireguard.com/install){target="_blank"} och importerar sedan filen för att starta en anslutning.

    - Om WireGuard-klienten är en annan GL.iNet-router, till exempel en GL.iNet-reserouter, följer du [den här guiden](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"} för att importera konfigurationsfilen till den och starta en anslutning.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
