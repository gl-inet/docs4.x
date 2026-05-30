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

### Automatic

In questa modalita', il router usera' automaticamente il server DNS fornito dal dispositivo a monte, ad esempio modem ISP o router principale, oppure le impostazioni DNS corrispondenti a ciascuna interfaccia di rete.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS

Fai riferimento alle istruzioni seguenti in base alla versione del firmware.

!!! note "Per il firmware v4.8 e precedenti"

    Sono disponibili quattro tipi di crittografia: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS e Oblivious DNS over HTTPS.

    Seleziona prima **Encryption Type**. Le opzioni rimanenti cambieranno in base alla selezione effettuata.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - Per **DNS over TLS (DoT)**, scegli un provider DNS tra **Control D**, **NextDNS** e **Cloudflare**.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - Per gli altri tre, cioe' **DNSCrypt-Proxy**, **DNS over HTTPS** e **Oblivious DNS over HTTPS**, seleziona almeno un server DNS dal repository.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

!!! note "Per il firmware v4.9 e successivi"

    Oltre a Control D, NextDNS e Cloudflare, la modalita' Encrypted DNS supporta anche altri provider DNS, tra cui **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** e **OpenDNS**. Se necessario, puoi anche specificare manualmente un server DNS crittografato.

    Seleziona prima **DNS Provider**. Le opzioni rimanenti cambieranno in base alla selezione effettuata.

    ![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

    - Se selezioni un provider DNS specifico, ad esempio NextDNS, scegli un tipo di crittografia tra **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** e **DNS over QUIC (DoQ)**. Tieni presente che **DNS over QUIC (DoQ)** e' stato introdotto nel firmware v4.9 ed e' disponibile solo quando usi Control D, NextDNS o AdGuard DNS come provider DNS.

        ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

    - Se selezioni **Manual** come provider DNS, scegli un tipo di crittografia tra **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** e **DNSCrypt**.

        ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

        Successivamente, fai clic su **Add a Server** per aggiungere almeno un server DNS. Puoi inserire direttamente l'URL o il formato stamp del DNS crittografato. Per un elenco di server pubblici, fai riferimento a [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

        ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Confronto tra i tipi di crittografia

1. **DNS over TLS (DoT)**

    Crittografa le query DNS tramite una porta TLS dedicata. Separa il traffico DNS dal normale traffico web ed e' facilmente identificabile dagli operatori di rete.

2. **DNS over HTTPS (DoH)**

    Trasmette i dati DNS all'interno del normale traffico HTTPS. Mescola le richieste DNS con il traffico web ordinario per offrire una maggiore privacy e aggirare i filtri del traffico piu' semplici.

3. **DNS over QUIC (DoQ)**

    Incapsula il DNS nel protocollo QUIC. Offre bassa latenza, riconnessione rapida e prestazioni stabili su reti instabili.

4. **Oblivious DNS over HTTPS (ODoH)**

    Una versione avanzata di DoH. Separa l'IP dell'utente dalle query DNS, impedendo sia al server sia ai provider di rete di tracciare l'attivita' di navigazione.

5. **DNSCrypt**

    Un protocollo di crittografia DNS maturo. Autentica e crittografa il traffico DNS, con particolare attenzione alla protezione dalle manomissioni e alla compatibilita' con ambienti di rete legacy.

### Manual DNS

In questa modalita', puoi personalizzare il server DNS del router. Seleziona dall'elenco a discesa almeno un **DNS Server** per il router.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy

In questa modalita', il router instradera' tutte le query DNS della LAN verso l'indirizzo del server proxy che specifichi, ad esempio `8.8.8.8#53`. Questa opzione puo' essere utile se nella tua rete e' in esecuzione un altro server DNS o Pi-hole.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Modifica Hosts

Puoi fare clic sul pulsante **Edit Hosts** in alto a destra per personalizzare le regole host statiche.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

Il router dara' priorita' a queste regole host durante la risoluzione delle richieste dei client connessi.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
