# Hur uppgraderar jag till firmware 4.x? {#how-to-upgrade-to-firmware-4x}

**Det här dokumentet är inaktuellt och underhålls inte längre. Klicka [här](../interface_guide/upgrade.md) för den senaste uppgraderingsguiden.**

---

Följ stegen nedan för att uppgradera routern från firmware 3.x till 4.x.

Obs! Behåll inte inställningarna när du uppgraderar från v3.x till v4.x, eftersom detta kan orsaka instabilitet. Säkerhetskopiera alla viktiga inställningar före uppgraderingen.

GL-B1300 och GL-S1300 stöder inte mesh-funktionen i firmware v4.x.

---

## Metod 1. Lokal uppgradering {#method-1-local-upgrade}

Du kan uppgradera firmware via webbadministrationspanelen.

1. Uppgradera firmware till den senaste stabila 3.x-versionen.

2. Ladda ned firmware 4.x [här](https://dl.gl-inet.com){target="_blank"}. Kontrollera att du **laddar ned versionen för en vanlig uppgradering**.

3. Logga in på webbadministrationspanelen och gå till **Upgrade** -> **Local Upgrade**. Ladda upp firmwarefilen som du just laddade ned.

    **Obs!** Firmware 4.x är inte kompatibel med firmware 3.x. När du uppgraderar från firmware 3.x ska du **INTE** behålla inställningarna.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow gl-90-desktop"}

## Metod 2. Uppgradering med U-Boot {#method-2-u-boot-upgrade}

1. Ladda ned firmware 4.x [här](https://dl.gl-inet.com){target="_blank"}. Kontrollera att du **laddar ned versionen för U-Boot**.

2. Följ den här [U-Boot-guiden](debrick.md) för att installera firmware.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
