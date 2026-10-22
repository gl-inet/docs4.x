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
        default: 'de',
        translations: {
            de: {
                consentModal: {
                    title: 'Wir verwenden Cookies',
                    description: 'Diese Website verwendet notwendige Cookies, um ihren ordnungsgemäßen Betrieb sicherzustellen, sowie Tracking-Cookies, um zu verstehen, wie Sie mit ihr interagieren. Letztere werden erst nach Ihrer Einwilligung gesetzt. <button type="button" data-cc="c-settings" class="cc-link">Auswahl treffen</button>',
                    acceptAllBtn: 'Alle akzeptieren',
                    acceptNecessaryBtn: 'Alle ablehnen',
                    showPreferencesBtn: 'Individuelle Einstellungen verwalten'
                },
                preferencesModal: {
                    title: 'Cookie-Einstellungen',
                    acceptAllBtn: 'Alle akzeptieren',
                    acceptNecessaryBtn: 'Alle ablehnen',
                    savePreferencesBtn: 'Aktuelle Auswahl akzeptieren',
                    closeIconLabel: 'Schließen',
                    sections: [
                        {
                            title: 'Verwendung von Cookies 📢',
                            description: 'Wir verwenden Cookies, um die grundlegenden Funktionen der Website sicherzustellen und Ihr Online-Erlebnis zu verbessern. Sie können Ihre Einwilligung für jede Kategorie jederzeit erteilen oder widerrufen. Weitere Informationen zu Cookies und anderen sensiblen Daten finden Sie in der vollständigen <a href="/privacy-policy/" class="cc-link">Datenschutzerklärung</a>.'
                        },
                        {
                            title: 'Unbedingt erforderliche Cookies',
                            description: 'Diese Cookies sind für den Betrieb der Website erforderlich und können in unseren Systemen nicht deaktiviert werden. Sie werden normalerweise nur als Reaktion auf Ihre Handlungen gesetzt, die einer Anforderung von Diensten entsprechen, etwa die Weiterleitung zum Webshop entsprechend unserem Standort, das Festlegen Ihrer Datenschutzeinstellungen, die Anmeldung oder das Ausfüllen von Formularen. Sie können Ihren Browser so einstellen, dass er diese Cookies blockiert oder Sie darüber informiert. Einige Bereiche der Website funktionieren dann jedoch nicht. Diese Cookies speichern keine Informationen, mit denen Sie persönlich identifiziert werden können.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Leistung und Analyse',
                            description: 'Diese Cookies ermöglichen uns, Besuche und Datenverkehrsquellen zu zählen, damit wir die Leistung unserer Website messen und verbessern können. Sie helfen uns zu erkennen, welche Seiten am beliebtesten und welche am wenigsten beliebt sind und wie sich Besucher auf der Website bewegen. Alle von diesen Cookies erfassten Informationen werden zusammengefasst und sind daher anonym. Wenn Sie diese Cookies nicht zulassen, wissen wir nicht, wann Sie unsere Website besucht haben, und können ihre Leistung nicht überwachen.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Chat-Cookies',
                            description: 'Diese Cookies ermöglichen uns, Ihnen über den freshchat-Chat einen reibungslosen Kundenservice und nahtlosen technischen Support auf unserer Website anzubieten.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Werbe- und Targeting-Cookies',
                            description: 'Diese Cookies können von unseren Werbepartnern über unsere Website gesetzt werden. Diese Unternehmen können sie nutzen, um ein Profil Ihrer Interessen zu erstellen und Ihnen auf anderen Websites relevante Werbung anzuzeigen. Sie speichern keine personenbezogenen Daten direkt, sondern basieren auf der eindeutigen Identifizierung Ihres Browsers und Internetgeräts. Wenn Sie diese Cookies nicht zulassen, erhalten Sie weniger zielgerichtete Werbung.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Weitere Informationen',
                            description: 'Bei Fragen zu unserer Cookie-Richtlinie und Ihren Auswahlmöglichkeiten <a class="cc-link" href="/contacts/">kontaktieren Sie uns</a>.',
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
