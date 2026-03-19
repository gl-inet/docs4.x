# Guía de usuario de GL-S10

## Información del hardware

[Especificaciones del GL-S10](https://www.gl-inet.com/products/gl-s10/#specs){target="\_blank"}

## Lista de GPIO

| Etiquetado GPIO de ESP32-WROOM-32U | SIGNAL        | FUNCTION                                                                                                      |
| ---------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------- |
| GPIO0                              | GPIO0         | control del botón de descarga; por defecto en alto; al iniciar, poner en bajo para entrar en modo de descarga |
| GPIO1                              | UART_TX0      | utilizado para la salida del puerto serie de depuración                                                       |
| GPIO2                              | TP3           | puntos de prueba JTAG reservados                                                                              |
| GPIO3                              | UART_RX0      | utilizado para la entrada del puerto serie de depuración                                                      |
| GPIO4                              | GPIO4         | NC                                                                                                            |
| GPIO5                              | PHY_RESET     | control de reinicio del PHY MAC                                                                               |
| GPIO6                              | PSRAM_CLK     | señal de reloj de psram                                                                                       |
| GPIO7                              | PSRAM SDO/SD0 | señal de datos de psram SDO/SD0                                                                               |
| GPIO8                              | PSRAM SDI/SD1 | señal de datos de psram SDI/SD1                                                                               |
| GPIO9                              | PSRAM SHD/SD2 | señal de datos de psram SHD/SD2                                                                               |
| GPIO10                             | PSRAM SWP/SD3 | señal de datos de psram SWP/SD3                                                                               |
| GPIO11                             | GPIO11        | NC                                                                                                            |
| GPIO12                             | BT LED        | control del LED BLE; poner en bajo para encender                                                              |
| GPIO13                             | I2C_CLK       | señal de reloj I2C                                                                                            |
| GPIO14                             | POWER_LED     | control del LED de alimentación                                                                               |
| GPIO15                             | I2C_DATA      | señal de datos I2C                                                                                            |
| GPIO16                             | PSRAM_CE      | señal de control de psram                                                                                     |
| GPIO17                             | PHY_CLK       | señal de reloj del chip PHY                                                                                   |
| GPIO18                             | MDIO          | señal de control MDIO del chip PHY                                                                            |
| GPIO19                             | RMII_TXD0     | dato TXD0 de la interfaz RMII                                                                                 |
| GPIO21                             | RMII_TXEN     | habilitación TXEN de la interfaz RMII                                                                         |
| GPIO22                             | RMII_TXD1     | dato TXD1 de la interfaz RMII                                                                                 |
| GPIO23                             | MDC           | señal de control MDC del chip PHY                                                                             |
| GPIO25                             | RMII_RXD0     | dato RXD0 de la interfaz RMII                                                                                 |
| GPIO26                             | RMII_RXD1     | dato RXD1 de la interfaz RMII                                                                                 |
| GPIO27                             | RMII_CS_DV    | señal de detección de colisión CS_DV de la interfaz RMII                                                      |
| GPIO32                             | NETWORK LED   | control del LED de red                                                                                        |
| GPIO33                             | BUTTON        | entrada del botón                                                                                             |
| GPIO34                             | GPIO34        | NC                                                                                                            |
| GPIO35                             | GPIO35        | NC                                                                                                            |
| GPIO36                             | GPIO36        | NC                                                                                                            |
| GPIO39                             | GPIO39        | NC                                                                                                            |

## Pinout de la PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Configuración inicial

Consulte [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="\_blank"} en la documentación IoT.

---

## Manual de usuario

Consulte [User Manual](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="\_blank"} en la documentación IoT.

---

## Guía de compilación del firmware

Consulte [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="\_blank"} en la documentación IoT.
