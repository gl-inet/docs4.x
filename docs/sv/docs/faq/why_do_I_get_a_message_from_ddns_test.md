# Varför visas ett meddelande från DDNS-testet? {#why-do-i-get-a-message-from-ddns-test}

När du kör DDNS-testet på sidan Dynamic DNS kan ett meddelande enligt nedan visas.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

Det är inte ett **Warning**- eller **Error**-meddelande, utan en påminnelse som visar routerns nätverksstatus.

Resultatet visar vanligtvis routerns position i nätverket. Meddelandet visas till exempel om GL.iNet-routern är konfigurerad som sekundär router i hemnätverket.

Det försvinner inte även om du har konfigurerat portvidarebefordran på den primära routern. Det visar helt enkelt att routern finns bakom NAT.

Om du behöver göra tjänster tillgängliga via NAT, till exempel för fjärråtkomst, krävs ytterligare inställningar.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
