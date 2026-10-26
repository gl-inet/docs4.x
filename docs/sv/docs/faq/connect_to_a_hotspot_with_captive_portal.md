# Anslut en GL.iNet-router till en offentlig hotspot med captive portal {#connect-a-glinet-router-to-public-hotspots-with-a-captive-portal}

## Vad är en captive portal? {#what-is-a-captive-portal}

En captive portal är en webbsida som användare av en offentlig hotspot måste visa och interagera med innan de får internetåtkomst.

## Varför använda en router för offentliga hotspots? {#why-use-a-router-for-public-hotspots}

* Offentligt Wi-Fi är inte säkert

    Riskerna med offentligt Wi-Fi är stora. Genom att ansluta GL.iNet-routern till offentligt Wi-Fi kan du logga in på VPN-kontot direkt via routerns administrationspanel. Routern krypterar automatiskt trafiken för alla anslutna enheter i det lokala nätverket, så att du slipper konfigurera VPN på varje enskild enhet.

* Använd routern som repeater för att ansluta flera enheter

    Vissa offentliga Wi-Fi-nätverk, till exempel på hotell, begränsar dessutom åtkomsten till exempelvis två enheter. Det är opraktiskt när flera personer reser tillsammans. Du kan i stället ansluta en reserouter till hotellets Wi-Fi och använda den som repeater för att sända en Wi-Fi-signal till alla dina enheter, till exempel bärbara datorer, smarttelefoner och surfplattor. Hotellets Wi-Fi identifierar endast reseroutern som en enda enhet, men du kan ansluta valfritt antal enheter till det kostnadsfria nätverket.

## Hur ansluter jag routern till en offentlig hotspot med captive portal? {#how-to-connect-router-to-public-hotspots-with-captive-portal}

Titta på videon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Anslut en smarttelefon eller dator till routern.

    Slå på routern. Sök efter routerns SSID på smarttelefonen eller datorn och ange Wi-Fi-lösenordet. Standard-SSID och standardlösenordet står på routerns undersida.

2. Logga in på routerns webbadministrationspanel.

    Öppna en webbläsare på smarttelefonen eller datorn och ange routerns IP-adress (standard-IP: `192.168.8.1`) i adressfältet. Routerns webbadministrationspanel öppnas.

    Om du loggar in för första gången väljer du ett språk och skapar ett inloggningslösenord för routerns webbadministrationspanel.

3. Anslut routern till den offentliga hotspoten. Följ guiden för [Repeater](../interface_guide/internet_repeater.md/).

## Felsökning {#troubleshooting}

Om captive portal-sidan inte öppnas kanske routern inte kommer åt internet. Prova följande felsökningsmetoder.

### Metod 1: Aktivera inloggningsläge för offentliga hotspots och kamouflage {#method-1-enable-public-hotspot-login-mode-camouflage}

**Obs!** De två funktionerna är endast tillgängliga i firmware v4.6 och senare.

När du ansluter routern till en offentlig hotspot kan följande funktioner på sidan **Join Network** öka chansen att anslutningen lyckas.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    Om alternativet är aktiverat växlar routern automatiskt till Login Mode for Public Hotspots när den har anslutits till en hotspot men inte till internet. I läget pausas vissa tjänster och DNS-läget ändras till automatiskt. Det kan göra att din nätverksaktivitet blir synlig för hotspot-leverantören, till exempel ett hotell eller köpcentrum.

- Enable Camouflage

    Om alternativet är aktiverat imiterar routern den klientenhet som du använder för att öppna administrationspanelen genom att emulera enhetens MAC-adress.

---

### Metod 2: Ändra routerinställningarna {#method-2-change-router-settings}

1. Logga in på webbadministrationspanelen och gå till NETWORK -> DNS. Kontrollera att **DNS Rebinding Attack Protection** är inaktiverat och att **Mode** är inställt på **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. Gå till VPN -> VPN Dashboard i webbadministrationspanelen. Kontrollera att alla VPN-anslutningar är inaktiverade.

    **För firmware v4.7 och tidigare** visas sidan enligt nedan.

    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}

    **För firmware v4.8 och senare** visas sidan enligt nedan.

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. Gå till APPLICATIONS -> AdGuard Home i webbadministrationspanelen. Kontrollera att AdGuard Home är inaktiverat.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Öppna en webbläsare och öppna eller uppdatera captive portal-sidan igen. Vänta i en minut och kontrollera om du omdirigeras automatiskt till captive portal-sidan för autentisering.

    Om du använder en smarttelefon och webbläsaren inte omdirigerar till captive portal stänger du av telefonens Wi-Fi och slår sedan på det igen. Återanslut därefter till routerns Wi-Fi. Captive portal-sidan ska visas direkt efter att du har angett Wi-Fi-lösenordet.

    ![connected](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Metod 3: Klona MAC-adressen {#method-3mac-clone}

Vissa hotell begränsar antalet enheter som varje kund får ansluta till hotellets Wi-Fi genom att identifiera enheternas MAC-adresser. De registrerar enhetens MAC-adress vid den första anslutningen. I så fall kan du klona MAC-adressen som telefonen använder för hotellets Wi-Fi till routern, så att routern använder den MAC-adressen för åtkomst till hotellets Wi-Fi.

1. Anslut telefonen till hotellets Wi-Fi. Leta reda på MAC-adressen som telefonen använder för att ansluta till hotellets Wi-Fi.

    På en iPhone (iOS 16.1.2) kan du till exempel gå till Settings -> Wi-Fi -> välj hotellets Wi-Fi. Där hittar du Wi-Fi Address. Anteckna adressen.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    På vissa äldre modeller kanske MAC-adressen inte är tillgänglig i Wi-Fi-inställningarna. Enheten kan då använda sin verkliga MAC-adress vid anslutning till offentligt Wi-Fi. Du hittar den i telefonens Settings > About (eller "About Phone").

2. Anslut telefonen eller datorn till routern. Logga in på routerns webbadministrationspanel och klona eller ange MAC-adressen manuellt.

    **För firmware v4.5 och tidigare** väljer du NETWORK till vänster -> MAC Address.

    Välj Manual Mode, ange MAC-adressen från steg 1 och klicka på Apply.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **För firmware v4.6 och senare** väljer du INTERNET till vänster -> avsnittet Repeater och klickar på Modify.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    Ändra MAC Mode till Clone i dialogrutan, ange MAC-adressen manuellt och klicka på Apply.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. Routern kan behöva startas om för att ändringen ska börja gälla.

---

### Metod 4: Be hotellpersonalen om hjälp {#method-4seek-help-from-hotel-staff}

Vissa hotell har mycket strikta verifieringsregler för sina nätverk. Om ingen av metoderna ovan fungerar kan du be hotellpersonalen att lägga till routerns MAC-adress direkt i hotellets tillåtelselista. Använd MAC-adressen som är inställd från fabriken, inte den slumpmässiga adressen.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
