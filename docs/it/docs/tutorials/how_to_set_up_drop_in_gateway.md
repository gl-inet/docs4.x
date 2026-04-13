# Come configurare drop-in gateway su un router GL.iNet

GL.iNet offre la funzione drop-in gateway, che migliora le funzionalita' del router principale aggiungendo caratteristiche che potrebbe non avere, tra cui AdGuard Home, DNS crittografato e VPN. Usando questa funzione, puoi continuare a usare il router principale come sempre, beneficiando al tempo stesso di funzioni aggiuntive.

Puoi abilitare drop-in gateway per [tutti i dispositivi](#abilitare-drop-in-gateway-per-tutti-i-dispositivi) oppure per [dispositivi specifici](#abilitare-drop-in-gateway-per-dispositivi-specifici) collegati al router principale. Segui la sezione appropriata per la tua configurazione.

**Nota**: i modelli con firmware inferiore alla versione v4.5.0 supportano solo l'abilitazione del drop-in gateway per tutti i dispositivi. Quando il drop-in gateway e' abilitato, tutti i dispositivi client passeranno in rete attraverso il drop-in gateway, il che significa che tutto il traffico dei client connessi verra' gestito prima da questo router.

---

## Abilitare drop-in gateway per tutti i dispositivi

### 1. Collega il router GL.iNet al router principale

Collega la porta WAN del router GL.iNet alla porta LAN del router principale con un cavo Ethernet.

### 2. Abilita drop-in gateway

Esistono due metodi per abilitare drop-in gateway: tramite pannello di amministrazione del router oppure tramite app mobile GL.iNet.

??? "Uso del pannello di amministrazione web"

    1. In un browser web, inserisci `192.168.8.1`.

    2. Inserisci la password, poi fai clic su **Login**.

    3. Nella barra laterale sinistra, fai clic su **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Accanto a **Enable Drop-in Gateway Mode**, attiva l'interruttore.

    5. Seleziona **All devices are networked through drop-in gateway**.

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Fai clic su **Apply**.

??? "Uso dell'app mobile GL.iNet"

    **Nota**: prima di iniziare, installa l'app mobile GL.iNet sul tuo dispositivo.

    1. Nella schermata principale dell'app, tocca la scheda **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tocca **Enable**.

    3. Per **Devices are networked via drop-in gateway**, tocca **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Tocca **Done**.

### 3. Disabilita il server DHCP sul router principale

Accedi al router principale per disabilitare il server DHCP. Puoi fare riferimento alle istruzioni fornite dal produttore del router oppure contattare il relativo supporto.

### 4. Configura AdGuard, DNS, VPN e altre funzioni

Segui queste guide per abilitare le funzioni che desideri sul router GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

## Abilitare drop-in gateway per dispositivi specifici

### 1. Collega il router GL.iNet al router principale

Collega la porta WAN del router GL.iNet alla porta LAN del router principale con un cavo Ethernet.

### 2. Abilita drop-in gateway

Esistono due metodi per abilitare drop-in gateway: tramite [pannello di amministrazione del router](#uso-del-pannello-di-amministrazione-web) oppure tramite [app mobile GL.iNet](#uso-dellapp-mobile-glinet).

??? "Uso del pannello di amministrazione web"

    1. In un browser web, inserisci `192.168.8.1`.

    2. Inserisci la password, poi fai clic su **Login**.

    3. Nella barra laterale sinistra, fai clic su **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Accanto a **Enable Drop-in Gateway Mode**, attiva l'interruttore.

    5. Seleziona **Some devices select their own networking gateway**.

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Fai clic su **Apply**.

    **Nota**: NON chiudere questa scheda. Ti servira' inserire l'indirizzo IP mostrato sullo schermo nel passaggio successivo.

??? "Uso dell'app mobile GL.iNet"

    **Nota**: prima di iniziare, installa l'app mobile GL.iNet sul tuo dispositivo.

    1. Nella schermata principale dell'app, tocca la scheda **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tocca **Enable**.

    3. Per **Devices are networked via drop-in gateway**, tocca **part**.

        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Tocca **Done**.

    **Nota**: NON chiudere questa scheda. Ti servira' inserire l'indirizzo IP mostrato sullo schermo nel passaggio successivo.

### 3. Imposta gateway e DNS sul dispositivo specifico

??? "Windows"

    1. Collega il dispositivo al router principale.
    2. Su Windows, apri **Settings** > **Network & Internet**.
    3. In base al metodo di connessione, segui questi passaggi:
        * Ethernet: fai clic su **Ethernet**.
        * Wi-Fi: fai clic su **Wi-Fi**, poi fai clic sul nome della rete Wi-Fi.
    4. Copia l'indirizzo IPv4. Accanto a **IP assignment**, fai clic su **Edit**.
    5. Fai clic su **Manual**.
    6. Attiva **IPv4**.
    7. Inserisci le seguenti informazioni:
        * **IP address:** incolla l'indirizzo IP copiato al passaggio 4.
        * **Subnet mask:** inserisci **255.255.255.0**.
        * **Gateway:** inserisci l'indirizzo IP mostrato nella pagina **Drop-in Gateway**.
        * **Preferred DNS:** inserisci l'indirizzo IP mostrato nella pagina **Drop-in Gateway**.
    8. Fai clic su **Save**.

??? "Android"
    1. Collega il dispositivo al router principale.
    2. Su Android, apri **Settings**.
    3. Tocca **Connections** > **Wi-Fi**.
    4. Tocca l'icona **Settings** accanto alla rete a cui sei collegato.
    5. Tocca **View more**.
    6. Tocca **IP settings** > **Static**.
    7. Per **Gateway** e **DNS 1**, inserisci l'indirizzo IP mostrato nella schermata **Drop-in Gateway**.
    8. Tocca **Save**.

??? "iOS"
    1. Collega il dispositivo al router principale.
    2. Su iOS, apri **Settings**.
    3. Tocca **Wi-Fi**.
    4. Tocca la rete Wi-Fi a cui sei collegato.
    5. In **IPv4 Address**, annota **IP Address** e **Subnet Mask**.
    6. Tocca **Configure IP** > **Manual**.
    7. Inserisci le seguenti informazioni:
        * **IP Address:** inserisci l'IP Address ottenuto al passaggio 5.
        * **Subnet Mask:** inserisci la Subnet Mask ottenuta al passaggio 5.
        * **Router:** inserisci l'indirizzo IP mostrato nella schermata **Drop-in Gateway**.
    8. Tocca **Save**.
    9. Tocca **Configure DNS**, poi tocca **Manual**.
    10. Tocca **Add Server**, poi inserisci l'indirizzo IP mostrato nella schermata **Drop-in Gateway**.
    11. Tocca **Save**.

??? "Mac"
    1. Collega il dispositivo al router principale.
    2. Sul Mac, fai clic sull'icona Apple > **System Settings**.
    3. Nella barra laterale sinistra, fai clic su **Network**.
    4. Accanto alla rete a cui sei collegato, fai clic su **Details**.
    5. Fai clic su **TCP/IP**.
    6. Annota **IP Address** e **Subnet Mask**.
    7. Accanto a **Configure IPv4**, fai clic su **Manually**.
    8. Inserisci le seguenti informazioni:
        * **IP address:** inserisci l'IP Address ottenuto al passaggio 6.
        * **Subnet mask:** inserisci la Subnet Mask ottenuta al passaggio 6.
        * **Router:** inserisci l'indirizzo IP mostrato nella pagina **Drop-in Gateway**.
    9. Fai clic su **OK** > **OK**.

### 4. Configura AdGuard, DNS, VPN e altre funzioni

Segui queste guide per abilitare le funzioni che desideri sul router GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

Articolo correlato:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
