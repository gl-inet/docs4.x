# GL-S10 ユーザーガイド

## ハードウェア情報

[GL-S10 仕様](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## GPIOリスト

| ESP32-WROOM-32U GPIO Labeling | SIGNAL        | FUNCTION                                                     |
| ----------------------------- | ------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0         | ダウンロードボタン制御（デフォルト: High。起動時にLowでダウンロードモードに移行） |
| GPIO1                         | UART_TX0      | デバッグ用シリアルポート出力 |
| GPIO2                         | TP3           | JTAGテストポイント予約 |
| GPIO3                         | UART_RX0      | デバッグ用シリアルポート入力 |
| GPIO4                         | GPIO4         | NC |
| GPIO5                         | PHY_RESET     | MAC PHYリセット制御 |
| GPIO6                         | PSRAM_CLK     | PSRAMクロック信号 |
| GPIO7                         | PSRAM SDO/SD0 | PSRAMデータ信号 SDO/SD0 |
| GPIO8                         | PSRAM SDI/SD1 | PSRAMデータ信号 SDI/SD1 |
| GPIO9                         | PSRAM SHD/SD2 | PSRAMデータ信号 SHD/SD2 |
| GPIO10                        | PSRAM SWP/SD3 | PSRAMデータ信号 SWP/SD3 |
| GPIO11                        | GPIO11        | NC |
| GPIO12                        | BT LED        | BLE LED制御（プルダウンで点灯） |
| GPIO13                        | I2C_CLK       | I2Cクロック信号 |
| GPIO14                        | POWER_LED     | 電源LED制御 |
| GPIO15                        | I2C_DATA      | I2Cデータ信号 |
| GPIO16                        | PSRAM_CE      | PSRAM制御信号 |
| GPIO17                        | PHY_CLK       | PHYチップクロック信号 |
| GPIO18                        | MDIO          | PHYチップ制御信号 MDIO |
| GPIO19                        | RMII_TXD0     | RMIIインターフェイス送信データ TXD0 |
| GPIO21                        | RMII_TXEN     | RMIIインターフェイス送信イネーブル TXEN |
| GPIO22                        | RMII_TXD1     | RMIIインターフェイス送信データ TXD1 |
| GPIO23                        | MDC           | PHYチップ制御信号 MDC |
| GPIO25                        | RMII_RXD0     | RMIIインターフェイス受信データ RXD0 |
| GPIO26                        | RMII_RXD1     | RMIIインターフェイス受信データ RXD1 |
| GPIO27                        | RMII_CS_DV    | RMIIインターフェイス衝突検出信号 CS_DV |
| GPIO32                        | NETWORK LED   | ネットワークLED制御 |
| GPIO33                        | BUTTON        | ボタン入力 |
| GPIO34                        | GPIO34        | NC |
| GPIO35                        | GPIO35        | NC |
| GPIO36                        | GPIO36        | NC |
| GPIO39                        | GPIO39        | NC |

## PCBピン設定

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回セットアップ

IoTドキュメントの[GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"}をご参照ください。

---

## ユーザーマニュアル

IoTドキュメントの[ユーザーマニュアル](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"}をご参照ください。

---

## ファームウェアコンパイルガイド

IoTドキュメントの[ファームウェアコンパイルガイド](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"}をご参照ください。
