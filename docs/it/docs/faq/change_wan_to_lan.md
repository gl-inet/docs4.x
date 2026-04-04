# Cambiare WAN in LAN

Puoi modificare la porta WAN del router affinché funzioni come porta LAN. Questa opzione è particolarmente utile quando il router viene usato in modalità repeater, in cui la porta WAN non è necessaria. Cambiando la porta WAN in porta LAN, avrai una porta LAN aggiuntiva per ampliare la connettività.

Segui i passaggi seguenti per cambiare WAN in LAN.

## Per firmware 4.7 e successivi

1. Lascia la porta WAN scollegata.

2. Collega un dispositivo al router e accedi al pannello di amministrazione web del router.

3. Nel pannello di amministrazione web, vai a **INTERNET** -> sezione **Ethernet** e fai clic sull'icona a forma di ingranaggio nell'angolo in alto a destra.

    ![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

    Verrai indirizzato alla pagina **Port Management**, dove lo stato della porta WAN viene mostrato come in uso per WAN.

    ![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Fai clic su **LAN** per modificare le proprietà della porta Ethernet e poi fai clic su **Apply**.

    ![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

    Nella finestra popup di avviso, fai clic su **Apply** per confermare.

    ![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

    **Nota**: durante questo processo il Wi-Fi potrebbe disconnettersi temporaneamente. Ricollegati al router al termine dell'operazione.

5. Tornando alla sezione Ethernet, verrà mostrato che la porta WAN ora è usata come porta LAN.

    ![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

    Puoi riportarla a WAN nella pagina **Port Management**, oppure premere il pulsante RESET per 4 secondi per riavviare l'interfaccia WAN.

## Per firmware 4.6 e precedenti

1. Lascia la porta WAN scollegata.

2. Collega un dispositivo al router e accedi al pannello di amministrazione web.

3. Nel pannello di amministrazione web, vai a **INTERNET** -> sezione **Ethernet**, dove lo stato della porta WAN viene mostrato come **Using as WAN**. Fai clic su **Change to LAN**.

    ![internet page](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Fai clic su **Apply** per confermare.

    ![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

    **Nota**: durante questo processo il Wi-Fi potrebbe disconnettersi temporaneamente. Ricollegati al router al termine dell'operazione.

5. Tornando alla sezione Ethernet, verrà mostrato `Using as LAN`.

    ![using as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

    Puoi semplicemente ripristinare l'impostazione ripetendo la procedura sopra.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
