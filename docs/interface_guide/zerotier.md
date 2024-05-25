# ZeroTier

ZeroTier機能はV4.2以降で利用可能

ZeroTierは、インターネット上のデバイス間で安全な暗号化通信を可能にするソフトウェアベースの仮想プライベートネットワーク（VPN）です。これにより、デバイスは物理的な場所やネットワークトポロジーに関係なく、同じローカルネットワーク上にあるかのように通信できます。ZeroTierは簡単に設定でき、エンドツーエンドの暗号化、ネットワークセグメンテーション、ネットワークブリッジ機能などの機能を提供します。

GL.iNetルーターのZeroTier機能を使用すると、ルーターがZeroTier仮想ネットワークに参加できるようになり、リモートでアクセスすることができ、WANやLANのリソースにもアクセスできます。

**注意**: ZeroTierはWireGuardに基づいているため、OpenVPNクライアントやWireGuardクライアントと同時に使用することは推奨されません。バグが発生する可能性があります。

**注意**: この機能は現在ベータ版であり、いくつかのバグがある可能性があります。

## 対応モデル

| ルーターモデル                  | 対応       |
| :----------------------------- | :-------: |
| GL-MT6000 (Flint2)             | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-AXT1800 (Slate AX)          | √         |
| GL-A1300 (Slate Plus)          | √         |
| GL-MT2500/GL-MT2500A (Brume 2) | √         |
| GL-SFT1200 (Opal)              | -         |
| GL-S1300 (Convexa-S)           | -         |
| GL-MT1300 (Beryl)              | -         |
| GL-AX1800 (Flint)              | √         |
| GL-AR750S (Slate)              | -         |
| GL-XE300 (Puli)                | -         |
| GL-X750 (Spitz)                | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-AP1300 (Cirrus)             | -         |
| GL-X300B (Collie)              | -         |
| GL-MV1000/GL-MV1000W (Brume)   | √         |

## 設定

以下はGL-MT2500の例です。

1. 最初のZeroTierネットワークを作成

    [ZeroTierの公式スタートガイド](https://docs.zerotier.com/getting-started/getting-started/)を参照して、ZeroTierアカウントとネットワークを作成します。後で他のデバイスを接続する際に必要となる16桁の英数字のネットワークIDを記録しておいてください。

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. GL.iNetルーターでZeroTierを有効化

    ルーターのウェブ管理パネルにアクセスし、左側 -> アプリケーション -> ZeroTier

    トグルボタンを有効にし、最初のステップでネットワークIDを入力して**適用**をクリックします。
    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

しばらくすると、インターフェースが認証が必要であることを示します。次のステップでこれを処理します。

テストを容易にするために、[この文書](https://docs.zerotier.com/getting-started/getting-started/#setup-the-zerotier-app)の指示に従って、別のデバイス（コンピュータやスマホなど）をZeroTierネットワークに追加します。

3. ネットワーク上のデバイスを認証する

![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

ネットワーク上のデバイスを認証するには、ZeroTier Centralアイコンをクリックし、ZeroTierウェブサイトのネットワーク設定のメンバーセクションに移動します。

![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

新しいデバイスを見つけて、認証チェックボックスをクリックして認証します。必要に応じてデバイスの名前をカスタマイズします。

**注意**: デバイスのアドレスはルーターのZeroTierページに表示されるはずですが、この機能は将来的なバージョンで追加されるかもしれません。ルーターのZeroTierの現在のアドレスを確認するには、ルーターにSSHで接続し、「zerotier-cli info」コマンドを使用します。

![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

しばらくすると、ZeroTier がマネージド IP をデバイスに割り当てます。 この IP アドレスはテスト手順で使用されるため、メモしておいてください。

## 接続性のテスト

同じZeroTierネットワーク上にある別のデバイスで、ウェブブラウザを使用して前のステップで取得したマネージドIPを使用してルーターのウェブ管理パネルにアクセスします。

通常、ルーターのウェブ管理パネルにアクセスできるはずです。また、[公式ドキュメント](https://docs.zerotier.com/getting-started/getting-started/#test-connectivity)に記載されている`ping`コマンドを使用してテストすることもできます。

![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

## リモートアクセスWANの許可

このオプションが有効になっている場合、デバイスのWAN側のリソースはZeroTier仮想ネットワークを介してアクセス可能になります。

例えば、以下のように、この機能が有効な場合、`GL-MT2500`の上位デバイスである`GL-AXT1800`に接続されているため、`leo-phone`から`GL-AXT1800`のIP（`192.168.29.1`）にアクセスできます。

![zerotier, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

操作手順は以下の通りです。

1. リモートアクセスWANを許可を有効にします。

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    ルーティングルールの設定を求められます。

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. [my.zerotier.com](https://my.zerotier.com)にアクセスするか、上の画像の**ZeroTier Central**をクリックし、設定パネルの**Advanced**セクションを見つけます。前のステップで要求されたルート（宛先および経由）を入力します。**Submit**をクリックします。

![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

追加後。

![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}


3. 他のデバイスからIP(`192.168.29.1`)を使用してGL-AXT1800にアクセスできます。実際には、`192.168.29.0/24`のデバイスにアクセスできます。

![zerotier, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow"}

## リモートアクセスLANの許可

このオプションが有効になっている場合、デバイスLAN内のリソースはZeroTier仮想ネットワークを介してアクセス可能になります。

例えば、以下のように、この機能が有効な場合、`GL-MT2500`の下層デバイスである`GL-MT2500`のLANポートに接続されているため、`leo-phone`から`Ubuntu`のIP(`192.168.8.110`)を使用してSSH接続できます。

![ZeroTier, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

操作手順は以下の通りです。

1. リモートアクセスLANを許可を有効にします。

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    ルーティングルールの設定を求められます。

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. [my.zerotier.com](https://my.zerotier.com)にアクセスするか、上の画像の**ZeroTier Central**をクリックし、設定パネルの**Advanced**セクションを見つけます。前のステップで要求されたルート（宛先および経由）を入力します。**Submit**をクリックします。

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    追加後。

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. 他のデバイスでIP(`192.168.8.110`)を使用してpingまたはSSH接続できます。実際には、`192.168.8.0/24`のデバイスにアクセスできます。

![zerotier, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-50-desktop"}

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪問してください。