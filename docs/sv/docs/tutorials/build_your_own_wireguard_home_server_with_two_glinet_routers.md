# Bygg en egen WireGuard-hemmaserver med två GL.iNet-routrar {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Den här artikeln visar hur du konfigurerar hemroutern som WireGuard VPN-server och reseroutern som WireGuard VPN-klient för fjärranslutning. På så sätt kan du använda hemmets IP-adress med reseroutern var du än befinner dig.

Titta på videon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(I videon används GL-MT5000 (Brume 3) och GL-MT3600BE (Beryl 7) för att demonstrera VPN-konfigurationen.)</small>

I följande steg används GL-MT6000 (Flint 2) och GL-MT3000 (Beryl AX) som exempel:

- GL-MT6000, som är hemrouter, konfigureras som WireGuard VPN-server. Om trådlös kapacitet inte behövs kan du även använda säkerhetsgatewayen GL-MT2500 eller andra modeller.

- GL-MT3000, som är reserouter, konfigureras som WireGuard VPN-klient och ansluter på distans till VPN-servern hemma.

## Varför bygga en egen WireGuard-hemmaserver? {#why-build-your-own-wireguard-home-server}

1. Använd den offentliga IP-adressen för din hemanslutning så att trafiken ser ut att komma från hemmet.
2. Slipp månadsavgifterna för en VPN-tjänst från tredje part.
3. Skydda din integritet genom att leda all internettrafik till hemnätverket via en krypterad tunnel.
4. Kom åt enheterna hemma och lokala strömningstjänster var du än befinner dig.

## Förberedelser {#preparations}

### Kontrollera om du har en offentlig IP-adress {#check-if-you-have-a-public-ip}

Kontrollera först att GL-MT6000 har en offentlig IP-adress på WAN-sidan så att den kan nås globalt. Annars kan reseroutern inte upprätta en VPN-anslutning till den när du reser.

Kontrollera den offentliga IP-adressen genom att öppna en webbläsare och ange [what is my ip](https://whatismyipaddress.com/){target="_blank"} i adressfältet.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Din offentliga IP-adress visas. Om den stämmer överens med WAN-IP-adressen som internetleverantören har tilldelat GL-MT6000 har du en offentlig IP-adress.

Om du inte har en offentlig IP-adress kan du prova följande metoder.

1. Om du har en primär router loggar du in på den och kontrollerar om den får en offentlig IP-adress från internetleverantören.
2. Be internetleverantören om en offentlig IP-adress. Det kan tillkomma en avgift.
3. Om de två metoderna ovan inte fungerar, till exempel om nätverket ligger bakom CGNAT, kan du prova vår SD-WAN-lösning [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

### Kontrollera om portvidarebefordran krävs {#check-if-port-forwarding-is-required}

??? "GL.iNet som primär router"

    Om GL.iNet-routern är direkt ansluten till internetleverantörens modem med en Ethernet-kabel är GL.iNet-routern den primära routern.

    **Hur kontrollerar du om GL.iNet-routern är direkt ansluten till internetleverantörens modem?**

    Logga in på GL.iNet-routerns webbadministrationspanel. Välj **INTERNET** i det vänstra sidofältet och kontrollera nätverkstopologin och anslutningsinformationen.

    Vid direkt Ethernet-anslutning visas ett avsnitt som heter "Ethernet" med anslutningens protokoll, IP-adress och gateway.

    Den markerade IP-adressen i bilden är den WAN-IP-adress som internetleverantören har tilldelat GL.iNet-routern.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    WAN-IP-adressen är offentlig. GL.iNet-routern fungerar därmed som primär router, har en offentlig IP-adress och **behöver ingen portvidarebefordran**.

    Konfigurera bara GL.iNet-routern som WireGuard-server och en reserouter som WireGuard-klient som ansluter till servern. En VPN-tunnel upprättas då mellan dem.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet som sekundär router"

    Konfigurera **portvidarebefordran** på den primära routern för GL.iNet-routern om den senare finns bakom NAT.

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Exempel: En TP-Link-router används som primär hemrouter.

    Anslut till hemrouterns Wi-Fi eller LAN. Logga sedan in på webbadministrationspanelen. Kontrollera WAN-IP-adressen som routern får från internetleverantören. I bilden nedan är den offentliga IP-adressen **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Innan du konfigurerar portvidarebefordran rekommenderar vi att du reserverar en IP-adress för GL.iNet-routern på den primära routern så att GL.iNet-routern alltid får en fast IP-adress.** Annars kan den primära routern tilldela GL.iNet-routern en annan IP-adress när någon av routrarna startas om, vilket gör att regeln för portvidarebefordran slutar fungera.

    Konfigurera sedan portvidarebefordran på den primära routern för GL.iNet-routern.

    1. Gå till “Advanced”, klicka på “virtual Server” och sedan på “Add”.

    2. Internal IP (Device IP): IP-adressen som har tilldelats GL.iNet-routern. Du hittar den i TP-Link-routerns klientlista.

    3. External/Internal port: Ange "51820" i båda fälten.

    4. Protocol: Välj "All or UDP or TCP/UDP".

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Fler exempel på [portvidarebefordran](how_to_set_up_port_forwarding.md)**

## Konfigurera WireGuard-servern {#set-up-wireguard-server}

1. Logga in på webbadministrationspanelen och gå till **VPN** -> **WireGuard Server**. Klicka på **Generate Configuration** första gången du konfigurerar VPN-servern.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Kontrollera konfigurationen.

    Standardkonfigurationen nedan fungerar i de flesta fall.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address** är WireGuard-serverns tunnel-IP-adress. Behåll den om den inte krockar med den uppströms routerns gateway.

        Om adresserna krockar väljer du en annan adress, till exempel **10.1.0.1/24**, och klickar sedan på **Apply**. Ta med CIDR-prefixet ”/24” för att undvika anslutningsproblem.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        En uppströms Xfinity-router kan till exempel ha IP-adressen 10.0.0.1. Den adressen kan krocka med tunnel-IP-adressen på vissa GL.iNet-routrar som konfigurerats som WireGuard-server. Ändra bara tunnel-IP-adressen om adresserna krockar.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. IPv6 är inaktiverat som standard på GL.iNet-routrar. Aktivera [IPv6](../interface_guide/ipv6.md) på routern om du vill använda en IPv6-adress.

    - **Listen Port**. WireGuard-servern lyssnar som standard på UDP-port `51820`. Om du byter port och använder portvidarebefordran ska du uppdatera regeln på den uppströms routern så att den vidarebefordrar trafiken till serverns nya lyssningsport. Ange den externa porten i vidarebefordringsregeln i fältet `Endpoint` i varje klientprofil. Om servern kan nås direkt anger du serverns lyssningsport.

    - **Enable Obfuscation**. När alternativet är aktiverat använder VPN-servern AmneziaWG-protokollet för att dölja VPN-trafiken. Vi rekommenderar att du behåller standardinställningarna och bara ändrar dem om du känner till parametrarna.

        - [AmneziaWG-obfuskering på GL.iNet-routrar](../faq/amneziawg_obfuscation.md)
        - [Konfigurera VPN-obfuskering på GL.iNet-routrar](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Lägg till en profil.

    Öppna fliken **Profiles** och klicka på **Add** för att skapa en profil för enheten.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Ge profilen ett beskrivande namn och klicka på **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Klicka vid behov på **Set More** för att visa avancerade inställningar. Klicka sedan på **Apply**.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Lägg till routningsregler vid behov"

        I de flesta fall behöver du inte lägga till routningsregler.

        Om du vill komma åt enheter på WireGuard-klientens LAN från servern öppnar du fliken **Route Rules** på sidan **WireGuard Server** och ställer in reglerna. Följ [instruktionerna för åtkomst till klientens LAN](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Gå annars vidare till steg 4 för att hämta en klientkonfiguration.

4. Hämta konfigurationen.

    När du har lagt till en profil och klickat på **Apply** kan du hämta konfigurationen som QR-kod, oformaterad text eller en nedladdningsbar `.conf`-fil.

    - **QR-kod**. Skanna koden i WireGuard-appen för att importera en vanlig WireGuard-profil. Om du har aktiverat obfuskering använder du AmneziaWG-appen eller en annan klient som har stöd för AmneziaWG-obfuskering.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Oformaterad text**. Granska inställningarna och kopiera dem om du vill konfigurera exempelvis WireGuard-appen eller en GL.iNet-router manuellt.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf-fil**. Klicka på **Download** för att spara filen på enheten. Du kan importera filen direkt i WireGuard-appen eller ladda upp den till en GL.iNet-router.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    Från och med firmware v4.8 kan du välja den offentliga IP-adressen, DDNS-domänen eller den aktuella WAN-IP-adressen som serveradress. Om du ändrar valet uppdateras serveradressen i konfigurationsfilen samtidigt.

    Om nätverkets offentliga IP-adress till exempel ändras ofta aktiverar du [DDNS](../interface_guide/ddns.md) och använder DDNS-domänen som serveradress.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Klicka på **Start** uppe till höger för att starta WireGuard-servern. Anslutningsstatusen visas på samma sida.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Konfigurera WireGuard-klienten {#set-up-wireguard-client}

### Ändra LAN-IP-adressen {#change-the-lan-ip}

I den här guiden används GL-MT6000 och GL-MT3000, vars standard-IP-adress för LAN är **192.168.8.1** på båda modellerna. Därför måste vi ändra LAN-IP-adressen på en av dem för att undvika en konflikt.

Så här ändrar du LAN-IP-adressen på GL-MT3000, som fungerar som WireGuard-klient.

Logga in på webbadministrationspanelen för GL-MT3000 och gå till **NETWORK** -> **LAN**. Ändra LAN-IP-adressen från standardadressen 192.168.8.1 till exempelvis `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Lägg till konfigurationen {#add-the-configuration}

Gå till **VPN** -> **WireGuard Client** på webbadministrationspanelen för GL-MT3000 och klicka på **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Skapa en grupp till vänster och ge den ett namn. Välj sedan konfigurationsfilen som ska laddas upp eller dra den till uppladdningsrutan till höger.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Klicka på **Apply** när filen har verifierats.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Du kan även klicka på **Manually Add Configuration**, klistra in konfigurationstexten och sedan klicka på **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

När konfigurationsfilen har laddats upp visas den på sidan WireGuard Client.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Starta anslutningen {#start-the-connection}

Klicka på ikonen med tre punkter och välj **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Vänta några minuter. När anslutningen har upprättats blir indikatorn grön.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Gå till **VPN Dashboard**. Där visas att klienten är ansluten till servern med hemmets offentliga IP-adress. Sidan kan se något annorlunda ut beroende på firmwareversion.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Logga in igen på webbadministrationspanelen för GL-MT6000 (WireGuard-servern) och gå till **VPN** -> **WireGuard Server** (eller **VPN** -> **VPN Dashboard** om du använder firmware v.4.7 eller tidigare). Där visas även anslutningsstatusen, som anger att klienten är ansluten.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Sidan WireGuard Server i FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(Sidan VPN Dashboard i FW v4.7 och tidigare)</small>

## Förbered fjärråtkomst för framtida VPN-felsökning {#prep-for-remote-vpn-fixes-ahead}

Bind båda routrarna till ditt GoodCloud-konto innan du reser. Då kan du felsöka på distans om VPN-anslutningen slutar fungera på grund av konfigurationen eller andra nätverksproblem. Fjärråtkomst fungerar bara när routrarna är påslagna och anslutna till internet.

---

Relaterade artiklar

- [Konfigurera en WireGuard-server på GL.iNet-routrar](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
