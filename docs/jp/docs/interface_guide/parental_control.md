# ペアレンタルコントロール

ペアレンタルコントロールは、不適切な Web サイトをブロックし、デバイスの利用時間を制限することで、子どもが安全にインターネットを利用できるようにする機能です。有害なコンテンツへのアクセスを防ぎ、スクリーンタイムを管理し、インターネットを適切に利用できるよう支援します。

この機能はファームウェア v4.2 以降で利用できます。

GL.iNet ルーターの Parental Control については、以下の動画、またはその下の手順をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## ローカル版

ローカル版は GL.iNet が提供するバージョンです。現在はベータ版で、追加料金はかかりません。このバージョンでは、アプリケーション単位でリクエストをフィルタリングしたい場合、ドメインを手動で入力する必要があります。

### 対応モデル

??? "Supported Models"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Unsupported Models"
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
    - GL-X300B (Collie)

### Setup

ルーターの Web 管理画面にログインし、**APPLICATIONS** -> **Parental Control** に移動します。

ファームウェア ver.4.8.4 以降では、**Flow Control** -> **Parental Control** に移動してください。

ルーターの時刻が正確であることを確認してください。正しくない場合は、先に **SYSTEM** -> **Time Zone** で同期します。

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Parental Control を有効にして、**Apply** をクリックします。

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: 管理対象外のデバイスによるインターネットアクセスをブロックするための設定です。

その後、セットアップウィザードに従って Parental Control を設定します。

以下に参考用の 2 つの利用例を示します。実際の利用状況に合わせて調整してください。

**Case 1**

**Scenario**: このプロファイル内のデバイスは、平日の午前 8 時から午前 11 時までは学習目的でのみインターネットにアクセスでき、週末の午後 6 時から午後 8 時まではゲーム目的で利用できます。それ以外の時間帯は、デフォルトでインターネットアクセスがブロックされます。

以下の手順に従って設定してください。

1. プロファイルを作成し、名前を付けます。

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

2. 管理したいデバイスを選択します。まだルーターに接続したことがない場合は、MAC アドレスを入力して手動で追加します。

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

3. アクセス制限を設定します。

    デフォルトでは **Block Internet Access** と **No Limit** の 2 つのルールセットが用意されています。ここでは後で使用するため、さらに **Learning** と **Play** の 2 つのルールセットを作成します。

    **Add a New Ruleset** をクリックします。

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

4. ルールセット名（例: Learning）、色、ブロックするサイトの一覧を設定し、**Apply** をクリックします。

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

    **Note**: ブロックリストに入力したドメイン名にはサブドメインも含まれます。たとえば `example.com` を入力すると、`subdomain.example.com` のようなサブドメインも対象になります。

    同様に、Play という名前の別のルールセットも作成します。色とブロックするサイトを設定し、**Apply** をクリックします。

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

5. 適用後は、以下のようにルールセットが合計 4 つ表示されます。

    **Default Ruleset** に **Block Internet Access** を選択し、**Finish** をクリックしてください。

    ![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

6. 次に Set Schedule に進みます。**Go to Set** をクリックします。

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

7. スケジュールに **Learning** ルールセットを追加します。**Execution Time** を平日の午前 8 時から午前 11 時に設定し、**Apply** をクリックします。

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

8. 新しく作成したプロファイルの編集ページに移動します。

    ![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

    スケジュールが 1 つ作成されていることを確認できます。右上の **Add Schedule** をクリックします。

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/add_schedule.png){class="glboxshadow"}

9. 別のルールセット **Play** をスケジュールに追加します。**Execution Time** を週末の午後 6 時から午後 8 時に設定し、**Apply** をクリックします。

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

10. すると、Play ルールセットもスケジュールに追加されます。

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

    **Note**: 赤い破線は現在時刻を示します。

    スケジュール内の該当部分をクリックすると、ルールセットを編集することもできます。

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.jpg){class="glboxshadow"}

11. 上部の **Parental Control** をクリックして、Parental Control ページに戻ります。

    ![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

    最終的な設定内容が表示されます。既存のプロファイルやルールセットを編集したり、新しく追加したりできます。

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/final_configuration.png){class="glboxshadow"}

**Case 2**

**Scenario**: このプロファイル内のデバイスは、週末の夕方 6 時から 8 時までの間だけ、ゲームや短い動画の視聴のためにインターネットへアクセスできます。それ以外の時間帯は、午後 9 時から翌朝 7 時までの就寝時間を含め、デフォルトでインターネットアクセスがブロックされます。

以下の動画チュートリアルをご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Troubleshooting

設定内容が反映されない場合は、以下の原因が考えられます。

1. DNS キャッシュ。
  
    ブラウザやオペレーティングシステムは DNS キャッシュを保持しているため、変更が反映されるまで時間がかかることがあります。すぐに反映させたい場合は、キャッシュを削除してください。
  
      * [Clear the cache in desktop Chrome](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [Clear the cache in desktop Edge](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. プロファイルのスケジュールがまだ開始されていません。

3. 入力したドメイン名が正しくない可能性があります。

    Web サイトのドメインは公開されていますが、アプリで使用される API ドメインは公開されていないことがよくあります。その場合は、Wireshark などのツールでパケットをキャプチャするか、該当するドメインを調べてください。

    たとえば `www.google.com` をブロックしたい場合は、`www.google.com` よりも `google.com` を使用する方が効果的です。

4. 対象デバイスが接続のたびにランダムな MAC アドレスを使用しているため、ルールが適用されていない可能性があります。

## Bark版

[Bark](https://www.bark.us/){target="_blank"} 版は、Bark が自社プラットフォーム上で提供・管理しているバージョンで、アプリケーションや Web サイトをワンクリックでフィルタリングし、リクエスト履歴を監視できます。

24 種類を超える人気アプリやソーシャルメディアプラットフォームに対する監視機能を提供しており、これらはローカル版ペアレンタルコントロール機能のプリセット一覧にも含まれています。

ログ機能により、どのクライアントがどの Web サイトにいつアクセスしたかを記録できます。これにより、保護者はログを簡単に確認し、ブラックリストに含まれていない Web サイトを特定して、すばやく管理対象に追加できます。

Bark Parental Control 機能はファームウェア v4.5 以降で利用でき、対応するのは一部の GL.iNet ルーターのみです。

**Note**:

1. Bark サービスは **米国、オーストラリア、南アフリカでのみ** 利用できます。詳細は [こちら](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"} をご確認ください。

2. Bark サービスは通常、有料サブスクリプションが必要です。ただし、Bark との提携の一環として、GL.iNet は一部のルーターモデルで Bark Home プランを無料で提供しており、追加費用なしで高度な監視機能とアラートを利用できます。

3. 2 種類の Parental Control を同時に有効にすることはできません。片方のバージョンに切り替えると、もう一方は自動的に無効になります。

### 対応モデル

??? "Supported Models"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)

??? "Unsupported Models"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
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
    - GL-X300B (Collie)

### Setup

ルーターの Web 管理画面にログインし、**APPLICATIONS** -> **Parental Control** に移動します。

Bark 版を選択し、スイッチをオンにして **Apply** をクリックします。

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Note:** Bark のサービスは、一部の国では利用できない場合があります。GL.iNet はこのサービスの提供元ではないため、Bark の利用中に問題が発生した場合は、[Bark's Technical Support ](https://www.bark.us/contact-us/?ref=glinet&home=glinet) まで直接お問い合わせください。

Bark サービスは有効になっていますが、このデバイスはまだどのアカウントにもペアリングされていません。[Device Pairing Link](https://www.bark.us/app/signup/?ref=glinet&home=glinet) を使用して、このデバイスを Bark アカウントにペアリングしてください。

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

ペアリングが完了すると、ページは次のように表示されます。

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

これでデバイスは Bark Cloud Services に接続され、アカウントとのペアリングも完了しています。[Bark を開く](https://www.bark.us/app/children/?ref=glinet&home=glinet) からアカウントにログインし、ネットワーク制御用のプロファイルを作成してください。

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご覧いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
