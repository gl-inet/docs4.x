# Client

Sul lato sinistro del pannello di amministrazione web, vai su **CLIENTS**.

La pagina Client mostra le informazioni sui dispositivi connessi, inclusi nome del dispositivo, tipo di connessione, indirizzo IP, indirizzo MAC, velocita' e traffico, disposte da sinistra a destra.

## Nome del dispositivo

La prima colonna mostra il nome e il tipo del dispositivo, che dipendono dal nome host impostato sul dispositivo.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Per modificare il nome e il tipo del dispositivo, fai clic sull'icona con i tre puntini nella colonna Action e, nel menu a discesa, fai clic su **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Tipo di connessione

L'icona blu sul lato destro del nome del dispositivo rappresenta il tipo/metodo di connessione del dispositivo.

Indica come il dispositivo e' collegato alla rete, cioe' tramite Wi-Fi oppure tramite cavo Ethernet.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## Indirizzo IP e MAC

La seconda colonna elenca gli indirizzi IP e MAC del dispositivo connesso.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Molti dispositivi utilizzano indirizzi MAC casuali. Se i dispositivi connessi usano indirizzi MAC casuali, verra' visualizzato il seguente avviso.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Nota**: la regola utilizzata qui e' che, se il secondo carattere dell'indirizzo MAC e' 2, 6, A oppure E (senza distinzione tra maiuscole e minuscole), viene considerato un indirizzo MAC casuale. Tuttavia, alcuni dispositivi possono usare regole diverse per generare un indirizzo MAC casuale, quindi questo metodo di rilevamento potrebbe non essere accurato.

## Velocita'

La terza colonna mostra la velocita' Internet del dispositivo connesso.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

La velocita' qui indicata e' la velocita' media su 3 minuti.

- Se apri la pagina corrente per 10 secondi, viene mostrata la velocita' media degli ultimi 10 secondi.
- Se apri la pagina corrente per 30 secondi, viene mostrata la velocita' media degli ultimi 30 secondi.
- Se apri la pagina corrente per 60 secondi, viene mostrata la velocita' media degli ultimi 60 secondi.
- Se apri la pagina corrente per 3 minuti, viene mostrata la velocita' media degli ultimi 3 minuti.
- Se apri la pagina corrente per 10 minuti, viene mostrata la velocita' media degli ultimi 3 minuti.

## Traffico

La quarta colonna mostra il traffico Internet del dispositivo connesso.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## IP riservato

Nella quinta colonna puoi riservare un indirizzo IP per uno specifico dispositivo connesso con un solo clic.

Questa funzione e' disponibile dalla v4.8.

Quando specifichi un indirizzo IP riservato per un client all'interno della LAN, il client ricevera' sempre lo stesso indirizzo IP ogni volta che accede al server DHCP del router.

Puoi assegnare indirizzi IP riservati a computer o server che richiedono impostazioni IP permanenti.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blocklist {#blocklist}

Nella sesta colonna puoi bloccare specifici dispositivi connessi con un solo clic.

Per impostazione predefinita, la regola di controllo accessi e' Blocklist, ma se necessario puoi cambiarla in Allowlist dalla parte superiore.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: i dispositivi con indirizzi MAC presenti nella blocklist non possono connettersi a questo router.

- **Allowlist**: solo i dispositivi con specifici indirizzi MAC possono connettersi, soluzione adatta a dispositivi IoT e alla gestione di reti aziendali.

Per creare una Blocklist, puoi caricare una lista di blocco in formato Excel in **(1)** oppure inserire manualmente gli indirizzi MAC in **(2)**.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Metodo 1. Importa client**

Nella pagina Access Control, fai clic su **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Fai clic su **Download Import Template** per scaricare un foglio di lavoro XLS denominato "mac-template.csv".

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Apri il file, importa gli indirizzi MAC e salva.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Seleziona il file salvato oppure trascinalo nell'area di caricamento.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Una volta completato il caricamento, fai clic su **Import** per completare l'importazione in blocco degli indirizzi MAC.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Metodo 2. Inserimento manuale**

Nella pagina Access Control, inserisci manualmente l'indirizzo MAC dei dispositivi che vuoi bloccare e fai clic su **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Nota**: il blocco del client si basa sull'indirizzo MAC del dispositivo. Se il dispositivo bloccato utilizza un indirizzo MAC diverso la volta successiva, potra' comunque connettersi al router.

## Ordinamento

Il tipo di ordinamento corrente e' mostrato nell'angolo superiore destro e puoi passare ad altri tipi di ordinamento.

Il tipo di ordinamento predefinito e' il seguente:

- Il dispositivo in uso e' sempre in cima.
- Nella sezione dei client online, piu' recentemente si e' connesso un dispositivo, piu' in alto apparira' nell'elenco.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Azione

### Dettagli del client

Se hai bisogno di visualizzare i dettagli del dispositivo client, fai clic sull'icona con i tre puntini nella colonna Action all'estrema destra, quindi fai clic su **View Details** nel menu a discesa.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Nella sottopagina aperta potrai vedere tutte le informazioni sul dispositivo client, inclusi tutti gli eventuali indirizzi IPv6 del dispositivo.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modifica

Fai clic sull'icona con i tre puntini nella colonna Action e, nel menu a discesa, fai clic su **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Limita velocita'

Fai clic sull'icona con i tre puntini nella colonna Action e, nel menu a discesa, fai clic su **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Se a un client e' stata applicata una limitazione della velocita', le frecce su e giu' della velocita' diventeranno gialle.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

Fai clic sull'icona con i tre puntini nella colonna Action per disabilitare il limite di velocita'.

### Usa tunnel VPN

**Nota**: questa opzione e' disponibile a partire dal firmware v4.8 e apparira' nel menu Action solo se e' configurata una policy basata su MAC.

Aggiungi un client all'elenco del tunnel VPN con una policy basata su MAC. Se hai bisogno di regolare in dettaglio i tunnel, vai al VPN Dashboard per gestirli.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Rimuovi client offline

Nella sezione dei client offline, puoi fare clic su **Delete All** in alto a destra per eliminare tutti i client offline.

Se vuoi rimuovere un client specifico, fai clic sull'icona con i tre puntini nella colonna Action e, nel menu a discesa, fai clic su **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
