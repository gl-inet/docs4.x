# Rete IoT

> La funzione IoT Network è stata introdotta nel firmware v4.9.

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **IoT Network**.

Questa pagina ti consente di creare una rete Wi-Fi dedicata ai dispositivi IoT. Isolata dalla rete principale, offre maggiore compatibilità e una sicurezza migliorata.

**Nota**: alcuni modelli, ad esempio GL-MT5000 e GL-MT2500/GL-MT2500A, non dispongono della funzione Wi-Fi; per questo motivo le impostazioni della IoT Network non sono disponibili nel loro pannello di amministrazione web.

Include due sezioni: Impostazioni di base e Impostazioni del server DHCP.

## Impostazioni di base

Puoi impostare la subnet all’interno degli intervalli di indirizzi privati IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot1.png){class="glboxshadow"}

- **Gateway**

    Il **gateway predefinito** della rete IoT è **192.168.10.1**. Se è in conflitto con la rete locale, modificalo con un altro.

- **Netmask**

    Per impostazione predefinita è **255.255.255.0**. Puoi anche selezionare **255.255.0.0** se hai bisogno di una subnet più ampia con più indirizzi IP.

- **AP Isolation**

    Questa funzione è disponibile dal firmware v4.5

    Consente di isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

- **Block WAN Subnets**

    Questa funzione è disponibile dal firmware v4.8

    Quando è abilitata, la rete IoT non può accedere alla rete a monte e alla relativa subnet.

## Server DHCP

Se la rete IoT è abilitata, verrà abilitato di conseguenza anche il relativo server DHCP.

Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client connesso alla rete IoT. Se il server DHCP è disabilitato, dovrai configurare manualmente le impostazioni di rete dei dispositivi client. Fai clic [qui](../tutorials/manually_configure_static_ip.md) per sapere come configurare manualmente un IP statico.

Puoi modificare gli indirizzi IP iniziale e finale in base alle tue esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP oppure se viene modificato l’intervallo della subnet mask.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot2.png){class="glboxshadow"}

Fai clic su **Advanced** per ulteriori configurazioni, se necessario.

![iot network 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot3.png){class="glboxshadow"}

![iot network 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot4.png){class="glboxshadow"}

- **Lease Time**: il periodo di validità di un indirizzo IP assegnato tramite DHCP a un dispositivo.

- **Gateway**: il dispositivo che instrada il traffico tra la rete IoT e le reti esterne, come Internet.

- **DNS Server 1**: il server primario che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2**: il server secondario usato per la risoluzione dei nomi di dominio se il server DNS primario non è disponibile.

- **LPR Server**: (Line Printer Remote Server) un servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. Possono essere configurate più porte stampante LPR.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
