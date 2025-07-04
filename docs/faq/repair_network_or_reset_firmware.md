# How to repair network or factory reset?

All GL.iNet routers are equipped with a physical reset mechanism (either a reset button or a pinhole). Pressing the button or poking the pinhole has the same effect: restoring network connectivity or resetting the router to factory defaults. 

For models with a pinhole, use a pin, straightened paperclip or similar tool to perform the action.  

Ensure the router has fully booted up before performing a reset. **Do NOT** press the reset button immediately after powering on, as this may trigger U-Boot failsafe mode.  

## Repair network

Press and hold the reset button for **4 seconds** then release to perform a soft reset, which can repair your network.

This operation will reboot the network interface and restore the Internet interface to default settings, while preserving Wi-Fi settings, VPN settings, system settings, etc. 

**Note**: If WiFi has been disabled, a soft reset will restore WiFi to its default enabled state.

A soft reset can also be used to quickly switch from non-router mode to router mode.

## Reset to factory

There are two ways to reset the firmware.

1. Using reset button

    Press and hold the reset button for **10 seconds** then release to reset the router to factory settings. All user data will be cleared.

    **Note:** If the factory reset is not working. You might need to follow the [Uboot tutorial](debrick.md) to debrick your router.

2. Reset firmware in web Admin Panel

    If you can access the web Admin Panel, you can reset firmware to factory.

    On the left side of web Admin Panel -> SYSTEM -> Reset Firmware

    **Note:** All your current settings, applications and data will be lost. The process will take about 3 minutes. DO NOT power off the router during this process.

    ![glinet reset firmware](https://static.gl-inet.com/docs/router/en/4/tutorials/reset_firmware/reset_firmware.png){class="glboxshadow"}

---

Video guide: How to Reset GL.iNet Router to Factory Default

<iframe width="560" height="315" src="https://www.youtube.com/embed/ON6PtGH_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
