# Usare WireGuard per proteggere RDP da una rete esterna

Potresti aver bisogno di accedere in remoto al tuo PC da una rete esterna, o viceversa. Il modo piu sicuro e accedervi tramite il tuo tunnel WireGuard. Offre piu sicurezza rispetto al port forwarding e all'accesso tramite il tuo indirizzo IP pubblico. Dopo aver configurato il tunnel, puoi usare l'app **Remote Desktop** di Windows per accedere al PC ovunque ti trovi.

## Topologia

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Configurare la tua rete WireGuard

Devi configurare il tuo server WireGuard e il client WireGuard prima di poter usare il tunnel WireGuard per RDP. Puoi configurare il tunnel con due router GL.iNet. Fai riferimento a [Crea il tuo server WireGuard domestico con due router GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Consentire al server di accedere al lato LAN del client

Se vuoi un accesso reciproco tra server e client, devi prima consentire al server di accedere al lato LAN del client. Fai riferimento a [Accesso alla LAN del client dal server](wireguard_server_access_to_client_lan_side.md).

## Consentire al client di accedere al lato LAN del server

Successivamente, abilita **Allow Remote LAN Access** su entrambe le VPN Dashboard, sia del server sia del client. Per i dettagli, per il lato client fai clic [qui](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options); per il lato server fai clic [qui](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Rendere accessibile il PC sul lato server

### PC lato server

Se vuoi accedere al PC collegato al lato LAN del server con IP **192.168.29.123**, vai alle impostazioni di Windows di quel PC e fai clic su **Remote Desktop**.

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Attivalo.

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Fai clic su **Confirm**.

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Avviare l'app Remote Desktop sul laptop client

### Laptop lato client

Cerca l'app **Remote Desktop Connection**.

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Avviala e inserisci nel riquadro l'IP del PC lato server **192.168.29.123**.

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Inserisci le credenziali del PC lato server.

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

Controllerai immediatamente da remoto il PC lato server.

Se vuoi fare il contrario, basta invertire i passaggi del PC server e del laptop client.
