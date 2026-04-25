# eSIM 管理

Web管理パネル左側の **APPLICATIONS** -> **eSIM Management** に移動します。

このページでは、eSIM Physical Card の状態確認と eSIM プロファイルの管理ができます。内容は **Current eSIM Status** と **eSIM Profile List** の 2 つの部分で構成されています。

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## 対応モデル

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | √         |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**※ が付いたモデルについて**

1. 現在の安定版ファームウェアでは eSIM をサポートしていません。eSIM 機能を使用するには、eSIM 対応ファームウェアをインストールする必要があります。詳細は [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} ください。

2. ※ のモデルで EP06-A モジュールを搭載している場合、Qualcomm ソフトウェアが必要な AT コマンドをサポートしていないため、eSIM は利用できません。

3. GL-E750 (Mudi) および ※ のモデルで EP06-E モジュールを搭載している場合は、この[リンク](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}を参照して、まずモジュールのファームウェアをアップグレードしてください。その後、eSIM 対応ファームウェアをインストールして eSIM 機能を有効にします。

**X が付いたモデルについて**

1. GL-E750V2 vSIM は eSIM 機能をサポートしていません。

2. GL-E5800 (Mudi 7) には eSIM が内蔵されています。そのため、Mudi 7 では eSIM Physical Card は eSIM 機能のない通常の SIM カードとして認識されます。

## Current eSIM Status

このセクションには、現在有効な eSIM プロファイルの基本情報と詳細が表示されます。

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** 識別とプロファイル管理に使用される eUICC（eSIM チップ）のグローバル一意識別子です。
- **ICCID:** 現在有効な eSIM プロファイルの Integrated Circuit Card Identifier です。
- **IMSI:** 現在有効な eSIM プロファイルの International Mobile Subscriber Identity です。
- **eSIM OS Version:** eUICC の互換性と対応機能を定義するオペレーティングシステムのバージョンです。
- **eSIM Storage (remain/total):** eSIM プロファイル保存用の eUICC 上の空き容量と総容量です。
- **eSIM Profile Number:** 現在 eUICC に保存されている eSIM プロファイル数です。通信事業者ごとに eSIM プロファイルのサイズが異なるため、保存できるプロファイル数も異なります。

## eSIM Profile List

このセクションには、シードプロファイルと通常プロファイルの情報が表示されます。

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: シードプロファイルには、アクティベーション日から 1 年間有効な米国およびヨーロッパ向け 1GB の無料データと、100MB のグローバルデータが事前に読み込まれています。このデータを利用して、世界中で他のプロファイルをダウンロードできます。残量、総量、有効期限などの利用状況も確認できます。

- **Normal Profile**: eSIM プロファイルを購入し、QR コードまたはアクティベーションコードでアップロードすると、ここに表示されます。

### シードプロファイルをチャージする

GL.iNet は、初期設定と eSIM プロファイルの有効化向けに、100MB のグローバルデータと、ヨーロッパおよび米国向け 1GB のデータを含むシードプロファイルを事前に提供しています。このプランは、インターネット接続のない場所に到着した際に新しい eSIM プロファイルをダウンロードするためのものです。

事前読み込みされた無料データを使い切った場合、または有効期限が切れた後もサービスを継続したい場合は、シードプロファイルをチャージできます。

**Seed Profile** セクション右側の **Top-up** ボタンをクリックします。

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

ポップアップ画面で QR コードをスキャンし、案内に従ってチャージを完了してください。

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### eSIM プロファイルを購入する

eSIM プロファイルは、推奨ストア、テスト済みストア、またはその他のサードパーティ eSIM プロバイダーから購入できます。

??? note "Option 1: 推奨ストアで購入する"

    推奨ストアは 2 つあります。[EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} と [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"} です。

    **Normal Profile** セクション右側の **eSIM Profile Recommended Store** をクリックします。

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    QR コードをスキャンするか、リンクをクリックして eSIM プロファイルを購入します。

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Note**: これら 2 つのストアで購入した eSIM プロファイルパッケージは、GL.iNet ルーターとの完全な互換性が確認されています。ご不明点があれば、[support@gl-inet.com](mailto:support@gl-inet.com) までご連絡ください。

??? note "Option 2: テスト済みストアで購入する"

    GL.iNet がテストしたストア一覧は [このリンク](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} を参照してください。

    **Note**: これらのストアのすべてのプロファイルやパッケージについて、GL.iNet ルーターとの完全な互換性は保証できません。GL.iNet はこれらのストアと提携していないため、アフターサポートや返金対応はできません。

??? note "Option 3: その他のサードパーティ eSIM プロバイダーから購入する"

    他のサードパーティプロバイダーから eSIM プロファイルを購入することもできます。

    ただし、他のサードパーティプロバイダーから購入した eSIM プロファイルについて、GL.iNet ルーターとの完全な互換性は保証できません。ご自身の判断で購入してください。GL.iNet は互換性の問題について責任を負いません。

    アフターサポートや返金については、該当する eSIM プロバイダーへお問い合わせください。

### eSIM プロファイルをアップロードする

eSIM プロファイルを購入すると、通常は QR コードまたはアクティベーションコードを受け取ります。この QR コードをローカルに保存し、以下の手順で eSIM プロファイルをアップロードしてください。

1. **Normal Profile** セクション下部の **Add eSIM Profile** をクリックします。

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. eSIM の QR コードをアップロードするか、アクティベーションコードを入力して **Install** をクリックします。すると、eSIM プロファイルがルーターにダウンロードされてインストールされます。

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Note:**

    1. ほとんどの eSIM プロファイルは 1 回しかダウンロードおよびインストールできません。

    2. 正しい形式の QR コードでは、**LPA:** で始まるアクティベーションコードが表示されます。ただし、標準外の QR コードでは LPA プレフィックスなしの生のコードしか表示されない場合があります。その場合は、**Install** をクリックする前に、コードの先頭へ手動で `LPA:` を追加してください。

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. まだ eSIM プロファイルを購入していない場合は、**eSIM Profile Recommended Store** から購入できます。詳細は [こちら](#esim-プロファイルを購入する) を参照してください。

3. eSIM プロファイルを有効にします。

    アップロードが成功すると、新しい eSIM プロファイルが **Normal Profile** の一覧に表示されます。**Enable** をクリックして有効化します。

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. インターネットに接続します。

    eSIM プロファイルを有効にしたら、**INTERNET** -> **Cellular** に移動します。**Connect** をクリックして、eSIM プロファイル経由でインターネット接続を確立します。

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Note**: 一部の eSIM プロファイルでは、APN、PIN、TTL などの追加設定が必要な場合があります。必要に応じて **Manual Setup** または **SIM Card Settings** をクリックして調整してください。場合によっては、インターネット接続を確立するためにデバイスの再起動が必要です。*

5. ルーターが eSIM プロファイル経由で正常に接続されると、ページは次のように表示されます。

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### サポート用ログをエクスポートする

**Export Log for Support** をクリックすると、eSIM 関連のログをすべて確認できます。問題が発生して技術サポートが必要な場合は、eSIM ログをエクスポートし、[support@gl-inet.com](mailto:support@gl-inet.com) 宛てにメールでサポートチームへ共有してください。

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

関連記事:

- [GL.iNetルーターでeSIM Physical Cardを使用する方法](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Android デバイスで eSIM Physical Card を使用する方法](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} ください。
