# Critical Problem Notification for GL-MT2500/GL-X3000/GL-XE3000

Dear GL.iNet Customers,

This announcement addresses the startup failure and firmware recovery issues via U-Boot on the GL-MT2500/GL-X3000/GL-XE3000 devices. The problem stemmed from a software defect where some parameters were incorrectly defined, causing the routers to operate abnormally. As a result, we assessed that this issue might reduce the routers' service life to some extent, for which we sincerely apologize.

To completely resolve this issue, we strongly recommend that all users of GL-MT2500, GL-X3000, and GL-XE3000 perform both a U-Boot bootloader upgrade and a firmware upgrade. Both upgrade procedures are essential and should not be omitted.

Even if your device has already been upgraded to the latest firmware, a U-Boot bootloader upgrade remains mandatory to prevent potential issues. After completing the U-Boot bootloader upgrade, if the latest firmware is already installed, you may skip reinstalling the firmware.

Please try upgrading with Chrome or Microsoft Edge. DO NOT use Mozilla/Firefox.

## GL-MT2500

1. Download and upgrade the U-Boot bootloader to [version 2025-02-24 15:04:07](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}

2. Download and upgrade the firmware to [version 4.7.4](https://fw.gl-inet.com/firmware/mt2500/release/openwrt-mt2500-4.7.4-0328-1743128340.bin)

## GL-X3000

1. Download and upgrade the U-Boot bootloader to [version 2025-02-25 19:05:24](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}

2. Download and upgrade the firmware to [version 4.7.4](https://fw.gl-inet.com/firmware/x3000/release/openwrt-x3000-4.7.4-0317-1742206344.bin)

## GL-XE3000

1. Download upgrade the U-Boot bootloader to [version 2025-02-25 19:07:14](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}

2. Download and upgrade the firmware to [version 4.7.4](https://fw.gl-inet.com/firmware/xe3000/release/openwrt-xe3000-4.7.4-0317-1742206184.bin)

!!! Note

    For the methods to upgrade the U-Boot bootloader, you can refer to [this link](https://docs.gl-inet.com/router/en/4/faq/upgrade_uboot_version/){target="_blank"}.

    For the methods to upgrade the firmware, you can refer to [this link](https://docs.gl-inet.com/router/en/4/tutorials/how_to_upgrade_downgrade_router/){target="_blank"}.

<br>
We sincerely apologize for any inconvenience this may have caused. Moving forward, we are committed to enhancing our products and firmware with greater diligence and care.

For those who currently own these routers, we will extend the warranty period by one year at no cost. Should you encounter any issues, please do not hesitate to contact our support teams.

If the problem persists despite the upgrade, please contact our support teams via support@gl-inet.com, and we will provide a new replacement free of charge.

Your trust and support mean the world to us, and we are deeply grateful for it.

<br>

Sincerely,

GL.iNet Technical Support

March 26, 2025