# DPI Engine

DPI (Deep Packet Inspection) ist eine Kerntechnologie für intelligentes Netzwerkmanagement. Im Gegensatz zu herkömmlichen Routern, die nur Quell- und Zieladressen identifizieren, analysiert DPI Paketnutzdaten eingehend und erkennt mithilfe einer Signaturbibliothek Anwendungen und Websites präzise. Dadurch wird eine fein granulare Klassifizierung und Steuerung des Datenverkehrs ermöglicht.

Die GL.iNet DPI Engine läuft lokal auf Ihrem Router und bietet intelligentes Netzwerkmanagement bei voller Privatsphäre. Sie ermöglicht umfassenden Zugriff auf Datenstatistiken, Inhaltsfilter und QoS für eine vollständige Verkehrssteuerung.

Integriert mit [Netify](https://www.netify.ai/){target="_blank"} nutzt GL.iNet DPI ein leichtgewichtiges Embedded-Plug-in für eine effiziente Bereitstellung. Mit der online aktualisierten Netify-Signaturdatenbank wird die Netzwerksteuerung präziser und zuverlässiger.

**Hinweis**:

1. Wenn sich der Router im Drop-in Gateway-Modus befindet, wirken DPI-Funktionen (einschließlich Datenstatistiken, Inhaltsfilter und QoS) sowie SQM nicht.

2. Wenn DPI aktiviert ist, wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle

!!! note "Unterstützte Modelle"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **DPI Engine** und klicken Sie auf **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

Lesen Sie im Pop-up-Fenster die Nutzungsbedingungen und die Datenschutzrichtlinie, stimmen Sie ihnen zu und klicken Sie dann auf **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Bitte warten Sie, während der Router Systemvorgänge ausführt. Dabei werden die Netzwerkbeschleunigung deaktiviert sowie Datenstatistiken und Inhaltsfilter aktiviert.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Klicken Sie nach der Aktivierung auf **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Sie werden zum **DPI Engine Version Center** weitergeleitet, wo Sie die DPI-Programmversion und die Datenbankversion einsehen können.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Hinweis**: Diese Seite zeigt nur Statusindikatoren des Kernsystems an. Die Verkehrsverarbeitung beginnt erst, wenn die jeweiligen Funktionen aktiviert werden.

## Datenbank-Upgrade

Wenn eine neuere Datenbankversion verfügbar ist, klicken Sie einfach auf **Upgrade**, um die Datenbank zu aktualisieren.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
