# GL-S20 User Guide

## Hardware info

[GL-S20 specifications](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## GPIO list

| ESP32-WROOM-32U GPIO Labeling | SIGNAL         | FUNCTION                                                     |
| ----------------------------- | -------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0          | connected to ch340c pin DTR for the device to enter download mode |
| GPIO1                         | BUTTON         | button input, used for reset                                 |
| GPIO2                         | GPIO2          | used for control h2 reset io                                 |
| GPIO3                         | GPIO3          | used for control h2 boot io                                  |
| GPIO4                         | PHY_SPI_INT    | interrupt GPIO number SPI Ethernet module                    |
| GPIO5                         | PHY_RESET      | PHY reset GPIO number of SPI Ethernet module                 |
| GPIO6                         | NETWORK_LED    | network led control (green)                                  |
| GPIO7                         | NETWORK_LED    | network led control (red)                                    |
| GPIO8                         | UART1 RX	     | used for connect to h2 uart0 tx                              |
| GPIO9                         | POWER_LED      | power led control (green)                                    |
| GPIO10                        | PHY_SPI_CSN    | SPI CS GPIO number for SPI Ethernet module                   |
| GPIO11                        | PHY_SPI_MOSI   | SPI MOSI GPIO number for SPI Ethernet module                 |
| GPIO12                        | PHY_SPI_CK     | SPI SCLK GPIO number for SPI Ethernet module                 |
| GPIO13                        | PHY_SPI_MISO   | SPI MISO GPIO number for SPI Ethernet module                 |
| GPIO14                        | POWER_LED      | power led control (red)                                      |
| GPIO15                        | NETWORK_LED    | network led control (yellow)                                 |
| GPIO16                        | BUTTON         | button input, used for iot function control                  |
| GPIO17                        | IOT_LED        | iot led control (green)                                      |
| GPIO18                        | IOT_LED        | iot led control (red)                                        |
| GPIO19                        | IOT_LED        | iot led control (yellow)                                     |
| GPIO20                        | POWER_LED	     | power led control (yellow)                                   |
| GPIO21                        | UART1 RTS      | used for connect to h2 uart0 cts                             |
| GPIO35                        | GPIO35         | NC                                                           |
| GPIO36                        | GPIO36         | NC                                                           |
| GPIO37                        | GPIO37         | NC                                                           |
| GPIO38                        | GPIO38         | NC                                                           |
| GPIO39                        | GPIO39         | NC                                                           |
| GPIO40                        | PTA_REQUEST    | used for PTA                                                 |
| GPIO41                        | PTA_PRIORITY   | used for PTA                                                 |
| GPIO42                        | PTA_GRANT      | used for PTA                                                 |
| GPIO43                        | UART0 TX       | used for debugging serial port output                        |
| GPIO44                        | UART0 RX       | used for debugging serial port output                        |
| GPIO45                        | PTA_TX_LINE    | used for PTA                                                 |
| GPIO46                        | GPIO46         | NC                                                           |
| GPIO47                        | UART1 CTS      | used for connect to h2 uart0 rts                             |
| GPIO48                        | UART1 TX       | used for connect to h2 uart0 rx                              |

## PCB Pinout

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## First-time setup

Please refer to [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"} on IoT docs.

---

## User Manual

Please refer to [User Manual](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"} on IoT docs.

---

## Firmware Compilation Guide

Please refer to [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"} on IoT docs.
