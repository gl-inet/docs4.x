# Uppdatera OpenVPN-servercertifikat {#how-to-update-openvpn-server-certificates}

Den här guiden beskriver hur du uppdaterar OpenVPN-servercertifikat på GL.iNet-routrar.

**Obs!** Processen kräver att Root CA-certifikatet uppdateras, vilket gör alla befintliga klientcertifikat (inbäddade i konfigurationsfiler) ogiltiga. Du måste exportera alla konfigurationsfiler på nytt för att OpenVPN-klienterna ska kunna återansluta till servern.

1. Logga in på routerns webbadministrationspanel och gå till **VPN** -> **OpenVPN Server**.

    Stoppa tjänsten om OpenVPN-servern körs.

2. Klicka på **Advanced Configuration** på fliken Configuration för att visa inställningarna.

    ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. Leta reda på **Server Root Certificate** och radera allt innehåll i textrutan.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

    Det matchande Server Certificate och Server Key tas också bort automatiskt enligt nedan.

    ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. Lämna alla tre rutorna tomma och klicka på **Apply** längst ned. Nya certifikat genereras automatiskt och läggs in i rutorna.

    ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. OpenVPN-servercertifikaten har nu uppdaterats. Klicka på **Export Client Configuration** längst ned för att exportera nya konfigurationsfiler som enheterna kan använda för att ansluta.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
