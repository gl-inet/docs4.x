# OpenVPN: TCP jämfört med UDP {#openvpn-tcp-vs-udp}

OpenVPN-servern på en GL.iNet-router stöder både TCP- och UDP-protokollet. Vad är skillnaden?

TCP är mer tillförlitligt men långsammare. UDP är snabbare men mindre tillförlitligt.

Om ett program behöver låg latens och kontinuerlig dataöverföring för att fungera korrekt är UDP ett bättre val. I andra fall är TCP ett tillförlitligt protokoll för dataöverföring utan förlust under överföringen.

UDP passar bättre för spel, strömning och VoIP-tjänster. TCP passar bättre för e-post, webbsurfning och filöverföring.

Vi rekommenderar att du provar UDP-protokollet först och endast byter till TCP om anslutningen är instabil, paket förloras eller andra tillförlitlighetsproblem uppstår.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
