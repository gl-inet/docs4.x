# Viktigt problemmeddelande för GL-MT2500/GL-X3000/GL-XE3000 {#critical-problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

Bästa GL.iNet-kund,

Det här meddelandet gäller startproblem och problem med återställning av firmware via U-Boot på enheterna GL-MT2500/GL-X3000/GL-XE3000. Problemet berodde på ett programvarufel där vissa parametrar var felaktigt definierade, vilket gjorde att routrarna fungerade onormalt. Vi bedömde därför att problemet i viss utsträckning kan förkorta routrarnas livslängd, vilket vi ber uppriktigt om ursäkt för.

För att lösa problemet helt rekommenderar vi starkt att alla användare av GL-MT2500, GL-X3000 och GL-XE3000 både uppgraderar U-Boot-starthanteraren och firmware. Båda uppgraderingarna är nödvändiga och får inte utelämnas.

Även om enheten redan har uppgraderats till den senaste firmwareversionen måste U-Boot-starthanteraren uppgraderas för att förhindra potentiella problem. När U-Boot-starthanteraren har uppgraderats kan du hoppa över ominstallationen av firmware om den senaste firmwareversionen redan är installerad.

Försök genomföra uppgraderingen med Chrome eller Microsoft Edge. Använd **INTE** Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Ladda ned och uppgradera U-Boot-starthanteraren till [version 2025-02-24 15:04:07](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}

2. Ladda ned och uppgradera firmware till [version 4.7.4](https://fw.gl-inet.com/firmware/mt2500/release/openwrt-mt2500-4.7.4-0328-1743128340.bin)

## GL-X3000 {#gl-x3000}

1. Ladda ned och uppgradera U-Boot-starthanteraren till [version 2025-02-25 19:05:24](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}

2. Ladda ned och uppgradera firmware till [version 4.7.4](https://fw.gl-inet.com/firmware/x3000/release/openwrt-x3000-4.7.4-0317-1742206344.bin)

## GL-XE3000 {#gl-xe3000}

1. Ladda ned och uppgradera U-Boot-starthanteraren till [version 2025-02-25 19:07:14](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}

2. Ladda ned och uppgradera firmware till [version 4.7.4](https://fw.gl-inet.com/firmware/xe3000/release/openwrt-xe3000-4.7.4-0317-1742206184.bin)

!!! Note

    Information om hur du uppgraderar U-Boot-starthanteraren finns via [den här länken](upgrade_uboot_version.md).

    Information om hur du uppgraderar firmware finns via [den här länken](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
Vi ber uppriktigt om ursäkt för de besvär som detta kan ha orsakat. Framöver kommer vi att arbeta ännu mer omsorgsfullt med att förbättra våra produkter och firmware.

För dig som redan äger någon av dessa routrar förlänger vi garantin med ett år utan kostnad. Tveka inte att kontakta vår support om du får problem.

Om problemet kvarstår trots uppgraderingen kontaktar du vår support via support@gl-inet.com. Vi skickar då en ny ersättningsenhet utan kostnad.

Vi är mycket tacksamma för ditt förtroende och stöd.

<br>

Med vänlig hälsning,

GL.iNet Technical Support

26 mars 2025
