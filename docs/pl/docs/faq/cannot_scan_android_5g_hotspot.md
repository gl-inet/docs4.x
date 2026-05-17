# Nie można wykryć hotspotu 5G z Androida

Podłączenie routera GL.iNet jako repeatera do hotspotu 5G telefonu z Androidem to jeden z częstych sposobów uzyskania dostępu do Internetu.

Jeśli jednak nie możesz wyszukać hotspotu 5G swojego telefonu z Androidem, problem może być związany z kanałem Wi‑Fi.

Niektóre telefony z Androidem domyślnie ustawiają hotspot 5G na kanał używany w USA. Jeśli router GL.iNet nie został pierwotnie kupiony w USA, może wystąpić ten problem.

Możesz zmienić kod kraju Wi‑Fi routera GL.iNet w interfejsie LuCI, wykonując poniższe kroki.

1. Zaloguj się do LuCI.

    Zaloguj się do routera GL.iNet, a następnie wybierz **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Do LuCI zaloguj się tym samym hasłem administratora.

2. Edytuj ustawienia Wi‑Fi.

    Przejdź do **Network** -> **Wireless**, znajdź sieć Wi‑Fi 5G i kliknij po prawej stronie **Edit**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

3. Wybierz US jako kod kraju.

    Na stronie Wireless kliknij kartę **Advanced Settings** w sekcji **Device Configuration**. Wybierz US (United States) jako kod kraju dla sieci Wi‑Fi 5 GHz.

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

4. Kliknij **Save & Apply** przed wylogowaniem.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

    Następnie spróbuj ponownie wyszukać hotspot 5G telefonu z Androidem.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
