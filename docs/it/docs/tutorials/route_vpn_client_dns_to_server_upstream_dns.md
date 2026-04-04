# Come instradare le query DNS del client VPN verso il DNS upstream del server VPN?

Questo tutorial illustra i passaggi per reindirizzare tutte le query DNS dei client VPN verso il tuo server DNS self-hosted presente sul lato LAN del router principale, a monte del server VPN.

## Topologia

In questo tutorial utilizziamo **Flint 3 (GL-BE9300)** e **Slate 7 (GL-BE3600)** come esempi.

Flint 3 e il server VPN, che ha un router principale sulla rete upstream, mentre Slate 7 e il client VPN che si collega a Flint 3.

Quando viene stabilito un tunnel VPN tra server e client, per impostazione predefinita le query DNS del client VPN vengono prima inviate al server VPN, poi inoltrate al router principale e infine risolte dai server DNS assegnati dall'ISP configurati sulla WAN del router principale.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Tuttavia, se hai distribuito un server DNS self-hosted, con indirizzo IP `192.168.1.13`, sul router principale, sono necessarie configurazioni aggiuntive per instradare le query DNS verso questo server DNS self-hosted.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Configurazione

1. Accedi al pannello di amministrazione web di Flint 3 e vai su **NETWORK** -> **DNS**. Imposta DNS Server Mode su **Manual DNS** e inserisci l'indirizzo IP del tuo server DNS.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Vai su **VPN** -> **WireGuard Server** -> scheda **Configuration** e annota l'IPv4 Address, che di solito e `10.0.0.1/24` oppure `10.1.0.1/24`, a seconda del modello e della versione firmware.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Passa alla scheda **Profiles**, aggiungi una configurazione client ed esporta un profilo per Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Apri il profilo e verifica che il DNS corrisponda all'indirizzo IP del server VPN ottenuto nel passaggio 2.

    Per evitare errori di risoluzione DNS, elimina `64.6.64.6` se presente e salva le modifiche.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Nel pannello di amministrazione web di Flint 3, fai clic sul pulsante **Start** nella parte superiore della pagina **WireGuard Server** per avviare il server.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Accedi al pannello di amministrazione web di Slate 7 e vai su **VPN** -> **WireGuard Client**.

    Fai clic su **Add Manually** e carica il profilo modificato.

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Fai clic sull'icona con i tre puntini per avviare la connessione VPN. Se l'indicatore di stato diventa verde, significa che la connessione VPN e riuscita.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Verificare la risoluzione DNS

Esegui il seguente comando per catturare il traffico DNS sul client VPN. Vedrai che tutto il traffico DNS del client VPN viene inviato al server VPN, cioe `10.0.0.1` in questo esempio.

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Esegui il seguente comando per catturare il traffico DNS sul server VPN. Vedrai che tutto il traffico DNS del client VPN viene infine inviato al server DNS self-hosted, cioe `192.168.1.13` in questo esempio.

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
