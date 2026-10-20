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
        default: 'es',
        translations: {
            es: {
                consentModal: {
                    title: 'Utilizamos cookies',
                    description: 'Este sitio web utiliza cookies esenciales para garantizar su correcto funcionamiento y cookies de seguimiento para entender cómo interactúa con él. Estas últimas solo se instalarán después de obtener su consentimiento. <button type="button" data-cc="c-settings" class="cc-link">Elegir preferencias</button>',
                    acceptAllBtn: 'Aceptar todas',
                    acceptNecessaryBtn: 'Rechazar todas',
                    showPreferencesBtn: 'Gestionar preferencias individuales'
                },
                preferencesModal: {
                    title: 'Preferencias de cookies',
                    acceptAllBtn: 'Aceptar todas',
                    acceptNecessaryBtn: 'Rechazar todas',
                    savePreferencesBtn: 'Aceptar la selección actual',
                    closeIconLabel: 'Cerrar',
                    sections: [
                        {
                            title: 'Uso de cookies 📢',
                            description: 'Utilizamos cookies para garantizar las funciones básicas del sitio web y mejorar su experiencia en línea. Puede dar o retirar su consentimiento para cada categoría en cualquier momento. Para obtener más información sobre las cookies y otros datos sensibles, lea la <a href="/privacy-policy/" class="cc-link">política de privacidad</a> completa.'
                        },
                        {
                            title: 'Cookies estrictamente necesarias',
                            description: 'Estas cookies son necesarias para que el sitio web funcione y no se pueden desactivar en nuestros sistemas. Normalmente solo se instalan en respuesta a acciones que usted realiza y que constituyen una solicitud de servicios, como redirigirle a la tienda en línea según nuestra ubicación, establecer sus preferencias de privacidad, iniciar sesión o rellenar formularios. Puede configurar el navegador para bloquear estas cookies o recibir avisos sobre ellas, pero algunas partes del sitio dejarán de funcionar. Estas cookies no almacenan información que permita identificarle personalmente.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Rendimiento y análisis',
                            description: 'Estas cookies nos permiten contar las visitas y las fuentes de tráfico para medir y mejorar el rendimiento de nuestro sitio. Nos ayudan a saber qué páginas son las más y las menos populares y cómo se desplazan los visitantes por el sitio. Toda la información que recopilan se agrega y, por tanto, es anónima. Si no permite estas cookies, no sabremos cuándo ha visitado nuestro sitio y no podremos supervisar su rendimiento.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Cookies del chat',
                            description: 'Estas cookies nos permiten ofrecerle una experiencia fluida de atención al cliente mediante el chat de freshchat y asistencia técnica sin interrupciones en nuestro sitio.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Cookies de publicidad y segmentación',
                            description: 'Nuestros socios publicitarios pueden instalar estas cookies a través de nuestro sitio. Esas empresas pueden utilizarlas para crear un perfil de sus intereses y mostrarle anuncios relevantes en otros sitios. No almacenan información personal directamente, sino que se basan en la identificación única de su navegador y dispositivo de Internet. Si no permite estas cookies, verá publicidad menos personalizada.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Más información',
                            description: 'Si tiene alguna pregunta sobre nuestra política de cookies o sus opciones, <a class="cc-link" href="/contacts/">póngase en contacto con nosotros</a>.',
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
