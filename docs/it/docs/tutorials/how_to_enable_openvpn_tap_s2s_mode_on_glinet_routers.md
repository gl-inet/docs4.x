# Come abilitare la modalità OpenVPN TAP-S2S sui router GL.iNet? {#how-to-enable-openvpn-tap-s2s-mode-on-glinet-routers}

## Scenari di utilizzo {#usage-scenarios}

Dopo aver abilitato la modalità TAP-S2S, il dispositivo client OpenVPN può accedere da remoto al dispositivo server OpenVPN e anche il dispositivo server OpenVPN può accedere da remoto al dispositivo client OpenVPN. Lo svantaggio è che, dopo aver abilitato TAP-S2S, le regole VPN impostate sul client OpenVPN non avranno effetto.

## Modalità TAP-S2S vs TUN {#tap-s2s-vs-tun-mode}

Topologia di rete

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

Le modalità TAP-S2S e TUN hanno lo stesso metodo di connessione fisica, ma il loro metodo di connessione logica è diverso. Ecco le differenze:

1. Quando i dispositivi sul lato LAN del GL-X3000 accedono al backend di gestione del GL-MT6000, la modalità TAP-S2S non usa un IP virtuale, mentre la modalità TUN sì.
2. Quando i dispositivi sul lato LAN del GL-X3000 accedono al backend di gestione del GL-X3000, la modalità TAP-S2S usa un IP virtuale, mentre la modalità TUN no.
3. Quando un dispositivo sul lato LAN del GL-X3000 conosce l'indirizzo IP di un dispositivo sul lato LAN del GL-MT6000, la modalità TAP-S2S consente l'accesso remoto diretto, mentre la modalità TUN non consente l'accesso diretto senza abilitare impostazioni aggiuntive.
4. In modalità TAP-S2S, il GL-X3000 deve passare attraverso il GL-MT6000 per accedere a Internet, mentre in modalità TUN il GL-X3000 può accedere direttamente a Internet. Pertanto, in modalità TAP-S2S le regole VPN impostate sul GL-X3000 non hanno effetto e devono essere seguite le regole VPN impostate sul GL-MT6000.

## Tutorial {#tutorials}

Per prima cosa, usa un router, supponiamo GL-MT6000, con un IP pubblico per avviare OpenVPN Server, imposta la modalità del dispositivo su **TAP-S2S**, fai clic su Apply e poi su **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

Inoltre, usa un router, supponiamo GL-X3000, per aprire OpenVPN Client, importa il file di configurazione scaricato nei passaggi precedenti, fai clic su **Apply** e poi abilita la funzione.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

A questo punto, l'indirizzo IP del router GL-X3000 cambierà. Puoi accedere alla dashboard di gestione del GL-MT6000, aprire **Clients** e trovare il nuovo indirizzo IP del GL-X3000.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Se il GL-MT6000 perde la connessione di rete oppure spegne il server OpenVPN, o se il GL-X3000 spegne il client OpenVPN, l'indirizzo IP del GL-X3000 verrà ripristinato.

Punti da notare:

- Entrambi i dispositivi devono essere aggiornati alla versione v4.5, altrimenti non potranno connettersi;
- TAP-S2S funziona solo con Global Proxy Mode e si regolerà automaticamente quando OpenVPN è attivo;
- Dopo aver abilitato questa funzione sul client OpenVPN, non possono essere usate le seguenti funzioni: VPN server, Adguard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping e così via.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
