# Jak używać kaskadowania VPN na routerach GL.iNet?

## Wprowadzenie

Kaskadowanie VPN jest często określane jako „podwójny VPN" w niektórych kontekstach, ale może się nieznacznie różnić na routerach GL.iNet. Podstawowa koncepcja jest zilustrowana poniżej.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (Router jako serwer VPN)**: Gdy router działa jako serwer VPN, klienci podłączeni do tego serwera będą domyślnie uzyskiwać dostęp do Internetu za pośrednictwem sieci ISP routera.

**VPN 2 (Router jako klient VPN)**: Router działa również jako klient VPN, łącząc się z usługą VPN innej firmy.

**Kaskadowanie VPN**: Router będzie przekierowywać ruch z tunelu VPN 1 do tunelu VPN 2, umożliwiając urządzeniom podłączonym do routera przez VPN 1 dostęp do Internetu za pośrednictwem usługi VPN innej firmy (VPN 2) zamiast sieci ISP routera.

## Jak włączyć kaskadowanie VPN

### Dla firmware v4.7 i wcześniejszych

1. Najpierw ustaw router jako serwer VPN. Protokół WireGuard jest zalecany dla większej prędkości. Zapoznaj się z [tym linkiem](../interface_guide/wireguard_server.md){target="_blank"}.

2. Wyeksportuj plik konfiguracyjny z routera i prześlij go na urządzenie klienckie, które będzie łączyć się z routerem przez VPN.

3. Ustaw router jako klient VPN, łącząc się z usługą VPN innej firmy. Protokół WireGuard jest zalecany dla większej prędkości. Zapoznaj się z [tym linkiem](../interface_guide/wireguard_client.md){target="_blank"}.

4. Po połączeniu strona **VPN Dashboard** zostanie wyświetlona jak poniżej, gdzie router został ustawiony jako serwer VPN i klient VPN jednocześnie.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Przejdź do sekcji VPN Server na tej samej stronie i kliknij **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Włącz **VPN Cascading** i kliknij **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. Kaskadowanie VPN jest włączone. Urządzenia podłączone do routera przez VPN będą uzyskiwać dostęp do Internetu za pośrednictwem usługi VPN innej firmy, zamiast sieci ISP routera.

### Dla firmware v4.8 i nowszych

1. Najpierw ustaw router jako serwer VPN. Protokół WireGuard jest zalecany dla większej prędkości. Zapoznaj się z [tym linkiem](../interface_guide/wireguard_server.md){target="_blank"}.

2. Wyeksportuj plik konfiguracyjny z routera i prześlij go na urządzenie klienckie, które będzie łączyć się z routerem przez VPN.

3. Ustaw router jako klient VPN, łącząc się z usługą VPN innej firmy. Protokół WireGuard jest zalecany dla większej prędkości. Zapoznaj się z [tym linkiem](../interface_guide/wireguard_client.md){target="_blank"}.

4. W panelu administracyjnym przejdź do **VPN Dashboard**. Wybierz odpowiednie instrukcje poniżej na podstawie trybu VPN.

    ??? "Tryb globalny"
    
        Jeśli Twój tryb VPN to tryb globalny, po włączeniu klienta VPN (jak pokazano poniżej), kaskadowanie VPN zostanie włączone automatycznie. 
        
        Urządzenia podłączone do routera przez VPN będą uzyskiwać dostęp do Internetu za pośrednictwem usługi VPN innej firmy, zamiast sieci ISP routera.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Tryb polityk"
    
        Jeśli Twój tryb VPN to tryb polityk, musisz skonfigurować regułę tunelu VPN.
        
        Kliknij wyszarzone pole po lewej stronie.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        Wybierz źródło ruchu, do którego ma być zastosowana ta reguła. Aby włączyć kaskadowanie VPN, wybierz **All Clients** lub wybierz **Specified Connection Types**, a następnie **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: Obejmuje wszystkie urządzenia LAN, urządzenia z Drop-in Gateway, urządzenia z sieci gościnnej oraz urządzenia podłączone do routera przez VPN. 
        
            Jeśli chcesz, aby ruch ze wszystkich urządzeń stosował tę samą regułę tunelu, wybierz **All Clients** i kliknij **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: Umożliwia określenie tych urządzeń podłączonych do routera przez określoną metodę (np. urządzenia podłączone przez VPN), aby zastosować tę regułę tunelu. 

            Jeśli chcesz określić klientów VPN routera, aby zastosowali inną regułę niż inne urządzenia, wybierz **WireGuard/OpenVPN Server** i kliknij **Apply**.
        
            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}
            
            To jest przykład reguł tunelu VPN w trybie polityk.
            
            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. Kaskadowanie VPN jest włączone. Urządzenia podłączone do routera przez VPN będą uzyskiwać dostęp do Internetu za pośrednictwem usługi VPN innej firmy, zamiast sieci ISP routera.

6. **Test połączenia**: Na laptopie podłączonym do routera przez VPN otwórz przeglądarkę i odwiedź [What Is My IP](https://whatismyipaddress.com/){target="_blank"}, aby sprawdzić jego publiczny adres IP. 

    Jeśli pokazuje, że adres IP laptopa znajduje się w regionie serwera VPN innej firmy (którym w tej instrukcji jest Buenos Aires), oznacza to, że kaskadowanie VPN zaczęło działać.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.