# WANをLANに変更 {#change-wan-to-lan}

ルーターのWANポートをLANポートとして使用できます。これは、WANポートが不要なリピーターモードでルーターを使用する場合に便利です。WANポートをLANポートに変更すると、LANポートが1つ増え、より多くのデバイスを有線で接続できます。

以下の手順に従って、WANをLANに変更してください。

## ファームウェア 4.10 {#for-firmware-410}

1. WANポートは未接続のままにしておきます。

2. デバイスをルーターに接続し、ルーターのWeb管理パネルにアクセスします。

3. Web管理パネルで、**INTERNET** -> **Ethernet 1** セクションに移動し、右上のギアアイコンをクリックします。

	![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_1.png){class="glboxshadow"}

4. **Ethernet Port** ページに移動します。WANポートの下にあるギアアイコンをクリックします。

	![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_2.png){class="glboxshadow"}

5. **LAN** をクリックしてEthernetポートのプロパティを変更し、**Apply** をクリックします。

	![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_3.png){class="glboxshadow"}

6. Ethernet PortページまたはEthernetセクションに戻ると、WANポートがLANポートとして使用されていることが表示されます。

	![ethernet port 4](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_4.png){class="glboxshadow"}

	![ethernet port 5](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_5.png){class="glboxshadow"}

Ethernet PortページでWANに戻すことも、RESETボタンを4秒押してWANインターフェースを再起動することもできます。

## ファームウェア 4.7-4.9 {#for-firmware-47-49}

1. WANポートは未接続のままにしておきます。

2. デバイスをルーターに接続し、ルーターのWeb管理パネルにアクセスします。

3. Web管理パネルで、**INTERNET** -> **Ethernet** セクションに移動し、右上のギアアイコンをクリックします。

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

	**Port Management** ページに移動します。WANポートはWANとして使用中と表示されています。

	![port management](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. **LAN** をクリックしてEthernetポートのプロパティを変更し、**Apply** をクリックします。

	![switch to lan apply](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

	ポップアップの警告ウィンドウで **Apply** をクリックして確定します。
	
	![caution](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

	**注意**: このプロセス中にWi-Fiが一時的に切断される場合があります。完了したら、必ずルーターに再接続してください。

5. Ethernetセクションに戻ると、WANポートがLANポートとして使用されていることが表示されます。

	![wan using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

	**Port Management** ページでWANに戻すことも、RESETボタンを4秒押してWANインターフェースを再起動することもできます。

## ファームウェア 4.6 以前 {#for-firmware-46-and-earlier}

1. WANポートは未接続のままにしておきます。

2. デバイスをルーターに接続し、Web管理パネルにアクセスします。

3. Web管理パネルで **INTERNET** -> **Ethernet** セクションに移動すると、WANポートの状態が **Using as WAN** と表示されます。**Change to LAN** をクリックします。

	![internet page](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. **Apply** をクリックして確定します。

	![caution change wan as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

	**注意**: このプロセス中にWi-Fiが一時的に切断される場合があります。完了したら、必ずルーターに再接続してください。

5. Ethernetセクションに戻ると、`Using as LAN` と表示されます。

	![using as lan](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

	上記の手順を繰り返すだけで設定を元に戻すことができます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
