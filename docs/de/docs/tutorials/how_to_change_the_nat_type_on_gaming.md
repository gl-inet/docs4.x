# So ändern Sie den NAT-Typ beim Gaming {#how-to-change-the-nat-type-on-gaming}

Einige Spieleentwickler empfehlen, UPnP auf dem Router zu aktivieren, um einen besseren NAT-Typ zu erhalten. UPnP birgt jedoch potenzielle Sicherheitsrisiken.

Sie können dasselbe Ziel mit DMZ oder Portweiterleitung auf Ihrem Router erreichen. Bevor Sie eine dieser Funktionen aktivieren, sollten Sie deren Funktionsweise und die damit verbundenen Sicherheitsrisiken verstehen.

## Überprüfen Sie die IP Ihrer Spielkonsole oder Ihres Gaming-Geräts {#check-your-game-ip}

Melden Sie sich zunächst bei Ihrem Router an. Öffnen Sie die Client-Liste und prüfen Sie die Ihrem Gaming-Gerät zugewiesene IP-Adresse. Diese IP-Adresse benötigen Sie für die folgende Einrichtung.

![gameip](https://static.gl-inet.com/docs/router/de/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Methode 1: DMZ {#method-1-dmz}

Gehen Sie in der Seitenleiste zu **Network** -> **Port Forwarding** und aktivieren Sie die DMZ mit der IP Ihres Gaming-Geräts.

![dmz](https://static.gl-inet.com/docs/router/de/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Methode 2: Portweiterleitung {#method-2-port-forward}

Gehen Sie in der Seitenleiste zu **Network** -> **Port Forwarding** und fügen Sie die erforderlichen Ports mit der IP Ihres Gaming-Geräts hinzu.

![inputport](https://static.gl-inet.com/docs/router/de/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Beispiel: Ports für PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/de/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox-Ports

UDP 88, 3074

TCP 3074

Bei einigen Spielen müssen möglicherweise weitere Ports weitergeleitet werden. Weitere Details finden Sie auf dieser Website.

[Portweiterleitung für verschiedene Spiele](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

Sie können Full Cone NAT aktivieren, um die Latenz zu verbessern. Diese Funktion ist seit Firmware v4.5 verfügbar.

Gehen Sie zu **Network** -> **NAT Settings**, aktivieren Sie bei Bedarf **Full Cone NAT** und klicken Sie auf **Apply**.

![conenat](https://static.gl-inet.com/docs/router/de/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
