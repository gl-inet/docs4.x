# Jak ręcznie zaktualizować lub cofnąć wersję firmware routera (z v4.x do v4.x)?

Ten przewodnik pokaże, **jak ręcznie zaktualizować lub cofnąć wersję firmware routera (z v4.x do v4.x)**. Kroki dla ręcznej aktualizacji i cofania wersji firmware routera są takie same.

!!! Note "O aktualizacji i cofaniu wersji firmware routera"

    **Aktualizacja:** Routery GL.iNet z firmware w wersji 4.x nie oferują funkcji automatycznej aktualizacji. 
    
    Gdy dostępna jest nowa wersja firmware, po zalogowaniu do panelu administracyjnego routera zobaczysz komunikat „Upgrade Reminder". Możesz kliknąć przycisk **Upgrade**, aby zainstalować najnowszą wersję firmware wymienioną tam. Jeśli chcesz zaktualizować do konkretnej wersji firmware, wykonaj poniższe kroki, aby ręcznie zaktualizować router. 

    **Cofnięcie wersji:** Możesz cofnąć wersję firmware routera, aby rozwiązać określone problemy.

## 1. Sprawdź, czy router ma najnowszą wersję firmware (tylko dla aktualizacji)

1. W przeglądarce internetowej wprowadź adres URL panelu administracyjnego routera (np. 192.168.8.1) i zaloguj się.
2. Z lewego paska bocznego wybierz **SYSTEM** > **Upgrade**.  

## 2. Pobierz plik firmware

1. W pasku wyszukiwania [centrum pobierania firmware](https://dl.gl-inet.com/) wyszukaj i wybierz model swojego routera.
2. W zakładce **Stable** lub innych zakładkach wybierz **Download for common upgrade and uboot** obok wersji firmware, którą chcesz pobrać. 

## 3. Wgraj firmware

Poniższe instrukcje opisują wgrywanie firmware przez panel administracyjny routera. (Aby wgrać firmware przez aplikację mobilną GL.iNet, [pobierz aplikację](https://www.gl-inet.com/app/) i skonfiguruj ją.)

1. W przeglądarce internetowej wprowadź adres URL panelu administracyjnego routera (np. 192.168.8.1) i zaloguj się. 
2. (Opcjonalnie) Jeśli chcesz wykonać kopię zapasową bieżących ustawień, wykonaj poniższe kroki.

    ??? "Utwórz kopię zapasową bieżących ustawień"

        a. Z lewego paska bocznego kliknij **SYSTEM** > **Advanced Settings**. 

        b. Kliknij link lub przycisk **Go To LuCI**, aby uzyskać dostęp do strony logowania LuCI. 

        c. Wprowadź hasło administratora, a następnie kliknij **Log in**. 

        d. Kliknij **System** > **Backup / Flash Firmware**. 

        e. W sekcji **Backup** kliknij **Generate archive**. Plik zawierający Twoje bieżące ustawienia zostanie pobrany na Twoje urządzenie. 
        
        **Należy pamiętać, że ten plik jest używany tylko dla wersji firmware z momentu wykonania kopii zapasowej, a nie dla innych wersji firmware.**

3. Z lewego paska bocznego kliknij **SYSTEM** > **Upgrade**. 
4. Kliknij **Local Upgrade** i wybierz wcześniej pobrany plik. 
5. Aby zachować bieżące ustawienia (np. hasło administratora routera), włącz opcję **Keep Settings**. 
6. Kliknij **Install**.

**Uwaga:** Podczas procesu aktualizacji nie wyłączaj routera. Po zakończeniu aktualizacji zobaczysz ekran logowania do routera. 

Jeśli podczas procesu aktualizacji firmware utraciłeś ustawienia routera, przywróć ustawienia routera. 

Jeśli powyższa metoda nie działa, spróbuj zaktualizować firmware przez [U-boot](../faq/debrick.md).

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
