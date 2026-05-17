# Impossible de détecter le point d'accès 5G d'Android

Connecter le routeur GL.iNet comme répéteur au point d'accès 5G d'un téléphone Android est l'une des méthodes courantes pour accéder à Internet.

Cependant, si vous ne parvenez pas à détecter le point d'accès 5G de votre téléphone Android, le problème peut être lié au canal Wi-Fi.

Certains téléphones Android définissent par défaut leur point d'accès 5G sur un canal américain. Si votre routeur GL.iNet n'a pas été acheté à l'origine aux États-Unis, vous pouvez rencontrer ce problème.

Vous pouvez modifier le code pays Wi-Fi de votre routeur GL.iNet dans l'interface LuCI en suivant les étapes ci-dessous.

1. Connectez-vous à votre routeur GL.iNet, puis accédez à **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Connectez-vous à LuCI avec le même mot de passe administrateur.

2. Modifiez les paramètres Wi-Fi.

    Accédez à **Network** -> **Wireless**, repérez le Wi-Fi 5G et cliquez sur **Edit** à droite.

    ![5gwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gwifi.jpg){class="glboxshadow"}

3. Sélectionnez US comme code pays.

    Sur la page Wireless, cliquez sur l'onglet **Advanced Settings** sous **Device Configuration**. Sélectionnez US (United States) comme code pays pour votre Wi-Fi 5 GHz.

    ![5gus](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/5gus.jpg){class="glboxshadow"}

4. Cliquez sur **Save & Apply** avant de vous déconnecter.

    ![saveapply](https://static.gl-inet.com/docs/router/en/4/tutorials/5ghotspot/saveapply.jpg){class="glboxshadow"}

    Essayez ensuite de détecter à nouveau le point d'accès 5G de votre téléphone Android.

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
