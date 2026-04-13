# Jak rozwiązać konflikt podsieci LAN?

Gdy podłączysz kabel Ethernet z routera domowego do portu WAN routera GL.iNet, czasami może pojawić się następujący komunikat:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Dzieje się tak, ponieważ router domowy używa tego samego adresu LAN IP co router GL.iNet. Taka sytuacja jest nazywana konfliktem LAN.

Wykonaj poniższe kroki, aby zmienić podsieć LAN.

## 1. Zmień podsieć LAN

Kliknij odnośnik **Change LAN Subnet**, a nastąpi przekierowanie do strony ustawień **LAN**.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Zmień liczbę po drugiej kropce (domyślnie jest to **8**) na inną. Na przykład wpisz 192.168.10.1, a następnie kliknij **Apply**.

Po zmianie odczekaj kilka sekund. Strona zostanie odświeżona i automatycznie przekieruje Cię pod nowy adres IP **192.168.10.1**. Komunikat o konflikcie podsieci powinien zniknąć.

Jeśli strona nie zostanie przekierowana, przejdź do następnego kroku.

## 2. Zaloguj się przy użyciu nowego adresu LAN IP

Ręcznie wpisz zmieniony adres LAN IP w pasku adresu i naciśnij Enter.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Zaloguj się przy użyciu hasła administratora, a komunikat o konflikcie podsieci zniknie.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
