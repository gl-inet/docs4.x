# Komunikat o problemie i rozwiązania dla GL-X3000/GL-XE3000/GL-X2000, które nie działają z kartami SIM EE

Drodzy Klienci GL.iNet,

Ostatnio zauważyliśmy, że część klientów napotyka problemy z łącznością w modelach GL-X3000/GL-XE3000/GL-X2000 podczas korzystania z kart SIM EE. Dalsza analiza wykazała, że niektóre karty SIM EE obsługują wyłącznie protokół IPv4. Tymczasem domyślne ustawienia routerów komórkowych GL.iNet jednocześnie włączają IPv4 i IPv6, co powoduje ten problem.

## Rozwiązania i obejścia

1. **Aktualizacja firmware**

    Udostępniliśmy nowe wersje firmware, w których zmieniono domyślny protokół na IPv4, aby rozwiązać ten problem. Użytkownicy, którzy potrzebują IPv6, nadal mogą zmienić ustawienie na IPv4 & IPv6 w panelu administracyjnym.

    | Router Model                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Firmware Download](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Firmware Download](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Firmware Download](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Obejście dla innych modeli**

    Jeśli masz inny model lub wolisz nie używać powyższego firmware, po uruchomieniu połączenia komórkowego wykonaj kolejno poniższe komendy AT.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Uwaga**: W przypadku kart SIM EE wartość "User_APN" to zwykle "everywhere". Powtarzaj tę procedurę po każdym restarcie routera.

    ??? note "Jak uruchomić komendy AT?"

        1. W panelu administracyjnym WWW przejdź do sekcji INTERNET -> Cellular, kliknij ikonę z trzema kropkami w prawym górnym rogu i wybierz **Modem AT Command**.
        
            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}
        
            W starszych wersjach firmware kliknij przycisk narzędzi w prawym górnym rogu, aby przejść do strony zarządzania modemem.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}
        
        2. Odszukaj pole komend AT, jak pokazano poniżej.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Jeśli problem nadal występuje, skontaktuj się z naszym zespołem wsparcia pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Z poważaniem,

GL.iNet Technical Support

17 czerwca 2025
