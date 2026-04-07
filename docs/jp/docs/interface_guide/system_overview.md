# システム概要

Web管理パネルの左側で、**SYSTEM** -> **Overview** に移動します。

Overview ページには一部のハードウェア状態が表示され、次のような簡単な操作も行えます。

- CPU、メモリ、フラッシュ、外部ストレージデバイスの状態
- ファン、バッテリーなどのハードウェアの状態
- LED とファンの制御
- デバイス情報

以下は GL-MT3000 の例です。

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## CPU平均負荷

ファンのないほとんどのモデルでは、CPU Average Load は以下のように表示されます。

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

一部のファン内蔵モデルでは、CPU Average Load は以下のように表示されます。

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

グラフにマウスカーソルを合わせると、具体的な値を確認できます。

右側の温度表示をクリックすると、摂氏と華氏を切り替えられます。

右上の Fan アイコンをクリックすると、Fan Settings に入れます。

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Models with Built-in Fans"

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

グラフにマウスカーソルを合わせると、具体的な値を確認できます。

**Note**: ここに表示されるメモリは Linux システムで利用可能なメモリです。一部は Wi-Fi サブシステムやその他のブート領域に割り当てられるため、ここに表示される合計メモリは物理メモリより少なくなります。

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

歯車アイコンをクリックすると、LED の [Scheduled Tasks](scheduled_tasks.md) ページへ移動します。

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

システムで使用中、アプリで使用中、残りの利用可能容量を含む、合計 Flash メモリが表示されます。

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## デバイス情報

このセクションには、デバイスの基本情報が表示されます。

Device ID、device MAC、device S/N は、ファームウェア v4.7 以降で追加されました。

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## 外部ストレージ

このセクションは v4.5 以降で利用でき、USB Disk の合計容量と利用可能容量が表示されます。

ファームウェア v4.7 以降では、一部モデルで USB プロトコルの切り替えをサポートしています。

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

ご不明な点がありましたら、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
