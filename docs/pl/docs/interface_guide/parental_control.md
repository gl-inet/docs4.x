# Kontrola rodzicielska

Kontrola rodzicielska to sposób na zapewnienie dzieciom bezpieczeństwa w sieci poprzez blokowanie nieodpowiednich stron internetowych i ograniczanie czasu korzystania z urządzeń. Pomaga zapobiegać dostępowi do szkodliwych treści, zarządzać czasem ekranowym i dbać o odpowiedzialne korzystanie z Internetu.

> Uwaga: Niektóre modele nie obsługują kontroli rodzicielskiej z powodu niewystarczającej ilości pamięci, np. Mango (GL-MT300N-V2) i Shadow (GL-AR300M series).

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

- **Block WAN for Unmanaged Devices**: Blokuje dostęp do Internetu dla wszystkich urządzeń, których nie ma na liście kontroli rodzicielskiej.

Następnie postępuj zgodnie z kreatorem konfiguracji, aby skonfigurować kontrolę rodzicielską.

---

Poniżej znajduje się przykładowe zastosowanie. Ustawienia możesz dostosować do własnych potrzeb.

**Scenariusz**: Urządzenia w profilu mogą korzystać z Internetu tylko do nauki od godziny 8:00 do 11:00 w dni powszednie oraz do gier od godziny 18:00 do 20:00 w weekendy. W pozostałym czasie dostęp do Internetu jest domyślnie zablokowany.

Wykonaj poniższe kroki, aby skonfigurować kontrolę rodzicielską.

1. Utwórz profil i nadaj mu własną nazwę.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Wybierz urządzenia, którymi chcesz zarządzać. Najpierw podłącz je do routera. Jeśli nie były jeszcze połączone z routerem, dodaj je ręcznie, wpisując ich adresy MAC.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Ustaw limit dostępu.

    Dostępne są dwa domyślne zestawy reguł: **Block Internet Access** i **No Limit**.

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    Kliknij **Add a New Ruleset**, aby utworzyć jeszcze dwa zestawy reguł do późniejszego użycia: **Learning** i **Play**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    Określ nazwę zestawu reguł (np. Learning), kolor oraz wpisz strony, które chcesz blokować, a następnie kliknij **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Uwaga**: Nazwy domen wprowadzone na liście blokowanych powinny obejmować ich subdomeny. Przykładowo wprowadzenie „example.com" obejmuje również wszelkie subdomeny, takie jak „subdomain.example.com".

    Analogicznie utwórz drugi zestaw reguł. Określ nazwę zestawu reguł (np. Play), kolor oraz wpisz strony, które chcesz blokować, a następnie kliknij **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    Po zastosowaniu będą dostępne łącznie cztery zestawy reguł. Upewnij się, że jako **Default Ruleset** wybrano **Block Internet Access**, a następnie kliknij **Finish**.

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

### Rozwiązywanie problemów

Jeśli skonfigurowane ustawienia nie działają, sprawdź poniższe możliwe przyczyny.

1. Problem z pamięcią podręczną DNS.
  
    Przeglądarki i systemy operacyjne utrzymują pamięć podręczną DNS, dlatego zastosowanie zmian konfiguracji może zająć trochę czasu. Wyczyść pamięć podręczną DNS, aby zastosować zmiany od razu.
  
      * [Wyczyść pamięć podręczną DNS w Chrome na komputerze](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [Wyczyść pamięć podręczną DNS w Edge na komputerze](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. Harmonogram profilu jeszcze się nie rozpoczął.

3. Wprowadzona nazwa domeny może być nieprawidłowa.

    Publiczną domenę strony internetowej łatwo znaleźć, ale domeny API używane przez aplikacje często nie są publicznie dostępne. Aby ustalić właściwą domenę, użyj narzędzia do przechwytywania pakietów, takiego jak Wireshark, albo wyszukaj odpowiednie informacje o domenie.

    Przykładowo, aby zablokować `www.google.com`, użycie `google.com` jest skuteczniejsze niż `www.google.com`.

4. Docelowe urządzenie używa losowego adresu MAC dla każdego połączenia sieciowego, co uniemożliwia działanie reguł dostępu. Wyłącz losowy adres MAC na docelowym urządzeniu, a następnie ponownie dodaj to urządzenie do profilu.

## Wersja Bark {#bark-version}

> Ten przewodnik dotyczy firmware v4.8 i wcześniejszych. W przypadku nowszych wersji kliknij [tutaj](bark.md).

Usługa [Bark](https://www.bark.us/){target="_blank"} pomaga chronić cyfrowy świat dziecka i zapewnia kompleksową ochronę online. Zwykle wymaga płatnej subskrypcji. Jednak w ramach partnerstwa z Bark, GL.iNet oferuje plan Bark Home bezpłatnie **na wybranych modelach routerów**, zapewniając zaawansowane monitorowanie i alerty bez dodatkowych kosztów.

**Uwaga**:

1. Usługa Bark jest dostępna **tylko w Stanach Zjednoczonych, Australii i Republice Południowej Afryki**. Kliknij [tutaj](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"}, aby uzyskać szczegóły.

2. Obie wersje kontroli rodzicielskiej nie mogą być włączone jednocześnie. Włączenie jednej automatycznie wyłączy drugą.

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

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **Parental Control**. Wybierz wersję Bark.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

Włącz przełącznik Bark, a następnie kliknij **Apply**.

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

Następnie sparuj urządzenie ze swoim kontem Bark. Kliknij **Device Pairing Link** lub [tutaj](https://www.bark.us/app/signup/?ref=glinet&home=glinet), aby sparować ten router z kontem Bark.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Zostaniesz przekierowany na stronę Bark. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby się zalogować, sparować urządzenie, utworzyć profil i zakończyć konfigurację początkową.

![bark_welcome_page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_welcome.png){class="glboxshadow"}
<small>(Logowanie do Bark)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow"}
<small>(Urządzenie sparowane)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_create_profile.png){class="glboxshadow"}
<small>(Tworzenie profilu)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_get_started.png){class="glboxshadow"}
<small>(Konfiguracja początkowa)</small>

Gdy urządzenie połączy się z usługami Bark Cloud i zostanie sparowane z Twoim kontem, webowy panel administracyjny routera będzie wyglądał następująco.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Kliknij **Go to Bark** lub [tutaj](https://www.bark.us/app/children/?ref=glinet&home=glinet), aby zalogować się do pulpitu Bark i skonfigurować reguły kontroli rodzicielskiej.

Ponieważ GL.iNet nie jest dostawcą tej usługi, w razie problemów podczas korzystania z Bark skontaktuj się bezpośrednio z [pomocą techniczną Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet).

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
