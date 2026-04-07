# U-Bootを使用してルーターをデブリックする

DIYプロジェクトや誤ったファームウェアのフラッシュによってルーターがブリックしてしまった場合、U-Bootフェイルセーフを使用してファームウェアを再インストールできます。

**注意:** U-Boot操作により、ルーターの設定とインストールされているプラグインが削除されます。

---

## 準備

イーサネットポートを備えたコンピュータまたはノートパソコンをご用意ください。コンピュータにイーサネットポートがない場合は、追加のUSBイーサネットアダプターが必要です。

**注意**: GL-E5800 (Mudi 7) は現在、U-Boot経由でのファームウェアフラッシュに対応していません。

## デブリック手順

以下のビデオチュートリアルを参照するか、以下の手順に従ってU-Boot Web UIにアクセスし、ファームウェアを再インストールしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>U-Bootを使用したファームウェア再インストールの手順はほぼ同じです。このビデオではMudi/Mudi V2を例にしています。他のモデルについては、以下の手順に従ってください。</small>

1. U-Bootファームウェアを[ここから](https://dl.gl-inet.com/){target="_blank"}コンピュータにダウンロードしてください。

    一部のモデルでは2つのファームウェアバリアントが提供されています。U-Boot対応ファームウェアをダウンロードしてください。

2. ルーターの電源を切ります。コンピュータをルーターの**イーサネットLANポート**に接続し、他のすべてのポートは接続しないでください。

    !!! note

        一部のモデルでは、特定のLANポートをWANに切り替えることができます。ファームウェアフラッシュにはこのLANポートを使用しないでください。例えば、GL-MT6000 (Flint 2)では、LAN 1を使用せず、LAN 2、LAN 3、またはLAN 4を使用してください。

3. リセットボタンをしっかりと押したまま、**同時にルーターの電源を入れます**。ルーターに電源ボタンがない場合は、電源を差し込むと自動的に電源が入ります。

    LEDが規則的なシーケンスで数回点滅します。点滅パターンが変わった**後に**リセットボタンを離してください。

    !!! note "デバイスモデルごとのLED点滅パターン"

        **注意:** 同じルーターモデルでも製造バッチが異なると、LEDの色や点滅シーケンスが異なる場合があります。これはU-Bootリカバリープロセスには影響しません。LED点滅状態の変化に注目してください。

        - **GL-MT3600BE (Beryl 7)**の場合: 青色LEDが7回点滅し、その後白色に点灯します。
        
        - **GL-MT5000 (Brume 3)**の場合: 電源LEDが青色で7回点滅し、その後白色に点灯します。

        - **GL-BE6500 (Flint 3e)**の場合: 青色LEDが6回点滅し、その後白色に点灯します。
        
        - **GL-BE9300 (Flint 3)**の場合: 青色LEDが6回点滅し、その後白色に点灯します。
        
        - **GL-BE3600 (Slate 7)**の場合: リセットボタンを約5秒間押し続けると、タッチスクリーンに5秒間のカウントダウンが表示されます。次のプロンプトが画面に表示されるまでリセットボタンを押し続けてください。例：コンピュータのIPアドレスを192.168.1.2に手動で設定し、ブラウザでhttp://192.168.1.1にアクセスしてください。詳細な手順については手順4に進んでください。

        - **GL-X2000 (Spitz Plus)**の場合: インターネットLEDが5回点滅し、その後Wi-Fi LEDが点灯し続けます。

        - **GL-B3000 (Marble)**の場合: 青色LEDが7回点滅し、その後白色に点灯します。

        - **GL-MT6000 (Flint 2)**の場合: 青色LEDが6回点滅し、その後白色に点灯します。

        - **GL-MT3000 (Beryl AX)**の場合: 青色LEDが6回点滅し、その後白色に点灯します。

        - **GL-MT2500/GL-MT2500A (Brume 2)**の場合: 電源LEDが青色で5回点滅し、その後白色に点灯します。

        - **GL-X3000 (Spitz AX)**の場合: インターネットLEDが5回点滅し、その後Wi-Fi LEDが点灯し続けます。

        - **GL-XE3000 (Puli AX)**の場合: インターネットLEDが5回点滅し、その後Wi-Fi LEDが点灯し続けます。
            
        - **GL-XE300 (Puli)**の場合: LAN LEDが5回点滅し、その後Wi-Fi LEDが点灯し続けます。

        - **GL-E750 (Mudi)**の場合: 画面には最初に「Booting」、次に「Reset Counting 1 to 4」、最後に「Please Open Web 192.168.1.1」と表示されます。

        - **GL-X750 (Spitz)**の場合: インターネットLEDが5回点滅し、その後Wi-Fi LEDが点灯し続けます。

        - **GL-AX1800 (Flint)**の場合: 青色LEDが5回点滅し、その後白色に点灯します。

        - **GL-AXT1800 (Slate AX)**の場合: 青色LEDが5回点滅し、その後白色に点灯します。

        - **GL-SFT1200 (Opal)**の場合: 青色LEDが5回点滅し、その後白色に点灯します。

        - **GL-MT1300 (Beryl)**の場合: 青色LEDがゆっくり2回点滅し、その後5回速く点滅して白色に点灯します。

        - **GL-A1300 (Slate Plus)**の場合: LEDがゆっくり5回点滅し、その後短時間点灯し、その後常に速く点滅します。

        - **GL-MT300N-V2 (Mango)** および **GL-AR300M (Shadow)**の場合: LEDが5回点滅します。 

        - **GL-X300B (Collie)**の場合: WAN LEDが5回点滅し、その後Wi-Fi LEDが点灯し続けます。

        - **GL-AP1300 (Cirrus)**の場合: 電源LEDがゆっくり5回点滅し、その後短時間点灯し、その後常に速く点滅します。

        - **GL-B1300 (Convexa-B)** および **GL-S1300 (Convexa-S, EOL)**の場合: LEDが4回点滅します。
            
            左端の電源LEDは常に点灯したままで、右端のWi-Fi LEDが4回点滅し、その後中央のMesh LEDが点灯し続けます。
            
            （一部の古いGL-B1300では、左端の電源LEDは常に点灯したままで、中央のLEDと右端のLEDが同時に5回点滅し、その後点灯し続けます。）

        - **GL-B2200 (Velica)**の場合: 2つのLEDは最初青色で、次に白色に変わり5回点滅し、その後青色に点灯します。

        - **GL-SF1200**の場合: 5G LEDが5回点滅し、その後点灯し続けます。

        - **GL-S200**の場合: シアン色LEDが5回点滅し、その後短時間紫色に変わり、その後シアン色に点灯します。
        
        - **GL-AR750 (Creta)** および **GL-AR750S-EXT (Slate)**の場合: LEDが5回点滅します。 
        
        - **GL-USB150 (Microuter)**、**microuter-N300** および **GL-AR150 (White)**の場合: LEDが5回点滅します。

        - **GL-MV1000/GL-MV1000W (Brume)**の場合: LED点滅の繰り返しシグナルはありません。電源およびWAN LEDは常に点灯したままです。
        
        - **GL-MiFi**の場合: LEDが6回点滅します。

        - **GL-MT300N** および **GL-MT300A**の場合: LEDが3回点滅します。

4. コンピュータのIPアドレスを**192.168.1.2**に手動で設定します。以下は異なるオペレーティングシステムごとのステップバイステップガイドです：

    ??? "Windows 7 / Windows 10"

        1. **コントロールパネル** -> **ネットワークとインターネット** -> **ネットワークと共有センター** -> **アダプター設定の変更**に移動します。

        2. **ローカルエリア接続**を右クリック -> **プロパティ**。

        3. **インターネットプロトコルバージョン4 (TCP/IPv4)**をクリック -> **プロパティ**。

        4. **IPアドレス**を`192.168.1.2`に手動で設定します。

        5. **サブネットマスク**を`255.255.255.0`に設定します。

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. **OK**ボタンをクリックします。

    ??? "Windows 11"

        7. 設定を開きます。

        8. **ネットワークとインターネット**をクリックします。

        9. **イーサネット**タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. 「IP割り当て」セクションで、**編集**ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. **手動**オプションを選択します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. **IPv4**トグルスイッチをオンにします。

        13. 固定**IPアドレス**を**192.168.1.2**に設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. **サブネットマスク**を**255.255.255.0**に指定します。

        15. **保存**ボタンをクリックします。

    ??? "macOS"
    
        16. 画面左上の**Apple**アイコンをクリックし、**システム環境設定**を選択します。

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. **ネットワーク**をクリックします。

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. 左側の**イーサネット**をクリックし、**IPv4の設定**の横にあるドロップダウンボックスをクリックして**手動**を選択します。USBイーサネットアダプターを使用している場合、イーサネットが見つからず、USBイーサネットアダプターの名前として表示される場合があります。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. **IPv4アドレス**に`192.168.1.2`、**サブネットマスク**に`255.255.255.0`、**ルーター**に`192.168.1.1`を入力し、右下の適用ボタンをクリックします。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. ブラウザで**http://192.168.1.1**にアクセスします。これはU-Boot Web UIです。

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}
    
    !!! Note 
    
        - U-Boot Web UIにアクセスできない場合は、実行中のVPNまたはプロキシソフトウェアがないか確認してください。TailscaleやZeroTierを含む、すべてのVPNまたはプロキシソフトウェアを無効にしてください。
    
        - 上記のU-Boot Web UIは、製造日によってU-Bootバージョンが異なるため、実際に表示されるものと完全に同じではない場合があります。極端な場合には、U-Bootバージョンのアップグレードをお勧めします。[こちら](upgrade_uboot_version.md)のチュートリアルを参照してください。

6. **ファイルを選択**ボタンをクリックしてファームウェアファイルを見つけます。次に、**ファームウェアをアップデート**ボタンをクリックします。

7. 約3分間待ちます。ファームウェアアップデート中はデバイスの電源を切らないでください。

    LEDが青色に点滅し続けている場合、ルーターの準備ができています。一部のセルラーモデルでは、電源およびWi-Fi LEDの両方が点灯している場合に準備完了です。

8. 手順4で行ったIP設定を元に戻し、コンピュータをルーターのLANまたはWi-Fiに接続します。**192.168.8.1**でルーターのWeb管理パネルに再度アクセスできるようになります。

    **注意:** ルーターにアクセスするには、シークレットモードを使用するか、ブラウザのキャッシュとCookieを削除する必要がある場合があります。

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
