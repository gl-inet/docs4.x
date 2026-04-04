# Configurare una WAN Ethernet cablata duale tramite adattatore Ethernet-USB-A

Puoi configurare un accesso WAN Ethernet cablato duale su un router con una sola porta WAN usando un adattatore Ethernet-USB-A.

I router GL.iNet supportano i comuni adattatori Ethernet-USB-A, consentendoti di convertire l'accesso Ethernet cablato dal router ISP in una connessione USB tramite la porta USB del router, fornendo cosi' al router un accesso Ethernet cablato aggiuntivo oltre alla porta WAN.

## Topologia

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Passaggi di configurazione

1. Collega l'adattatore Ethernet-USB-A alla porta USB del router GL.iNet e collega l'altra estremita' al router ISP.

2. Installa il driver USB.

    Accedi al pannello di amministrazione web del router, vai su **Application** -> **Plug-ins** e installa il driver USB network per il tuo adattatore.

    Ad esempio, se stai usando un adattatore Realtek, installa il driver **kmod-usb-net-rtl8152**.

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Attendi il completamento dell'installazione.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Connettiti tramite USB Tethering.

    Una volta completata l'installazione del driver, vai su **INTERNET** -> sezione **Tethering**.

    La connessione USB verra' rilevata, consentendoti di collegarti al router ISP.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Fai clic su **Connect** e attendi circa un minuto. Quando si accende un punto verde e la pagina mostra informazioni come l'indirizzo IP, significa che la connessione USB Tethering e' riuscita.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
