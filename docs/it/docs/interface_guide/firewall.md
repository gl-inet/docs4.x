# Firewall

Questa guida si applica al firmware v4.5 e precedenti.

Dalla v4.6, la pagina Firewall e' stata suddivisa. Le funzioni Port Forwarding e DMZ sono state spostate in [Port Forwarding](port_forwarding.md). La funzione Open Ports e' stata spostata in [Security](security.md).

---

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Firewall**.

La pagina Firewall consente di impostare regole firewall come **Port Forwarding**, **Open Ports on Router** e **DMZ**.

## Port Forwards

Port Forwarding consente ai computer remoti di collegarsi a un computer locale o a un server dietro il firewall del router nella LAN, ad esempio server web o server FTP.

Per configurare il port forwarding, fai clic sulla scheda **Port Forwards**, quindi su **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/firewall.png){class="glboxshadow"}

Nella finestra a comparsa, aggiungi una regola di port forwarding e fai clic su **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** Inserisci un nome per la regola.

**Protocol:** Seleziona il protocollo: TCP, UDP o entrambi.

**External Zone:** Seleziona l’interfaccia da cui arriva il traffico in ingresso. Le opzioni sono `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` e `wgserver`. Le opzioni relative alla VPN compaiono solo dopo aver configurato una connessione VPN.

**External Port:** Inserisci il numero di porta esterna.

**Internal Zone:** Seleziona l’interfaccia a cui viene inoltrato il traffico. Le opzioni sono `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` e `wgserver`. Le opzioni relative alla VPN compaiono solo dopo aver configurato una connessione VPN.

**Internal IP:** Inserisci l’indirizzo IP LAN del dispositivo a cui vuoi accedere da remoto.

**Internal Port:** Inserisci il numero di porta interna del dispositivo. Lascia il campo vuoto se coincide con la porta esterna.

**Enable:** Usa l’interruttore per abilitare o disabilitare la regola.

## Open Ports on Router

I servizi del router, come web e FTP, richiedono che le relative porte siano aperte sul router per poter essere raggiunti pubblicamente.

Per aprire una porta, passa alla scheda **Open Ports on Router**, quindi fai clic su **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/open_ports_on_router.png){class="glboxshadow"}

Nella finestra pop-up, apri una nuova porta e fai clic su **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** il nome della regola, specificabile dall'utente.

**Protocol:** il protocollo usato. Puoi scegliere TCP, UDP oppure sia TCP sia UDP.

**Port:** il numero di porta che vuoi aprire.

**Enable:** abilita o disabilita la regola.

## DMZ

DMZ consente di esporre un computer a Internet, quindi tutti i pacchetti in ingresso verranno reindirizzati a questo computer.

Attiva **Enable DMZ**. Seleziona l'indirizzo IP interno del dispositivo host che dovra' ricevere tutti i pacchetti in ingresso.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/dmz.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
