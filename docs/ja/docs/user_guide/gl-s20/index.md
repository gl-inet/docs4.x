# GL-S20 ユーザーガイド

## ハードウェア情報

[GL-S20 仕様](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## GPIOリスト

| ESP32-WROOM-32U GPIO Labeling | SIGNAL         | FUNCTION                                                     |
| ----------------------------- | -------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0          | デバイスをダウンロードモードにするためにch340cピンDTRに接続 |
| GPIO1                         | BUTTON         | ボタン入力（リセット用） |
| GPIO2                         | GPIO2          | h2リセットIO制御用 |
| GPIO3                         | GPIO3          | h2ブートIO制御用 |
| GPIO4                         | PHY_SPI_INT    | SPI EthernetモジュールのGPIO割り込み番号 |
| GPIO5                         | PHY_RESET      | SPI EthernetモジュールのPHYリセットGPIO番号 |
| GPIO6                         | NETWORK_LED    | ネットワークLED制御（緑） |
| GPIO7                         | NETWORK_LED    | ネットワークLED制御（赤） |
| GPIO8                         | UART1 RX	     | h2 uart0 txへの接続用 |
| GPIO9                         | POWER_LED      | 電源LED制御（緑） |
| GPIO10                        | PHY_SPI_CSN    | SPI EthernetモジュールのSPI CS GPIO番号 |
| GPIO11                        | PHY_SPI_MOSI   | SPI EthernetモジュールのSPI MOSI GPIO番号 |
| GPIO12                        | PHY_SPI_CK     | SPI EthernetモジュールのSPI SCLK GPIO番号 |
| GPIO13                        | PHY_SPI_MISO   | SPI EthernetモジュールのSPI MISO GPIO番号 |
| GPIO14                        | POWER_LED      | 電源LED制御（赤） |
| GPIO15                        | NETWORK_LED    | ネットワークLED制御（黄） |
| GPIO16                        | BUTTON         | ボタン入力（IoT機能制御用） |
| GPIO17                        | IOT_LED        | IoT LED制御（緑） |
| GPIO18                        | IOT_LED        | IoT LED制御（赤） |
| GPIO19                        | IOT_LED        | IoT LED制御（黄） |
| GPIO20                        | POWER_LED	     | 電源LED制御（黄） |
| GPIO21                        | UART1 RTS      | h2 uart0 ctsへの接続用 |
| GPIO35                        | GPIO35         | NC |
| GPIO36                        | GPIO36         | NC |
| GPIO37                        | GPIO37         | NC |
| GPIO38                        | GPIO38         | NC |
| GPIO39                        | GPIO39         | NC |
| GPIO40                        | PTA_REQUEST    | PTA用 |
| GPIO41                        | PTA_PRIORITY   | PTA用 |
| GPIO42                        | PTA_GRANT      | PTA用 |
| GPIO43                        | UART0 TX       | デバッグ用シリアルポート出力 |
| GPIO44                        | UART0 RX       | デバッグ用シリアルポート出力 |
| GPIO45                        | PTA_TX_LINE    | PTA用 |
| GPIO46                        | GPIO46         | NC |
| GPIO47                        | UART1 CTS      | h2 uart0 rtsへの接続用 |
| GPIO48                        | UART1 TX       | h2 uart0 rxへの接続用 |

## PCBピン設定

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## 初回セットアップ

IoTドキュメントの[GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"}をご参照ください。

---

## ユーザーマニュアル

IoTドキュメントの[ユーザーマニュアル](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"}をご参照ください。

---

## ファームウェアコンパイルガイド

IoTドキュメントの[ファームウェアコンパイルガイド](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"}をご参照ください。
