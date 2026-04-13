# Come accedere dal server alla LAN del client OpenVPN

Questo tutorial illustra i passaggi per accedere, dal lato server OpenVPN, alla sottorete LAN del client OpenVPN, ad esempio NAS, telecamera IP e cosi via.

## Topologia

Come mostrato sotto, il GL-AXT1800 e un server OpenVPN e il GL-MT2500 e un client OpenVPN collegato ad esso. Dal lato server puoi accedere ai dispositivi presenti nella LAN del GL-MT2500, ad esempio un NAS o il GL-MT3000, un router secondario.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Aggiungere una regola di instradamento sul server

??? "Per firmware v4.7 e precedenti"

    Accedi al pannello di amministrazione web del <u>tuo server OpenVPN</u> e vai su **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Fai clic sull'icona di routing a destra per entrare nella regola di instradamento.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    Nella finestra pop-up, fai clic sul pulsante **Add Route Rule** a destra e inserisci la sottorete a cui vuoi accedere.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Ad esempio, la sottorete LAN del client OpenVPN GL-MT2500 e **192.168.48.0/24**, quindi il Target Address e **192.168.48.0/24**.

    Gateway e il Client IP generato dal tuo server OpenVPN per questo client OpenVPN. Qui impostiamo Gateway su **10.8.0.1**, quindi fai clic su **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Nota: se hai piu client OpenVPN le cui sottoreti LAN devono essere raggiungibili, fai riferimento a [questo link](reserve_fixed_IP_for_ovpn_client.md) per riservare un Client IP per ciascun client OpenVPN prima di configurare le regole di instradamento.

??? "Per firmware v4.8 e successivi"

    Accedi al pannello di amministrazione web del <u>tuo server OpenVPN</u> e vai su **VPN** -> **OpenVPN Server**.

    Fai clic sulla scheda **Route Rules**, quindi sul pulsante **Add Route Rule** a destra.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    Nella finestra pop-up, inserisci la sottorete a cui vuoi accedere.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Ad esempio, la sottorete LAN del client OpenVPN GL-MT2500 e **192.168.48.0/24**, quindi il Target Address e **192.168.48.0/24**.

    Gateway e il Client IP generato dal tuo server OpenVPN per questo client OpenVPN. Qui impostiamo Gateway su **10.8.0.2**, quindi fai clic su **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Nota: se hai piu client OpenVPN le cui sottoreti LAN devono essere raggiungibili, fai riferimento a [questo link](reserve_fixed_IP_for_ovpn_client.md) per riservare un Client IP per ciascun client OpenVPN prima di configurare le regole di instradamento.

## 2. Consentire l'accesso remoto alla LAN del client

??? "Per firmware v4.7 e precedenti"

    Accedi al pannello di amministrazione web del <u>tuo client OpenVPN</u> e vai su **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Fai clic sull'icona dell'ingranaggio per entrare nelle opzioni del client.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    Nella finestra pop-up, abilita **Remote Access LAN**, quindi fai clic su **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Per firmware v4.8 e successivi"

    Accedi al pannello di amministrazione web del <u>tuo client OpenVPN</u> e vai su **VPN** -> **VPN Dashboard**.

    Nell'angolo in alto a sinistra del tunnel VPN, fai clic sull'icona dell'ingranaggio per entrare nelle opzioni del tunnel.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    Nella finestra pop-up, abilita **Allow Remote Access the LAN Subnet**, quindi fai clic su **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Testare la connessione

Ecco un esempio di accesso al GL-MT3000, un dispositivo nella LAN del client OpenVPN, con IP **192.168.48.211**.

Su un dispositivo collegato al tuo server OpenVPN, esegui un ping verso l'indirizzo IP del GL-MT3000, **192.168.48.211**. Questo e l'indirizzo IP che il client OpenVPN, GL-MT2500, assegna al GL-MT3000 nella propria LAN.

Se il ping ha esito positivo, significa che le impostazioni sono corrette. Potrai accedere a tutti gli altri dispositivi all'interno della sottorete LAN del client OpenVPN tramite i rispettivi indirizzi IP.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
