# How to upgrade GL-AX1800(Flint) to firmware 4.x?

The GL-AX1800 is already available in 4.x firmware. For those who want to try it, you can follow the steps below to upgrade GL-AXT1800 from firmware 3.x to 4.x.

## Upgrade

There are two ways to upgrade to firmware 4.x. The first method is recommended, it is easier.

- Method 1:

    Use the Local Upgrade in web Admin Panel.

    1. Please upgrade the firmware to 3.214 (the latest stable version).

    2. Download the 4.x firmware [here](https://dl.gl-inet.com/?model=ax1800){target="_blank"}, please download the one for uboot, its file name extension is **.img**. There may be some confusion here, the firmware used for uboot is not normally available for Local Upgrade, this is a special case.

    3. Upgrade it via the **Local Upgrade** in web Admin Panel -> UPGRADE with the .img firmware file.

        **Note:** 4.x firmware is not compatible with 3.x firmware. When you upgrade from 3.x firmware, please do **NOT** keep settings.

        ![local upgrade](https://static.gl-inet.com/docs/en/4/tutorials/gl-ax1800_upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow" width="60%"}

- Method 2:

    1. Download the 4.x firmware [here](https://dl.gl-inet.com/?model=ax1800){target="_blank"}, please download the one for uboot, its file name extension is **.img**.

    2. Please flash the firmware by [Uboot](../debrick/).

## Downgrade

1. Please download the latest 3.x release firmware [here](https://dl.gl-inet.com/?model=ax1800){target="_blank"}

2. Please flash the firmware by [Uboot](../debrick/).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
