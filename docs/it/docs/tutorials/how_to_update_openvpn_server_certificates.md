# Come aggiornare i certificati del server OpenVPN?

Questo tutorial spiega come aggiornare i certificati del server OpenVPN sui router GL.iNet.

**Nota**: questo processo richiede l'aggiornamento del certificato Root CA, che rendera' non validi tutti i certificati client esistenti, incorporati nei file di configurazione. Dovrai riesportare tutti i file di configurazione per consentire ai client OpenVPN di riconnettersi al server.

1. Accedi al pannello di amministrazione web del router e vai su **VPN** -> **OpenVPN Server**.

    Se il server OpenVPN e' in esecuzione, arresta il servizio.

2. Nella scheda Configuration, fai clic su **Advanced Configuration** per espandere le impostazioni.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Individua **Server Root Certificate** ed elimina tutto il contenuto nella casella di testo.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Anche il Server Certificate e il Server Key associati verranno rimossi automaticamente, come mostrato di seguito.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Lascia vuote tutte e tre le caselle e fai clic su **Apply** in basso. I nuovi certificati verranno generati automaticamente e inseriti nelle caselle.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. I certificati del server OpenVPN sono ora aggiornati. Fai clic su **Export Client Configuration** in basso per esportare nuovi file di configurazione per i dispositivi che devono collegarsi.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
