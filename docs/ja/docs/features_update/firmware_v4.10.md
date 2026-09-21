# ファームウェア v4.10

このリリースでは、Mesh、GL.iNetアカウント、ネイティブVLAN対応が導入されました。また、GoodCloudアカウント管理が改善され、全体的な操作性を高める、より使いやすいインターフェースが提供されます。

最新のファームウェアは[ファームウェアダウンロードセンター](https://dl.gl-inet.com/){target="_blank"}から入手できます。

## Mesh

[Mesh](../interface_guide/mesh.md)は、Wi-Fi EasyMesh™規格に基づき、家全体のWi-Fiカバレッジを拡張してシームレスローミングを実現する機能です。複数のGL.iNetルーターがある場合は、1台をメインルーター、残りをメッシュノードに設定すると、家の中を移動してもWi-Fiをシームレスに利用できます。

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/mesh.png){class="glboxshadow"}

## クラウドサービス

クラウドサービスは、ルーターに組み込まれ、GL.iNetアカウントから一元管理されるクラウド機能群です。リアルタイムの状態監視、デバイスのリモート管理、ファームウェアの一括展開、安全なリモートアクセスが可能です。ファームウェアv4.10では、統合クラウド管理機能が強化されています。

クラウドサービスモジュールには、GL.iNetアカウント、GoodCloud、GoodPASが含まれます。

### GL.iNetアカウント

[GL.iNetアカウント](../interface_guide/glinet_account.md)には、デバイスの接続や管理、クラウドサービスへのアクセスを行うための一元化されたプロフィールページがあります。1つのGL.iNetアカウントでGoodCloud、GoodPAS、GL.iNetアプリをシームレスに利用でき、ネットワークをより簡単に管理できます。

![gl.inet account](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/account.png){class="glboxshadow"}

### GoodCloud

[GoodCloud](../interface_guide/cloud.md)は、GL.iNetルーターをリモートで展開・管理するためのクラウドプラットフォームです。複数拠点のデバイスを一元管理し、設定やファームウェア更新を一括で行えます。また、Web管理画面へのリモートアクセスや、SSHによるデバイス端末へのアクセスにも対応しています。

ファームウェアv4.10では、GoodCloudのアカウント連携が簡素化され、工場出荷時設定へのリセット時にクラウドアカウントデータを消去できるようになりました。

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/goodcloud.png){class="glboxshadow"}

### GoodPAS

[GoodPAS](../interface_guide/goodpas.md)は、GL.iNetルーターSDKに統合された高度なリモートアクセスソリューションです。AmneziaWGプロトコルを基盤とし、アカウント登録やユーザーログインを必要とせず、簡単なデバイスペアリングでホームネットワークへ安全にアクセスできます。

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/goodpas.png){class="glboxshadow"}

## サブネット

[サブネット](../interface_guide/subnet.md)ページでは、LAN、ゲストネットワーク、IoTネットワーク、カスタムVLANネットワークの設定を1つの画面にまとめています。サブネット関連の設定を一元管理でき、複数のサブネットを作成・管理して、種類の異なるデバイスやトラフィックを分離できます。

次の図は、Flint 3（GL-BE9300）のサブネット画面です。

![subnet](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/subnet.png){class="glboxshadow"}

## Ethernet Port

[Ethernet Port](../interface_guide/ethernet_port_v4.10.md)ページには、ルーターのすべてのEthernetインターフェースが表示されます。接続状態の確認、WANとLAN間でのポートの役割の切り替え、MACアドレス、ネゴシエート速度、リンク状態などの詳細確認が可能です。作成したサブネットに物理インターフェースを割り当てることもできます。

次の図は、Flint 3（GL-BE9300）のEthernet Port画面です。

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/ehternet_port.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
