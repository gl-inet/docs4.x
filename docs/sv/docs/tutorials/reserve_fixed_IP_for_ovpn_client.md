# Reservera en fast IP-adress för en OpenVPN-klient i en egen OpenVPN-anslutning {#how-to-reserve-a-fixed-ip-for-openvpn-client-in-a-self-built-openvpn-connection}

Den här guiden visar hur du reserverar en fast IP-adress för OpenVPN-klienten som ansluter till servern. Konfigurera först en GL.iNet-router som OpenVPN-server innan du följer stegen nedan.

1. Logga in på OpenVPN-serverns webbadministrationspanel och gå till **VPN** -> **OpenVPN Server** i det vänstra sidofältet.

    Anteckna **IPv4 subnet** (till exempel 10.8.0.0/24 i följande bild) på fliken **Configuration** och ändra Authentication Mode till **Username and Password Only**.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Öppna fliken **Users** och skapa ett användarnamn och lösenord enligt nedan.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Logga in på routern via SSH och kör följande kommando för att öppna OpenVPN-serverns konfigurationsskript:

    `vi /lib/netifd/proto/openserver.sh`

    Kontrollera i filen om raden "*client-config-dir /etc/openvpn/ccd*" finns i skriptet.

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    Lägg till den manuellt om den saknas. Spara och stäng sedan filen.

4. Gå till `/etc/openvpn/` och lägg till en ccd-mapp med `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Gå till `/etc/openvpn/ccd`, lägg till filen "GLsupport", skriv `ifconfig-push 10.8.0.10 255.255.255.0` och spara och stäng filen.

    Verifiera innehållet med `cat GLsupport`.

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - När du ansluter till OpenVPN-servern med GLsupport tilldelas användaren GLsupport den fasta IP-adressen 10.8.0.10.

    - "255.255.255.0" är nätmasken. Du kan ersätta den med OpenVPN-serverns nätmask.

    **Obs!** Om du vill tilldela fasta IP-adresser till flera OpenVPN-klienter skapar du flera användarnamn och lösenord i steg 2. Upprepa sedan steg 5 och lägg till filer i CCD-mappen för respektive användare, till exempel user_1, user_2 och user_3, med kommandot "ifconfig-push" och motsvarande fasta IP-adress och nätmask.

    Exempel: `ifconfig-push 10.8.0.20 255.255.255.0`, `ifconfig-push 10.8.0.30 255.255.255.0`, `ifconfig-push 10.8.0.40 255.255.255.0`

6. Testa slutligen med OVPN-klienten och kontrollera att Client Virtual IP (IPv4) är den reserverade adressen.

    Om OpenVPN-klienten är en GL.iNet-router kan du till exempel logga in på klientrouterns webbadministrationspanel och gå till VPN Dashboard för att verifiera Client Virtual IP (IPv4).

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(VPN Dashboard i firmware v4.7 och tidigare)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(VPN Dashboard i firmware v4.8)</small>

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
