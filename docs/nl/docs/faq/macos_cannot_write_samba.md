# macOS cannot write to a Samba share {#macos-cannot-write-to-a-samba-share}

Bij een Samba-share op een exFAT-geformatteerd opslagapparaat kunnen sommige macOS-apparaten een van de volgende fouten melden wanneer ze bestanden naar de share schrijven.

- "The operation can't be completed because an unexpected error occurred (error code 100093)."

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred (error code -50)."

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Probeer het probleem met de volgende methoden op te lossen.

1. **Check Samba share permissions​.**

    Controleer of de Samba-share schrijftoegang toestaat. Meld je aan bij het webbeheerpaneel van de router en controleer of de gedeelde map voor je gebruikersaccount de machtiging "Read/Write" heeft.

2. **Use the `cp -X file-name` command to copy the file.**

    Finder voegt tijdens overdrachten automatisch uitgebreide kenmerken toe, zoals resource forks en metagegevens. Dit kan botsen met de verwerking van exFAT-opslag door Samba. Probeer het bestand met de opdracht **cp -X file-name** te kopiëren.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Or use **cp -rX folder-name** command to copy the folder.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Restart your Mac.**

    Open het Apple-menu en klik op Restart. Als het probleem aanhoudt, schakel je het apparaat uit, koppel je alle externe apparaten los, wacht je 30 seconden en start je het opnieuw op.​

4. **Rename the file.**

    Klik met de rechtermuisknop op het bestand en klik op Rename. Gebruik eenvoudige namen zonder speciale tekens zoals !@# en zonder spaties.​

5. **Reconnect the storage device.**

    Werp een extern station zoals een USB-station uit voordat je het loskoppelt. Wacht 10 seconden en sluit het opnieuw aan. Probeer eventueel een andere USB-poort.

6. **Repair disk errors with First Aid.**

    Beschadigde schijfgegevens kunnen schrijffouten veroorzaken. Gebruik macOS Disk Utility om problemen te herstellen.

    1. ​Open Finder -> Applications -> Utilities -> Disk Utility.​
    2. Select the drive/storage device (local or external) in the left sidebar.​
    3. Klik op First Aid -> Run en wacht tot het proces is voltooid.

7. **Adjust File System or Format the Drive​.**

    Een exFAT-geformatteerd station kan op macOS compatibiliteitsproblemen met Samba veroorzaken. Probeer de volgende methoden.​

    - **Format to FAT32** (for external drives, cross-platform compatibility)

        1. Back up data on the drive first (formatting erases all files).​
        2. Open Disk Utility -> Select the drive -> Erase.​
        3. Choose "MS-DOS (FAT)" (FAT32) as the format -> Click Erase.​

    - **Format to ext4**

        !!! Note

            ext4 wordt voornamelijk door Linux-systemen ondersteund. Na formatteren als ext4 is het opslagapparaat mogelijk niet compatibel met Windows en kan Windows het station niet herkennen of beschrijven.​

        1. Back up all data on the drive as formatting will erase it.​
        2. Use a Linux system or third-party tools to format the drive as ext4.

8. **Update macOS and Clear Caches​.**

    Verouderde software of beschadigde caches kunnen conflicten veroorzaken. Ga naar System Settings -> General -> Software Update, installeer de nieuwste versie en wis de systeemcaches.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
