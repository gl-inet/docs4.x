# Set Up WireGuard Client on GL.iNet Routers {#set-up-wireguard-client-on-glinet-routers}

Innehållet bygger på firmware v4.7 och senare. Använd väljaren för en annan version.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.7 and above" markdown="1">

- [Firmware v4.6 and earlier](wireguard_client_v4.6.md)

</div>

---

WireGuard® är ett enkelt, snabbt och modernt VPN med avancerad kryptografi och högre prestanda än OpenVPN.

Titta på videon eller följ stegen för att konfigurera WireGuard Client.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

GL.iNet-routrar har inbyggt WireGuard-stöd för följande leverantörer. Ange tjänstuppgifterna på **WireGuard Client**.

Select the corresponding WireGuard service provider below to quickly locate the step-by-step instructions.

* [Set Up AzireVPN](#set-up-azirevpn)
* [Set Up Hide.me](#set-up-hideme)
* [Set Up IPVanish](#set-up-ipvanish)
* [Set Up Mullvad](#set-up-mullvad)
* [Set Up NordVPN](#set-up-nordvpn)
* [Set Up PIA (Private Internet Access)](#set-up-pia-private-internet-access)
* [Set up PureVPN](#set-up-purevpn)
* [Set Up Surfshark](#set-up-surfshark)
* [Set Up Windscribe](#set-up-windscribe)
* [Set Up X-VPN](#set-up-x-vpn)

För andra leverantörer hämtar du en konfigurationsfil och laddar upp den till routern.

* [Set Up WireGuard Client Manually (for other providers)](#set-up-wireguard-client-manually-for-other-providers)

## Set Up AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

Videon visar AzireVPN-konfiguration via webbadministrationspanelen eller mobilappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Or follow the steps below to set up AzireVPN via web Admin Panel.

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Ange AzireVPN **Username** och **Password** och klicka på **Save and Continue**. Konfigurationsfiler skapas för varje server.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

3. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Go renew.

    Klicka på **Go Renew** för att förnya prenumerationen på den officiella webbplatsen.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Set Up Hide.me {#set-up-hideme}

[Official Website](https://hide.me/en/){target="_blank"}

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Ange Hide.me **Username** och **Password** och klicka på **Save and Continue**. Konfigurationsfiler skapas för varje server.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

3. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Set Up IPVanish {#set-up-ipvanish}

[Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Ange IPVanish **Username** och **Password** och klicka på **Save and Continue**. Konfigurationsfiler skapas för varje server.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Select servers.

    Välj servrar och klicka på **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

4. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Set Up Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} är en VPN-tjänst som skyddar aktivitet, identitet och plats.

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Ange Mullvad **Account** (16 siffror) och klicka på **Save and Continue**. Serverfiler skapas.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Select servers.

    Välj servrar och klicka på **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

4. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Go renew.

    Klicka på **Go Renew** för att förnya prenumerationen på den officiella webbplatsen.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Set Up NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} är en VPN-tjänst som kombinerar hastighet och säkerhet.

1. Click [here](https://my.nordaccount.com/){target="_blank"} to log in to your NordVPN web account.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}

    Klicka på **NordVPN** i Nord dashboard, hitta **Access Token** och klicka på **Get Access token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token1.png){class="glboxshadow"}

    Klicka på **Generate new token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token2.png){class="glboxshadow"}

    Välj utgångsdatum och klicka på **Generate token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token3.png){class="glboxshadow"}

    Kopiera den genererade åtkomsttoken.

    **Obs!** Token visas endast en gång. Kopiera den innan fönstret stängs, annars måste en ny skapas.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token4.png){class="glboxshadow"}

2. Logga in och öppna **VPN** -> **WireGuard Client** -> **NordVPN**.

    Ange **Token** och klicka på **Save and Continue**. Serverfiler skapas.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Select servers.

    Välj servrar och klicka på **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

5. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Set Up PIA (Private Internet Access) {#set-up-pia-private-internet-access}

[Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **PIA**.

1. Ange PIA **Username** och **Password** och klicka på **Save and Continue**. Konfigurationsfiler skapas för varje server.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Select servers.

    Välj servrar och klicka på **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

4. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Set Up PureVPN {#set-up-purevpn}

[Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

[PureVPN 15-days free trial](https://purevpn.com/refer-a-friend-v2?referrer=bEZTci9KcmtQSTFPbXlPak03NWtENWZaL1BHNENlR0JOMzV6RURhWFhSOD0=){target="_blank"}

1. Click [here](https://www.purevpn.com/){target="_blank"} to log in to your PureVPN dashboard.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn_login.png){class="glboxshadow"}

    Klicka på **Subscriptions**, bläddra längst ned till **credentials** och kopiera användarnamn och lösenord.

    ![purevpn credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn_credentials.png){class="glboxshadow"}

2. Logga in och öppna **VPN** -> **WireGuard Client** -> **PureVPN**.

    Ange **Username** och **Password** och klicka på **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    It will generate all available configuration files.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

3. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

4. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Set Up Surfshark {#set-up-surfshark}

[Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Ange Surfshark **Username** och **Password** och klicka på **Save and Continue**. Konfigurationsfiler skapas för varje server.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Select servers.

    Välj servrar och klicka på **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

4. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Refresh.

    Klicka på **Refresh** för att uppdatera den offentliga nyckeln om servern inte kan anslutas.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Set Up Windscribe {#set-up-windscribe}

[Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

In the web Admin Panel, go to **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Ange Windscribe **Username** och **Password** och klicka på **Save and Continue**. Konfigurationsfiler skapas för varje server.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Select servers.

    Välj servrar och klicka på **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    En lista över konfigurationsfiler för vald server visas.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

4. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Edit credentials or logout.

    Klicka på kugghjulet för att ändra inloggningsuppgifter eller logga ut.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Refresh.

    Klicka på **Refresh** för att uppdatera den offentliga nyckeln om servern inte kan anslutas.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Delete All.

    Klicka på **Delete All** för att radera alla konfigurationsfiler och välj om privata och offentliga nycklar också ska raderas.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Set Up X-VPN {#set-up-x-vpn}

[Official Website](https://xvpn.io/){target="_blank"}

**Note**: X-VPN is integrated into GL.iNet routers starting from firmware v4.11.

1. First, obtain X-VPN token on the official website.

    Click [here](https://xvpn.io/login){target="_blank"} to log in to your X-VPN web account.

    ![xvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn1.png){class="glboxshadow"}

    Klicka på **Settings**, hitta **Login Token** och klicka på **Generate**.

    ![xvpn settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn2.png){class="glboxshadow"}

    Kopiera token, som är giltig i 15 minuter.

    ![xvpn generate token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn3.png){class="glboxshadow"}

2. Logga in, öppna **VPN** -> **VPN Client Profile** och klicka på **X-VPN**.

    ![xvpn enter token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn4.png){class="glboxshadow"}

    Ange token och klicka på **Save and Continue**.

    ![xvpn enter token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn5.png){class="glboxshadow"}

3. Välj servrar och klicka på **Apply**.

    ![xvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn6.png){class="glboxshadow"}

    En lista över konfigurationsfiler för vald server visas.

    ![xvpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn7.png){class="glboxshadow"}

4. Start a connection.

    Välj server och klicka på ikonen med tre punkter för att ansluta.

    ![xvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn8.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    ![xvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn9.png){class="glboxshadow"}

    Visa anslutningsinformation och hantera tunnlar och principer på **VPN Dashboard**.

5. Update servers.

    Klicka på **Update Servers** för aktuell serverlista.

    ![xvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn10.png){class="glboxshadow"}

6. Go renew.

    Klicka på **Go Renew** för att förnya prenumerationen på den officiella webbplatsen.

    ![xvpn renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn11.png){class="glboxshadow"}

7. Delete configurations.

    Klicka på kugghjulet och välj **Delete Configurations** för att radera vissa eller alla filer.

    ![xvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn12.png){class="glboxshadow"}

8. Modify authentication information.

    Välj **Modify Authentication Information** på kugghjulet för att ändra token.

    ![xvpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn13.png){class="glboxshadow"}

    ![xvpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn14.png){class="glboxshadow" width="600"}

9. Log out.

    Välj **Logout** för att logga ut. Det raderar inloggningsuppgifter, nycklar och filer på routern. Fortsätt försiktigt.

    ![xvpn logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn15.png){class="glboxshadow"}

## Set Up WireGuard Client Manually (for other providers) {#set-up-wireguard-client-manually-for-other-providers}

För andra leverantörer hämtar du en fil och följer stegen. Se [denna guide](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) eller kontakta supporten.

In the web Admin Panel, go to **VPN** -> **WireGuard Client**.

1. Click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. It will create a group on the left sidebar.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Namnge gruppen, till exempel azirevpn, och ladda upp zip, tar, gz, conf eller txt eller lägg till text manuellt.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Upload a configuration file**.

        Klicka på uppladdningsområdet, ladda upp filen och klicka på **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Manually add configuration**.

        Klicka på **Manually Add Configuration** längst ned.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Ange ett namn, klistra in konfigurationen och klicka på **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        Byt till Item mode för att kontrollera varje post och klicka på **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Klicka på ikonen med tre punkter för att ansluta.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

    Once connected, a green dot will appear next to the configuration file.

    Kontrollera även anslutningsinformationen på **VPN Dashboard**.

## Set Up WireGuard Client via Mobile App {#set-up-wireguard-client-via-mobile-app}

Du kan även konfigurera WireGuard Client via [mobilappen](https://www.gl-inet.com/app/#download-app-glinet).

Mobilappen integrerar AzireVPN, Mullvad VPN, OVPN, StrongVPN och PIA VPN. Ange tjänstens inloggningsuppgifter.

Installera appen och följ anvisningarna på skärmen.

## Set Up WireGuard Server on GL.iNet Router {#set-up-wireguard-server-on-glinet-router}

Som alternativ till tredjepartstjänster kan två GL.iNet-routrar användas, en som WireGuard Server och en som WireGuard Client.

Det passar när hemnätverket har offentlig IP och ska nås säkert via VPN utifrån, utan löpande kommersiellt abonnemang.

For WireGuard server setup, please check [here](wireguard_server.md).

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
