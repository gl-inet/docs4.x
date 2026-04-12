# Zmiana WAN na LAN

Możesz zmienić port WAN routera na port LAN. Jest to szczególnie przydatne podczas korzystania z routera w trybie repeatera, gdy port WAN nie jest potrzebny. Po zmianie portu WAN na LAN zyskasz dodatkowy port LAN, co zwiększy możliwości połączeń przewodowych.

Wykonaj poniższe kroki, aby zmienić WAN na LAN.

## Dla firmware 4.7 i nowszego

1. Pozostaw port WAN niepodłączony.

2. Podłącz urządzenie do routera i otwórz panel administracyjny routera.

3. W panelu administracyjnym przejdź do sekcji **INTERNET** -> **Ethernet** i kliknij ikonę koła zębatego w prawym górnym rogu.

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

	Zostaniesz przeniesiony na stronę **Port Management**, gdzie status portu WAN będzie widoczny jako używany dla WAN.

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Kliknij **LAN**, aby zmienić właściwości portu Ethernet, a następnie kliknij **Apply**.

	![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

	W wyświetlonym oknie ostrzeżenia kliknij **Apply**, aby potwierdzić.
	
	![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

	**Uwaga**: Podczas tego procesu połączenie Wi-Fi może zostać chwilowo przerwane. Po zakończeniu połącz się z routerem ponownie.

5. Po powrocie do sekcji **Ethernet** zobaczysz, że port WAN jest teraz używany jako port LAN.

	![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

	Możesz zmienić go z powrotem na WAN na stronie **Port Management** albo przytrzymać przycisk RESET przez 4 sekundy, aby ponownie uruchomić interfejs WAN.

## Dla firmware 4.6 i starszego

1. Pozostaw port WAN niepodłączony.

2. Podłącz urządzenie do routera i otwórz panel administracyjny.

3. W panelu administracyjnym przejdź do sekcji **INTERNET** -> **Ethernet**, gdzie status portu WAN będzie wyświetlany jako **Using as WAN**. Kliknij **Change to LAN**.

	![internet page](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Kliknij **Apply**, aby potwierdzić.

	![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

	**Uwaga**: Podczas tego procesu połączenie Wi-Fi może zostać chwilowo przerwane. Po zakończeniu połącz się z routerem ponownie.

5. Po powrocie do sekcji **Ethernet** zobaczysz status `Using as LAN`.

	![using as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

	Możesz łatwo cofnąć tę zmianę, powtarzając powyższe kroki.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
