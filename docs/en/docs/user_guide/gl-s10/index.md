# GL-S10 User Guide

## Hardware info

[GL-S10 specifications](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## GPIO list

| ESP32-WROOM-32U GPIO Labeling | SIGNAL        | FUNCTION                                                     |
| ----------------------------- | ------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0         | download button control, default to high, when starting, low to enter download mode |
| GPIO1                         | UART_TX0      | used for debugging serial port output                        |
| GPIO2                         | TP3           | reserve JTAG testing points                                  |
| GPIO3                         | UART_RX0      | used for debugging serial port input                         |
| GPIO4                         | GPIO4         | NC                                                           |
| GPIO5                         | PHY_RESET     | MAC phy reset control                                        |
| GPIO6                         | PSRAM_CLK     | psram clock signal                                           |
| GPIO7                         | PSRAM SDO/SD0 | psram data signal SDO/SD0                                    |
| GPIO8                         | PSRAM SDI/SD1 | psram data signal SDI/SD1                                    |
| GPIO9                         | PSRAM SHD/SD2 | psram data signal SHD/SD2                                    |
| GPIO10                        | PSRAM SWP/SD3 | psram data signal SWP/SD3                                    |
| GPIO11                        | GPIO11        | NC                                                           |
| GPIO12                        | BT LED        | ble led control, pull down to light up                       |
| GPIO13                        | I2C_CLK       | I2C clock signal                                             |
| GPIO14                        | POWER_LED     | power led control                                            |
| GPIO15                        | I2C_DATA      | I2C data signal                                              |
| GPIO16                        | PSRAM_CE      | psram control signal                                         |
| GPIO17                        | PHY_CLK       | phy chip clock signal                                        |
| GPIO18                        | MDIO          | phy chip control signal MDIO                                 |
| GPIO19                        | RMII_TXD0     | RMII interface TX data TXD0                                  |
| GPIO21                        | RMII_TXEN     | RMII interface TX enable TXEN                                |
| GPIO22                        | RMII_TXD1     | RMII interface TX data TXD1                                  |
| GPIO23                        | MDC           | phy chip control signal MDC                                  |
| GPIO25                        | RMII_RXD0     | RMII interface RX data RXD0                                  |
| GPIO26                        | RMII_RXD1     | RMII interface RX data RXD1                                  |
| GPIO27                        | RMII_CS_DV    | RMII interface collision detection signal CS_DV              |
| GPIO32                        | NETWORK LED   | network led control                                          |
| GPIO33                        | BUTTON        | button input                                                 |
| GPIO34                        | GPIO34        | NC                                                           |
| GPIO35                        | GPIO35        | NC                                                           |
| GPIO36                        | GPIO36        | NC                                                           |
| GPIO39                        | GPIO39        | NC                                                           |

## PCB Pinout

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## First-time setup

Please refer to [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"} on IoT docs.

---

## User Manual

Please refer to [User Manual](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"} on IoT docs.

---

## Firmware Compilation Guide

Please refer to [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"} on IoT docs.
