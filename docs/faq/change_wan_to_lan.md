# WANをLANに変更

ルーターのWANポートをLANポートとして使用できます。これは、WANポートが不要なリピーターモードでルーターを使用する場合に便利です。WANポートをLANポートに変更すると、追加のLANポート用に拡張接続できます。

以下の手順に従って、WANをLANに変更してください。

## ファームウェア4.7で上

1. WANポートは未接続のままにしておきます。

2. デバイスをルーターに接続し、ルーターのウェブ管理パネルにアクセスします。

3. ウェブ管理パネルで、**インターネット** → **イーサネット**セクションに移動し、右上のギアアイコンをクリックします。

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

	**ポート管理**ページにリダイレクトされ、WANポートの状態がWANに使用中として表示されます。

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. **LAN**をクリックしてイーサネットポートのプロパティを変更し、**適用**をクリックします。

	![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

	ポップアップの警告ウィンドウで、**適用**をクリックして確認します。
	
	![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

	**注意**: このプロセス中にWi-Fiが一時的に切断される場合があります。完了したら、必ずルーターに再接続してください。

5. イーサネットセクションに戻ると、WANポートがLANポートとして使用されていることが表示されます。

	![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

	**ポート管理**ページで元WANに戻したり、リセットボタンを4秒押してWANインターフェースを再起動したりできます。

## ファームウェア4.6で前

1. WANポートは未接続のままにしておきます。

2. デバイスをルーターに接続し、ウェブ管理パネルにアクセスします。

3. ウェブ管理パネルで、**インターネット** → **イーサネット**セクションに移動すると、WANポートの状態が**WANとして使用中**と表示されます。**LANに変更**をクリックします。

	![internet page](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. **適用**をクリックして確定します。

	![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

	**注意**: このプロセス中にWi-Fiが一時的に切断される場合があります。完了したら、必ずルーターに再接続してください。

5. イーサネットセクションに戻ると、`LANとして使用中`と表示されます。

	![using as lan](https://static.gl-inet.com/docs/router/en/4/tutorials/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

	上記の手順を繰り返すだけで設定を元に戻すことができます。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
