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
        default: 'ja',
        translations: {
            ja: {
                consentModal: {
                    title: 'Cookieを使用しています',
                    description: 'このウェブサイトでは、正常な動作に必要なCookieと、サイトの利用状況を把握するためのトラッキングCookieを使用します。トラッキングCookieは同意後にのみ設定されます。<button type="button" data-cc="c-settings" class="cc-link">設定を選択する</button>',
                    acceptAllBtn: 'すべて同意する',
                    acceptNecessaryBtn: 'すべて拒否する',
                    showPreferencesBtn: '個別の設定を管理する'
                },
                preferencesModal: {
                    title: 'Cookieの設定',
                    acceptAllBtn: 'すべて同意する',
                    acceptNecessaryBtn: 'すべて拒否する',
                    savePreferencesBtn: '現在の選択に同意する',
                    closeIconLabel: '閉じる',
                    sections: [
                        {
                            title: 'Cookieの使用について 📢',
                            description: 'ウェブサイトの基本機能を提供し、オンラインでの利用体験を向上させるためにCookieを使用します。カテゴリごとにいつでも同意または同意の撤回を選択できます。Cookieやその他の機密データに関する詳細は、<a href="/privacy-policy/" class="cc-link">プライバシーポリシー</a>の全文をご覧ください。'
                        },
                        {
                            title: '必須Cookie',
                            description: 'これらのCookieはウェブサイトの動作に必要なため、当社のシステムでは無効にできません。通常は、当社の所在地に応じたウェブストアへのリダイレクト、プライバシー設定の保存、ログイン、フォームへの入力など、サービスの要求に該当する操作に応じてのみ設定されます。ブラウザでこれらのCookieをブロックしたり、警告を表示したりできますが、その場合はサイトの一部が動作しなくなります。これらのCookieには、個人を特定できる情報は保存されません。',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'パフォーマンスと分析',
                            description: 'これらのCookieにより、アクセス数とトラフィックの流入元を集計し、サイトのパフォーマンスを測定・改善できます。人気の高いページと低いページや、訪問者がサイト内をどのように移動するかを把握するのに役立ちます。これらのCookieが収集する情報はすべて集計されるため、匿名です。これらのCookieを許可しない場合、当社はお客様がサイトを訪問したことを把握できず、サイトのパフォーマンスを監視できません。',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'チャットCookie',
                            description: 'これらのCookieにより、freshchatのチャットを通じた円滑なカスタマーサービスと、サイト上での途切れのないテクニカルサポートを提供できます。',
                            linkedCategory: 'chat'
                        },
                        {
                            title: '広告・ターゲティングCookie',
                            description: 'これらのCookieは、広告パートナーによって当社のサイトを通じて設定される場合があります。各社は、お客様の関心に基づくプロフィールを作成し、他のサイトで関連する広告を表示するために使用する場合があります。個人情報を直接保存するものではなく、ブラウザとインターネット接続デバイスの一意の識別に基づいています。これらのCookieを許可しない場合、関心に合わせた広告が少なくなります。',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: '詳しい情報',
                            description: 'Cookieに関する当社のポリシーやお客様の選択についてご質問がある場合は、<a class="cc-link" href="/contacts/">お問い合わせください</a>。',
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
