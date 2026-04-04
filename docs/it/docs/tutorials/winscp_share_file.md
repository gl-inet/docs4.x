# Usare WinSCP per accedere ai file condivisi

Puoi usare **WinSCP** per accedere ai file condivisi tramite la funzione di condivisione file dei **router GL.iNet**.

Configura prima i collegamenti **WebDAV** nella scheda di archiviazione di rete. Per i dettagli di configurazione, fai riferimento alla guida [WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav).

## Configurare i collegamenti in WinSCP

Dopo aver configurato WebDAV, puoi tornare alla pagina **Share Folders** dell'archiviazione di rete.

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Fai clic con il tasto destro sull'icona **"..."** e copia il collegamento HTTPS.

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Avvia WinSCP e seleziona WebDAV, quindi seleziona anche la crittografia TLS/SSL. Poi incolla il collegamento nel campo **Host name**; il numero di porta cambiera automaticamente in 6008.

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Inserisci nome utente e password, quindi fai clic su save e login: la cartella condivisa verra aperta.

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
