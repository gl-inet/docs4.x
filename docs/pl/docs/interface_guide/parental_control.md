# Kontrola rodzicielska

Kontrola rodzicielska to sposób na zapewnienie dzieciom bezpieczeństwa w sieci poprzez blokowanie nieodpowiednich stron internetowych i ograniczanie czasu korzystania z urządzeń. Pomaga zapobiegać dostępowi do szkodliwych treści, zarządzać czasem ekranowym i dbać o odpowiedzialne korzystanie z Internetu.

Ta funkcja jest dostępna od wersji oprogramowania v4.2. **Uwaga**: Niektóre modele, mimo że korzystają z oprogramowania v4.2 lub nowszego, nie obsługują kontroli rodzicielskiej z powodu niewystarczającej ilości pamięci.

Obejrzyj ten film lub wykonaj poniższe kroki, aby skonfigurować kontrolę rodzicielską na routerach GL.iNet.

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

### Kroki konfiguracji

Zaloguj się do panelu administratora routera i przejdź do **APPLICATIONS** -> **Parental Control**.

W oprogramowaniu w wersji 4.8.4 i nowszej przejdź do **FLOW CONTROL** -> **Parental Control**.

Upewnij się, że czas routera jest dokładny. Jeśli nie, przejdź do **SYSTEM** -> **Time Zone**, aby go zsynchronizować.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Włącz kontrolę rodzicielską i kliknij **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Służy do blokowania niezarządzanym urządzeniom dostępu do Internetu.

Następnie postępuj zgodnie z kreatorem konfiguracji, aby skonfigurować kontrolę rodzicielską.

---

Poniżej znajdują się dwa przykładowe zastosowania. Ustawienia możesz dostosować do własnych potrzeb.

**Przypadek 1**

**Scenariusz**: Urządzenia w profilu mogą korzystać z Internetu tylko do nauki od godziny 8:00 do 11:00 w dni powszednie oraz do gier od godziny 18:00 do 20:00 w weekendy. W pozostałym czasie dostęp do Internetu jest domyślnie zablokowany.

Wykonaj poniższe kroki.

1. Utwórz profil i nadaj mu własną nazwę.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Wybierz urządzenia, którymi chcesz zarządzać. Najpierw podłącz je do routera. Jeśli nie były jeszcze połączone z routerem, dodaj je ręcznie, wpisując ich adresy MAC.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Ustaw limit dostępu.

    Dostępne są dwa domyślne zestawy reguł: **Block Internet Access** i **No Limit**.

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    Utwórz jeszcze dwa zestawy reguł do późniejszego użycia: **Learning** i **Play**. Kliknij **Add a New Ruleset**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    Określ nazwę zestawu reguł (np. Learning), kolor oraz wpisz strony, które chcesz blokować, a następnie kliknij **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Uwaga**: Nazwy domen wprowadzone na liście blokowanych powinny obejmować ich subdomeny. Przykładowo wprowadzenie „example.com" obejmuje również wszelkie subdomeny, takie jak „subdomain.example.com".

    Analogicznie utwórz drugi zestaw reguł. Określ nazwę zestawu reguł (np. Play), kolor oraz wpisz strony, które chcesz blokować, a następnie kliknij **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    Po zastosowaniu będą dostępne łącznie cztery zestawy reguł, jak pokazano poniżej. Upewnij się, że jako **Default Ruleset** wybrano **Block Internet Access**, a następnie kliknij **Finish**.

    ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. Następnie ustaw harmonogram dla swojego profilu. Kliknij **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

    Dodaj do harmonogramu zestaw reguł **Learning**. Ustaw **Execution Time** od 8:00 do 11:00 w dni powszednie, a następnie kliknij **Apply**.

    ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. Następnie zostaniesz przekierowany na stronę edycji nowo utworzonego profilu.

    ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    Przejdź na dół strony. Zobaczysz, że harmonogram został już utworzony. Kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **Add Schedule**.

    ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Dodaj do harmonogramu kolejny zestaw reguł **Play**. Ustaw **Execution Time** od 18:00 do 20:00 w weekendy, a następnie kliknij **Apply**.

    ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    Zestaw reguł Play zostanie wtedy dodany do harmonogramu.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Uwaga**: Czerwona przerywana linia wskazuje bieżący czas.

    Możesz również zmodyfikować czas wykonania, klikając określony zestaw reguł w harmonogramie.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Kliknij **Parental Control** u góry, aby wrócić do strony Parental Control.

    ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    Zobaczysz końcową konfigurację. Kontrola rodzicielska działa już zgodnie z harmonogramem. Możesz modyfikować istniejące profile i zestawy reguł albo dodawać nowe w razie potrzeby.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

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

### Kroki konfiguracji

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
