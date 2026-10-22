# Carrier aggregation op je mobiele router controleren {#how-to-check-the-carrier-aggregation-status-on-your-cellular-router}

Carrier aggregation combineert meerdere netwerkbanden voor meer bandbreedte en een snellere mobiele verbinding.

Je kunt deze functie niet via het webbeheerpaneel inschakelen, omdat ze afhankelijk is van ondersteuning door je simprovider.

Je kunt de status wel met AT-opdrachten in het webbeheerpaneel controleren.

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Follow the steps below to check the carrier aggregation status.

1. Insert a SIM card into the router.
2. Open een webbrowser, voer `192.168.8.1` in de adresbalk in en meld je aan.
3. Ga naar **INTERNET** -> **Cellular**, klik rechtsboven op het pictogram met drie puntjes en klik op **Modem AT Command**.

    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. Voer in het pop-upvenster **AT+QCAINFO** in en klik op **Send**.

    Als carrier aggregation actief is, worden meerdere netwerkbanden in de lijst weergegeven.

    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
