# ゲストネットワーク

Guest Network の設定は、ファームウェア v4.5 以降 [LAN](lan.md) から分離されました。

Web Admin Panel の左側で、**NETWORK** -> **Guest Network** に移動します。

このページには Guest Network の基本設定と DHCP サーバー設定が含まれます。

## 基本設定

IPv4 プライベートアドレス範囲 `192.168.0.0/16`、`172.16.0.0/12`、`10.0.0.0/8` の中でサブネットを設定できます。

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

一時的な利用者向けに、メインネットワークから分離された独立ネットワークを設定できます。これにより、アクセスを制限しつつセキュリティを高められます。

**Note**: 一部のモデル（例: GL-MT5000、GL-MT2500/GL-MT2500A）は Wi-Fi をサポートしていないため、Web Admin Panel に Guest Network の設定は表示されません。

- **Gateway**

    Guest Network の **default gateway** は **192.168.9.1** です。ローカルネットワークと競合する場合は別のアドレスに変更してください。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスが必要な大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **AP Isolation**

    この機能はファームウェア v4.5 から利用できます。

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

- **Block WAN Subnets**

    この機能はファームウェア v4.8 から利用できます。

    有効にすると、Guest Network から上位ネットワークおよびそのサブネットへアクセスできなくなります。

## DHCPサーバー

Guest Network を有効にすると、DHCP Server もデフォルトで有効になります。

DHCP サーバーは Guest Network に接続した各クライアントデバイスに、IP アドレスやそのほかの通信パラメーターを自動的に割り当てます。DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ゲストネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**: （Line Printer Remote Server）印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

---

Related Articles:

- [How to set up a guest Wi-Fi network on GL.iNet routers](../tutorials/how_to_set_up_a_guest_network.md)

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
