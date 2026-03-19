# GL.iNetルーターでeSIM物理カードを使う方法

このガイドでは、GL.iNet オンラインストアで購入した eSIM 物理カードを GL.iNet ルーターで使用する方法を説明します。

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## 特長

eSIM物理カードの主な特長は次のとおりです。

- 4G および 5G ネットワークに対応し、高速かつ安定した接続を利用できます。
- eSIM プロファイルの追加、削除、有効化を簡単に管理できます。
- 世界中の多くの eSIM ストアから、好みのデータプランを選んで購入できます。
- 世界中の多くの eSIM ストアの eSIM プロファイルに対応しています。
- 個人情報を提供せずにオンラインで eSIM プロファイルを購入できるため、プライバシー漏えいのリスクを低減できます。
- 米国およびヨーロッパ向けの無料データ 1GB と、グローバルデータ 100MB を含むシードプロファイルが付属します。有効期間は有効化日から 1 年間です。
- 一部の GL.iNet デバイスで利用できます。

## 対応モデル

| ルーター型番          | 対応 |
| :-------------------- | :--: |
| GL-X2000 (Spitz Plus) |  √   |
| GL-X3000 (Spitz AX)   |  √   |
| GL-XE3000 (Puli AX)   |  √   |
| GL-E750V2 (Mudi V2)   |  √   |
| GL-E750 (Mudi)        |  ※   |
| GL-XE300 (Puli)       |  ※   |
| GL-X750 (Spitz)       |  ※   |
| GL-X300B (Collie)     |  ※   |
| GL-E750V2 vSIM        |  X   |
| GL-E5800 (Mudi 7)     |  X   |

**※ 印のモデルについて**

1. 現在の安定版ファームウェアでは eSIM をサポートしていません。eSIM 機能を利用するには、eSIM 対応ファームウェアをインストールする必要があります。詳細は [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} ください。

2. ※ 印のモデルで EP06-A モジュールを使用している場合、Qualcomm ソフトウェアが一部の AT コマンドをサポートしていないため、eSIM は利用できません。

3. ※ 印のモデルで EP06-E モジュールを使用している場合は、[こちらのリンク](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="\_blank"} を参照し、モジュールのファームウェアをアップグレードしたうえで、eSIM 対応ファームウェアを導入してください。

**X 印のモデルについて**

1. GL-E750V2 vSIM は eSIM 機能をサポートしていません。

2. GL-E5800 (Mudi 7) は eSIM を内蔵しているため、eSIM 物理カードを挿しても通常の SIM カードとして認識され、eSIM 機能は利用できません。

## eSIM物理カードを設定する

初めて eSIM 物理カードを使用する場合は、以下の動画を見るか、手順に従って GL.iNet ルーターで設定してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**ステップ1:** eSIM 物理カードをルーターに挿入します。詳しくは以下の画像を参照してください。

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**ステップ2:** ブラウザを開き、アドレスバーに `192.168.8.1` と入力して GL.iNet 管理パネルにログインします。

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**ステップ3:** インターネットに接続します。

**INTERNET** に移動し、**Connect** をクリックします。古いファームウェアでは **Auto Setup** と表示される場合があります。モバイル回線経由でインターネットに接続してください。

_この eSIM 物理カードには、米国およびヨーロッパ向けの無料データ 1GB と、グローバルデータ 100MB を含むシードプロファイルが付属しています。有効期間は有効化日から 1 年間です。このデータは eSIM プロファイルの購入およびダウンロード専用であり、通常のインターネット利用を目的としたものではありません。_

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

インターネット接続に成功すると、次のような画面が表示されます。

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## eSIMプロファイルを管理する

**ステップ1:** GL.iNet デバイスに最新ファームウェアがインストールされていることを確認します。

バージョンが 4.0 以上で、Firmware Type 番号が 0319 以上であることを確認してください。

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

ファームウェアが**最新ではない**場合は、オンラインまたは手動でアップグレードできます。

<u>オプション1</u>: オンラインアップグレード

1. デバイスがインターネットに接続されていることを確認します。

2. Web 管理パネルで **SYSTEM** > **Upgrade** > **Online Upgrade** に移動し、**Install** をクリックすると、自動的に最新ファームウェアへ更新されます。

   ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>オプション2</u>: 手動アップデート

1. [こちら](https://dl.gl-inet.com/){target="\_blank"} から、eSIM 機能に対応した対象モデル用ファームウェアをダウンロードします。

2. Web 管理パネルで **SYSTEM** > **Upgrade** > **Local Upgrade** に移動し、ファームウェアファイルを選択するか指定領域にドラッグして、最新バージョンへアップグレードします。

   ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Mudi (GL-E750)、Puli (GL-XE300)、Spitz (GL-X750) など一部のモデルは、Quectel EP06-A モジュールを搭載している場合、Qualcomm ソフトウェアが一部の AT コマンドをサポートしていないため eSIM を利用できません。

    2. EP06-E モジュールを搭載している場合は、[こちらのリンク](https://forum.gl-inet.com/t/48907){target="_blank"} を参照し、モジュールを最新ソフトウェアにアップグレードしてください。

**ステップ2:** eSIM Management に移動します。

ファームウェア更新後、デバイスが再起動したら GL.iNet 管理パネルにログインします。

**APPLICATIONS** > **eSIM Management** に移動すると、現在の eSIM 状態を確認できます。

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

同時に有効化できる eSIM プロファイルは 1 つだけです。緑色のドットは、そのプロファイルが現在有効であることを示します。

## eSIM Management ガイド

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. 現在のeSIM状態:**

このセクションには、eSIM の基本情報と現在有効なプロファイルの詳細が表示されます。

- **EID:** eUICC（eSIM チップ）のグローバルで一意な識別子です。プロファイルの識別や制御に使用されます。
- **ICCID:** 現在有効な eSIM プロファイルの Integrated Circuit Card Identifier です。
- **IMSI:** 現在有効な eSIM プロファイルの International Mobile Subscriber Identity です。
- **eSIM OS Version:** eUICC の互換性や機能を定義するオペレーティングシステムのバージョンです。
- **eSIM Storage (remain/total):** eSIM プロファイル保存用として eUICC 上で利用可能な容量と総容量です。
- **eSIM Profile Number:** eUICC に保存されている eSIM プロファイル数です。

**B. シードプロファイル:**

このセクションには、シードプロファイルの詳細が表示されます。シードプロファイルには、有効化日から 1 年間有効な米国およびヨーロッパ向けの無料データ 1GB と、グローバルデータ 100MB があらかじめ含まれています。このデータを使って世界各地で他のプロファイルをダウンロードできます。残量、総量、有効期限などの使用状況も確認できます。

**C. 通常プロファイル:**

このセクションには、通常プロファイルの情報が表示されます。オンラインストアで eSIM プロファイルを購入し、**Add eSIM Profile (QR Code Install)** 機能で QR コードをアップロードすると、アップロード完了後にここへ表示されます。

**D. eSIMプロファイルを追加する（QR Code Install）:**

eSIM プロファイルをアップロードしてインストールする中心機能です。オンラインストアで eSIM プロファイルを購入すると QR コードが発行されます。このボタンから QR コードをアップロードすると、ルーターへ eSIM プロファイルがダウンロードされてインストールされます。

**E. サポート用ログをエクスポートする:**

このセクションでは、eSIM の動作に関連するログを確認できます。問題が発生して技術サポートが必要な場合は、ログをエクスポートし、support@gl-inet.com 宛てに送信してください。

**F. トップアップ:**

GL.iNet が提供する無料データやプリロード済みデータを使い切った場合、または有効期限切れ後もサービスを継続したい場合は、**Top-up** をクリックし、QR コードをスキャンして追加データを購入できます。

**G. 推奨eSIMプロファイルストア:**

GL.iNet では、EIOTCLUB と Tuge の 2 つのパートナー eSIM ストアを推奨しています。QR コードをスキャンするか、[EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="\_blank"} または [Tuge eSIM Store](https://esim_store.gl-inet.com/){target="\_blank"} のリンクを開いて購入できます。ほかのサードパーティープロバイダーから eSIM パッケージを購入することも可能です。

**H. 操作:**

このセクションでは、eSIM プロファイルの有効化、切り替え、削除を簡単に行えます。

## eSIMシードプロファイルをトップアップする

初期設定や eSIM プロファイル購入のために、GL.iNet はプリロード済みデータとして、グローバル向け 100MB とヨーロッパ / 米国向け 1GB を提供しています。これらのプランは比較的高価ですが、インターネットに接続できない場所へ到着した直後に新しい eSIM プロファイルをダウンロードする必要がある場面を想定して用意されています。

eSIM シードプロファイルをトップアップするには、**Top-up** ボタンをクリックし、QR コードをスキャンして画面の案内に従ってください。

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## eSIMプロファイルを購入してインストールする

ルーターの設定が完了したら、以下の手順に従って eSIM プロファイルを購入し、有効化してください。

**ステップ1:** eSIM ストアで eSIM プロファイルを購入します。

<u>オプション1</u>: 推奨ストアのいずれかから購入します。[EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="\_blank"} または [Tuge eSIM Store](https://esim_store.gl-inet.com){target="\_blank"} を利用してください。直接リンクは以下の画像からも確認できます。

_これら 2 つのストアで購入した eSIM プロファイルパッケージは、当社ルーターとの完全互換性が確認されています。ご不明点があれば support@gl-inet.com までお問い合わせください。_

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>オプション2</u>: [こちらのリンク](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="\_blank"} を参照すると、GL.iNet がテストしたストアの一覧を確認できます。ただし、これらのストアのすべてのパッケージについて、GL.iNet ルーターとの完全な互換性を保証するものではありません。

_GL.iNet はこれらのストアと提携していないため、これらのパッケージに関するアフターサポートや返金には対応できません。_

<u>オプション3</u>: 任意のサードパーティープロバイダーから eSIM プロファイルを購入します。

**ステップ2:** eSIM プロファイルをインストールします。

購入後に発行される QR コードをコンピューターへ保存します。その後、**Add eSIM Profile (QR Code Install)** をクリックして、購入した eSIM プロファイルをアップロードし、インストールします。

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**注意:** 上の画像で緑色の矢印が示しているように、正しくフォーマットされた QR コードでは、**LPA:** で始まるアクティベーションコードが表示されます。

_一部の非標準 QR コードでは、LPA プレフィックスのない生のアクティベーションコードだけが表示される場合があります。その場合は、**Download & Install** をクリックする前に、コードの先頭へ手動で `LPA:` を追加してください。_

**ステップ3:** 新しいプロファイルを有効化します。

QR コードのアップロードに成功すると、新しい eSIM プロファイルが **通常プロファイル** の下に表示されます。**Enable** をクリックして有効化してください。

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**ステップ4:** 新しい eSIM プロファイルを適用し、インターネットへ接続します。

eSIM プロファイルを有効化したら、**INTERNET** に移動し、**Connect** をクリックしてプロファイルを適用します。

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

_注意: 一部の eSIM プロファイルでは、APN、PIN、TTL などの追加設定が必要になることがあります。必要な場合は **Manual Setup** または **SIM Card Settings** をクリックして設定してください。インターネット接続を確立するために、デバイスの再起動が必要な場合もあります。_

設定が完了すると、次のような画面が表示されます。

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**ステップ5:** eSIM プロファイルを切り替える、または削除します。

有効化したいプロファイルの横にある **Enable** をクリックすると、簡単にプロファイルを切り替えられます。削除する場合は **Delete** をクリックしてください。

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
