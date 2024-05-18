# ペアレンタル・コントロール

V4.2からペアレンタルコントロール機能が利用可能

管理画面の左側 -> アプリケーション -> ペアレンタルコントロール

## ローカル・バージョン

ローカル版はGL.iNetが提供しています。現在ベータ版ですので、追加費用はかかりません。このバージョンでは、アプリケーション別にリクエストをフィルタリングする必要がある場合、ドメインを手動で入力する必要があります。

### 対応モデル

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

### セットアップ

ルーターの時刻が正しいことを確認してください。そうでない場合は、まず「タイムゾーン」で時刻を同期させてください。

![parental control, router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

ここでは例として 2 つの典型的なケースを取り上げます。状況に合わせて調整できます。

#### ケース　1

最初の使用例では、デフォルトでインターネットにアクセスできないようにデバイスを設定します。

**学習**と**遊び**の2つのルールセットを作成し、月曜日から金曜日の午前8時から午前11時までを学習時間、週末の午後6時から午後8時までを遊び時間に設定します。

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

**アンマネージドデバイスのWANブロック**は、アンマネージドデバイスがインターネットにアクセスするのをブロックするために使用されます。

初回はセットアップ・ウィザードが表示されます。

プロフィールに名前を付けます。

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

管理したいデバイスを選択するか、MACアドレスを入力してデバイスを手動で追加します。

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

まずこれらのデバイスをルーターに接続する必要があります。接続しない場合は、MAC アドレスを手動で入力する必要があります。

アクセスのデフォルトのルールセットは、**インターネットアクセスをブロック** です。ここでは、後で使用する2つのルールセットを作成します。**新しいルールセットの追加**をクリックします。

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

ルールセット名、色、ブロックするサイトのリストを指定します。

![create a ruleset guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

ブロックリストに入力されたドメイン名には、そのサブドメインも含まれます。例えば、"example.com "が入力された場合、"subdomain.example.com "のようなサブドメインも含まれます。

ドメイン名の入力に加えて、特定の構文オプションもあります。詳しくは [こちらのページ](https://github.com/gl-inet/gl-feeds/tree/common/gl-sdk4-parental-control#app-feature-library-syntax) をご覧ください。

同様に、別のルールセットを作成します。

![create a ruleset guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

この時点で、合計4つのルールセットが存在することになります。**インターネットアクセスをブロックする**を選択します。

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

次にスケジュールを設定しましょう。**設定へ移動**をクリックします。

![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

月曜日から金曜日の午前8時から午前11時までが学習時間であり、ここでのルールセットは**学習**であると仮定します。**適用**をクリックしてください。

![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

新しく作成されたプロフィールの編集ページに移動します。

![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

スケジュールが作成されました。**スケジュールの追加**をクリックします。

![schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_1.png){class="glboxshadow"}

スケジュールに別のルールセットを追加します。

![add a schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

適用後の**遊び**スケジュールは以下の通りです。

![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

上の画像の紫か緑の部分をクリックすれば、修正することもできます。

![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.png){class="glboxshadow"}

下図のように、一番上の「ペアレンタルコントロール」をクリックすると、ペアレンタルコントロールのページに戻ります。

![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

下の画像は、最終的な設定内容を示しています。既存のプロファイルやルールセットを変更したり、プロファイルやルールセットを追加したりすることができます。

![parental control, finally](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_finally.png){class="glboxshadow"}

#### ケース 2

２つ目の使用例では、デフォルトでインターネットへのアクセスが制限されるようにデバイスを設定します。そして、週末の夕方6時から8時まではゲームや短い動画をプレイできるように設定します。就寝時間の夜9時から翌朝7時までは、インターネットへのアクセスを無効にします。以下のビデオチュートリアルをご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### トラブルシューティング

設定が有効でない理由はいくつか考えられます：

1. DNSキャッシュ
  
    ブラウザやOSにはキャッシュがあるため、変更が反映されるまでには時間がかかります。キャッシュをクリアすればすぐに有効になることもあります。
  
      * [デスクトップのChromeブラウザのキャッシュをクリアする。](https://support.google.com/accounts/answer/32050)
      
      * [デスクトップのEdgeブラウザでキャッシュをクリアする](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2)

2. おそらく、設定したプロファイルのスケジュールがまだ到着していない可能性があります。

3. 設定したドメイン名が間違っている可能性があります。
  
    ウェブサイトのドメイン名は公開されているが、アプリがAPIを呼び出すときに使われるドメイン名は公開されていません。これを解決するには、ツール（Wiresharkなど）を使ってパケットをキャプチャするまたは検索する必要があります。

4. 各接続にランダムなMACアドレスを使用するデバイスを使用している場合、その機能も無効になります。


## Bark バージョン

[Bark](https://www.bark.us/){target="_blank"}バージョンは、Barkが独自のプラットフォーム上で提供・管理しており、アプリケーションやウェブサイトをワンクリックでフィルタリングしたり、リクエスト履歴を監視したりすることができます。このサービスをご利用いただくには、Barkに直接追加料金をお支払いいただく必要があります。

v4.5 以降、Barkペアレンタルコントロール機能が利用可能になりました。

**注意:** アメリカ、オーストラリア、グアム、南アフリカでのみ入手可能。

### 使用シナリオ

Barkは、24以上の異なるアプリケーションやソーシャルメディアネットワークの監視機能を備えており、ローカルのペアレンタルコントロール機能であらかじめ設定されたユーザーリストとして機能します。

ログ機能により、どのクライアントがどの時間帯にどのウェブサイトにアクセスしたかを把握でき、保護者がログを見てブラックリストに載っていないウェブサイトを特定し、速やかに管理制御の範囲に加えることができます。

### 対応モデル

| ルーターモデル       | サポート |
| :------------------ | :-----: |
| GL-MT6000 (Flint 2) |    √    |


### セットアップ

ウェブ管理画面の左側 -> アプリケーション -> ペアレンタルコントロール.

Barkのバージョンを選択したら、有効にして適用します。ペアレンタルコントロールの両方のバージョンを同時に有効にすることはできず、バージョンを切り替えると、もう一方のバージョンは自動的に無効になります。


![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

**ご注意ください：** Barkのサービスは、国によってはご利用いただけない場合があります。 GL.iNetはこのサービスの提供者ではありませんので、Barkを使用して問題が発生した場合は、 [Barkのテクニカルサポート](https://www.bark.us/contact-us/?ref=glinet&home=glinet)に直接お問い合わせください。


![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

Barkサービスは有効ですが、このデバイスはまだどのアカウントともペアリングされていません。 [バイスペアリングリンク](http://go.bark.us/?ref=glinet&home=glinet) を使用して、このデバイスをBarkアカウントとペアリングしてください。


![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing_link.png){class="glboxshadow"}

デバイスはBarkクラウドサービスに接続され、アカウントとペアリングされています。  [Barkにアクセス](https://www.bark.us/app/children/?ref=glinet&home=glinet) ペアリングされたアカウントにログインしてアクセスを制御してください。


![device_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/device_set_up.png){class="glboxshadow"}


![bark_success_pair](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_success_pair.png){class="glboxshadow"}
