# AstroWarp {#astrowarp}

**Obs!** Guiden gäller den nya versionen av AstroWarp. Funktionen bytte namn till [GoodPAS](./goodpas.md) i firmware v4.11 (v4.10 för GL-MG1300).


Nya AstroWarp är integrerat i GL.iNets router-SDK. Det använder AmneziaWG-protokollet med inbyggd trafikobfuskering och ger stabila, säkra anslutningar för tillförlitlig fjärråtkomst.

Funktionen ger smidig fjärråtkomst till hemnätverket. Du kan konfigurera och parkoppla enheter direkt med en dynamisk åtkomstkod i webbadministrationspanelen och snabbt upprätta en säker anslutning mellan reseroutern och hemnätverket utan registrering eller inloggning.

Äldre AstroWarp visas i webbadministrationspanelen men använde en fristående AstroWarp-plattform för fjärrnätverksanslutningar. Dokumentation om äldre AstroWarp finns [här](https://docs.astrowarp.net/){target="_blank"}.

**Note:**

1. AstroWarp bör inte användas samtidigt med följande funktioner eftersom routningskonflikter kan uppstå: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, Tailscale och Tor.

2. Network Mode kan inte användas när AstroWarp är aktiverat.

3. När AstroWarp är aktiverat har tjänsten högst routningsprioritet och kan inte kaskadkopplas med VPN Client.

    Om Router A och Router B upprättar ett AstroWarp-nätverk med Router B som utgångsnod går trafik via AstroWarp ut på internet genom Router B:s offentliga WAN-IP, även om VPN Client är aktiverad på Router B. Trafiken vidarebefordras inte genom VPN Client-tunneln på Router B.

## Supported Models {#supported-models}

??? "Supported Models"

    Modellerna är kompatibla med nya AstroWarp. Listan över modeller som stöder äldre AstroWarp finns [här](https://docs.astrowarp.net/en/quick_start/){target="_blank"}.

    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-MG1300 (Mango 2)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-X2000 (Spitz Plus)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)
    - ※GL-MT2500/GL-MT2500A (Brume 2)

    **Note**: Models marked with ※ support the integrated AstroWarp in Beta firmware.

??? "Unsupported Models"

    Enheterna är inte kompatibla med nya AstroWarp, men vissa modeller fungerar fortfarande med den äldre versionen. Mer information finns [här](https://docs.astrowarp.net/en/quick_start/){target="_blank"}.

    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-B3000 (Marble)
    - GL-A1300 (Slate Plus)
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
    - GL-X300B (Collie)

## Quick Setup {#quick-setup}

I följande exempel använder vi **Flint 3 (GL-BE9300)** och **Slate 7 (GL-BE3600)** för att konfigurera ett AstroWarp-nätverk.

Flint 3 fungerar som hemrouter, medan Slate 7 fungerar som reserouter och dirigerar nätverkstrafiken tillbaka till Flint 3 för internetåtkomst.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

1. Configure Flint 3 for Internet.

    Logga in på webbadministrationspanelen för Flint 3 och öppna **INTERNET**. Anslut routern till internet med Ethernet, Repeater, Tethering eller Cellular.

    As shown below, the Flint 3 home router is connected to the ISP modem (Hong Kong Broadband Network Ltd) via an Ethernet cable.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Generate Access Code.

    On the Flint 3's web admin panel, navigate to **CLOUD SERVICES** -> **AstroWarp**. Click **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    It will generate an **Access Code**. Copy this code for later use.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configure Slate 7 for Internet.

    Logga in på webbadministrationspanelen för Slate 7 och öppna **INTERNET**. Anslut routern till internet med Ethernet, Repeater, Tethering eller Cellular.

    I exemplet nedan är reseroutern Slate 7 ansluten till en personlig hotspot på en iPhone 15 Pro i Shenzhen via nätverket China Unicom Guangdong Province.

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Enter Access Code.

    On the Slate 7's web admin panel, navigate to **CLOUD SERVICES** -> **AstroWarp**. Click **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Enter the Access Code obtained in Step 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Wait for the verification to complete.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    Anslutningen till hemroutern Flint 3 upprättas. Du kan nu använda internet säkert via hemnätverket.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    On the Flint 3's web admin panel, it also displays the connection status, as shown below.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Test Connectivity {#test-connectivity}

1. Anslut en bärbar dator eller smartphone till Wi-Fi-nätverket på reseroutern Slate 7.

2. Open a browser and visit [ipcheck.ing](https://ipcheck.ing/){target="_blank"} or any other IP address lookup website.

    Den offentliga IP-adressen för Flint 3 visas, vilket anger att Slate 7 använder internet via hemroutern Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Koppla från AstroWarp-anslutningen på Slate 7 och uppdatera webbsidan för att skicka IP-frågan igen.

    Den offentliga IP-adressen för Slate 7 visas, vilket anger att Slate 7 använder internet via sitt lokala nätverk.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## FAQ {#faq}

1. **Q: What is the format of the dynamic access code, and how long is it valid?**

    A: It is an 8-character code combining numbers and uppercase letters, valid for 10 minutes.

2. **Q: What happens to the travel router if I terminate the connection on the home router?**

    S: Reseroutern kopplas från och väntar utan nätverksåtkomst. När hemroutern återansluts kan reseroutern automatiskt ansluta igen utan att åtkomstkoden anges på nytt.

3. **Q: In what scenarios will the travel router enter pending state?**

    S: Reseroutern övergår till vänteläge när något av följande gäller för hemroutern:

    - Terminates the AstroWarp connection
    - Loses internet access

4. **Q: What does the Reset button in the top right corner do?**

    S: Alla behöriga enheter rensas och sidan för val av routerroll visas igen.

5. **Q: What happens to the travel router if I reset the AstroWarp on the home router?**

    S: När hemroutern återställs kopplas fjärranslutna enheter från AstroWarp-nätverket och återgår till sina lokala nätverk för internetåtkomst.

6. **Q: If I have enabled the new AstroWarp in the router's web Admin Panel, how do I disable it and switch back to the legacy AstroWarp?**

    S: Öppna **CLOUD SERVICES** -> **AstroWarp** i routerns webbadministrationspanel och klicka på **Reset** uppe till höger.

    ![reset](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/reset.png){class="glboxshadow"}

    Logga sedan in på [astrowarp.net](https://my.astrowarp.net/#/login){target="_blank"} med molnkontot. Klicka på **"+"** efter inloggning för att lägga till routern i AstroWarp-nätverket.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/add_device.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
