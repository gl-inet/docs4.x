# DNS

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **DNS**.

Le impostazioni DNS del router controllano come i nomi di dominio vengono tradotti in indirizzi IP. Questa pagina consente di usare automaticamente i server DNS ottenuti dai dispositivi a monte, oppure di impostarne di personalizzati e configurare le priorita' DNS.

Se imposti server DNS personalizzati, tutte le query DNS verranno risolte tramite i server specificati anziche' tramite i server DNS ottenuti dalle singole interfacce di rete. In caso contrario, verranno usate le impostazioni DNS configurate per ciascuna interfaccia.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** l'attivazione di questa opzione puo' causare errori nella risoluzione DNS privata. Se la tua rete usa un captive portal, disabilita questa opzione.

- **Override DNS Settings for All Clients:** se abilitata, il router sovrascrivera' le impostazioni DNS non crittografate per tutti i client.

- **Allow Custom DNS to Override VPN DNS:** se abilitata, dopo aver impostato un DNS personalizzato, i pacchetti trasmessi attraverso il tunnel VPN verranno risolti usando il DNS personalizzato anziche' le impostazioni DNS delle connessioni VPN.

## Impostazioni del server DNS

Sono disponibili quattro modalita': Automatic, Encrypted DNS, Manual DNS e DNS Proxy.

- **Automatic**: il router usera' automaticamente il server DNS fornito dal dispositivo a monte, ad esempio modem ISP o router principale, oppure le impostazioni DNS corrispondenti a ciascuna interfaccia di rete.

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS**: sono disponibili quattro tipi di crittografia: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS, Oblivious DNS over HTTPS.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - Per DNS over TLS, seleziona un provider DNS tra Control D, NextDNS e Cloudflare.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - Per gli altri tre, cioe' DNSCrypt-Proxy, DNS over HTTPS e Oblivious DNS over HTTPS, seleziona almeno un server DNS dal repository.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS**: seleziona dall'elenco a discesa almeno un server DNS per il router.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy**: il router instradera' tutte le query DNS della LAN verso l'indirizzo del server proxy specificato, ad esempio `8.8.8.8#53`. Questa opzione puo' essere utile se nella tua rete e' in esecuzione un altro server DNS o Pi-hole.

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Modifica Hosts

Le richieste dei client verranno risolte in via prioritaria usando le regole DNS statiche che scrivi in Hosts.

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
