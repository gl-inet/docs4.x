# ペアレンタルコントロール

ペアレンタルコントロールは、不適切な Web サイトをブロックし、デバイスの利用時間を制限することで、子どもが安全にインターネットを利用できるようにする機能です。有害なコンテンツへのアクセスを防ぎ、スクリーンタイムを管理し、インターネットを適切に利用できるよう支援します。

この機能はファームウェア v4.2 以降で利用できます。**Note**: 一部のモデルでは、ファームウェア v4.2 以降を実行していても、メモリ不足のため Parental Control をサポートしていません。

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

### セットアップ手順

ルーターの Web 管理画面にログインし、**APPLICATIONS** -> **Parental Control** に移動します。

ファームウェア ver.4.8.4 以降では、**FLOW CONTROL** -> **Parental Control** に移動してください。

ルーターの時刻が正確であることを確認してください。正しくない場合は、先に **SYSTEM** -> **Time Zone** で同期します。

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Parental Control を有効にして、**Apply** をクリックします。

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Parental Control の一覧に含まれていないすべてのデバイスのインターネットアクセスをブロックします。

その後、セットアップウィザードに従って Parental Control を設定します。

---

以下に参考用の利用例を 1 つ示します。必要に応じて設定を調整してください。

**Scenario**: このプロファイル内のデバイスは、平日の午前 8 時から午前 11 時までは学習目的でのみインターネットにアクセスでき、週末の午後 6 時から午後 8 時まではゲーム目的で利用できます。それ以外の時間帯は、デフォルトでインターネットアクセスがブロックされます。

以下の手順に従って Parental Control を設定してください。

1. プロファイルを作成し、名前をカスタマイズします。

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. 管理したいデバイスを選択します。先にそれらをルーターへ接続しておく必要があります。まだルーターに接続していない場合は、MAC アドレスを入力して手動で追加します。

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. アクセス制限を設定します。

    デフォルトでは **Block Internet Access** と **No Limit** の 2 つのルールセットが用意されています。

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    **Add a New Ruleset** をクリックして、後で使用する **Learning** と **Play** の 2 つのルールセットを作成します。

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    ルールセット名（例: Learning）、色、ブロックしたいサイトを入力し、**Apply** をクリックします。

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Note**: ブロックリストに入力したドメイン名は、そのサブドメインも含めて適用されます。たとえば `example.com` を入力すると、`subdomain.example.com` のようなサブドメインにも適用されます。

    同様に、別のルールセットも作成します。ルールセット名（例: Play）、色、ブロックしたいサイトを入力し、**Apply** をクリックします。

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    適用後、ルールセットは合計 4 つになります。**Default Ruleset** には **Block Internet Access** を選択し、**Finish** をクリックします。

    ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. 次に、プロファイルのスケジュールを設定します。**Go to Set** をクリックします。

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

    スケジュールに **Learning** ルールセットを追加します。**Execution Time** を平日の午前 8 時から午前 11 時に設定し、**Apply** をクリックします。

    ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. すると、新しく作成したプロファイルの編集ページへ移動します。

    ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    下へ移動すると、スケジュールが 1 つ作成されていることが確認できます。右上の歯車アイコンをクリックして **Add Schedule** を選択します。

    ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. 別のルールセット **Play** をスケジュールに追加します。**Execution Time** を週末の午後 6 時から午後 8 時に設定し、**Apply** をクリックします。

    ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    その後、Play ルールセットがスケジュールに追加されます。

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Note**: 赤い破線は現在時刻を示します。

    スケジュール内の特定のルールセットをクリックすると、実行時間を変更することもできます。

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. 上部の **Parental Control** をクリックして、Parental Control ページに戻ります。

    ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    最終的な設定内容が表示されます。ペアレンタルコントロールは、設定したスケジュールに従って有効になります。既存のプロファイルやルールセットを編集したり、必要に応じて新しく追加したりできます。

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

### Troubleshooting

設定内容が反映されない場合は、以下の原因が考えられます。

1. DNS キャッシュの問題。
  
    ブラウザやオペレーティングシステムは DNS キャッシュを保持しているため、設定変更の反映に時間がかかることがあります。すぐに反映させたい場合は、DNS キャッシュを削除してください。
  
      * [デスクトップ版 Chrome の DNS キャッシュをクリアする](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [デスクトップ版 Edge の DNS キャッシュをクリアする](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. プロファイルのスケジュールがまだ開始されていません。

3. 入力したドメイン名が正しくない可能性があります。

    Web サイトの公開ドメインは見つけやすい一方で、アプリが使用する API ドメインは公開されていないことがよくあります。正しいドメインを特定するには、Wireshark などのパケットキャプチャツールを使うか、関連するドメイン情報を調べてください。

    たとえば `www.google.com` をブロックしたい場合は、`www.google.com` よりも `google.com` を使用する方が効果的です。

4. 対象デバイスがネットワーク接続ごとにランダムな MAC アドレスを使用しているため、アクセスルールが適用されない可能性があります。対象デバイスでランダム MAC アドレスを無効にし、その後デバイスをプロファイルに再追加してください。

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

### セットアップ手順

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
