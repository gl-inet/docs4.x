# ACL

> La funzione ACL e' stata introdotta nel firmware v4.9.

ACL, abbreviazione di Access Control List, ti consente di creare regole per gestire il traffico di rete in base a protocolli di connessione, indirizzi dei dispositivi e porte. Controlla se consentire o bloccare l'accesso alla rete. Se piu' regole ACL entrano in conflitto, il sistema applica quella con priorita' piu' alta.

ACL funziona in modo diverso da Port Forwarding: ACL consente o blocca l'accesso alla rete principalmente per motivi di sicurezza, mentre Port Forwarding reindirizza il traffico esterno verso dispositivi specifici della rete locale per consentire l'accesso remoto ai servizi locali.

---

Sul lato sinistro del pannello di amministrazione web, vai su **SECURITY** -> **ACL**.

Fai clic sul pulsante **Add Rule** sulla destra.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Crea la regola ACL nella finestra pop-up, quindi fai clic su **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: inserisci un nome personalizzato per la regola.

- **Protocol**: specifica a quale tipo di traffico di rete si applica la regola. Seleziona un protocollo tra `Any`, `TCP`, `UDP`, `TCP+UDP` e `ICMP`.

- **IP Type**: definisce il formato dell'indirizzo IP del traffico di rete. Seleziona il tipo IP tra `IPv4 & IPv6`, `IPv4` e `IPv6`.

- **Source Zone**: seleziona la zona di rete da cui proviene il traffico. Opzioni disponibili: `LAN`, `Guest`, `IoT` e `WAN`.

- **Source Address**: (facoltativo) limita la regola a dispositivi o indirizzi IP sorgente specifici. Puoi selezionare un indirizzo sorgente dall'elenco a discesa.

- **Destination Zone**: indica dove e' diretto il traffico di rete. Seleziona la zona di rete di destinazione. Opzioni disponibili: `LAN`, `Guest`, `IoT` e `WAN`.

- **Destination Address**: (facoltativo) limita la regola a dispositivi o indirizzi IP di destinazione specifici. Puoi selezionare un indirizzo di destinazione dall'elenco a discesa.

- **Action**: scegli se il traffico che corrisponde a questa regola deve essere `Accept` oppure `Block`.

- **Enable**: abilita o disabilita questa regola.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.