# Kontrola rodzicielska (Firmware v4.9)

> Ten przewodnik dotyczy firmware v4.9 i nowszego. W przypadku wcześniejszych wersji kliknij [tutaj](parental_control.md).

Po lewej stronie webowego panelu administracyjnego przejdź do **FLOW CONTROL** -> **Parental Control**.

Kontrola rodzicielska chroni dzieci w Internecie, blokując nieodpowiednie strony i ograniczając czas spędzany przed ekranem. Filtruje szkodliwe treści i zachęca do odpowiedzialnego korzystania z Internetu.

GL.iNet Parental Control oferuje elastyczne harmonogramy, które pozwalają ograniczyć dostęp do Internetu na urządzeniach najczęściej używanych przez dzieci. Możesz jednym kliknięciem blokować nieodpowiednie aplikacje i strony internetowe. Dodatkowo w razie potrzeby możesz ręcznie wprowadzać domeny, aby uzyskać pełną ochronę online.

Układ strony i przebieg konfiguracji Parental Control zostały ulepszone w firmware v4.9, co upraszcza konfigurację i zapewnia bardziej intuicyjny widok reguł.

---

Wykonaj poniższe kroki, aby skonfigurować kontrolę rodzicielską.

1. Zaloguj się do webowego panelu administracyjnego routera i przejdź do **FLOW CONTROL** -> **Parental Control**. Upewnij się, że czas routera jest prawidłowy.

    ![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/router_time.png){class="glboxshadow"}

    Jeśli nie, przejdź najpierw do **SYSTEM** -> **Time Zone**, aby go zsynchronizować.

2. Włącz Parental Control i kliknij **Apply**.

    ![enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/enable.png){class="glboxshadow"}

3. Zobaczysz listę reguł, jak poniżej. Kliknij **Add a New Rule**.

    ![add a new rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/add_rules.png){class="glboxshadow"}

4. W wyskakującym oknie utwórz regułę, ustaw własną nazwę, a następnie kliknij **Next**.

    ![create a rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/create_rule.png){class="glboxshadow gl-90-desktop"}

5. Wybierz urządzenie dziecka, a następnie kliknij **Next**.

    Urządzenie pojawi się na tej stronie tylko wtedy, gdy jest połączone z routerem przez Wi‑Fi lub Ethernet. Kolor cyjan oznacza stan online, a szary stan offline.

    ![select device](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/select_device.png){class="glboxshadow gl-90-desktop"}

    **Wskazówka**: Jeśli chcesz łatwiej odróżniać podłączone urządzenia, przejdź do strony **CLIENTS** i dostosuj nazwy urządzeń.

6. Ustaw porę snu dla urządzenia dziecka, a następnie kliknij **Next**.

    W tym okresie Internet na wybranych urządzeniach będzie niedostępny. Domyślnie ta sama pora snu obowiązuje każdego dnia.

    ![bedtime1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/bedtime1.png){class="glboxshadow gl-90-desktop"}

    Jeśli chcesz ustawić różne pory snu dla poszczególnych dni tygodnia, wybierz **Customize Days**, ustaw różne godziny, a następnie kliknij **Next**.

    ![bedtime2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/bedtime2.png){class="glboxshadow gl-90-desktop"}

7. Wybierz filtr treści.

    Domyślnie zaznaczone są trzy kategorie: **Gambling**, **Malicious Content** oraz **Sexual Content**.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/filter.png){class="glboxshadow gl-90-desktop"}

    W razie potrzeby możesz wybrać inne kategorie, takie jak **Games**, **Shopping**, **Social Media**, **Entertainment** itd.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Jeśli trudno znaleźć konkretną aplikację, którą chcesz zablokować, skorzystaj z wyszukiwania u góry, aby szybko ją odszukać.

    ![search app](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/search_app.png){class="glboxshadow gl-90-desktop"}

8. Jeśli chcesz zablokować określone domeny, kliknij **Advanced Settings** w prawym dolnym rogu.

    ![block domain1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/block_domain1.png){class="glboxshadow gl-90-desktop"}

    Wprowadź domeny ręcznie, a następnie kliknij **Finish**.

    ![block domain2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/block_domain2.png){class="glboxshadow gl-90-desktop"}

9. Reguła została dodana. Lista pokazuje nazwę reguły, liczbę podłączonych urządzeń, harmonogram pory snu, filtrowane treści oraz status reguły (włączona/wyłączona).

    ![rules added](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/rules_added.png){class="glboxshadow"}

    Na istniejących regułach możesz wykonywać podstawowe operacje: Modify, Copy i Delete.

    ![action](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action.png){class="glboxshadow"}

    - **Modify**: Zmienia wybrane urządzenia, pory snu i reguły filtru treści.

        ![action modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action_modify.png){class="glboxshadow"}

    - **Copy**: Tworzy kopię istniejącej reguły, aby uniknąć ręcznej ponownej konfiguracji.

        ![action copy](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action_copy.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
