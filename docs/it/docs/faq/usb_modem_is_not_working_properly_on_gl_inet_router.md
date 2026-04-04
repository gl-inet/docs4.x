# Il modem USB non funziona correttamente sul router GL.iNet

Alcuni router GL.iNet hanno porte USB: gli utenti possono collegare un modem USB alla porta USB per configurare l'accesso a Internet, anche per realizzare scenari Multi-WAN se combinato con altri metodi di accesso a Internet.

Tuttavia, potresti riscontrare il problema per cui alcuni modem USB (come ZTE F50 Mobile Wi-Fi Hotspot) non possono essere usati normalmente sul router, causando frequenti interruzioni di rete.

Questo può dipendere da un problema di compatibilità tra la porta USB del router (di solito USB 3.0) e il Wi-Fi 2.4G, che porta il modem USB a disconnettersi continuamente e a non poter accedere normalmente a Internet.

Per risolvere il problema, puoi cambiare la specifica della porta USB da USB 3.0 a USB 2.0.

Accedi al pannello di amministrazione del router GL.iNet e vai su **SYSTEM -> Overview -> External Storage**.

Vedrai un'opzione per **USB Protocol Switch**.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Passa a USB 2.0 e verrà mostrato un messaggio come quello riportato di seguito. Fai clic su **Switch** per continuare.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Quando viene mostrato che il protocollo USB è USB 2.0, significa che il cambio è stato eseguito correttamente.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Successivamente, verifica se la connessione Internet è migliorata.

---

Articoli correlati

- [Compatible Modems](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
