# GoodPAS {#goodpas}

**Obs!** Funktionen introducerades i firmware v4.11 (v4.10 för GL-MG1300), då AstroWarp bytte namn till GoodPAS. Om enheten kör äldre firmware, se [AstroWarp](./astrowarp.md).

---

Öppna **CLOUD SERVICES** -> **GoodPAS** på vänster sida i webbadministrationspanelen.

GoodPAS är en avancerad fjärråtkomstlösning som är integrerad i GL.iNets router-SDK. Den använder AmneziaWG-protokollet med inbyggd trafikobfuskering och ger stabila, säkra anslutningar för tillförlitlig fjärråtkomst.

Funktionen ger smidig fjärråtkomst till hemnätverket. Du kan konfigurera och parkoppla enheter direkt med en dynamisk åtkomstkod i webbadministrationspanelen och snabbt upprätta en säker anslutning mellan reseroutern och hemnätverket utan registrering eller inloggning.

**Note**:

1. GoodPAS bör inte användas samtidigt med följande funktioner eftersom routningskonflikter kan uppstå: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, Tailscale och Tor.

2. Network Mode kan inte användas när GoodPAS är aktiverat.

3. När GoodPAS är aktiverat har tjänsten högst routningsprioritet och kan inte kaskadkopplas med VPN Client.

    Om Router A och Router B upprättar ett GoodPAS-nätverk med Router B som utgångsnod går trafik som vidarebefordras via GoodPAS ut på internet via Router B:s offentliga WAN-IP, även om VPN Client är aktiverad på Router B. Trafiken vidarebefordras inte genom VPN Client-tunneln på Router B.

## Quick Setup {#quick-setup}

I följande exempel använder vi **Flint 3(GL-BE9300)** och **Mango 2(GL-MG1300)** för att konfigurera ett GoodPAS-nätverk.

Flint 3 fungerar som hemrouter, medan Mango 2 fungerar som reserouter och dirigerar nätverkstrafiken tillbaka till Flint 3 för internetåtkomst.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Configure Flint 3 for Internet.

    Logga in på webbadministrationspanelen för Flint 3 och öppna sidan INTERNET. Anslut routern till internet med Ethernet, Repeater, Tethering eller Cellular.

    As shown below, the Flint 3 home router is connected to the ISP modem (Hong Kong Broadband Network Ltd) via an Ethernet cable.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Generate Access Code.

    On the Flint 3's web admin panel, navigate to **CLOUD SERVICES** -> **GoodPAS**. Click **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    It will generate an Access Code. Copy this code for later use.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Configure Mango 2 for Internet.

    Logga in på webbadministrationspanelen för Mango 2 och öppna sidan INTERNET. Anslut routern till internet med Ethernet, Repeater, Tethering eller Cellular.

    I exemplet nedan är reseroutern Mango 2 ansluten till en personlig hotspot på en iPhone 17 i Shenzhen via nätverket China Unicom Guangdong Province.

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Enter Access Code.

    On the Mango 2's web Admin Panel, navigate to **CLOUD SERVICES** -> **GoodPAS**. Click **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Enter the Access Code obtained in Step 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Wait for the verification to complete.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    Anslutningen till hemroutern Flint 3 upprättas. Du kan nu använda internet säkert via hemnätverket.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    On the Flint 3's web Admin Panel, it also displays the connection status, as shown below.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Test Connectivity {#test-connectivity}

1. Anslut en bärbar dator eller smartphone till Wi-Fi-nätverket på reseroutern Mango 2.

2. Open a browser and visit [ipcheck.ing](https://ipcheck.ing/){target="_blank"} or any other IP address lookup website.

    Den offentliga IP-adressen för Flint 3 visas, vilket anger att Mango 2 använder internet via hemroutern Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Koppla från GoodPAS-anslutningen på Mango 2 och uppdatera sedan webbsidan för att skicka IP-frågan igen.

    Den offentliga IP-adressen för Mango 2 visas, vilket anger att Mango 2 använder internet via sitt lokala nätverk.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ {#faq}

1. **Q: What is the format of the dynamic access code, and how long is it valid?**

    A: It is an 8-character code combining numbers and uppercase letters, valid for 10 minutes.

2. **Q: What happens to the travel router if I terminate the connection on the home router?**

    S: Reseroutern kopplas från och väntar utan nätverksåtkomst. När hemroutern återansluts kan reseroutern automatiskt ansluta igen utan att åtkomstkoden anges på nytt.

3. **Q: In what scenarios will the travel router enter pending state?**

    S: Reseroutern övergår till vänteläge när något av följande gäller för hemroutern:

    - Terminates the GoodPAS connection
    - Loses internet access

4. **Q: What does the Reset button in the top right corner do?**

    S: Alla behöriga enheter rensas och sidan för val av routerroll visas igen.

5. **Q: What happens to the travel router if I reset the GoodPAS on the home router?**

    S: När hemroutern återställs kopplas fjärranslutna enheter från GoodPAS-nätverket och återgår till sina lokala nätverk för internetåtkomst.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
