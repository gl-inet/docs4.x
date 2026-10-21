# IPv6 {#ipv6}

IPv6, Internet Protocol version 6, è il protocollo Internet più recente progettato per sostituire IPv4. Offre un insieme più ampio di IP univoci, risolvendo il problema dell'esaurimento degli indirizzi IPv4 e supportando il numero crescente di dispositivi connessi a livello globale.

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **IPv6**.

Questa pagina consente di abilitare e configurare IPv6 sul router.

![ipv6](https://static.gl-inet.com/docs/router/en/4/interface_guide/ipv6/ipv6.png){class="glboxshadow"}

Quando IPv6 è abilitato, le interfacce WAN, come Ethernet, otterranno i rispettivi indirizzi IPv6 tramite DHCPv6. Puoi anche modificare manualmente l'indirizzo IPv6 nella pagina delle impostazioni Ethernet.

**Nota**: alcune funzioni, ad esempio firewall, GoodCloud e OpenVPN DCO, non supportano ancora IPv6. Se usi queste funzioni e IPv6 contemporaneamente, è probabile che si verifichino problemi di connettività.

Attiva **Enable IPv6**, seleziona la modalità per la rete principale e il metodo di acquisizione DNS, quindi fai clic su **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: sono disponibili quattro modalità: **Native**, **Passthrough**, **NAT6** e **Static IPv6**.

- Native: questa modalità si applica quando il router ottiene direttamente un indirizzo IPv6 pubblico e assegna automaticamente indirizzi IPv6 ai dispositivi online. Questa modalità può soddisfare le esigenze di accesso IPv6 della maggior parte degli utenti.

- Passthrough: questa modalità si applica quando i pacchetti IPv6 devono essere inoltrati direttamente senza elaborazione o conversione. Ad esempio, alcune specifiche applicazioni o servizi di rete possono richiedere la completa preservazione del contenuto dei pacchetti IPv6 per ulteriori elaborazioni o analisi; viene usata da personale tecnico per il debugging della rete o l'analisi di sicurezza.

- NAT6: questa modalità è adatta agli scenari in cui un router viene usato come gateway di gestione per assegnare indirizzi IPv6 interni dinamici a ciascun dispositivo della rete. In questa modalità, i dispositivi terminali si collegano tramite un Optical Network Terminal e ottengono un indirizzo IPv6 di rete locale.

- Static IPv6: questa modalità è adatta a dispositivi o servizi che richiedono un indirizzo IPv6 fisso, ad esempio server o stampanti di rete. Questa modalità garantisce che il dispositivo usi sempre lo stesso indirizzo IPv6, facilitando la gestione e l'accesso.

**DNS acquisition method**: determina come il router ottiene gli indirizzi dei server DNS IPv6. Sono disponibili due opzioni: **Automatic** e **Manual**.

- Automatic: il router otterrà dinamicamente gli indirizzi dei server DNS IPv6, ad esempio tramite DHCPv6.

- Manual: inserisci indirizzi di server DNS IPv6 personalizzati. Tuttavia, poiché il DNS viene usato per risolvere i nomi di dominio nei corrispondenti indirizzi IP, la configurazione manuale dei server DNS può causare errori di risoluzione DNS. Usala con cautela.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
