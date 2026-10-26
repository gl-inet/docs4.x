# Så tillåter du åtkomst till WAN när VPN-klienten är aktiverad {#how-to-allow-access-to-wan-when-vpn-client-is-enabled}

När VPN-klienten är aktiverad på GL.iNet-routrar kan LAN-enheter i det globala standardläget inte komma åt enheter eller tjänster på det lokala WAN-nätverket. All trafik från LAN dirigeras genom VPN-tunneln i stället för genom det uppströms nätverket (WAN) för att förhindra DNS-läckor.

Den här guiden beskriver hur du gör lokala WAN-tjänster, till exempel skrivare och NAS, åtkomliga för enheter på VPN-klientens LAN.

![allow access wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## För firmware v4.7 och tidigare {#for-firmware-v47-and-earlier}

Logga in på VPN-klientens webbadministrationspanel och gå till **VPN** -> **VPN Dashboard** -> **VPN Client**. Klicka på **Global Options** i det övre högra hörnet.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Aktivera **Allow Access WAN** och klicka på **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

När det här alternativet är aktiverat kan klientenheter fortfarande komma åt WAN-tjänster i det överordnade subnätet, till exempel skrivare och NAS, medan VPN-anslutningen är aktiv.

## För firmware v4.8 och senare {#for-firmware-v48-and-higher}

Alternativet **Allow Access WAN** har tagits bort från VPN Dashboard i firmware v4.8. Du kan i stället använda en VPN-policy för att ge åtkomst till det lokala WAN-nätverket.

Följ stegen nedan.

1. Logga in på VPN-klientens webbadministrationspanel och gå till **VPN** -> **VPN Dashboard**.

    Klicka på läget i det övre högra hörnet.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Växla till **Policy Mode** och klicka på **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    Sidan uppdateras och visas enligt nedan.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Klicka på rutan i mitten för att ange tunnelns mål.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Välj **Exclude specified Domain / IP List**, ange routerns WAN-subnät och klicka sedan på **Apply**.

    Detta gör att all trafik till WAN-subnätet dirigeras genom det lokala WAN-nätverket i stället för genom VPN-tunneln.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    Här använder vi subnätet 192.168.0.1/24 som exempel. Ange subnätet och tillämpa inställningen. VPN-tunneln visas då enligt nedan.

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Hur tar jag reda på GL.iNet-routerns WAN-subnät?"

        GL.iNet-routerns WAN-subnät visas vanligtvis på sidan INTERNET. Det bestäms av den uppströmsenhet som routerns WAN-gränssnitt är anslutet till, till exempel ett modem från internetleverantören eller en uppströmsgateway.

        Om routern till exempel används som sekundär router och dess WAN-port är ansluten till ett annat lokalt nätverk, såsom ett modem från internetleverantören eller huvudrouterns LAN-port, och routerns WAN-IP är 192.168.1.165, gatewayen är 192.168.1.1 och nätmasken är 255.255.255.0 (en vanlig nätmask för små nätverk), är motsvarande WAN-subnät 192.168.1.0/24. Det är även den uppströmsenhetens LAN-subnät.

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Obs!** Prefixlängden för 192.168.1.0/24 är 24, vilket motsvarar nätmasken 255.255.255.0. Om routerns WAN-nätmask inte är 255.255.255.0 är prefixlängden för WAN-subnätet inte "/24". Fastställ WAN-subnätet utifrån den faktiska WAN-konfigurationen.

3. Klicka på rutan till höger för att ange tunnelåtgärden, det vill säga om VPN ska användas.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Välj **Use VPN** och välj en VPN-konfigurationsfil. Klicka sedan på **Apply**.

    Om det inte finns någon tillgänglig konfiguration laddar du först upp en för att använda routern som VPN-klient. Gå sedan tillbaka till den här sidan, välj **Use VPN**, välj en VPN-konfigurationsfil och klicka på **Apply**.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Aktivera VPN-tunneln med reglaget i det övre högra hörnet. Anslutningen startar.

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Vänta några minuter. När anslutningen har upprättats blir indikatorn grön.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Sök efter din offentliga IP-adress för att testa VPN-anslutningen. Öppna till exempel en webbläsare och besök [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Sidan visar din offentliga IP-adress och plats enligt nedan.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Öppna enheter eller tjänster i WAN-subnätet och kontrollera att de är åtkomliga.

    Du kan testa anslutningen med kommandot ping.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
