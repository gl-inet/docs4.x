# Guida utente di GL-S10

## Informazioni hardware

[Specifiche di GL-S10](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## Elenco GPIO

| Etichettatura GPIO ESP32-WROOM-32U | SEGNALE       | FUNZIONE                                                     |
| ---------------------------------- | ------------- | ------------------------------------------------------------ |
| GPIO0                              | GPIO0         | controllo del pulsante download, predefinito su alto; all'avvio, basso per entrare in modalità download |
| GPIO1                              | UART_TX0      | utilizzato per l'output della porta seriale di debug         |
| GPIO2                              | TP3           | punto di test JTAG riservato                                 |
| GPIO3                              | UART_RX0      | utilizzato per l'ingresso della porta seriale di debug       |
| GPIO4                              | GPIO4         | NC                                                           |
| GPIO5                              | PHY_RESET     | controllo reset del PHY MAC                                  |
| GPIO6                              | PSRAM_CLK     | segnale di clock PSRAM                                       |
| GPIO7                              | PSRAM SDO/SD0 | segnale dati PSRAM SDO/SD0                                   |
| GPIO8                              | PSRAM SDI/SD1 | segnale dati PSRAM SDI/SD1                                   |
| GPIO9                              | PSRAM SHD/SD2 | segnale dati PSRAM SHD/SD2                                   |
| GPIO10                             | PSRAM SWP/SD3 | segnale dati PSRAM SWP/SD3                                   |
| GPIO11                             | GPIO11        | NC                                                           |
| GPIO12                             | BT LED        | controllo LED BLE, attivo a livello basso                    |
| GPIO13                             | I2C_CLK       | segnale di clock I2C                                         |
| GPIO14                             | POWER_LED     | controllo LED di alimentazione                               |
| GPIO15                             | I2C_DATA      | segnale dati I2C                                             |
| GPIO16                             | PSRAM_CE      | segnale di controllo PSRAM                                   |
| GPIO17                             | PHY_CLK       | segnale di clock del chip PHY                                |
| GPIO18                             | MDIO          | segnale di controllo MDIO del chip PHY                       |
| GPIO19                             | RMII_TXD0     | dato TXD0 dell'interfaccia RMII                              |
| GPIO21                             | RMII_TXEN     | segnale TXEN di abilitazione trasmissione dell'interfaccia RMII |
| GPIO22                             | RMII_TXD1     | dato TXD1 dell'interfaccia RMII                              |
| GPIO23                             | MDC           | segnale di controllo MDC del chip PHY                        |
| GPIO25                             | RMII_RXD0     | dato RXD0 dell'interfaccia RMII                              |
| GPIO26                             | RMII_RXD1     | dato RXD1 dell'interfaccia RMII                              |
| GPIO27                             | RMII_CS_DV    | segnale di rilevamento collisione CS_DV dell'interfaccia RMII |
| GPIO32                             | NETWORK LED   | controllo LED di rete                                        |
| GPIO33                             | BUTTON        | ingresso pulsante                                            |
| GPIO34                             | GPIO34        | NC                                                           |
| GPIO35                             | GPIO35        | NC                                                           |
| GPIO36                             | GPIO36        | NC                                                           |
| GPIO39                             | GPIO39        | NC                                                           |

## Piedinatura PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Configurazione iniziale

Fai riferimento a [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"} nella documentazione IoT.

---

## Manuale utente

Fai riferimento a [User Manual](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"} nella documentazione IoT.

---

## Guida alla compilazione del firmware

Fai riferimento a [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"} nella documentazione IoT.
