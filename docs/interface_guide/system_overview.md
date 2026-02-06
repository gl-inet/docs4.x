# System Overview

On the left side of web Admin Panel -> SYSTEM -> Overview

The Overview page displays the status of some hardwares and supports some simple controls, including the following:

- Status of CPU, Memory, Flash and External Storage devices.
- Status of hardware such as Fan, Battery, etc.
- Control of LEDs and Fan.
- Device information.

Here is an example of GL-MT3000.

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## CPU Average Load

For most models without a fan, the CPU average load is displayed as below.

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

For some models with a built-in fan, the CPU average load is displayed as below.

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Mouse over the graph to display specific values.

Click on the temperature on the right to switch between Celsius and Fahrenheit.

Click on the Fan icon at the upper-right corner to enter the Fan Settings.

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Models with Built-in Fans"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Memory Usage

Mouse over the graph to display specific values.

**Note**: The memory shown here is the memory available to the Linux system. The total memory here will be less than the physical memory because some of it will be allocated to the Wi-Fi subsystem or other boot areas.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

Click the gear icon will go to the [Scheduled Tasks](scheduled_tasks.md) of LED.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

It displays total flash memory, including those System used, Apps used and the left Available.

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## Device Info

This section displays the basic information of the device. 

Device ID, device MAC, and device S/N have been added in firmware v4.7 and above versions.

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## External Storage

This section, available since v4.5, displays the total and available capacity of the USB Disk.

Some models in firmware v4.7 and above version support switching USB protocol.

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.