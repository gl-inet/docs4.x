# DPI Engine

**Hinweis**: Diese Funktion wurde mit Firmware v4.9 eingeführt.

Einige Modelle, darunter Mango 2 (GL-MG1300), unterstützen DPI Engine wegen unzureichenden Speichers auch mit Firmware v4.9 oder höher nicht. Weitere Informationen finden Sie unter [Unterstützte Modelle](#supported-models).

---

DPI (Deep Packet Inspection) ist eine Kerntechnologie für intelligentes Netzwerkmanagement. Im Gegensatz zu herkömmlichen Routern, die nur Quell- und Zieladressen identifizieren, analysiert DPI Paketnutzdaten eingehend und erkennt mithilfe einer Signaturbibliothek Anwendungen und Websites präzise. Dadurch wird eine fein granulare Klassifizierung und Steuerung des Datenverkehrs ermöglicht.

Die GL.iNet DPI Engine läuft lokal auf Ihrem Router und bietet intelligentes Netzwerkmanagement bei voller Privatsphäre. Sie ermöglicht umfassenden Zugriff auf Datenstatistiken, Inhaltsfilter und QoS für eine vollständige Verkehrssteuerung.

Integriert mit [Netify](https://www.netify.ai/){target="_blank"} nutzt GL.iNet DPI ein leichtgewichtiges Embedded-Plug-in für eine effiziente Bereitstellung. Mit der online aktualisierten Netify-Signaturdatenbank wird die Netzwerksteuerung präziser und zuverlässiger.

**Hinweis**:

1. Wenn sich der Router im Drop-in Gateway-Modus befindet, wirken DPI-Funktionen (einschließlich Datenstatistiken, Inhaltsfilter und QoS) sowie SQM nicht.

2. Wenn DPI aktiviert ist, wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle {#supported-models}

??? "Unterstützte Modelle"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Nicht unterstützte Modelle"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)


## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **DPI Engine** und klicken Sie auf **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/de/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

Lesen Sie im Pop-up-Fenster die Nutzungsbedingungen und die Datenschutzrichtlinie, stimmen Sie ihnen zu und klicken Sie dann auf **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/de/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Bitte warten Sie, während der Router Systemvorgänge ausführt. Dabei werden die Netzwerkbeschleunigung deaktiviert sowie Datenstatistiken und Inhaltsfilter aktiviert.

![activate 2](https://static.gl-inet.com/docs/router/de/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Klicken Sie nach der Aktivierung auf **Done**.

![activated](https://static.gl-inet.com/docs/router/de/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Sie werden zum **DPI Engine Version Center** weitergeleitet, wo Sie die DPI-Programmversion und die Datenbankversion einsehen können.

![dpi version center](https://static.gl-inet.com/docs/router/de/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Hinweis**: Diese Seite zeigt nur Statusindikatoren des Kernsystems an. Die Verkehrsverarbeitung beginnt erst, wenn die jeweiligen Funktionen aktiviert werden.

## Datenbank-Upgrade

Wenn eine neuere Datenbankversion verfügbar ist, klicken Sie einfach auf **Upgrade**, um die Datenbank zu aktualisieren.

![database upgrade](https://static.gl-inet.com/docs/router/de/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
