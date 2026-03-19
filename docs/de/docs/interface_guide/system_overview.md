# Systemübersicht

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **SYSTEM** -> **Overview**.

Die Seite **Overview** zeigt den Status verschiedener Hardwarekomponenten an und bietet einige einfache Steuerungsmöglichkeiten, darunter die folgenden:

- Status von CPU, Speicher, Flash und externen Speichergeräten.
- Status von Hardware wie Lüfter, Akku usw.
- Steuerung von LEDs und Lüfter.
- Geräteinformationen.

Hier sehen Sie ein Beispiel für den GL-MT3000.

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## Durchschnittliche CPU-Auslastung

Bei den meisten Modellen ohne Lüfter wird die durchschnittliche CPU-Auslastung wie unten dargestellt angezeigt.

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

Bei einigen Modellen mit integriertem Lüfter wird die durchschnittliche CPU-Auslastung wie unten dargestellt angezeigt.

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Bewegen Sie den Mauszeiger über das Diagramm, um die genauen Werte anzuzeigen.

Klicken Sie rechts auf die Temperaturanzeige, um zwischen Celsius und Fahrenheit umzuschalten.

Klicken Sie oben rechts auf das Fan-Symbol, um die **Fan Settings** zu öffnen.

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Modelle mit integriertem Lüfter"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Speicherauslastung

Bewegen Sie den Mauszeiger über das Diagramm, um die genauen Werte anzuzeigen.

**Hinweis**: Der hier angezeigte Speicher ist der Speicher, der dem Linux-System zur Verfügung steht. Der hier angegebene Gesamtspeicher ist kleiner als der physische Speicher, da ein Teil davon dem Wi‑Fi-Subsystem oder anderen Boot-Bereichen zugewiesen wird.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

Wenn Sie auf das Zahnradsymbol klicken, gelangen Sie zu den [Scheduled Tasks](scheduled_tasks.md) für die LED.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

Hier wird der gesamte Flash-Speicher angezeigt, einschließlich des vom System belegten, des von Apps belegten und des noch verfügbaren Speicherplatzes.

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## Geräteinformationen

Dieser Abschnitt zeigt die grundlegenden Informationen des Geräts an.

Device ID, Geräte-MAC und Geräte-S/N wurden ab Firmware v4.7 hinzugefügt.

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## Externer Speicher

Dieser Abschnitt ist seit v4.5 verfügbar und zeigt die Gesamt- und verfügbare Kapazität des USB-Datenträgers an.

Einige Modelle unterstützen ab Firmware v4.7 und höher das Umschalten des USB-Protokolls.

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
