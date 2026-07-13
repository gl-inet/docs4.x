# Profilo client VPN

> Questa guida si applica al firmware v4.9 e successivi.

Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **VPN Client Profile**.

Dal firmware v4.9, [OpenVPN Client](openvpn_client.md) e [WireGuard Client](wireguard_client.md) sono stati unificati in un'unica pagina **Profilo client VPN** per una gestione più snella. Sebbene il layout sia stato leggermente modificato, le funzioni principali restano invariate. Se necessario, puoi comunque fare riferimento alle guide separate.

Questa pagina ti consente di accedere ad alcuni servizi VPN integrati e di scaricare facilmente i relativi profili per la connessione VPN, oppure di caricare manualmente i file di configurazione esportati dal sito web di altri provider VPN. Se necessario, puoi cambiare protocollo VPN nell'angolo in alto a destra.

## WireGuard

WireGuard® è una VPN moderna, leggera e ad alte prestazioni basata su crittografia all'avanguardia. Offre velocità, semplicità e praticità superiori rispetto a IPsec, e garantisce prestazioni nettamente migliori rispetto a OpenVPN.

I router GL.iNet offrono il supporto WireGuard integrato per i seguenti provider VPN. Se hai un abbonamento attivo, ti basta inserire le credenziali del servizio nella pagina **VPN Client Profile** per completare rapidamente la configurazione.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

Se usi un altro provider di servizi WireGuard, scarica un file di configurazione dal suo sito web, quindi fai clic su **Add Manually** per caricarlo sul router e usarlo per la connessione VPN. Se non sai come scaricare i file di configurazione, fai riferimento [qui](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oppure contatta il relativo supporto.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

Prendiamo [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} come esempio.

1. Fai clic su **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Inserisci **Username** e **Password**, quindi fai clic su **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    Il sistema genererà i file di configurazione per tutti i server disponibili.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Segui la guida corrispondente qui sotto in base alle tue esigenze.

    !!! note "Caso 1. Se vuoi che tutti i client connessi usino la VPN per accedere a Internet, segui questi passaggi."

        1. Seleziona il server che preferisci e fai clic sull'icona con tre puntini sulla destra per avviare la connessione.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Una volta connesso, comparirà un punto verde accanto al file di configurazione.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            La connessione VPN è ora attiva e tutti i client connessi a questo router dovrebbero usare la VPN per un accesso a Internet sicuro.

        3. (Opzionale) Se desideri che il sistema interrompa automaticamente tutto l'accesso a Internet per la tua rete locale quando la connessione VPN si interrompe inaspettatamente, impedendo l'esposizione del tuo indirizzo IP reale e dei tuoi dati online e garantendo continua privacy e sicurezza, vai su **VPN Dashboard** per abilitare il **Kill Switch**.

            * Per configurare il Kill Switch per ogni singolo tunnel VPN, fai riferimento [qui](vpn_dashboard.md#tunnel-options).
            
            * Per configurare il Kill Switch per la connessione VPN globale (ovvero l'Enhanced Kill Switch), fai riferimento [qui](vpn_dashboard.md#all-other-traffic).

    !!! note "Caso 2. Se preferisci personalizzare i criteri VPN, segui questi passaggi."

        1. Fai clic su **Go to Dashboard** in basso.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. Verrai reindirizzato a **VPN Dashboard** per configurare i criteri VPN. Fai clic [qui](vpn_dashboard.md#set-up-vpn-policy) per i dettagli.

## OpenVPN

OpenVPN è un protocollo VPN open-source che usa tecniche di rete privata virtuale per stabilire connessioni sicure site-to-site o point-to-point.

I router GL.iNet offrono il supporto OpenVPN integrato per [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Se hai un abbonamento attivo, ti basta inserire le credenziali del servizio nella pagina **VPN Client Profile** per completare rapidamente la configurazione.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Se usi un altro provider di servizi OpenVPN, scarica un file di configurazione dal suo sito web, quindi fai clic su **Add Manually** per caricarlo sul router e usarlo per la connessione VPN. Se non sai come scaricare i file di configurazione, fai riferimento [qui](openvpn_client.md#get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers) oppure contatta il relativo supporto.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

Articoli correlati

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard.md)
- [Configurare WireGuard Client sui router GL.iNet](wireguard_client.md)
- [Configurare OpenVPN Client sui router GL.iNet](openvpn_client.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
