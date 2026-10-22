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
        default: 'nl',
        translations: {
            nl: {
                consentModal: {
                    title: 'Wij gebruiken cookies',
                    description: 'Deze website gebruikt noodzakelijke cookies voor een goede werking en trackingcookies om te begrijpen hoe je de website gebruikt. Trackingcookies worden pas geplaatst nadat je toestemming hebt gegeven. <button type="button" data-cc="c-settings" class="cc-link">Zelf kiezen</button>',
                    acceptAllBtn: 'Alles accepteren',
                    acceptNecessaryBtn: 'Alles weigeren',
                    showPreferencesBtn: 'Individuele voorkeuren beheren'
                },
                preferencesModal: {
                    title: 'Cookievoorkeuren',
                    acceptAllBtn: 'Alles accepteren',
                    acceptNecessaryBtn: 'Alles weigeren',
                    savePreferencesBtn: 'Huidige selectie accepteren',
                    closeIconLabel: 'Sluiten',
                    sections: [
                        {
                            title: 'Gebruik van cookies 📢',
                            description: 'Wij gebruiken cookies om de basisfuncties van de website te laten werken en je online ervaring te verbeteren. Je kunt voor elke categorie op elk moment toestemming geven of intrekken. Lees voor meer informatie over cookies en andere gevoelige gegevens ons volledige <a href="/privacy-policy/" class="cc-link">privacybeleid</a>.'
                        },
                        {
                            title: 'Strikt noodzakelijke cookies',
                            description: 'Deze cookies zijn noodzakelijk voor de werking van de website en kunnen in onze systemen niet worden uitgeschakeld. Ze worden meestal alleen geplaatst als reactie op handelingen waarmee je om een dienst vraagt, zoals doorsturen naar de webwinkel op basis van onze locatie, privacyvoorkeuren instellen, inloggen of formulieren invullen. Je kunt je browser zo instellen dat deze cookies worden geblokkeerd of dat je ervoor wordt gewaarschuwd, maar sommige delen van de website werken dan niet. Deze cookies slaan geen persoonlijk identificeerbare informatie op.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Prestaties en analyse',
                            description: 'Met deze cookies kunnen we bezoeken en verkeersbronnen tellen, zodat we de prestaties van onze website kunnen meten en verbeteren. Ze laten zien welke pagina\'s het meest en minst populair zijn en hoe bezoekers door de website navigeren. Alle informatie die deze cookies verzamelen, wordt samengevoegd en is daarom anoniem. Als je deze cookies niet toestaat, weten we niet wanneer je onze website hebt bezocht en kunnen we de prestaties ervan niet volgen.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Chatcookies',
                            description: 'Met deze cookies kunnen we je via de freshchat-chat een soepele klantenservice en naadloze technische ondersteuning op onze website bieden.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Advertentie- en targetingcookies',
                            description: 'Onze advertentiepartners kunnen deze cookies via onze website plaatsen. Deze bedrijven kunnen ze gebruiken om een profiel van je interesses op te stellen en je relevante advertenties op andere websites te tonen. Ze slaan niet rechtstreeks persoonlijke informatie op, maar zijn gebaseerd op de unieke identificatie van je browser en internetapparaat. Als je deze cookies niet toestaat, krijg je minder gerichte advertenties te zien.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Meer informatie',
                            description: 'Neem bij vragen over ons cookiebeleid en je keuzes <a class="cc-link" href="/contacts/">contact met ons op</a>.',
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
