# How to Set Up Urban Shield VPN on GL.iNet Router {#how-to-set-up-urban-shield-vpn-on-glinet-router}

[Urban Shield VPN](https://urbanshieldvpn.com/) är en VPN-leverantör som erbjuder säkra och högpresterande VPN-lösningar för användare i hela världen. Tjänsten tillhandahåller förkonfigurerade GL.iNet VPN-routrar och flexibla abonnemang för säker och privat surfning. Aktivera Urban Shield VPN på routern för skydd och åtkomst till deras globala servrar.

## Setup Guide {#setup-guide}

Följande exempel visar hur GL-B3000 konfigureras som WireGuard-klient för anslutning till Urban Shield VPN.

### 1. Sign Up Urban Shield VPN {#1-sign-up-urban-shield-vpn}

Visit [Urban Shield VPN official website](https://urbanshieldvpn.com/){target="_blank"} to sign up an Urban Shield VPN account.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Power on Router {#2-power-on-router}

Slå på routern och anslut sedan en enhet, till exempel en bärbar dator eller smartphone, via en Ethernet-kabel eller Wi-Fi.

### 3. Access Web Admin Panel {#3-access-web-admin-panel}

Följ stegen nedan för att öppna webbadministrationspanelen. Om du redan är inloggad fortsätter du till [nästa del](#4-network-setup).

Öppna en webbläsare (Chrome, Edge eller Safari rekommenderas) och gå till [192.168.8.1](http://192.168.8.1){target="_blank"}. Den första konfigurationen av webbadministrationspanelen öppnas enligt bilden nedan. Ange administratörslösenordet och klicka på **Next**.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Konfigurera Wi-Fi-nätverket. Sidan visar fabriksinställda Wi-Fi-uppgifter, däribland Wi-Fi-namn (SSID) och lösenord, som du kan ändra eller behålla. Om du ändrar uppgifterna ansluter du enheten till det uppdaterade Wi-Fi-nätverket igen.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Klicka sedan på **Next** och logga in med administratörslösenordet.

### 4. Network Setup {#4-network-setup}

I det övre högra hörnet finns **Network Setup Wizard** (tillgänglig i firmware v4.7 och senare). Följ guiden och konfigurera routern för internetåtkomst innan du konfigurerar VPN.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Activate Urban Shield VPN {#5-activate-urban-shield-vpn}

Öppna **VPN** -> **WireGuard Client** på vänstermenyn. Inloggningssidan för Urban Shield VPN visas.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Ange inloggningsuppgifterna för Urban Shield VPN (**Email** och **Password**) och klicka på **Save And Continue**. Konfigurationsfiler skapas för varje server.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Välj önskad server och klicka på **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Tillgängliga servrar visas sedan i listan.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Klicka på ikonen med tre punkter för att starta anslutningen.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Once connected, a blue dot will appear to indicate a successful connection.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Du kan även kontrollera anslutningsstatusen på VPN Dashboard.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Edit Account Info or Logout {#edit-account-info-or-logout}

Klicka på kugghjulsikonen för att ändra kontoinformationen eller logga ut.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Go renew {#go-renew}

Klicka på **Go Renew** för att öppna den officiella webbplatsen och förnya prenumerationen.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Delete {#delete}

Du kan radera alla konfigurationsfiler samt den privata och offentliga nyckeln med ett klick.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
