# Använda WinSCP för att ändra filer på GL.iNet-routrar {#how-to-use-winscp-to-modify-files-on-glinet-routers}

WinSCP är ett lättanvänt verktyg för att redigera, kopiera och ladda ned filer eller kataloger på routern. Du kan kopiera filer mellan en lokal dator och routern med filöverföringsprotokollen FTP, SCP, SFTP, WebDAV eller S3. Verktyget används med Windows.

---

1. Ladda ned WinSCP [här](https://winscp.net/eng/download.php){target="_blank"} och installera det i Windows.

2. Anslut till routern och starta sedan WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * File protocol: Välj `SCP` som protokoll.
    * Host name: Ange routerns IP-adress. Om du inte har ändrat routerns IP-adress ska den vara `192.168.8.1`.
    * Port number: `22`
    * Username & Password: Ange `root` som användarnamn och ange ditt lösenord.

    Klicka sedan på knappen `Login`.

3. När du har loggat in har du fullständig åtkomst till routern.

    Du kan välja, visa, redigera och överföra filer och kataloger till eller från routern.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Om du till exempel vill redigera brandväggskonfigurationen går du till /etc/config, letar reda på filen firewall, högerklickar på den och väljer **Edit**.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Nu kan du redigera filinnehållet. Var försiktig så att inställningarna inte skadas.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
