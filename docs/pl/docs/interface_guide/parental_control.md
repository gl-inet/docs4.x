# Kontrola rodzicielska

Kontrola rodzicielska to sposób na zapewnienie dzieciom bezpieczeństwa w sieci poprzez blokowanie nieodpowiednich stron internetowych i ograniczanie czasu korzystania z urządzeń. Pomaga zapobiegać dostępowi do szkodliwych treści, zarządzać czasem ekranowym i dbać o odpowiedzialne korzystanie z Internetu.

Funkcja dostępna od wersji oprogramowania v4.2.

Obejrzyj poniższy film lub wykonaj opisane kroki, aby dowiedzieć się więcej o kontroli rodzicielskiej na routerach GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Wersja lokalna

Wersja lokalna jest dostarczana przez GL.iNet. Aktualnie jest w fazie beta i nie wiąże się z żadnymi dodatkowymi kosztami. W tej wersji, jeśli chcesz filtrować żądania według aplikacji, musisz ręcznie wpisać domenę.

### Obsługiwane modele

??? "Obsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Nieobsługiwane modele"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Konfiguracja

Zaloguj się do panelu administratora routera i przejdź do **APPLICATIONS** -> **Parental Control**.

W oprogramowaniu w wersji 4.8.4 i nowszej przejdź do **Flow Control** -> **Parental Control**.

Upewnij się, że czas routera jest dokładny. Jeśli nie, przejdź do **SYSTEM** -> **Time Zone**, aby go zsynchronizować.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Włącz kontrolę rodzicielską i kliknij **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Służy do blokowania niezarządzanym urządzeniom dostępu do Internetu.

Następnie postępuj zgodnie z kreatorem konfiguracji, aby skonfigurować kontrolę rodzicielską.

Poniżej przedstawiono dwa przykładowe scenariusze użycia, które możesz dostosować do własnych potrzeb.

**Przypadek 1**

**Scenariusz**: Urządzenia w profilu mogą korzystać z Internetu tylko do nauki od godziny 8:00 do 11:00 w dni powszednie oraz do gier od godziny 18:00 do 20:00 w weekendy. W pozostałym czasie dostęp do Internetu jest domyślnie zablokowany.

Wykonaj poniższe kroki.

1. Utwórz profil i nadaj mu nazwę.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

2. Wybierz urządzenia, którymi chcesz zarządzać. Jeśli nie były jeszcze połączone z routerem, dodaj je ręcznie, wprowadzając ich adresy MAC.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

3. Ustaw limit dostępu.

    Dostępne są dwa domyślne zestawy reguł: **Block Internet Access** i **No Limit**. Utwórz tutaj dwa dodatkowe zestawy reguł do późniejszego użycia: **Learning** i **Play**.

    Kliknij **Add a New Ruleset**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

4. Podaj nazwę zestawu reguł (np. Learning), kolor oraz listę stron do zablokowania. Następnie kliknij **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

    **Uwaga**: Nazwy domen wprowadzone na liście blokowanych powinny obejmować ich subdomeny. Przykładowo wprowadzenie „example.com" obejmuje również wszelkie subdomeny, takie jak „subdomain.example.com".

    Analogicznie utwórz kolejny zestaw reguł o nazwie Play. Podaj kolor, strony do zablokowania i kliknij **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

5. Po zastosowaniu dostępne będą łącznie cztery zestawy reguł, jak pokazano poniżej.

    Upewnij się, że jako **Default Ruleset** wybrano **Block Internet Access**, i kliknij **Finish**.

    ![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

6. Przejdź do ustawiania harmonogramu. Kliknij **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

7. Dodaj zestaw reguł **Learning** do harmonogramu. Ustaw **Execution Time** od 8:00 do 11:00 w dni powszednie. Kliknij **Apply**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

8. Zostaniesz przeniesiony na stronę edycji nowo utworzonego profilu.

    ![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

    Zobaczysz, że harmonogram został utworzony. Kliknij **Add Schedule** w prawym górnym rogu.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/add_schedule.png){class="glboxshadow"}

9. Dodaj kolejny zestaw reguł **Play** do harmonogramu. Ustaw **Execution Time** od 18:00 do 20:00 w weekendy. Kliknij **Apply**.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

10. Zobaczysz, że zestaw reguł Play został również dodany do harmonogramu.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

    **Uwaga**: Czerwona przerywana linia wskazuje bieżący czas.

    Możesz również zmodyfikować zestaw reguł harmonogramu, klikając określony fragment harmonogramu.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.jpg){class="glboxshadow"}

11. Kliknij **Parental Control** na górze, aby wrócić do strony Parental Control.

    ![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

    Zobaczysz ostateczną konfigurację. Możesz modyfikować istniejące profile i zestawy reguł lub dodawać nowe.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/final_configuration.png){class="glboxshadow"}

**Przypadek 2**

**Scenariusz**: Urządzenia w profilu mogą korzystać z Internetu do gier i krótkich filmów tylko od godziny 18:00 do 20:00 w weekendowe wieczory. W pozostałym czasie, w tym w czasie nocnym od 21:00 do 7:00 następnego dnia rano, dostęp do Internetu jest domyślnie zablokowany.

Zobacz poniższy samouczek wideo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Rozwiązywanie problemów

Jeśli skonfigurowane ustawienia nie działają, sprawdź poniższe możliwe przyczyny.

1. Pamięć podręczna DNS.
  
    Przeglądarki i systemy operacyjne utrzymują pamięć podręczną DNS, dlatego zmiany mogą potrzebować czasu, aby zaczęły obowiązywać. Możesz wyczyścić pamięć podręczną, aby natychmiast zastosować zmiany.
  
      * [Wyczyść pamięć podręczną w Chrome na komputerze](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [Wyczyść pamięć podręczną w Edge na komputerze](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. Harmonogram profilu jeszcze się nie rozpoczął.

3. Wprowadzona nazwa domeny może być nieprawidłowa.

    Domena strony internetowej jest publiczna, ale domena API używana przez aplikację często nie jest. Aby to rozwiązać, użyj narzędzia takiego jak Wireshark do przechwytywania pakietów lub poszukaj odpowiedniej domeny.

    Przykładowo, aby zablokować „www.google.com", użycie „google.com" jest skuteczniejsze niż „www.google.com".

4. Docelowe urządzenie używa losowego adresu MAC dla każdego połączenia, co uniemożliwia działanie reguł.

## Wersja Bark

Wersja [Bark](https://www.bark.us/){target="_blank"}, dostarczana i zarządzana przez Bark na ich własnej platformie, umożliwia filtrowanie aplikacji i stron internetowych jednym kliknięciem oraz monitorowanie historii żądań.

Oferuje funkcję monitorowania ponad 24 popularnych aplikacji i platform mediów społecznościowych, które są uwzględnione na liście ustawień wstępnych naszej lokalnej funkcji kontroli rodzicielskiej.

Dzięki funkcji rejestrowania zapisuje, które urządzenie klienta odwiedziło jaką stronę i o której godzinie. Umożliwia to rodzicom łatwe przeglądanie dzienników, identyfikowanie stron nieznajdujących się na liście blokowanych i szybkie dodawanie ich do zakresu zarządzania.

Funkcja Bark Parental Control jest dostępna od wersji oprogramowania v4.5 i obsługiwana tylko na wybranych routerach GL.iNet.

**Uwaga**:

1. Usługa Bark jest dostępna **wyłącznie w Stanach Zjednoczonych, Australii i Republice Południowej Afryki**. Kliknij [tutaj](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"}, aby uzyskać szczegółowe informacje.

2. Usługa Bark zazwyczaj wymaga płatnej subskrypcji. Jednak w ramach naszego partnerstwa z Bark, GL.iNet oferuje plan Bark Home bezpłatnie na wybranych modelach routerów, zapewniając zaawansowane monitorowanie i alerty bez dodatkowych kosztów.

3. Obie wersje kontroli rodzicielskiej nie mogą być włączone jednocześnie. Przełączenie między wersjami automatycznie wyłącza drugą.

### Obsługiwane modele

??? "Obsługiwane modele"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)

??? "Nieobsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Konfiguracja

Zaloguj się do panelu administratora routera i przejdź do **APPLICATIONS** -> **Parental Control**.

Wybierz wersję Bark, przełącz przełącznik i kliknij **Apply**.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Uwaga:** Usługa Bark może być niedostępna w niektórych krajach. Ponieważ GL.iNet nie jest dostawcą tej usługi, w przypadku problemów z jej używaniem prosimy o bezpośredni kontakt z [Działem wsparcia technicznego Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet).

Usługa Bark jest włączona, ale to urządzenie nie jest jeszcze sparowane z żadnym kontem. Użyj [linku do parowania urządzenia](https://www.bark.us/app/signup/?ref=glinet&home=glinet), aby sparować urządzenie ze swoim kontem Bark.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Po sparowaniu strona wyświetla się jak poniżej.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Twoje urządzenie jest teraz połączone z usługami Bark Cloud i sparowane z Twoim kontem. Przejdź do [Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) i zaloguj się na swoje konto, aby utworzyć profil do kontroli sieci.

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.