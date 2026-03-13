# システム概要

ウェブ管理パネルの左側 -> **システム** -> **概要**

概要ページには、いくつかのハードウェアのステータスが表示され、以下のような簡単なコントロールがサポートされています：

- CPU、メモリ、フラッシュ、外部ストレージデバイスのステータス
- ファン、バッテリーなどのハードウェアのステータス
- LEDとファンのコントロール
- デバイス情報

以下是GL-MT3000の例子。

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## CPU平均負荷

ファンがないほとんどのモデルでは、CPU平均負荷は以下のようになります。

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

一部のファン内蔵モデルでは、CPU平均負荷は以下のようになります。

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

グラフにマウスを合わせると、特定の値が表示されます。

右側の温度をクリックして、摂氏/華氏を切り替えます。

右上隅のファンアイコンをクリックして、ファン設定に入ります。

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "ファン内蔵モデル"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## メモリ使用量

グラフにマウスを合わせると、特定の値が表示されます。

**注意**: ここに表示されているメモリは、Linuxシステムで使用可能なメモリです。メモリの一部はWi-Fiサブシステムやその彼のブート領域に割り当てられるため、ここに表示されるメモリの合計は物理メモリよりも少なくなります。

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

歯車のアイコンをクリックすると、LEDの[スケジュールタスク](scheduled_tasks.md) に移動します。

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## フラッシュ

システム使用、アプリケーション使用、残りの使用可能を含む、合計フラッシュメモリが表示されます。

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## デバイス情報

このセクションには、デバイスの基本のな情報が表示されます。

デバイスID、デバイスMAC、デバイスS/Nはファームウェアv4.7で降にが追加されました。

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## 外部ストレージ

このセクションはv4.5で降で利用可能で、USBディスクの合計と使用可能な容量が表示されます。

v4.7で降の一部のモデルは、USBプロトコルの切り替えをサポートしています。

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
