# Comment ajouter Brume 2 dans l'application mobile GL.iNet ?

Vous pouvez ajouter votre Brume 2 (GL-MT2500/GL-MT2500A) dans l'application mobile GL.iNet même s'il ne dispose pas de la fonction Wi-Fi. Vous pouvez le configurer comme routeur principal ou comme routeur secondaire.

Les méthodes ci-dessous s'appliquent également à Brume (GL-MV1000).

## Brume 2 comme routeur secondaire

**Topologie**

Ici, Slate AX (GL-AXT1800) est utilisé comme routeur principal et Brume 2 (GL-MT2500) comme routeur secondaire.

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Connectez-vous au panneau d'administration web de votre Brume 2, allez dans **SYSTEM** -> **Security** -> **Open Ports on Router**, puis ouvrez le port **80**.

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    Sur certains anciens modèles, allez dans **Firewall** -> **Open Ports on Router**, puis ouvrez le port **80**.

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Connectez-vous au routeur principal et notez la **WAN IP** de Brume 2.

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Connectez un téléphone au Wi-Fi de votre routeur principal.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

4. Ouvrez l'application GL.iNet et appuyez sur **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

5. Cliquez ensuite sur **Initialized Devices**.

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.PNG){class="glboxshadow gl-50-desktop"}

6. Saisissez la **WAN IP** que vous avez relevée auparavant sur le routeur principal.

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.PNG){class="glboxshadow gl-50-desktop"}

7. Saisissez le mot de passe de connexion de Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Votre Brume 2 apparaîtra alors dans l'application mobile GL.iNet.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

## Brume 2 comme routeur principal

**Topologie**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Connectez-vous à votre routeur secondaire, qui est ici un GL-AXT1800, puis réglez-le en mode Access Point.

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Connectez un téléphone au Wi-Fi de votre routeur secondaire.

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"} 

3. Ouvrez l'application GL.iNet et appuyez sur **Add New Device**.

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

4. Sélectionnez votre routeur principal.

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.PNG){class="glboxshadow gl-50-desktop"}

5. Cliquez sur **Next**

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.PNG){class="glboxshadow gl-50-desktop"}

6. Si vous êtes toujours connecté au Wi-Fi du routeur secondaire, attendez simplement. Sinon, reconnectez-vous au Wi-Fi du routeur secondaire.

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.PNG){class="glboxshadow gl-50-desktop"}

7. Saisissez le mot de passe de connexion de Brume 2.

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    Votre Brume 2 apparaîtra alors dans l'application mobile GL.iNet.

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
