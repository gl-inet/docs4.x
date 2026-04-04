# Dynamic DNS

Dynamic Domain Name Service (Dynamic DNS o DDNS) e' un servizio usato per associare un nome di dominio all'indirizzo IP dinamico di un dispositivo di rete. Con Dynamic DNS puoi accedere al router da remoto. Per questa funzione e' richiesto un indirizzo IP pubblico Internet.

## Abilitare DDNS

Sul lato sinistro del pannello di amministrazione web, vai su **APPLICATIONS** -> **Dynamic DNS**.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Attiva **Enable DDNS**, accetta i **Terms of Services & Privacy Policy**, quindi fai clic su **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Fai clic su **Security Settings** nell'angolo inferiore destro.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

Nella finestra pop-up, controlla che il protocollo di accesso remoto che vuoi usare sia abilitato. In caso contrario, vai su SYSTEM -> Security -> Remote Access Control per abilitarlo.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Abilita il protocollo di accesso remoto desiderato e fai clic su **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Potrebbe esserci un ritardo fino a 10 minuti nella sincronizzazione dei record tra i server DNS. Questo puo' impedirti di accedere immediatamente tramite il nome di dominio DDNS dopo l'attivazione o quando cambia il tuo IP pubblico.

**Nota**: se abiliti DDNS e VPN Client contemporaneamente, assicurati che **Services From GL.iNet Use VPN** sia disabilitato. Questa funzione si trova nelle [VPN Client Options](vpn_dashboard.md#tunnel-options) del VPN Dashboard.

## Verificare se DDNS funziona

Puoi verificare se DDNS funziona usando lo strumento di test DDNS oppure controllando manualmente tramite comandi.

=== "Usare lo strumento DDNS Test"

    Nella pagina Dynamic DNS, fai clic su **DDNS Test**.

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Assicurati che l'indirizzo IP ottenuto dalla risoluzione del dominio DDNS corrisponda all'IP WAN del router.

    In caso contrario, nella parte superiore apparira' un avviso giallo che indica che il router potrebbe trovarsi dietro NAT e che devi configurare il port forwarding sul router a monte.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Controllo manuale"

    1. Usa il comando `nslookup` per ottenere la mappatura tra nome di dominio e indirizzo IP, come mostrato di seguito.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        Sostituisci "xxxxxxx.glddns.com" nell'immagine sopra con il tuo Host Name.

        "8.8.8.8" nell'immagine sopra e' il DNS di Google. Usalo oppure sostituiscilo con un altro DNS, quindi premi Invio.

    2. Se come risultato ottieni un indirizzo IP pubblico, ad esempio "103.81.180.10" come nell'immagine seguente, significa che il tuo dominio DDNS e' stato associato correttamente a un indirizzo IP pubblico.

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}

        Su un dispositivo connesso al router, cerca "what is my ip address" in un browser oppure visita un sito come [What Is My IP Address](https://whatismyipaddress.com){target="_blank"}. Otterrai il tuo indirizzo IP pubblico. Confronta i due indirizzi IP ottenuti dai passaggi 1 e 2. Se coincidono, DDNS e' attivo; in caso contrario, non lo e'.

    3. Se ricevi un messaggio `** server can't find xxxxxxx.glddns.com: NXDOMAIN`, come mostrato di seguito, significa che la risoluzione del dominio non e' riuscita e che il tuo dominio DDNS non e' stato associato correttamente a un indirizzo IP pubblico.

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## Accesso remoto HTTPS

!!! Note

    1. Per l'accesso remoto HTTPS e' necessario un indirizzo **Public IP**.

        Fai clic [qui](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) per verificare se il tuo Internet Provider Service (ISP) ti assegna un indirizzo IP pubblico.

    2. Se il router si trova dietro NAT, configura il port forwarding (porta **443**) sul router a monte per l'accesso HTTPS.

Segui i passaggi seguenti per abilitare l'accesso remoto HTTPS per il router.

1. Nella pagina Dynamic DNS, attiva **Enable DDNS**, accetta i **Terms of Services & Privacy Policy**, quindi fai clic su **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Nel pannello di amministrazione web, vai su SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Abilita **HTTPS Remote Access** e fai clic su **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Una volta abilitato, potrai accedere al pannello di amministrazione del router da qualsiasi luogo usando il nome host DDNS tramite **HTTPS** (ad esempio `https://xxxxxxx.glddns.com`).

Se il port forwarding e' configurato, accedi usando `https://xxxxxxx.glddns.com:external_port` (sostituisci `external_port` con il numero di porta effettivo).

**Nota**: questa funzione usa certificati autofirmati, quindi i browser mostreranno **Your connection is not private** quando accedi al pannello di amministrazione del router tramite il nome host DDNS su **HTTPS**, come mostrato di seguito (la porta 8001 e' usata sotto come esempio).

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Per procedere con l'accesso remoto HTTPS, fai clic su **Advanced** in basso.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Poi fai clic su **Proceed to xxxxxxx.glddns.com** per continuare.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

A questo punto potrai accedere al pannello di amministrazione web usando il nome host DDNS tramite HTTPS.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## Accesso remoto SSH

!!! Note

    1. Per l'accesso remoto SSH e' necessario un indirizzo **Public IP**.

        Fai clic [qui](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) per verificare se il tuo Internet Provider Service (ISP) ti assegna un indirizzo IP pubblico.

    2. Se il router si trova dietro NAT, configura il port forwarding (porta **22**) sul router a monte per l'accesso SSH.

Segui i passaggi seguenti per abilitare l'accesso remoto SSH per il router.

1. Nella pagina Dynamic DNS, attiva **Enable DDNS**, accetta i **Terms of Services & Privacy Policy**, quindi fai clic su **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Nel pannello di amministrazione web, vai su SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Abilita **SSH Remote Access** e fai clic su **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Una volta abilitato, potrai accedere al pannello di amministrazione del router da qualsiasi luogo usando il nome host DDNS tramite **SSH** (ad esempio `ssh root@xxxxxxx.glddns.com`).

Se il port forwarding e' configurato, accedi usando `ssh root@xxxxxxx.glddns.com:external_port` (sostituisci `external_port` con il numero di porta effettivo).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
