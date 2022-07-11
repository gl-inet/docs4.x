# Uboot を使用してルーターをデブリックする

DIYをしたり、間違ったファームウェアをフラッシュした場合、ルーターがブリックした可能性があります。ルーターにアクセスできないかもしれませんが、Ubootフェイルセーフを使用してファームウェアを再インストールすることができます。

**注::** Uboot操作により、ルーターの設定やインストールされているプラグインが削除されます。

---

イーサネットポートのあるPCをご用意ください。ない場合は、USBイーサネットアダプターを別途ご用意ください。

以下の手順でUboot Web UIにアクセスし、ファームウェアを再インストールしてください。

また、以下のビデオチュートリアルもご参照ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/EAaaw8nyrnE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1.ファームウェアをパソコンにダウンロードしてください。[ここ](https://dl.gl-inet.com/){target="_blank"}  

    GL-AR750S-EXTなど一部の機種では、2種類の形式のファームウェアが用意されていますが、uboot用のファームウェアは、ファイル名の拡張子が**.img**となっていますので、そちらをご利用ください。

2.ルーターの電源を抜きます。お使いのコンピュータをルーターの**イーサネットポート（LANまたはWANのいずれか）**に接続します。あなたは**他のポートを**未接続のままにしておく必要があります**。

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

        1. Go to **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Right click **Local Area Connection** -> **Properties**.

        3. Click **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Set the **IP adress** to `192.168.1.2` manually.

        5. Set the **Subnet mask** to `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/en/2.x/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Click the **OK** button.

    ??? "Windows 11"

        1. Open Settings.

        2. Click on **Network & Internet**.

        3. Click the **Ethernet** tab.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. Under the "IP settings" section, click the **Edit** button.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Select the **Manual** option.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Turn on the **IPv4 toggle** switch.

        7. Set the static **IP address** as **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Specify the **Subnet mask** as **255.255.255.0**.

        9. Click the **Save** button.

    ??? "macOS"

        1. Go to System Preferences -> Network.

        2. Chooose Ethernet -> Advanced -> TCP/IP.

        3. In Configure IPv4, choose Manually.

        4. Set the IPv4 Address to 192.168.1.2 manually.

5. Use browser to visit **http://192.168.1.1**, this is the Uboot Web UI.

    ![uboot web ui](https://static.gl-inet.com/docs/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Note:** The uboot Web UI above may not be exactly the same as what you see, because the Uboot version is different for different production dates. In some cases, we recommend upgrading the Uboot version. Please refer to the tutorial below.

    ??? "Upgrade the Uboot version"

        Some Uboot versions are too old or its Web UI is not easy for users to understand, so we recommend upgrading the Uboot version.

        For example, the following figure shows the Web UI of the old Uboot version of GL-AR750S. It has two **Choose file** buttons, which can be confusing for users.

        ![gl-ar750s old uboot version](https://static.gl-inet.com/docs/en/4/tutorials/debrick/gl-ar750s_firmware_update_page_of_old_uboot_version.png){class="glboxshadow" width="700"}

        1. You need to download the uboot file [here](https://github.com/gl-inet/uboot-for-qca95xx/tree/master/bin){target="_blank"} in advance.

        2. Repeat the above steps until you can access the uboot FIRMWARE UPDATE page.

        3. Use browser to visit **http://192.168.1.1/uboot.html**

            ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

        4. Click the **Choose file** button and choose the uboot file you just downloaded.

        5. Click **Update U-Boot** button.

        6. It will take several minutes to update. After a successful update, it will reboot the router.

        7. At this time you can change the IP setting back in step 4 and try to access the web Admin Panel, if you can access the web Admin Panel normally, it means the router has been rebooted.

        8. Repeate the above steps to upgrade the firmware. If the uboot version is updated successfully, you will see that the uboot FIRMWARE UPDATE page has changed at step 5. 

6. Click **Choose file** button to find the firmware file. Then click **Update firmware** button.

7. Wait for around 3 minutes. Don’t power off your device when updating. The router is ready when both power and  Wi-Fi LED are on or you can find its SSID on your device.

8. Revert the IP setting you did in step 4 and connect your device to the LAN or Wi-Fi of the router. You will be able to access the router via **192.168.8.1** again.
