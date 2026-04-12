# macOS nie może zapisywać do udziału Samba

Podczas używania nośnika sformatowanego jako exFAT w udziale Samba na niektórych urządzeniach z macOS może wystąpić jeden z poniższych błędów podczas próby zapisu plików do udziału.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Spróbuj rozwiązać ten problem, korzystając z poniższych metod.

1. **Sprawdź uprawnienia udziału Samba​.**

    Upewnij się, że udział Samba jest skonfigurowany z uprawnieniami do zapisu. Zaloguj się do panelu administracyjnego WWW routera i sprawdź, czy dla Twojego konta użytkownika włączono uprawnienia "Read/Write" do udostępnionego folderu.

2. **Użyj polecenia `cp -X file-name`, aby skopiować plik.**

    Finder automatycznie dodaje podczas transferu rozszerzone atrybuty (np. resource forks i metadane), co może kolidować z obsługą nośników exFAT przez Sambę. Spróbuj skopiować plik za pomocą polecenia **cp -X file-name**.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Możesz też użyć polecenia **cp -rX folder-name**, aby skopiować folder.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Uruchom ponownie komputer Mac.**

    Kliknij menu Apple i wybierz Restart. Jeśli problem nadal występuje, wyłącz komputer, odłącz wszystkie urządzenia zewnętrzne, odczekaj 30 sekund, a następnie uruchom go ponownie.​

4. **Zmień nazwę pliku.**

    Kliknij plik prawym przyciskiem myszy i wybierz Rename. Używaj prostych nazw i unikaj znaków specjalnych, takich jak !@#, a także spacji.​

5. **Podłącz nośnik ponownie.**

    Jeśli używasz dysku zewnętrznego, takiego jak dysk USB, najpierw go wysuń przed odłączeniem, odczekaj 10 sekund, a następnie podłącz go ponownie. Możesz też spróbować użyć innego portu USB.

6. **Napraw błędy dysku za pomocą First Aid.**

    Uszkodzone dane na dysku mogą powodować błędy zapisu. Do naprawy problemu możesz użyć Narzędzia dyskowego macOS.
    
    1. ​Otwórz Finder -> Applications -> Utilities -> Disk Utility.​ 
    2. Wybierz dysk lub nośnik (lokalny albo zewnętrzny) na lewym pasku bocznym.​ 
    3. Kliknij First Aid -> Run. Poczekaj na zakończenie procesu.

7. **Dostosuj system plików lub sformatuj dysk​.**

    Jeśli używasz dysku sformatowanego jako exFAT, w macOS mogą występować problemy ze zgodnością z Sambą. Możesz wypróbować poniższe metody.​
    
    - **Sformatuj do FAT32** (dla dysków zewnętrznych, zgodność międzyplatformowa)
    
        1. Najpierw wykonaj kopię zapasową danych z dysku (formatowanie usuwa wszystkie pliki).​
        2. Otwórz Disk Utility -> wybierz dysk -> Erase.​
        3. Jako format wybierz "MS-DOS (FAT)" (FAT32) -> kliknij Erase.​

    - **Sformatuj do ext4**
    
        !!! Note
        
            ext4 jest obsługiwany przede wszystkim przez systemy Linux. Po sformatowaniu do ext4 nośnik może być niezgodny z systemami Windows, co może prowadzić do problemów, takich jak brak rozpoznawania dysku lub brak możliwości zapisu na urządzeniach z Windows.​
        
        1. Wykonaj kopię zapasową wszystkich danych z dysku, ponieważ formatowanie je usunie.​
        2. Użyj narzędzia takiego jak Disk Utility albo systemu Linux, aby sformatować dysk do ext4.

8. **Zaktualizuj macOS i wyczyść pamięć podręczną​.**

    Nieaktualne oprogramowanie lub uszkodzona pamięć podręczna mogą powodować konflikty. Przejdź do System Settings -> General -> Software Update, zainstaluj najnowszą wersję systemu i wyczyść pamięć podręczną.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
