# Guide d'utilisation du GL-S10

## Informations matérielles

[Spécifications du GL-S10](https://www.gl-inet.com/products/gl-s10/#specs){target="_blank"}

## Liste GPIO

| Étiquetage GPIO ESP32-WROOM-32U | SIGNAL        | FONCTION                                                     |
| ------------------------------- | ------------- | ------------------------------------------------------------ |
| GPIO0                           | GPIO0         | contrôle du bouton de téléchargement, niveau haut par défaut ; au démarrage, niveau bas pour entrer en mode téléchargement |
| GPIO1                           | UART_TX0      | utilisé pour la sortie du port série de débogage             |
| GPIO2                           | TP3           | points de test JTAG réservés                                 |
| GPIO3                           | UART_RX0      | utilisé pour l'entrée du port série de débogage              |
| GPIO4                           | GPIO4         | NC                                                           |
| GPIO5                           | PHY_RESET     | contrôle de réinitialisation du PHY MAC                      |
| GPIO6                           | PSRAM_CLK     | signal d'horloge PSRAM                                       |
| GPIO7                           | PSRAM SDO/SD0 | signal de données PSRAM SDO/SD0                              |
| GPIO8                           | PSRAM SDI/SD1 | signal de données PSRAM SDI/SD1                              |
| GPIO9                           | PSRAM SHD/SD2 | signal de données PSRAM SHD/SD2                              |
| GPIO10                          | PSRAM SWP/SD3 | signal de données PSRAM SWP/SD3                              |
| GPIO11                          | GPIO11        | NC                                                           |
| GPIO12                          | BT LED        | contrôle de la LED ble, tirage bas pour l'allumer            |
| GPIO13                          | I2C_CLK       | signal d'horloge I2C                                         |
| GPIO14                          | POWER_LED     | contrôle de la LED d'alimentation                            |
| GPIO15                          | I2C_DATA      | signal de données I2C                                        |
| GPIO16                          | PSRAM_CE      | signal de contrôle PSRAM                                     |
| GPIO17                          | PHY_CLK       | signal d'horloge de la puce PHY                              |
| GPIO18                          | MDIO          | signal de contrôle MDIO de la puce PHY                       |
| GPIO19                          | RMII_TXD0     | données TXD0 de l'interface RMII                             |
| GPIO21                          | RMII_TXEN     | signal d'activation TXEN de l'interface RMII                 |
| GPIO22                          | RMII_TXD1     | données TXD1 de l'interface RMII                             |
| GPIO23                          | MDC           | signal de contrôle MDC de la puce PHY                        |
| GPIO25                          | RMII_RXD0     | données RXD0 de l'interface RMII                             |
| GPIO26                          | RMII_RXD1     | données RXD1 de l'interface RMII                             |
| GPIO27                          | RMII_CS_DV    | signal de détection de collision CS_DV de l'interface RMII   |
| GPIO32                          | NETWORK LED   | contrôle de la LED réseau                                    |
| GPIO33                          | BUTTON        | entrée du bouton                                             |
| GPIO34                          | GPIO34        | NC                                                           |
| GPIO35                          | GPIO35        | NC                                                           |
| GPIO36                          | GPIO36        | NC                                                           |
| GPIO39                          | GPIO39        | NC                                                           |

## Brochage du PCB

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s10/hardware_info/gl-s10-pinout.jpg" itemprop="thumbnail" alt="gl-s10 pinout" loading="lazy" />
    </a>
  </figure>
</div>

---

## Configuration initiale

Veuillez consulter [GL-S10](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/){target="_blank"} dans la documentation IoT.

---

## Manuel d'utilisation

Veuillez consulter le [User Manual](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/user_manual/){target="_blank"} dans la documentation IoT.

---

## Guide de compilation du firmware

Veuillez consulter le [Firmware Compilation Guide](https://docs.gl-inet.com/iot/en/ble_proxy/gl-s10/firmware_compilation_guide/){target="_blank"} dans la documentation IoT.
