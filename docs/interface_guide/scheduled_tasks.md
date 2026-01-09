# Scheduled Tasks

On the left side of web Admin Panel -> SYSTEM -> Scheduled Tasks

Schedule Tasks allows you to set up a daily schedule for some basic actions, such as turning LED lights on and off, restarting the router, turning Wi-Fi on and off, and switching TX power.

**Note**: Please first synchronize the time in the [Time Zone](time_zone.md) before using this function. If the device is shut down at the scheduled time, the task will not be executed.

## LED Display Schedule

This feature allows you to set a schedule for your router's LED lights. 

When enabled, set the on and off times, select the weekly effective dates, and then click Apply.

![led display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

## Schedule Reboot

This feature allows you to set a schedule for automatically restarting your router. 

When enabled, set the reboot times, select the weekly effective dates, and then click Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Wi-Fi Schedule

This feature allows you to set Wi-Fi schedules based on the Wi-Fi frequency bands supported by your router (such as 2.4 GHz, 5 GHz, 6 GHz, and MLO Wi-Fi).

Except for MLO Wi-Fi, which only supports the on/off schedule mode, all other Wi-Fi frequency bands support two schedule modes: Turn On/Off and Switch TX Power.

- **Turn On/Off**: It helps balance connectivity convenience and energy conservation by automatically enabling or disabling the wireless network at specific times (e.g., turning it off during sleep hours to reduce unnecessary power consumption).

- **Switch TX Power**: It refers to adjusting wireless transmission power (which determines signal strength and coverage) automatically at specific times, balancing performance and energy efficiency (e.g., reducing power during low usage).

### MLO Wi-Fi Schedule

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-MT3600BE (Beryl 7)    |    √    |
| GL-BE6500 (Flint 3e)     |    √    |
| GL-BE9300 (Flint 3)      |    √    |
| GL-BE3600 (Slate 7)      |    √    |

You can set an on/off schedule for both the MLO Main Wi-Fi and Guest Wi-Fi.

Enable the Main or Guest Wi-Fi Schedule, set the on and off times, select the weekly effective dates, and then click Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### 6 GHz Wi-Fi Schedule

| Supported Models         |         |
| :----------------------- | :-----: |
| GL-BE9300 (Flint 3)      |    √    |

When the Wi-Fi schedule mode is **Turn On/Off**, you can set an on/off schedule for both the 6 GHz Main Wi-Fi and Guest Wi-Fi. 

Enable the Main or Guest Wi-Fi Schedule, set the on and off times, select the weekly effective dates, and then click Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

When the Wi-Fi schedule mode is **Switch TX Power**, you can set a TX power switching schedule for the 6 GHz Main Wi-Fi. Note that 6 GHz Guest Wi-Fi is not supported for this schedule mode.

Enable the Main Wi-Fi Schedule, set two timed actions to switch TX power, select the weekly effective dates, and then click Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Set TX Power to a certain level (e.g., Low) at a specific time (e.g., 22:00).
- **Restore**: Restore TX Power to another level (e.g., Max) at another time (e.g., 07:00).
- **days**: Select the effective days of the week for these settings.

### 5 GHz Wi-Fi Schedule

When the Wi-Fi schedule mode is **Turn On/Off**, you can set an on/off schedule for both the 5 GHz Main Wi-Fi and Guest Wi-Fi. 

Enable the Main or Guest Wi-Fi Schedule, set the on and off times, select the weekly effective dates, and then click Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

When the Wi-Fi schedule mode is **Switch TX Power**, you can set a TX power switching schedule for the 5 GHz Main Wi-Fi. Note that 5 GHz Guest Wi-Fi is not supported for this schedule mode.

Enable the Main Wi-Fi Schedule, set two timed actions to switch TX power, select the weekly effective dates, and then click Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Set TX Power to a certain level (e.g., Low) at a specific time (e.g., 22:00).
- **Restore**: Restore TX Power to another level (e.g., Max) at another time (e.g., 07:00).
- **days**: Select the effective days of the week for these settings.

### 2.4 GHz Wi-Fi Schedule

When the Wi-Fi schedule mode is **Turn On/Off**, you can set an on/off schedule for both the 2.4 GHz Main Wi-Fi and Guest Wi-Fi. 

Enable the Main or Guest Wi-Fi Schedule, set the on and off times, select the weekly effective dates, and then click Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

When the Wi-Fi schedule mode is **Switch TX Power**, you can set a TX power switching schedule for the 2.4 GHz Main Wi-Fi. Note that 2.4 GHz Guest Wi-Fi is not supported for this schedule mode.

Enable the Main Wi-Fi Schedule, set two timed actions to switch TX power, select the weekly effective dates, and then click Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Set TX Power to a certain level (e.g., Low) at a specific time (e.g., 22:00).
- **Restore**: Restore TX Power to another level (e.g., Max) at another time (e.g., 07:00).
- **days**: Select the effective days of the week for these settings.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
