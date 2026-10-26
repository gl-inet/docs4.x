# Kontrollera status för bärvågsaggregering på mobilroutern {#how-to-check-the-carrier-aggregation-status-on-your-cellular-router}

Bärvågsaggregering kombinerar flera nätverksband för att ge mobilanslutningen större bandbredd och högre hastighet.

Funktionen kan inte aktiveras i routerns webbadministrationspanel eftersom den är beroende av stöd från SIM-operatören.

Du kan dock kontrollera status för bärvågsaggregering med AT-kommandon i routerns webbadministrationspanel.

!!! note "Modeller som stöds"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Följ stegen nedan för att kontrollera status för bärvågsaggregering.

1. Sätt i ett SIM-kort i routern.
2. Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in.
3. Gå till **INTERNET** -> avsnittet **Cellular**, klicka på ikonen med tre punkter i det övre högra hörnet och klicka på **Modem AT Command**.

    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. Ange **AT+QCAINFO** i dialogrutan och klicka på **Send**.

    Om bärvågsaggregering är aktiv visas flera nätverksband i listan.

    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
