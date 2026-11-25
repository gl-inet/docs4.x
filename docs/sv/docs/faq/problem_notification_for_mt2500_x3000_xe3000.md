# Problemmeddelande för GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Senast uppdaterat 11 november 2026**

Det kända problemet berör bara vissa tillverkningspartier. Enheter som beställdes den 1 juli 2025 eller senare är sannolikt från ett nyare parti och behöver ingen uppdatering av starthanteraren U-Boot.

Om du är osäker på vilket parti din enhet kommer från skickar du följande uppgifter till [support@gl-inet.com](mailto:support@gl-inet.com) innan du gör några ändringar:

- Routermodell och firmwareversion
- Enhetens MAC-adress
- En beskrivning av problemet, inklusive vad du gjorde när det uppstod, eventuella felmeddelanden och de felsökningssteg du redan provat

Vi bekräftar tillverkningspartiet och ger dig råd om hur du går vidare.

---

Det ursprungliga meddelandet finns kvar nedan som referens. Uppdateringsstegen gäller endast berörda partier. Om du är osäker på om din enhet berörs kontaktar du supporten enligt anvisningarna ovan innan du gör ändringar.

**Publicerat 26 mars 2025**

Bästa GL.iNet-kund,

Det här meddelandet gäller startproblem och problem med återställning av firmware via U-Boot på enheterna GL-MT2500/GL-X3000/GL-XE3000. Problemet berodde på ett programvarufel där vissa parametrar var felaktigt definierade, vilket gjorde att routrarna fungerade onormalt. Vi bedömde därför att problemet i viss utsträckning kan förkorta routrarnas livslängd, vilket vi ber uppriktigt om ursäkt för.

För att lösa problemet helt rekommenderar vi starkt att alla användare av GL-MT2500, GL-X3000 och GL-XE3000 både uppgraderar U-Boot-starthanteraren och firmware. Båda uppgraderingarna är nödvändiga och får inte utelämnas.

Även om enheten redan har uppgraderats till den senaste firmwareversionen måste U-Boot-starthanteraren uppgraderas för att förhindra potentiella problem. När U-Boot-starthanteraren har uppgraderats kan du hoppa över ominstallationen av firmware om den senaste firmwareversionen redan är installerad.

Försök genomföra uppgraderingen med Chrome eller Microsoft Edge. Använd **INTE** Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Uppdatera starthanteraren U-Boot.

    Ladda ner [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"} och [uppdatera sedan starthanteraren U-Boot](upgrade_uboot_version.md).

2. Uppdatera firmware.

    Ladda ner [den senaste firmwareversionen för routern](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"} och [uppdatera sedan routerns firmware](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Uppdatera starthanteraren U-Boot.

    Ladda ner [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"} och [uppdatera sedan starthanteraren U-Boot](upgrade_uboot_version.md).

2. Uppdatera firmware.

    Ladda ner [den senaste firmwareversionen för routern](https://dl.gl-inet.com/router/x3000/stable){target="_blank"} och [uppdatera sedan routerns firmware](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-XE3000 {#gl-xe3000}

1. Uppdatera starthanteraren U-Boot.

    Ladda ner [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"} och [uppdatera sedan starthanteraren U-Boot](upgrade_uboot_version.md).

2. Uppdatera firmware.

    Ladda ner [den senaste firmwareversionen för routern](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"} och [uppdatera sedan routerns firmware](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
Vi ber uppriktigt om ursäkt för de besvär som detta kan ha orsakat. Framöver kommer vi att arbeta ännu mer omsorgsfullt med att förbättra våra produkter och firmware.

För dig som redan äger någon av dessa routrar förlänger vi garantin med ett år utan kostnad. Tveka inte att kontakta vår support om du får problem.

Om problemet kvarstår trots uppgraderingen kontaktar du vår support via [support@gl-inet.com](mailto:support@gl-inet.com). Vi skickar då en ny ersättningsenhet utan kostnad.

Vi är mycket tacksamma för ditt förtroende och stöd.

<br>
Med vänliga hälsningar,<br>
GL.iNet-teamet<br>
26 mars 2025
