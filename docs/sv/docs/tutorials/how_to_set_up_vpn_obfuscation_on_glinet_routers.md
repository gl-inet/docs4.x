# Så konfigurerar du VPN-obfuskering på GL.iNet-routrar {#how-to-set-up-vpn-obfuscation-on-glinet-routers}

**Obs!** GL.iNet-routrar stöder AmneziaWG med firmware v4.9 eller senare. Uppgradera först routern till en firmwareversion som stöds.

Den här guiden beskriver två scenarier för att konfigurera AmneziaWG-obfuskering på GL.iNet-routrar.

## Scenario 1. Använda två GL.iNet-routrar {#scenario-1-using-two-glinet-routers}

I det här scenariot används två GL.iNet-routrar för att upprätta en obfuskerad VPN-anslutning via AmneziaWG-protokollet.

- Brume 3 (GL-MT5000): En VPN-server för hemmet.
- Beryl AX (GL-MT3000): En bärbar VPN-klient för användning på resan.

### Konfigurera VPN-servern {#set-up-vpn-server}

1. Logga in på webbadministrationspanelen för Brume 3.

    Anslut en enhet, till exempel en bärbar eller stationär dator, till LAN-porten på Brume 3 med en Ethernet-kabel. Öppna en webbläsare, ange standardadressen för administration (vanligtvis `192.168.8.1`) och logga in med administratörslösenordet.

2. Slutför den första konfigurationen av Brume 3 för internetåtkomst.

    Om Brume 3 används som primär router ansluter du dess WAN-port till det uppströms nätverket, till exempel internetleverantörens modem.

    Om den inte är primär router, det vill säga om en annan uppströmsenhet som internetleverantörens router fungerar som primär router, måste du konfigurera **portvidarebefordran** på den primära routern. Se [den här länken](how_to_set_up_port_forwarding.md).

3. Aktivera DDNS (valfritt).

    Aktivera DDNS om din offentliga IP-adress är dynamisk i stället för statisk.

    Gå till **APPLICATIONS** -> **Dynamic DNS** i det vänstra sidofältet. Aktivera **Enable DDNS**, godkänn **Terms of Service & Privacy Policy** och klicka sedan på **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/enable_ddns.png){class="glboxshadow"}

4. Aktivera VPN-obfuskering.

    Gå till **VPN** > **WireGuard Server** -> fliken **Configurations** i det vänstra sidofältet, aktivera **Enable Obfuscation** och klicka sedan på **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    Du kan anpassa obfuskeringsparametrarna efter behov. Klicka [här](../faq/amneziawg_obfuscation.md#parameter-overview) för mer information.

    Vi rekommenderar att du behåller standardinställningarna.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Exportera konfigurationsfilen.

    Gå till fliken **Profiles** på sidan **WireGuard Server** och klicka på **Add** för att skapa en konfigurationsfil som Beryl AX kan använda för anslutningen.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Ange ett beskrivande namn, till exempel Travel Router, och klicka sedan på **Apply**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    Klicka på **Export** i popup-fönstret för att hämta konfigurationsfilen till enheten för senare användning.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Starta VPN-servern.

    Klicka på **Start** längst upp på sidan **WireGuard Server** för att starta servern.

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    VPN-servern med AmneziaWG-obfuskering är nu aktiverad. Du kan ansluta till VPN-servern Brume 3 med AmneziaWG-appen eller en GL.iNet-router med firmware som stöder AmneziaWG-obfuskering.

    **Obs! Klienter som inte stöder AmneziaWG-obfuskering kan inte ansluta.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

### Konfigurera VPN-klienten {#set-up-vpn-client}

1. Logga in på webbadministrationspanelen för Beryl AX.

    Anslut en enhet, till exempel en bärbar eller stationär dator, till Beryl AX via Wi-Fi eller till LAN-porten med en Ethernet-kabel. Öppna en webbläsare, ange standardadressen för administration (vanligtvis `192.168.8.1`) och logga in med administratörslösenordet.

2. Slutför den första konfigurationen av Beryl AX för internetåtkomst.

    **Tips**: Anslut Beryl AX till ett annat nätverk än Brume 3. Du kan till exempel aktivera en mobil hotspot och ansluta Beryl AX till den.

3. Ladda upp konfigurationsfilen.

    Gå till **VPN** > **WireGuard Client** i det vänstra sidofältet. Lägg till en ny grupp och ange ett beskrivande namn, till exempel Home Router.

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Ladda upp den tidigare exporterade konfigurationsfilen på höger sida.

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    Klicka på **Apply** när konfigurationsfilen har laddats upp och verifierats.

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    Sidan uppdateras och en konfigurationsfil visas i listan.

4. Starta VPN-anslutningen.

    Klicka på ikonen med tre punkter och välj sedan **Start**.

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Vänta i ungefär 1 minut. När statusindikatorn blir grön har VPN-anslutningen upprättats.

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Gå till **VPN Dashboard**. Där visas att Beryl AX är ansluten till hemroutern Brume 3.

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Dubbelkontroll (valfritt).

    Logga in på webbadministrationspanelen för Brume 3 och gå till **VPN** -> **WireGuard Server**. Där visas även en onlineklient, Beryl AX, som är ansluten till VPN-servern Brume 3.

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    VPN-anslutningen är klar. Alla enheter på Beryl AX ansluter nu till internet via gatewayen på Brume 3 och använder en obfuskerad VPN-anslutning.

## Scenario 2. Använda en enda GL.iNet-router {#scenario-2-using-a-single-glinet-router}

I det här scenariot används en enda GL.iNet-router, **Brume 3 (GL-MT5000)**, som VPN-klient för anslutning till en AmneziaVPN-server.

Du behöver då inte driftsätta en egen server. Hämta bara en AmneziaWG-konfigurationsfil från [Amnezias officiella webbplats](https://amnezia.org/){target="_blank"} eller en VPN-tjänsteleverantör som har stöd för AmneziaWG och ladda sedan upp filen till GL.iNet-routern. Därefter kan du upprätta en VPN-anslutning med obfuskering aktiverad.

### Hämta konfigurationen {#download-configuration}

<u>Alternativ 1</u>: Hämta en konfiguration från Amnezias officiella tjänst (Premium-prenumeration krävs).

1. Logga in på [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} med din Subscription Key.

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Gå till **Connection Assets** -> **Configuration Files** på Amnezia Dashboard, välj ett land och hämta en konfigurationsfil till enheten för senare användning.

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Alternativ 2</u>: Hämta en konfiguration från en annan VPN-leverantör med stöd för AmneziaWG.

StarVPN används som exempel.

1. Öppna StarVPNs [prisplaner](https://www.starvpn.com/#pricing){target="_blank"} och välj en VPN-plan som passar dina behov. Du kan registrera ett StarVPN-konto i kassan eller direkt [här](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

2. Logga in på [StarVPN Dashboard](https://www.starvpn.com/dashboard){target="_blank"}, leta reda på **VPN Configuration** och klicka på **AmneziaWG Config** för att hämta konfigurationsfilen.

    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. Konfigurationen kan innehålla en IPv6-adress. Undvik kompatibilitets- och anslutningsproblem genom att öppna .conf-filen och ta bort IPv6-adressen enligt nedan.

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Följ sedan stegen nedan för att konfigurera VPN-klienten.

### Konfigurera VPN-klienten {#set-up-vpn-client_1}

1. Logga in på webbadministrationspanelen för Brume 3.

    Anslut en enhet, till exempel en bärbar eller stationär dator, till LAN-porten på Brume 3 med en Ethernet-kabel. Öppna en webbläsare, ange standardadressen för administration (vanligtvis `192.168.8.1`) och logga in med administratörslösenordet.

2. Slutför den första konfigurationen av Brume 3 för internetåtkomst.

3. Ladda upp konfigurationsfilen.

    Gå till **VPN** > **WireGuard Client** i det vänstra sidofältet. Lägg till en ny grupp och ange ett beskrivande namn, till exempel AmneziaVPN.

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Ladda upp den tidigare exporterade AmneziaVPN-konfigurationsfilen på höger sida.

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    Klicka på **Apply** när konfigurationsfilen har laddats upp och verifierats.

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    Sidan uppdateras och en konfigurationsfil visas i listan.

4. Starta VPN-anslutningen.

    Klicka på ikonen med tre punkter och välj sedan **Start**.

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Vänta i ungefär 1 minut. När statusindikatorn blir grön har VPN-anslutningen upprättats.

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Gå till **VPN Dashboard**. Där visas att Brume 3 är ansluten till en AmneziaVPN-server.

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

    VPN-anslutningen är klar. Alla enheter på Brume 3 ansluter nu till internet via AmneziaVPN-servern och använder en obfuskerad VPN-anslutning.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
