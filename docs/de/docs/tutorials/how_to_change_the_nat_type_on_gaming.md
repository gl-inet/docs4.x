# So ändern Sie den NAT-Typ beim Gaming

Die meisten Spielehersteller empfehlen, UPnP auf dem Router zu aktivieren, um einen besseren NAT-Typ zu erhalten. Studien zeigen jedoch, dass UPnP kein sicheres Protokoll ist.

Sie können dasselbe Ziel auf sicherere Weise erreichen, entweder mit der DMZ-Funktion oder mit Portweiterleitung.

## Überprüfen Sie die IP Ihrer Spielkonsole oder Ihres Gaming-Geräts

Öffnen Sie die Client-Liste und prüfen Sie die Ihrem Gaming-Gerät zugewiesene IP-Adresse. Diese IP-Adresse benötigen Sie für die folgende Einrichtung.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Methode 1: DMZ

Gehen Sie in der Seitenleiste zu **Network > Port Forwarding** und aktivieren Sie die DMZ mit der IP Ihres Gaming-Geräts.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Methode 2: Portweiterleitung

Gehen Sie in der Seitenleiste zu **Network > Port Forwarding** und fügen Sie die erforderlichen Ports mit der IP Ihres Gaming-Geräts hinzu.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Beispiel: Ports für PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox-Ports

UDP 88, 3074

TCP 3074

Bei einigen Spielen müssen möglicherweise weitere Ports weitergeleitet werden. Weitere Details finden Sie auf dieser Website.

[Portweiterleitung für verschiedene Spiele](https://portforward.com/games/)

## Full Cone NAT

Sie können **Full Cone NAT** unter **Network > NAT Settings** aktivieren, um die Latenz zu verbessern.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* Diese Funktion ist ab Firmware 4.5 verfügbar.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
