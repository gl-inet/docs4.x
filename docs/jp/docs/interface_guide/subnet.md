# サブネット

**注記**: このページは現在 Flint 4 (GL-BE14000) で利用できます。ファームウェア v4.10 により、今後ほかのモデルにも展開される予定です。

---

Web Admin Panel の左側で、**NETWORK** -> **Subnet** に移動します。

このページでは、**LAN**、**Guest Network**、**IoT Network**、およびカスタム **VLAN Networks** の設定を 1 つの統合ビューにまとめています。サブネット関連の設定を一元管理でき、複数のサブネットを作成、管理して、異なる種類のデバイスやトラフィックを分離できます。

## メインネットワーク

**Main Network** は、メイン Wi-Fi または Ethernet ケーブルでデバイスが接続されるネットワークです。

Main Network では、すべてのインターフェース状態、VLAN ID、ルーター IP アドレス、DHCP Range を直接確認できます。

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

右下の **Edit** をクリックして Main Network を設定します。

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

設定ページには、Basic settings、DHCP server settings、Address Reservation が含まれます。

### 基本設定

IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` 内でサブネットを設定できます。

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    ルーターの管理ページにアクセスするために、ブラウザーのアドレスバーに入力するアドレスです。

    デフォルトは **192.168.8.1** です。ネットワークと競合する場合は変更できます。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを持つ大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    Main Network のデフォルト VLAN ID は **1** で、変更できません。

- **AP Isolation**

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

### DHCP Server

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスやその他の通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合、クライアントデバイスのネットワーク設定を手動で構成する必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md)をクリックしてください。

ネットワークの拡張や縮小、IP アドレス競合の発生、サブネットマスク範囲の変更などに応じて、開始 IP アドレスと終了 IP アドレスを変更できます。

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

必要に応じて **Advanced** をクリックし、詳細設定を行います。

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: DHCP により割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server**: プライマリリゾルバーとセカンダリリゾルバーを設定するための DNS サーバーフィールドが 2 つあります。

    **注記**: プライマリ DNS は上のフィールドに、セカンダリ DNS は下のフィールドに入力します。プライマリサーバーが利用できない場合、クライアントデバイスは自動的にセカンダリリゾルバーへフェイルオーバーし、ドメイン名解決を継続します。

- **LPR Server** (Line Printer Remote Server): 印刷ジョブを管理し、ネットワークデバイスがリモートプリンターへ印刷要求を送信できるようにするサービスです。複数の LPR プリンターポートを設定できます。

### アドレス予約

LAN 内のクライアントに予約 IP アドレスを指定すると、そのクライアントはルーターの DHCP サーバーにアクセスするたびに同じ IP アドレスを受け取ります。恒久的な IP 設定が必要なコンピューターやサーバーに、予約 IP アドレスを割り当てることができます。

**注記:** 設定済みのクライアントは、有効化するためにルーターへ再接続する必要があります。

IP を予約するには **Add** をクリックします。

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

ポップアップウィンドウが表示されます。

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

ドロップダウンリストから **MAC** を選択します。対応する利用可能な **IP** が自動入力されます。識別しやすくするために、必要に応じて **hostname** とカスタム **name** を入力できます。その後、**Submit** をクリックします。

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

新しい IP アドレス予約を追加すると、以下のページが表示されます。これは設定が正常に完了したことを示します。

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## ゲストネットワーク

**Guest Network** は、訪問者向けの専用 Wi-Fi ネットワークを提供します。プライマリネットワークから分離されるため、セキュリティを高めながら便利なインターネットアクセスを提供できます。

**注記**: 一部のモデル（例: GL-MT5000、GL-MT2500/GL-MT2500A）は Wi-Fi 機能を搭載していないため、Web Admin Panel に Guest Network 設定は表示されません。

Guest Network では、インターフェース状態、VLAN ID、Gateway、DHCP Range を直接確認できます。

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

右下の **Edit** をクリックすると、Guest Network の設定パネルがページ右側に開きます。

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

設定ページには Basic settings と DHCP server settings が含まれます。

### 基本設定

IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` 内でサブネットを設定できます。

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/gest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    Guest Network の**デフォルトゲートウェイ**は **192.168.9.1** です。ローカルネットワークと競合する場合は別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを持つ大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    Guest Network のデフォルト VLAN ID は **9** で、必要に応じて変更できます。

- **AP Isolation**

    この機能はファームウェア v4.5 以降で利用できます。

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

- **WAN Access Control**

    WAN Access Control は、ローカルサブネットから WAN 側ネットワークへのアクセスを管理します。これにはインターネットやほかの WAN サブネットが含まれます。

    WAN アクセス制御には次の 3 つのモードがあります。

    - **Unrestricted**: このサブネットからインターネットおよびほかの WAN 側サブネットへ制限なくアクセスできます。

    - **Block WAN Subnet**: ほかの WAN 側サブネットへのアクセスをブロックします。インターネットアクセスは引き続き利用できます。

    - **Block Internet Access**: インターネットおよび WAN 側サブネットを含む、すべての外向きアクセスをブロックします。

### DHCP Server

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスやその他の通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合、クライアントデバイスのネットワーク設定を手動で構成する必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md)をクリックしてください。

ネットワークの拡張や縮小、IP アドレス競合の発生、サブネットマスク範囲の変更などに応じて、開始 IP アドレスと終了 IP アドレスを変更できます。

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

必要に応じて **Advanced** をクリックし、詳細設定を行います。

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: DHCP により割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server**: プライマリリゾルバーとセカンダリリゾルバーを設定するための DNS サーバーフィールドが 2 つあります。

    **注記**: プライマリ DNS は上のフィールドに、セカンダリ DNS は下のフィールドに入力します。プライマリサーバーが利用できない場合、クライアントデバイスは自動的にセカンダリリゾルバーへフェイルオーバーし、ドメイン名解決を継続します。

- **LPR Server** (Line Printer Remote Server): 印刷ジョブを管理し、ネットワークデバイスがリモートプリンターへ印刷要求を送信できるようにするサービスです。複数の LPR プリンターポートを設定できます。

## IoT Network

IoT Network は、IoT デバイス専用の Wi-Fi ネットワークを作成します。プライマリネットワークから分離されるため、互換性とセキュリティが向上します。

**注記**: 一部のモデル（例: GL-MT5000、GL-MT2500/GL-MT2500A）は Wi-Fi 機能を搭載していないため、Web Admin Panel に IoT Network 設定は表示されません。

IoT Network では、インターフェース状態、VLAN ID、Gateway、DHCP Range を直接確認できます。

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

右下の **Edit** をクリックすると、IoT Network の設定パネルがページ右側に開きます。このパネルでは Basic Settings と DHCP Server Settings を設定できます。

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### 基本設定

IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` 内でサブネットを設定できます。

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    IoT Network の**デフォルトゲートウェイ**は **192.168.10.1** です。ローカルネットワークと競合する場合は別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを持つ大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    IoT Network のデフォルト VLAN ID は **10** で、必要に応じて変更できます。

- **AP Isolation**

    この機能はファームウェア v4.5 以降で利用できます。

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

- **WAN Access Control**

    WAN Access Control は、ローカルサブネットから WAN 側ネットワークへのアクセスを管理します。これにはインターネットやほかの WAN サブネットが含まれます。

    WAN アクセス制御には次の 3 つのモードがあります。

    - **Unrestricted**: このサブネットからインターネットおよびほかの WAN 側サブネットへ制限なくアクセスできます。

    - **Block WAN Subnet**: ほかの WAN 側サブネットへのアクセスをブロックします。インターネットアクセスは引き続き利用できます。

    - **Block Internet Access**: インターネットおよび WAN 側サブネットを含む、すべての外向きアクセスをブロックします。

### DHCP Server

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスやその他の通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合、クライアントデバイスのネットワーク設定を手動で構成する必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md)をクリックしてください。

ネットワークの拡張や縮小、IP アドレス競合の発生、サブネットマスク範囲の変更などに応じて、開始 IP アドレスと終了 IP アドレスを変更できます。

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

必要に応じて **Advanced** をクリックし、詳細設定を行います。

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: DHCP により割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server**: プライマリリゾルバーとセカンダリリゾルバーを設定するための DNS サーバーフィールドが 2 つあります。

    **注記**: プライマリ DNS は上のフィールドに、セカンダリ DNS は下のフィールドに入力します。プライマリサーバーが利用できない場合、クライアントデバイスは自動的にセカンダリリゾルバーへフェイルオーバーし、ドメイン名解決を継続します。

- **LPR Server** (Line Printer Remote Server): 印刷ジョブを管理し、ネットワークデバイスがリモートプリンターへ印刷要求を送信できるようにするサービスです。複数の LPR プリンターポートを設定できます。

## VLAN Networks

メインページの上部で、必要に応じて追加の **VLAN networks** を作成し、異なる種類のデバイスや訪問者トラフィックを分離できます。

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

ページ右側の **+ Add** ボタンをクリックして、新しいネットワークを設定します。

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### 基本設定

このページでは、**VLAN Networks** の基本情報を設定できます。

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    新しく作成するサブネットを識別しやすくするため、名前をカスタマイズします。

- **Gateway**

    新しいサブネットのゲートウェイを手動で設定します。このゲートウェイが既存の LAN セグメントと競合する場合は変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを持つ大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    サブネットを作成する際は、**9** から **4000** の間で VLAN ID を割り当てる必要があります。ネットワーク競合を防ぐため、すでに使用されている VLAN ID は避けてください。

- **AP Isolation**

    この機能はファームウェア v4.5 以降で利用できます。

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

- **WAN Access Control**

    WAN Access Control は、ローカルサブネットから WAN 側ネットワークへのアクセスを管理します。これにはインターネットやほかの WAN サブネットが含まれます。

    WAN アクセス制御には次の 3 つのモードがあります。

    - **Unrestricted**: このサブネットからインターネットおよびほかの WAN 側サブネットへ制限なくアクセスできます。

    - **Block WAN Subnet**: ほかの WAN 側サブネットへのアクセスをブロックします。インターネットアクセスは引き続き利用できます。

    - **Block Internet Access**: インターネットおよび WAN 側サブネットを含む、すべての外向きアクセスをブロックします。

### DHCP Server

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスやその他の通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合、クライアントデバイスのネットワーク設定を手動で構成する必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md)をクリックしてください。

ネットワークの拡張や縮小、IP アドレス競合の発生、サブネットマスク範囲の変更などに応じて、開始 IP アドレスと終了 IP アドレスを変更できます。

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

必要に応じて **Advanced** をクリックし、詳細設定を行います。

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: DHCP により割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server**: プライマリリゾルバーとセカンダリリゾルバーを設定するための DNS サーバーフィールドが 2 つあります。

    **注記**: プライマリ DNS は上のフィールドに、セカンダリ DNS は下のフィールドに入力します。プライマリサーバーが利用できない場合、クライアントデバイスは自動的にセカンダリリゾルバーへフェイルオーバーし、ドメイン名解決を継続します。

- **LPR Server** (Line Printer Remote Server): 印刷ジョブを管理し、ネットワークデバイスがリモートプリンターへ印刷要求を送信できるようにするサービスです。複数の LPR プリンターポートを設定できます。

設定が完了すると、新しい VLAN ネットワークが現在のページに表示され、サブネット情報を確認できます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}にアクセスするか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。

