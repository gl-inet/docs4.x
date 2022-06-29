# How to upgrade GL-AX1800(Flint) to firmware 4.x?

The GL-AX1800 is already available in 4.x beta firmware. For those who want to try it, you can follow the steps below to upgrade GL-AXT1800 from firmware 3.x to 4.x.

**Note:** the beta firmware may has bugs.

## Upgrade

There are two ways to upgrade to firmware 4.x. The first method is recommended, it is easier.

- Method 1:

    Use the Local Upgrade in web Admin Panel.

    1. Please upgrade the firmware to 3.214 (the latest stable version).

    2. Download the 4.x beta firmware [here](https://dl.gl-inet.com/?model=ax1800&type=beta){target="_blank"}, please download the one for uboot, its file name extension is **.img**.

    3. Upgrade it via the **Local Upgrade** in web Admin Panel -> UPGRADE with the .img firmware file.

        ![local upgrade](https://static.gl-inet.com/docs/en/3/setup/share/upgrade/local_upgrade.png){class="glboxshadow"}

- Method 2:

    1. Download the 4.x beta firmware [here](https://dl.gl-inet.com/?model=ax1800&type=beta){target="_blank"}, please download the one for uboot, its file name extension is **.img**.

    2. Please flash the firmware by [Uboot](../debrick/).

## Downgrade

1. Please download the latest 3.x release firmware [here](https://dl.gl-inet.com/?model=ax1800){target="_blank"}

2. Please flash the firmware by [Uboot](../debrick/).
