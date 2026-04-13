# Nie można wykryć hotspotu 5G z Androida

Podłączenie routera GL.iNet jako repeatera do hotspotu 5G telefonu z Androidem to jeden z częstych sposobów uzyskania dostępu do Internetu.

Jeśli jednak nie możesz wyszukać hotspotu 5G swojego telefonu z Androidem, problem może być związany z kodem kraju Wi-Fi.

Niektóre telefony z Androidem domyślnie ustawiają hotspot 5G na kanał używany w USA. Jeśli router GL.iNet nie został pierwotnie kupiony w USA, może wystąpić ten problem.

Możesz zmienić kod kraju Wi-Fi routera GL.iNet na stronie LuCI, wykonując poniższe kroki.

## Krok 1. Zaloguj się do LuCI

Zaloguj się do routera GL.iNet, a następnie na lewym pasku bocznym wybierz **SYSTEM -> Advanced Settings -> Go to LuCI**. Do LuCI zaloguj się tym samym hasłem administratora.

## Krok 2. Edytuj ustawienia Wi-Fi

Przejdź do **Network -> Wireless**, wybierz sieć Wi-Fi 5G i kliknij edycję. Jeśli używasz GL-MT3000, przejdź do **Network -> MTK Wi-Fi**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

![mtkwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/mtkwifi.jpg){class="glboxshadow"}

## Krok 3. Wybierz US jako kod kraju

W sekcji **Device Configuration -> Advanced Settings** wybierz US (United States) jako kod kraju dla swojej sieci Wi-Fi 5 GHz.

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

Przed wylogowaniem kliknij **Save & Apply**.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

Następnie spróbuj ponownie wyszukać hotspot 5G telefonu z Androidem.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
