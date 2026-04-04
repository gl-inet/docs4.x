# Come consentire l'accesso alla WAN quando il client VPN e' abilitato?

Quando il client VPN e' abilitato sui router GL.iNet, nella modalita' globale predefinita i dispositivi LAN non possono accedere ai dispositivi o ai servizi della WAN locale, poiche' tutto il traffico proveniente dalla LAN viene instradato attraverso il tunnel VPN invece che attraverso la rete a monte, WAN, per evitare DNS leak.

Questo tutorial presenta i passaggi per rendere accessibili i servizi della WAN locale, ad esempio stampante, NAS e cosi' via, ai dispositivi LAN del client VPN.

![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Per firmware v4.7 e precedenti

Accedi al pannello di amministrazione web del client VPN e vai su **VPN** -> **VPN Dashboard** -> **VPN Client**. Fai clic su **Global Options** nell'angolo in alto a destra.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Abilita **Allow Access WAN** e fai clic su **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

Se questa opzione e' abilitata, mentre la VPN e' connessa i dispositivi client potranno comunque accedere ai servizi WAN nella subnet superiore, ad esempio stampante, NAS e cosi' via.

## Per firmware v4.8 e successivi

L'opzione **Allow Access WAN** e' stata rimossa dal VPN Dashboard nel firmware v4.8. Tuttavia, puoi ottenere l'accesso alla WAN locale tramite VPN policy.

Segui i passaggi seguenti.

1. Accedi al pannello di amministrazione web del client VPN e vai su **VPN** -> **VPN Dashboard**.

    Fai clic sulla modalita' nell'angolo in alto a destra.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Passa a **Policy Mode** e fai clic su **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    La pagina verra' aggiornata e mostrata come segue.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Fai clic sul riquadro centrale per impostare la destinazione del tunnel.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Seleziona **Exclude Speficied Domain / IP**, inserisci la subnet WAN del router, poi fai clic su **Apply**.

    In questo modo tutto il traffico verso la subnet WAN verra' instradato attraverso la WAN locale invece che tramite il tunnel VPN.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    Qui usiamo come esempio la subnet `192.168.0.1/24`. Inserisci questa subnet e applica; il tunnel VPN verra' mostrato come segue.

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Come faccio a sapere qual e' la subnet WAN del router GL.iNet?"

        La subnet WAN del router GL.iNet in genere si trova nella pagina INTERNET. E' determinata dal dispositivo a monte a cui si collega l'interfaccia WAN del router, ad esempio un modem ISP o un gateway a monte.

        Ad esempio, se il router funziona come router secondario, quindi la sua porta WAN e' collegata a un'altra rete locale come un modem ISP o la porta LAN del router principale, e il WAN IP del router e' `192.168.1.165`, il Gateway e' `192.168.1.1` e la Subnet Mask e' `255.255.255.0`, una maschera comune per reti di piccole dimensioni, allora la corrispondente subnet WAN e' `192.168.1.0/24`. Questa coincide anche con la subnet LAN del dispositivo a monte.

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Nota**: la lunghezza del prefisso di `192.168.1.0/24` e' 24, che corrisponde alla subnet mask `255.255.255.0`. Se la WAN Subnet Mask del router non e' `255.255.255.0`, il prefisso della subnet WAN non sara' `/24`. Conferma quindi la subnet WAN in base alla configurazione WAN reale.

3. Fai clic sul riquadro di destra per impostare l'azione del tunnel, cioe' usare o non usare la VPN.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Seleziona **Use VPN** e scegli un file di configurazione VPN. Poi fai clic su **Apply**.

    Se non c'e' alcuna configurazione disponibile, caricane prima una per impostare il router come client VPN. Poi torna a questa pagina, seleziona Use VPN e scegli un file di configurazione VPN. Quindi fai clic su Apply.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Attiva l'interruttore nell'angolo in alto a destra per abilitare questo tunnel VPN. Iniziera' a connettersi.

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Attendi alcuni minuti. Una volta connesso correttamente, diventera' verde.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Cerca il tuo IP pubblico per testare la connessione VPN. Ad esempio, apri un browser e visita [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Verranno mostrati il tuo indirizzo IP pubblico e la tua posizione, come indicato di seguito.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Accedi ai dispositivi o ai servizi presenti nella subnet WAN e verifica se l'accesso avviene correttamente.

    Puoi usare il comando ping per testare la connettivita'.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
