# macOS kan inte skriva till en Samba-resurs {#macos-cannot-write-to-a-samba-share}

När en exFAT-formaterad lagringsenhet används för en Samba-resurs kan vissa macOS-enheter visa något av följande fel när de försöker skriva filer till resursen.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Försök lösa problemet med följande metoder.

1. **Kontrollera behörigheterna för Samba-resursen.**

    Kontrollera att Samba-resursen är konfigurerad med skrivbehörighet. Logga in på routerns webbadministrationspanel och kontrollera att "Read/Write"-behörighet är aktiverad för ditt användarkonto i den delade mappen.

2. **Använd kommandot `cp -X file-name` för att kopiera filen.**

    Finder lägger automatiskt till utökade attribut (t.ex. resursdelar och metadata) vid överföringar, vilket kan strida mot Sambas hantering av exFAT-lagring. Prova därför att kopiera filen med kommandot **cp -X file-name**.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Du kan även kopiera mappen med kommandot **cp -rX folder-name**.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Starta om din Mac.**

    Klicka på Apple-menyn och sedan på Restart. Om problemet kvarstår stänger du av datorn, kopplar från alla externa enheter, väntar i 30 sekunder och startar sedan om den.

4. **Byt namn på filen.**

    Högerklicka på filen och klicka på Rename. Använd enkla namn och undvik specialtecken som !@# och blanksteg.

5. **Anslut lagringsenheten igen.**

    Om du använder en extern enhet, till exempel ett USB-minne, matar du först ut den innan du kopplar ur den. Vänta i 10 sekunder och anslut den sedan igen. Du kan även prova en annan USB-port.

6. **Reparera diskfel med First Aid.**

    Skadade data på disken kan orsaka skrivfel. Du kan använda Skivverktyg i macOS för att åtgärda problem.

    1. Öppna Finder -> Applications -> Utilities -> Disk Utility.
    2. Välj enheten/lagringsenheten (lokal eller extern) i det vänstra sidofältet.
    3. Klicka på First Aid -> Run. Vänta tills processen är klar.

7. **Justera filsystemet eller formatera enheten.**

    Om du använder en exFAT-formaterad enhet kan kompatibilitetsproblem med Samba uppstå i macOS. Du kan prova följande metoder.

    - **Formatera som FAT32** (för externa enheter och kompatibilitet mellan plattformar)

        1. Säkerhetskopiera först data på enheten (formateringen raderar alla filer).
        2. Öppna Disk Utility -> välj enheten -> Erase.
        3. Välj "MS-DOS (FAT)" (FAT32) som format -> klicka på Erase.

    - **Formatera som ext4**

        !!! Note

            ext4 stöds främst av Linux-system. När lagringsenheten har formaterats som ext4 kan den vara inkompatibel med Windows-operativsystem, vilket kan leda till problem som att enheten inte kan identifieras eller skrivas till på Windows-enheter.

        1. Säkerhetskopiera alla data på enheten eftersom formateringen raderar dem.
        2. Använd ett Linux-system eller verktyg från tredje part för att formatera enheten som ext4.

8. **Uppdatera macOS och rensa cacheminnen.**

    Föråldrad programvara och skadade cacheminnen kan orsaka konflikter. Gå till System Settings -> General -> Software Update, installera den senaste versionen och rensa systemets cacheminnen.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
