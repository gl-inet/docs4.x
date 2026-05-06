# ZeroTier

ZeroTier は、インターネットを介してデバイス間の安全な暗号化通信を可能にするソフトウェアベースの仮想プライベートネットワーク（VPN）です。物理的な場所やネットワークトポロジーに関係なく、同じローカルネットワーク上にあるかのようにデバイス同士を通信させる、プライベートな仮想ネットワークを構築できます。ZeroTier は簡単に導入でき、エンドツーエンド暗号化、ネットワーク分離、ネットワークブリッジなどの機能を提供します。

ファームウェア v4.2 以降で利用できる GL.iNetルーターのZeroTier機能を使うと、ルーターをZeroTier仮想ネットワークに参加させることができます。接続後は、ルーター本体だけでなく、WAN側およびLAN側のリソースにもリモートアクセスできます。

**Note**:

1. ZeroTier は、OpenVPN Client、WireGuard Client、GoodCloud Site to Site、Tailscale、AstroWarp と同時に使用すると、ルーティング競合が発生する可能性があるため推奨されません。

2. この機能は現在ベータ版であり、不具合が含まれる可能性があります。

3. 一部のモデルでは、ファームウェア v4.2 以降を実行していても、メモリ不足のため ZeroTier をサポートしていません。

## 対応モデル

??? "Supported Models"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Unsupported Models"
    - GL-X2000 (Spitz Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## ZeroTierネットワークを設定する

ZeroTier Central には、New Central と Legacy Central の2つのバージョンがあります。

- **New Central**: 操作性の向上と新機能が追加された新しいバージョンです。新規ユーザーには、より良い操作体験と最新機能を利用できるためこちらを推奨します。

- **Legacy Central**: 2025年11月以前に作成されたアカウント向けです。既存ユーザーは引き続きネットワーク管理に利用できます。

現時点では両方を並行して利用できますが、直接の移行パスはありません。

使用するバージョンを選んで進めてください。

### New Central

以下は GL-MT3600BE を例にした手順です。

1. [ZeroTier official website](https://www.zerotier.com/){target="_blank"} にアクセスし、アカウントでサインインします。

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. 組織を作成します。

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/create_org.png){class="glboxshadow"}

3. プランを選択します。ここでは例として Personal plan を選びます。このプランには、10台のデバイス、1人のネットワーク管理者、1つのネットワークが含まれます。さらに多くのネットワーク作成、デバイス追加、カスタムルートやDNS設定が必要な場合は、Essential または Scale plan を選択してください。

    ![select plan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. これでZeroTierネットワークが作成されます。右上に表示される16文字の英数字から成る **Network ID** を控えておいてください。後で他のデバイスを接続する際に必要です。

    ![network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. GL.iNetルーターでZeroTierを有効にします。

    ルーターのWeb Admin Panelにログインし、**APPLICATIONS** -> **ZeroTier** に移動します。

    ZeroTier を有効にし、同じページで Network ID を入力して **Apply** をクリックします。

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    しばらくすると、認証が必要であることが画面に表示されます。**ZeroTier Central** のハイパーリンクをクリックして ZeroTier Central に移動します。

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. ZeroTier Central でデバイスを認証します。

    ZeroTier Central で Pending device を見つけ、認証します。

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize2.png){class="glboxshadow"}

    認証後、ページは以下のように表示されます。

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. [このガイド](https://docs.zerotier.com/platforms/){target="_blank"} に従って、別のデバイス（PCやスマートフォンなど）も同じZeroTierネットワークへ追加します。

    以下は Windows 10 Pro ノートPCの例です。

    1. [こちら](https://www.zerotier.com/download/){target="_blank"} からノートPCにZeroTierをインストールします。

    2. ZeroTier を起動すると、デスクトップ右下のシステムトレイにZeroTierアイコンが表示されます。

    3. アイコンを右クリックし、**Join New Network** を選択して、ステップ4で取得した **Network ID** をポップアップウィンドウに入力します。

        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        続いて ZeroTier Central に戻り、Pending device を見つけて認証します。

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. 認証後、ページは以下のように表示されます。**Device ID**、**Name**、**Status**、**Managed IP**、**Public IP** などのメンバーデバイス詳細を確認できます。

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Tips**: 右側の三点アイコンをクリックすると、デバイス名、Managed IP(s)、詳細設定など、メンバーデバイス設定を編集できます。

8. ルーターの **Managed IP** をクリックしてコピーします。この Managed IP を使って、同じZeroTierネットワーク上のノートPCからルーターへアクセスできます。

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. 接続を確認します。

    同じZeroTierネットワークに接続したノートPCでWebブラウザを開き、前の手順で取得したルーターの Managed IP を入力します。

    ルーターのWeb Admin Panel にアクセスできれば、ZeroTier接続は成功です。

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    ノートPCからルーターの Managed IP に対して `ping` を実行して接続確認することもできます。応答が返ってくれば、ZeroTier接続は正常に確立されています。

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central

以下は GL-MT2500 を例にした手順です。

1. 最初のZeroTierネットワークを作成します。

    ZeroTier公式の [Getting Started Guide](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"} を参照して、ZeroTierアカウントとネットワークを作成します。後で他のデバイスを接続する際に必要になるため、16文字の英数字で構成される Network ID を必ず控えておいてください。

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. GL.iNetルーターでZeroTierを有効にします。

    ルーターのWeb Admin Panelにログインし、**APPLICATIONS** -> **ZeroTier** に移動します。

    ZeroTier を有効にし、同じページで Network ID を入力して **Apply** をクリックします。

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    しばらくすると、認証が必要であることが画面に表示されます。

    **ZeroTier Central** のハイパーリンクをクリックして ZeroTier Central に移動します。

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

3. ZeroTier Central でデバイスを認証します。

    ZeroTier Central の **Members** セクションに移動し、新しいデバイスを見つけて **Auth** チェックボックスをクリックし認証します。必要に応じてデバイス名も変更できます。

    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    しばらくすると、ZeroTier がデバイスに **Managed IP** を割り当てます。これは後の接続確認で使用するため、控えておいてください。

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

4. [このガイド](https://docs.zerotier.com/platforms/){target="_blank"} に従って、別のデバイス（PCやスマートフォンなど）も同じZeroTierネットワークへ追加します。

5. 接続を確認します。

    同じZeroTierネットワークに接続された別のデバイスでWebブラウザを開き、前の手順で取得したルーターの ZeroTier Managed IP を入力します。

    ルーターのWeb Admin Panel にアクセスできます。

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

    `ping` コマンドを使って接続確認することもできます。詳細は ZeroTier の [Quickstart Guide](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"} を参照してください。

## WAN からのリモートアクセスを許可する

このオプションを有効にすると、デバイスのWAN側にあるリソースへZeroTier仮想ネットワーク経由でアクセスできます。

たとえば、下図の構成でこの機能を有効にすると、`leo-phone` から `GL-AXT1800` のIPアドレス（`192.168.29.1`）へアクセスできます。これは、GL-AXT1800 が `GL-MT2500` の上位デバイスであり、後者が leo-phone と同じZeroTierネットワークに接続されているためです。

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Note**: この機能を有効にするには、ZeroTierネットワークにルーティングルールを追加する必要があります。Legacy Central ではカスタムルートを1つ無料で追加できますが、New Central では Essential plan 以上でのみカスタムルートを設定できます。詳細は [こちら](https://www.zerotier.com/pricing/) を参照してください。

以下の手順では Legacy Central を例に説明します。

1. ルーターのWeb Admin Panelにログインし、**APPLICATIONS** -> **ZeroTier** に移動します。

    **Allow Remote Access WAN** を有効にし、**Apply** をクリックします。

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    ルーティングルールを設定するよう案内が表示されます。この画面は開いたままにするか、次の手順で必要になるルート情報（Destination と Via）を控えてください。

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. **ZeroTier Central** を開き、**Advanced** セクションを見つけます。

    前の手順で取得したルート情報（Destination と Via）を入力し、**Submit** をクリックします。

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

    ルート追加後、**Managed Routes** セクションは以下のように表示されます。

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. これで、他のデバイスから `GL-AXT1800` のIPアドレス（`192.168.29.1`）へアクセスできます。実際には、`192.168.29.0/24` サブネット内のすべてのデバイスへアクセスできます。

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## LAN へのリモートアクセスを許可する

このオプションを有効にすると、デバイスのLAN側にあるリソースへZeroTier仮想ネットワーク経由でアクセスできます。

たとえば、下図の構成でこの機能を有効にすると、`leo-phone` から `Ubuntu` のIPアドレス（`192.168.8.110`）を使ってSSH接続できます。これは、`Ubuntu` が `GL-MT2500` の下位デバイスであり、後者が leo-phone と同じZeroTierネットワークに接続されているためです。

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Note**: この機能を有効にするには、ZeroTierネットワークにルーティングルールを追加する必要があります。Legacy Central ではカスタムルートを1つ無料で追加できますが、New Central では Essential plan 以上でのみカスタムルートを設定できます。詳細は [こちら](https://www.zerotier.com/pricing/) を参照してください。

以下の手順では Legacy Central を例に説明します。

1. ルーターのWeb Admin Panelにログインし、**APPLICATIONS** -> **ZeroTier** に移動します。

    **Allow Remote Access LAN** を有効にし、**Apply** をクリックします。

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    ルーティングルールを設定するよう案内が表示されます。この画面は開いたままにするか、次の手順で必要になるルート情報（Destination と Via）を控えてください。

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. **ZeroTier Central** を開き、**Advanced** セクションを見つけます。

    前の手順で取得したルート情報（Destination と Via）を入力し、**Submit** をクリックします。

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    ルート追加後、**Managed Routes** セクションは以下のように表示されます。

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. これで、他のデバイスから `Ubuntu` のIPアドレス（`192.168.8.110`）へ ping やSSH接続ができます。実際には、`192.168.8.0/24` サブネット内のすべてのデバイスへアクセスできます。

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
