# Gebruikershandleiding GL-S20 {#gl-s20-user-guide}

## Hardwaregegevens {#hardware-info}

[Specificaties van GL-S20](https://www.gl-inet.com/products/gl-s20/#specs){target="_blank"}

## GPIO-lijst {#gpio-list}

| ESP32-WROOM-32U GPIO-label | SIGNAAL         | FUNCTIE                                                     |
| ----------------------------- | -------------- | ------------------------------------------------------------ |
| GPIO0                         | GPIO0          | verbonden met ch340c-pin DTR om het apparaat in downloadmodus te zetten |
| GPIO1                         | BUTTON         | knopinvoer, gebruikt voor reset                                 |
| GPIO2                         | GPIO2          | gebruikt om h2 reset-IO aan te sturen                                 |
| GPIO3                         | GPIO3          | gebruikt om h2 boot-IO aan te sturen                                  |
| GPIO4                         | PHY_SPI_INT    | GPIO-nummer voor interrupts van SPI Ethernet-module                    |
| GPIO5                         | PHY_RESET      | GPIO-nummer voor PHY-reset van SPI Ethernet-module                 |
| GPIO6                         | NETWORK_LED    | bediening netwerkled (groen)                                  |
| GPIO7                         | NETWORK_LED    | bediening netwerkled (rood)                                    |
| GPIO8                         | UART1 RX	     | gebruikt voor verbinding met h2 uart0 tx                              |
| GPIO9                         | POWER_LED      | bediening voedingsled (groen)                                    |
| GPIO10                        | PHY_SPI_CSN    | SPI CS-GPIO-nummer voor SPI Ethernet-module                   |
| GPIO11                        | PHY_SPI_MOSI   | SPI MOSI-GPIO-nummer voor SPI Ethernet-module                 |
| GPIO12                        | PHY_SPI_CK     | SPI SCLK-GPIO-nummer voor SPI Ethernet-module                 |
| GPIO13                        | PHY_SPI_MISO   | SPI MISO-GPIO-nummer voor SPI Ethernet-module                 |
| GPIO14                        | POWER_LED      | bediening voedingsled (rood)                                      |
| GPIO15                        | NETWORK_LED    | bediening netwerkled (geel)                                 |
| GPIO16                        | BUTTON         | knopinvoer, gebruikt voor bediening van IoT-functie                  |
| GPIO17                        | IOT_LED        | bediening IoT-led (groen)                                      |
| GPIO18                        | IOT_LED        | bediening IoT-led (rood)                                        |
| GPIO19                        | IOT_LED        | bediening IoT-led (geel)                                     |
| GPIO20                        | POWER_LED	     | bediening voedingsled (geel)                                   |
| GPIO21                        | UART1 RTS      | gebruikt voor verbinding met h2 uart0 cts                             |
| GPIO35                        | GPIO35         | NC                                                           |
| GPIO36                        | GPIO36         | NC                                                           |
| GPIO37                        | GPIO37         | NC                                                           |
| GPIO38                        | GPIO38         | NC                                                           |
| GPIO39                        | GPIO39         | NC                                                           |
| GPIO40                        | PTA_REQUEST    | gebruikt voor PTA                                                 |
| GPIO41                        | PTA_PRIORITY   | gebruikt voor PTA                                                 |
| GPIO42                        | PTA_GRANT      | gebruikt voor PTA                                                 |
| GPIO43                        | UART0 TX       | gebruikt voor uitvoer via seriële debugpoort                        |
| GPIO44                        | UART0 RX       | gebruikt voor invoer via seriële debugpoort                        |
| GPIO45                        | PTA_TX_LINE    | gebruikt voor PTA                                                 |
| GPIO46                        | GPIO46         | NC                                                           |
| GPIO47                        | UART1 CTS      | gebruikt voor verbinding met h2 uart0 rts                             |
| GPIO48                        | UART1 TX       | gebruikt voor verbinding met h2 uart0 rx                              |

## PCB-pintoewijzing {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s20/hardware_info/gl-s20_pinout_1.jpg" itemprop="thumbnail" alt="gl-s20 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Eerste installatie {#first-time-setup}

Raadpleeg [GL-S20](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/){target="_blank"} in de IoT-documentatie.

---

## Gebruikershandleiding {#user-manual}

Raadpleeg de [User Manual](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/){target="_blank"} in de IoT-documentatie.

---

## Handleiding voor firmwarecompilatie {#firmware-compilation-guide}

Raadpleeg de [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s20/user_manual/gl-s20-tbr_firmware_compilation_guide/){target="_blank"} in de IoT-documentatie.
