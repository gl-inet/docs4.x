# Avviso del browser: Your Connection is not Private

Potresti visualizzare questo avviso del browser se stai configurando per la prima volta il router GL.iNet: Your Connection is not Private.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Si tratta di un normale avviso di sicurezza emesso dal browser quando rileva un sito web privo di un certificato SSL/TLS attendibile.

I browser sono normalmente progettati per considerare attendibili i certificati emessi da autorità di certificazione (CA) di terze parti. Tuttavia, i router GL.iNet usano certificati autofirmati, che non sono emessi da CA. Per questo motivo i browser li segnalano come non sicuri e mostrano questo avviso.

## È sicuro visitare 192.168.8.1?

La sicurezza della rete è una nostra priorità. Durante la configurazione iniziale non è necessaria una connessione Internet, poiché il processo avviene interamente in locale.

Quando ti colleghi al Wi-Fi del router GL.iNet durante la configurazione, potresti vedere **"Connected, No internet"**. È normale, perché il router opera in una rete locale autonoma durante la configurazione.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

Allo stesso modo, l'IP **192.168.8.1** è un indirizzo IP locale privato assegnato al router stesso. Viene usato per accedere al pannello di amministrazione locale del dispositivo, non a un sito web pubblico.

Poiché la connessione è puramente locale e durante la configurazione non è richiesto l'accesso a Internet, **non c'è alcun rischio di perdita della privacy**. Questo garantisce un ambiente sicuro e isolato per configurare il router.

## Perché continuo a vedere un avviso?

I browser normalmente non distinguono tra un IP di configurazione predefinito e i normali siti web; trattano tutti gli indirizzi IP come siti web e si aspettano che le connessioni HTTPS siano protette da certificati SSL/TLS.

I router GL.iNet usano effettivamente certificati SSL/TLS, ma sono autofirmati e non emessi da autorità di certificazione (CA) di terze parti. Sebbene l'accesso a questo IP sia sicuro (perché avviene su una rete locale privata), il browser lo considera comunque "insecure", ed è per questo che viene mostrato l'avviso.

## Cosa posso fare con questo avviso?

Fai clic su **Advanced** e su **Continue to 192.168.8.1**.

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Verrai quindi reindirizzato al pannello di amministrazione web.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Posso aggiungere un certificato SSL nel router?

Sì, puoi aggiungere un certificato SSL ai router GL.iNet.

[Come aggiungere un certificato SSL](../faq/use_https_for_adh.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
