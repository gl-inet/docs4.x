# Dlaczego otrzymuję komunikat podczas testu DDNS?

Po uruchomieniu testu DDNS na stronie Dynamic DNS możesz otrzymać komunikat pokazany poniżej.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

Nie jest to komunikat **Warning** ani **Error**, lecz przypomnienie informujące o stanie sieci routera.

Taki wynik zwykle odzwierciedla pozycję routera w sieci. Na przykład jeśli router GL.iNet jest skonfigurowany jako router podrzędny w sieci domowej, pojawi się ten komunikat.

Komunikat nie zniknie nawet wtedy, gdy skonfigurujesz przekierowanie portów na routerze głównym — oznacza to po prostu, że router znajduje się za NAT.

Jeśli chcesz udostępniać usługi przez NAT, na przykład na potrzeby zdalnego dostępu, wymagane są dodatkowe ustawienia.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
