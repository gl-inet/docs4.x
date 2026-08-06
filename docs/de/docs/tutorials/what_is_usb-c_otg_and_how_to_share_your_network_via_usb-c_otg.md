# Was ist USB-C OTG und wie teilen Sie Ihr Netzwerk über USB-C OTG

## USB OTG
**USB OTG** (On-The-Go) ist ein USB-Standard, mit dem kompatible Geräte wie Router zwischen **Host**- und **Device**-Rolle wechseln können. Dadurch sind direkte Datenübertragung und Stromversorgung ohne separates Host-Gerät möglich.

Die folgenden zwei Modi können über **USB OTG** gewechselt werden:

- Wenn ein Gerät über USB OTG in den **Host-Modus** wechselt, agiert es als USB-Host, startet die Datenübertragung, liefert Strom und steuert alle Lese- und Schreibvorgänge zwischen den beiden verbundenen Geräten.

- Im **Device-Modus** arbeitet das Gerät als Peripheriegerät. Es bezieht Strom vom Host und reagiert passiv auf dessen Befehle, ohne selbstständig Kommunikation zu starten.

## Netzwerkfreigabe über USB-C OTG auf Mudi 7

Der OTG-fähige USB-C-Port des Mudi 7 arbeitet je nach Szenario im **Device**- oder **Host**-Modus, um die Netzwerkfreigabe mit externen Geräten zu ermöglichen.

### Verbindung mit einem Computer

Die meisten Computer arbeiten nur als Host und unterstützen OTG nicht. Wenn ein Computer per USB mit dem Router verbunden wird, zeigt der Router ein Fenster zur Modusauswahl an. Sie können einen beliebigen Modus auswählen; der Mudi 7 handelt die Rolle automatisch aus. Der Computer erkennt ihn anschließend ohne zusätzliche Treiber als USB-Adapter für den direkten Internetzugang.

### Verbindung mit einem Smartphone

- **Device Mode**: Der Mudi 7 agiert als USB-Gerät und teilt sein Netzwerk mit dem Smartphone.

- **Host Mode**: Wenn Sie USB Tethering auf dem Smartphone aktivieren, kann das Smartphone sein Mobilfunknetz per USB mit dem Mudi 7 teilen. Diese USB-Verbindung kann als eigenständige WAN-Schnittstelle dienen und Multi-WAN ermöglichen.

!!! Note

    1. Wenn Sie die OTG-Funktion des Smartphones für die Verbindung verwenden, stellen Sie sicher, dass das Smartphone OTG unterstützt und ein datenfähiges USB-Kabel verwendet wird. Reine Ladekabel können keine Netzwerksignale übertragen.

    2. Wenn Device Mode aktiviert ist, zeigt das Smartphone keine Benachrichtigung zur Netzwerkverbindung an. Prüfen Sie zur Kontrolle den Netzwerkstatus in den Smartphone-Einstellungen oder führen Sie einen Verbindungstest aus.

        Wenn Sie beispielsweise das Netzwerk des Mudi 7 per **Device Mode** mit einem Smartphone teilen (z. B. iPhone 17 Pro), prüfen Sie mit den folgenden Schritten, ob Device Mode aktiv ist.

        1. Verbinden Sie den USB-3.1-Port des Mudi 7 mit einem OTG-fähigen USB-Kabel mit dem iPhone 17 Pro.

        2. Wählen Sie auf dem Mudi 7 **Device Mode** aus.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. In den Einstellungen des Smartphones sehen Sie, dass der Mudi 7 Ihrem Smartphone Netzwerkzugang bereitstellt, wie im folgenden Screenshot gezeigt.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
