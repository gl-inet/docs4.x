# Proteggere RDP da una rete esterna con WireGuard

Potresti aver bisogno di accedere in remoto al tuo PC da una rete esterna, o viceversa. Il modo più sicuro è usare il tuo tunnel WireGuard. Questo offre maggiore sicurezza rispetto al port forwarding e all’accesso diretto al PC tramite il tuo indirizzo IP pubblico. Dopo aver configurato il tunnel, puoi usare **Windows Remote Desktop** per accedere al PC ovunque ti trovi.

Questo tutorial usa due router GL.iNet come esempio per mostrare come proteggere Windows RDP tramite una rete WireGuard.

## Topologia

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Passaggi di configurazione

1. Configura la tua rete WireGuard.

    Per prima cosa, configura il tuo server WireGuard e il client WireGuard con due router GL.iNet. Consulta [Creare un server WireGuard con due router GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Consenti al server WireGuard di accedere alla LAN del client.

    Per abilitare l’accesso bidirezionale tra server e client, consenti prima al server di accedere alla LAN del client. Consulta [Accedere alla LAN del client WireGuard dal server](wireguard_server_access_to_client_lan_side.md).

    I passaggi possono variare in base alla versione del firmware.

3. Consenti al client WireGuard di accedere alla LAN del server.

    Questo passaggio può variare in base alla versione del firmware. Seleziona di seguito la versione del firmware del router configurato come client WireGuard.

    ??? note "Per firmware v4.7 e precedenti"

        Accedi al client WireGuard e vai a **VPN** -> **VPN Dashboard**. Individua **VPN Server** e fai clic sull’icona dell’ingranaggio a destra.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        Nella finestra a comparsa, abilita **Remote Access LAN** e fai clic su **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Per firmware v4.8 e successivi"

        Accedi al client WireGuard e vai a **VPN** -> **WireGuard Server**. Fai clic su **Options** in alto a destra.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        Nella finestra a comparsa, abilita **Allow Remote Access to the LAN Subnet** e fai clic su **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Collega al server VPN il computer a cui vuoi accedere e individua il suo indirizzo IP LAN.

    Nell’esempio seguente, l’indirizzo IP del PC lato server è **192.168.29.123**.

5. Rendi accessibile il PC lato server.

    Sul PC lato server, vai a **System Settings** e fai clic su **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Abilita **Remote Desktop** e fai clic su **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Accedi in remoto dal laptop lato client.

    Cerca **Remote Desktop Connection** nella barra di ricerca.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Avvia l’app e inserisci l’indirizzo IP del PC lato server, ad esempio **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Inserisci le credenziali del PC lato server per connetterti.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Potrai quindi controllare in remoto il PC lato server.

    Se vuoi fare il contrario, basta invertire i passaggi del PC server e del laptop client.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
