# How to upgrade to firmware 4.x?

Some old models already have the 4.x beta firmware. For those who want to try it, you can follow the steps below to upgrade it from firmware 3.x to 4.x.

The following models are currently supported:

GL-AX1800(Flint), GL-MT1300(Beryl), GL-B1300(Convexa-B), GL-S1300(Convexa-S), GL-AP1300(Cirrus), GL-SFT1200(Opal), GL-AR750S(Slate).

**Note:** The beta firmware may has bugs. Currently, it is recommended not to keep settings when upgrading, since they may be lost during the upgrade, or they may cause instability. Therefore, be sure to backup any critical settings before upgrading. We will improving the process to make the upgrade smoother.

**Note:** Currently, the GL-B1300 and GL-S1300 do not have mesh function.

## Upgrade

There are two methods to upgrade to firmware 4.x. The first method can be used for some models, and the second method can be used for all models.

### Method 1

Upgrade via the Local Upgrade in web Admin Panel.

Suitable for GL-AX1800, GL-MT1300, GL-SFT1200, GL-B1300, GL-AR750S.

1. Upgrade the firmware to the latest stable 3.x version.

2. Download the 4.x firmware [here](https://dl.gl-inet.com){target="_blank"}.

    * For GL-MT1300, GL-B1300, GL-SFT1200, GL-AR750S, please download the one for Local Upgrade, its file name extension is **.tar** or **.bin**.

    * For GL-AX1800, please download the one for Uboot, its file name extension is **.img**.

3. Upgrade it via the **Local Upgrade** in web Admin Panel -> UPGRADE with the firmware file you just donwloaded.

    **Note:** 4.x firmware is not compatible with 3.x firmware. When you upgrade from 3.x firmware, please do **NOT** keep settings.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/gl-ax1800_upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow gl-90-desktop"}

### Method 2

Upgrade via Uboot.

Suitable for all models.

1. Download the 4.x firmware [here](https://dl.gl-inet.com){target="_blank"}, please download the one for Uboot.

2. Please flash the firmware by [Uboot](debrick.md).

## Downgrade

1. Please download the latest 3.x release firmware [here](https://dl.gl-inet.com){target="_blank"}.

2. Please flash the firmware by [Uboot](debrick.md).

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
