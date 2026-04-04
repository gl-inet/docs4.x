# Come accedere dal server alla LAN del client WireGuard

Questo tutorial illustra i passaggi per accedere, dal lato server WireGuard, alla sottorete LAN del client WireGuard, ad esempio telecamera IP, NAS e cosi via.

## Topologia

Come mostrato sotto, il GL-MT2500 e un server WireGuard e il GL-AXT1800 e un client WireGuard collegato ad esso. Dal lato server puoi accedere ai dispositivi presenti nella LAN del GL-AXT1800, ad esempio una telecamera IP o un NAS.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Aggiungere una regola di instradamento sul server

??? "Per firmware v4.7 e precedenti"

    Accedi al pannello di amministrazione web del <u>tuo server WireGuard</u>, quindi vai su **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Fai clic sull'icona di routing a destra per entrare nella regola di instradamento.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Fai clic su **Add Route Rule** nell'angolo in alto a destra e inserisci la sottorete a cui vuoi accedere.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Ad esempio, la sottorete LAN del client WireGuard GL-AXT1800 e **192.168.8.0/24**, quindi il Target Address e **192.168.8.0/24**.

    Gateway e l'indirizzo IP del client generato dal tuo server WireGuard per questo client WireGuard. Puoi trovarlo nella scheda **Profiles** della pagina **WireGuard Server**. Come mostrato sotto, l'IP client del client WireGuard GL-AXT1800 e **10.0.0.4**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    Quindi imposta Gateway su **10.0.0.4** e Scope su **global**, poi fai clic su **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Per firmware v4.8 e successivi"

    Accedi al pannello di amministrazione web del <u>tuo server WireGuard</u>, quindi vai su **VPN** -> **WireGuard Server**.

    Fai clic sulla scheda **Route Rules** e poi su **Add Route Rule** sul lato destro.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    Nella finestra pop-up, inserisci la sottorete a cui vuoi accedere.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Ad esempio, la sottorete LAN del client WireGuard GL-AXT1800 e **192.168.8.0/24**, quindi il Target Address e **192.168.8.0/24**.

    Gateway e l'indirizzo IP del client generato dal tuo server WireGuard per questo client WireGuard. Puoi trovarlo nella scheda **Profiles** della stessa pagina. Come mostrato sotto, l'IP client del client WireGuard GL-AXT1800 e **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Quindi imposta Gateway su **10.1.0.2**, poi fai clic su **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Consentire l'accesso remoto alla LAN del client

??? "Per firmware v4.7 e precedenti"

    Accedi al pannello di amministrazione web del <u>tuo client WireGuard</u> e vai su **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Fai clic sull'icona dell'ingranaggio sul lato destro di WireGuard.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    Nella finestra pop-up, abilita **Remote Access LAN**, quindi fai clic su **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Per firmware v4.8 e successivi"

    Accedi al pannello di amministrazione web del <u>tuo client WireGuard</u> e vai su **VPN** -> **VPN Dashboard**.

    Nell'angolo in alto a sinistra del tunnel VPN, fai clic sull'icona dell'ingranaggio per entrare nelle opzioni del tunnel.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    Nella finestra pop-up, abilita **Allow Remote Access the LAN Subnet**, quindi fai clic su **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Testare la connessione

Verifica se riesci ad accedere ai dispositivi LAN del client WireGuard dal lato server.

Puoi testare la connessione tramite ping. Ad esempio, su un dispositivo collegato al server WireGuard, GL-MT2500, esegui il ping dell'indirizzo IP di un dispositivo all'interno della LAN del client WireGuard, GL-AXT1800, e verifica se la risposta arriva correttamente.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
