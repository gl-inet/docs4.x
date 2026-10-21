# Använd WinSCP för att komma åt delade filer {#use-winscp-to-access-your-share-files}

Du kan använda **WinSCP** för att komma åt delade filer med fildelningsfunktionen på **GL-Routers**.

Konfigurera dina **WebDAV**-länkar på fliken för nätverkslagring. Detaljerade konfigurationsanvisningar finns under [WebDAV](../interface_guide/network_storage.md#set-up-webdav).

## Konfigurera länkar i WinSCP {#setup-links-in-winscp}

När du har konfigurerat WebDAV kan du gå tillbaka till sidan **Share Folders** för nätverkslagring.

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Högerklicka på ikonen **"..."** och kopiera HTTPS-länken.

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Starta WinSCP och välj WebDAV samt TLS/SSL-kryptering. Klistra sedan in länken i **Host name**. Portnumret ändras automatiskt till 6008.

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Ange användarnamn och lösenord, klicka på Save och logga in. Den delade mappen öppnas.

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
