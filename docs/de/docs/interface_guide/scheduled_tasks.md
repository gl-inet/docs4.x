# Geplante Aufgaben

Gehen Sie in der Web-Adminoberfläche auf der linken Seite zu **SYSTEM** -> **Scheduled Tasks**.

Mit Scheduled Tasks können Sie tägliche Zeitpläne für grundlegende Vorgänge festlegen, z. B. zum Ein-/Ausschalten der LED, zum Neustarten des Routers, zum Aktivieren/Deaktivieren von Wi‑Fi und zum Umschalten der TX-Leistungsstufe.

**Hinweis**: Synchronisieren Sie zuerst die Zeit in der [Time Zone](time_zone.md), bevor Sie diese Funktion verwenden. Wenn das Gerät zur geplanten Zeit ausgeschaltet ist, wird die Aufgabe nicht ausgeführt.

## Zeitplan für die LED-Anzeige

Mit dieser Funktion können Sie einen Ein-/Ausschaltzeitplan für die LED Ihres Routers festlegen.

Wenn die Funktion aktiviert ist, stellen Sie die Ein- und Ausschaltzeiten ein, wählen die Wochentage aus, an denen sie gelten soll, und klicken dann auf Apply.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

Bei Modellen mit Touchscreen (z. B. GL-BE3600 Slate 7) können Sie mit dem LCD-Anzeigezeitplan einen Ein-/Ausschaltzeitplan für den Touchscreen festlegen.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Geplanter Neustart

Mit dieser Funktion können Sie einen Zeitplan für den automatischen Neustart Ihres Routers festlegen.

Wenn die Funktion aktiviert ist, stellen Sie die Neustartzeiten ein, wählen die Wochentage aus, an denen sie gelten soll, und klicken dann auf Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Wi‑Fi-Zeitplan

Mit dieser Funktion können Sie Wi‑Fi-Zeitpläne auf Grundlage der von Ihrem Router unterstützten Wi‑Fi-Frequenzbänder festlegen (z. B. 2,4 GHz, 5 GHz, 6 GHz und MLO Wi‑Fi).

Mit Ausnahme von MLO Wi‑Fi, das nur den Modus für Ein-/Ausschaltzeitpläne unterstützt, unterstützen alle anderen Wi‑Fi-Frequenzbänder zwei Zeitplanmodi: Turn On/Off und Switch TX Power.

- **Turn On/Off**: Hilft dabei, Komfort bei der Konnektivität und Energieeinsparung auszubalancieren, indem das Drahtlosnetzwerk zu bestimmten Zeiten automatisch aktiviert oder deaktiviert wird (z. B. Ausschalten während der Schlafenszeit, um unnötigen Stromverbrauch zu reduzieren).

- **Switch TX Power**: Bezieht sich auf das automatische Anpassen der Wireless-Sendeleistung (die Signalstärke und Reichweite bestimmt) zu bestimmten Zeiten, um Leistung und Energieeffizienz auszubalancieren (z. B. reduzierte Leistung bei geringer Nutzung).

### MLO Wi‑Fi-Zeitplan

| Unterstützte Modelle      |         |
| :------------------------ | :-----: |
| GL-E5800 (Mudi 7)         |    √    |
| GL-MT3600BE (Beryl 7)     |    √    |
| GL-BE6500 (Flint 3e)      |    √    |
| GL-BE9300 (Flint 3)       |    √    |
| GL-BE3600 (Slate 7)       |    √    |

Sie können sowohl für das MLO Main Wi‑Fi als auch für das Guest Wi‑Fi einen Ein-/Ausschaltzeitplan festlegen.

Aktivieren Sie den Zeitplan für Main oder Guest Wi‑Fi, stellen Sie die Ein- und Ausschaltzeiten ein, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### 6-GHz-Wi‑Fi-Zeitplan

| Unterstützte Modelle      |         |
| :------------------------ | :-----: |
| GL-E5800 (Mudi 7)         |    √    |
| GL-BE9300 (Flint 3)       |    √    |

Wenn der Wi‑Fi-Zeitplanmodus **Turn On/Off** ist, können Sie sowohl für das 6 GHz Main Wi‑Fi als auch für das Guest Wi‑Fi einen Ein-/Ausschaltzeitplan festlegen.

Aktivieren Sie den Zeitplan für Main oder Guest Wi‑Fi, stellen Sie die Ein- und Ausschaltzeiten ein, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Wenn der Wi‑Fi-Zeitplanmodus **Switch TX Power** ist, können Sie für das 6 GHz Main Wi‑Fi einen Zeitplan zum Umschalten der TX-Leistung festlegen. Beachten Sie, dass 6 GHz Guest Wi‑Fi diesen Zeitplanmodus nicht unterstützt.

Aktivieren Sie den Zeitplan für Main Wi‑Fi, legen Sie zwei zeitgesteuerte Aktionen zum Umschalten der TX-Leistung fest, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Legt die TX-Leistung zu einer bestimmten Zeit (z. B. 22:00) auf eine bestimmte Stufe fest (z. B. Low).
- **Restore**: Stellt die TX-Leistung zu einer anderen Zeit (z. B. 07:00) auf eine andere Stufe zurück (z. B. Max).
- **days**: Wählen Sie die Wochentage aus, an denen diese Einstellungen wirksam sein sollen.

### 5-GHz-Wi‑Fi-Zeitplan

Wenn der Wi‑Fi-Zeitplanmodus **Turn On/Off** ist, können Sie sowohl für das 5 GHz Main Wi‑Fi als auch für das Guest Wi‑Fi einen Ein-/Ausschaltzeitplan festlegen.

Aktivieren Sie den Zeitplan für Main oder Guest Wi‑Fi, stellen Sie die Ein- und Ausschaltzeiten ein, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Wenn der Wi‑Fi-Zeitplanmodus **Switch TX Power** ist, können Sie für das 5 GHz Main Wi‑Fi einen Zeitplan zum Umschalten der TX-Leistung festlegen. Beachten Sie, dass 5 GHz Guest Wi‑Fi diesen Zeitplanmodus nicht unterstützt.

Aktivieren Sie den Zeitplan für Main Wi‑Fi, legen Sie zwei zeitgesteuerte Aktionen zum Umschalten der TX-Leistung fest, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Legt die TX-Leistung zu einer bestimmten Zeit (z. B. 22:00) auf eine bestimmte Stufe fest (z. B. Low).
- **Restore**: Stellt die TX-Leistung zu einer anderen Zeit (z. B. 07:00) auf eine andere Stufe zurück (z. B. Max).
- **days**: Wählen Sie die Wochentage aus, an denen diese Einstellungen wirksam sein sollen.

### 2,4-GHz-Wi‑Fi-Zeitplan

Wenn der Wi‑Fi-Zeitplanmodus **Turn On/Off** ist, können Sie sowohl für das 2,4 GHz Main Wi‑Fi als auch für das Guest Wi‑Fi einen Ein-/Ausschaltzeitplan festlegen.

Aktivieren Sie den Zeitplan für Main oder Guest Wi‑Fi, stellen Sie die Ein- und Ausschaltzeiten ein, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Wenn der Wi‑Fi-Zeitplanmodus **Switch TX Power** ist, können Sie für das 2,4 GHz Main Wi‑Fi einen Zeitplan zum Umschalten der TX-Leistung festlegen. Beachten Sie, dass 2,4 GHz Guest Wi‑Fi diesen Zeitplanmodus nicht unterstützt.

Aktivieren Sie den Zeitplan für Main Wi‑Fi, legen Sie zwei zeitgesteuerte Aktionen zum Umschalten der TX-Leistung fest, wählen Sie die Wochentage aus, an denen sie gelten soll, und klicken Sie dann auf Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Legt die TX-Leistung zu einer bestimmten Zeit (z. B. 22:00) auf eine bestimmte Stufe fest (z. B. Low).
- **Restore**: Stellt die TX-Leistung zu einer anderen Zeit (z. B. 07:00) auf eine andere Stufe zurück (z. B. Max).
- **days**: Wählen Sie die Wochentage aus, an denen diese Einstellungen wirksam sein sollen.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
