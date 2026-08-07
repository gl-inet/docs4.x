# Czym jest USB-C OTG i jak udostępnić sieć przez USB-C OTG

## USB OTG
**USB OTG** (On-The-Go) to standard USB, który umożliwia zgodnym urządzeniom, takim jak routery, przełączanie się między rolami **Host** i **Device**. Pozwala to na bezpośrednią transmisję danych i obsługę zasilania bez osobnego urządzenia hosta.

Za pomocą **USB OTG** można przełączać dwa poniższe tryby:

- Gdy urządzenie przełącza się przez USB OTG w **tryb Host**, działa jako host USB: inicjuje transmisję danych, dostarcza zasilanie i kontroluje wszystkie operacje odczytu oraz zapisu między dwoma podłączonymi urządzeniami.

- W **Device mode** urządzenie działa jako urządzenie peryferyjne, pobiera zasilanie z hosta i pasywnie odpowiada na jego polecenia, bez możliwości samodzielnego inicjowania komunikacji.

## Udostępnianie sieci przez USB-C OTG na Mudi 7

Port USB-C z obsługą OTG w Mudi 7 działa w trybie **Device** albo **Host**, umożliwiając elastyczne udostępnianie sieci urządzeniom zewnętrznym.

### Połączenie z komputerem

Większość komputerów działa wyłącznie jako host i nie obsługuje OTG. Po podłączeniu komputera do routera przez USB router wyświetla okno wyboru trybu. Możesz wybrać dowolny tryb, a Mudi 7 automatycznie uzgodni rolę. Komputer rozpozna go następnie jako adapter USB do bezpośredniego dostępu do Internetu, bez dodatkowych sterowników.

### Połączenie ze smartfonem

- **Device Mode**: Mudi 7 działa jako urządzenie USB i udostępnia swoją sieć telefonowi.

- **Host Mode**: Po włączeniu USB Tethering w telefonie telefon może udostępnić swoją sieć komórkową Mudi 7 przez USB. To połączenie USB może działać jako niezależny interfejs WAN i umożliwiać Multi-WAN.

!!! Note

    1. Gdy używasz funkcji OTG w telefonie do połączenia urządzeń, upewnij się, że telefon obsługuje OTG i użyj kabla USB obsługującego transmisję danych. Kable wyłącznie do ładowania nie mogą przesyłać sygnałów sieciowych.

    2. Gdy Device Mode jest włączony, telefon nie wyświetli powiadomienia o połączeniu sieciowym. Aby sprawdzić działanie, sprawdź stan sieci w ustawieniach telefonu albo wykonaj test łączności.

        Jeśli na przykład udostępniasz sieć Mudi 7 telefonowi przez **Device Mode** (np. iPhone 17 Pro), sprawdź aktywność Device Mode, wykonując poniższe kroki.

        1. Użyj kabla USB obsługującego OTG, aby połączyć port USB 3.1 w Mudi 7 z iPhone 17 Pro.

        2. Na Mudi 7 wybierz **Device Mode**.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. W ustawieniach telefonu zobaczysz, że Mudi 7 zapewnia telefonowi dostęp do sieci, jak pokazano na poniższym zrzucie ekranu.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Masz dodatkowe pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} albo [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
