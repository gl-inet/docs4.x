# Notifica di problema e soluzioni per il malfunzionamento con schede SIM EE su GL-X3000/GL-XE3000/GL-X2000

Gentili clienti GL.iNet,

Di recente abbiamo notato che alcuni clienti riscontrano problemi di connettività su GL-X3000/GL-XE3000/GL-X2000 quando usano schede SIM EE. Dopo ulteriori verifiche, abbiamo scoperto che alcune schede SIM EE supportano solo il protocollo IPv4. Tuttavia, le impostazioni predefinite dei router cellulari GL.iNet abilitano contemporaneamente IPv4 e IPv6, causando questo problema.

## Soluzioni e workaround

1. **Aggiornamento firmware**

    Abbiamo rilasciato nuovi aggiornamenti firmware che hanno modificato il protocollo predefinito in IPv4 per risolvere il problema. I clienti che hanno bisogno di IPv6 possono comunque modificare l'impostazione in IPv4 & IPv6 nel pannello di amministrazione.

    | Router Model                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Firmware Download](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Firmware Download](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Firmware Download](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Workaround per altri modelli**

    Se possiedi altri modelli oppure preferisci non usare il firmware sopra indicato, esegui i comandi AT in sequenza dopo aver avviato la connessione cellulare.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Nota**: "User_APN" in genere è "everywhere" per le schede SIM EE. Ripeti questa procedura dopo ogni riavvio del router.

    ??? note "Come eseguire un comando AT?"

        1. Nel pannello di amministrazione web, vai a INTERNET -> sezione Cellular, fai clic sull'icona con i tre puntini in alto a destra e seleziona **Modem AT Command**.

            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

            Per i firmware meno recenti, fai clic sul pulsante degli strumenti in alto a destra per accedere alla pagina di gestione del modem.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

        2. Individua la sezione AT command, come mostrato di seguito.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Se riscontri ulteriori problemi, contatta il nostro team di supporto all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Cordiali saluti,

GL.iNet Technical Support

June 17, 2025
