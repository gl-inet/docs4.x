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
        default: 'sv',
        translations: {
            sv: {
                consentModal: {
                    title: 'Vi använder cookies',
                    description: 'Den här webbplatsen använder nödvändiga cookies för att fungera korrekt och spårningscookies för att förstå hur du använder den. Spårningscookies sparas först efter att du har samtyckt. <button type="button" data-cc="c-settings" class="cc-link">Låt mig välja</button>',
                    acceptAllBtn: 'Acceptera alla',
                    acceptNecessaryBtn: 'Avvisa alla',
                    showPreferencesBtn: 'Hantera enskilda inställningar'
                },
                preferencesModal: {
                    title: 'Cookieinställningar',
                    acceptAllBtn: 'Acceptera alla',
                    acceptNecessaryBtn: 'Avvisa alla',
                    savePreferencesBtn: 'Acceptera aktuellt val',
                    closeIconLabel: 'Stäng',
                    sections: [
                        {
                            title: 'Användning av cookies 📢',
                            description: 'Vi använder cookies för webbplatsens grundläggande funktioner och för att förbättra din upplevelse online. Du kan när som helst välja att godkänna eller avvisa cookies i varje kategori. Mer information om cookies och andra känsliga uppgifter finns i vår fullständiga <a href="/privacy-policy/" class="cc-link">integritetspolicy</a>.'
                        },
                        {
                            title: 'Absolut nödvändiga cookies',
                            description: 'Dessa cookies är nödvändiga för att webbplatsen ska fungera och kan inte stängas av i våra system. De sparas vanligtvis endast som svar på åtgärder som du utför och som innebär en begäran om tjänster, till exempel att du omdirigeras till webbutiken utifrån din plats, anger dina integritetsinställningar, loggar in eller fyller i formulär. Du kan ställa in webbläsaren så att den blockerar eller varnar om dessa cookies, men då fungerar inte vissa delar av webbplatsen. Dessa cookies lagrar inga uppgifter som kan identifiera dig personligen.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Prestanda och analys',
                            description: 'Med dessa cookies kan vi räkna besök och trafikkällor så att vi kan mäta och förbättra webbplatsens prestanda. De hjälper oss att se vilka sidor som är mest och minst populära och hur besökare rör sig på webbplatsen. All information som dessa cookies samlar in sammanställs och är därför anonym. Om du inte tillåter dessa cookies vet vi inte när du har besökt webbplatsen och kan inte övervaka dess prestanda.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Chattcookies',
                            description: 'Dessa cookies gör att vi kan erbjuda smidig kundservice via Freshchat och ge sammanhängande teknisk support på webbplatsen.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Cookies för annonsering och inriktning',
                            description: 'Dessa cookies kan sparas via vår webbplats av våra annonseringspartner. Företagen kan använda dem för att skapa en profil över dina intressen och visa relevanta annonser på andra webbplatser. De lagrar inte personuppgifter direkt, utan bygger på att din webbläsare och internetenhet identifieras unikt. Om du inte tillåter dessa cookies får du mindre riktad annonsering.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Mer information',
                            description: 'Om du har frågor om vår cookiepolicy eller dina val kan du <a class="cc-link" href="/contacts/">kontakta oss</a>.',
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
