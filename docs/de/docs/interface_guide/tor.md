# Tor

Tor (abgeleitet von **The Onion Router**) ist eine kostenlose Open-Source-Software, die anonyme Kommunikation ermöglicht. Sie hilft Benutzern, das Internet mit mehr Privatsphäre zu nutzen. [Mehr über Tor erfahren](https://www.torproject.org/){target="_blank"}.

**Hinweis**: Diese Funktion befindet sich derzeit in der Beta-Phase und kann in einigen Ländern problematisch sein. Wenn Tor aktiviert ist, funktionieren die folgenden Funktionen nicht ordnungsgemäß:

  - VPN
  - DNS
  - IPv6
  - ADGuard Home.

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Hinweis**: Mit * markierte Modelle unterstützen Tor nicht nativ, Benutzer können Tor jedoch manuell über ein Plug-in installieren. Klicken Sie [hier](#manuelle-installation) für Details.

??? "Nicht unterstützte Modelle"
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **VPN** -> **Tor**.

Bei Firmware-Version 4.8.4 und höher gehen Sie zu **APPLICATIONS** -> **Tor**.

Klicken Sie auf den Umschalter, um Tor zu aktivieren, aktivieren Sie bei Bedarf **Custom Exit Nodes**, und klicken Sie dann auf **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/enable_tor.png){class="glboxshadow"}

Der Verbindungsaufbau startet anschließend. Wenn Ihr Netzwerk die Anforderungen erfüllt, wird „connected“ angezeigt.

![tor connected](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/connected.png){class="glboxshadow" width="672"}

## Manuelle Installation

**Hinweis**: Auf einigen Modellen kann Tor manuell über ein Plug-in installiert werden, dies kann jedoch die CPU-Last erhöhen und die Reaktionsgeschwindigkeit des Systems verringern.

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **APPLICATIONS** -> **Plug-ins**.

Suchen Sie nach **gl-sdk4-ui-torview** und installieren Sie es.

![torview](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torpage.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
