(function () {
    const host = window.location.hostname;
    const isLocalPreview = window.location.protocol === 'file:' ||
        host === 'localhost' ||
        host === '127.0.0.1' ||
        host === '0.0.0.0' ||
        host === '::1' ||
        host === '[::1]';

    if (isLocalPreview) {
        return;
    }

    CookieConsent.run({
    guiOptions: {
        consentModal: {
            layout: "box",
            position: "bottom left",
            equalWeightButtons: true,
            flipButtons: false
        },
        preferencesModal: {
            layout: "box",
            position: "right",
            equalWeightButtons: true,
            flipButtons: false
        }
    },

    categories: {
        necessary: {
            enabled: true,  // this category is enabled by default
            readOnly: true  // this category cannot be disabled
        },
        analytics: {
            services: {}
        },
        chat: {},
        marketing: {}
    },
    cookie: { domain: '.gl-inet.com' },
    language: {
        default: 'it',
        translations: {
            it: {
                consentModal: {
                    title: 'Utilizziamo i cookie',
                    description: 'Questo sito utilizza cookie essenziali per garantirne il corretto funzionamento e cookie di tracciamento per capire come interagisci con il sito. Questi ultimi vengono impostati solo dopo il tuo consenso. <button type="button" data-cc="c-settings" class="cc-link">Scegli le preferenze</button>',
                    acceptAllBtn: 'Accetta tutti',
                    acceptNecessaryBtn: 'Rifiuta tutti',
                    showPreferencesBtn: 'Gestisci le singole preferenze'
                },
                preferencesModal: {
                    title: 'Preferenze dei cookie',
                    acceptAllBtn: 'Accetta tutti',
                    acceptNecessaryBtn: 'Rifiuta tutti',
                    savePreferencesBtn: 'Accetta la selezione attuale',
                    closeIconLabel: 'Chiudi',
                    sections: [
                        {
                            title: 'Utilizzo dei cookie 📢',
                            description: 'Utilizziamo i cookie per garantire le funzionalità di base del sito e migliorare la tua esperienza online. Puoi dare o revocare il consenso per ogni categoria in qualsiasi momento. Per maggiori dettagli sui cookie e altri dati sensibili, leggi l’<a href="/privacy-policy/" class="cc-link">informativa sulla privacy</a> completa.'
                        },
                        {
                            title: 'Cookie strettamente necessari',
                            description: 'Questi cookie sono necessari per il funzionamento del sito e non possono essere disattivati nei nostri sistemi. Di solito vengono impostati solo in risposta ad azioni che costituiscono una richiesta di servizi, come il reindirizzamento al negozio online in base alla nostra posizione, l’impostazione delle preferenze sulla privacy, l’accesso o la compilazione di moduli. Puoi configurare il browser per bloccare questi cookie o ricevere un avviso, ma alcune parti del sito non funzioneranno. Questi cookie non memorizzano informazioni che consentono di identificarti personalmente.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Prestazioni e analisi',
                            description: 'Questi cookie ci consentono di contare le visite e le fonti di traffico per misurare e migliorare le prestazioni del sito. Ci aiutano a capire quali pagine sono più e meno popolari e come i visitatori si spostano nel sito. Tutte le informazioni raccolte da questi cookie sono aggregate e quindi anonime. Se non autorizzi questi cookie, non sapremo quando hai visitato il sito e non potremo monitorarne le prestazioni.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Cookie della chat',
                            description: 'Questi cookie ci consentono di offrirti un servizio clienti fluido tramite la chat freshchat e assistenza tecnica senza interruzioni sul nostro sito.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Cookie pubblicitari e di targeting',
                            description: 'Questi cookie possono essere impostati sul nostro sito dai nostri partner pubblicitari. Le aziende possono utilizzarli per creare un profilo dei tuoi interessi e mostrarti annunci pertinenti su altri siti. Non memorizzano direttamente informazioni personali, ma si basano sull’identificazione univoca del browser e del dispositivo connesso a Internet. Se non autorizzi questi cookie, vedrai pubblicità meno mirate.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Ulteriori informazioni',
                            description: 'Per qualsiasi domanda sulla nostra politica sui cookie e sulle tue scelte, <a class="cc-link" href="/contacts/">contattaci</a>.',
                        }
                    ]
                }
            }
        }
    },

    onConsent: ({ cookie }) => {   
        gtag('consent', 'update', {
            'ad_storage': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_user_data': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_personalization': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'analytics_storage': cookie.categories.includes('analytics') ? 'granted' : 'denied',
            'functionality_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'personalization_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'security_storage': 'granted',
        });
    },


    onChange: ({ cookie, changedCategories, changedServices }) => {
        console.log(cookie, changedCategories, changedServices)
        gtag('consent', 'update', {
            'ad_storage': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_user_data': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_personalization': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'analytics_storage': cookie.categories.includes('analytics') ? 'granted' : 'denied',
            'functionality_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'personalization_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'security_storage': 'granted',
        });
    }
    });
})();
