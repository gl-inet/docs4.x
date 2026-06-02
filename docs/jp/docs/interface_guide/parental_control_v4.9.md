# ペアレンタルコントロール（ファームウェア v4.9）

> このガイドはファームウェア v4.9 以降に適用されます。以前のバージョンについては [こちら](parental_control.md) をクリックしてください。

Web Admin Panel の左側で、**FLOW CONTROL** -> **Parental Control** に移動します。

ペアレンタルコントロールは、不適切な Web サイトをブロックし、スクリーンタイムを制限することで、子どもをオンライン上で保護します。有害なコンテンツをフィルタリングし、責任あるインターネット利用を促します。

GL.iNet Parental Control では、子どもがよく使うデバイスのインターネットアクセスを制限するための柔軟なスケジュール設定を利用できます。不適切なアプリや Web サイトをワンクリックでブロックできます。さらに、必要に応じてドメインを手動で入力し、包括的なオンライン保護を実現できます。

ファームウェア v4.9 では、Parental Control のページレイアウトと操作フローが改善され、設定が簡単になり、ルールをより直感的に確認できるようになりました。

---

以下の手順でペアレンタルコントロールを設定してください。

1. ルーターの Web Admin Panel にログインし、**FLOW CONTROL** -> **Parental Control** に移動します。ルーターの時刻が正しいことを確認してください。

    ![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/router_time.png){class="glboxshadow"}

    正しくない場合は、まず **SYSTEM** -> **Time Zone** に移動して同期してください。

2. Parental Control を有効にして、**Apply** をクリックします。

    ![enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/enable.png){class="glboxshadow"}

3. 以下のようなルール一覧が表示されます。**Add a New Rule** をクリックします。

    ![add a new rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/add_rules.png){class="glboxshadow"}

4. ポップアップウィンドウでルールを作成し、カスタム名を設定してから **Next** をクリックします。

    ![create a rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/create_rule.png){class="glboxshadow gl-90-desktop"}

5. 子どものデバイスを選択し、**Next** をクリックします。

    このページに表示されるのは、Wi-Fi または Ethernet でルーターに接続されているデバイスのみです。シアンはオンライン、グレーはオフラインを示します。

    ![select device](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/select_device.png){class="glboxshadow gl-90-desktop"}

    **ヒント**: 接続されているデバイスを区別しやすくしたい場合は、**CLIENTS** ページでデバイス名をカスタマイズしてください。

6. 子どものデバイスの就寝時間を設定し、**Next** をクリックします。

    この時間帯は、選択したデバイスでインターネットを利用できません。デフォルトでは、毎日同じ就寝時間が適用されます。

    ![bedtime1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/bedtime1.png){class="glboxshadow gl-90-desktop"}

    曜日ごとに異なる就寝時間を設定したい場合は、**Customize Days** を選択して時刻を設定し、**Next** をクリックします。

    ![bedtime2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/bedtime2.png){class="glboxshadow gl-90-desktop"}

7. コンテンツフィルターを選択します。

    デフォルトでは、**Gambling**、**Malicious Content**、**Sexual Content** の 3 つのカテゴリが選択されています。

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/filter.png){class="glboxshadow gl-90-desktop"}

    必要に応じて、**Games**、**Shopping**、**Social Media**、**Entertainment** などのほかのカテゴリも選択できます。

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/filter.png){class="glboxshadow gl-90-desktop"}

    ブロックしたい特定のアプリが見つけにくい場合は、上部の検索を使うとすばやく見つけられます。

    ![search app](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/search_app.png){class="glboxshadow gl-90-desktop"}

8. 特定のドメインをブロックする必要がある場合は、右下の **Advanced Settings** をクリックします。

    ![block domain1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/block_domain1.png){class="glboxshadow gl-90-desktop"}

    ドメインを手動で入力し、**Finish** をクリックします。

    ![block domain2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/block_domain2.png){class="glboxshadow gl-90-desktop"}

9. これでルールが追加されます。一覧には、ルール名、接続デバイス数、就寝時間スケジュール、フィルタリングされた内容、ルールの状態（有効/無効）が表示されます。

    ![rules added](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/rules_added.png){class="glboxshadow"}

    既存のルールに対しては、Modify、Copy、Delete という基本操作を実行できます。

    ![action](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action.png){class="glboxshadow"}

    - **Modify**: 選択したデバイス、就寝時間、コンテンツフィルタールールを変更します。

        ![action modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action_modify.png){class="glboxshadow"}

    - **Copy**: 既存のルールをコピーして、手動で再設定する手間を省きます。

        ![action copy](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action_copy.png){class="glboxshadow"}

---

ご不明な点がありましたら、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} ください。
