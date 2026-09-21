# DNS

**Nota**: il contenuto di questa pagina è stato introdotto per la prima volta nel firmware v4.11.

Se il dispositivo esegue una versione firmware diversa, usa il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 e precedenti](dns.md)

</div>

---

Sul lato sinistro del pannello di amministrazione web, vai a **DNS**.

Le impostazioni DNS del router controllano la traduzione dei nomi di dominio in indirizzi IP. Questa pagina consente di usare i server DNS ottenuti automaticamente dai dispositivi upstream o di impostarne di personalizzati. Puoi inoltre configurare le opzioni DNS e modificare le regole host statiche.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

Per impostazione predefinita, le richieste DNS del traffico che corrisponde ai criteri VPN usano i server DNS forniti dal tunnel VPN. Le altre richieste DNS usano i server ottenuti dall'interfaccia WAN attiva. Se imposti server DNS personalizzati, puoi applicarli ai tunnel VPN, al router stesso o a entrambi. Quando queste opzioni sono abilitate, le richieste DNS nell'ambito selezionato vengono risolte tramite i server specificati anziché tramite quelli ottenuti dalle relative interfacce di rete. Se non è impostato alcun server DNS personalizzato, il router usa i server ottenuti dalle relative interfacce di rete.

## DNS WAN

DNS WAN mostra i server DNS recuperati da ogni collegamento WAN, inclusi Ethernet, ripetitore, tethering e rete cellulare.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Se un collegamento WAN è attivo, i relativi indirizzi dei server DNS vengono visualizzati a destra, come mostrato di seguito.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## DNS VPN

DNS VPN mostra i server DNS ottenuti da ogni tunnel VPN attivo.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Se è in esecuzione un tunnel VPN, le richieste DNS del traffico VPN seguono la configurazione DNS VPN, come mostrato di seguito.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## DNS manuale

Il DNS manuale supporta due tipi di configurazione: **Static DNS** ed **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: se questa opzione è abilitata, per i pacchetti che attraversano il tunnel VPN verrà usato il DNS manuale personalizzato al posto delle impostazioni DNS della VPN.

- **Apply Manual DNS to Router Itself**: questa opzione è abilitata per impostazione predefinita. Quando è attiva, i servizi integrati del router, come GoodCloud, applicano le impostazioni DNS manuali personalizzate.

### DNS statico

Il DNS statico consente di inserire manualmente indirizzi di server DNS IPv4 o IPv6. Puoi digitare direttamente gli indirizzi oppure selezionare server DNS pubblici predefiniti dall'elenco a discesa.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Puoi inserire fino a quattro indirizzi di server DNS. Fai clic su **Apply** per salvare le modifiche.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### DNS crittografato

La modalità DNS crittografato supporta più provider DNS, tra cui Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS e OpenDNS. Se necessario, puoi anche specificare manualmente un server DNS crittografato.

Seleziona prima il provider DNS. Le opzioni restanti cambiano in base alla selezione.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Se selezioni un provider DNS specifico, ad esempio NextDNS, scegli un tipo di crittografia tra DNS over TLS (DoT), DNS over HTTPS (DoH) e DNS over QUIC (DoQ). DNS over QUIC (DoQ) è stato introdotto nel firmware v4.9 ed è disponibile solo con Control D, NextDNS o AdGuard DNS.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Se selezioni Manual come provider DNS, scegli un tipo di crittografia tra DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS e DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Quindi fai clic su **Add a Server** per aggiungere almeno un server DNS. Puoi inserire direttamente l'URL o il formato stamp del DNS crittografato. Per un elenco dei server pubblici, consulta [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Confronto dei tipi di crittografia"

    1. **DNS over TLS (DoT)**

        Crittografa le richieste DNS tramite una porta TLS dedicata. Separa il traffico DNS dal normale traffico web ed è facile da identificare per gli operatori di rete.

    2. **DNS over HTTPS (DoH)**

        Trasmette i dati DNS all'interno del normale traffico HTTPS. Mescola le richieste DNS con il traffico web, offrendo una maggiore privacy e aggirando i semplici filtri del traffico.

    3. **DNS over QUIC (DoQ)**

        Incapsula il DNS nel protocollo QUIC. Offre bassa latenza, riconnessione rapida e prestazioni stabili su reti instabili.

    4. **Oblivious DNS over HTTPS (ODoH)**

        Versione avanzata di DoH. Separa l'IP dell'utente dalle richieste DNS, impedendo sia al server sia ai provider di rete di tracciare l'attività di navigazione.

    5. **DNSCrypt**

        Protocollo di crittografia DNS consolidato. Autentica e crittografa il traffico DNS, con particolare attenzione alla protezione dalle manomissioni e alla compatibilità con gli ambienti di rete meno recenti.

## Opzioni DNS

Fai clic su **Options** nell'angolo superiore destro per configurare le impostazioni DNS avanzate.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Puoi attivare o disattivare queste opzioni in base alle esigenze.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: l'attivazione di questa opzione può causare errori nelle ricerche DNS private. Se la rete usa un captive portal, disabilita questa opzione.

- **Override DNS Settings of All Clients**: se abilitata, il router sostituisce le impostazioni DNS non crittografate di tutti i client.

## Modifica degli host

Fai clic sul pulsante **Edit Hosts** in alto a destra per personalizzare le regole host statiche.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

Il router assegna priorità a queste regole host quando risolve le richieste dei client connessi.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
