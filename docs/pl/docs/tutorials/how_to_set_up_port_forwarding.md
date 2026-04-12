# Jak skonfigurować przekierowanie portów na routerze głównym

Jeśli konfigurujesz serwer (taki jak [serwer OpenVPN](how_to_set_up_openvpn_server.md) lub [serwer WireGuard](build_your_own_wireguard_home_server_with_two_glinet_routers.md)) na routerze GL.iNet, który jest podłączony do routera głównego, musisz skonfigurować przekierowanie portów na routerze głównym. Zapewnia to prawidłową dostępność serwera.

Należy pamiętać, że jeśli między routerem głównym a routerem GL.iNet znajdują się inne routery, musisz skonfigurować przekierowanie portów na wszystkich tych poprzednich routerach.

## Przygotowanie

Przed skonfigurowaniem przekierowania portów zalecamy **zarezerwowanie statycznego adresu IP** dla routera GL.iNet na routerze głównym. Zapewnia to, że router GL.iNet zawsze otrzymuje stały adres IP.

W przeciwnym razie, jeśli router główny lub router GL.iNet zostanie ponownie uruchomiony, router główny może przypisać nowy adres IP do routera GL.iNet, powodując niepowodzenie reguły przekierowania portów.

Następnie skonfiguruj przekierowanie portów na routerze głównym dla routera GL.iNet.

Kroki konfigurowania przekierowania portów różnią się w zależności od marki i modelu routera. Zapoznaj się z odpowiednią sekcją poniżej.

## Używanie routera GL.iNet jako routera głównego

Zapoznaj się z [tym linkiem](../interface_guide/port_forwarding.md){target="_blank"}.

## Używanie innej marki routera jako routera głównego

!!! note "Upewnij się, że wprowadzasz następujące informacje podczas konfigurowania przekierowania portów"

    Podczas konfigurowania przekierowania portów upewnij się, że podano następujące informacje. Należy pamiętać, że terminologia może się różnić w zależności od marki i modelu routera.
    
    * **External port/Internal port:** Wprowadź używany port. Na przykład domyślne porty to **1194** (dla serwerów OpenVPN) i **51820** (dla serwerów WireGuard).
    * **Protocol:** Wybierz **All** lub **UDP/TCP**.
    * **Internal IP** (lub wyświetlany jako **Host IP**): Wprowadź adres IP WAN routera pomocniczego lub wybierz router pomocniczy z listy rozwijanej, jeśli jest dostępny.

Oto instrukcje krok po kroku konfigurowania przekierowania portów na popularnych markach i modelach routerów głównych.

Jeśli marka lub model routera głównego nie jest wymieniony poniżej, zapoznaj się z dokumentacją routera lub skontaktuj się z zespołem wsparcia w celu uzyskania dalszej pomocy.

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link 

* [Seria Deco](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Seria routerów bezprzewodowych](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero 

Zapoznaj się z [tym linkiem](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys

Zapoznaj się z [tym linkiem](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear 

Zapoznaj się z [tym linkiem](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.