# Webbläsarvarning: Anslutningen är inte privat {#warning-from-your-browser-your-connection-is-not-private}

Om det är första gången du konfigurerar GL.iNet-routern kan webbläsaren visa varningen `Your Connection is not Private`.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Det är en vanlig säkerhetsvarning som webbläsaren visar när den identifierar en webbplats utan ett betrott SSL/TLS-certifikat.

Webbläsare är vanligtvis utformade för att lita på certifikat som utfärdas av externa certifikatutfärdare (CA). GL.iNet-routrar använder däremot självsignerade certifikat som inte har utfärdats av en CA. Därför markerar webbläsare dem som osäkra och visar varningen.

## Är det säkert att öppna 192.168.8.1? {#is-it-safe-to-browse-19216881}

Vi prioriterar din nätverkssäkerhet. Under den första konfigurationen behövs ingen internetanslutning eftersom hela processen sker lokalt.

När du ansluter till GL.iNet-routerns Wi-Fi under konfigurationen kan **"Connected, No internet"** visas. Det är förväntat eftersom routern fungerar i ett fristående lokalt nätverk under konfigurationen.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

IP-adressen **192.168.8.1** är på samma sätt en privat lokal IP-adress som har tilldelats själva routern. Den används för att öppna enhetens lokala administrationspanel, inte en offentlig webbplats.

Eftersom anslutningen är helt lokal och ingen internetåtkomst krävs under konfigurationen finns **ingen risk för att privata uppgifter läcker**. Det ger en säker och isolerad miljö för konfiguration av routern.

## Varför visas varningen ändå? {#why-do-i-still-get-a-warning}

Webbläsare skiljer vanligtvis inte mellan en förinställd IP-adress för konfiguration och vanliga webbplatser. De behandlar alla IP-adresser som webbplatser och förväntar sig att HTTPS-anslutningar skyddas med SSL/TLS-certifikat.

GL.iNet-routrar använder SSL/TLS-certifikat, men de är självsignerade och har inte utfärdats av externa certifikatutfärdare (CA). Även om det är säkert att öppna IP-adressen eftersom den finns i ett privat lokalt nätverk, betraktar webbläsaren den ändå som "osäker" och visar därför varningen.

## Vad gör jag med varningen? {#what-can-i-do-with-this-warning}

Klicka på **Advanced** och **Continue to 192.168.8.1**.

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Du omdirigeras sedan till webbadministrationspanelen.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Kan jag lägga till ett SSL-certifikat i routern? {#can-i-add-an-ssl-certificate-in-the-router}

Ja, du kan lägga till ett eget SSL-certifikat i GLiNet-routrar.

[Lägga till ett SSL-certifikat](../faq/use_https_for_adh.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
