# Jak zaktualizować do firmware 4.x?

**Ten dokument jest nieaktualny i nie jest już utrzymywany. Kliknij [tutaj](../interface_guide/upgrade.md), aby przejść do najnowszego przewodnika aktualizacji.**

---

Wykonaj poniższe kroki, aby zaktualizować router z firmware 3.x do 4.x.

Uwaga: podczas aktualizacji z v3.x do v4.x nie zachowuj ustawień, ponieważ może to spowodować niestabilność. Przed aktualizacją wykonaj kopię zapasową wszystkich ważnych ustawień.

GL-B1300 i GL-S1300 nie obsługują funkcji mesh w firmware v4.x.

---

## Metoda 1. Aktualizacja lokalna

Możesz zaktualizować firmware przez panel administracyjny WWW.

1. Zaktualizuj firmware do najnowszej stabilnej wersji 3.x.

2. Pobierz firmware 4.x [tutaj](https://dl.gl-inet.com){target="_blank"}. Upewnij się, że pobierasz wersję przeznaczoną do **common upgrade**.

3. Zaloguj się do panelu administracyjnego WWW, przejdź do **Upgrade** -> **Local Upgrade**. Prześlij plik firmware, który właśnie pobrałeś.

    **Uwaga:** Firmware 4.x nie jest zgodny z firmware 3.x. Podczas aktualizacji z firmware 3.x **NIE** zachowuj ustawień.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/gl-ax1800_upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow gl-90-desktop"}

## Metoda 2. Aktualizacja przez U-Boot

1. Pobierz firmware 4.x [tutaj](https://dl.gl-inet.com){target="_blank"}. Upewnij się, że pobierasz wersję przeznaczoną do **U-Boot**.

2. Skorzystaj z tego przewodnika [U-Boot](debrick.md), aby wgrać firmware.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
