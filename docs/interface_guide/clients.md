# クライアント

Web 管理パネルの左側 -> クライアント

クライアントページには、デバイス名、接続タイプ、IP アドレス、MAC アドレス、速度、トラフィックなど、接続されているデバイスに関する情報が表示されます。

## クライアント名とタイプの変更

デバイスの名前とタイプを変更したい場合、「アクション」の下のアイコンをクリックし、ポップアップするメニューで、**変更**アイテムをクリックしてください。

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_three_dots.png){class="glboxshadow"}

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/edit_client_device.png){class="glboxshadow"}

## MACアドレス

多くのデバイスはランダム化されたMACアドレスを使用します。ランダム化されたMACアドレスが使用されている場合、プロンプトが表示されます。

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac_address.png){class="glboxshadow"}

**注意**: ここでのルールは、MACアドレスの2番目の文字が2、6、A、またはE（大文字と小文字を無視）であれば、ランダム化されたMACアドレスとみなすというものであります。ただし、デバイスによっては、異なるルールを使用してランダム化されたMACアドレスを生成する場合があるため、正確でない可能性があります。

## ブロックリスト

**ブロック**を有効にすると、クライアントデバイスをブロックし、ブロックされたデバイスはLANインターフェイスとWANインターフェイスにアクセスできなくなります。

![clients page](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients.png){class="glboxshadow"}


ブラックリスト: 禁止リストの MAC アドレスを持つデバイスは、このルーターに接続できません。

ホワイトリスト: 特定のMACアドレスを持つデバイスのみが接続を許可されるため、IoTデバイスや企業のネットワーク管理に適している。


![clients page](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_whitelist.png){class="glboxshadow"}


ファームウェア 4.4.x 以降、ブロック リストを Excel 形式でアップロードするか、Mac アドレスを手動で入力して **ブロック リスト** を作成できます。

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

**(1)** で CSV ファイルからリストをインポートするか、**(2)** で Mac アドレスを 1 つずつ入力することができます。

![inputblock](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/inputblock.jpg){class="glboxshadow gl-80-desktop"}

![importcsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

![dragcsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow gl-80-desktop"}

![loadcsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/loadcsv.jpg){class="glboxshadow"}

![applycsv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/applycsv.jpg){class="glboxshadow"}

**注意**: クライアントのブロックは、デバイスのMACアドレスに基づいているため、ブロックされたデバイスが次回別のMACアドレスを使用しても、ルータに接続することができます。

## スピード

![clients page](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_speed.png){class="glboxshadow"}

ここでのスピードは3分間の平均スピードで表示さ れます。

- 現在のページを10秒間開くと、過去10秒間の平均スピードが表示されます。
- 現在のページを30秒間開くと、過去30秒間の平均スピードが表示されます。
- 現在のページを60秒間開くと、過去60秒間の平均スピードが表示されます。
- 現在のページを3分間開くと、過去3分間の平均レートが表示されます。
- 現在のページを10分間開くと、過去10分間の平均レートが表示されます。

## ソート

現在のソート順序のタイプは右上に表示され、他のソート順序のタイプに切り替えることもできます。

デフォルトのソート順序のタイプ：

- 自分のデバイスが常に一番上に表示されます。
- オンライン クライアント セクターでは、デバイスの接続が遅くなるほど、上位に表示されます。

![clients page](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_sort.png){class="glboxshadow"}

## スピードの制限

デバイスの速度を制限したい場合は、アクション 下のアイコンをクリックし、ポップアップするメニューで、**スピード制限**項目をクリックしてください。

![clients page, three dots](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_three_dots.png){class="glboxshadow"}

![clients page](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

クライアントが速度制限を適用している場合、速度の上矢印と下矢印が黄色に変わります。

![clients page](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed.png){class="glboxshadow"}

制限を無効にするには、**アクション**をクリックします。

## オフラインクライアントの削除

オフラインクライアントセクターでは、オフラインクライアントを**すべて削除**することができます。特定のクライアントを削除したい場合は、アクション 下のアイコンをクリックし、ポップアップするメニューで、**クライアントを削除**項目をクリックしてください。

![remove clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_client.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
