# Aggiornare la versione di Uboot

## Avviso

**L'aggiornamento di U-Boot è molto pericoloso e in generale non è consigliato. Se fallisce, il dispositivo verrà bloccato e non ci sarà modo di ripristinarlo. Esegui questa operazione solo quando necessario o se richiesto dal supporto GL.iNet**.

**NON** spegnere l'alimentazione durante il processo di aggiornamento, altrimenti l'aggiornamento potrebbe fallire e il dispositivo potrebbe bloccarsi.

## Preparazione

- Un computer con porta Ethernet. In caso contrario, prepara un adattatore USB Ethernet aggiuntivo.
- Un cavo Ethernet.
- Scarica il file Uboot seguendo le istruzioni del personale di supporto GL.iNet. Assicurati di usare il file Uboot corretto. Se non sai come scaricare il file Uboot, contattaci via email all'indirizzo support@gl-inet.com.

## Passaggi per l'aggiornamento

Segui la procedura riportata di seguito per accedere alla pagina di aggiornamento U-Boot.

1. Scollega l'alimentazione del router. Collega il computer alla **porta Ethernet LAN** del router. **TUTTE** le altre porte devono rimanere **scollegate**.

    !!! note

        Per alcuni modelli, alcune singole porte LAN e la porta WAN sono intercambiabili. Non usare questa porta LAN. Ad esempio, su GL-MT6000 (Flint 2), non usare LAN 1. Usa invece LAN 2, LAN 3 o LAN 4.

2. Tieni premuto con decisione il pulsante Reset e, allo stesso tempo, accendi il router. Se il router non ha un pulsante di alimentazione, collegare l'alimentazione lo accenderà automaticamente.

    Vedrai quindi il LED lampeggiare in una sequenza regolare alcune volte; rilascia il dito quando la sequenza cambia.

3. Imposta manualmente l'indirizzo IP del computer su **192.168.1.2**. Consulta la guida dettagliata per i diversi sistemi operativi qui sotto:

    ??? "Windows 7 / Windows 10"

        1. Vai su **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Fai clic con il tasto destro su **Local Area Connection** -> **Properties**.

        3. Fai clic su **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Imposta manualmente **IP address** su `192.168.1.2`.

        5. Imposta **Subnet mask** su `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Fai clic sul pulsante **OK**.

    ??? "Windows 11"

        7. Apri Settings.

        8. Fai clic su **Network & Internet**.

        9. Fai clic sulla scheda **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Nella sezione "IP assignment", fai clic sul pulsante **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Seleziona l'opzione **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Attiva l'interruttore **IPv4**.

        13. Imposta l'**IP address** statico su **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Specifica **Subnet mask** come **255.255.255.0**.

        15. Fai clic sul pulsante **Save**.

    ??? "macOS"

        16. Fai clic sull'icona **Apple** nell'angolo in alto a sinistra dello schermo e seleziona **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Fai clic su **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Fai clic su **Ethernet** a sinistra e poi sulla casella a discesa accanto a **Configure IPv4**, quindi seleziona **Manually**. Se stai usando un adattatore USB Ethernet, Ethernet potrebbe non essere visibile e potrebbe comparire invece il nome dell'adattatore USB Ethernet.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Inserisci **IPv4 Address** come `192.168.1.2`, **Subnet Mask** come `255.255.255.0`, **Router** come `192.168.1.1`, quindi fai clic sul pulsante Apply in basso a destra.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4. **Usa Google Chrome o Microsoft Edge per visitare `http://192.168.1.1/uboot.html`**. Assicurati di inserire l'URL completo per evitare suggerimenti memorizzati nella cache che portano all'indirizzo sbagliato.

    **NON usare Mozilla Firefox, perché potrebbe bloccare il router.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5. Fai clic sul pulsante **Choose file** e seleziona il file Uboot scaricato.

6. Fai clic sul pulsante **Update U-Boot**. **NON** spegnere l'alimentazione durante il processo di aggiornamento. L'aggiornamento richiederà alcuni minuti.

7. Dopo un aggiornamento riuscito, il router si riavvierà. A questo punto puoi ripristinare l'impostazione IP modificata al passaggio 3 e provare ad accedere al pannello di amministrazione web tramite **192.168.8.1**. Se riesci ad accedere normalmente al pannello di amministrazione web, significa che il router si è riavviato correttamente.

    **Nota:** potrebbe essere necessario usare la modalità in incognito oppure eliminare cache e cookie del browser per accedere al router.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
