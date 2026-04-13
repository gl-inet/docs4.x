# Come usare VPN Cascading sui router GL.iNet?

## Introduzione

VPN Cascading viene spesso chiamato anche "Double VPN" in alcuni contesti, anche se sui router GL.iNet puo differire leggermente. Il concetto di base e illustrato di seguito.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (router come server VPN)**: quando il router agisce come server VPN, i client collegati a questo server accedono a Internet tramite la rete ISP del router per impostazione predefinita.

**VPN 2 (router come client VPN)**: il router agisce anche come client VPN, collegandosi a un servizio VPN di terze parti.

**VPN Cascading**: il router inoltra il traffico dal tunnel VPN 1 al tunnel VPN 2, consentendo ai dispositivi collegati al router tramite VPN 1 di accedere a Internet attraverso il servizio VPN di terze parti (VPN 2) invece che tramite la rete ISP del router.

## Come abilitare VPN Cascading

### Per firmware v4.7 e precedenti

1. Per prima cosa, configura il router come server VPN. Per una maggiore velocita e consigliato il protocollo WireGuard. Fai riferimento a [questo link](../interface_guide/wireguard_server.md){target="_blank"}.

2. Esporta un file di configurazione dal router e caricalo su un dispositivo client che si colleghera al router tramite VPN.

3. Configura il router come client VPN, collegandolo a un servizio VPN di terze parti. Per una maggiore velocita e consigliato il protocollo WireGuard. Fai riferimento a [questo link](../interface_guide/wireguard_client.md){target="_blank"}.

4. Una volta connesso, la pagina **VPN Dashboard** verra visualizzata come mostrato di seguito, con il router configurato contemporaneamente come server VPN e client VPN.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Nella sezione VPN Server della stessa pagina, fai clic su **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Abilita **VPN Cascading** e fai clic su **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. VPN Cascading e ora abilitato. I dispositivi collegati al router tramite VPN accederanno a Internet attraverso il servizio VPN di terze parti, invece che tramite la rete ISP del router.

### Per firmware v4.8 e successivi

1. Per prima cosa, configura il router come server VPN. Per una maggiore velocita e consigliato il protocollo WireGuard. Fai riferimento a [questo link](../interface_guide/wireguard_server.md){target="_blank"}.

2. Esporta un file di configurazione dal router e caricalo su un dispositivo client che si colleghera al router tramite VPN.

3. Configura il router come client VPN, collegandolo a un servizio VPN di terze parti. Per una maggiore velocita e consigliato il protocollo WireGuard. Fai riferimento a [questo link](../interface_guide/wireguard_client.md){target="_blank"}.

4. Nel pannello di amministrazione web, vai su **VPN Dashboard**. Scegli quindi le istruzioni corrispondenti in base alla modalita VPN in uso.

    ??? "Global Mode"

        Se la modalita VPN e Global Mode, una volta abilitato il client VPN, come mostrato sotto, VPN Cascading verra abilitato automaticamente.

        I dispositivi collegati al router tramite VPN accederanno a Internet attraverso il servizio VPN di terze parti, invece che tramite la rete ISP del router.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        Se la modalita VPN e Policy Mode, devi configurare la regola del tunnel VPN.

        Fai clic sul riquadro grigio a sinistra.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        Seleziona l'origine del traffico a cui applicare questa regola. Per abilitare VPN Cascading, seleziona **All Clients**, oppure seleziona **Specified Connection Types** e quindi **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: include tutti i dispositivi LAN, i dispositivi di Drop-in Gateway, i dispositivi della rete ospite e i dispositivi collegati al router tramite VPN.

            Se vuoi che il traffico di tutti i dispositivi utilizzi la stessa regola del tunnel, seleziona **All Clients** e fai clic su **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: consente di specificare i dispositivi collegati al router tramite un metodo particolare, ad esempio dispositivi collegati via VPN, a cui applicare questa regola del tunnel.

            Se vuoi che i client VPN del router utilizzino una regola diversa rispetto agli altri dispositivi, seleziona **WireGuard/OpenVPN Server** e fai clic su **Apply**.

            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            Questo e un esempio di regole del tunnel VPN in Policy Mode.

            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. VPN Cascading e ora abilitato. I dispositivi collegati al router tramite VPN accederanno a Internet attraverso il servizio VPN di terze parti, invece che tramite la rete ISP del router.

6. **Test della connessione**: su un laptop collegato al router tramite VPN, apri un browser e visita [What Is My IP](https://whatismyipaddress.com/){target="_blank"} per controllare l'IP pubblico.

    Se viene mostrato che l'indirizzo IP del laptop si trova nella regione del server VPN di terze parti, che in questa guida e Buenos Aires, significa che VPN Cascading e entrato in funzione.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
