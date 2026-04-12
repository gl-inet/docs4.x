# Przewodnik rozwiązywania problemów z siecią komórkową

Jeśli nie możesz nawiązać połączenia komórkowego, sprawdź poniższe kwestie.

??? "Sprawdź sprzęt urządzenia"

    **1.1** Użyj standardowego zasilacza przeznaczonego do urządzenia. Niestandardowe zasilacze mogą powodować niewystarczające zasilanie.
    
    **1.2** Upewnij się, że w panelu administracyjnym WWW są wyświetlane **Modem name**, **IMEI** i **SIM ICCID**.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}
    
    W firmware ver.4.8 i nowszym kliknij **View More Information**, aby znaleźć **SIM ICCID**.

    Jeśli nie możesz ich znaleźć, uruchom router ponownie. Jeśli nazwa modemu i IMEI nadal nie są wykrywane, skontaktuj się z nami pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).
    
    **1.3** Kliknij **View More**, aby sprawdzić **Cells Info** i potwierdzić, że sygnał jest stabilny. Jeśli sygnał jest bardzo słaby, upewnij się, że anteny są zainstalowane prawidłowo, albo przenieś router w miejsce z dobrym sygnałem i sprawdź ponownie.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}
    
    **1.4** Kliknij **View More**, aby sprawdzić, czy pasma częstotliwości obsługiwane przez urządzenie są zgodne z Twoim regionem.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Sprawdź ustawienia oprogramowania"

    **2.1** Zaloguj się do panelu administracyjnego WWW i upewnij się, że połączenie komórkowe zostało uruchomione. Możesz także kliknąć **Abort**, a następnie **Connect**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}
    
    **2.2** Niektórzy operatorzy mogą wymagać użycia protokołu 3G do nawiązania połączenia. Przełącz na protokół 3G i sprawdź ponownie.

    W firmware ver.4.7 i starszym przejdź do **Manual Setup** -> **Protocol**, wybierz **3G**, a następnie kliknij **Apply**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    W firmware ver.4.8 i nowszym przejdź do **SIM Card Settings** -> **Protocol**, wybierz **3G**, a następnie kliknij **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    Urządzenie automatycznie połączy się ponownie. Odczekaj kilka minut i sprawdź, czy połączenie zostało nawiązane.

    **2.3** Niektóre karty SIM wymagają określonego APN. Jeśli karta SIM nie może się zarejestrować, skontaktuj się z operatorem, aby sprawdzić, czy nie obowiązują dodatkowe ograniczenia. W razie potrzeby skonfiguruj prawidłowy APN na routerze, a następnie kliknij **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}
    
    **2.4** Włącz **Band Maksing** i sprawdź ponownie. W przypadku firmware ver.4.7 i starszego zobacz [ten link](../interface_guide/internet_cellular_v4.7.md/#band-masking). W przypadku firmware ver.4.8 i nowszego zobacz [ten link](../interface_guide/internet_cellular.md/#band-masking).

    **2.5** Zablokuj lub odblokuj stację bazową i sprawdź ponownie. Ta funkcja jest dostępna tylko w GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) i GL-X2000 (Spitz Plus). Kliknij [tutaj](../interface_guide/internet_cellular.md/#lock-tower), aby uzyskać więcej instrukcji.
    
    Zablokowanie konkretnej stacji bazowej pozwala routerowi korzystać z wysokiej jakości zasobów sieciowych i utrzymywać stabilne połączenie komórkowe.
    
    Jednak po zablokowaniu stacji bazowej router będzie nadal próbował łączyć się z nią po ponownym uruchomieniu, nawet jeśli zostanie przeniesiony do nowej lokalizacji. Może to uniemożliwić routerowi automatyczne połączenie z siecią komórkową. Jeśli tak się stanie, możesz odblokować bieżącą stację bazową w panelu administracyjnym WWW routera albo ręcznie zablokować nową.

    **Uwaga:** Zablokowana stacja bazowa musi odpowiadać pasmom częstotliwości obsługiwanym przez operatora i urządzenie, w przeciwnym razie połączenie może się nie udać.

??? "Sprawdź zgodność karty SIM"
    
    **3.1** Potwierdź typ karty SIM. Routery komórkowe GL.iNet są certyfikowane jako urządzenia IoT. Teoretycznie urządzenie obsługuje tylko karty SIM typu IoT. Jeśli nie masz pewności, jaki to typ karty SIM, skontaktuj się z operatorem.
    
    Typowe rodzaje kart SIM to: data-only, data-only + voice, IoT i hotspot. Zalecamy używanie kart SIM typu IoT lub hotspot. Działanie kart data-only albo data-only + voice nie jest gwarantowane.
    
    **3.2** Niektóre karty SIM trzeba najpierw aktywować. Upewnij się, że karta SIM ma dostęp do Internetu po włożeniu do telefonu, a dopiero potem przełóż ją do routera.
    
    **3.3** Niektóre niestandardowe karty SIM mogą działać tylko w telefonach komórkowych albo na określonych urządzeniach. Upewnij się, że karta SIM nie jest przypisana do konkretnego urządzenia.
    
    **3.4** W niektórych stanach lub miastach w USA (np. w sieci AT&T w Seattle) może być konieczne zarejestrowanie IMEI urządzenia u operatora. Jeśli nie masz pewności co do rejestracji, skontaktuj się z operatorem.
    
    **3.5** Jeśli panel administracyjny WWW wyświetla komunikat „SIM card not registered”, najpierw wykonaj powyższe kroki.

    Zalecamy wyłączenie routera, włożenie karty SIM, a następnie ponowne uruchomienie routera. Niektóre modele nie obsługują wymiany podczas pracy i mogą nie wykryć karty SIM, jeśli zostanie włożona przy włączonym zasilaniu.

    Upewnij się, że wszystkie anteny są prawidłowo zainstalowane, a następnie przetestuj urządzenie ponownie na zewnątrz, w miejscu z silnym sygnałem komórkowym. Słaby sygnał może uniemożliwić zarejestrowanie karty SIM w sieci.

    Jeśli problem nadal występuje, karta SIM może być niezgodna z routerem. Skontaktuj się z operatorem sieci, aby uzyskać dalszą pomoc.

    Jeśli operator potwierdzi, że problem nie jest związany z kartą SIM, skontaktuj się z naszym zespołem wsparcia pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Jeśli karta SIM może się zarejestrować i uzyskać adres IP, ale nie ma dostępu do Internetu (wysyłanie działa, ale pobieranie nie), karta SIM jest najprawdopodobniej ograniczana przez operatora. Skontaktuj się z operatorem, aby usunąć to ograniczenie, albo ustaw TTL na 65 i sprawdź ponownie, jak pokazano poniżej.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    Kontaktując się z operatorem sieci, podaj nazwę modemu urządzenia, IMEI, SIM ICCID i model routera.
    
Jeśli żadne z powyższych rozwiązań nie pomoże, skontaktuj się z naszym zespołem wsparcia pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).
