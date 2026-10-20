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
        default: 'pl',
        translations: {
            pl: {
                consentModal: {
                    title: 'Używamy plików cookie',
                    description: 'Ta witryna używa niezbędnych plików cookie do prawidłowego działania oraz śledzących plików cookie, aby zrozumieć, jak z niej korzystasz. Te drugie zostaną ustawione dopiero po uzyskaniu zgody. <button type="button" data-cc="c-settings" class="cc-link">Wybierz ustawienia</button>',
                    acceptAllBtn: 'Zaakceptuj wszystkie',
                    acceptNecessaryBtn: 'Odrzuć wszystkie',
                    showPreferencesBtn: 'Zarządzaj poszczególnymi preferencjami'
                },
                preferencesModal: {
                    title: 'Preferencje plików cookie',
                    acceptAllBtn: 'Zaakceptuj wszystkie',
                    acceptNecessaryBtn: 'Odrzuć wszystkie',
                    savePreferencesBtn: 'Zaakceptuj bieżący wybór',
                    closeIconLabel: 'Zamknij',
                    sections: [
                        {
                            title: 'Korzystanie z plików cookie 📢',
                            description: 'Używamy plików cookie, aby zapewnić podstawowe funkcje witryny i poprawić komfort korzystania z niej. W każdej chwili możesz udzielić lub wycofać zgodę dla każdej kategorii. Więcej informacji o plikach cookie i innych danych wrażliwych znajdziesz w pełnej <a href="/privacy-policy/" class="cc-link">polityce prywatności</a>.'
                        },
                        {
                            title: 'Ściśle niezbędne pliki cookie',
                            description: 'Te pliki cookie są niezbędne do działania witryny i nie można ich wyłączyć w naszych systemach. Zwykle są ustawiane wyłącznie w odpowiedzi na działania stanowiące prośbę o usługę, takie jak przekierowanie do sklepu internetowego zgodnie z naszą lokalizacją, ustawienie preferencji prywatności, logowanie lub wypełnianie formularzy. Możesz ustawić przeglądarkę tak, aby blokowała te pliki cookie lub ostrzegała o nich, ale niektóre części witryny nie będą wtedy działać. Te pliki cookie nie przechowują informacji pozwalających zidentyfikować użytkownika.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Wydajność i analityka',
                            description: 'Te pliki cookie pozwalają nam zliczać odwiedziny i źródła ruchu, aby mierzyć i poprawiać wydajność witryny. Pomagają ustalić, które strony są najbardziej i najmniej popularne oraz jak odwiedzający poruszają się po witrynie. Wszystkie zbierane przez nie informacje są agregowane, a zatem anonimowe. Jeśli nie zezwolisz na te pliki cookie, nie będziemy wiedzieć, kiedy odwiedzasz naszą witrynę, ani nie będziemy mogli monitorować jej wydajności.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Pliki cookie czatu',
                            description: 'Te pliki cookie pozwalają nam zapewnić sprawną obsługę klienta przez czat freshchat oraz nieprzerwane wsparcie techniczne w naszej witrynie.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Reklamowe i targetujące pliki cookie',
                            description: 'Te pliki cookie mogą być ustawiane za pośrednictwem naszej witryny przez partnerów reklamowych. Firmy te mogą używać ich do tworzenia profilu Twoich zainteresowań i wyświetlania odpowiednich reklam w innych witrynach. Nie przechowują bezpośrednio danych osobowych, lecz opierają się na unikalnej identyfikacji przeglądarki i urządzenia internetowego. Jeśli nie zezwolisz na te pliki cookie, zobaczysz mniej dopasowane reklamy.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Więcej informacji',
                            description: 'W razie pytań dotyczących naszej polityki plików cookie lub Twoich wyborów <a class="cc-link" href="/contacts/">skontaktuj się z nami</a>.',
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
