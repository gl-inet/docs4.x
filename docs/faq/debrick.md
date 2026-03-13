# U-Bootを使用してルーターをデブリックする

DIYプロジェクトを行っていたり、間違ったファームウェアをフラッシュしたりした場合、ルーターがブリックしてしまう可できる性があります。その場合、U-Bootフェイルセーフを使用してファームウェアを再インストールできます。

**注意:** U-Boot操作により、ルーターの設定とインストールされているプラグインが削除されます。

---

## 準備

イーサネットポートを備えたコンピュータをご用意ください。コンピュータにイーサネットポートがない場合は、追加のUSBイーサネットアダプターをご用意ください。

## デブリック手順

で下のビデオチュートリアルを参照するか、で下の手順に従ってU-Boot Web UIにアクセスし、ファームウェアを再インストールしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>U-Bootを使用してファームウェアを再インストールするステップはほとんど same じであり、このビデオではMudi/Mudi V2を例にしています。彼のモデルについては、で下の手順に従ってください。</small>

1. [ここから](https://dl.gl-inet.com/){target="_blank"}ファームウェアをコンピュータにダウンロードしてください。

    一部のモデル（GL-AR750S-EXTなど）は2つの形式のファームウェアで利用可できるです。U-Boot用のファームウェアを使用し、ファイル名拡張子は**.img**です。

2. ルーターの電源を切ります。コンピュータをルーターの**イーサネットLANポート**に接続します。**必ず**彼のすべてのポートは**未接続**のままにしておきます。

    !!! 注意

        一部のモデルでは、特定のLANポートとWANポートは入れ替え可できるです。このLANポートを使用しないでください。例えば、GL-MT6000 (Flint 2)では、LAN 1を使用しないでください。LAN 2、LAN 3、またはLAN 4を使用してください。

3. リセットボタンを**押さえながら**、 same 時にルーターの電源を入れます。ルーターに電源ボタンがない場合は、電源を差し込むとから動のに電源が入ります。

    LEDが規則のなシーケンスで数回時滅するのが見えます。シーケンスが変わった後**指を放してください**。

    で下は各モデルのLED時滅シーケンスの説明です。

    **注意:**  same じルーターモデルでも製造年月日が異なると、LEDの色や時滅順序が異なる場合がありますが、U-Bootプロセスには影響しません。時滅するLEDの変化にご注目ください。

    - **GL-BE9300(Flint 3)**の場合、青色LEDが6回時滅し、その後白色に時灯します。
    
    - **GL-BE3600(Slate 7)**の場合、リセットボタンを約5秒間押し続けると、LEDディスプレイに5秒間のカウントダウンが表示されます。画面に次のステップが表示されるまでリセットボタンを押し続けてください：

        1. コンピュータのIPアドレスを192.168.1.2に設定
        2. ブラウザでhttp://192.168.1.1にアクセス

        手順4に進んでください。

    - **GL-B3000(Marble)**の場合、青色LEDが7回時滅し、その後白色に時灯します。

    - **GL-MT6000(Flint 2)**の場合、青色LEDが6回時滅し、その後白色に時灯します。

    - **GL-MT3000(Beryl AX)**の場合、青色LEDが6回時滅し、その後白色に時灯します。

    - **GL-MT2500/GL-MT2500A(Brume 2)**の場合、青色LEDが5回時滅し、その後白色に時灯します。

    - **GL-S200**の場合、シアン色LEDが5回時滅し、その後短時間に紫色に変わり、その後シアン色に時灯します。

    - **GL-A1300(Slate Plus)**の場合、LEDがゆっくり5回時滅し、その後短時間時灯し、その後常に速く時滅します。

    - **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)**, **microuter-N300**の場合、LEDが5回時滅します。

    - **GL-E750(Mudi)**の場合、画面には最も初に「Booting」、次に「Reset Counting 1 to 4」、最も後に「Please Open Web 192.168.1.1」と表示されます。

    - **GL-S1300(Convexa-S)**と**GL-B1300(Convexa-B)**の場合、LEDが4回時滅します。
        
        一番左の電源LEDはずっと時灯し続ける可できる性があり、右端のWi-Fi LEDが4回時滅し、その後中央のMesh LEDが時灯し続けます。
        
       （一古いGL-B1300では、左端の電源LEDはずっと時灯し続ける可できる性があり、中央のLEDと右端のLEDが same 時に5回時滅し、その後時灯し続けます。）

    - **GL-SF1200**の場合、5G LEDが5回時滅し、その後時灯し続けます。

    - **GL-AX1800(Flint)**の場合、青色LEDが5回時滅し、その後白色に時灯します。

    - **GL-AXT1800(Slate AX)**の場合、青色LEDが5回時滅し、その後時灯し続けます。

    - **GL-XE300(Puli)**の場合、LAN LEDが5回時滅し、その後Wi-Fi LEDが時灯し続けます。

    - **GL-X300B(Collie)**の場合、WAN LEDが5回時滅し、その後Wi-Fi LEDが時灯し続けます。

    - **GL-X3000(Spitz AX)**の場合、WAN LEDが5回時滅し、その後Wi-Fi LEDが時灯し続けます。

    - **GL-XE3000(Puli AX)**の場合、WAN LEDが5回時滅し、その後Wi-Fi LEDが時灯し続けます。

    - **GL-SFT1200(Opal)**の場合、青色LEDが5回時滅し、その後白色に時灯します。

    - **GL-AP1300(Cirrus)**の場合、電源LEDがゆっくり5回時滅し、その後短時間時灯し、その後常に速く時滅します。

    - **GL-MT1300(Beryl)**の場合、LEDは最も初青色で、ゆっくり2回時滅し、その後より速く5回時滅して白色に時灯します。

    - **GL-B2200(Velica)**の場合、2つのLEDは最も初青色で、次に白色に変わり5回時滅、その後青色に時灯します。

    - **GL-MV1000/GL-MV1000W(Brume)**の場合、LED時滅の繰り返しシグナルはありません。（電源とWAN LEDはずっと時灯し続けます。）

    - **GL-MiFi**の場合、LEDが6回時滅します。

    - **GL-MT300N**, **GL-MT300A**の場合、LEDが3回時滅します。

4. コンピュータのIPアドレスを**192.168.1.2**に手動で設定します。で下は異なるオペレーティングシステムごとのステップバイステップガイドです：

    ??? "Windows 7 / Windows 10"

        1. **コントロールパネル** -> **ネットワークとインターネット** -> **ネットワークと共有センター** -> ** adapter設定の変より**に移動します。

        2. **ローカルエリア接続**を右クリック -> **プロパティ**。

        3. **インターネットプロトコルバージョン4 (TCP/IPv4)**をクリック -> **プロパティ**。

        4. **IPアドレス**を`192.168.1.2`に手動で設定します。

        5. **サブネットマスク**を`255.255.255.0`に設定します。

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. **OK**ボタンをクリックします。

    ??? "Windows 11"

        1. 設定を開きます。

        2. **ネットワークとインターネット**をクリックします。

        3. **イーサネット**タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. 「IP割り当て」セクションで、**編集**ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. **手動**オプションを選択します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. **IPv4**トグルスイッチをオンにします。

        7. 静の**IPアドレス**を**192.168.1.2**に設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. **サブネットマスク**を**255.255.255.0**に設定します。

        9. **保存**ボタンをクリックします。

    ??? "macOS"
    
        1. 画面左上の**Apple**アイコンをクリックし、**システム環境設定**を選択します。

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        2. **ネットワーク**をクリックします。

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        3. 左側の**イーサネット**をクリックし、**IPv4の設定**の横にあるドロップダウンボックスをクリックして**手動**を選択します。USBイーサネットアダプターを使用している場合、イーサネットが見つからず、USBイーサネットアダプターの名前として表示される場合があります。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        4. **IPv4アドレス**を`192.168.1.2`、**サブネットマスク**を`255.255.255.0`、**ルーター**を`192.168.1.1`に入力し、右下の適用ボタンをクリックします。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. ブラウザで**http://192.168.1.1**にアクセスします。これはU-Boot Web UIです。

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}
    
    !!! 注意 
    
        - U-Boot Web UIにアクセスできない場合、実行中のVPNまたはプロキシソフトウェアがあるか確認してください。TailscaleやZeroTierを含むすべてのVPNまたはプロキシソフトウェアを無効にしてください。
    
        - 上記のU-Boot Web UIは、U-Bootのバージョンが異なるため、見たものとまったく same じではない場合があります。場合によっては、U-Bootバージョンをアップグレードすることをお勧めします。[ここ](upgrade_uboot_version.md)にあるチュートリアルを参照してください。

6. **ファイルを選択**ボタンをクリックしてファームウェアファイルを見つけます。次に、**ファームウェアをアップデート**ボタンをクリックします。

7. 約3分間待ちます。アップデート中はデバイスの電源を切らないでください。電源とWi-Fi LEDの両方が時灯している場合、またはデバイスでSSIDを確認できると、ルーターの準備が完たしています。

8. 手順4で行ったIP設定を元に戻し、デバイスをルーターのLANまたはWi-Fiに接続します。**192.168.8.**でルーターに もう一度アクセスできるようになります。

    **注意:** ルーターにアクセスするには、シークレットモードを使用するか、ブラウザのキャッシュとCookieを削除する必要がある場合があります。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
