# Een LAN-subnetconflict oplossen {#how-to-resolve-a-lan-subnet-conflict}

Wanneer je een Ethernetkabel van je thuisrouter op de WAN-poort van de GL.iNet-router aansluit, kan het volgende bericht verschijnen:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Dit komt doordat je thuisrouter hetzelfde LAN-IP gebruikt als de GL.iNet-router. Dit wordt een LAN-conflict genoemd.

Follow the steps below to change the LAN subnet.

## 1. Change LAN Subnet {#1-change-lan-subnet}

Klik op **Change LAN Subnet**. Je wordt naar de instellingenpagina **LAN** geleid.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Wijzig het getal na de tweede punt, standaard **8**, in een ander getal, bijvoorbeeld 192.168.10.1. Klik daarna op **Apply**.

Wacht na de wijziging enkele seconden. De pagina wordt vernieuwd en automatisch doorgestuurd naar het gewijzigde IP-adres **192.168.10.1**. De melding over het subnetconflict verdwijnt.

Ga door met de volgende stap als de pagina niet wordt doorgestuurd.

## 2. Aanmelden met het nieuwe LAN-IP {#2-login-with-new-lan-ip}

Voer het gewijzigde LAN-IP handmatig in de adresbalk in en druk op Enter.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Meld je aan met je beheerderswachtwoord. De melding over het subnetconflict verdwijnt.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
