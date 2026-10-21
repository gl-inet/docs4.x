# Konfigurera dubbelt trådbundet Ethernet WAN med en Ethernet-till-USB-A-adapter {#configure-dual-wired-ethernet-wan-via-an-ethernet-to-usb-a-adapter}

Du kan konfigurera dubbla trådbundna Ethernet WAN-anslutningar på en router med en enda WAN-port genom att använda en Ethernet-till-USB-A-adapter.

GL.iNet-routrar stöder vanliga Ethernet-till-USB-A-adaptrar. Det gör att du kan omvandla den trådbundna Ethernet-anslutningen från internetleverantörens router till en USB-anslutning via routerns USB-port och ge routern ytterligare en trådbunden Ethernet-anslutning vid sidan av WAN-porten.

## Topologi {#topology}

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Konfigurationssteg {#setup-steps}

1. Anslut Ethernet-till-USB-A-adaptern till USB-porten på GL.iNet-routern och anslut den andra änden till internetleverantörens router.

2. Installera USB-drivrutinen.

    Logga in på routerns webbadministrationspanel, gå till **Application** -> **Plug-ins** och installera USB-nätverksdrivrutinen för adaptern.

    Om du till exempel använder en Realtek-adapter installerar du drivrutinen **kmod-usb-net-rtl8152**.

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Vänta tills installationen är klar.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Anslut med internetdelning via USB.

    När drivrutinen har installerats går du till **INTERNET** -> avsnittet **Tethering**.

    USB-anslutningen identifieras så att du kan ansluta till internetleverantörens router.

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Klicka på **Connect** och vänta i en minut. När en grön punkt tänds och sidan visar information som IP-adressen har anslutningen med internetdelning via USB upprättats.

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
