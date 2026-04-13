# クライアント

Web 管理パネルの左側で、**CLIENTS** に移動します。

Clients ページには、接続されているデバイスのデバイス名、接続タイプ、IP アドレス、MAC アドレス、速度、トラフィックが左から右の順に表示されます。

## デバイス名

1列目には、デバイス名とデバイスタイプが表示されます。これはデバイスの使用者が設定したホスト名によって異なります。

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

デバイス名とタイプを変更するには、Action 列の三点アイコンをクリックし、ドロップダウンメニューで **Modify** をクリックします。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## 接続タイプ

デバイス名の右側にある青いアイコンは、そのデバイスの接続タイプ/接続方法を表します。

Wi-Fi またはイーサネットケーブルのどちらでネットワークに接続されているかを示します。

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IP アドレスと MAC アドレス

2列目には、接続されているデバイスの IP アドレスと MAC アドレスが表示されます。

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

多くのデバイスはランダム化された MAC アドレスを使用します。接続中のデバイスがランダム化 MAC アドレスを使用している場合は、次のプロンプトが表示されます。

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**注意**: ここでの判定ルールは、MAC アドレスの2文字目が 2、6、A、E のいずれか（大文字小文字を区別しない）であれば、ランダム化 MAC アドレスとみなすというものです。ただし、一部デバイスでは別のルールでランダム化 MAC アドレスを生成するため、この検出方法が正確でない場合があります。

## 速度

3列目には、接続されているデバイスのインターネット速度が表示されます。

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

ここで表示される速度は、3分間の平均速度です。

- 現在のページを 10 秒間開くと、直近 10 秒間の平均速度が表示されます。
- 現在のページを 30 秒間開くと、直近 30 秒間の平均速度が表示されます。
- 現在のページを 60 秒間開くと、直近 60 秒間の平均速度が表示されます。
- 現在のページを 3 分間開くと、直近 3 分間の平均速度が表示されます。
- 現在のページを 10 分間開いても、直近 3 分間の平均速度が表示されます。

## トラフィック

4列目には、接続されているデバイスのインターネットトラフィックが表示されます。

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## IP予約

5列目では、ワンクリックで特定の接続済みデバイスに IP アドレスを予約できます。

この機能は v4.8 以降で利用できます。

LAN 内のクライアントに予約 IP アドレスを指定すると、そのクライアントはルーターの DHCP サーバーにアクセスするたびに、常に同じ IP アドレスを受け取ります。

固定 IP 設定が必要なコンピューターやサーバーに、予約 IP アドレスを割り当てることができます。

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Blocklist {#blocklist}

6列目では、ワンクリックで特定の接続済みデバイスをブロックできます。

アクセス制御ルールはデフォルトで Blocklist に設定されており、必要に応じて上部から Allowlist に切り替えられます。

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Blocklist に登録された MAC アドレスを持つデバイスは、このルーターへ接続できません。

- **Allowlist**: 指定した MAC アドレスを持つデバイスだけが接続を許可されます。IoT デバイスや企業ネットワークの管理に適しています。

Blocklist を作成するには、**(1)** で Excel 形式のブロックリストをアップロードするか、**(2)** で MAC アドレスを手動入力します。

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**方法1. Import Clients**

Access Control ページで、**Import Clients** をクリックします。

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

**Download Import Template** をクリックすると、"mac-template.csv" という名前の XLS ワークシートがダウンロードされます。

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

ファイルを開き、MAC アドレスを入力して保存します。

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

保存したファイルを選択するか、アップロードエリアへドラッグします。

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow gl-80-desktop"}

アップロードに成功したら、**Import** をクリックして MAC アドレスの一括インポートを完了します。

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**方法2. 手動入力**

Access Control ページで、ブロックしたいデバイスの MAC アドレスを手動入力し、**Apply** をクリックします。

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**注意**: クライアントのブロックはデバイスの MAC アドレスに基づきます。ブロックされたデバイスが次回別の MAC アドレスを使用した場合、再びルーターへ接続できる可能性があります。

## Sort

現在の並べ替えタイプは右上に表示され、他の並べ替えタイプへ切り替えることもできます。

デフォルトの並べ替えルールは次のとおりです。

- 自分のデバイスは常に最上部に表示されます。
- オンラインクライアントセクションでは、後から接続されたデバイスほど上に表示されます。

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Action

### クライアント詳細

クライアントデバイスの詳細を表示したい場合は、右端の Action 列にある三点アイコンをクリックし、ドロップダウンメニューで **View Details** をクリックします。

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

開いたサブページでは、該当する場合はすべての IPv6 アドレスを含め、クライアントデバイスのすべての情報を確認できます。

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modify

Action 列の三点アイコンをクリックし、ドロップダウンメニューで **Modify** をクリックします。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### 速度制限

Action 列の三点アイコンをクリックし、ドロップダウンメニューで **Limit Speed** をクリックします。

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

速度制限が適用されているクライアントでは、速度表示の上矢印と下矢印が黄色になります。

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

速度制限を無効にするには、Action 列の三点アイコンをクリックします。

### VPNトンネルを使用

**注意**: このオプションはファームウェア v4.8 以降で利用でき、MAC ベースのポリシーが設定されている場合にのみ Action メニューへ表示されます。

MAC ベースのポリシーを使用してクライアントを VPN トンネルリストに追加します。トンネルの詳細設定を行う場合は、VPN ダッシュボードに移動して管理してください。

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## オフラインクライアントの削除

オフラインクライアントセクションでは、右上の **Delete All** をクリックすると、すべてのオフラインクライアントを削除できます。

特定のクライアントだけを削除したい場合は、Action 列の三点アイコンをクリックし、ドロップダウンメニューで **Remove Client** をクリックします。

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
