# Tailscale

V4.2から Tailscale 機能が利用可能

Tailscaleは、あなたが所有するデバイスやアプリケーションを、世界中のどこからでも安全かつ簡単にアクセスできるようにするVPNサービスです。Tailscaleの詳細については、[ ホームページ ](https://tailscale.com/)にアクセスしてください。

GL.iNetルーターのTailscale機能により、ルーターはTailscale仮想ネットワークに参加することができ、WANまたはLANリソースにリモートアクセスすることができます。

**注意**: Tailscale は WireGuard に基づいている、バグが発生する可能性があるため、Tailscale 機能を OpenVPN クライアントまたは WireGuard クライアントと同時に使用することはお勧めできません。

**注意**: この機能は現在ベータ版であり、いくつかのバグがある可能性があります。

## 対応モデル

| ルーターモデル                  | サポート   |
| :----------------------------- | :-------: |
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

## セットアップ

以下はGL-MT2500の例です。

### バインディング

まずTailscaleアカウントを登録してください。テスト用に、まず1台または2台のデバイスをTailscaleアカウントにバインドしてください。バインド後、Tailscale管理コンソールでデバイスとそのステータスを確認できるようになります。

![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

左側 -> アプリケーション -> Tailscale

![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

Tailscaleを有効に切り替え、**適用**をクリックします。

![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

**デバイスバインドリンク**が表示されます。デバイスバインドリンクをクリックします。

![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

ポップアップしてtailscaleのリンクが表示されるので、それをクリックします。

![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

リンクがブラウザで開き、Tailscaleアカウントにログインするよう求められます。

ログインすると、接続するデバイスの確認画面が表示されます。**接続**をクリックします。

![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

接続が成功すると、自動的に管理コンソールにリダイレクトされます。ここでGL-MT2500のIPが`100.88.54.21`であることがわかり、このIPを使ってルーターにアクセスすることができます。

![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

### 接続性テスト

GL-MT2500がTailscale仮想ネットワークに接続されたので、3つの方法で他のデバイスでテストすることができます。

* pingコマンドを使用する

    ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

* ルーターにSSH接続する

    ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

* ウェブ管理パネルにアクセスする

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## リモートアクセスWANの許可

このオプションを有効にすると、デバイスのWAN側のリソースにTailscale仮想ネットワーク経由でアクセスできるようになります。

例えば、この機能を有効にすると、上位デバイスである`GL-MT2500`のWANポートに`GL-AXT1800`が接続されるため、`leo-phone`から`GL-AXT1800`のIP(`192.168.29.1`)でアクセスできるようになります。

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

操作の手順は以下の通り。

1. リモートアクセスWANを許可する。

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Tailscaleの管理コンソールにアクセスすると、GL-MT2500にサブネットがある旨のアラートが表示されます。GL-MT2500のメニューをクリックし、**ルート設定の編集**を選択します。

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. サブネットのルートを有効にする。

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. これで他の端末からGL-AXT1800のIP(`192.168.29.1`)でアクセスできるようになります。実際には、`192.168.29.0/24`のデバイスにアクセスできます。

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow"}

## リモートアクセスLANの許可

このオプションを有効にすると、Tailscale仮想ネットワーク経由でデバイスLAN内のリソースにアクセスできるようになります。

例えば、この機能を有効にすると、 `Ubuntu`は`GL-MT2500`のLANポートに接続されているので、`leo-phone`から`Ubuntu`のIP(`192.168.8.110`)でSSH接続することができます。

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

操作手順は以下の通り。

1. リモートアクセスLANを許可する。

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Tailscaleの管理コンソールにアクセスすると、GL-MT2500にサブネットがある旨のアラートが表示されます。GL-MT2500のメニューをクリックし、**ルート設定の編集**を選択します。

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. サブネットのルートを有効にする。

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. これで他のデバイスでIP(`192.168.8.110`)を使ってpingやSSHができるようになります。実際には`192.168.8.0/24`のデバイスにアクセスできます。

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.jpg){class="glboxshadow gl-50-desktop"}

## カスタム出口ノード

出口ノード機能を使用すると、Tailscale以外のすべてのインターネットトラフィックをネットワーク上の特定のデバイス経由でルーティングできます。トラフィックをルーティングするデバイスは「出口ノード」と呼ばれます。

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

**注意**: GL.iNet ルーターはまだ出口ノードとして利用できません。

**注意 **: ルーターのDNSサーバーがローカルネットワークでのみアクセス可能なプライベートIPアドレスである場合、出口ノードを実行するとインターネットアクセスができなくなる可能性があります。ネットワーク > DNSメニューから、8.8.8.8などの手動パブリックDNSサーバーを設定してください。

セットアップの手順

1. 出口ノードとして使用するデバイスで、**出口ノードの実行**を選択します。Windowsの場合は、以下の手順に従ってください。

    ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    **はい**をクリックしてください。

    ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

2. 管理コンソールでデバイスを出口ノードとして設定します。

    ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

3. GL- ルーターで**カスタム出口ノード**を有効にし、更新ボタンをクリックして、出口ノードとして設定されたデバイスのIPをドロップダウンメニュー から選択し、**適用**をクリックします。以上で設定は完了です。

    ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

4. そのGL-ルーターの下にあるデバイスは、**出口ノード**のホームIPを使用します。

[リンクを参照：出口ノード（すべてのトラフィックをルーティングする)](https://tailscale.com/kb/1103/exit-nodes/)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
