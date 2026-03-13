# Brume 2をGLiNetモバイルアプリに追加する方法

Wi-Fi機できるがない場合でも、Brume 2（GL-MT2500/GL-MT2500A）をGLiNetモバイルアプリに追加できます。メアルーターとしてもセカンダリールーターとしても設定できます。

で下の方法はBrume（GL-MV1000）にも適用できます。

## Brume 2をセカンダリールーターとして設定

**構成図**

ここではSlate AX（GL-AXT1800）をメアルーター、Brume 2（GL-MT2500）をセカンダリールーターとして説明します。

![top1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Brume 2のWeb管理パネルにログインし、システム -> セキュリティ -> ルーターで開くポートに移動し、ポート80を開きます。

    ![open80 1](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    一部の古いモデルの場合は、ファイアウォール -> ルーターで開くポートに移動し、ポート80を開きます。

    ![open80 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. メアルーターにログインし、Brume 2のWAN IPを記録します。

    ![assignip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. 携帯電話をメアルーターのWi-Fiに接続します。

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"}

4. glinetアプリを起動し、「新しいデバイスを追加」をクリックします。

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

5. 「初期化されたデバイス」をクリックします。

    ![initdevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.PNG){class="glboxshadow gl-50-desktop"}

6. メアルーターでメモしたWAN IPを入力します。

    ![inputip](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.PNG){class="glboxshadow gl-50-desktop"}

7. Brume 2のログインパスワードを入力します。

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    これでBrume 2がglinetモバイルアプリに表示されます。

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

## Brume 2をメアルーターとして設定

**構成図**

![top2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. セカンダリールーター（ここではGL-AXT1800）にログインし、アクセスポイントモードに設定します。

    ![setrouteap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. 携帯電話をセカンダリールーターのWi-Fiに接続します。

    ![upperwifi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.PNG){class="glboxshadow gl-50-desktop"} 

3. glinetアプリを起動し、「新しいデバイスを追加」をクリックします。

    ![adddevice](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.PNG){class="glboxshadow gl-50-desktop"}

4. メアルーターを選択します。

    ![selectbrume2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.PNG){class="glboxshadow gl-50-desktop"}

5. 「次へ」をクリックします

    ![setupap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.PNG){class="glboxshadow gl-50-desktop"}

6. まだセカンダリールーターのWi-Fiに接続している場合は、そのまま待ちます。接続していない場合は、セカンダリールーターのWi-Fiに再度接続します。

    ![connectap](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.PNG){class="glboxshadow gl-50-desktop"}

7. Brume 2のログインパスワードを入力します。

    ![inputpw](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.PNG){class="glboxshadow gl-50-desktop"}

    これでBrume 2がglinetモバイルアプリに表示されます。

    ![showup](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.PNG){class="glboxshadow gl-50-desktop"}

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
