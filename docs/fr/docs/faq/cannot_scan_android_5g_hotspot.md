# Impossible de détecter le point d'accès 5G d'Android

Connecter le routeur GL.iNet comme répéteur au point d'accès 5G d'un téléphone Android est l'une des méthodes courantes pour accéder à Internet.

Cependant, si vous ne parvenez pas à détecter le point d'accès 5G de votre téléphone Android, le problème peut être lié au code pays du Wi-Fi.

Certains téléphones Android définissent par défaut leur point d'accès 5G sur un canal américain. Si votre routeur GL.iNet n'a pas été acheté à l'origine aux États-Unis, vous pouvez rencontrer ce problème.

Vous pouvez modifier le code pays Wi-Fi de votre routeur GL.iNet sur la page LuCI en suivant les étapes ci-dessous.

## Étape 1. Se connecter à LuCI

Connectez-vous à votre routeur GL.iNet puis, dans la barre latérale gauche, choisissez **SYSTEM -> Advanced Settings -> Go to LuCI**. Connectez-vous à LuCI avec le même mot de passe administrateur.

## Étape 2. Modifier les paramètres Wi-Fi

Accédez à **Network -> Wireless**, sélectionnez le Wi-Fi 5G puis cliquez sur Modifier. Si vous utilisez un GL-MT3000, accédez à **Network -> MTK Wi-Fi**.

![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

![mtkwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/mtkwifi.jpg){class="glboxshadow"}

## Étape 3. Sélectionner US comme code pays

Sous **Device Configuration -> Advanced Settings**, sélectionnez US (United States) comme code pays pour votre Wi-Fi 5 GHz.

![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

Cliquez sur **Save & Apply** avant de quitter.

![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

Essayez ensuite de détecter à nouveau le point d'accès 5G de votre téléphone Android.

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

