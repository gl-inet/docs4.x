# Come accedere da remoto al pannello di amministrazione web di un router GL.iNet?

I metodi seguenti richiedono una preconfigurazione mentre ci si trova ancora fisicamente vicino al router.

## Metodo 1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} è una piattaforma progettata per semplificare la distribuzione e la gestione da remoto dei dispositivi connessi. Offre un modo semplice per accedere e gestire da remoto i router GL.iNet. È sufficiente associare il router GL.iNet a GoodCloud; dopodiché sarà possibile accedere da remoto al pannello di amministrazione web del router in qualsiasi momento e da qualsiasi luogo.

Per i dettagli, consulta [questa guida](../interface_guide/cloud.md){target="_blank"}.

## Metodo 2. VPN

Se il router dispone di un **IP pubblico**, puoi accedere da remoto al suo pannello di amministrazione web tramite un tunnel VPN. Tieni presente che questo metodo richiede configurazioni avanzate e più tempo per la configurazione.

1. Assicurati che il router disponga di un IP pubblico. [Come posso verificare se ho un indirizzo IP pubblico?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Configura il router come WireGuard Server. Consulta i dettagli [qui](../interface_guide/wireguard_server.md){target="_blank"}.

3. Esporta un file di configurazione dal WireGuard Server per usarlo in seguito.

4. Nel pannello di amministrazione web del router, vai su **VPN** -> **WireGuard Server** e fai clic su **Options** nell'angolo in alto a destra. Abilita **Allow Remote Access to the LAN Subnet**, quindi fai clic su **Apply**.

5. Configura come WireGuard Client il dispositivo da cui desideri accedere da remoto al router importando manualmente il file di configurazione.

    - Se il WireGuard Client è un dispositivo terminale, ad esempio uno smartphone o un laptop, [installa l'app WireGuard](https://www.wireguard.com/install){target="_blank"}, quindi importa il file per avviare una connessione.

    - Se il WireGuard Client è un altro router GL.iNet, ad esempio un router da viaggio GL.iNet, consulta [questa guida](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"} per importare il file di configurazione e avviare una connessione.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
