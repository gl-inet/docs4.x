# WireGuard-Client auf GL.iNet-Routern einrichten

**Hinweis**: Diese Anleitung gilt für Firmware v4.7 und höher. Für frühere Versionen siehe [hier](wireguard_client_v4.6.md).

---

WireGuard® ist ein äußerst einfaches und dennoch schnelles, modernes VPN, das modernste Kryptografie verwendet. Es wurde entwickelt, um schneller, einfacher, schlanker und nützlicher als IPsec zu sein, ohne den üblichen großen Aufwand zu verursachen. Zudem bietet es eine deutlich höhere Leistung als OpenVPN.

Um den WireGuard-Client auf einem GL.iNet-Router einzurichten, sehen Sie sich dieses Video an oder folgen Sie den nachstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Bevor Sie beginnen, stellen Sie sicher, dass Sie ein aktives Abonnement bei einem VPN-Dienstanbieter haben, der die manuelle WireGuard-Konfiguration unterstützt. Klicken Sie [hier](https://www.gl-inet.com/solutions/vpn/){target="_blank"}, um die mit GL.iNet kompatiblen WireGuard-Anbieter zu sehen.

In der Regel müssen Sie zuerst die offizielle Website des VPN-Dienstanbieters aufrufen, bei dem Sie ein Abonnement abgeschlossen haben, die Konfigurationsdatei herunterladen und diese dann auf den Router hochladen, um ihn als WireGuard-Client einzurichten. Wenn Sie nicht wissen, wie Sie die Konfigurationsdatei erhalten, lesen Sie [diese Anleitung](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oder wenden Sie sich an den Support des Anbieters.

Sie können einen WireGuard-Client über das webbasierte Admin Panel oder die [GL.iNet App](../faq/mobile_app.md) einrichten.

- **Die GL.iNet App** integriert einige WireGuard-Dienstanbieter wie AzireVPN, Mullvad VPN, OVPN, StrongVPN und PIA VPN. Das bedeutet, dass Sie die Einrichtung einfach durch Eingabe der Zugangsdaten Ihres gebuchten WireGuard-Dienstes vornehmen können. Öffnen Sie die App und folgen Sie den Anweisungen auf dem Bildschirm.

- **Das webbasierte Admin Panel** integriert nicht nur einige WireGuard-Dienstanbieter, sondern bietet auch einen Einstiegspunkt für die manuelle Konfiguration. Sie können entweder die Zugangsdaten Ihres gebuchten WireGuard-Dienstes für eine schnelle Einrichtung eingeben oder manuell eine Konfigurationsdatei hochladen, um die Einrichtung abzuschließen.

Im Folgenden finden Sie die Schritte für die Einrichtung über das webbasierte Admin Panel. Wählen Sie unten den entsprechenden WireGuard-Dienstanbieter aus, um die gewünschte Schritt-für-Schritt-Anleitung direkt aufzurufen.

* [AzireVPN einrichten](#azirevpn-einrichten)
* [Hide.me einrichten](#hideme-einrichten)
* [IPVanish einrichten](#ipvanish-einrichten)
* [Mullvad einrichten](#mullvad-einrichten)
* [NordVPN einrichten](#nordvpn-einrichten)
* [PIA (Private Internet Access) einrichten](#pia-private-internet-access-einrichten)
* [PureVPN einrichten](#purevpn-einrichten)
* [Surfshark einrichten](#surfshark-einrichten)
* [WireGuard-Client manuell einrichten (andere Anbieter)](#wireguard-client-manuell-einrichten-andere-anbieter)

## AzireVPN einrichten {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} ist ein datenschutzorientierter VPN-Dienst, der sichere, moderne und robuste Tunnel wie WireGuard bereitstellt.

Sehen Sie sich dieses Video an, um AzireVPN auf GL.iNet-Routern über das webbasierte Admin Panel oder die GL.iNet App einzurichten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Oder folgen Sie den nachstehenden Schritten, um AzireVPN über das webbasierte Admin Panel einzurichten.

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}
    
    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Verlängern.

    Wenn Sie auf **Go Renew** klicken, werden Sie zur offiziellen Website weitergeleitet, um Ihr Abonnement zu verlängern.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Hide.me einrichten {#set-up-hideme}

[Offizielle Website](https://www.hideipvpn.com/){target="_blank"}

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## IPVanish einrichten {#set-up-ipvanish}

[Offizielle Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Server auswählen.

    Wählen Sie die Server aus, mit denen Sie sich verbinden möchten, und klicken Sie auf **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Mullvad einrichten {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} ist ein VPN-Dienst, der Ihre Online-Aktivitäten, Ihre Identität und Ihren Standort privat hält.

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Geben Sie **Account** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Server auswählen.

    Wählen Sie die Server aus, mit denen Sie sich verbinden möchten, und klicken Sie auf **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}
    
    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Verlängern.

    Wenn Sie auf **Go Renew** klicken, werden Sie zur offiziellen Website weitergeleitet, um Ihr Abonnement zu verlängern.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## NordVPN einrichten {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} ist ein Online-VPN-Dienst, der Geschwindigkeit und Sicherheit kombiniert.

1. Klicken Sie [hier](https://my.nordaccount.com/){target="_blank"}, um sich mit Ihrem NordVPN-Webkonto anzumelden.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}
    
    Klicken Sie nach der Anmeldung im Nord-Dashboard links auf NordVPN und dann auf **Set up NordVPN manually**.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_dashboard.png){class="glboxshadow"}

    Anschließend finden Sie dort den **Access token**.

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/manual_setup.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/generate_new_token.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/copy_access_token.png){class="glboxshadow"}

2. Melden Sie sich im webbasierten Admin Panel des Routers an und wechseln Sie zu **VPN** -> **WireGuard Client** -> **NordVPN**. 

    Geben Sie **Token** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Server auswählen.

    Wählen Sie die Server aus, mit denen Sie sich verbinden möchten, und klicken Sie auf **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## PIA (Private Internet Access) einrichten {#set-up-pia-private-internet-access}

[Offizielle Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **PIA**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Server auswählen.

    Wählen Sie die Server aus, mit denen Sie sich verbinden möchten, und klicken Sie auf **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## PureVPN einrichten {#set-up-purevpn}

[Offizielle Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **PureVPN**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    Dadurch werden alle verfügbaren Konfigurationsdateien erstellt.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

4. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Surfshark einrichten {#set-up-surfshark}

[Offizielle Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Server auswählen.

    Wählen Sie die Server aus, mit denen Sie sich verbinden möchten, und klicken Sie auf **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Aktualisieren.

    Sie können auf **Refresh** klicken, um den öffentlichen Schlüssel zu aktualisieren, wenn keine Verbindung zum VPN-Server hergestellt werden kann.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Windscribe einrichten {#set-up-windscribe}

[Offizielle Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Server auswählen.

    Wählen Sie die Server aus, mit denen Sie sich verbinden möchten, und klicken Sie auf **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Anschließend erhalten Sie eine Liste mit Konfigurationsdateien, die den ausgewählten Servern entsprechen.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Starten Sie eine Verbindung.

    Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    Die Details der VPN-Verbindung werden außerdem im **VPN Dashboard** angezeigt.

    ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die aktuelle Liste verfügbarer Server abzurufen und Verbindungsfehler durch Serverwartung oder Abschaltung zu vermeiden.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Zugangsdaten bearbeiten oder abmelden.

    Klicken Sie auf das Zahnradsymbol, um Ihre Anmeldedaten zu bearbeiten oder sich abzumelden.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Aktualisieren.

    Sie können auf **Refresh** klicken, um den öffentlichen Schlüssel zu aktualisieren, wenn keine Verbindung zum VPN-Server hergestellt werden kann.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Alles löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen, und auswählen, ob die privaten und öffentlichen Schlüssel gleichzeitig gelöscht werden sollen.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## WireGuard-Client manuell einrichten (andere Anbieter) {#set-up-wireguard-client-manually-for-other-providers}

Wenn Sie einen anderen WireGuard-Dienstanbieter verwenden, können Sie die WireGuard-Konfigurationsdateien herunterladen und den nachstehenden Schritten folgen, um den WireGuard-Client einzurichten. Falls Sie nicht wissen, wie Sie die Konfigurationsdateien herunterladen, lesen Sie bitte [diese Anleitung](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oder wenden Sie sich an den Support des Anbieters.

Gehen Sie im webbasierten Admin Panel zu **VPN** -> **WireGuard Client**.

1. Klicken Sie auf **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. Dadurch wird in der linken Seitenleiste eine Gruppe erstellt.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Legen Sie einen aussagekräftigen Namen für die Gruppe fest (z. B. azirevpn). Laden Sie dann eine Konfigurationsdatei hoch (unterstützte Formate: zip, tar, gz, conf, txt) oder fügen Sie die Konfigurationsdetails manuell hinzu (in Textform).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Eine Konfigurationsdatei hochladen**.

        Klicken Sie in den Upload-Bereich, um Ihre WireGuard-Konfigurationsdatei hochzuladen, und klicken Sie anschließend auf **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Konfiguration manuell hinzufügen**.
    
        Klicken Sie unten im Upload-Bereich auf **Manually Add Configuration**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Legen Sie einen aussagekräftigen Namen fest und fügen Sie die Konfiguration in das Textfeld ein. Klicken Sie dann auf **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        Wenn Sie jeden Eintrag einzeln prüfen möchten, können Sie in den **Item mode** wechseln und die Konfigurationsdetails kontrollieren. Klicken Sie danach auf **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. Nach erfolgreicher Verbindung können Sie den Verbindungsstatus auf der Seite **VPN Dashboard** prüfen.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## WireGuard-Server auf GL.iNet-Routern einrichten

Wenn Sie kein Abonnement bei VPN-Diensten von Drittanbietern abschließen möchten, können Sie stattdessen zwei GL.iNet-Router einsetzen – einen als WireGuard-Server und den anderen als WireGuard-Client.

Das eignet sich besonders für Szenarien, in denen der ISP Ihres Heimnetzwerks eine öffentliche IP bereitstellt und Sie unterwegs per VPN eine Verbindung zu Ihrem Heimnetzwerk herstellen möchten, um Sicherheit zu gewährleisten und auf interne Netzwerkressourcen zuzugreifen. Dadurch entfallen die laufenden Kosten und der Aufwand eines dauerhaften Abonnements kommerzieller VPN-Dienste.

Für die Einrichtung des WireGuard-Servers lesen Sie bitte [hier](wireguard_server.md).

---

WireGuard® ist eine eingetragene Marke von Jason A.Donenfeld.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
