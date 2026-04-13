# IPv6

IPv6, Internet Protocol version 6, e' il protocollo Internet piu' recente progettato per sostituire IPv4. Offre un insieme piu' ampio di IP univoci, risolvendo il problema dell'esaurimento degli indirizzi IPv4 e supportando il numero crescente di dispositivi connessi a livello globale.

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **IPv6**.

Questa pagina consente di abilitare e configurare IPv6 sul router.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

Quando IPv6 e' abilitato, le interfacce WAN, come Ethernet, otterranno i rispettivi indirizzi IPv6 tramite DHCPv6. Puoi anche modificare manualmente l'indirizzo IPv6 nella pagina delle impostazioni Ethernet.

**Nota**: alcune funzioni, ad esempio firewall, GoodCloud e OpenVPN DCO, non supportano ancora IPv6. Se usi queste funzioni e IPv6 contemporaneamente, e' probabile che si verifichino problemi di connettivita'.

Attiva **Enable IPv6**, seleziona la modalita' per la rete principale e il metodo di acquisizione DNS, quindi fai clic su **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: sono disponibili quattro modalita': **Native**, **Passthrough**, **NAT6** e **Static IPv6**.

- Native: questa modalita' si applica quando il router ottiene direttamente un indirizzo IPv6 pubblico e assegna automaticamente indirizzi IPv6 ai dispositivi online. Questa modalita' puo' soddisfare le esigenze di accesso IPv6 della maggior parte degli utenti.

- Passthrough: questa modalita' si applica quando i pacchetti IPv6 devono essere inoltrati direttamente senza elaborazione o conversione. Ad esempio, alcune specifiche applicazioni o servizi di rete possono richiedere la completa preservazione del contenuto dei pacchetti IPv6 per ulteriori elaborazioni o analisi; viene usata da personale tecnico per il debugging della rete o l'analisi di sicurezza.

- NAT6: questa modalita' e' adatta agli scenari in cui un router viene usato come gateway di gestione per assegnare indirizzi IPv6 interni dinamici a ciascun dispositivo della rete. In questa modalita', i dispositivi terminali si collegano tramite un Optical Network Terminal e ottengono un indirizzo IPv6 di rete locale.

- Static IPv6: questa modalita' e' adatta a dispositivi o servizi che richiedono un indirizzo IPv6 fisso, ad esempio server o stampanti di rete. Questa modalita' garantisce che il dispositivo usi sempre lo stesso indirizzo IPv6, facilitando la gestione e l'accesso.

**DNS acquisition method**: determina come il router ottiene gli indirizzi dei server DNS IPv6. Sono disponibili due opzioni: **Automatic** e **Manual**.

- Automatic: il router otterra' dinamicamente gli indirizzi dei server DNS IPv6, ad esempio tramite DHCPv6.

- Manual: inserisci indirizzi di server DNS IPv6 personalizzati. Tuttavia, poiche' il DNS viene usato per risolvere i nomi di dominio nei corrispondenti indirizzi IP, la configurazione manuale dei server DNS puo' causare errori di risoluzione DNS. Usala con cautela.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
