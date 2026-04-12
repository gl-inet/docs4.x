# Jak sprawdzić status agregacji operatora na routerze komórkowym

Agregacja operatora łączy wiele pasm sieci, aby zapewnić większą przepustowość i wyższe prędkości dla połączenia komórkowego.

Tej funkcji nie można włączyć w panelu administracyjnym routera, ponieważ zależy ona od wsparcia operatora karty SIM.

Możesz jednak sprawdzić status agregacji operatora za pomocą poleceń AT w panelu administracyjnym routera.

!!! note "Obsługiwane modele"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Wykonaj poniższe kroki, aby sprawdzić status agregacji operatora.

1. Włóż kartę SIM do routera. 
2. Otwórz przeglądarkę internetową, wprowadź `192.168.8.1` w pasku adresu i zaloguj się. 
3. Przejdź do sekcji **INTERNET** -> **Cellular**, kliknij ikonę trzech kropek w prawym górnym rogu i kliknij **Modem AT Command**. 
    
    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. W wyskakującym oknie wprowadź **AT+QCAINFO** i kliknij **Send**.

    Jeśli agregacja operatora jest aktywna, zobaczysz wiele pasm sieci na liście. 
    
    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
