# MAC Address

Questa guida si applica al firmware v4.5 e precedenti.

La pagina MAC Address in precedenza era intitolata MAC Clone ed e' stata rinominata in MAC Address a partire dalla v4.2.

Dalla v4.6, le impostazioni dell'indirizzo MAC per le interfacce Ethernet e Repeater sono state spostate rispettivamente in [Ethernet Port](ethernet_port.md) e [Repeater](internet_repeater.md).

---

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **MAC Address**.

Puoi trovare l'indirizzo MAC predefinito del router, clonare l'indirizzo MAC di un client, inserire manualmente un indirizzo MAC oppure generarne uno casuale.

Se il dispositivo supporta l'impostazione di piu' porte Ethernet da usare come porte WAN, puoi impostare separatamente l'indirizzo MAC per ciascuna porta. Tieni presente che l'impostazione dell'indirizzo MAC e' valida solo quando la porta Ethernet viene usata come porta WAN.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* L'indirizzo MAC predefinito di fabbrica.

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Clonare l'indirizzo MAC di un client.

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Nota:** molti dispositivi recenti usano indirizzi MAC casuali diversi per connettersi a reti Wi-Fi differenti, quindi l'indirizzo MAC mostrato qui potrebbe non essere il vero indirizzo MAC del dispositivo dell'utente. Il MAC casuale puo' anche essere chiamato Private Wi-Fi Address o random hardware address su dispositivi diversi.

* Inserimento manuale o generazione di un indirizzo MAC casuale.

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Scenari di utilizzo

Quando ti connetti a un hotspot pubblico, usa un indirizzo MAC casuale se non vuoi che l'hotspot conosca il tuo vero indirizzo MAC o limiti il tuo accesso a Internet in base ad esso. Leggi questa guida [Connect to a Hotspot with a Captive Portal](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
