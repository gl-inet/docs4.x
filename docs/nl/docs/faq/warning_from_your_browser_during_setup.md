# Browserwaarschuwing: `Your Connection is not Private` {#warning-from-your-browser-your-connection-is-not-private}

Wanneer je de GL.iNet-router voor het eerst instelt, kan de browser de waarschuwing `Your Connection is not Private` weergeven.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Dit is een standaardbeveiligingswaarschuwing die de browser toont bij een website zonder vertrouwd SSL/TLS-certificaat.

Browsers vertrouwen normaal certificaten van externe certificeringsinstanties (CA's). GL.iNet-routers gebruiken zelfondertekende certificaten die niet door een CA zijn uitgegeven. Daarom markeert de browser ze als onveilig en verschijnt deze waarschuwing.

## Is it safe to browse 192.168.8.1? {#is-it-safe-to-browse-19216881}

Tijdens de eerste installatie is geen internetverbinding nodig, omdat het proces volledig lokaal wordt uitgevoerd.

Wanneer je tijdens de installatie verbinding maakt met de wifi van de GL.iNet-router, kan **"Connected, No internet"** verschijnen. Dit is normaal, omdat de router tijdens de configuratie in een zelfstandig lokaal netwerk werkt.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

Het IP-adres **192.168.8.1** is een privé lokaal adres van de router. Het wordt gebruikt voor toegang tot het lokale beheerpaneel en is geen openbare website.

Omdat de verbinding volledig lokaal is en geen internet vereist, bestaat er **geen risico op privacylekken**. Je configureert de router in een veilige, geïsoleerde omgeving.

## Why do I still get a warning? {#why-do-i-still-get-a-warning}

Browsers maken meestal geen onderscheid tussen een vooraf ingesteld installatieadres en gewone websites. Ze behandelen elk IP-adres als een website en verwachten dat HTTPS met een SSL/TLS-certificaat is beveiligd.

GL.iNet-routers gebruiken SSL/TLS-certificaten, maar deze zijn zelfondertekend en niet door een externe CA uitgegeven. Toegang tot dit IP-adres is veilig omdat het zich in een privé lokaal netwerk bevindt, maar de browser beschouwt het toch als "onveilig" en toont daarom de waarschuwing.

## Wat kan ik met deze waarschuwing doen? {#what-can-i-do-with-this-warning}

Please click **Advanced** and **Continue to 192.168.8.1**

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Daarna word je naar het webbeheerpaneel geleid.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Kan ik een SSL-certificaat aan de router toevoegen? {#can-i-add-an-ssl-certificate-in-the-router}

Ja, je kunt een eigen SSL-certificaat aan GL.iNet-routers toevoegen.

[How to add a SSL certificate](../faq/use_https_for_adh.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
