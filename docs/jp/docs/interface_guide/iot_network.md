# IoT Network

Web Admin Panel の左側で、**NETWORK** -> **IoT Network** に移動します。

このページでは、IoT デバイス専用の Wi-Fi ネットワークを作成できます。メインネットワークから分離されるため、互換性とセキュリティの向上に役立ちます。

**Note**: 一部のモデル（例: GL-MT5000、GL-MT2500/GL-MT2500A）は Wi-Fi 機能を備えていないため、Web Admin Panel に IoT Network の設定は表示されません。

基本設定と DHCP サーバー設定の 2 つのセクションがあります。

## 基本設定

IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` の中でサブネットを設定できます。

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot1.png){class="glboxshadow"}

- **Gateway**

    IoT Network の **default gateway** は **192.168.10.1** です。ローカルネットワークと競合する場合は別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスが必要な大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **AP Isolation**

    この機能はファームウェア v4.5 から利用できます。

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

- **Block WAN Subnets**

    この機能はファームウェア v4.8 から利用できます。

    有効にすると、IoT Network から上位ネットワークおよびそのサブネットへアクセスできなくなります。

## DHCPサーバー

IoT Network を有効にすると、それに応じて DHCP サーバーも有効になります。

DHCP サーバーは IoT Network に接続した各クライアントデバイスに、IP アドレスやそのほかの通信パラメーターを自動的に割り当てます。DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot2.png){class="glboxshadow"}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![iot network 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot3.png){class="glboxshadow"}

![iot network 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/iot_network/iot4.png){class="glboxshadow"}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: IoT ネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**: （Line Printer Remote Server）印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
