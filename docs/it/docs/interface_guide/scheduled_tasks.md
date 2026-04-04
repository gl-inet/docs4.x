# Scheduled Tasks

Sul lato sinistro del pannello di amministrazione web, vai su **SYSTEM** -> **Scheduled Tasks**.

Scheduled Tasks consente di impostare pianificazioni giornaliere per operazioni di base come accensione e spegnimento del LED, riavvio del router, abilitazione e disabilitazione del Wi-Fi e cambio del livello di potenza TX.

**Nota**: prima di usare questa funzione, sincronizza l'orario in [Time Zone](time_zone.md). Se il dispositivo e' spento all'orario programmato, l'attivita' non verra' eseguita.

## Pianificazione del display LED

Questa funzione consente di impostare un orario di accensione e spegnimento per la luce LED del router.

Quando e' abilitata, imposta gli orari di accensione e spegnimento, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

Per i modelli con touchscreen, ad esempio GL-BE3600 Slate 7, la pianificazione del display LCD consente di impostare un orario di accensione e spegnimento per il touchscreen.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Pianificazione del riavvio

Questa funzione consente di impostare una pianificazione per riavviare automaticamente il router.

Quando e' abilitata, imposta gli orari di riavvio, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Pianificazione Wi-Fi

Questa funzione consente di impostare pianificazioni Wi-Fi in base alle bande di frequenza Wi-Fi supportate dal router, ad esempio 2.4 GHz, 5 GHz, 6 GHz e MLO Wi-Fi.

Tranne MLO Wi-Fi, che supporta solo la modalita' di pianificazione accensione/spegnimento, tutte le altre bande di frequenza Wi-Fi supportano due modalita' di pianificazione: Turn On/Off e Switch TX Power.

- **Turn On/Off**: aiuta a bilanciare comodita' di connettivita' e risparmio energetico abilitando o disabilitando automaticamente la rete wireless in orari specifici, ad esempio spegnendola durante le ore di sonno per ridurre consumi non necessari.

- **Switch TX Power**: si riferisce alla regolazione automatica della potenza di trasmissione wireless, che determina forza del segnale e copertura, in orari specifici, bilanciando prestazioni ed efficienza energetica, ad esempio riducendo la potenza durante i periodi di basso utilizzo.

### Pianificazione MLO Wi-Fi

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

Puoi impostare una pianificazione di accensione e spegnimento sia per MLO Main Wi-Fi sia per Guest Wi-Fi.

Abilita la pianificazione Main o Guest Wi-Fi, imposta gli orari di accensione e spegnimento, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### Pianificazione Wi-Fi 6 GHz

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-E5800 (Mudi 7)        |    √    |
| GL-BE9300 (Flint 3)      |    √    |

Quando la modalita' di pianificazione Wi-Fi e' **Turn On/Off**, puoi impostare una pianificazione di accensione e spegnimento sia per 6 GHz Main Wi-Fi sia per Guest Wi-Fi.

Abilita la pianificazione Main o Guest Wi-Fi, imposta gli orari di accensione e spegnimento, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Quando la modalita' di pianificazione Wi-Fi e' **Switch TX Power**, puoi impostare una pianificazione di commutazione della potenza TX per il 6 GHz Main Wi-Fi. Tieni presente che il 6 GHz Guest Wi-Fi non e' supportato in questa modalita' di pianificazione.

Abilita la pianificazione Main Wi-Fi, imposta due azioni temporizzate per cambiare la potenza TX, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: imposta la potenza TX a un determinato livello, ad esempio Low, a un orario specifico, ad esempio 22:00.
- **Restore**: ripristina la potenza TX a un altro livello, ad esempio Max, a un altro orario, ad esempio 07:00.
- **days**: seleziona i giorni della settimana in cui queste impostazioni devono avere effetto.

### Pianificazione Wi-Fi 5 GHz

Quando la modalita' di pianificazione Wi-Fi e' **Turn On/Off**, puoi impostare una pianificazione di accensione e spegnimento sia per 5 GHz Main Wi-Fi sia per Guest Wi-Fi.

Abilita la pianificazione Main o Guest Wi-Fi, imposta gli orari di accensione e spegnimento, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Quando la modalita' di pianificazione Wi-Fi e' **Switch TX Power**, puoi impostare una pianificazione di commutazione della potenza TX per il 5 GHz Main Wi-Fi. Tieni presente che il 5 GHz Guest Wi-Fi non e' supportato in questa modalita' di pianificazione.

Abilita la pianificazione Main Wi-Fi, imposta due azioni temporizzate per cambiare la potenza TX, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: imposta la potenza TX a un determinato livello, ad esempio Low, a un orario specifico, ad esempio 22:00.
- **Restore**: ripristina la potenza TX a un altro livello, ad esempio Max, a un altro orario, ad esempio 07:00.
- **days**: seleziona i giorni della settimana in cui queste impostazioni devono avere effetto.

### Pianificazione Wi-Fi 2.4 GHz

Quando la modalita' di pianificazione Wi-Fi e' **Turn On/Off**, puoi impostare una pianificazione di accensione e spegnimento sia per 2.4 GHz Main Wi-Fi sia per Guest Wi-Fi.

Abilita la pianificazione Main o Guest Wi-Fi, imposta gli orari di accensione e spegnimento, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Quando la modalita' di pianificazione Wi-Fi e' **Switch TX Power**, puoi impostare una pianificazione di commutazione della potenza TX per il 2.4 GHz Main Wi-Fi. Tieni presente che il 2.4 GHz Guest Wi-Fi non e' supportato in questa modalita' di pianificazione.

Abilita la pianificazione Main Wi-Fi, imposta due azioni temporizzate per cambiare la potenza TX, seleziona i giorni della settimana in cui devono avere effetto e poi fai clic su Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: imposta la potenza TX a un determinato livello, ad esempio Low, a un orario specifico, ad esempio 22:00.
- **Restore**: ripristina la potenza TX a un altro livello, ad esempio Max, a un altro orario, ad esempio 07:00.
- **days**: seleziona i giorni della settimana in cui queste impostazioni devono avere effetto.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
