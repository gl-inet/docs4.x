# Come controllare lo stato della carrier aggregation sul router cellulare

La carrier aggregation combina piu' bande di rete per offrire maggiore larghezza di banda e velocita' piu' elevate alla connessione cellulare.

Questa funzione non puo' essere abilitata dal pannello di amministrazione web del router, poiche' dipende dal supporto del gestore della SIM.

Tuttavia, puoi controllare lo stato della carrier aggregation usando i comandi AT nel pannello di amministrazione web del router.

!!! note "Modelli supportati"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Segui i passaggi seguenti per controllare lo stato della carrier aggregation.

1. Inserisci una SIM card nel router.
2. Apri un browser web, inserisci `192.168.8.1` nella barra degli indirizzi ed effettua l'accesso.
3. Vai su **INTERNET** -> sezione **Cellular**, fai clic sull'icona con tre puntini nell'angolo in alto a destra, poi fai clic su **Modem AT Command**.

    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. Nella finestra pop-up, inserisci **AT+QCAINFO** e fai clic su **Send**.

    Se la carrier aggregation e' attiva, vedrai piu' bande di rete mostrate nell'elenco.

    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
