# Ubootを使用してルーターをデブリックする

DIY プロジェクトを行っていたり、間違ったファームウェアをフラッシュしたりした場合、ルーターがブリックしてしまう可能性があります。 ルーターにアクセスできない場合がありますが、Uboot フェイルセーフを使用してファームウェアを再インストールできます。

**注意:** Uboot 操作により、ルーターの設定とインストールされているプラグインが削除されます。

---

イーサネットポートを備えたコンピュータをご用意ください。イーサネットポートがない場合は、追加の USB イーサネットアダプタをご用意ください。

以下の手順に従って Uboot Web UI にアクセスし、ファームウェアを再インストールしてください。

以下のビデオチュートリアルも参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/EAaaw8nyrnE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. [ここから](https://dl.gl-inet.com/){target="_blank"}ファームウェアをコンピュータにダウンロードしてください。

    GL-AR750S-EXT などの一部のモデルでは、2 つの形式のファームウェアがありますが、Uboot 用のファームウェアを使用してください。ファイル名拡張子は **.img** です。

2. ルーターの電源を切ります。コンピューターをルーターの **イーサネット ポート (LAN または WAN)** に接続します。他のポートはすべて**未接続**にしておく必要があります。

3. リセット ボタンをしっかりと押したままにして、ルーターの電源を入れます。 ルーターに電源ボタンがない場合は、電源プラグを差し込むと自動的に電源が入ります。

    LED が規則的なシーケンスで数回点滅します。シーケンスが変わったら指を放してください。

    以下は各モデルのLED点滅シーケンスを説明します。

    **注意:** 同じルーターモデルでも製造年月日が異なると、LEDの色や点滅順序が異なる場合がありますが、UBootプロセスには影響しません。LEDの点滅の変化にご注意ください。

    - **GL-MT3000(Beryl AX)**の場合、青色LEDが6回点滅し、その後白色に変わり点灯します。

    -  **GL-MT2500/GL-MT2500A(Brume 2)**の場合、 青色LEDが5回点滅した後、白色に点灯します。

    -  **GL-S200**の場合、シアン色のLEDが5回点滅した後、短時間紫色に変わり、その後シアン色に変わって点灯したままになります。

    -  **GL-A1300(Slate Plus)**の場合、 LEDがゆっくり5回点滅した後、しばらく点灯し、その後ずっと速く点滅します。

    - **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)**, **microuter-N300**の場合、 LEDが5回点滅します。

    -  **GL-E750(Mudi)**の場合、 画面には最初に「Booting」、次に「Reset Counting 1 to 4」、最後に「Please Open Web 192.168.1.1」が表示されます。

    -  **GL-S1300(Convexa-S), GL-B1300(Convexa-B)**の場合、 LEDが4回点滅します。
        
        一番左のLEDがずっと点灯したまま、一番右のLEDが4回点滅し、その後、真ん中のLEDが点灯し続けることがあります。
        
        (一部の古いGL-B1300では、一番左のLEDがずっと点灯し、真ん中のLEDと一番右のLEDが同時に5回点滅した後、点灯したままになります。)

    -  **GL-SF1200**の場合、 5G LEDが5回点滅した後、点灯したままになります。

    -  **GL-AX1800(Flint)**の場合、 青色LEDが5回点滅した後、白色に変わり点灯し続けます。

    -  **GL-AXT1800(Slate AX)**の場合、 青色LEDが5回点滅した後、点灯したままになります。

    -  **GL-XE300(Puli)**の場合、LAN LED が 5 回点滅し、その後 WIFI LED が点灯したままになります。

    -  **GL-X300B(Collie)**の場合、 WAN LED が 5 回点滅し、その後 WIFI LED が点灯したままになります。

    -  **GL-SFT1200(Opal)**の場合、 青色の LED が 5 回点滅し、その後白色に変わり、点灯したままになります。

    -  **GL-AP1300(Cirrus)**の場合、 電源LEDがゆっくり5回点滅した後、しばらく点灯し、その後常に速く点滅します。

    -  **GL-MT1300(Beryl)**の場合、 LEDは最初青色で、ゆっくり2回点滅し、その後少し速く5回点滅して白色に変わり、点灯したままになります。

    -  **GL-B2200(Velica)**の場合、 2つのLEDは最初青色で、次に白色に変わり5回点滅した後、青色に変わり点灯し続けます。

    -  **GL-MV1000/GL-MV1000W(Brume)**の場合、 LEDが点滅しません。（電源と WAN LED はずっと点灯したままです）。

    -  **GL-MiFi**の場合、 LEDが6回点滅します。

    -  **GL-MT300N**, **GL-MT300A**の場合、 LEDが3回点滅します。

4. 手動でコンピュータのIPアドレスを**192.168.1.2**に設定します。各オペレーティングシステムの手順をご覧ください：

    ??? "Windows 7 / Windows 10"

        1. **コントロールパネル**-> **ネットワークとインターネットt** -> **ネットワークと共有センター** -> **アダプタ設定の変更**をクリックください。

        2. **ローカルエリア接続**を右クリック -> **プロパティ**。

        3. **インターネットプロトコルバージョン4 (TCP/IPv4)** をクリック-> **プロパティ**.
 
        4. **IP アドレス**を手動で「192.168.1.2」に設定します。

        5. **サブネット マスク**を「255.255.255.0」に設定します。

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. **OK** ボタンをクリックします。

    ??? "Windows 11"

        1. 設定を開きます。

        2. **ネットワークとインターネット**をクリックしてください。

        3. **イーサネット** タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. [IP 割り当て] セクションで、**編集** ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. **手動** オプションを選択します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. **IPv4 トグル** スイッチをオンにします。

        7. 静的 **IP アドレス** を **192.168.1.2** に設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. **サブネット マスク**を**255.255.255.0**として指定します。

        9. **保存** ボタンをクリックします。

    ??? "macOS"

        1. 画面左上の**Apple**アイコンをクリックし、**システム環境設定**を選択します。

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        2.  **ネットワーク**をクリックします。

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        3. 左側の**イーサネット**をクリックし、**IPv4の設定**の隣にあるドロップダウンボックスをクリックし、**手動**を選択します。USBイーサネットアダプターを使用している場合、イーサネットが見つからず、USB イーサネット アダプタの名前として表示される場合があります。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        4. **IPv4 アドレス** に「192.168.1.2」、**サブネット マスク** に「255.255.255.0」、**ルーター** に「192.168.1.1」を入力し、右下隅の [適用] ボタンをクリックします。 

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. ブラウザを使用して **http://192.168.1.1** にアクセスします。これは Uboot Web UI です。

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **注意:** Uboot のバージョンは製造日によって異なるため、上記の Uboot Web UI は表示されるものとまったく同じではない可能性があります。場合によっては、Uboot バージョンをアップグレードすることをお勧めします。 以下のチュートリアルを参照してください。

    ??? "Ubootのバージョンをアップグレードする"

        Uboot のバージョンによっては古すぎる、または Web UI がユーザーにとって理解しにくい場合があるため、Uboot のバージョンをアップグレードすることをお勧めします。

        たとえば、次の図は、GL-AR750S の古い Uboot バージョンの Web UI を示しています。 2 つの **ファイルを選択** ボタンがあるため、ユーザーは混乱する可能性があります。

        ![gl-ar750s old Uboot version](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/gl-ar750s_firmware_update_page_of_old_uboot_version.png){class="glboxshadow" width="700"}

        1. 事前にUbootファイルを [ここから](https://github.com/gl-inet/uboot-for-qca95xx/tree/master/bin){target="_blank"} ダウンロードしておく必要があります。

        2. Uboot Web UIにアクセスできるようになるまで、上記の手順を繰り返します。

        3. ブラウザを使用して **http://192.168.1.1/uboot.html** にアクセスします

            ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

        4. **ファイルを選択**ボタンをクリックし、ダウンロードしたUbootファイルを選択します。

        5. **U-Bootの更新**ボタンをクリックします。

        6. アップデートには数分かかります。アップデートに成功すると、ルーターが再起動します。

        7. この時、ステップ4に戻りIP設定を変更し、ウェブ管理パネルにアクセスしてみてください。ウェブ管理パネルに正常にアクセスできれば、ルーターが再起動されたことを意味します。

        8. 上記の手順を繰り返してファームウェアをアップグレードします。Ubootバージョンが正常に更新されると、ステップ5でUboot Web UIが変更されたことが確認できます。

6. **ファイルを選択** ボタンをクリックして、ファームウェア ファイルを見つけます。 次に、**ファームウェアの更新** ボタンをクリックします。

7. 約3分間待ちます。アップデート中はデバイスの電源を切らないでください。電源とWi-Fi LEDの両方が点灯している場合、またはデバイスでSSIDを確認できる場合、ルーターの準備は完了です。

8. ステップ4で行ったIP設定を元に戻し、デバイスをルーターのLANまたはWi-Fiに接続します。再び**192.168.8.1**でルーターにアクセスできるようになります。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
