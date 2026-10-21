# Dynamic DNS {#dynamic-dns}

Dynamic Domain Name Service (Dynamic DNS eller DDNS) kopplar ett domännamn till en nätverksenhets dynamiska IP-adress. Med Dynamic DNS kan du fjärransluta till routern. Funktionen kräver en offentlig IP-adress på internet.

## Enable DDNS {#enable-ddns}

Öppna **APPLICATIONS** -> **Dynamic DNS** på vänster sida i webbadministrationspanelen.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Aktivera **Enable DDNS**, godkänn **Terms of Services & Privacy Policy** och klicka på **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Klicka på **Security Settings** i det nedre högra hörnet.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

Kontrollera i popup-fönstret att önskat fjärråtkomstprotokoll är aktiverat. Annars öppnar du SYSTEM -> Security -> Remote Access Control och aktiverar det.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Aktivera önskat fjärråtkomstprotokoll och klicka på **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Synkroniseringen av poster mellan DNS-servrar kan ta upp till 10 minuter. Därför kanske DDNS-domännamnet inte fungerar omedelbart efter aktivering eller när den offentliga IP-adressen ändras.

**Obs!** Om DDNS och VPN Client aktiveras samtidigt måste **Services From GL.iNet Use VPN** vara inaktiverat. Alternativet finns under [VPN Client Options](vpn_dashboard_v4.8.md#tunnel-options) på VPN Dashboard.

## Kontrollera att DDNS fungerar {#check-if-ddns-works}

Kontrollera DDNS med testverktyget eller manuellt med kommandon.

=== "Using the DDNS Test tool"

    Klicka på **DDNS Test** på sidan Dynamic DNS.

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Kontrollera att IP-adressen från DDNS-domänupplösningen motsvarar routerns WAN-IP.

    Annars visas ett gult meddelande som anger att routern kan finnas bakom NAT och att portvidarebefordran måste konfigureras på den uppströms routern.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Using commands"

    1. Använd kommandot `nslookup` för att hämta kopplingen mellan domännamn och IP-adress enligt nedan.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup.png){class="glboxshadow" width="600"}

        **Tips:**

        - Ersätt "xxxxxxx.glddns.com" i bilden ovan med ditt Host Name.

        - "8.8.8.8" i bilden ovan är Google DNS. Använd den eller ersätt den med en annan DNS och tryck på Enter.

    2. Avgör utifrån resultatet om DDNS-domänen har kopplats till en offentlig IP-adress.

        - En offentlig IP-adress som "183.178.10.100" anger att DDNS-domänen har kopplats korrekt.

        - Meddelandet "server can't find xxxxxxx.glddns.com" kan ange att domänupplösningen misslyckades och att domänen inte har kopplats till en offentlig IP-adress. Fortsätt till nästa steg.

    3. Logga in på routerns webbadministrationspanel och öppna **INTERNET**. Leta reda på routerns WAN-IP-adress i det aktiva gränssnittet och jämför den med den offentliga adressen ovan. Om de är samma fungerar DDNS.

## HTTPS Remote Access {#https-remote-access}

!!! Note

    1. A **Public IP** address is required for HTTPS remote access.

        Klicka [här](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) för att kontrollera om internetleverantören tilldelar en offentlig IP-adress.

    2. Om routern finns bakom NAT konfigurerar du portvidarebefordran (port **443**) på den uppströms routern för HTTPS-åtkomst.

Följ stegen nedan för att aktivera HTTPS-fjärråtkomst.

1. Aktivera **Enable DDNS** på sidan Dynamic DNS, godkänn **Terms of Services & Privacy Policy** och klicka på **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. In the web admin panel, go to SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Enable **HTTPS Remote Access**, and click **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

När funktionen är aktiverad kan du öppna routerns administratörspanel var som helst med DDNS-värdnamnet via **HTTPS**, till exempel `https://xxxxxxx.glddns.com`.

Om portvidarebefordran är konfigurerad använder du `https://xxxxxxx.glddns.com:external_port` och ersätter external_port med det faktiska portnumret.

**Obs!** Funktionen använder självsignerade certifikat. Webbläsaren visar därför **Your connection is not private** när administratörspanelen öppnas via DDNS-värdnamnet över **HTTPS**. Port 8001 används i exemplet nedan.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Fortsätt med HTTPS-fjärråtkomst genom att klicka på **Advanced** längst ned.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Klicka sedan på **Proceed to xxxxxxx.glddns.com**.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Du kan därefter öppna webbadministrationspanelen med DDNS-värdnamnet via HTTPS.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSH Remote Access {#ssh-remote-access}

!!! Note

    1. A **Public IP** address is required for SSH remote access.

        Klicka [här](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) för att kontrollera om internetleverantören tilldelar en offentlig IP-adress.

    2. Om routern finns bakom NAT konfigurerar du portvidarebefordran (port **22**) på den uppströms routern för SSH-åtkomst.

Följ stegen nedan för att aktivera SSH-fjärråtkomst.

1. Aktivera **Enable DDNS** på sidan Dynamic DNS, godkänn **Terms of Services & Privacy Policy** och klicka på **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. In the web admin panel, go to SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Enable **SSH Remote Access**, and click **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

När funktionen är aktiverad kan du fjärransluta till routerns terminal med DDNS-värdnamnet via **SSH**, till exempel `ssh root@xxxxxxx.glddns.com`.

Om portvidarebefordran är konfigurerad använder du `ssh -p external_port root@xxxxxxx.glddns.com` och ersätter external_port med det faktiska portnumret.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
