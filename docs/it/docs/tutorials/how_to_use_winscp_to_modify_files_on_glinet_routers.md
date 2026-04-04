# Come usare WinSCP per modificare i file sui router GL.iNet

WinSCP e uno strumento semplice per modificare, copiare e scaricare file o directory sul router. Puoi copiare file tra un computer locale e il router usando i protocolli di trasferimento FTP, SCP, SFTP, WebDAV o S3. Si applica al sistema operativo Windows.

---

1. Scarica WinSCP da [qui](https://winscp.net/eng/download.php){target="_blank"} e installalo su Windows.

2. Collegati al router, quindi avvia WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * Protocollo file: scegli `SCP` come protocollo.
    * Nome host: inserisci l'IP del router. Se non hai cambiato l'IP del router, dovrebbe essere `192.168.8.1`
    * Numero di porta: `22`
    * Nome utente e password: inserisci `root` come nome utente e la tua password.

    Quindi fai clic sul pulsante `Login`.

3. Dopo l'accesso avrai il pieno controllo del router.

    Potrai scegliere, visualizzare, modificare o trasferire file e directory da e verso il router.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Ad esempio, se vuoi modificare la configurazione del firewall, puoi andare in `/etc/config`, trovare il file firewall, fare clic destro su di esso e scegliere **Edit**.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Ora puoi modificare liberamente il contenuto del file. Fai attenzione a non alterare le impostazioni in modo errato.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
