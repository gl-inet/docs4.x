# Konfiguracja podwójnego przewodowego portu WAN Ethernet przez adapter Ethernet na USB-A

Możesz skonfigurować podwójny przewodowy dostęp WAN Ethernet na routerze z pojedynczym portem WAN za pomocą adaptera Ethernet na USB-A. 

Routery GL.iNet obsługują popularne adaptery Ethernet na USB-A, umożliwiając konwersję przewodowego dostępu Ethernet z routera ISP na połączenie USB przez port USB routera, zapewniając routerowi dodatkowy przewodowy dostęp Ethernet obok portu WAN.

## Topologia

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Kroki konfiguracji

1. Podłącz adapter Ethernet na USB-A do portu USB routera GL.iNet i podłącz drugi koniec do routera ISP.

2. Zainstaluj sterownik USB. 

    Zaloguj się do panelu administracyjnego routera, przejdź do **Application** -> **Plug-ins** i zainstaluj sterownik sieci USB dla swojego adaptera. 

    Na przykład, jeśli używasz adaptera Realtek, zainstaluj sterownik **kmod-usb-net-rtl8152**. 

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Poczekaj na zakończenie instalacji.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Połącz przez USB Tethering.

    Po zakończeniu instalacji sterownika przejdź do sekcji **INTERNET** -> **Tethering**. 
    
    Połączenie USB zostanie wykryte, umożliwiając połączenie z routerem ISP.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Kliknij **Connect** i poczekaj minutę. Gdy zapali się zielona kropka, a na stronie wyświetlą się informacje takie jak adres IP, oznacza to, że połączenie USB Tethering zakończyło się pomyślnie.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
