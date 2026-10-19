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
        default: 'uk',
        translations: {
            uk: {
                consentModal: {
                    title: 'Ми використовуємо файли cookie',
                    description: 'Цей сайт використовує необхідні файли cookie для належної роботи та файли cookie для відстеження, щоб зрозуміти, як ви взаємодієте із сайтом. Файли cookie для відстеження встановлюються лише після вашої згоди. <button type="button" data-cc="c-settings" class="cc-link">Вибрати налаштування</button>',
                    acceptAllBtn: 'Прийняти всі',
                    acceptNecessaryBtn: 'Відхилити всі',
                    showPreferencesBtn: 'Керувати окремими налаштуваннями'
                },
                preferencesModal: {
                    title: 'Налаштування файлів cookie',
                    acceptAllBtn: 'Прийняти всі',
                    acceptNecessaryBtn: 'Відхилити всі',
                    savePreferencesBtn: 'Прийняти поточний вибір',
                    closeIconLabel: 'Закрити',
                    sections: [
                        {
                            title: 'Використання файлів cookie 📢',
                            description: 'Ми використовуємо файли cookie для забезпечення основних функцій сайту та покращення вашого досвіду користування ним. Ви можете будь-коли надати або відкликати згоду для кожної категорії. Докладну інформацію про файли cookie та інші конфіденційні дані наведено в повній <a href="/privacy-policy/" class="cc-link">політиці конфіденційності</a>.'
                        },
                        {
                            title: 'Суворо необхідні файли cookie',
                            description: 'Ці файли cookie необхідні для роботи сайту, і їх неможливо вимкнути в наших системах. Зазвичай вони встановлюються лише у відповідь на ваші дії, які є запитом на послуги, наприклад для перенаправлення до інтернет-магазину відповідно до нашого розташування, збереження налаштувань конфіденційності, входу в обліковий запис або заповнення форм. Ви можете налаштувати браузер так, щоб він блокував ці файли cookie або попереджав про них, але тоді деякі частини сайту не працюватимуть. Ці файли cookie не зберігають інформацію, яка дозволяє ідентифікувати особу.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Продуктивність та аналітика',
                            description: 'Ці файли cookie дозволяють нам підраховувати відвідування та джерела трафіку, щоб оцінювати й покращувати роботу сайту. Вони допомагають визначити найпопулярніші та найменш популярні сторінки й зрозуміти, як відвідувачі переміщуються сайтом. Уся інформація, яку збирають ці файли cookie, узагальнюється і тому є анонімною. Якщо ви не дозволите ці файли cookie, ми не знатимемо, коли ви відвідали наш сайт, і не зможемо відстежувати його продуктивність.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Файли cookie чату',
                            description: 'Ці файли cookie дозволяють нам забезпечувати зручне обслуговування через чат freshchat і безперебійну технічну підтримку на нашому сайті.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Рекламні та таргетингові файли cookie',
                            description: 'Наші рекламні партнери можуть встановлювати ці файли cookie через наш сайт. Ці компанії можуть використовувати їх для створення профілю ваших інтересів і показу відповідної реклами на інших сайтах. Вони не зберігають персональні дані безпосередньо, а ґрунтуються на унікальній ідентифікації вашого браузера та інтернет-пристрою. Якщо ви не дозволите ці файли cookie, реклама буде менш персоналізованою.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Додаткова інформація',
                            description: 'Якщо у вас є запитання щодо нашої політики використання файлів cookie або вашого вибору, <a class="cc-link" href="/contacts/">зв’яжіться з нами</a>.',
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
