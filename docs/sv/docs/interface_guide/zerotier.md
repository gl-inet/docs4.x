# ZeroTier {#zerotier}

ZeroTier är ett programvarubaserat VPN för säker, krypterad kommunikation mellan enheter. Det skapar ett privat virtuellt nätverk där enheter kommunicerar som i samma LAN oavsett plats, med end-to-end-kryptering, segmentering och bryggning.

ZeroTier finns på GL.iNet-routrar från firmware v4.2 och låter routern ansluta till ett virtuellt ZeroTier-nätverk för fjärråtkomst till WAN- och LAN-resurser.

**Note**:

1. ZeroTier bör inte användas samtidigt med OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale eller AstroWarp eftersom routningskonflikter kan uppstå.

2. Funktionen är i beta och kan innehålla fel.

3. Some models, although running firmware v4.2 or higher, do not support ZeroTier due to insufficient memory.

## Supported Models {#supported-models}

??? "Supported Models"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Unsupported Models"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Set up ZeroTier network {#set-up-zerotier-network}

ZeroTier Central finns som New Central och Legacy Central.

- **New Central**: Ny version med förbättrad användning och nya funktioner, rekommenderad för nya användare.

- **Legacy Central**: For accounts created before November 2025. Legacy Central continues to support existing users managing their networks.

Båda versionerna kan användas parallellt, men direkt migrering saknas.

Välj lämplig version.

### New Central {#new-central}

The following is an example using the GL-MT3600BE.

1. Besök [ZeroTiers webbplats](https://www.zerotier.com/){target="_blank"} och logga in.

    ![zerotier login](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Create an organization.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Välj abonnemang. Personal används som exempel och omfattar 10 enheter, 1 nätverksadministratör och 1 nätverk. Välj Essential eller Scale för fler nätverk, enheter, egna rutter och DNS.

    ![select plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Nätverket har skapats. Anteckna **Network ID**, en alfanumerisk kombination med 16 tecken uppe till höger.

    ![network id](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Enable ZeroTier on GL.iNet router.

    Logga in och öppna **APPLICATIONS** -> **ZeroTier**.

    Aktivera ZeroTier, ange Network ID och klicka på **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    Efter en stund anges att auktorisering krävs. Klicka på **ZeroTier Central**.

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Authorize your device on ZeroTier Central.

    Leta reda på Pending-enheten i ZeroTier Central och auktorisera den.

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Once authorized, the page displays as follows.

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Add another device (such as a computer or smartphone) to the same ZeroTier network by following [this guide](https://docs.zerotier.com/platforms/){target="_blank"}.

    Below is an example using a Windows 10 Pro laptop.

    1. Installera ZeroTier på den bärbara datorn [härifrån](https://www.zerotier.com/download/){target="_blank"}.

    2. Starta ZeroTier. Ikonen visas i systemfältet nere till höger.

    3. Högerklicka på ikonen, välj **Join New Network** och ange **Network ID** från steg 4.

        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Öppna ZeroTier Central, leta reda på Pending-enheten och auktorisera den.

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Efter auktorisering visas **Device ID**, **Name**, **Status**, **Managed IP** och **Public IP**.

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Tips!** Klicka på ikonen med tre punkter för att ändra namn, Managed IP och avancerade inställningar.

8. Klicka på routerns **Managed IP** för att kopiera den och nå routern från en dator i samma ZeroTier-nätverk.

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Test connectivity.

    Öppna en webbläsare på datorn och ange routerns Managed IP.

    Om webbadministrationspanelen öppnas fungerar anslutningen.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Du kan även testa med `ping` mot Managed IP.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central {#legacy-central}

The following is an example using the GL-MT2500.

1. Create your first ZeroTier network.

    Följ ZeroTiers [Getting Started Guide](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"} för konto och nätverk. Anteckna Network ID med 16 tecken.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Enable ZeroTier on GL.iNet router.

    Logga in och öppna **APPLICATIONS** -> **ZeroTier**.

    Aktivera ZeroTier, ange Network ID och klicka på **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_enable.png){class="glboxshadow"}

    Efter en stund anges att auktorisering krävs.

    Klicka på **ZeroTier Central**.

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_central.png){class="glboxshadow"}

3. Authorize your device on ZeroTier Central.

    Öppna **Members** i ZeroTier Central, hitta enheten och markera **Auth**. Anpassa namnet vid behov.

    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    ZeroTier tilldelar en **Managed IP**. Anteckna adressen för testet.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/managed_ip.png){class="glboxshadow"}

4. Add another device (such as a computer or smartphone) to the same ZeroTier network by following [this guide](https://docs.zerotier.com/platforms/){target="_blank"}.

5. Test connectivity.

    Öppna en webbläsare på en annan enhet i nätverket och ange routerns Managed IP.

    Routerns webbadministrationspanel öppnas.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/web_admin_panel.png)

    Du kan även testa med `ping`. Se ZeroTiers [Quickstart Guide](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"}.

## Allow Remote Access WAN {#allow-remote-access-wan}

När alternativet är aktiverat kan resurser på WAN-sidan nås via ZeroTier.

I topologin kan `leo-phone` nå `GL-AXT1800` via `192.168.29.1` eftersom GL-AXT1800 är uppströms `GL-MT2500`, som finns i samma ZeroTier-nätverk.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Obs!** Funktionen kräver routningsregler. Legacy Central tillåter en kostnadsfri egen rutt, medan New Central kräver Essential eller högre. Se [priser](https://www.zerotier.com/pricing/).

The following steps use Legacy Central as an example.

1. Logga in och öppna **APPLICATIONS** -> **ZeroTier**.

    Enable **Allow Remote Access WAN**, and click **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    Du uppmanas att konfigurera rutter. Behåll sidan öppen eller anteckna Destination och Via.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Öppna **Advanced** i **ZeroTier Central**.

    Ange Destination och Via och klicka på **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_1.png){class="glboxshadow"}

    Once the route is added, the **Managed Routes** section will display as shown below.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_2.png){class="glboxshadow"}

3. Andra enheter kan nu nå `GL-AXT1800` via `192.168.29.1` och alla enheter i `192.168.29.0/24`.

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN {#allow-remote-access-lan}

När alternativet är aktiverat kan resurser på LAN-sidan nås via ZeroTier.

I topologin kan `leo-phone` logga in via SSH på `Ubuntu` med `192.168.8.110`, eftersom Ubuntu är nedströms `GL-MT2500` i samma nätverk.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Obs!** Funktionen kräver routningsregler. Legacy Central tillåter en kostnadsfri egen rutt, medan New Central kräver Essential eller högre. Se [priser](https://www.zerotier.com/pricing/).

The following steps use Legacy Central as an example.

1. Logga in och öppna **APPLICATIONS** -> **ZeroTier**.

    Enable **Allow Remote Access LAN**, and click **Apply**.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    Du uppmanas att konfigurera rutter. Behåll sidan öppen eller anteckna Destination och Via.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Öppna **Advanced** i **ZeroTier Central**.

    Ange Destination och Via och klicka på **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_3.png){class="glboxshadow"}

    Once the route is added, the **Managed Routes** section will display as shown below.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_4.png){class="glboxshadow"}

3. Andra enheter kan nu pinga eller SSH-logga in på `Ubuntu` via `192.168.8.110` och nå alla enheter i `192.168.8.0/24`.

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
