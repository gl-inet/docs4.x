# Krytyczny komunikat o problemie dla GL-MT2500/GL-X3000/GL-XE3000

Drodzy Klienci GL.iNet,

Ten komunikat dotyczy problemów z uruchamianiem urządzenia oraz odzyskiwaniem firmware przez U-Boot w modelach GL-MT2500/GL-X3000/GL-XE3000. Przyczyną był defekt oprogramowania, w którym część parametrów została nieprawidłowo zdefiniowana, przez co routery działały nieprawidłowo. W rezultacie oceniliśmy, że problem ten mógł w pewnym stopniu skrócić żywotność routerów, za co szczerze przepraszamy.

Aby całkowicie rozwiązać ten problem, zdecydowanie zalecamy wszystkim użytkownikom GL-MT2500, GL-X3000 i GL-XE3000 wykonanie zarówno aktualizacji bootloadera U-Boot, jak i aktualizacji firmware. Obie procedury są niezbędne i nie należy pomijać żadnej z nich.

Nawet jeśli urządzenie zostało już zaktualizowane do najnowszej wersji firmware, aktualizacja bootloadera U-Boot nadal jest obowiązkowa, aby zapobiec potencjalnym problemom. Po zakończeniu aktualizacji bootloadera U-Boot możesz pominąć ponowną instalację firmware, jeśli najnowsza wersja jest już zainstalowana.

Do aktualizacji użyj przeglądarki Chrome lub Microsoft Edge. NIE używaj Mozilla/Firefox.

## GL-MT2500

1. Pobierz i zaktualizuj bootloader U-Boot do [wersji 2025-02-24 15:04:07](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}

2. Pobierz i zaktualizuj firmware do [wersji 4.7.4](https://fw.gl-inet.com/firmware/mt2500/release/openwrt-mt2500-4.7.4-0328-1743128340.bin)

## GL-X3000

1. Pobierz i zaktualizuj bootloader U-Boot do [wersji 2025-02-25 19:05:24](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}

2. Pobierz i zaktualizuj firmware do [wersji 4.7.4](https://fw.gl-inet.com/firmware/x3000/release/openwrt-x3000-4.7.4-0317-1742206344.bin)

## GL-XE3000

1. Pobierz i zaktualizuj bootloader U-Boot do [wersji 2025-02-25 19:07:14](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}

2. Pobierz i zaktualizuj firmware do [wersji 4.7.4](https://fw.gl-inet.com/firmware/xe3000/release/openwrt-xe3000-4.7.4-0317-1742206184.bin)

!!! Note

    Metody aktualizacji bootloadera U-Boot opisano [pod tym linkiem](https://docs.gl-inet.com/router/en/4/faq/upgrade_uboot_version/){target="_blank"}.

    Metody aktualizacji firmware opisano [pod tym linkiem](https://docs.gl-inet.com/router/en/4/tutorials/how_to_upgrade_downgrade_router/){target="_blank"}.

<br>
Szczerze przepraszamy za wszelkie niedogodności, jakie mogła spowodować ta sytuacja. W przyszłości dołożymy jeszcze większej staranności do ulepszania naszych produktów i firmware.

W przypadku osób, które już posiadają te routery, bezpłatnie przedłużymy okres gwarancji o jeden rok. Jeśli napotkasz jakiekolwiek problemy, skontaktuj się z naszymi zespołami wsparcia.

Jeśli problem będzie się utrzymywał mimo aktualizacji, skontaktuj się z naszym zespołem wsparcia pod adresem support@gl-inet.com, a bezpłatnie zapewnimy nowe urządzenie zastępcze.

Twoje zaufanie i wsparcie są dla nas niezwykle ważne i jesteśmy za nie bardzo wdzięczni.

<br>

Z poważaniem,

GL.iNet Technical Support

26 marca 2025
