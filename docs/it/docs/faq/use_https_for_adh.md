# Accedere via HTTPS al router GL.iNet e ad AdGuard Home

Se vuoi usare HTTPS per accedere al router GL.iNet e ad AdGuard Home, segui i passaggi riportati di seguito.

## 1. Aggiorna il certificato e la chiave nel router GL.iNet

Per prima cosa, richiedi un certificato SSL oppure usa un certificato SSL autofirmato.

Poi accedi via SSH al router GL.iNet oppure usa WinSCP per caricare sul router il certificato e la chiave aggiornati. I percorsi sono:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Abilita AdGuard Home

Accedi al pannello di amministrazione web GL.iNet -> APPLICATIONS -> AdGuard Home, quindi abilita AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Poi fai clic su **Settings Page** nella parte superiore di questa pagina: verrai reindirizzato alla pagina delle impostazioni di AdGuard Home.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Modifica le impostazioni di Encryption

Nella pagina delle impostazioni di AdGuard Home, vai su Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Seleziona la casella **Enable Encryption** in alto a sinistra e inserisci 3001 come porta HTTPS.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Aggiungi i percorsi del certificato e della chiave aggiornati, quindi fai clic su **Save**.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

A questo punto potrai usare HTTPS per visitare **192.168.8.1** oppure **192.168.8.1:3001**.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
