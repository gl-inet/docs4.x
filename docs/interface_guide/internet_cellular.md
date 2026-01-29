# Connect to the Internet via cellular/USB modem

!!! Note

    This guide is based on firmware v4.8. If you are using old firmware, please visit [here](internet_cellular_v4.7.md).
    
    Some features are only available in v4.8

---

Most GL.iNet routers support cellular internet access.

There are three scenarios:

1. Some models have a built-in 4G module with a single SIM card slot, such as the GL-XE300 (Puli). Please refer to [Setup for Single-SIM models](#setup-for-single-sim-models).

2. Some models have a USB port and can be plugged with a USB modem, such as the GL-MT3000 (Beryl AX). Please refer to [Setup for Single-SIM models](#setup-for-single-sim-models).

3. Some models have a built-in 5G module and support dual SIM cards, such as the GL-X3000 (Spitz AX). Their cellular settings on the web admin panel may be slightly different. Please refer to [Setup for Dual-SIM models](#setup-for-dual-sim-models).

**Note:** Some SIM cards may require activation upon first use. Please activate the SIM card on your phone before inserting it into the router.

## Setup for Single-SIM models

The following configuration steps apply to models with a built-in cellular modem and a single SIM card slot (e.g., GL-XE300 Puli), or a USB port for connecting an external USB modem (e.g., GL-MT3000 Beryl AX).

Here we use the **GL-MT3000 (Beryl AX)** and the external 5G development board **GL-M2** as an example. Since the GL-M2 has a built-in module, this connection is implemented through the router's Cellular interface. If using an external USB modem, the connection will instead be implemented through the router's Tethering interface.

We recommend powering off the router first. Plug the USB modem with a pre-installed SIM card into the router's USB port, then power the router back on. If you connect the USB modem after the router has started up, the web admin panel may not update automatically. Please refresh the page to check for changes.

### Auto Setup

Log in to the router's web Admin Panel, and navigate to **INTERNET** -> **Cellular** section.

1. When there's no SIM card inserted, the page displays a message "Your SIM card has not been detected". 

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_no_sim.png){class="glboxshadow"}

2. Insert a SIM card, and it will start connecting, as shown below. 

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    If it does not connect automatically, please click **Connect**.
    
    Ignore the warning of *Incompatible Modem* if any.

    ![incompatible modem](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/incompatible_modem.png){class="glboxshadow"}
    
    **Note:** Some SIM cards may have special usage restrictions, such as the need to use a special APN. If your SIM card cannot be registered, please consult your network operator if it has special restrictions.
    
3. Once the cellular network is connected, the page will display the network details with a green dot, which indicates a successful connection.
    
    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

    **Note:** After initial setup, if you restart the router with the USB modem still connected, or re-insert the modem into the router, the USB modem will be automatically recognized, and a network connection will establish without re-clicking "Connect".

If the Auto Setup failed, please try [Manual Setup](#manual-setup).

### Manual Setup

Sometimes, Auto Setup may not work, you can try Manual Setup.

In the Cellular section, click **SIM Card Settings**.

![manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_manual_setup.png){class="glboxshadow"}

You can view or modify the cellular settings of the current SIM card. It also stores some pre-configured settings, and you can manually add configurations to the "Saved Settings" as well.

Changing the configuration and applying it will result in redialing.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_card_settings_1.png){class="glboxshadow"}

If you want the router block certain bands or only use certain bands, you can enable **Band Masking**. 

Switch the Masking Mode between Block mode and Open mode, then select the LTE bands, 5G NSA Bands and 5G SA Bands.

![single sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_card_settings_2.png){class="glboxshadow"}

### Compatible Modems

Here is a list of supported modems that we had tested before. 

SIMPoYo uFi is a compact plug & play USB dongle with the Wi-Fi hotspot, designed for fast, reliable connectivity anywhere. It works seamlessly with most GL.iNet routers, as well as laptops, power banks, car USB ports, and other USB power sources. It comes with 10GB of free data for 30 days, valid in the UK, and 34 European countries. Click [here](https://www.gl-inet.com/campaign/simpoyo-ufi/) for details.

| Model                                  | Cellular | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| SIMPoYo 5G uFi                         | 5G    | Yes    | GL.iNet         |           |
| SIMPoYo 4G uFi SP-N150C4               | 4G    | Yes    | GL.iNet         |           |
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
| Huawei E3372                           | 4G    | Yes    | anonymous       |           |
| Huawei E3372h-320 (Ukraine)            | 4G    | Yes    | anonymous       | Host-less |
| TP-Link MA260                          | 3G    | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G    | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Yes    | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)             | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Yes    | anonymous       | Host-less |

**QMI**: This modem supports QMI mode. Please choose **/dev/cdc-wdm0** in the Device list.

**Host-less**: This modem supports tethering mode. Please set up by using Tethering but not 3G/4G modem.

You can also search on the [forum](https://forum.gl-inet.com){target="_blank"} or create a post for asking.

## Setup for Dual-SIM models

Some models have a built-in modem that supports dual SIM cards, and the interface may be slightly different compared to models with only one SIM card. 

Taking the GL-X3000 (Spitz AX) as an example. It supports "Dual SIM, Single Standby", which means it can hold two SIM cards for internet access, but only one SIM card can be active at a time. Users can switch between the two SIM cards.

We recommend powering off the router first, inserting your SIM card into the slot, and then powering the router back on.

### Auto Setup

Log in to the router's web Admin Panel, and navigate to **INTERNET** -> **Cellular** section.

1. When there's no SIM card inserted, the page displays a message "Your SIM card has not been detected". 

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. When there's a SIM card inserted, the page displays as follows. Click **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

3. Once the cellular network is connected, the page will display the network details with a green dot, which indicates a successful connection.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Click **View More Information** to show more cellular information, including the modem details, SIM card details, Internet details, and cellular details.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-80-desktop"}

If the Auto Setup failed, please try Manual Setup.

### Manual Setup

In the Cellular section, click **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

You can view or modify the cellular settings of the current SIM card. It also stores some pre-configured settings, and you can manually add configurations to the "Saved Settings" as well.
 
Changing the configuration will result in redialing.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

If you want the router block certain bands or only use certain bands, you can enable **Band Masking**. 

Switch the Masking Mode between Block mode and Open mode, then select the LTE bands, 5G NSA Bands and 5G SA Bands.

![sim card settings 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_3.png){class="glboxshadow"}

**Note:** Some SIM cards may have special usage restrictions, such as the need to use a special APN. If your SIM card can't be registered, please consult your network operator if it has special restrictions.

### SIM Card Slot Settings

In the Cellular section, click **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

You will enter the SIM Card Slot Settings. It displays the auto switch button, the activated SIM card, the ICCID and Network Operator.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

If two SIM cards are inserted, you can enable **Auto Switch**.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- Auto Switch. It allows auto switch between SIM 1 and SIM 2. 
    
    The networking status detection method of SIM card Auto Switch is the same as that configured in the Multi-WAN page.

- Preferred SIM Card Slot. Set the preferred SIM card as SIM 1 or Sim 2.

- Failover Interval. The options range from 5 minutes to 24 hours.
    
    If the Internet connection is still not available after failover has occurred, the device will switch back to the preferred SIM slot and will only retry failover after this interval.

    This option applies when both the preferred SIM card and the backup SIM card have no signal. If the preferred SIM card also has no signal, the device will switch to the backup SIM card and so on until one of the SIM cards has a signal.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_card_slot_settings_failover_interval.png){class="glboxshadow"}

- Checking Preferred Slot Status Scheduled. 
    
    If this option is enabled, the device will try to switch back to the preferred SIM slot at the specified time. This feature allows you to switch back to the preferred SIM slot when its internet connection is available.

    When this feature is enabled, the device will attempt to switch to the preferred SIM at this set time each day, for example, this feature is intended to prevent the backup SIM from using too much data, and if the preferred SIM still has no signal, it will fail to switch to the backup SIM.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_card_slot_settings_checking_preferred_slot_status_scheduled.png){class="glboxshadow"}

**Note**: The Auto Switch feature does not immediately switch to another SIM card. On one hand, it takes time to confirm that the current SIM card cannot access the internet, and only after confirming this will it switch. On the other hand, the other SIM card is not in standby mode, so it also takes some time to activate it.

## Traffic Statistics

In the Cellular section, click **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

You will enter the Traffic Statistics page. It displays the used data of SIM card(s), and provides data limit settings.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

If the Data Used exceeds the Data Cap Amount, please modify the **Data Cap Amount** or the **Data Used** manually. Otherwise, the network may be disconnected, or the SIM card may Auto Switch (for Dual-SIM models).

- **Modify the Data Used**

    Click on **Modify** on the right side of SIM 1/2 Data Used. 

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Then you can modify or reset the data used. 

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Set up SIM data limit**

    If you want to set up the SIM data limit, enable **Save data when power off** first. It means the data can be saved even after the device is powered off.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Then enable the SIM 1 or SIM 2 Limit Settings.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

For Dual-SIM models, we suggest enabling the **SIM Card Slot Auto Switch** at the same time. If the SIM 1 Data Cap Amount is set and the SIM Card Slot Auto Switch is enabled, SIM 1 will automatically switch to SIM 2 when it's data exceeds the Data Cap Amount and SIM 1 will be disabled.

## Historical Signal Record

In the Cellular section, click **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Checking your router's signal strength can help you determine the quality of your Internet connection. If the quality of your internet connection is poor, you can try switching to get a better signal.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

You can view the Cellular signal strength history by selecting different time frames in the upper right.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## SMS

Please refer to the [SMS tutorial](sms.md).

## SMS Forwarding

Please refer to the [SMS Forwarding tutorial](../tutorials/sms_forwarding.md).

## Lock Tower

This feature is only supported by GL-X3000, GL-XE3000, and GL-X2000 (firmware ver.4.7). 

If you want to receive high-quality signal sources to ensure stable cellular connection, you can try locking tower.

**Note:** Locking onto a base station requires matching the carrier and the device's supported frequency bands; otherwise, it may affect dialing. Please confirm the base station information to avoid potential issues.

In the Cellular section, click the three-dot icon in the upper right, then select **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Click Scan to start scanning the cellular towers or the base stations. It will take about a few minutes to scan the tower. 

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

When scanning, do NOT refresh the page.

It will display the available towers.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Click a tower to view the details and lock onto it.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

Please note that if the locked tower does not match the band masking or APN parameters in the cellular settings, the cellular interface will not be able to connect to the Internet.

After locking a signal tower, if the router is moved to another location, it will still attempt to reconnect to the locked tower after booting up. This may consequently prevent the router from connecting to the cellular network automatically at the new location. In this case, you need to either unlock the current signal tower via the router's web admin panel, or manually lock it to a new tower.

## Lock Operator

This feature is only supported by GL-X3000, GL-XE3000, and GL-X2000 (firmware ver.4.8). 

If you want to lock onto specific operator, in the Cellular section, click the three-dot icon in the upper right, then select **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

The operator lock function supports three modes: 

- Auto. Automatically connect to an available operator network.
- Manual. Manually lock onto a specific operator.
- Manual-Auto. Automatically switch to an available operator network if the manual lock fails.

![lock operatpr 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Modem AT Command

In the Cellular section, click the three-dot icon in the upper right, then select **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

You will enter the AT Command page.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Modem AT commands are instructions that are used to control modems.

When the 'Shortcut' option is selected as 'Manual command', you can enter the command to be executed in the 'AT Command' field.

You can also click the 'Shortcut' to switch to other preset commands.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

The following AT Commands have been pre-set.

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

As an example, the shortcut "Request IMEI" has been selected here. Click "Send" and you will get the result as below.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

In the bottom right corner, you can **Export Debug Info** and get a .json file. 

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

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
