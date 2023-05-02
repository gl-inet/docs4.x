# Connect to the Internet via cellular

The router can be used to access the Internet through cellular. There are two cases, some models have a built-in 3G/4G model; some models have a usb port and can be plugged into a usb 3G/4G modem. The operation steps are similar, here is GL-AXT1800(Slate AX) as an example.

Some models have built-in modems and support dual SIM cards, and the interface may be slightly different. Please refer to [Dual-SIM](#dual-sim).

## Setup

On the left side of web Admin Panel -> INTERNET, Cellular sector.

**Note:** Some SIM cards may need to be activated the first time you use them, so please activate them in your phone before using them in your router.

1. We recommend to turn off the router first, insert your SIM card into the USB modem then plug the USB modem into the USB port of the router, and then turn it on again. If you insert a usb modem at power on, the page may be no change, please refresh the page.

2. Please access the web Admin Panel -> INTERNET, Cellular sector. The first time, it may not connect automatically, but it has read the name of your carrier in the upper left corner and the IMEI, then please click **Auto Setup**.

    Please ignore the warning of *Incompatible Modem*

    ![usb modem auto setup](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

3. Connecting.

    **Note:** Some SIM cards may have special usage restrictions, such as the need to use a special APN. If your SIM card can't be registered, please consult your network operator if it has special restrictions.

    ![usb modem connecting](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

4. After a while, it will be connected. Otherwise, try [Manual Setup](#manual-setup).

    When the usb modem is plugged into the router the second time it is powered on, it is usually automatically recognized and a connection is established. It may not get the information of signal, modem name and IMEI.

    ![usb modem connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

---

### Manual Setup

Sometimes, **Auto Setup** may not work, you can try **Manual Setup**.

![4g modem manual setup](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/cellular_settings.png){class="glboxshadow"}

---

### Compatible Modems

Here is a list of supported modems that we had tested before.

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel UC20-E                         | 3G    | Yes    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Yes    | GL.iNet         |           |
| Huawei E1550                           | 3G    | Yes    | GL.iNet         |           |
| Huawei E3276                           | 4G    | Yes    | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G    | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Yes    | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Yes    | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Yes    |                 | Host-less |

*QMI: This modem supports QMI mode. Please choose **/dev/cdc-wdm0** in the **Device** list.

*Host-less: This modem supports tethering mode, please set up by using Tethering but not 3G/4G modem.

You can also search on the [forum](https://forum.gl-inet.com){target="_blank"} or create a post for asking.

## Dual-SIM

Some models have built-in modems and support dual SIM cards, and the interface may be slightly different. Take the GL-X3000 (Spitz AX) as an example.

When no SIM card is detected.

![dual-sim, no sim](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

When a SIM card is inserted.

![dual-sim, 5g sim](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Click current sim card.

![dual-sim, current sim card](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

It will open the SIM card slot settings dialog box.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

If two SIM cards are inserted, you can enable Auto Switch.

![dual-sim, auto switch](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

* Auto Switch

    The Internet status is detected in the same way as the settings in the Multi-WAN page.

* Failover Interval

    If Internet connection is still not available after failover, the device will switch back to the preferred SIM slot and will only retry failover after this interval.

* Checking Preferred Slot Status Scheduled

    If this option is enabled, the device will try to switch back to the preferred SIM slot at the specified time. So that you can switch back to using the preferred SIM slot when its internet connection is available.

## SMS

Please refer to the [SMS tutorial](../sms).

## SMS Forwarding

Please refer to the [SMS Forwarding tutorial](../sms_forwarding).

## Modem Management

Click the button to go to modem management page.

![modem management button](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/modem_management_button.png){class="glboxshadow"}

It includes information about the modem and AT commands.

![modem management](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/modem_management.png){class="glboxshadow"}

Modem AT commands are instructions that are used to control modems.

When the 'Shortcut' option is selected as 'Manual command', you can enter the command to be executed in the 'AT Command' field.

The following AT Commands have been pre-set.

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

## Warning

When Internet access is not available, the corresponding warning is displayed. To determine whether you can access the Internet or not, please go to [Multi-WAN](../multi-wan) page.

- Warning: *The interface is connected, but the Internet can't be accessed with IPv4 protocol.*

    Solution: Please check if the sim card has internet access in a smart phone.

---

Related Articles

- [Internet page](../internet)
- [How to set the priority of each Internet access method?](../multi-wan/)
- [How to set the load balance when multiple Internet access methods are used at the same time?](../multi-wan/)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
