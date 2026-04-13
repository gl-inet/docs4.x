# LAN

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **LAN**.

La LAN e' la rete a cui il dispositivo e' connesso quando si collega tramite il Wi-Fi principale o tramite un cavo Ethernet.

Include impostazioni di base, impostazioni del server DHCP e prenotazione degli indirizzi.

## Impostazioni di base

Puoi impostare la subnet all'interno degli intervalli di indirizzi privati IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    Questo e' l'indirizzo da inserire nella barra degli indirizzi del browser per accedere alla pagina di amministrazione del router.

    Per impostazione predefinita e' **192.168.8.1**. Puoi modificarlo se entra in conflitto con la tua rete.

- **Netmask**

    Il valore predefinito e' **255.255.255.0**. Puoi anche selezionare **255.255.0.0** se hai bisogno di una subnet piu' ampia con un numero maggiore di indirizzi IP.

- **AP Isolation**

    Puoi isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

## Server DHCP

Il **DHCP Server** e' abilitato per impostazione predefinita. Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client.

Se il server DHCP e' disabilitato, dovrai configurare manualmente le impostazioni di rete dei dispositivi client. Fai clic [qui](../tutorials/manually_configure_static_ip.md) per scoprire come configurare manualmente un IP statico.

Puoi modificare gli indirizzi IP iniziale e finale in base alle tue esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP oppure se viene modificato l'intervallo della subnet mask.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Se necessario, fai clic su **Advanced** per ulteriori configurazioni.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: il periodo per cui un indirizzo IP assegnato dal DHCP resta valido per un dispositivo.

- **Gateway**: il dispositivo che instrada il traffico tra la rete locale e reti esterne come Internet.

- **DNS Server 1**: il server primario che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2**: il server secondario usato per la risoluzione dei nomi di dominio se il server DNS primario non e' disponibile.

- **LPR Server**: (Line Printer Remote Server) un servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. E' possibile configurare piu' porte stampante LPR.

## Prenotazione degli indirizzi

Quando specifichi un indirizzo IP riservato per un client all'interno della LAN, il client riceve sempre lo stesso indirizzo IP ogni volta che accede al server DHCP del router. Puoi assegnare indirizzi IP riservati a computer o server che richiedono impostazioni IP permanenti.

**Nota:** i client configurati devono riconnettersi al router per attivare la modifica.

Fai clic su **Add** per riservare un IP.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

Comparira' una finestra pop-up.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Seleziona il **MAC** dall'elenco a discesa e l'**IP** corrispondente al MAC selezionato verra' compilato automaticamente. Assegna un nome descrittivo, quindi fai clic su **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

Dopo aver aggiunto una nuova prenotazione IP, vedrai la pagina mostrata di seguito, il che significa che la configurazione e' stata completata con successo.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
