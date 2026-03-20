# Urban Shield VPN auf einem GL.iNet-Router einrichten

[Urban Shield VPN](https://urbanshieldvpn.com/) ist ein VPN-Anbieter, der sich auf hochsichere und leistungsstarke VPN-Lösungen für Nutzer weltweit spezialisiert hat. Er bietet vorkonfigurierte GL.iNet-VPN-Router und flexible Abonnements an, damit Sie sicher und privat surfen können. Aktivieren Sie Urban Shield VPN einfach auf Ihrem Router, und Sie sind durch den Zugriff auf die globalen Server geschützt, sodass Sie beruhigt surfen und streamen können.

## Einrichtungsanleitung

Im folgenden Beispiel wird gezeigt, wie Urban Shield VPN auf einem GL-B3000 aktiviert wird, indem er als WireGuard-Client eingerichtet wird.

### 1. Bei Urban Shield VPN registrieren

Besuchen Sie die [offizielle Website von Urban Shield VPN](https://urbanshieldvpn.com/){class="_blank"} oder klicken Sie [hier](https://payment.urbanshieldvpn.com/sign-up), um ein Urban-Shield-VPN-Konto zu erstellen.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Einschalten und verbinden

Schalten Sie Ihren Router ein. Verbinden Sie ein Gerät per Ethernet-Kabel oder über Wi-Fi mit dem Router.

### 3. Auf das webbasierte Admin Panel zugreifen

Folgen Sie den nachstehenden Schritten, um auf das webbasierte Admin Panel zuzugreifen. Wenn Sie bereits angemeldet sind, gehen Sie bitte direkt zum [nächsten Abschnitt](#4-network-setup).

Öffnen Sie einen Webbrowser (Chrome, Edge oder Safari werden empfohlen) und rufen Sie [192.168.8.1](http://192.168.8.1){target="_blank"} auf. Sie werden zur Ersteinrichtung des webbasierten Admin Panels weitergeleitet, wie unten gezeigt. Legen Sie Ihr Admin-Passwort fest und klicken Sie auf **Next**, um fortzufahren.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Richten Sie Ihr Wi-Fi-Netzwerk ein. Auf der Seite werden die werkseitigen Wi-Fi-Daten angezeigt, einschließlich Wi-Fi-Name (SSID) und Passwort. Sie können diese übernehmen oder ändern. Wenn Sie Wi-Fi-Daten ändern, verbinden Sie Ihr Gerät bitte erneut mit dem aktualisierten Wi-Fi.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Klicken Sie anschließend auf **Next**, um sich mit Ihrem Admin-Passwort anzumelden.

### 4. Netzwerkeinrichtung

Oben rechts befindet sich ein **Network Setup Wizard** (verfügbar ab Firmware v4.7). Folgen Sie bitte diesem Assistenten, um Ihren Router vor der VPN-Einrichtung für den Internetzugang zu konfigurieren.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Urban Shield VPN aktivieren

Wählen Sie im linken Menü **VPN** -> **WireGuard Client**. Dort wird eine integrierte Urban-Shield-VPN-Anmeldeseite angezeigt.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Geben Sie Ihre **Email** und Ihr **Password** ein und klicken Sie dann auf **Save And Continue**. Dadurch werden Konfigurationsdateien für die einzelnen Server erzeugt.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Wählen Sie Ihren bevorzugten Server und klicken Sie auf **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Die verfügbaren Server erscheinen anschließend in der Liste.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Klicken Sie auf das Drei-Punkte-Symbol, um die Verbindung zu starten.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Sobald die Verbindung hergestellt ist, erscheint ein blauer Punkt als Hinweis auf eine erfolgreiche Verbindung.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Sie können den Verbindungsstatus auch im VPN Dashboard prüfen.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Kontoinformationen bearbeiten oder abmelden

Klicken Sie auf das Zahnradsymbol, um die Kontoinformationen zu bearbeiten oder sich abzumelden.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Abo verlängern

Wenn Sie auf **Go Renew** klicken, werden Sie zur offiziellen Website weitergeleitet, um Ihr Abonnement zu verlängern.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Löschen

Sie können alle Konfigurationsdateien sowie den privaten und den öffentlichen Schlüssel mit einem Klick löschen.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
