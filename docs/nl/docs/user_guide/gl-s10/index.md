# Gebruikershandleiding GL-S10 {#gl-s10-user-guide}

## Hardwaregegevens {#hardware-info}

[Specificaties van GL-S10](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## GPIO-lijst {#gpio-list}

| ESP32-WROOM-32U GPIO-label | SIGNAAL        | FUNCTIE                                                     |
| ----------------------------- | ------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0         | bediening downloadknop, standaard hoog; bij opstarten laag voor downloadmodus |
| GPIO1                         | UART_TX0      | gebruikt voor uitvoer via seriële debugpoort                        |
| GPIO2                         | TP3           | gereserveerde JTAG-testpunten                                  |
| GPIO3                         | UART_RX0      | gebruikt voor invoer via seriële debugpoort                         |
| GPIO4                         | GPIO4         | NC                                                           |
| GPIO5                         | PHY_RESET     | bediening MAC PHY-reset                                        |
| GPIO6                         | PSRAM_CLK     | PSRAM-kloksignaal                                           |
| GPIO7                         | PSRAM SDO/SD0 | PSRAM-gegevenssignaal SDO/SD0                                    |
| GPIO8                         | PSRAM SDI/SD1 | PSRAM-gegevenssignaal SDI/SD1                                    |
| GPIO9                         | PSRAM SHD/SD2 | PSRAM-gegevenssignaal SHD/SD2                                    |
| GPIO10                        | PSRAM SWP/SD3 | PSRAM-gegevenssignaal SWP/SD3                                    |
| GPIO11                        | GPIO11        | NC                                                           |
| GPIO12                        | BT LED        | bediening BLE-led, omlaag trekken om in te schakelen                       |
| GPIO13                        | I2C_CLK       | I2C-kloksignaal                                             |
| GPIO14                        | POWER_LED     | bediening voedingsled                                            |
| GPIO15                        | I2C_DATA      | I2C-gegevenssignaal                                              |
| GPIO16                        | PSRAM_CE      | PSRAM-besturingssignaal                                         |
| GPIO17                        | PHY_CLK       | kloksignaal van PHY-chip                                        |
| GPIO18                        | MDIO          | besturingssignaal van PHY-chip MDIO                                 |
| GPIO19                        | RMII_TXD0     | TX-gegevens van RMII-interface TXD0                                  |
| GPIO21                        | RMII_TXEN     | TX inschakelen op RMII-interface TXEN                                |
| GPIO22                        | RMII_TXD1     | TX-gegevens van RMII-interface TXD1                                  |
| GPIO23                        | MDC           | besturingssignaal van PHY-chip MDC                                  |
| GPIO25                        | RMII_RXD0     | RX-gegevens van RMII-interface RXD0                                  |
| GPIO26                        | RMII_RXD1     | RX-gegevens van RMII-interface RXD1                                  |
| GPIO27                        | RMII_CS_DV    | botsingsdetectiesignaal van RMII-interface CS_DV              |
| GPIO32                        | NETWORK LED   | bediening netwerkled                                          |
| GPIO33                        | BUTTON        | knopinvoer                                                 |
| GPIO34                        | GPIO34        | NC                                                           |
| GPIO35                        | GPIO35        | NC                                                           |
| GPIO36                        | GPIO36        | NC                                                           |
| GPIO39                        | GPIO39        | NC                                                           |

## PCB-pintoewijzing {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Eerste installatie {#first-time-setup}

Raadpleeg [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"} in de IoT-documentatie.

---

## Gebruikershandleiding {#user-manual}

Raadpleeg de [User Manual](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"} in de IoT-documentatie.

---

## Handleiding voor firmwarecompilatie {#firmware-compilation-guide}

Raadpleeg de [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"} in de IoT-documentatie.
