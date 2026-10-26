# Scheduled Tasks {#scheduled-tasks}

Öppna **SYSTEM** -> **Scheduled Tasks**.

Scheduled Tasks skapar dagliga scheman för LED, omstart, Wi‑Fi och TX-effekt.

**Obs!** Synkronisera först tiden under [Time Zone](time_zone.md). Uppgiften körs inte om enheten är avstängd.

## LED Display Schedule {#led-display-schedule}

Funktionen schemalägger routerns LED-lampa.

Ange på- och av-tider, välj veckodagar och klicka på Apply.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

På modeller med pekskärm schemalägger LCD Display skärmen.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Schedule Reboot {#schedule-reboot}

Funktionen schemalägger automatisk omstart.

Ange omstartstider, välj veckodagar och klicka på Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Wi-Fi Schedule {#wi-fi-schedule}

Funktionen schemalägger Wi-Fi-band som 2.4 GHz, 5 GHz, 6 GHz och MLO Wi-Fi.

MLO Wi-Fi stöder endast Turn On/Off. Övriga band stöder Turn On/Off och Switch TX Power.

- **Turn On/Off**: Aktiverar eller inaktiverar nätverket vid angivna tider för tillgänglighet och energibesparing.

- **Switch TX Power**: Justerar automatiskt sändningseffekten vid angivna tider för balans mellan prestanda och energi.

### MLO Wi-Fi Schedule {#mlo-wi-fi-schedule}

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-BE14000 (Flint 4)     |    √    |
| GL-BE10000 (Slate 7 Pro) |    √    |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

Du kan schemalägga MLO Main Wi-Fi och Guest Wi-Fi.

Aktivera Main eller Guest Wi-Fi Schedule, ange tider och veckodagar och klicka på Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### 6 GHz Wi-Fi Schedule {#6-ghz-wi-fi-schedule}

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-BE14000 (Flint 4)     |    √    |
| GL-BE10000 (Slate 7 Pro) |    √    |
| GL-E5800 (Mudi 7)        |    √    |
| GL-BE9300 (Flint 3)      |    √    |

I **Turn On/Off** kan du schemalägga 6 GHz Main Wi-Fi och Guest Wi-Fi.

Aktivera Main eller Guest Wi-Fi Schedule, ange tider och veckodagar och klicka på Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

I **Switch TX Power** kan du schemalägga TX-effekt för 6 GHz Main Wi-Fi. 6 GHz Guest Wi-Fi stöds inte.

Aktivera Main Wi-Fi Schedule, ange två tidsstyrda TX-åtgärder och veckodagar och klicka på Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Set TX Power to a certain level (e.g., Low) at a specific time (e.g., 22:00).
- **Restore**: Restore TX Power to another level (e.g., Max) at another time (e.g., 07:00).
- **days**: Välj veckodagar för inställningarna.

### 5 GHz Wi-Fi Schedule {#5-ghz-wi-fi-schedule}

I **Turn On/Off** kan du schemalägga 5 GHz Main Wi-Fi och Guest Wi-Fi.

Aktivera Main eller Guest Wi-Fi Schedule, ange tider och veckodagar och klicka på Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

I **Switch TX Power** kan du schemalägga TX-effekt för 5 GHz Main Wi-Fi. 5 GHz Guest Wi-Fi stöds inte.

Aktivera Main Wi-Fi Schedule, ange två tidsstyrda TX-åtgärder och veckodagar och klicka på Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Set TX Power to a certain level (e.g., Low) at a specific time (e.g., 22:00).
- **Restore**: Restore TX Power to another level (e.g., Max) at another time (e.g., 07:00).
- **days**: Välj veckodagar för inställningarna.

### 2.4 GHz Wi-Fi Schedule {#24-ghz-wi-fi-schedule}

I **Turn On/Off** kan du schemalägga 2.4 GHz Main Wi-Fi och Guest Wi-Fi.

Aktivera Main eller Guest Wi-Fi Schedule, ange tider och veckodagar och klicka på Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

I **Switch TX Power** kan du schemalägga TX-effekt för 2.4 GHz Main Wi-Fi. 2.4 GHz Guest Wi-Fi stöds inte.

Aktivera Main Wi-Fi Schedule, ange två tidsstyrda TX-åtgärder och veckodagar och klicka på Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Set TX Power to a certain level (e.g., Low) at a specific time (e.g., 22:00).
- **Restore**: Restore TX Power to another level (e.g., Max) at another time (e.g., 07:00).
- **days**: Välj veckodagar för inställningarna.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
