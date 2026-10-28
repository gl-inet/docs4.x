# UPnP {#upnp}

**Obs!**: Den här funktionen infördes i firmware v4.11.

---

Gå till **SECURITY** -> **UPnP** till vänster i webbadministrationspanelen.

UPnP (Universal Plug and Play) låter kompatibla LAN-enheter och program automatiskt begära portmappningar på GL.iNet-routrar. Mappningarna vidarebefordrar inkommande WAN-trafik till angivna LAN-IP-adresser och portar, så att externa klienter kan ansluta till lokala tjänster utan manuellt konfigurerade regler för portvidarebefordran.

UPnP skiljer sig från [portvidarebefordran](./port_forwarding.md) och [DMZ](./port_forwarding.md#dmz): UPnP skapar mappningar automatiskt på begäran av enheter. Portvidarebefordran exponerar valda portar, medan DMZ exponerar alla portar på en LAN-värd. Både portvidarebefordran och DMZ kräver manuell konfiguration. Se till att du förstår hur funktionerna fungerar och vilka säkerhetsrisker de medför innan du aktiverar dem.

**Obs!**: 

1. När UPnP är aktiverat kan kompatibla LAN-enheter och program begära portmappningar utan godkännande för varje begäran.

2. En komprometterad enhet eller ett skadligt program kan använda UPnP för att exponera lokala tjänster på internet. Aktivera UPnP endast i betrodda nätverk och inaktivera det när det inte behövs.

3. UPnP kräver en offentlig IP-adress på routerns WAN-gränssnitt för att acceptera inkommande anslutningar från internet. Det fungerar inte om din internetleverantör använder CGNAT.

Vanliga användningsområden för UPnP är:

- **Onlinespel**: kompatibla spel och konsoler (t.ex. Steam-spel för flera spelare, Xbox Series X|S, PlayStation 5, Nintendo Switch) kan automatiskt skapa portmappningar för att underlätta anslutningar till andra spelare.

- **Peer-to-peer-fildelning**: BitTorrent-klienter och andra kompatibla P2P-program kan automatiskt mappa lyssningsportar för att acceptera inkommande anslutningar från andra deltagare.

- **Fjärråtkomst**: enheter och program som stöder UPnP-portmappning, exempelvis vissa NAS-enheter, IP-kameror och medieservrar, kan automatiskt konfigurera mappningar för åtkomst utanför det lokala nätverket.

## Snabbkonfiguration {#quick-setup}

Aktivera UPnP med reglaget. Kompatibla enheter och program kan sedan begära portmappningar efter behov, som i exemplet nedan.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- Client / Application: beskrivningen av klienten eller programmet och den begärande enhetens LAN-IP-adress.

- Protocol: mappningens transportprotokoll, t.ex. TCP eller UDP.

- External Port: WAN-porten för inkommande anslutningar.

- Internal Target: LAN-IP-adress och port för målet.

- Lease: återstående tid innan mappningen upphör. Standardlånetiden är 7 dagar.

- Action: klicka på papperskorgsikonen för att ta bort mappningen. Klienten eller programmet kan begära den igen om det fortfarande körs.

Aktiva portmappningar tas bort när klienten frigör dem eller deras lånetid löper ut. Klicka på **Refresh** för att visa de senaste portmappningarna.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

Har du fler frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
