# Come risolvere un conflitto di sottorete LAN?

Quando colleghi un cavo Ethernet dal router di casa alla porta WAN del router GL.iNet, a volte potresti vedere questo messaggio:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Questo accade perché il router di casa usa lo stesso IP LAN del router GL.iNet, e questo è chiamato conflitto LAN.

Segui i passaggi seguenti per cambiare la sottorete LAN.

## 1. Cambia la sottorete LAN

Fai clic sul collegamento **Change LAN Subnet** e verrai reindirizzato alla pagina di configurazione **LAN**.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Cambia il numero dopo il secondo punto (che per impostazione predefinita è **8**) con un altro numero. Ad esempio, 192.168.10.1, quindi fai clic su **Apply**.

Dopo la modifica, attendi alcuni secondi: la pagina verrà aggiornata e reindirizzata automaticamente al nuovo indirizzo IP **192.168.10.1**. Vedrai che l'avviso di conflitto di sottorete scompare.

Se la pagina non viene reindirizzata, passa al punto successivo.

## 2. Accedi con il nuovo IP LAN

Inserisci manualmente il nuovo IP LAN nella barra degli indirizzi e premi Invio.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Accedi con la password amministratore e l'avviso di conflitto di sottorete scomparirà.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
