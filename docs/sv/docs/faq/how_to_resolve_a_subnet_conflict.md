# Hur löser jag en konflikt i LAN-subnätet? {#how-to-resolve-a-lan-subnet-conflict}

När du ansluter en Ethernet-kabel från hemmaroutern till WAN-porten på GL.iNet-routern kan följande meddelande ibland visas:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Det beror på att hemmaroutern använder samma LAN-IP-adress som GL.iNet-routern. Detta kallas en LAN-konflikt.

Följ stegen nedan för att ändra LAN-subnätet.

## 1. Ändra LAN-subnätet {#1-change-lan-subnet}

Klicka på länken **Change LAN Subnet**. Du omdirigeras till inställningssidan **LAN**.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Ändra talet efter den andra punkten (som standard **8**) till ett annat tal, till exempel 192.168.10.1, och klicka sedan på **Apply**.

Vänta några sekunder efter ändringen. Sidan uppdateras och omdirigeras automatiskt till den nya IP-adressen **192.168.10.1**. Meddelandet om subnätskonflikten försvinner.

Fortsätt med nästa steg om sidan inte omdirigeras.

## 2. Logga in med den nya LAN-IP-adressen {#2-login-with-new-lan-ip}

Ange den nya LAN-IP-adressen manuellt i adressfältet och tryck på Enter.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Logga in med ditt administratörslösenord. Meddelandet om subnätskonflikten försvinner.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
