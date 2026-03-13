# GL.iNetルーターでeSIM物理カードを使用する方法

このガイドでは、GL.iNetオンラインストアで購入したeSIM物理カードをGL.iNetルーターで使用する方法について説明します。

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## 機できる

eSIM物理カードの利時はで下の通りです：

- 信頼性の高い高速接続を実現する4Gおよび5Gネットワークに対応
- eSIMプロファイルの追加、削除、有効化を簡単に管理
- 世界中のほとんどのeSIMストアから好きなデータプランを選択・購入可できる
- 世界中のほとんどのeSIMストアのeSIMプロファイルに対応
- オンラインでeSIMプロファイルを購入でき、個人情報を提供する必要がなく、プライバシー侵害のリスクを低減
- 米国およびヨーロッパへけの1GBの無料データと、100MBのグローバルデータが付いたシードプロファイルが付属（有効期限から1年間有効）
- 対応のGL.iNet機器に対応

## 対応モデル

| ルーター型名                   | 対応   |
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

**※印のモデルについて**：

1. 現にの安定版ファームウェアはeSIMに対応していません。eSIM機できるを使用するには、eSIM対応ファームウェアをインストールする必要があります。詳細な手順については、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
    
2. ※モデルをEP06-Aモジュールで使用している場合、Qualcommソフトウェアが特定のATコマンドをサポートしていないため、eSIMはサポートされていません。
    
3. ※モデルをEP06-Eモジュールで使用している場合は、[こちらリンク](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}を参照して、モジュールのファームウェアをアップグレードし、eSIM対応ファームウェアをインストールしてeSIM機できるを有効にしてください。

**X印のモデルについて**：

1. GL-E750V2 vSIMはeSIM機できるに対応していません。

2. GL-E5800 (Mudi 7)には内蔵のeSIMが搭載されています。そのため、eSIM物理カードはMudi 7では通例のSIMカードとして認識され、eSIM機できるはありません。

## eSIM物理カードの設定

eSIM物理カードを初めて使用する場合は、で下の設定動画を見るか、手順に従ってGL.iNetルーターで設定してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**ステップ1：** eSIM物理カードをルーターに挿入します。詳細な手順については、で下の画像を参照してください。

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**ステップ2：** ブラウザを開き、アドレスバーに「192.168.8.1」と入力してGL.iNet管理パネルにログインします。

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**ステップ3：** 機器をインターネットに接続します。

**INTERNET**に移動し、**Connect**（または旧ファームウェアバージョンでは**Auto Setup**）をクリックして、モバイル通信でインターネットに接続します。

*このeSIM物理カードには、シードプロファイルとして米国およびヨーロッパへけの1GBの無料データと、100MBのグローバルデータが付いています（有効期限から1年間有効）。このデータはeSIMプロファイルの購入とダウンロードのみを目のとしており、一般のなインターネットアクセスへけではありませんので注意してください。*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

インターネットへの接続に成功すると、で下の画面が表示されます。

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## eSIMプロファイルの管理

**ステップ1：** GL.iNet機器に最も新のファームウェアがインストールされていることを確認してください。

バージョンが4.0で上、ファームウェアタイプの番号が0319で上であることを確認してください。

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

ファームウェアが**最も新でない**場合は、オンラインでから動のにアップグレードするか、手動でアップグレードできます。

<u>オプション1</u>：オンラインファームウェアアップグレード

1. 機器がインターネットに接続されていることを確認します。
    
2. Web管理パネルで、**SYSTEM** > **Upgrade** > **Online Upgrade**に移動し、**Install**ボタンをクリックしてから動のに最も新のファームウェアにアップデートします。

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>オプション2</u>：手動ファームウェアアップデート

1. [こちら](https://dl.gl-inet.com/){target="_blank"}からeSIM機できる対応の該当モデルのファームウェアをダウンロードします。
    
2. Web管理パネルで、**SYSTEM** > **Upgrade** > **Local Upgrade**に移動します。ファームウェアファイルを選択するか、指定のエリアにドラッグして最も新バージョンにアップグレードします。

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! 注意

    1. 一部のモデル（Mudi (GL-E750)、Puli (GL-XE300)、Spitz (GL-X750)）は、Qualcommソフトウェアが特定のATコマンドをサポートしていないため、Quectel EP06-Aモジュールが搭載されている場合、eSIMに対応していません。
    
    2. EP06-Eモジュールが搭載されている場合は、[こちらリンク](https://forum.gl-inet.com/t/48907){target="_blank"}を参照して、eSIM機できるのためにモジュールを最も新のソフトウェアにアップグレードしてください。

**ステップ2：** eSIM管理に移動します。

ファームウェアのアップデート後、機器が再起動するのを待って、GL.iNet管理パネルにログインします。

**APPLICATIONS** > **eSIM Management**に移動します。eSIMの現にの状態を確認できます。

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

一度にアクティブにできるeSIMプロファイルは1つのみです。緑色の時は、選択したeSIMプロファイルが現にアクティブであることを示しています。

## eSIM管理ガイド

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. 現にのeSIM状態：**

このセクションでは、eSIMの基本情報と現にアクティブなプロファイルの詳細が表示されます。

- **EID：** eUICC（eSIMチップ）のグローバルにユニークな識別子で、プロファイルの識別と制御に使用されます。
- **ICCID：** 現にアクティブなeSIMプロファイルの集積回路カード識別子。
- **IMSI：** 現にアクティブなeSIMプロファイルの国際モバイル参加者識別子。
- **eSIM OSバージョン：** 互換性と機できるを定義するeUICCのオペレーティングシステムバージョン。
- **eSIMストレージ（残り/合計）：** eSIMプロファイルの保存に使用できるeUICCの利用可できると合計ストレージ容量。
- **eSIMプロファイル番号：** eUICCに保存されているeSIMプロファイルの数。

**B. シードプロファイル：**

このセクションでは、シードプロファイルの詳細が表示されます。シードプロファイルには、有効期限から1年間有効な、米国およびヨーロッパへけの1GBの無料データと、100MBのグローバルデータがプリロードされています。このデータにより、世界中の彼のプロファイルをダウンロードできます。シードプロファイルの使用状況（残りのデータ、合計データ、有効期限など）を監視することもできます。

**C. 通例プロファイル：**

このセクションでは、通例プロファイルの情報が表示されます。オンラインストアでeSIMプロファイルを購入し、**eSIMプロファイルの追加（QRコードインストール）**機できるを使用してeSIM QRコードをアップロードすると、アップロード完た後にここにプロファイルが表示されます。

**D. eSIMプロファイルの追加（QRコードインストール）：**

これはeSIMプロファイルをアップロードしてインストールするコア機できるです。オンラインストアでeSIMプロファイルを購入すると、QRコードが交付されます。このボタンをクリックしてQRコードをアップロードすると、eSIMプロファイルがルーターにダウンロードされてインストールされます。

**E. サポート用ログのエクスポート：**

このセクションでは、eSIMの操作に関連するすべてのログを表示できます。問題が発生し、技術サポートが必要な場合は、これらのログをエクスポートして、support@gl-inet.comまでメールでお送りください。

**F. トップアップ：**

GL.iNet提供の無料およびプリロードされたデータを使い果たした場合、またはデータが期限切れになってサービスを継続して使用したい場合は、**トップアップ**ボタンをクリックしてQRコードをスキャンし、追加データを購入できます。

**G. 推奨eSIMプロファイルストア：**

GL.iNetでは、便宜上2つのパートナーeSIMストア（EIOTCLUBとTuge）を推奨しています。ニーズに基づいてQRコードをスキャンするかリンク（[EIOTCLUB eSIMストア](https://www.eiotclub.com/pages/esim){target="_blank"}または[Tuge eSIMストア](https://esim_store.gl-inet.com/){target="_blank"}）をクリックして購入できます。その彼のサードパーティープロバイダーからeSIMパッケージを購入することもできます。

**H. アクション：**

このセクションでは、eSIMプロファイルを簡単に管理できます。有効化、切り替え、削除を行うことができます。

## eSIMシードプロファイルのトップアップ

初期設定やeSIMプロファイルの購入のために、GL.iNetはプリロードされたデータを提供します：グローバル使用用の100MBとヨーロッパ・米国用の1GB。これらのプランはより高額ですが、インターネットにアクセスできない場所にまで着したときに新しいeSIMプロファイルをダウンロードする必要がある状況へけに設計されています。

eSIMシードプロファイルをトップアップするには、**トップアップ**ボタンをクリックし、QRコードをスキャンして手順に従ってください。

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## eSIMプロファイルの購入とインストール

ルーターの設定が完たしたら、で下の手順に従ってeSIMプロファイルを購入して有効化してください。

**ステップ1：** eSIMストアでeSIMプロファイルを購入します。

<u>オプション1</u>：推奨ストアのいずれかからeSIMプロファイルを購入します。[EIOTCLUB eSIMストア](https://www.eiotclub.com/pages/esim){target="_blank"}または[Tuge eSIMストア](https://esim_store.gl-inet.com){target="_blank"}。直接ストアへのリンクについては、で下の画像を参照してください。

*これらの2つのストアから購入されたすべてのeSIMプロファイルパッケージは当社のルー器と完全に互換性があります。ご質問がございましたら、support@gl-inet.comまでお問い合わせください。*

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>オプション2</u>：[こちらリンク](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"}を参照して、GL.iNetによってテストされたストアのリストを取なければならないします。これらのストアのすべてのパケットがGL.iNetルーターと完全に互換性があることを保証できないことにご注意くだい。

*GL.iNetはこれらのストアとのパートナーシップしていないため、これらのパッケージに関するカスタマーサポートや払い戻しについては支援できません。*

<u>オプション3</u>：お好みの彼のサードパーティープロバイダーからeSIMプロファイルを購入します。

**ステップ2**：eSIMプロファイルをインストールする

eSIMプロファイルを購入すると、QRコードが交付されます。このQRコードをコンピューターに保存します。次に、**eSIMプロファイルの追加（QRコードインストール）**ボタンをクリックして、購入したeSIMプロファイルをアップロードしてインストールします。

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**注意：** 上記の画像の緑色の矢印に示すように、適切にフォーマットされたQRコードは、**LPA:**で始まるアクティブコードを表示します。

*ただし、一部の非標準QRコードは、LPAプレフィックスなしの生のアクティブコードのみを生成場合があります。この場合は、**ダウンロードとインストール**ボタンをクリックする前に、コードの先頭に手動で「LPA:」を追加してください。*

**ステップ3：** 新しいプロファイルを有効化する

QRコードを正常にアップロードすると、新しいeSIMプロファイルが**通例プロファイル**の下に表示されます。**有効化**をクリックして、新しいeSIMプロファイルをアクティブにします。

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**ステップ4：** 新しいeSIMプロファイルを適用してインターネットに接続する

eSIMプロファイルを有効化したら、**INTERNET**に移動し、**Connect**をクリックしてeSIMプロファイルを適用し、インターネットに接続します。

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

*注意：一部のeSIMプロファイルには、APN、PIN、TTLなどの追加設定が必要な場合があります。必要な場合は、**手動設定**または**SIMカード設定**をクリックしてこれらの設定を構成してください。場合によっては、インターネット接続を確立するために機器を再起動する必要があるかもしれません。*

eSIMプロファイルの設定が正常に完たすると、で下の画面が表示されます。

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**ステップ5：** eSIMプロファイルを簡単に切り替えるか削除する

有効化したいプロファイルの横にある**有効化**をクリックすることで、eSIMプロファイルを簡単に切り替えることができます。eSIMプロファイルを削除するには、**削除**をクリックするだけです。

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
