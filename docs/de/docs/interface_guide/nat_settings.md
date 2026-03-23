# NAT-Einstellungen

Diese Funktion ist seit v4.5.16 verfügbar.

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **NAT Settings**.

Auf dieser Seite können Sie **Full Cone NAT** aktivieren, um die Stabilität von Peer-to-Peer-Verbindungen für Anwendungen wie Gaming oder Streaming zu verbessern, sowie **SIP ALG**, um Kompatibilitätsprobleme mit VoIP-/SIP-basierten Telefondiensten zu beheben.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-X300B (Collie)
    - ※GL-SFT1200 (Opal)
    - ※GL-E750/E750V2 (Mudi)

    **Hinweis**: GL-SFT1200 (Opal) und GL-E750/E750V2 (Mudi) unterstützen diese Funktion ab Firmware v4.7.

??? "Nicht unterstützte Modelle"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT

Full Cone NAT fungiert als „direkte Abkürzung“ für Geräte wie Spielkonsolen oder Smartphones, wenn sie online Verbindungen zu anderen Geräten aufbauen, zum Beispiel in Multiplayer-Spielen oder Videoanrufen.

Indem externe Geräte lokale Geräte direkt über den Router erreichen können, anstatt sie hinter mehreren Ebenen zu verbergen, verbessert diese Funktion die Stabilität von Peer-to-Peer-Verbindungen (P2P), reduziert die Latenz und behebt Verbindungsfehler in P2P-Anwendungen.

**Hinweis**: Das Aktivieren dieser Funktion kann die Sicherheit im Vergleich zu anderen NAT-Typen verringern, da Geräteports dem öffentlichen Netzwerk stärker offengelegt werden.

## SIP ALG

SIP ALG (Application Layer Gateway) fungiert als „Übersetzer“ des Routers für VoIP-/SIP-basierte Kommunikationsdienste, zum Beispiel Bürotelefone oder anwendungsbasierte Anrufe.

Es wurde entwickelt, um Herausforderungen bei der NAT-Durchquerung zu lösen. Dazu passt es Anrufdaten an, damit sie reibungslos mehrere NAT-Ebenen passieren können — ein häufiges Szenario in Netzwerken mit mehreren Routern (z. B. einem Hauptrouter und einem GL.iNet-Router). So werden Konflikte reduziert und Gesprächsabbrüche verhindert.

**Hinweis**: Ein inkompatibles oder schlecht implementiertes SIP ALG kann die Gesprächsqualität verschlechtern und zu Problemen wie einseitiger Audioübertragung, nicht reagierendem Klingeln, abgebrochenen Anrufen oder direkt an die Voicemail weitergeleiteten Anrufen führen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
