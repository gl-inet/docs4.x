# ゲストネットワーク

ゲストネットワーク設定はファームウェアv4.5で降、[LAN](lan.md)から分離されました。

ウェブ管理パネルの左側 -> ネットワーク -> ゲストネットワーク。

ゲストネットワークの基本設定とDHCPサーバー設定が含まれています。

## 基本設定

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

一時のなユーザーのために設計された分離された隔離ネットワークを設定でき、プライマリネットワークから分離することで限定のなアクセスと強化されたセキュリティを提供します。

**注意**: 一部のモデルにはWi-Fiがないため（例：GL-MT2500/GL-MT2500A）、ゲストネットワークタブはありません。

**デフォルトゲートウェイ**は**192.168.9.1**です。ゲストWi-Fiを有効にしていて、ネットワークと競合する場合は、変更できます。

セキュリティ設定：

- AP分離

    ネットワークのクライアントデバイスを別のネットワーク領域に分離できます。これらのデバイスはネットワーク上の彼のデバイスと通信できません。

- WANサブネットをブロック

    この機能はv4.8で利用可能です。

    この機能を有効にすると、ゲストネットワークは上位ネットワークと上位ネットワークがあるネットワークセグメントにアクセスできなくなります。

その彼の基本設定とDHCPサーバー設定は[LAN](lan.md)と同じです。

## DHCPサーバー設定

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

---

関連記事：

- [GL.iNetルーターでゲストWi-Fiネットワークを設定する方法](../tutorials/how_to_set_up_a_guest_network.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
