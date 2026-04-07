# GL.iNetルーターでeSIM Physical Cardを使用する方法

このガイドでは、GL.iNetオンラインストアで購入したeSIM Physical CardをGL.iNetルーターで使用する方法を紹介します。

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## 特長

eSIM Physical Cardの主な特長は以下のとおりです。

- 4Gおよび5Gネットワークに対応し、安定した高速接続を実現します。
- eSIMプロファイルの追加、削除、有効化を簡単に管理できます。
- 世界中の多くのeSIMストアから、好みのデータパッケージをいつでも選択して購入できます。
- 世界中の多くのeSIMストアのeSIMプロファイルに対応しています。
- 個人情報を提供せずにオンラインでeSIMプロファイルを購入でき、プライバシー漏えいのリスクを軽減できます。
- シードプロファイルが付属し、アクティベーション日から1年間有効な米国およびヨーロッパ向け1GBの無料データと、100MBのグローバルデータが含まれます。
- 一部のGL.iNetデバイスに対応しています。

## 対応モデル

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | ※        |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**※ が付いたモデルについて**:

1. 現在の安定版ファームウェアではeSIMをサポートしていません。eSIM機能を使用するには、eSIM対応ファームウェアをインストールする必要があります。詳細は[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。

2. ※ のモデルで EP06-A モジュールを使用している場合、Qualcommソフトウェアが特定のATコマンドをサポートしていないため、eSIMは利用できません。

3. ※ のモデルで EP06-E モジュールを使用している場合は、この[リンク](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}を参照してモジュールのファームウェアをアップグレードし、eSIM対応ファームウェアをインストールしてeSIM機能を有効にしてください。

**X が付いたモデルについて**:

1. GL-E750V2 vSIM はeSIM機能をサポートしていません。

2. GL-E5800 (Mudi 7) にはeSIMが内蔵されています。そのため、Mudi 7ではeSIM Physical CardはeSIM機能のない通常のSIMカードとして認識されます。

## eSIM Physical Cardを設定する

初めてeSIM Physical Cardを使用する場合は、この設定動画を見るか、以下の手順に従ってGL.iNetルーターで設定してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Step 1:** eSIM Physical Cardをルーターに挿入します。詳しくは以下の画像を参照してください。

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Step 2:** ブラウザを開き、アドレスバーに "192.168.8.1" と入力してGL.iNet管理パネルにログインします。

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Step 3:** デバイスをインターネットに接続します。

**INTERNET** に移動し、**Connect**（古いファームウェアでは **Auto Setup**）をクリックしてCellular経由でインターネットに接続します。

*このeSIM Physical Cardには、アクティベーション日から1年間有効な米国およびヨーロッパ向け1GBの無料データと、100MBのグローバルデータを含むシードプロファイルが付属しています。このデータはeSIMプロファイルの購入とダウンロード専用であり、一般的なインターネット利用を目的としたものではありません。*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

インターネット接続に成功すると、画面は次のように表示されます。

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## eSIMプロファイルを管理する

**Step 1:** GL.iNetデバイスに最新のファームウェアがインストールされていることを確認します。

Version が 4.0 以上で、Firmware Type 番号が 0319 以上であることを確認してください。

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

ファームウェアが**最新でない**場合は、オンライン自動更新または手動更新でアップグレードできます。

<u>Option 1</u>: オンラインファームウェア更新

1. デバイスがインターネットに接続されていることを確認します。

2. Web管理パネルで **SYSTEM** > **Upgrade** > **Online Upgrade** に移動し、**Install** ボタンをクリックして最新ファームウェアに自動更新します。

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Option 2</u>: 手動ファームウェア更新

1. eSIM機能に対応した対象モデルのファームウェアを[こちら](https://dl.gl-inet.com/){target="_blank"}からダウンロードします。

2. Web管理パネルで **SYSTEM** > **Upgrade** > **Local Upgrade** に移動します。ファームウェアファイルを選択するか、指定エリアにドラッグして最新バージョンへ更新します。

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Mudi (GL-E750)、Puli (GL-XE300)、Spitz (GL-X750) など一部のモデルは、Qualcommソフトウェアが特定のATコマンドをサポートしていないため、Quectel EP06-A モジュール搭載時はeSIMをサポートしません。

    2. EP06-E モジュールを搭載している場合は、eSIM機能を利用するために、[このリンク](https://forum.gl-inet.com/t/48907){target="_blank"}を参照してモジュールを最新ソフトウェアへアップグレードしてください。

**Step 2:** eSIM管理画面に移動します。

ファームウェアの更新後、デバイスが再起動するのを待ってからGL.iNet管理パネルにログインします。

**APPLICATIONS** > **eSIM Management** に移動します。ここで現在のeSIMステータスを確認できます。

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

同時に有効化できるeSIMプロファイルは1つだけです。緑の点は、選択したeSIMプロファイルが現在有効であることを示します。

## eSIM管理ガイド

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. 現在のeSIMステータス:**

このセクションには、eSIMの基本情報と現在有効なプロファイルの詳細が表示されます。

- **EID:** 識別とプロファイル制御に使用される eUICC（eSIMチップ）のグローバル一意識別子です。
- **ICCID:** 現在有効なeSIMプロファイルの Integrated Circuit Card Identifier です。
- **IMSI:** 現在有効なeSIMプロファイルの International Mobile Subscriber Identity です。
- **eSIM OS Version:** eUICCの互換性と機能を定義するオペレーティングシステムのバージョンです。
- **eSIM Storage (remain/total):** eSIMプロファイル保存用の eUICC 上の空き容量と総容量です。
- **eSIM Profile Number:** 現在 eUICC に保存されているeSIMプロファイル数です。

**B. シードプロファイル:**

このセクションにはシードプロファイルの詳細が表示されます。シードプロファイルには、アクティベーション日から1年間有効な米国およびヨーロッパ向け1GBの無料データと、100MBのグローバルデータが事前に読み込まれています。このデータを使って世界中で他のプロファイルをダウンロードできます。残量、総量、有効期限などの使用状況も確認できます。

**C. 通常プロファイル:**

このセクションには通常プロファイルの情報が表示されます。オンラインストアでeSIMプロファイルを購入し、**Add eSIM Profile (QR Code Install)** 機能でeSIM QRコードをアップロードすると、アップロード完了後にここへ表示されます。

**D. Add eSIM Profile (QR Code Install):**

これはeSIMプロファイルをアップロードしてインストールするための中心的な機能です。オンラインストアでeSIMプロファイルを購入すると、QRコードが提供されます。このボタンをクリックしてQRコードをアップロードすると、ルーターにeSIMプロファイルがダウンロードおよびインストールされます。

**E. Export Log for Support:**

このセクションでは、eSIMの動作に関連するすべてのログを確認できます。問題が発生して技術サポートが必要な場合は、これらのログをエクスポートし、support@gl-inet.com までメールでサポートチームへ共有できます。

**F. Top-up:**

GL.iNetが提供する無料の事前読み込みデータを使い切った場合、または有効期限切れ後もサービスを継続したい場合は、**Top-up** ボタンをクリックしてQRコードをスキャンし、追加データを購入できます。

**G. 推奨eSIMプロファイルストア:**

GL.iNetでは、利便性のために EIOTCLUB と Tuge の2つの提携eSIMストアを推奨しています。QRコードをスキャンするか、リンク（[the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} または [the Tuge eSIM Store](https://esim_store.gl-inet.com/){target="_blank"}）をクリックして、必要に応じて購入できます。もちろん、他のサードパーティeSIMプロバイダーから購入することも可能です。

**H. Actions:**

このセクションでは、eSIMプロファイルの有効化、切り替え、削除などを簡単に管理できます。

## eSIMシードプロファイルをチャージする

初期設定やeSIMプロファイル購入のために、GL.iNetは事前読み込みデータとしてグローバル向け100MBと、ヨーロッパおよび米国向け1GBを提供しています。これらのプランは料金が高めに設定されており、インターネット接続がない場所に到着した際に新しいeSIMプロファイルをダウンロードする必要がある場合を想定しています。

eSIMシードプロファイルをチャージするには、**Top-up** ボタンをクリックし、QRコードをスキャンして案内に従ってください。

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## eSIMプロファイルを購入してインストールする

ルーターの設定完了後、以下の手順でeSIMプロファイルを購入して有効化します。

**Step 1:** eSIMストアでeSIMプロファイルを購入します。

<u>Option 1</u>: 推奨ストアである [the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} または [the Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"} のいずれかでeSIMプロファイルを購入します。ストアへの直接リンクは以下の画像を参照してください。


*これら2つのストアで購入したeSIMプロファイルパッケージは、当社ルーターとの完全な互換性が確認されています。ご不明な点がある場合は、support@gl-inet.com までサポートチームへお問い合わせください。*

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>Option 2</u>: GL.iNetでテスト済みのストア一覧は[このリンク](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"}を参照してください。なお、これらのストアのすべてのパッケージがGL.iNetルーターと完全互換であることは保証できません。

*GL.iNetはこれらのストアと提携していないため、これらのパッケージに関するアフターサポートや返金対応はできません。*

<u>Option 3</u>: 任意の他のサードパーティプロバイダーからeSIMプロファイルを購入します。

**Step 2**: eSIMプロファイルをインストールする

eSIMプロファイルを購入すると、QRコードが提供されます。このQRコードをコンピューターに保存してください。次に **Add eSIM Profile (QR Code Install)** ボタンをクリックして、購入したeSIMプロファイルをアップロードしてインストールします。

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**Note:** 上の画像の緑色の矢印が示すように、正しい形式のQRコードでは **LPA:** で始まるアクティベーションコードが表示されます。

*ただし、標準外のQRコードでは LPA プレフィックスなしの生のアクティベーションコードしか出ない場合があります。
その場合は、**Download & Install** ボタンをクリックする前に、コードの先頭へ手動で "LPA:" を追加してください。*

**Step 3:** 新しいプロファイルを有効にする

QRコードのアップロードに成功すると、新しいeSIMプロファイルが **Normal Profile** の一覧に表示されます。**Enable** をクリックして新しいeSIMプロファイルを有効化します。

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**Step 4:** 新しいeSIMプロファイルを適用してインターネットに接続する

eSIMプロファイルを有効にしたら、**INTERNET** に移動し、**Connect** をクリックしてeSIMプロファイルを適用し、インターネットへ接続します。

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

*注: 一部のeSIMプロファイルでは、APN、PIN、TTL などの追加設定が必要な場合があります。必要に応じて **Manual Setup** または **SIM Card Settings** をクリックして設定してください。場合によっては、インターネット接続を確立するためにデバイスの再起動が必要です。*

eSIMプロファイルの設定に成功すると、画面は次のように表示されます。

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**Step 5:** eSIMプロファイルを簡単に切り替えまたは削除する

有効化したいプロファイルの横にある **Enable** をクリックすると、eSIMプロファイルを簡単に切り替えられます。eSIMプロファイルを削除するには、**Delete** をクリックしてください。

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
