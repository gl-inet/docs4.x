# Problem Notification for GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Last updated: November 11, 2026**

This known issue affects only certain batches of devices. Devices ordered on or after July 1, 2025 are most likely from a newer batch and do not require a U-Boot bootloader update.

If you're not sure which batch your device is from, email the following to [support@gl-inet.com](mailto:support@gl-inet.com) before making any changes:

- Router model and firmware version
- Device's MAC address
- A description of the issue (including what you were doing when it occurred), any error messages, and the troubleshooting steps you have already tried

We will confirm your production batch and give you targeted troubleshooting advice.

---

**Published: March 26, 2025**

Dear GL.iNet Customers,

This announcement addresses the startup failure and firmware recovery issues via U-Boot on the GL-MT2500/GL-X3000/GL-XE3000 devices. The problem stemmed from a software defect where some parameters were incorrectly defined, causing the routers to operate abnormally. As a result, we assessed that this issue might reduce the routers' service life to some extent, for which we sincerely apologize.

To completely resolve this issue, we strongly recommend that all users of GL-MT2500, GL-X3000, and GL-XE3000 perform both a U-Boot bootloader upgrade and a firmware upgrade. Both upgrade procedures are essential and should not be omitted.

Even if your device has already been upgraded to the latest firmware, a U-Boot bootloader upgrade remains mandatory to prevent potential issues. After completing the U-Boot bootloader upgrade, if the latest firmware is already installed, you may skip reinstalling the firmware.

Please try upgrading with Chrome or Microsoft Edge. DO NOT use Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Update the U-Boot bootloader.

    Download [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}, then [update the U-Boot bootloader](upgrade_uboot_version.md).

2. Upgrade the firmware.

    Download [the latest firmware for your router](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"}, then [upgrade your router's firmware](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Update the U-Boot bootloader.

    Download [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}, then [update the U-Boot bootloader](upgrade_uboot_version.md).

2. Upgrade the firmware.

    Download [the latest firmware for your router](https://dl.gl-inet.com/router/x3000/stable){target="_blank"}, then [upgrade your router's firmware](../tutorials/how_to_upgrade_downgrade_router.md).


## GL-XE3000 {#gl-xe3000}

1. Update the U-Boot bootloader.

    Download [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}, then [update the U-Boot bootloader](upgrade_uboot_version.md).

2. Upgrade the firmware.

    Download [the latest firmware for your router](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"}, then [upgrade your router's firmware](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
We sincerely apologize for any inconvenience this may have caused. Moving forward, we are committed to enhancing our products and firmware with greater diligence and care.

For those who currently own these routers, we will extend the warranty period by one year at no cost. Should you encounter any issues, please do not hesitate to contact our support teams.

If the problem persists despite the upgrade, please contact our support teams via [support@gl-inet.com](mailto:support@gl-inet.com), and we will provide a new replacement free of charge.

Your trust and support mean the world to us, and we are deeply grateful for it.

<br>
Sincerely,  
GL.iNet Team  
March 26, 2025
