# Come riservare un IP fisso per un client OpenVPN in una connessione OpenVPN autogestita?

Questo tutorial mostra come riservare un IP fisso per il client OpenVPN che si collega al tuo server. Prima di seguire i passaggi sotto, configura un router GL.iNet come server OpenVPN.

1. Accedi al pannello di amministrazione web del server OpenVPN e, dalla barra laterale sinistra, vai su **VPN** -> **OpenVPN Server**.

    Nella scheda **Configuration**, annota la **IPv4 subnet**, ad esempio 10.8.0.0/24 nell'immagine seguente, e imposta Authentication Mode su **Username and Password Only**.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Vai alla scheda **Users** e crea un nome utente e una password, come mostrato sotto.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Accedi al router tramite SSH ed esegui il seguente comando per aprire il file di script di configurazione del server OpenVPN:

    `vi /lib/netifd/proto/openserver.sh`

    Nel file aperto, controlla se nello script e presente la riga "*client-config-dir /etc/openvpn/ccd*".

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    In caso contrario, aggiungila manualmente, quindi salva e chiudi il file.

4. Vai in `/etc/openvpn/` e aggiungi una cartella ccd con `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Aggiungi un file chiamato `GLsupport`, inserisci `ifconfig-push 10.8.0.10 255.255.255.0`, quindi salva e chiudi il file.

    Verifica il contenuto con `cat GLsupport`.

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Quando usi GLsupport per collegarti al server OpenVPN, verra assegnato l'IP fisso 10.8.0.10 a questo utente GLsupport.

    - `255.255.255.0` e la subnet mask e puoi sostituirla con la subnet mask del tuo server OpenVPN.

    **Nota**: se vuoi fissare indirizzi IP per piu client OpenVPN, crea piu nomi utente e password nel passaggio 2, quindi ripeti il passaggio 5 e aggiungi file nella cartella CCD secondo l'ordine degli utenti, ad esempio user_1, user_2, user_3, seguiti dal comando `ifconfig-push` e dai rispettivi IP fissi e subnet mask.

    Ad esempio, `ifconfig-push 10.8.0.20 225.225.225.0`, `ifconfig-push 10.8.0.30 225.225.225.0`, `ifconfig-push 10.8.0.40 225.225.225.0`

6. Infine, esegui un test con il client OVPN e controlla se il Client Virtual IP (IPv4) e quello riservato.

    Ad esempio, se il client OpenVPN e un router GL.iNet, puoi accedere al pannello di amministrazione web del router client OpenVPN e andare su VPN Dashboard per verificare il Client Virtual IP (IPv4).

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(VPN Dashboard nel firmware v4.7 e precedenti)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(VPN Dashboard nel firmware v4.8)</small>

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
