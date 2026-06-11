# Port Forwarding

Questa guida si applica al firmware v4.6 e versioni successive. Per le versioni precedenti, fare riferimento a [Firewall](firewall.md).

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Port Forwarding** oppure su **SECURITY** -> **Port Forwarding** (per firmware v4.9 e versioni successive).

Questa pagina consente di impostare regole firewall, incluse DMZ e port forwarding.

Nota: per aprire le porte del router, vai su SYSTEM -> [Security](security.md), oppure su SECURITY -> [Admin Access](admin_access.md) (per firmware v4.9 e versioni successive).

## DMZ

DMZ consente di esporre un computer a Internet, in modo che tutti i pacchetti in ingresso vengano reindirizzati a questo computer.

Attiva **Enable DMZ**. Seleziona l'indirizzo IP interno del dispositivo host che dovrà ricevere tutti i pacchetti in ingresso.

Puoi impostare la priorità della DMZ. Se la priorità della DMZ è più alta delle regole di port forwarding, tutte le regole di port forwarding verranno invalidate. In caso contrario, le richieste verranno inoltrate al dispositivo DMZ Host solo se la porta richiesta non ha una regola di port forwarding corrispondente.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding

Port Forwarding consente ai computer remoti di collegarsi a un computer locale o a un server dietro il firewall del router nella LAN, come web server, server FTP e così via.

Per configurare il port forwarding, fai clic su **Add** nella sezione Port Forwarding.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

Nella finestra pop-up, aggiungi una nuova regola di port forwarding e fai clic su **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

- **Protocol:** scegli `TCP`, `UDP` oppure `TCP and UDP` per questa regola.

- **External Zone:** le opzioni per la zona esterna sono `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN` e `Guest`.

- **External Port:** i numeri delle porte esterne. Puoi inserire qui un numero di porta specifico. L'intervallo va da 1 a 65535. Puoi impostare una singola porta oppure un intervallo concatenando il primo e l'ultimo numero di porta con il simbolo `-`, ad esempio `501-510`.

- **Internal Zone:** le opzioni per la zona interna sono `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server` e `WAN`.

- **Internal IP:** l'indirizzo IP assegnato dal router al dispositivo che deve essere accessibile da remoto. Se imposti una singola porta in **External Port**, dovresti impostare qui la porta singola. Se imposti un intervallo di porte in **External Port**, dovresti impostare qui l'intervallo di porte corrispondente.

- **Internal Port:** il numero di porta interna del dispositivo. Puoi inserire un numero di porta specifico. Lascialo vuoto se è uguale alla porta esterna.

- **Description:** imposta un nome personalizzato oppure aggiungi una descrizione per questa regola (facoltativo).

- **Enable:** abilita o disabilita questa regola.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
