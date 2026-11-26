# Komunikat o problemie dotyczącym GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Ostatnia aktualizacja 11 listopada 2026 r.**

Ten znany problem dotyczy tylko niektórych partii urządzeń. Urządzenia zamówione od 1 lipca 2025 r. najprawdopodobniej pochodzą z nowszej partii i nie wymagają aktualizacji programu rozruchowego U-Boot.

Jeśli nie wiesz, z której partii pochodzi Twoje urządzenie, przed wprowadzeniem zmian wyślij poniższe informacje na adres [support@gl-inet.com](mailto:support@gl-inet.com).

- Model routera i wersja firmware
- Adres MAC urządzenia
- Opis problemu z informacją o tym, co robiono w chwili jego wystąpienia, komunikatami o błędach i wykonanymi już próbami rozwiązania problemu

Potwierdzimy partię produkcyjną i podamy wskazówki dotyczące rozwiązania problemu.

---

Poniżej zachowano pierwotny komunikat w celach informacyjnych. Podane w nim kroki aktualizacji dotyczą wyłącznie partii objętych problemem. Jeśli nie wiesz, czy problem dotyczy Twojego urządzenia, przed wprowadzeniem zmian skontaktuj się z pomocą techniczną zgodnie z powyższymi wskazówkami.

**Opublikowano 26 marca 2025 r.**

Drodzy Klienci GL.iNet,

Ten komunikat dotyczy problemów z uruchamianiem urządzenia oraz odzyskiwaniem firmware przez U-Boot w modelach GL-MT2500/GL-X3000/GL-XE3000. Przyczyną był defekt oprogramowania, w którym część parametrów została nieprawidłowo zdefiniowana, przez co routery działały nieprawidłowo. W rezultacie oceniliśmy, że problem ten mógł w pewnym stopniu skrócić żywotność routerów, za co szczerze przepraszamy.

Aby całkowicie rozwiązać ten problem, zdecydowanie zalecamy wszystkim użytkownikom GL-MT2500, GL-X3000 i GL-XE3000 wykonanie zarówno aktualizacji bootloadera U-Boot, jak i aktualizacji firmware. Obie procedury są niezbędne i nie należy pomijać żadnej z nich.

Nawet jeśli urządzenie zostało już zaktualizowane do najnowszej wersji firmware, aktualizacja bootloadera U-Boot nadal jest obowiązkowa, aby zapobiec potencjalnym problemom. Po zakończeniu aktualizacji bootloadera U-Boot możesz pominąć ponowną instalację firmware, jeśli najnowsza wersja jest już zainstalowana.

Do aktualizacji użyj przeglądarki Chrome lub Microsoft Edge. NIE używaj Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Zaktualizuj program rozruchowy U-Boot.

    Pobierz plik [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}, a następnie [zaktualizuj program rozruchowy U-Boot](upgrade_uboot_version.md).

2. Zaktualizuj firmware.

    Pobierz [najnowsze firmware dla swojego routera](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"}, a następnie [zaktualizuj firmware routera](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Zaktualizuj program rozruchowy U-Boot.

    Pobierz plik [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}, a następnie [zaktualizuj program rozruchowy U-Boot](upgrade_uboot_version.md).

2. Zaktualizuj firmware.

    Pobierz [najnowsze firmware dla swojego routera](https://dl.gl-inet.com/router/x3000/stable){target="_blank"}, a następnie [zaktualizuj firmware routera](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-XE3000 {#gl-xe3000}

1. Zaktualizuj program rozruchowy U-Boot.

    Pobierz plik [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}, a następnie [zaktualizuj program rozruchowy U-Boot](upgrade_uboot_version.md).

2. Zaktualizuj firmware.

    Pobierz [najnowsze firmware dla swojego routera](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"}, a następnie [zaktualizuj firmware routera](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
Szczerze przepraszamy za wszelkie niedogodności, jakie mogła spowodować ta sytuacja. W przyszłości dołożymy jeszcze większej staranności do ulepszania naszych produktów i firmware.

W przypadku osób, które już posiadają te routery, bezpłatnie przedłużymy okres gwarancji o jeden rok. Jeśli napotkasz jakiekolwiek problemy, skontaktuj się z naszymi zespołami wsparcia.

Jeśli problem będzie się utrzymywał mimo aktualizacji, skontaktuj się z naszym zespołem wsparcia pod adresem [support@gl-inet.com](mailto:support@gl-inet.com), a bezpłatnie zapewnimy nowe urządzenie zastępcze.

Twoje zaufanie i wsparcie są dla nas niezwykle ważne i jesteśmy za nie bardzo wdzięczni.

<br>
Z poważaniem,<br>
Zespół GL.iNet<br>
26 marca 2025 r.
