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

ここでは eSIM の状態を確認し、eSIM プロファイルを管理できます。

同時に有効化できるeSIMプロファイルは1つだけです。緑の点は、選択したeSIMプロファイルが現在有効であることを示します。

---

関連記事:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
