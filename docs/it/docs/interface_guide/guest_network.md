# Rete ospite

Le impostazioni della rete ospite sono state separate da [LAN](lan.md) a partire dal firmware v4.5.

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Guest Network**.

Questa pagina ti consente di creare una rete Wi-Fi dedicata agli ospiti. Isolata dalla rete principale, migliora la sicurezza offrendo al tempo stesso un comodo accesso a Internet.

**Nota**: alcuni modelli, ad esempio GL-MT5000 e GL-MT2500/GL-MT2500A, non dispongono della funzione Wi-Fi; per questo motivo le impostazioni della Guest Network non sono disponibili nel loro pannello di amministrazione web.

Include due sezioni: Impostazioni di base e Impostazioni del server DHCP.

## Impostazioni di base

Puoi impostare la subnet all'interno degli intervalli di indirizzi privati IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

- **Gateway**

    Il **gateway predefinito** della Guest Network e' **192.168.9.1**. Se e' in conflitto con la rete locale, cambialo con un altro.

- **Netmask**

    Per impostazione predefinita e' **255.255.255.0**. Puoi anche selezionare **255.255.0.0** se hai bisogno di una subnet piu' ampia con piu' indirizzi IP.

- **AP Isolation**

    Questa funzione e' disponibile dal firmware v4.5.

    Consente di isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

- **Block WAN Subnets**

    Questa funzione e' disponibile dal firmware v4.8.

    Quando e' abilitata, la rete ospite non puo' accedere alla rete a monte e alla relativa subnet.

## Server DHCP

Se la Guest Network e' abilitata, verra' abilitato di conseguenza anche il relativo server DHCP.

Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client connesso alla Guest Network. Se il server DHCP e' disabilitato, dovrai configurare manualmente le impostazioni di rete dei dispositivi client. Fai clic [qui](../tutorials/manually_configure_static_ip.md) per sapere come configurare manualmente un IP statico.

Puoi modificare gli indirizzi IP iniziale e finale in base alle tue esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP oppure se viene modificato l'intervallo della subnet mask.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Fai clic su **Advanced** per ulteriori configurazioni, se necessario.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: il periodo di validita' di un indirizzo IP assegnato tramite DHCP a un dispositivo.

- **Gateway**: il dispositivo che instrada il traffico tra la rete ospite e le reti esterne come Internet.

- **DNS Server 1**: il server primario che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2**: il server secondario usato per la risoluzione dei nomi di dominio se il server DNS primario non e' disponibile.

- **LPR Server**: (Line Printer Remote Server) un servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. Possono essere configurate piu' porte stampante LPR.

---

Articoli correlati:

- [Come configurare una rete Wi-Fi ospite sui router GL.iNet](../tutorials/how_to_set_up_a_guest_network.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
