# Det går inte att ansluta till en obfuskerad WireGuard-server {#cannot-connect-to-an-obfuscated-wireguard-server}

VPN-obfuskering är en teknik som döljer VPN-trafik så att den ser ut som vanlig internettrafik. Vissa GL.iNet-routrar stöder för närvarande AmneziaWG-protokollet, så att du kan konfigurera en WireGuard-server med trafikobfuskering aktiverad.

Följ stegen nedan för att felsöka om det inte går att upprätta en anslutning till en obfuskerad WireGuard-server.

1. **Kontrollera att varje klient har en egen importerad WireGuard-konfiguration.**

    Varje klient behöver en unik konfigurationsfil för en peer. Om samma konfiguration delas av flera klienter misslyckas anslutningarna.

    Gå vid behov till **VPN** -> **WireGuard Server** -> **Profiles** för att visa de exporterade profilerna.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Kontrollera att klienten kan verifiera obfuskeringsparametrarna.**

    AmneziaWG-protokollet är bakåtkompatibelt. Om WireGuard-servern endast stöder AmneziaWG v1.0 godkänns konfigurationsfilen fortfarande vid verifiering när den importeras till en klient som stöder v2.0.

    Om konfigurationsfilen innehåller obfuskeringsparametrar för AmneziaWG v2.0 måste du däremot kontrollera att WireGuard-klienten stöder AmneziaWG v2.0. Annars kan parameterverifieringen misslyckas.

    !!! tip "Hur identifierar jag AmneziaWG-versionen?"

        **V1.0**: Inga S3-S4-parametrar. H1-H4 är fasta heltal.

        **V2.0**: Det är V2.0 om något av följande villkor är uppfyllt:

        - Parametrarna S3-S4 ingår
        - H1-H4 är angivna som numeriska intervall
        - Anpassade I1-I5-parametrar ingår.

        > Obs! I1-I5 genereras inte automatiskt. Du kan lägga till dem manuellt som extra rader i konfigurationsfilen för att få AmneziaWG-trafiken att likna andra vanliga protokoll, till exempel QUIC eller WebRTC.

    Om WireGuard-servern är en GL.iNet-router kan du kontrollera dess AmneziaWG-version på följande två sätt.

    ??? note "Kontrollera via routerns webbadministrationspanel"

        1. Logga in på routerns webbadministrationspanel.

        2. Gå till **VPN** -> **WireGuard Server** -> **Configuration** och kontrollera obfuskeringsparametrarna. Om konfigurationen innehåller **S3-S4** eller **H1–H4** som variabla intervall (i stället för fasta värden) kör routern AmneziaWG 2.0, som visas nedan.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            I annat fall använder den AmneziaWG 1.0, som visas nedan.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Kontrollera med ett SSH-kommando"

        1. Logga in på routern via SSH.

        2. Kör `opkg list|grep awg` och kontrollera suffixet för paketet **kmod-amneziawg** i utdata. Om det är märkt med **2.0** stöder routern AmneziaWG 2.0, som visas nedan.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            I annat fall kör den AmneziaWG 1.0, som visas nedan.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Justera obfuskeringsparametrarna.**

    Om du har konfigurerat [obfuskeringsparametrar](amneziawg_obfuscation.md#parameter-overview) (till exempel Jc, Jmin och Jmax) manuellt på WireGuard-servern kan felaktiga parameterinställningar leda till att handskakningen misslyckas.

    Prova att ändra obfuskeringsparametrarna och återansluta för att utesluta att parametrarna inte stämmer överens. Du kan även återställa standardinställningarna för obfuskering för att testa.

4. **Testa anslutningen med den officiella AmneziaWG-appen.**

    Gör ett jämförande test: Installera den officiella Amnezia WG-appen, importera den ursprungliga konfigurationsfilen som exporterades från servern och försök ansluta.

    - Om anslutningen lyckas i den officiella appen är konfigurationsfilen giltig. Problemet kan finnas på den ursprungliga klientenheten. Kontrollera dess nätverksanslutning eller kontakta supporten för mer hjälp.

    - Om anslutningen fortfarande misslyckas kan problemet bero på routerns VPN-serverkonfiguration, nätverksanslutningen eller brandväggsinställningarna. Kontrollera dessa inställningar och obfuskeringsparametrarna.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
