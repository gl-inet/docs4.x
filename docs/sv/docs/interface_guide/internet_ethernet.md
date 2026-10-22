# Anslut till internet via en Ethernet-kabel {#connect-to-the-internet-via-an-ethernet-cable}

Anslut routern till ett bredbandsnätverk med en Ethernet-kabel i WAN-porten. Routern hämtar vanligtvis en IP-adress automatiskt via DHCP. Du kan även konfigurera statisk IP eller PPPoE manuellt. Metoden ger hög stabilitet och hastighet och passar hem och kontor med fast bredbandsanslutning.

Följ stegen nedan för att ansluta routern till internet via en Ethernet-kabel.

1. Anslut routerns WAN-port till den uppströms enheten (t.ex. ett modem från internetleverantören, en router, nätverksswitch eller ett Ethernet-uttag) med en Ethernet-kabel.

2. Log in to the router's web admin panel, navigate to **INTERNET** -> **Ethernet** section.

    När anslutningen har upprättats visar avsnittet Ethernet nätverksinformation, däribland Protocol, IP Address, Gateway och DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Tips!** Du kan ändra WAN-portens roll till LAN vid behov. Det är användbart när routern används som [repeater](internet_repeater.md), eftersom den fysiska WAN-porten då är ledig. Om WAN ändras till LAN får du ytterligare en LAN-port.

## Protocol {#protocol}

Det finns tre protokolltyper: DHCP, Static och PPPoE. Klicka på **Modify** för att ändra.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP är standardprotokollet och det vanligaste protokollet. Det tilldelar automatiskt IP-adresser och andra kommunikationsparametrar till nätverksenheter via en klient-serverarkitektur i IP-nätverk.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static krävs om internetleverantören tillhandahåller en fast IP-adress eller om du vill konfigurera nätverksinformation som IP address, Gateway och Netmask manuellt.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE används av många internetleverantörer. De tillhandahåller vanligtvis ett modem samt användarnamn och lösenord som krävs för internetkonfigurationen.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Advanced {#advanced}

Utöver de grundläggande inställningarna finns valfria avancerade inställningar för de tre protokollen.

* **VLAN ID**: Inställningen krävs endast om leverantörens server kräver att gränssnittet använder ett visst taggat VLAN ID.

* **TTL**: TTL (Time To Live) anger den maximala tid som paket kan finnas kvar i nätverket. Som standard minskar routern TTL för inkommande paket från klientenheter med 1 innan de vidarebefordras. TTL-inställningen gäller endast IPv4.

    **Obs!** Om du behöver åsidosätta eller förfalska TTL anger du ett fast värde här. På de flesta modeller anger du önskad effektiv TTL plus 1 för att kompensera för den automatiska minskningen. Mudi 7 (GL‑E5800) använder det angivna värdet utan ändring.

* **HL**: I IPv6 begränsar fältet HL (Hop Limit) antalet överföringshopp för datapaket i nätverket och motsvarar TTL i IPv4.

* **MTU**: The default MTU value is 1500 bytes.

## Ethernet Port {#ethernet-port}

Klicka på kugghjulsikonen i det övre högra hörnet för att öppna [Ethernet Port](ethernet_port.md) och hantera routerns Ethernet-portar.

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

Sidan **WAN** visar portrollen (WAN eller LAN), MAC-läge och MAC-adress samt nätverksportens förhandlade hastighet.

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

Sidan **LAN** visar portrollen och nätverksportens förhandlade hastighet.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/lan.png){class="glboxshadow"}

Please refer to [Ethernet Port](ethernet_port.md) for details.

## Troubleshooting {#troubleshooting}

Om en Ethernet-kabel är ansluten till WAN-porten men internet inte är tillgängligt visas ett gult meddelande enligt bilden nedan.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

To fix this issue:

1. Kontrollera om den uppströms enheten har internetåtkomst.

2. Go to [Multi-WAN](multi-wan.md) page to check the Ethernet interface status.

---

Related Articles

- [Internet page](internet.md)
- [Ange prioriteten för varje internetanslutningsmetod](multi-wan.md)
- [Ange lastbalansering när flera internetanslutningsmetoder används samtidigt](multi-wan.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
