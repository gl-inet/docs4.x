# MAC Address {#mac-address}

Guiden gäller firmware v4.5 och tidigare.

Sidan MAC Address hette tidigare MAC Clone och bytte namn i v4.2.

Från v4.6 finns MAC-adressinställningarna för Ethernet och Repeater på [Ethernet Port](ethernet_port.md) respektive [Repeater](internet_repeater.md).

---

Öppna **NETWORK** -> **MAC Address** på vänster sida i webbadministrationspanelen.

Du kan visa routerns standard-MAC-adress, klona en klients adress, ange en adress manuellt eller generera en slumpmässig adress.

Om flera Ethernet-portar kan användas som WAN kan MAC-adressen anges separat för varje port. Inställningen gäller endast när porten används som WAN.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* The factory default MAC address.

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Clone a client's MAC address.

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Obs!** Många nya enheter använder olika slumpmässiga MAC-adresser för olika Wi-Fi-nätverk. Adressen som visas kanske därför inte är enhetens fysiska adress. Funktionen kan heta Private Wi-Fi Address eller random hardware address.

* Manual input or generate a random MAC address.

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Usage Scenarios {#usage-scenarios}

Använd en slumpmässig MAC-adress på offentliga hotspots om du inte vill röja den verkliga adressen eller få internetåtkomsten begränsad utifrån den. Se [Anslut till en hotspot med Captive Portal](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
