# Vad gör jag om installationen av eSIM-profilen misslyckas? {#what-should-i-do-if-esim-profile-installation-fails}

Följ stegen nedan för felsökning om du försöker lägga till en eSIM-profil på GL.iNet-routern men installationen misslyckas:

1. Kontrollera att routern är ansluten till internet.

    Kontrollera att routern har anslutits till internet. Ett instabilt nätverk kan påverka uppladdningen av eSIM-profilen så att routern inte kan hämta och installera den.

    Prova om möjligt att ansluta routern till en annan nätverkskälla (till exempel din smarttelefons hotspot eller ett offentligt Wi-Fi-nätverk) och ladda sedan upp eSIM-profilen igen för att testa.

2. Ändra DNS-inställningarna.

    Om internet fungerar korrekt loggar du in på routerns webbadministrationspanel och går till **NETWORK** -> **DNS**.

    Ändra DNS Mode till **Manual DNS** och ange andra offentliga DNS-servrar för routern för att testa, till exempel Google DNS (`8.8.8.8`, `8.8.4.4`) eller Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Klicka på **Apply** för att spara ändringarna och försök sedan ladda upp eSIM-profilen igen.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. Inaktivera AdGuard Home.

    Om AdGuard Home är tillgängligt och aktiverat på routern inaktiverar du det och försöker installera eSIM-profilen igen.

4. Kontrollera att eSIM-profilen är tillgänglig.

    Kontrollera om eSIM-profilen eller QR-koden redan har aktiverats eller installerats på en annan enhet.

    De flesta eSIM-profiler kan endast installeras en gång och kan inte aktiveras på flera enheter. Kontakta om möjligt eSIM-tjänsteleverantören för att kontrollera om den aktuella eSIM-profilen är tillgänglig. Om eSIM-QR-koden (eller aktiveringskoden) har upphört att gälla begär du en ny och försöker sedan ladda upp den till routern igen.

5. Kontrollera aktiveringskoden.

    En korrekt formaterad QR-kod visar en aktiveringskod som börjar med **LPA:**. Vissa QR-koder som inte följer standarden innehåller dock endast en obearbetad aktiveringskod utan LPA-prefix. Lägg i så fall till `LPA:` manuellt i början av koden innan du klickar på knappen Install.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Kontrollera om en bekräftelsekod krävs.

    För vissa eSIM-profiler måste du ange en bekräftelsekod under installationen (till exempel Smarty eSIM). Kontrollera eSIM-paketet eller installationsguiden för att ta reda på om en bekräftelsekod krävs. Ange i så fall rätt kod.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Om stegen ovan inte löser problemet exporterar du eSIM-loggen från sidan eSIM Management.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Skicka sedan loggen tillsammans med följande viktiga information till [support@gl-inet.com](mailto:support@gl-inet.com) för mer hjälp.

    - Problemet du har stött på
    - Felsökningsmetoder som du har provat (om några)
    - Din eSIM-leverantör

---
