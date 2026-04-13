# Jak naprawić sieć lub przywrócić ustawienia fabryczne?

Wszystkie routery GL.iNet są wyposażone w fizyczny mechanizm resetowania (przycisk resetowania lub otwór na szpilkę). Naciśnięcie przycisku lub użycie otworu na szpilkę daje ten sam efekt: przywrócenie łączności sieciowej albo zresetowanie routera do ustawień fabrycznych.

W modelach z otworem na szpilkę użyj szpilki, wyprostowanego spinacza lub podobnego narzędzia.  

Przed wykonaniem resetu upewnij się, że router całkowicie się uruchomił. **NIE** naciskaj przycisku resetowania bezpośrednio po włączeniu zasilania, ponieważ może to uruchomić tryb U-Boot failsafe.

## Naprawa sieci

Naciśnij i przytrzymaj przycisk resetowania przez **4 sekundy**, a następnie puść go, aby wykonać miękki reset, który może naprawić sieć.

Ta operacja uruchomi ponownie interfejs sieciowy i przywróci domyślne ustawienia interfejsu Internet, zachowując ustawienia Wi-Fi, ustawienia VPN, ustawienia systemowe itd.

**Uwaga**: 

1. Jeśli Wi-Fi zostało wyłączone, miękki reset przywróci domyślny stan Wi-Fi, czyli włączony.

2. Miękki reset można także wykorzystać do szybkiego przełączenia z trybu innego niż router do trybu routera.

## Przywracanie ustawień fabrycznych {#reset-to-factory}

Obejrzyj ten film lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jguDqBWP-Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Są dwa sposoby na zresetowanie firmware.

1. Korzystając z fizycznego mechanizmu resetowania (przycisku lub otworu na szpilkę).

    Naciśnij i przytrzymaj przycisk resetowania (lub włóż szpilkę do otworu) przez **10 sekund**, a następnie puść go, aby przywrócić router do ustawień fabrycznych. Wszystkie dane użytkownika zostaną usunięte.

    **Uwaga:** Jeśli przywracanie ustawień fabrycznych nie działa, może być konieczne skorzystanie z [samouczka U-Boot](debrick.md), aby odratować router.

2. Resetowanie firmware w panelu administracyjnym WWW.

    Zaloguj się do panelu administracyjnego WWW routera i przejdź do **SYSTEM -> Reset Firmware**. Kliknij przycisk, aby zresetować firmware.

    **Uwaga:** Wszystkie bieżące ustawienia i dane zostaną utracone. Proces potrwa około 2 minut. NIE wyłączaj routera w trakcie tego procesu.

    ![glinet reset firmware](https://static.gl-inet.com/docs/router/en/4/tutorials/reset_firmware/reset_firmware_4.8.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
