# LAN {#lan}

**注意**: このページの内容は、ファームウェア v4.11 以降を対象としています。異なるバージョンを使用している場合は、以下のセレクターで対応するガイドに切り替えてください。

<div class="gl-link-select" data-label="ファームウェアバージョン" data-placeholder="ファームウェア v4.11 以降" markdown="1">

- [ファームウェア v4.9 以前](lan.md)

</div>

---

Web 管理パネルの左側で、**NETWORK** -> **LAN** に移動します。

このページでは、メインネットワーク（**Main Network**）、ゲストネットワーク（**Guest Network**）、IoT ネットワーク（**IoT Network**）、カスタム VLAN ネットワーク（**VLAN Networks**）をまとめて設定・管理できます。複数のサブネットを作成・管理し、種類の異なるデバイスやトラフィックを分離できます。

## メインネットワーク {#main-network}

メインネットワーク（**Main Network**）は、デバイスがメイン Wi-Fi または Ethernet ケーブルで接続するときに利用するネットワークです。

メインネットワークでは、すべてのインターフェースの状態、VLAN ID、ルーターの IP アドレス、DHCP の割り当て範囲を確認できます。

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

右下の **Edit** をクリックして、メインネットワークを設定します。

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

設定ページには、基本設定、DHCP サーバー設定、アドレス予約が含まれます。

### 基本設定 {#basic-settings}

サブネットは、IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` の中で設定できます。

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    ルーターの Web 管理パネルにアクセスする際に、ブラウザーのアドレスバーへ入力するアドレスです。

    デフォルトは **192.168.8.1** です。ネットワークと競合する場合は変更できます。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを使用できる大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    メインネットワークのデフォルトの VLAN ID は **1** で、変更できません。

- **AP Isolation**

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは、同じネットワーク上のほかのデバイスと通信できなくなります。

    **注意:** AP Isolation は Wi-Fi クライアントのみに適用され、有線デバイスには適用されません。

### DHCPサーバー {#dhcp-server}

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスとそのほかの通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![main network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**（Line Printer Remote Server）: 印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

### アドレス予約 {#address-reservation}

LAN 内のクライアントに予約 IP アドレスを指定すると、そのクライアントはルーターの DHCP サーバーにアクセスするたびに常に同じ IP アドレスを受け取ります。固定 IP 設定が必要なコンピューターやサーバーに予約 IP アドレスを割り当てられます。

**注意:** 設定を有効にするには、対象のクライアントをルーターに再接続する必要があります。

**Add** をクリックして IP アドレスを予約します。

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

ポップアップウィンドウが表示されます。

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

ドロップダウンリストから **MAC** を選択すると、対応する利用可能な **IP** が自動入力されます。識別しやすくするために、必要に応じて **hostname** と任意の **name** を入力できます。その後、**Submit** をクリックします。

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

新しい IP アドレス予約を追加すると、以下の画面が表示され、設定が正常に完了したことを示します。

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## ゲストネットワーク {#guest-network}

ゲストネットワーク（**Guest Network**）は、訪問者向けの専用 Wi-Fi ネットワークです。メインネットワークから分離することで、手軽にインターネットへアクセスできるようにしながら、セキュリティを高めます。

**注意**: 一部のモデル（GL-MT5000、GL-MT2500/GL-MT2500A など）は Wi-Fi 機能を搭載していないため、Web 管理パネルにゲストネットワークの設定は表示されません。

ゲストネットワークでは、インターフェースの状態、VLAN ID、ゲートウェイ、DHCP の割り当て範囲を確認できます。

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

右下の **Edit** をクリックすると、ページの右側にゲストネットワークの設定パネルが開きます。

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

設定ページには、基本設定と DHCP サーバー設定が含まれます。

### 基本設定 {#basic-settings_1}

サブネットは、IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` の中で設定できます。

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    ゲストネットワークの**デフォルトゲートウェイ**は **192.168.9.1** です。ローカルネットワークと競合する場合は、別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを使用できる大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    ゲストネットワークのデフォルトの VLAN ID は **9** で、必要に応じて変更できます。

- **Associated LAN Ports**

    このサブネットに割り当てる LAN ポートを選択します。これらのポートに接続された有線デバイスは、このネットワークに参加します。

- **AP Isolation**

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは、同じネットワーク上のほかのデバイスと通信できなくなります。

    **注意:** AP Isolation は Wi-Fi クライアントのみに適用され、有線デバイスには適用されません。

- **WAN Access Control**

    WAN Access Control は、ローカルサブネットから、インターネットや WAN 側のほかのサブネットを含む WAN 側ネットワークへのアクセスを管理します。

    WAN アクセス制御には、次の 3 つのモードがあります。

    - **Unrestricted**: このサブネットから、インターネットおよび WAN 側のほかのサブネットへのアクセスを制限なく許可します。

    - **Block WAN Subnet**: WAN 側のほかのサブネットへのアクセスをブロックします。インターネットには引き続きアクセスできます。

    - **Block Internet Access**: インターネットや WAN 側のサブネットを含む、すべての外向きのアクセスをブロックします。

### DHCPサーバー {#dhcp-server_1}

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスとそのほかの通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![guest network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**（Line Printer Remote Server）: 印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

## IoT ネットワーク {#iot-network}

IoT ネットワークは、IoT デバイス向けの専用 Wi-Fi ネットワークを提供します。メインネットワークから分離することで、互換性とセキュリティを高めます。

**注意**: 一部のモデル（GL-MT5000、GL-MT2500/GL-MT2500A など）は Wi-Fi 機能を搭載していないため、Web 管理パネルに IoT ネットワークの設定は表示されません。

IoT ネットワークでは、インターフェースの状態、VLAN ID、ゲートウェイ、DHCP の割り当て範囲を確認できます。

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

右下の **Edit** をクリックすると、ページの右側に IoT ネットワークの設定パネルが開きます。このパネルで、基本設定と DHCP サーバー設定を行えます。

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### 基本設定 {#basic-settings_2}

サブネットは、IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` の中で設定できます。

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    IoT ネットワークの**デフォルトゲートウェイ**は **192.168.10.1** です。ローカルネットワークと競合する場合は、別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを使用できる大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    IoT ネットワークのデフォルトの VLAN ID は **10** で、必要に応じて変更できます。

- **Associated LAN Ports**

    このサブネットに割り当てる LAN ポートを選択します。これらのポートに接続された有線デバイスは、このネットワークに参加します。

- **AP Isolation**

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは、同じネットワーク上のほかのデバイスと通信できなくなります。

    **注意:** AP Isolation は Wi-Fi クライアントのみに適用され、有線デバイスには適用されません。

- **WAN Access Control**

    WAN Access Control は、ローカルサブネットから、インターネットや WAN 側のほかのサブネットを含む WAN 側ネットワークへのアクセスを管理します。

    WAN アクセス制御には、次の 3 つのモードがあります。

    - **Unrestricted**: このサブネットから、インターネットおよび WAN 側のほかのサブネットへのアクセスを制限なく許可します。

    - **Block WAN Subnet**: WAN 側のほかのサブネットへのアクセスをブロックします。インターネットには引き続きアクセスできます。

    - **Block Internet Access**: インターネットや WAN 側のサブネットを含む、すべての外向きのアクセスをブロックします。

### DHCPサーバー {#dhcp-server_2}

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスとそのほかの通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![iot network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**（Line Printer Remote Server）: 印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

## VLAN ネットワーク {#vlan-networks}

メインページの上部で、必要に応じて **VLAN ネットワーク**を追加し、種類の異なるデバイスや訪問者のトラフィックを分離できます。

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

ページ右側の **+ Add** ボタンをクリックして、新しいネットワークを設定します。

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### 基本設定 {#basic-settings_3}

このページで、VLAN ネットワーク（**VLAN Networks**）の基本情報を設定できます。

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    新しく作成するサブネットを識別するための名前を設定します。

- **Gateway**

    新しいサブネットのゲートウェイを手動で設定します。既存の LAN セグメントと競合する場合は、別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスを使用できる大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **VLAN ID**

    サブネットを作成するときは、**9** から **4000** までの VLAN ID を割り当てる必要があります。ネットワークの競合を防ぐため、すでに使用されている VLAN ID は指定しないでください。

- **Associated LAN Ports**

    このサブネットに割り当てる LAN ポートを選択します。これらのポートに接続された有線デバイスは、このネットワークに参加します。

- **AP Isolation**

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは、同じネットワーク上のほかのデバイスと通信できなくなります。

    **注意:** AP Isolation は Wi-Fi クライアントのみに適用され、有線デバイスには適用されません。

- **WAN Access Control**

    WAN Access Control は、ローカルサブネットから、インターネットや WAN 側のほかのサブネットを含む WAN 側ネットワークへのアクセスを管理します。

    WAN アクセス制御には、次の 3 つのモードがあります。

    - **Unrestricted**: このサブネットから、インターネットおよび WAN 側のほかのサブネットへのアクセスを制限なく許可します。

    - **Block WAN Subnet**: WAN 側のほかのサブネットへのアクセスをブロックします。インターネットには引き続きアクセスできます。

    - **Block Internet Access**: インターネットや WAN 側のサブネットを含む、すべての外向きのアクセスをブロックします。

### DHCPサーバー {#dhcp-server_3}

**DHCP Server** はデフォルトで有効です。DHCP サーバーは、各クライアントデバイスに IP アドレスとそのほかの通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![vlan networks dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**（Line Printer Remote Server）: 印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

設定が完了すると、現在のページに新しい VLAN ネットワークが表示され、サブネット情報を確認できます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
