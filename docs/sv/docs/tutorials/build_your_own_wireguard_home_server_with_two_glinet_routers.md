# Bygg en egen WireGuard-hemmaserver med två GL.iNet-routrar {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Den här artikeln visar hur du konfigurerar hemroutern som WireGuard VPN-server och reseroutern som WireGuard VPN-klient för fjärranslutning. På så sätt kan du använda hemmets IP-adress med reseroutern var du än befinner dig.

Titta på videon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(I videon används GL-MT5000 (Brume 3) och GL-MT3600BE (Beryl 7) för att demonstrera VPN-konfigurationen.)</small>

I följande steg används GL-MT6000 (Flint 2) och GL-MT3000 (Beryl AX) som exempel:

- GL-MT6000, som är hemrouter, konfigureras som WireGuard VPN-server. Om trådlös kapacitet inte behövs kan du även använda säkerhetsgatewayen GL-MT2500 eller andra modeller.

- GL-MT3000, som är reserouter, konfigureras som WireGuard VPN-klient och ansluter på distans till VPN-servern hemma.

## Därför kan du behöva en egen WireGuard-hemmaserver {#why-you-need-to-build-your-own-wireguard-home-server}

1. Använd hemmets IP-adress som internetadress, som om du befann dig hemma.
2. Undvik månadsavgiften för en VPN-tjänst från tredje part.
3. Dirigera all internettrafik till hemnätverket genom en krypterad VPN-tunnel och skydda din integritet.
4. Få enkel åtkomst till interna resurser och lokala strömningstjänster.

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

    Gör så här:

    1. Logga in på GL.iNet-administrationspanelen.

    2. Välj INTERNET i det vänstra sidofältet. Kontrollera topologin och anslutningsinformationen:

        Vid direkt Ethernet-anslutning visas ett avsnitt som heter "Ethernet" med uppgifter som Protocol, IP address och Gateway.

        I följande bild är den markerade IP Address den WAN-IP-adress som internetleverantören har tilldelat GL.iNet-routern.

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        WAN-IP-adressen är offentlig. GL.iNet-routern fungerar därmed som primär router, har en offentlig IP-adress och **behöver ingen portvidarebefordran**.

        Konfigurera bara GL.iNet-routern som WireGuard-server och en reserouter som WireGuard-klient som ansluter till servern. En VPN-tunnel upprättas då mellan dem.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet som sekundär router"

    Konfigurera **portvidarebefordran** på den primära routern för GL.iNet-routern om den senare finns bakom NAT.

    Topologi

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

### Aktivera DDNS (valfritt) {#enable-ddns-optional}

Aktivera DDNS om du har en dynamisk offentlig IP-adress i stället för en statisk offentlig IP-adress.

Logga in på webbadministrationspanelen för GL-MT6000 och gå till **APPLICATIONS** -> **Dynamic DNS**. Aktivera reglaget **Enable DDNS**.

Markera kryssrutan **Terms of Service & Privacy Policy** och klicka på **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Gå sedan till fliken **WireGuard Server** -> Configuration, kontrollera att Listen Port är 51820 och klicka på **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Skapa konfigurationen {#generate-configuration}

Klicka på fliken **Profiles** bredvid Configuration på samma sida och klicka sedan på **Add** (markerat med 1 i bilden nedan).

En klientkonfiguration skapas automatiskt. Klicka på **framåtpilen** (markerad med 2).

Aktivera DDNS Domain i popup-fönstret (markerat med 3). Detta är valfritt och ska endast aktiveras om du har en dynamisk offentlig IP-adress.

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Du kan sedan skanna QR-koden med WireGuards [mobilapp](https://www.wireguard.com/install/) för att testa servern. Klicka [här](../interface_guide/wireguard_server.md#check-if-wireguard-server-is-working-properly) för mer information.

Du kan även exportera en konfiguration i textformat för VPN-klientanslutningen.

Byt från QR-kod till textformat genom att klicka på fliken **Configuration File**.

Kopiera klienttexten eller klicka på Download och spara filen för senare användning.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Konfigurera WireGuard-klienten {#set-up-wireguard-client}

### Ändra LAN-IP-adressen {#change-the-lan-ip}

I den här guiden används GL-MT6000 och GL-MT3000, vars standard-IP-adress för LAN är **192.168.8.1** på båda modellerna. Därför måste vi ändra LAN-IP-adressen på en av dem för att undvika en konflikt.

Så här ändrar du LAN-IP-adressen för GL-MT3000 (WireGuard-klienten).

Logga in på webbadministrationspanelen för GL-MT3000 och gå till **NETWORK** i det vänstra sidofältet -> **LAN** för att ändra LAN-IP-adressen. Du kan till exempel ändra den från standardadressen 192.168.8.1 till `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Mer information om LAN-gränssnittet finns [här](../interface_guide/lan.md).

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

Bind båda routrarna till ditt GoodCloud-konto i förväg så att du kan felsöka VPN-anslutningen på distans om oväntade problem uppstår när du reser.

Servern kan ibland sluta fungera på grund av ett strömavbrott eller andra orsaker. Bind den till GL.iNet GoodCloud för att behålla fjärråtkomsten till servern.

---

Relaterade artiklar

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
