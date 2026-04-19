# UBootバージョンのアップグレード

## 警告

**U-Bootのアップグレードは非常に危険であり、一般的には推奨されません。失敗すると、デバイスがブリックされ、復元する方法がありません。必要な場合、またはGL.iNetサポートから指示された場合のみ実行してください**。

**アップグレード中に電源をオフにしないでください。アップグレードが失敗し、デバイスがブリックされる可能性があります**。

## 準備

- イーサネットポート付きのコンピュータ。ない場合は、追加のUSBイーサネットアダプターを準備してください。
- イーサネットケーブル。
- GL.iNetサポートスタッフの指示に従ってUbootファイルをダウンロードしてください。正しいubootファイルを使用していることを確認してください。Ubootファイルのダウンロード方法がわからない場合は、support@gl-inet.comまでメールでお問い合わせください。

## アップグレード手順

U-Bootアップグレードページにアクセスするには、以下の手順に従ってください。

1. ルーターの電源を切ります。コンピュータをルーターの**イーサネットLANポート**に接続します。他のすべてのポートは接続**しない**でください。

    !!! note

        一部のモデルでは、特定の LAN ポートと WAN ポートを入れ替えて使用できます。この LAN ポートは使用しないでください。たとえば GL-MT6000 (Flint 2) では LAN 1 を使用せず、LAN 2、LAN 3、または LAN 4 を使用してください。

2. リセットボタンをしっかりと押したまま、同時にルーターの電源を入れます。ルーターに電源ボタンがない場合は、電源を差し込むと自動的に電源が入ります。

    その後、LEDが数回規則的に点滅します。シーケンスが変わったら指を離してください。
    
3. コンピュータのIPアドレスを手動で**192.168.1.2**に設定します。以下は異なるOSごとのステップバイステップガイドです：

    ??? "Windows 7 / Windows 10"

        1. **コントロールパネル** -> **ネットワークとインターネット** -> **ネットワークと共有センター** -> **アダプター設定の変更**に移動します。

        2. **ローカルエリア接続**を右クリック -> **プロパティ**。

        3. **インターネットプロトコルバージョン4 (TCP/IPv4)** -> **プロパティ**をクリックします。

        4. **IPアドレス**を手動で`192.168.1.2`に設定します。

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

        18. 左側で**イーサネット**をクリックし、**IPv4の設定**の横にあるドロップダウンをクリックして**手動**を選択します。USBイーサネットアダプターを使用している場合、イーサネットが見つからず、USBイーサネットアダプターの名前として表示される場合があります。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. **IPv4アドレス**に`192.168.1.2`、**サブネットマスク**に`255.255.255.0`、**ルーター**に`192.168.1.1`を入力し、右下の適用ボタンをクリックします。

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4. **Google Chrome または Microsoft Edge を使って `http://192.168.1.1/uboot.html` にアクセスします**。キャッシュされた候補で誤ったアドレスが開かないよう、URL は必ず最後まで入力してください。

    **Mozilla Firefox は使用しないでください。ルーターがブリックする可能性があります。**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5. **ファイルを選択**ボタンをクリックし、ダウンロードしたUbootファイルを選択します。

6. **U-Bootをアップデート**ボタンをクリックします。アップグレード中に電源をオフにしないでください。アップデートには数分かかります。

7. アップデートが成功すると、ルーターが再起動します。この時点で、手順3のIP設定を元に戻し、**192.168.8.1**経由でWeb管理パネルにアクセスしてみてください。Web管理パネルに正常にアクセスできる場合は、ルーターが再起動したことを意味します。

    **注意:** ルーターにアクセスするには、シークレットモードを使用するか、ブラウザのキャッシュとCookieを削除する必要がある場合があります。

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}を訪問してください。
