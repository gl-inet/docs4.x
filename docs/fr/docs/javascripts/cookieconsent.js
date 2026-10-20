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
        default: 'fr',
        translations: {
            fr: {
                consentModal: {
                    title: 'Nous utilisons des cookies',
                    description: 'Ce site utilise des cookies essentiels pour assurer son bon fonctionnement et des cookies de suivi pour comprendre comment vous interagissez avec lui. Ces derniers ne seront déposés qu’après votre consentement. <button type="button" data-cc="c-settings" class="cc-link">Choisir mes préférences</button>',
                    acceptAllBtn: 'Tout accepter',
                    acceptNecessaryBtn: 'Tout refuser',
                    showPreferencesBtn: 'Gérer les préférences individuelles'
                },
                preferencesModal: {
                    title: 'Préférences de cookies',
                    acceptAllBtn: 'Tout accepter',
                    acceptNecessaryBtn: 'Tout refuser',
                    savePreferencesBtn: 'Accepter la sélection actuelle',
                    closeIconLabel: 'Fermer',
                    sections: [
                        {
                            title: 'Utilisation des cookies 📢',
                            description: 'Nous utilisons des cookies pour assurer les fonctionnalités de base du site et améliorer votre expérience en ligne. Vous pouvez donner ou retirer votre consentement pour chaque catégorie à tout moment. Pour plus de détails sur les cookies et les autres données sensibles, veuillez consulter la <a href="/privacy-policy/" class="cc-link">politique de confidentialité</a> complète.'
                        },
                        {
                            title: 'Cookies strictement nécessaires',
                            description: 'Ces cookies sont nécessaires au fonctionnement du site et ne peuvent pas être désactivés dans nos systèmes. Ils sont généralement déposés uniquement en réponse à vos actions correspondant à une demande de services, comme la redirection vers la boutique en ligne en fonction de notre localisation, la définition de vos préférences de confidentialité, la connexion ou le remplissage de formulaires. Vous pouvez configurer votre navigateur pour bloquer ces cookies ou vous en avertir, mais certaines parties du site ne fonctionneront alors pas. Ces cookies ne stockent aucune information permettant de vous identifier personnellement.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Performances et analyse',
                            description: 'Ces cookies nous permettent de compter les visites et les sources de trafic afin de mesurer et d’améliorer les performances de notre site. Ils nous aident à identifier les pages les plus et les moins populaires et à comprendre comment les visiteurs naviguent sur le site. Toutes les informations recueillies par ces cookies sont agrégées et donc anonymes. Si vous n’autorisez pas ces cookies, nous ne saurons pas quand vous avez visité notre site et ne pourrons pas surveiller ses performances.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Cookies de chat',
                            description: 'Ces cookies nous permettent de vous offrir un service client fluide via le chat freshchat et une assistance technique sans interruption sur notre site.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Cookies publicitaires et de ciblage',
                            description: 'Ces cookies peuvent être déposés sur notre site par nos partenaires publicitaires. Ces entreprises peuvent les utiliser pour établir un profil de vos centres d’intérêt et vous proposer des publicités pertinentes sur d’autres sites. Ils ne stockent pas directement d’informations personnelles, mais reposent sur l’identification unique de votre navigateur et de votre appareil connecté à Internet. Si vous n’autorisez pas ces cookies, les publicités seront moins ciblées.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Informations complémentaires',
                            description: 'Pour toute question concernant notre politique de cookies et vos choix, veuillez <a class="cc-link" href="/contacts/">nous contacter</a>.',
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
