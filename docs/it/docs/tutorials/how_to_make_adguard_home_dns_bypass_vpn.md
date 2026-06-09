# Come fare in modo che il DNS di AdGuard Home bypassi il tunnel VPN

Normalmente, VPN e AdGuard Home possono funzionare contemporaneamente sui router GL.iNet. Non si verificano problemi quando AdGuard Home non è configurato per gestire le richieste DNS.

Tuttavia, se configuri AdGuard Home per gestire tutto il traffico DNS e inoltrare le query a **server DNS pubblici a monte**, abilitare la VPN causerà errori di risoluzione DNS.

![adguardhome](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home abilitato e gestisce le richieste DNS)</small>

![adguard dns](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(Impostazioni DNS a monte di AdGuard Home)</small>

Per impostazione predefinita, tutto il traffico in uscita viene instradato attraverso il tunnel VPN. Questo costringe il traffico DNS a monte di AdGuard Home a passare attraverso la VPN, che non può raggiungere i server DNS pubblici a monte. Di conseguenza, tutti i client connessi non riusciranno a risolvere i nomi di dominio.

Per mantenere AdGuard Home funzionante mentre la VPN è attiva, puoi aggiungere una rotta statica in LuCI per inoltrare il traffico DNS a monte al gateway WAN regolare e bypassare il tunnel VPN. Segui i passaggi seguenti.

1. Accedi al pannello di amministrazione web del router e vai su **SYSTEM** -> **Advanced Settings** ->** Go to LuCI**.

    ![luci login 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Accedi con la stessa password di amministrazione.

    ![luci login 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. In LuCI, vai su **Network** -> **Routing**, quindi clicca **Add**.

    ![routing 1](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Crea una nuova rotta statica per i tuoi indirizzi DNS a monte.

    ![routing 2](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - Interface: Seleziona l'interfaccia WAN fisica **wan**.
    
    - Route type: Mantieni il valore predefinito.
    
    - Target: `[Il tuo server DNS pubblico a monte]/32`
    
        Puoi usare `nslookup` per verificare l'effettivo indirizzo IP del tuo server DNS pubblico a monte.
    
    - Gateway: `[Indirizzo IP del tuo gateway WAN a monte]`
    
        Di solito è l'indirizzo IP del tuo modem o gateway ISP, come `192.168.0.1`. Trovalo nella pagina dello stato internet del router.

    Questa rotta assicura che le query DNS a monte di AdGuard Home bypassino il tunnel VPN e vadano direttamente attraverso la connessione WAN.

4. Salva e applica le impostazioni. AdGuard Home riprenderà quindi la normale risoluzione DNS.

5. Verifica i server DNS a monte.

    Puoi verificare i tuoi server DNS a monte direttamente nell'interfaccia di AdGuard Home.
    
    Nel pannello di amministrazione web del router, vai su **APPLICATIONS** -> **AdGuard Home**, quindi clicca su **Settings Page** per aprire la dashboard di AdGuard Home.

    ![adguard settings](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    Nella dashboard di AdGuard Home, vai su **Settings** -> **DNS settings** -> **Upstream DNS servers** e clicca su **Test upstreams**. I risultati appariranno sulla destra.

    ![test upstreams](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Suggerimento**: Se hai più di un server DNS e sono un mix di IP e dominio, puoi separare il DNS di AdGuard dal DNS della VPN, il che potrebbe essere più semplice rispetto all'uso di una rotta statica.

Accedi via SSH al tuo router GL.iNet ed esegui i seguenti comandi per forzare AdGuard Home a inviare le query DNS solo attraverso la WAN.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [Contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
