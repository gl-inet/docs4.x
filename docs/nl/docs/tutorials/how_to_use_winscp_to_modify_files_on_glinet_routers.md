# How to use WinSCP to modify files on GL.iNet routers {#how-to-use-winscp-to-modify-files-on-glinet-routers}

WinSCP is een eenvoudig hulpmiddel om bestanden en mappen op de router te bewerken, kopiëren en downloaden. Je kunt bestanden tussen een Windows-computer en de router overdragen via FTP, SCP, SFTP, WebDAV of S3.

---

1. Download WinSCP [hier](https://winscp.net/eng/download.php){target="_blank"} en installeer het in Windows.

2. Maak verbinding met de router en start WinSCP.

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * File protocol: Choose `SCP` as the protocol.
    * Host name: voer het IP-adres van de router in. Als je dit niet hebt gewijzigd, is het `192.168.8.1`.
    * Port number: `22`
    * Username & Password: voer `root` als gebruikersnaam en je wachtwoord in.

    Then click `Login` button.

3. Na aanmelding heb je volledige toegang tot de router.

    Je kunt bestanden en mappen selecteren, bekijken, bewerken en van of naar de router overdragen.

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Ga bijvoorbeeld naar /etc/config, klik met de rechtermuisknop op het firewallbestand en kies **Edit** om de firewallconfiguratie te wijzigen.

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Je kunt de bestandsinhoud nu bewerken. Wijzig de instellingen voorzichtig.

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
