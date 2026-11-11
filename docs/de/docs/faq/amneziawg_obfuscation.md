# AmneziaWG-Verschleierungsparameter {#amneziawg-obfuscation}

AmneziaWG ist ein WireGuard-basiertes VPN-Protokoll mit integrierter Verschleierung des Datenverkehrs. Seine Verschleierungsparameter steuern, wie der Datenverkehr getarnt wird, um einer Erkennung durch strenge Netzwerkinspektion zu entgehen.

Nachfolgend finden Sie eine Einführung in AmneziaWG und die Unterschiede zwischen den Versionen.

## Warum AmneziaWG? {#why-amneziawg}

Der Vorgänger von AmneziaWG, WireGuard, hat sich dank seines kompakten Codebestands und seiner hohen Effizienz als schnelles und zuverlässiges VPN-Protokoll etabliert. Seine festen Paket-Header und vorhersagbaren Paketgrößen erzeugen jedoch ein leicht erkennbares Signaturmuster. DPI-Systeme können diese Pakete mühelos identifizieren und Verbindungen sofort beenden – ein kritisches Problem in Ländern mit strenger Internetzensur.

AmneziaWG übernimmt die architektonische Einfachheit und hohe Leistung der ursprünglichen WireGuard-Implementierung und ergänzt sie um ein eigenes Verschleierungsmodul, das VPN-Datenverkehrsmuster verbirgt. Dadurch können Privat- und Geschäftsanwender ihre Online-Privatsphäre schützen und auch in restriktiven Netzwerkumgebungen stabile Verbindungen aufrechterhalten.

Kurz gesagt:

- Es maskiert VPN-Merkmale, um eine Erkennung durch ISPs, Firewalls oder Deep Packet Inspection (DPI) zu verhindern.
- Es lässt Ihre VPN-Verbindung wie gewöhnlichen Web-Datenverkehr erscheinen, was die Verbindungsstabilität und Erfolgsquote in eingeschränkten Netzwerken verbessert.

## AmneziaWG V2.0 {#amneziawg-v20}

### Übersicht {#amneziawg-v20-overview}

<font color="red">**Hinweis**: GL.iNet-Router unterstützen AmneziaWG 2.0 ab Firmware v4.9.0.</font>

AmneziaWG 2.0 behält die Verschleierungsmechanismen aus v1.0 bei: eine Folge von Junk-Paketen (**Jc**, **Jmin**, **Jmax**) und zufällige Präfixe für Init- und Response-Pakete (**S1–S2**). Die folgenden Mechanismen verschleiern weitere, bisher vorhersagbare Merkmale der Verbindung:

* **S3–S4**: zufällige Präfixe für Cookie- und Datenpakete. v1.0 erweiterte nur Init- und Response-Pakete. Cookie-Pakete blieben daher genau 64 Bytes lang, und Datenpakete hatten genau die Länge der Nutzdaten.

* **H1–H4 als Wertebereiche**: Der Header-Wert für jeden Pakettyp wird aus einem Bereich gewählt. Beim Empfang wird jeder Wert innerhalb des Bereichs akzeptiert. Die vier Bereiche dürfen sich nicht überschneiden.

* **I1–I5**: benutzerdefinierte UDP-Pakete, die vor jedem Handshake gesendet werden. Dadurch beginnt die Sitzung mit Datenverkehr, der wie ein gängiges UDP-Protokoll aussieht und den WireGuard-Handshake verdeckt.

Diese Erweiterungen erschweren die Erkennung des VPN-Datenverkehrs und bewahren gleichzeitig die hohe Geschwindigkeit und geringe Latenz von WireGuard.

!!! Tip "Wie unterscheiden sich AmneziaWG 1.0 und 2.0?"

    **V1.0**: Keine S3-S4-Parameter; H1-H4 sind feste einzelne Ganzzahlen.
    
    **V2.0**: Es handelt sich um V2.0, wenn eine der folgenden Bedingungen erfüllt ist:
            
    - Enthält S3-S4-Parameter
    - H1-H4 sind als Zahlenbereiche festgelegt
    - Enthält angepasste I1-I5-Parameter.
            
    > Hinweis: I1-I5 werden nicht automatisch generiert. Benutzer können sie manuell als zusätzliche Zeilen in der Konfigurationsdatei ergänzen, damit AmneziaWG-Datenverkehr wie andere gängige Protokolle wie QUIC oder WebRTC aussieht.

### Parameter {#amneziawg-v20-parameters}

| Parameter | Beschreibung | Einschränkungen | Automatisch generiert |
| --------- | ------------ | --------------- | --------------------- |
| Jc | Anzahl der Junk-Pakete, bevor der Client den Handshake initiiert (zur Störung der Erkennung von Verkehrsmustern) | 1~128 | 4~12 |
| Jmin | Mindestgröße zufälliger Junk-Pakete (Bytes); muss zusammen mit Jmax konfiguriert werden, um die Größe der Junk-Pakete festzulegen | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax | Maximale Größe zufälliger Junk-Pakete | 0 ≤ Jmin < Jmax < 1280 | 0≤ Jmin < Jmax < 1280 |
| S1 | Zufällige Präfixe für Init-Pakete | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Zufällige Präfixe für Response-Pakete | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Zufällige Präfixe für Cookie-Pakete | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Zufällige Präfixe für Datenpakete | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | Dynamische Header für Pakettypen; Zufallswerte (v1.0) oder Bereiche (v2.0) | 5~2147483647; H1, H2, H3 und H4 müssen unterschiedlich sein | 5~2147483647 |
| I1~I5 | Signaturpakete zur Protokollnachahmung | beliebiger Hex-Blob | N/A |

Beispiel für die Verschleierungsparameter in v2.0:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1318795025-1318795156
H2 = 1029272944-1029273095
H3 = 966737016-966737098
H4 = 282229905-429495047
```

Referenzen: [Offizielle AmneziaWG-Dokumentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Übersicht {#amneziawg-v31-overview}

<font color="red">**Hinweis**: GL.iNet-Router unterstützen AmneziaWG 3.1 ab Firmware v4.11.1.</font>

AmneziaWG 3.1 behält alle Verschleierungsmechanismen von v2.0 bei: zufällige Präfixe für jeden Pakettyp (**S1–S4**), dynamische Header (**H1–H4**), Signaturpakete vor dem Handshake (**I1–I5**) und die Folge von Junk-Paketen (**Jc**, **Jmin**, **Jmax**). Die folgenden zusätzlichen Mechanismen erschweren es, den Datenverkehr anhand seiner Merkmale zu erkennen.

- **Header-Schutz**: Verbirgt mithilfe von ChaCha20 Felder in WireGuard-Paket-Headern, die sonst unverschlüsselt wären.
- **Auffüllen von Nutzdaten**: Ergänzt Transportdatenpakete um eine zufällige Anzahl von Füllbytes, soweit die MTU dies zulässt.
- **Konfigurierbare Zeitparameter**: Ermöglicht eigene Werte oder Bereiche für den Schlüsselwechsel, Handshake-Wiederholungen, Keepalive-Pakete und damit zusammenhängendes Verbindungsverhalten. Sowohl für den Server als auch für den Client werden die automatisch generierten Werte empfohlen.
- **Zufällige Paketzusätze**: Hängt Daten variabler Länge an Handshake- und Transportdatenpakete an, damit die Paketgrößen stärker variieren.
- **Cookie-Antworten deaktivieren**: Unterbindet das Senden von Cookie-Antworten beim Handshake. Der Empfang von Cookie-Antworten und die übrige Handshake-Verarbeitung bleiben möglich.

### Parameter {#amneziawg-v31-parameters}

AmneziaWG V3.1 führt die folgenden Parameter ein.

| Parameter | Beschreibung | Einschränkungen | GL.iNet-Bereich bzw. -Wert |
| --------- | ------------ | --------------- | --------------------------- |
| `HeaderProtectionKey` | Aktiviert den Schutz sonst unverschlüsselter Felder im Paket-Header mit ChaCha20 | Genau 32 Bytes. Bei aktiviertem Schutz müssen S1, S2, S3 und S4 jeweils gesetzt und ≥ 12 sein. Empfohlen wird `H1=1`, `H2=2`, `H3=3`, `H4=4`: Damit wird der Mechanismus für benutzerdefinierte Header deaktiviert und der Nachrichtentyp durch den Header-Schutz verborgen | 32-Byte-Schlüssel |
| `ContentPaddingAddition` | Ergänzt jedes Transportdatenpaket um eine zufällige Anzahl von Bytes aus dem konfigurierten Bereich | `range<uint16>`, 0–65535, min ≤ max; `0` oder `0-0` deaktiviert die Funktion | 0–65535 (Beispiel: `10-50`) |
| `RekeyAfterTime` | Dauer, für die der aktuelle Schlüssel verwendet wird, bevor ein aktiver Schlüsselwechsel eingeleitet wird (Sekunden) | `range<uint16>`, 0–65535, min ≤ max; bei `0` oder `0-0` gilt der WireGuard-Standardwert | 100–150 (WireGuard-Standardwert: 120) |
| `RekeyTimeout` | Wartezeit auf die Antwort auf eine einzelne Handshake-Anfrage vor einer Wiederholung (Sekunden) | `range<uint16>`, 0–65535, min ≤ max; bei `0` oder `0-0` gilt der WireGuard-Standardwert | 4–7 (WireGuard-Standardwert: 5) |
| `RejectAfterTime` | Dauer ohne Datenempfang, nach der die Verbindung einen neuen Handshake einleitet (Sekunden) | `range<uint16>`, 0–65535, min ≤ max; bei `0` oder `0-0` gilt der WireGuard-Standardwert | 180–240 (WireGuard-Standardwert: 180) |
| `KeepaliveTimeout` | Dauer ohne Datenversand, nach der ein internes Keepalive-Paket gesendet wird (Sekunden) | `range<uint16>`, 0–65535, min ≤ max; bei `0` oder `0-0` gilt der WireGuard-Standardwert | 8–20 (WireGuard-Standardwert: 10) |
| `MaxHandshakeAttempts` | Höchstzahl der Handshake-Wiederholungen | `range<uint16>`, 0–65535, min ≤ max; bei `0` oder `0-0` gilt der WireGuard-Standardwert | 12–18 (WireGuard-Standardwert: 18) |
| `RandomTrailers` | Hängt eine variable Anzahl von Bytes an Pakete an: bei Handshake-Paketen Zufallsdaten, bei Transportpaketen Nullen nach dem inneren IP-Paket. Die Länge wird dynamisch so gewählt, dass die MTU auf beiden Seiten eingehalten wird | `off` deaktiviert die Funktion. Bei aktivierter Funktion wird `S1 = S2 = S3 = S4` empfohlen, damit zufällige Paketgrößen seltener zu einer falschen Erkennung des Pakettyps führen | `on` / `off` |
| `DisableCookies` | Unterbindet das Senden von Cookie-Antworten beim Handshake durch das lokale Gerät. Der Empfang von Cookie-Antworten des Peers und die übrige Handshake-Verarbeitung bleiben unverändert | `off` deaktiviert die Funktion. S3/H3 müssen weiterhin gültig sein, da sie beim Empfang noch verwendet werden können | `on` / `off` |

**Hinweise**

* Die Wertebereiche in der letzten Spalte können vom Router generiert werden. `RandomTrailers` und `DisableCookies` werden pro Gerät eingestellt.
* `HeaderProtectionKey` muss auf Client und Server identisch sein.
* Zeitwerte außerhalb der aufgeführten Bereiche werden zur Laufzeit durch einen Zufallswert innerhalb des jeweiligen Bereichs ersetzt. Ein eigener Wert wird daher unter Umständen nicht wie eingegeben übernommen.
* `ContentPaddingAddition` und `S4` ändern beide die Länge von Transportpaketen, wirken aber auf unterschiedliche Teile des Pakets und können gemeinsam verwendet werden.
* Header-Schutz und dynamische `H`-Werte schließen sich nicht aus. `H1–H4` können dynamisch bleiben; empfohlen wird jedoch die Einstellung `1/2/3/4`.

---

Beispiel für die Verschleierungsparameter in v3.1:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

Referenzen: [Offizielle AmneziaWG-Dokumentation](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Verwandter Artikel:

- [VPN-Verschleierung auf GL.iNet-Routern einrichten](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
