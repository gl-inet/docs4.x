# Connect to the Internet via cellular (Firmware v4.7 and earlier)

!!! note

    This guide is based on firmware v4.7 and earlier. If you are using the latest firmware version, please visit [here](internet_cellular.md).

Most GL.iNet routers can be used to access the Internet through cellular.

There are three cases:

1. Some models have a built-in 3G/4G module with single SIM card, such as GL-XE300 (Puli). Please refer to [Setup for single SIM models](#setup-for-single-sim-models).

2. Some models have a USB port and can be plugged with a USB 3G/4G modem, such as GL-AXT1800 (Slate AX). Please refer to [Setup for single SIM models](#setup-for-single-sim-models).

3. Some models have a built-in modem and support dual SIM cards, such as GL-X3000 (Spitz AX). Its web admin interface may be slightly different. Please refer to [Setup for Dual-SIM models](#setup-for-dual-sim-models).

**Note:** Some SIM cards may need to be activated the first time you use them. Please activate them on your phone before using them in the router.

## Setup for single SIM models

The following configuration steps are for built-in modem or external USB modem with only single SIM card. Here we use the GL-AXT1800 (Slate AX) with external USB modem as an example.

We recommend turning off the router first, inserting your SIM card into the USB modem then plugging the USB modem into the USB port of the router, and then turning it on again. If you insert a USB modem after the startup, the page may not change. Please refresh the page.

### Auto Setup

On the left side of web Admin Panel -> INTERNET -> Cellular section.

1. When you access it for the first time, it may not connect automatically, but it should display the name of your carrier in the upper left corner and show the IMEI. Please click Auto Setup.

    Ignore the warning of *Incompatible Modem*

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. Connecting.

    **Note:** Some SIM cards may have special usage restrictions, such as the need to use a special APN. If your SIM card can't be registered, please consult your network operator if it has special restrictions.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. After a while, it will be connected. Otherwise, try [Manual Setup](#manual-setup).

    **Note:** After the initial setup, when you restart the router (with the USB modem still plugged in), or when you insert the USB modem into the router for the second time and power on the router, usually the USB modem can be automatically recognized and a cellular network connection can be established without the need to click "Auto Setup" again. At this time, information such as the cellular signal, modem name, and IMEI may not be displayed on the router management interface, but the network connection may already be working properly. 

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

### Manual Setup

Sometimes, Auto Setup may not work, you can try Manual Setup.

In the Cellular section, click **Manual Setup**.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

### Compatible Modems

Here is a list of supported modems that we had tested before.

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | Yes    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | Yes    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Yes    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Yes    | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | Yes    | akw2312         |           |
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
| Verizon U620L (Verizon)                | 4G    | Yes    | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | Yes    | anonymous       | Host-less |

**QMI**: This modem supports QMI mode. Please choose **/dev/cdc-wdm0** in the Device list.

**Host-less**: This modem supports tethering mode. Please set up by using Tethering but not 3G/4G modem.

You can also search on the [forum](https://forum.gl-inet.com){target="_blank"} or create a post for asking.

## Setup for Dual-SIM models

Some models have a built-in modem that supports dual SIM cards, and the interface may be slightly different compared to models with only one SIM card. 

Taking the GL-X3000 (Spitz AX) as an example. It supports "Dual SIM, Single Standby", which means it can hold two SIM cards for internet access, but only one SIM card can be active at a time. Users can switch between the two SIM cards.

We recommend turning off the router first, inserting your SIM card into the slot, and then turning it on again.

On the left side of web Admin Panel -> INTERNET -> Cellular section.

1. When there's no SIM card detected, the page is displayed as below.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. When a SIM card is inserted, the router will start connecting automatically.

    If the connection is successful, the page will appear as shown below.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

    If it does not connect automatically, click **Auto Setup** and wait for the cellular connection.

### SIM card slot settings

In the Cellular section, click **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

You will enter the SIM Card Slot Settings.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

If there are two SIM cards inserted, you can enable **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

* Auto Switch

    It allows auto switch between SIM 1 and SIM 2. 
    
    The networking status detection method of SIM card Auto Switch is the same as that configured in the Multi-WAN page.

* Failover Interval

    The options range from 5 minutes to 24 hours.
    
    If the Internet connection is still not available after failover has occurred, the device will switch back to the preferred SIM slot and will only retry failover after this interval.

    This option applies when both the preferred SIM card and the backup SIM card have no signal. If the preferred SIM card also has no signal, the device will switch to the backup SIM card and so on until one of the SIM cards has a signal.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_card_slot_settings_failover_interval.png){class="glboxshadow"}

* Checking Preferred Slot Status Scheduled

    If this option is enabled, the device will try to switch back to the preferred SIM slot at the specified time. This feature allows you to switch back to the preferred SIM slot when its internet connection is available.

    When this feature is enabled, the device will attempt to switch to the preferred SIM at this set time each day, for example, this feature is intended to prevent the backup SIM from using too much data, and if the preferred SIM still has no signal, it will fail to switch to the backup SIM.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_card_slot_settings_checking_preferred_slot_status_scheduled.png){class="glboxshadow"}

**Note**: The Auto Switch feature does not immediately switch to another SIM card. On one hand, it takes time to confirm that the current SIM card cannot access the internet, and only after confirming this will it switch. On the other hand, the other SIM card is not in standby mode, so it also takes some time to activate it.

### Traffic Statistics

In the Cellular section, click **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

You will enter the Traffic Statistics page.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

### Manual Setup

Click **Manual Setup** button, it will pop up the Cellular Settings dialog.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

You can view or modify the cellular settings of the current SIM card. It also stores some pre-configured settings, and you can manually add configurations to the "Saved Settings" as well.

## SMS

Please refer to the [SMS tutorial](sms.md).

## SMS Forwarding

Please refer to the [SMS Forwarding tutorial](../tutorials/sms_forwarding.md).

## Modem Management

Click the tool button to enter the modem management page.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

It includes information about the modem and AT commands.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

Modem AT commands are instructions that are used to control modems.

When the "Shortcut" option is selected as "Manual command", you can enter the command to be executed in the "AT Command" field.

You can also click the "Shortcut" to switch to other preset commands.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

The following AT Commands have been pre-set.

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

As an example, the shotcut "Request IMEI" has been selected here. Click "Send" and you will get the result as below.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Carrier profile

You can save different profiles for the same or different carriers.

Click Manage profile

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Add a new  profile or save the current profile

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Create the carrier own profile base on your needs

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

You can select a saved profile next time

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Choose any profiles you needed

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Signal Tower Lock

Click the signal tower icon.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Select an available signal tower and lock it.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

The device may not be able to scan all towers when the Cellular interface is enabled.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

If the locked tower does not match the band masking or APN parameters in the cellular settings, the cellular interface will not be able to connect to the Internet.

The tower lock status (e.g., Locked/Unlocked) is displayed at the top.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

## Historical Signal Record

You can select INTERNET on the left side of the GL-inet admin panel, scroll down to the Cellular section on the right side and click on the icon to bring up the pop-up window Historical Signal values

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Checking your router's signal strength can help you determine the quality of your Internet connection. If the quality of your internet connection is poor, you can try switching to get a better signal.

You can view Cellular's signal strength history by selecting different time frames.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking

You can check to the band signals by click **view more** in **cells info** and decide which band with stronger signal and which band with weaker signal. Then you can force your router just connect to bands you want or never connect to some bands you don't want. 

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Check **Block** or **Open** and select the below for bands you want to apply.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

## Warning

When the Cellular Internet is not available, a warning will be displayed at the top of the Cellular section. 

Warning: The interface is connected, but the Internet can't be accessed.

Solution: Please check if the SIM card has internet access in a smart phone.

## IoT Certification

### AT&T Certification

Click the link [att device certification](https://iotdevices.att.com/certified-devices.aspx#) and input the device name, you can find it. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile Certification

Click the link [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) and choose 5G in **Filter**, you can find it. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Related Articles

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
