# Duales kabelgebundenes Ethernet-WAN über einen Ethernet-auf-USB-A-Adapter konfigurieren

Sie können auf einem Router mit nur einem WAN-Port über einen Ethernet-auf-USB-A-Adapter einen dualen kabelgebundenen Ethernet-WAN-Zugang konfigurieren.

GL.iNet-Router unterstützen gängige Ethernet-auf-USB-A-Adapter. Damit können Sie den kabelgebundenen Ethernet-Zugang Ihres ISP-Routers über den USB-Port des Routers in eine USB-Verbindung umwandeln und dem Router zusätzlich zum WAN-Port einen weiteren kabelgebundenen Ethernet-Zugang bereitstellen.

## Topologie

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Einrichtungsschritte

1. Stecken Sie den Ethernet-auf-USB-A-Adapter in den USB-Port Ihres GL.iNet-Routers und verbinden Sie das andere Ende mit Ihrem ISP-Router.

2. Installieren Sie den USB-Treiber.

    Melden Sie sich am Web-Adminbereich des Routers an, navigieren Sie zu **Application** -> **Plug-ins** und installieren Sie den USB-Netzwerktreiber für Ihren Adapter.

    Wenn Sie beispielsweise einen Realtek-Adapter verwenden, installieren Sie bitte den Treiber **kmod-usb-net-rtl8152**.

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Warten Sie, bis die Installation abgeschlossen ist.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Über USB Tethering verbinden.

    Sobald die Treiberinstallation abgeschlossen ist, navigieren Sie zum Abschnitt **INTERNET** -> **Tethering**.
    
    Die USB-Verbindung wird erkannt, sodass Sie eine Verbindung zu Ihrem ISP-Router herstellen können.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Klicken Sie auf **Connect** und warten Sie etwa eine Minute. Wenn ein grüner Punkt aufleuchtet und auf der Seite Informationen wie die IP-Adresse angezeigt werden, wurde die USB-Tethering-Verbindung erfolgreich hergestellt.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
