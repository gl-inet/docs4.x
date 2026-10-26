# Ändra WAN till LAN {#change-wan-to-lan}

Du kan ändra routerns WAN-port till en LAN-port. Det är särskilt användbart när routern används i repeaterläge och WAN-porten inte behövs. Genom att ändra WAN-porten till en LAN-port får du ytterligare en LAN-port för fler anslutningar.

Följ stegen nedan för att ändra WAN till LAN.

## För firmware 4.10 {#for-firmware-410}

1. Låt WAN-porten vara oansluten.

2. Anslut en enhet till routern och öppna routerns webbadministrationspanel.

3. Gå till **INTERNET** -> avsnittet **Ethernet 1** i webbadministrationspanelen och klicka på kugghjulsikonen i det övre högra hörnet.

    ![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_1.png){class="glboxshadow"}

4. Sidan **Ethernet Port** öppnas. Klicka på kugghjulsikonen under WAN-porten.

    ![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_2.png){class="glboxshadow"}

5. Klicka på **LAN** för att ändra Ethernet-portens egenskaper och klicka på **Apply**.

    ![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_3.png){class="glboxshadow"}

6. På sidan Ethernet Port eller i avsnittet Ethernet visas nu att WAN-porten används som LAN-port.

    ![ethernet port 4](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_4.png){class="glboxshadow"}

    ![ethernet port 5](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_5.png){class="glboxshadow"}

Du kan ändra tillbaka till WAN på sidan Ethernet Port eller hålla RESET-knappen intryckt i 4 sekunder för att starta om WAN-gränssnittet.

## För firmware 4.7-4.9 {#for-firmware-47-49}

1. Låt WAN-porten vara oansluten.

2. Anslut en enhet till routern och öppna routerns webbadministrationspanel.

3. Gå till **INTERNET** -> avsnittet **Ethernet** i webbadministrationspanelen och klicka på kugghjulsikonen i det övre högra hörnet.

    ![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

    Sidan **Port Management** öppnas. Där visas att WAN-porten används för WAN.

    ![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Klicka på **LAN** för att ändra Ethernet-portens egenskaper och klicka på **Apply**.

    ![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

    Klicka på **Apply** i varningsfönstret för att bekräfta.

    ![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

    **Obs!** Wi-Fi kan kopplas från tillfälligt under processen. Anslut till routern igen när den är klar.

5. I avsnittet Ethernet visas nu att WAN-porten används som LAN-port.

    ![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

    Du kan ändra tillbaka till WAN på sidan **Port Management** eller hålla RESET-knappen intryckt i 4 sekunder för att starta om WAN-gränssnittet.

## För firmware 4.6 och tidigare {#for-firmware-46-and-earlier}

1. Låt WAN-porten vara oansluten.

2. Anslut en enhet till routern och öppna webbadministrationspanelen.

3. Gå till **INTERNET** -> avsnittet **Ethernet** i webbadministrationspanelen. Där visas WAN-portens status som **Using as WAN**. Klicka på **Change to LAN**.

    ![internet page](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Klicka på **Apply** för att bekräfta.

    ![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

    **Obs!** Wi-Fi kan kopplas från tillfälligt under processen. Anslut till routern igen när den är klar.

5. I avsnittet Ethernet visas `Using as LAN`.

    ![using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

    Du kan återställa inställningen genom att upprepa proceduren ovan.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
