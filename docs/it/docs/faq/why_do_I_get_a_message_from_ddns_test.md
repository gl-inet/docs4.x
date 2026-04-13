# Perché ricevo un messaggio dal test DDNS?

Quando esegui il test DDNS nella pagina Dynamic DNS, potresti ricevere un messaggio come quello mostrato di seguito.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

Non si tratta di un messaggio di **Warning** o di **Error**, ma di un promemoria che indica lo stato della rete del router.

Questo risultato riflette tipicamente la posizione del router nella rete. Ad esempio, se il router GL.iNet è configurato come router secondario nella rete domestica, verrà mostrato questo messaggio.

Non scomparirà nemmeno se hai configurato il port forwarding sul router principale: indica semplicemente che il router si trova dietro NAT.

Se devi esporre servizi attraverso NAT (ad esempio per l'accesso remoto), sono necessarie impostazioni aggiuntive.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
