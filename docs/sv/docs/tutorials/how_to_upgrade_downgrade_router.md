# Uppgradera eller nedgradera routerns firmware manuellt (från v4.x till v4.x) {#how-to-manually-upgrade-or-downgrade-your-router-firmware-from-v4x-to-v4x}

Den här guiden visar **hur du uppgraderar eller nedgraderar routerns firmware manuellt (från v4.x till v4.x)**. Samma steg används för manuell uppgradering och nedgradering av routerns firmware.

!!! Note "Om uppgradering och nedgradering av routerns firmware"

    **Uppgradering:** GL.iNet-routrar som kör firmwareversion 4.x har ingen automatisk uppdateringsfunktion.

    När en ny firmwareversion är tillgänglig visas uppmaningen "Upgrade Reminder" när du har loggat in på routerns administrationspanel. Du kan klicka på knappen **Upgrade** för att installera den senaste firmwareversionen som visas där. Om du vill uppgradera till en viss firmwareversion följer du stegen nedan för att uppgradera routern manuellt.

    **Nedgradering:** Du kan nedgradera routerns firmware för att lösa vissa problem.

## 1. Kontrollera om routern kör den senaste firmwareversionen (endast vid uppgradering) {#1-check-if-your-router-is-running-the-latest-firmware-version-only-for-upgrade}

1. Ange webbadressen till routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
2. Välj **SYSTEM** > **Upgrade** i det vänstra sidofältet.

## 2. Ladda ned firmwarefilen {#2-download-the-firmware-file}

1. Sök efter och välj routermodellen i sökfältet i [nedladdningscentret för firmware](https://dl.gl-inet.com/).
2. Välj **DOWNLOAD FOR COMMON UPGRADE AND U-BOOT** bredvid den firmwareversion som du vill ladda ned på fliken **Stable** eller någon av de andra flikarna.

## 3. Ladda upp firmware {#3-upload-the-firmware}

Följande instruktioner gäller uppladdning av firmware via routerns administrationspanel. (Om du vill ladda upp firmware via GL.iNet-mobilappen [laddar du ned appen](https://www.gl-inet.com/app/) och konfigurerar den.)

1. Ange webbadressen till routerns administrationspanel (t.ex. 192.168.8.1) i en webbläsare och logga in.
2. (Valfritt) Följ stegen nedan om du vill säkerhetskopiera de aktuella inställningarna.

    ??? "Säkerhetskopiera de aktuella inställningarna"

        a. Klicka på **SYSTEM** > **Advanced Settings** i det vänstra sidofältet.

        b. Klicka på länken eller knappen **Go To LuCI** för att öppna LuCI:s inloggningssida.

        c. Ange administratörslösenordet och klicka sedan på **Log in**.

        d. Klicka på **System** > **Backup / Flash Firmware**.

        e. Klicka på **Generate archive** under **Backup**. En fil med de aktuella inställningarna laddas ned till enheten.

        **Observera att filen endast gäller den firmwareversion som användes när säkerhetskopian skapades och inte andra firmwareversioner.**

3. Klicka på **SYSTEM** > **Upgrade** i det vänstra sidofältet.
4. Klicka på **Local Upgrade** och välj filen som du laddade ned tidigare.
5. Aktivera **Keep Settings** om du vill behålla de aktuella inställningarna, till exempel routerns administratörslösenord, vid en uppgradering. Aktivera inte alternativet när du nedgraderar firmware.
6. Klicka på **Install**.

**Obs!** Stäng inte av routern under uppgraderingen. När uppgraderingen är klar visas routerns inloggningsskärm.

Återställ routerinställningarna om de gick förlorade under firmwareuppdateringen.

Om metoden ovan inte fungerar försöker du uppgradera firmware via [U-Boot](../faq/debrick.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
