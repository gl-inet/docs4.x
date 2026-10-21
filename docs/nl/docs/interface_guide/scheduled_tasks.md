# Scheduled Tasks {#scheduled-tasks}

Ga links in het webbeheerpaneel naar **SYSTEM** -> **Scheduled Tasks**.

Met Scheduled Tasks kun je dagelijkse schema's maken voor basisbewerkingen, zoals leds in- of uitschakelen, de router herstarten, Wi‑Fi in- of uitschakelen en het TX-vermogen wijzigen.

**Opmerking**: synchroniseer vóór gebruik de tijd onder [Time Zone](time_zone.md). Als het apparaat op het geplande tijdstip is uitgeschakeld, wordt de taak niet uitgevoerd.

## Schema voor ledscherm {#led-display-schedule}

Met deze functie stel je een in- en uitschakelschema voor de led van de router in.

Stel na inschakeling de in- en uitschakeltijden en weekdagen in en klik op Apply.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

Bij modellen met touchscreen, zoals GL-BE3600 Slate 7, stel je met LCD Display Schedule een schema voor het touchscreen in.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Herstartschema {#schedule-reboot}

Met deze functie stel je een schema in om de router automatisch opnieuw op te starten.

Stel na inschakeling de herstarttijden en weekdagen in en klik op Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Wi-Fi-schema {#wi-fi-schedule}

Met deze functie stel je schema's in voor de Wi-Fi-banden die je router ondersteunt, zoals 2.4 GHz, 5 GHz, 6 GHz en MLO Wi-Fi.

MLO Wi-Fi ondersteunt alleen Turn On/Off. Alle andere Wi-Fi-banden ondersteunen Turn On/Off en Switch TX Power.

- **Turn On/Off**: schakelt het draadloze netwerk automatisch op ingestelde tijden in of uit voor gebruiksgemak en energiebesparing.

- **Switch TX Power**: past het draadloze zendvermogen, en daarmee signaalsterkte en dekking, automatisch op bepaalde tijden aan voor evenwicht tussen prestaties en energieverbruik.

### MLO Wi-Fi-schema {#mlo-wi-fi-schedule}

| Ondersteunde modellen         |         |
| :----------------------- | :-----: |
| GL-BE14000 (Flint 4)     |    √    |
| GL-BE10000 (Slate 7 Pro) |    √    |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

Je kunt een in- en uitschakelschema voor zowel MLO Main Wi-Fi als Guest Wi-Fi instellen.

Schakel Main of Guest Wi-Fi Schedule in, stel de in- en uitschakeltijden en weekdagen in en klik op Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### 6 GHz-Wi-Fi-schema {#6-ghz-wi-fi-schedule}

| Ondersteunde modellen         |         |
| :----------------------- | :-----: |
| GL-BE14000 (Flint 4)     |    √    |
| GL-BE10000 (Slate 7 Pro) |    √    |
| GL-E5800 (Mudi 7)        |    √    |
| GL-BE9300 (Flint 3)      |    √    |

In de modus **Turn On/Off** kun je een in- en uitschakelschema voor 6 GHz Main Wi-Fi en Guest Wi-Fi instellen.

Schakel Main of Guest Wi-Fi Schedule in, stel de in- en uitschakeltijden en weekdagen in en klik op Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

In de modus **Switch TX Power** kun je een schema voor het TX-vermogen van 6 GHz Main Wi-Fi instellen. 6 GHz Guest Wi-Fi ondersteunt deze modus niet.

Schakel Main Wi-Fi Schedule in, stel twee tijdgebonden acties voor het TX-vermogen en de weekdagen in en klik op Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: stel TX Power op een tijdstip, bijvoorbeeld 22:00, in op een niveau, bijvoorbeeld Low.
- **Restore**: herstel TX Power op een ander tijdstip, bijvoorbeeld 07:00, naar een ander niveau, bijvoorbeeld Max.
- **days**: selecteer de weekdagen waarop de instellingen gelden.

### 5 GHz-Wi-Fi-schema {#5-ghz-wi-fi-schedule}

In de modus **Turn On/Off** kun je een in- en uitschakelschema voor 5 GHz Main Wi-Fi en Guest Wi-Fi instellen.

Schakel Main of Guest Wi-Fi Schedule in, stel de in- en uitschakeltijden en weekdagen in en klik op Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

In de modus **Switch TX Power** kun je een schema voor het TX-vermogen van 5 GHz Main Wi-Fi instellen. 5 GHz Guest Wi-Fi ondersteunt deze modus niet.

Schakel Main Wi-Fi Schedule in, stel twee tijdgebonden acties voor het TX-vermogen en de weekdagen in en klik op Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: stel TX Power op een tijdstip, bijvoorbeeld 22:00, in op een niveau, bijvoorbeeld Low.
- **Restore**: herstel TX Power op een ander tijdstip, bijvoorbeeld 07:00, naar een ander niveau, bijvoorbeeld Max.
- **days**: selecteer de weekdagen waarop de instellingen gelden.

### 2.4 GHz-Wi-Fi-schema {#24-ghz-wi-fi-schedule}

In de modus **Turn On/Off** kun je een in- en uitschakelschema voor 2.4 GHz Main Wi-Fi en Guest Wi-Fi instellen.

Schakel Main of Guest Wi-Fi Schedule in, stel de in- en uitschakeltijden en weekdagen in en klik op Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

In de modus **Switch TX Power** kun je een schema voor het TX-vermogen van 2.4 GHz Main Wi-Fi instellen. 2.4 GHz Guest Wi-Fi ondersteunt deze modus niet.

Schakel Main Wi-Fi Schedule in, stel twee tijdgebonden acties voor het TX-vermogen en de weekdagen in en klik op Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/interface_guide/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: stel TX Power op een tijdstip, bijvoorbeeld 22:00, in op een niveau, bijvoorbeeld Low.
- **Restore**: herstel TX Power op een ander tijdstip, bijvoorbeeld 07:00, naar een ander niveau, bijvoorbeeld Max.
- **days**: selecteer de weekdagen waarop de instellingen gelden.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
