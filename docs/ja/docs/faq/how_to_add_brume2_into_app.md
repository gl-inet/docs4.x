# Brume 2をGLiNetモバイルアプリに追加する方法 {#how-to-add-brume-2-into-glinet-mobile-app}

Wi-Fi機能がない場合でも、Brume 2（GL-MT2500/GL-MT2500A）をGLiNetモバイルアプリに追加できます。メインルーターとしてもセカンダリールーターとしても設定できます。

以下の方法はBrume（GL-MV1000）にも適用できます。

## Brume 2をセカンダリールーターとして設定 {#brume-2-as-the-secondary-router}

**構成図**

ここではSlate AX（GL-AXT1800）をメインルーター、Brume 2（GL-MT2500）をセカンダリールーターとして説明します。

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Brume 2のWeb管理パネルにログインし、**SYSTEM** -> **Security** -> **Open Ports on Router** に移動して、ポート **80** を開きます。

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    一部の古いモデルの場合は、**Firewall** -> **Open Ports on Router** に移動して、ポート **80** を開きます。

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. メインルーターにログインし、Brume 2の **WAN IP** を控えます。

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. スマートフォンをメインルーターのWi-Fiに接続します。

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

4. glinetアプリを起動し、**Add New Device** をタップします。

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

5. **Initialized Devices** をタップします。

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.png){class="glboxshadow gl-50-desktop"}

6. 先ほどメインルーターで確認したWAN IPを入力します。

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.png){class="glboxshadow gl-50-desktop"}

7. Brume 2のログインパスワードを入力します。

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    これでBrume 2がglinetモバイルアプリに表示されます。

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

## Brume 2をメインルーターとして設定 {#brume-2-as-the-main-router}

**構成図**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. セカンダリールーター（ここではGL-AXT1800）にログインし、アクセスポイントモードに設定します。

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. スマートフォンをセカンダリールーターのWi-Fiに接続します。

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"} 

3. glinetアプリを起動し、**Add New Device** をタップします。

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

4. メインルーターを選択します。

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.png){class="glboxshadow gl-50-desktop"}

5. **Next** をタップします。

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.png){class="glboxshadow gl-50-desktop"}

6. まだセカンダリールーターのWi-Fiに接続している場合は、そのまま待ちます。接続していない場合は、セカンダリールーターのWi-Fiに再度接続します。

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.png){class="glboxshadow gl-50-desktop"}

7. Brume 2のログインパスワードを入力します。

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    これでBrume 2がglinetモバイルアプリに表示されます。

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
