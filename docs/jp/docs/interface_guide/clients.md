# クライアント

Web 管理パネルの左側 -> クライアント

クライアントページには、デバイス名、接続タイプ、IPアドレス、MACアドレス、速度、トラフィックなど、接続されているデバイスに関する情報が表示されます（左から右に設定）。

## デバイス名

最も初の列には、デバイス名とデバイスタイプが表示されます。これはデバイスのホスト名によって異なります。

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

デバイス名とタイプを変更するには、アクション列の三時アイコンをクリックし、プルダウンメニューで**変更**をクリックします。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## 接続タイプ

デバイス名の右側にある青いアイコンは、デバイスの接続タイプ/接続方法を表しています。

デバイスがWi-Fiか有線LANでネットワークに接続されているかを示します。

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IPとMACアドレス

2番目の列には、接続されているデバイスのIPアドレスとMACアドレスが表示されます。

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

多くのデバイスはランダム化されたMACアドレスを使用します。接続されたデバイスがランダム化されたMACアドレスを使用している場合、以下のプロンプトが表示されます。

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**注意**: ここでのルールは、MACアドレスの2番目の文字が2、6、A、またはE（大文字と小文字を区別しない）の場合、ランダム化されたMACアドレスとみなされます。ただし、デバイスによっては異なるルールを使用してランダム化されたMACアドレスを生成する場合があるため、この検出方法は正確ではない可能性があります。

## 速度

3番目の列には、接続されているデバイスのインターネット速度が表示されます。

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

ここでの速度は3分間の平均速度です。

- 現にのページを10秒間開くと、過去10秒間の平均速度が表示されます。
- 現にのページを30秒間開くと、過去30秒間の平均速度が表示されます。
- 現にのページを60秒間開くと、過去60秒間の平均速度が表示されます。
- 現にのページを3分間開くと、過去3分間の平均レートが表示されます。
- 現にのページを10分間開くと、過去3分間の平均レートが表示されます。

## トラフィック

4番目の列には、接続されているデバイスのインターネットトラフィックが表示されます。

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## 予約IP

5番目の列では、クリックだけで特定の接続済みデバイスのIPアドレスを予約できます。

この機能はv4.8で降で利用可能です。

LAN内のクライアントに予約IPアドレスを指定すると、そのクライアントはルーターのDHCPサーバーにアクセスするたびに同じIPアドレスを受け取るようになります。

永続のなIP設定が必要なコンピュータやサーバーに予約IPアドレスを割り当てることができます。

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## ブロックリスト

6番目の列では、クリックだけで特定の接続済みデバイスをブロックできます。

アクセス制御ルールはデフォルトでブロックリストとなっており、必要に応じて上部でホワイトリストに切り替えできます。

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **ブロックリスト**: ブロックリストにあるMACアドレスを持つデバイスは、このルーターへの接続が許可されません。

- **ホワイトリスト**: 特定のMACアドレスを持つデバイスのみが接続を許可され、IoTデバイスや企業ネットワーク管理に適しています。

ブロックリストを作成するには、**(1)** でExcel形式のブロックリストをアップロードするか、**(2)** でMACアドレスを手動で入力できます。

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**方法1. クライアントをインポート**

アクセス制御ページで、**クライアントをインポート**をクリックします。

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

**インポートテンプレートをダウンロード**をクリックし、"mac-template.csv"という名前のXLSワークシートをダウンロードします。

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

ファイルを開き、MACアドレスをインポートして保存します。

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

保存したファイルを選択するか、ドラッグしてアップロード領域にドロップします。

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow gl-80-desktop"}

アップロードが成功したら、**インポート**をクリックしてMACアドレスの一括インポートを完たします。

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**方法2. 手動入力**

アクセス制御ページで、ブロックしたいデバイスのMACアドレスを手動で入力し、**適用**をクリックします。

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**注意**: クライアントのブロックはデバイスのMACアドレスに基づいています。ブロックされたデバイスが次回異なるMACアドレスを使用した場合でも、ルーターに接続できる可能性があります。

## 並べ替え

現にの並べ替えタイプは右上に表示され、彼の並べ替えタイプに切り替えできます。

デフォルトの並べ替えタイプは次の通りです：

- から分のデバイスは常に一番上に表示されます。
- オンラインクライアントセクションでは、デバイスが後から接続なるほど、リストの上位に 設定されます。

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## アクション

### クライアントの詳細

クライアントデバイスの詳細を表示する必要がある場合は、最もも右にあるアクション列の三時アイコンをクリックし、プルダウンメニューで**詳細を表示**をクリックします。

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

開いたサブページでクライアントデバイスのすべての情報（該当する場合はデバイスのすべてのIPv6アドレスを含む）を確認できます。

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### 変更

アクション列の三時アイコンをクリックし、プルダウンメニューで**変更**をクリックします。

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### 速度制限

アクション列の三時アイコンをクリックし、プルダウンメニューで**速度制限**をクリックします。

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

速度制限が適用されているクライアントの場合、速度の上矢印と下矢印が黄色に変わります。

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

アクション列の三時アイコンをクリックして速度制限を無効にします。

### VPNトンネルの使用

**注意**: このオプションはファームウェアv4.8で降で利用可能で、MACベースのポリシーが設定されている場合にのみアクションメニューに表示されます。

MACベースのポリシーでクライアントをVPNトンネルリストに追加します。トンネルの詳細を調全体する必要がある場合は、管理のためにVPNダッシュボードに移動してください。

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## オフラインクライアントの削除

オフラインクライアントセクションで、右上の**すべて削除**をクリックしてすべてのオフラインクライアントを削除できます。

特定のクライアントを削除したい場合は、アクション列の三時アイコンをクリックし、プルダウンメニューで**クライアントを削除**をクリックします。

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
