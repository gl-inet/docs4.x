# Netzwerkbeschleunigung

Die Netzwerkbeschleunigung reduziert die CPU-Last und beschleunigt die Weiterleitung von Datenpaketen, kann jedoch mit einigen Funktionen in Konflikt geraten.

Wenn die Netzwerkbeschleunigung aktiviert ist, funktionieren die folgenden Funktionen nicht korrekt: **Client Speed and Traffic Statistics**, **Client Speed Limit**.

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
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Nicht unterstützte Modelle"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Einrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **Network Acceleration**.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Es gibt drei Modi.

- **Auto**

    Im Modus „Auto“ wird je nach tatsächlicher Nutzung automatisch zwischen den beiden Beschleunigungsmodi umgeschaltet.

- **Hardware Acceleration**

    Hardwarebeschleunigung funktioniert bei <u>Ethernet</u> und <u>Repeater</u>.

    Hardwarebeschleunigung lagert häufige Netzwerkaufgaben (z. B. NAT, Paketweiterleitung, Prüfsummenprüfung) auf dedizierte Hardware wie NPUs oder HWNAT-Chips aus. Sie arbeitet speziell mit Ethernet- (kabelgebundenem WAN/LAN) und Repeater-Verbindungen und ist in diesen Szenarien mit festen Pfaden und einfachen Regeln besonders leistungsfähig. Dadurch werden hoher Durchsatz, geringe Latenz und eine minimale CPU-Last für Datenübertragung mit Leitungsgeschwindigkeit erreicht.

- **Software Acceleration**

    Softwarebeschleunigung funktioniert bei <u>Cellular</u>.

    Softwarebeschleunigung nutzt die allgemeine CPU des Routers zusammen mit optimierten Kerneln oder Treibern (z. B. SWNAT). Sie arbeitet bei **Cellular**-Zugängen (4G/5G), typischerweise in Szenarien, in denen keine Hardwarebeschleunigung verfügbar ist, und bietet dabei hohe Kompatibilität sowie Unterstützung für komplexe Protokolle. Sie ist flexibel, kann jedoch bei hoher Bandbreitenlast an CPU-Grenzen stoßen, insbesondere wenn erweiterte Funktionen wie DPI, QoS oder Port Forwarding aktiv sind.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
