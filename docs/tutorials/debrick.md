# Uboot を使用してルーターをデブリックする

DIYをしたり、間違ったファームウェアをフラッシュした場合、ルーターがブリックした可能性があります。ルーターにアクセスできないかもしれませんが、Ubootフェイルセーフを使用してファームウェアを再インストールすることができます。

**注::** Uboot操作により、ルーターの設定やインストールされているプラグインが削除されます。

---

イーサネットポートのあるPCをご用意ください。ない場合は、USBイーサネットアダプターを別途ご用意ください。

以下の手順でUboot Web UIにアクセスし、ファームウェアを再インストールしてください。

また、以下のビデオチュートリアルもご参照ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/EAaaw8nyrnE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. ファームウェアをパソコンにダウンロードしてください。[ここ](https://dl.gl-inet.com/){target="_blank"}  

    GL-AR750S-EXTなど一部の機種では、2種類の形式のファームウェアが用意されていますが、uboot用のファームウェアは、ファイル名の拡張子が**.img**となっていますので、そちらをご利用ください。

2. ルーターの電源を抜きます。お使いのコンピュータをルーターの**イーサネットポート（LANまたはWANのいずれか）**に接続します。あなたは**他のポートを**未接続のままにしておく必要があります**。

3. リセットボタンをしっかりと押し続けてから、ルーターの電源を入れます。ルーターに電源ボタンがない場合は、電源を差し込むと自動的に電源が入ります。

    その後、規則的なパターンで数回ライトが点滅するのが見えますが、パターンが変わった後に指を放してください。

    以下、各機種の発光パターンについて説明する。

    **注: ** 別の製造業の日付の同じルーター モデルは異なった LED ライト色か点滅のパターンがあるかもしれません、それは UBoot プロセスに影響を与えません。点滅パターンの変更にもっと注意を払ってください。


    -  **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)**, **GL-E750(Mudi)**, **microuter-N300**が4回点滅します

    -  **GL-S1300(Convexa-S), GL-B1300(Convexa-B)**が4回点滅します
        
        一番左のLEDがずっと点灯し続け、右端のLEDが4回点滅すると、真ん中のLEDが点灯して点灯したままになります。
        
        (一部の古いGL-B1300では、一番左のLEDがずっと点灯し、真ん中のLEDと一番右のLEDが同時に5回点滅した後、点灯したままになります)。

    - **GL-SF1200**の場合、5G LEDが5回点滅した後、点灯したままになります。

    - **GL-AX1800(Flint)**の場合、青色ランプが5回点滅した後、白色に変わり、点灯したままになります。

    - **GL-AXT1800(Slate AX)**の場合、青ランプが5回点滅した後、点灯したままになります。

    - **GL-XE300(Puli)**の場合、LANランプが5回点滅し、WIFIランプが点灯したままとなります。

    - **GL-X300B(Collie)**の場合、WANライトは5回点滅し、WIFIライトは点灯したままです。

    - **GL-SFT1200(Opal)**の場合、青色ランプが5回点滅した後、白色に変化し、点灯したままになります。

    - **GL-MT1300（Beryl）**の場合、LEDは最初青色で、ゆっくり2回点滅し、その後少し早く5回点灯して白色に変わり、点灯したままになります。

    - **GL-B2200(Velica)**の場合、2つのLEDは最初青色で、その後白色に変わり5回点滅し、その後青色に変わり点灯し続けます。

    - **GL-MV1000**の場合、リピートLEDの点滅信号はありません。(電源とWANのLEDはずっと点灯しています）。

4. お使いのコンピュータのIPアドレスを手動で**192.168.1.2**に設定してください。以下、OS別の手順ガイドをご確認ください。

    ??? "Windows 7 / Windows 10"

        1. **コントロール パネル** -> **ネットワークとインターネット** -> **ネットワークと共有センター** -> **アダプター設定の変更**に移動します。

        2. **ローカルエリア接続**を右クリック -> **プロパティ**をクリックします。

        3.  **インターネットプロトコルバージョン4（TCP/IPv4）** -> **プロパティ**をクリックします。

        4. **IP アドレス**を手動で  `192.168.1.2` に設定します。

        5. **サブネット マスク** を`255.255.255.0`に設定します。

            ![ipv4 properties](https://static.gl-inet.com/docs/en/2.x/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6.  **OK** ボタンをクリックします。

    ??? "Windows 11"

        1. 設定を開きます。

        2.  **ネットワーク & インターネット**をクリックします。

        3.  **イーサネット** タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. "IP設定"セクションで、**編集**ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5.  **マニュアル** を選択します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. **IPv4トグル** スイッチをオンにします。

        7. 静的 **IPアドレス**を**192.168.1.2**に設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. **サブネットマスク** を **255.255.255.0**と指定します。

        9. **保存** ボタンをクリックします。

    ??? "macOS"

        1. システム環境設定 -> ネットワークを選択します。

        2. イーサネット -> 詳細設定-> TCP/IPを選択します。

        3. IPv4設定、手動 を選択します。
        4. IPv4 アドレスを 192.168.1.2 に手動で設定します。

5. ブラウザで**http://192.168.1.1**にアクセスしてください。これはUbootのWeb UIです。

    ![Uboot web ui](https://static.gl-inet.com/docs/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **注意:** Uboot のバージョンは製造日によって異なるため、上記の Uboot Web UI は実際に表示されているものとまったく同じではない場合があります。 場合によっては、Uboot のバージョンをアップグレードすることをお勧めします。 以下のチュートリアルを参照してください。

    ??? "Ubootのバージョンをアップグレードする"

        Ubootのバージョンが古すぎたり、そのWeb UIがユーザーにとってわかりにくいものもありますので、Ubootのバージョンアップをお勧めします。

        たとえば、次の図は、古い Uboot バージョンの GL-AR750S の Web UI を示しています。 [ファイルを選択] ボタンが 2 つあるため、ユーザーが混乱する可能性があります。

        ![gl-ar750s old Uboot version](https://static.gl-inet.com/docs/en/4/tutorials/debrick/gl-ar750s_firmware_update_page_of_old_uboot_version.png){class="glboxshadow" width="700"}

        1. 事前に [こちら](https://github.com/gl-inet/uboot-for-qca95xx/tree/master/bin){target="_blank"} からUbootファイルをダウンロードしておく必要があります。

        2. Uboot Web UIにアクセスできるようになるまで、上記の手順を繰り返します。

        3. ブラウザで**http://192.168.1.1/uboot.html**にアクセスしてください。

            ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

        4. **ファイルを選択する** ボタンをクリックし、先ほどダウンロードしたUbootファイルを選択します。

        5. **U-Bootのアップデート** ボタンをクリックします。

        6. アップデートには数分かかります。アップデートに成功すると、ルーターが再起動します。

        7. この時、手順4でIP設定を元に戻して、Web管理パネルにアクセスしてみてください。Web管理パネルに正常にアクセスできれば、ルーターが再起動されたことを意味します。

        8. 上記の手順を繰り返し、ファームウェアをバージョンアップします。Ubootのバージョンアップに成功すると、手順5でUbootのWeb UIが変更されたことが確認できます。 

6.  **ファイルを選択する**ボタンをクリックして、ファームウェアファイルを探します。 **ファームウェアの更新** ボタンをクリックします。

7. 3分程度お待ちください。アップデート中は端末の電源を切らないでください。電源とWi-Fi LEDの両方が点灯している場合、またはデバイスにルーターのSSIDが表示されている場合は、ルーターの準備が完了しています。

8. 手順4で行ったIP設定を元に戻し、端末をルーターのLANまたはWi-Fiに接続します。再び**192.168.8.1**経由でルーターにアクセスできるようになります。
