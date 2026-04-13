# Come verificare se hai un indirizzo IP pubblico

Un indirizzo pubblico, a differenza di un indirizzo IP privato, e' un identificatore numerico univoco assegnato ai dispositivi connessi a Internet. Ti serve un IP pubblico se vuoi ospitare un sito web, configurare un server VPN o offrire altri servizi online. In genere viene fornito dal tuo Internet Service Provider.

Se non sei sicuro di avere un indirizzo IP pubblico, segui uno di questi metodi per verificarlo.

**Metodo 1: contatta direttamente il tuo Internet Service Provider**

**Metodo 2: controlla il tuo indirizzo IP nel pannello di amministrazione del router e su Internet**

1. Accedi al pannello di amministrazione del router.
    * Per i router GL.iNet, inserisci `192.168.8.1` in un browser web ed effettua l'accesso.
    * Se nella tua configurazione hai piu' di un router, accedi al pannello di amministrazione del router principale.
2. Nel pannello di amministrazione del router, individua il tuo indirizzo WAN IP, ad esempio `42.XXX.XX.`.
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. In un browser web, cerca "what is my ip".
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Se i due indirizzi IP coincidono, allora hai un indirizzo IP pubblico.
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Se non hai un indirizzo IP pubblico, puoi valutare l'uso di uno strumento di intranet penetration. Ti permette di rendere accessibili su Internet il tuo sito web, il server VPN o altri servizi anche senza un IP pubblico.

---

Articoli correlati

- [Set Up WireGuard Server on GL.iNet Router](../interface_guide/wireguard_server.md)
- [Set Up OpenVPN Server on GL.iNet Router](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
