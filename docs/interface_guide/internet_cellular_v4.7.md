# Connect to the Internet via cellular (Firmware v4.7 and earlier)

!!! note

    This guide is based on firmware v4.7 and earlier. If you are using the latest firmware version, please check [here](internet_cellular.md).

---

Most GL.iNet routers support cellular connectivity. This guide covers three types of models:

1. **Built-in 4G Single-SIM models**

    Some models include a built-in 4G module with a single SIM card slot, such as the GL-XE300 (Puli). Please refer to [Setup for Single-SIM models](#setup-for-single-sim-models).

2. **USB Modem compatible models**

    Some models feature a USB port and support cellular connectivity via a USB modem, such as the GL-AXT1800 (Slate AX). The setup steps are similar to those of the built-in 4G single-SIM models. Please refer to [Setup for Single-SIM models](#setup-for-single-sim-models).

3. **Built-in 5G Dual-SIM models**

    Some models include a built-in 5G module with dual SIM card slots, such as the GL-X3000 (Spitz AX). The cellular settings in the web Admin Panel may differ slightly. Please refer to [Setup for Dual-SIM models](#setup-for-dual-sim-models).

**Note:** Some SIM cards require activation before first use. To ensure compatibility, activate the SIM card in a smartphone before inserting it into the router.

## Setup for Single-SIM models

The following steps apply to models with a built-in cellular modem and a single SIM card slot (e.g., GL-XE300 Puli), or a USB port for connecting an external USB modem (e.g., GL-AXT1800 Slate AX).

Here we use the **GL-AXT1800 (Slate AX)** with an external USB modem as an example.

We recommend powering off the router first. Insert a pre-activated SIM card into the USB modem, then plug the modem into the router's USB port. After that, power on the router.

If you plug the USB modem after the router has booted up, the web Admin Panel may not update automatically. In that case, please refresh the page or restart the router.

### Auto Setup

Log in to the router's web Admin Panel and navigate to **INTERNET** -> **Cellular**.

1. When you access it for the first time, it may not connect automatically, but it should display the name of your carrier in the upper left corner, and the IMEI. Click **Auto Setup**.

    Ignore the warning of *Incompatible Modem*

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. It will start connecting.

    **Note:** Some SIM cards may have special usage restrictions, such as requiring a specific APN. If your SIM card fails to register, contact your carrier to check for special restrictions.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Once connected, the page will display the network details with a green dot, indicating a successful connection.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Note:** After initial setup, if you restart the router with the USB modem plugged in, or replug the modem, the USB modem will be recognized automatically, and the network connection will be established without clicking the Auto Setup button again.

If Auto Setup fails, please try [Manual Setup](#manual-setup).

### Manual Setup

In the Cellular section, click **Manual Setup** to view or modify the cellular settings of the current SIM card. 

**Note**: Some SIM cards may require a specific APN. If your SIM card fails to register, please contact your carrier to check for any restrictions. Configure the correct APN on your router if necessary. 

Applying the changes will trigger a reconnection.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: The cellular communication protocol (e.g., 3G, QMI, or QCM). This is usually auto-detected, and you can change it to match your modem and carrier requirements.

- **Port**: The serial port used to communicate with the cellular modem. This is usually auto-detected and does not require manual adjustment.

- **APN**: APN (Access Point Name) is a gateway parameter required for a cellular network connection. It allows the router to connect to the internet provided by your mobile carrier. You can use the default APN or set a custom APN provided by your carrier.

- **PIN**: If your SIM card is protected by a PIN code, enter it here. This field is optional if no PIN is set.

- **TTL**: TTL (Time To Live) defines the maximum time packets can survive in the network. By default, the router decrements the TTL of incoming packets from client devices by 1 before forwarding them. If you need to override it, you can set a fixed value here. The TTL setting is valid only for IPv4.

- **Service**: Select the cellular service type to define the network technologies the modem will use.

- **Dial Number**: Enter the dial-up number provided by your carrier. This is often pre-configured and may be left blank for most modern networks.

- **Authentication**: Choose the authentication method required by your carrier (e.g., NONE, PAP, CHAP). This is usually set to NONE if no credentials are needed.

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

- **QMI**: This modem supports QMI mode. Please select QMI as the protocol, and **/dev/cdc-wdm0** as the serial port for your cellular router.

- **Host-less**: This modem supports Tethering mode. Please manage the connection via the router's Tethering interface rather than the Cellular interface.

## Setup for Dual-SIM models

The following steps apply to models with a built-in cellular modem that supports dual SIM cards. The web Admin Panel may differ slightly from single-SIM models.

Here we use the **GL-X3000 (Spitz AX)** as an example. It supports Dual SIM, Single Standby, which means it can hold two SIM cards for cellular access, but only one SIM card can be active at a time. You can manually switch between the two SIM cards.

We recommend you power off the router first, insert your pre-activated SIM card(s) into the slots, then power it on. If you insert the SIM card after the router has booted up, the web Admin Panel may not update automatically. In that case, please refresh the page or restart the router.

### Auto Setup

Log in to the router's web Admin Panel and navigate to **INTERNET** -> **Cellular**.

1. When no SIM card is inserted, the page displays as follows.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. When a SIM card is inserted, the router will start connecting automatically.

    If the connection is successful, the page will display as follows.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

If it does not connect automatically, click **Auto Setup** and wait for the router to connect, or try **Manual Setup**.

### Manual Setup

In the Cellular section, click **Manual Setup** to enter the Cellular Settings.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

You can view or modify the cellular settings of the current SIM card. It also stores some pre-configured profiles, and you can manually add configurations to the "Saved Settings".

### SIM Card Slot Settings

In the Cellular section, click **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

You will enter the **SIM Card Slot Settings**.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

If two SIM cards are inserted, you can enable **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

- **Auto Switch**: Enables automatic switching between SIM 1 and SIM 2. The network detection method for SIM Auto Switch is the same as the one configured on the Multi-WAN page.

- **Preferred SIM Card Slot**: Please set the preferred SIM card to SIM 1 or SIM 2.

- **Failover Interval**: Available values range from 5 minutes to 24 hours.

    If the internet connection is still unavailable after a failover, the device will switch back to the preferred SIM slot and wait for this interval before retrying failover.

    This option applies when both the preferred SIM card and the backup SIM card have no signal. The device will switch between SIM cards until one of them obtains a valid signal.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled** 
    
    When enabled, the device will check the preferred SIM slot daily at the configured time and attempt to switch back if the preferred SIM regains internet access.
    
    This prevents the backup SIM from consuming excessive data. If the preferred SIM still has no signal, the device will continue using the backup SIM.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Note**: The Auto Switch feature does not switch to another SIM card immediately. First, the device needs time to confirm that the current SIM cannot access the internet. Second, the other SIM is not in standby mode and requires time to activate.

## Traffic Statistics

In the Cellular section, click **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

You will enter the Traffic Statistics page. 

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

Please refer to the [SMS tutorial](sms.md).

## SMS Forwarding

Please refer to the [SMS Forwarding tutorial](../tutorials/sms_forwarding.md).

## Modem Management

In the Cellular section, click the **Tool** button in the upper-right corner to enter the Modem Management page.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

It includes two sections: **Modem Info** and **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

AT commands are standard instructions used to communicate with the cellular modem.

When Shortcut is set to **Manual command**, type your desired command in the AT Command field to check the modem status.

You can also click the Shortcut drop-down to select from a list of **preset commands**.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

The following commands are available as presets:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

As an example, the shortcut "Request IMEI" is selected here. Click "Send" and you will get the result as shown below.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Carrier profile

You can save different profiles for the same or different carriers.

In the Cellular section, click the **Profile** button in the upper-right corner to manage profiles.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Add a new profile or save the current profile.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Create your own profile based on your carrier's requirements.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

You can select a saved profile next time.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Choose any profiles you needed

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Lock Tower

This feature is available only on GL-X3000, GL-XE3000, and GL-X2000 (firmware ver.4.7 or later).

If you want to receive a high-quality signal and ensure a stable cellular connection, you can try locking tower.

**Note:** The locked tower must match the frequency bands supported by your carrier and device; otherwise, the connection may fail.

In the Cellular section, click the **Tower** icon in the upper-right corner.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

It will display the available towers.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Click a tower to view the details and lock onto it.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

The tower status (e.g., Locked/Unlocked) will be displayed at the top.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Note**: 

1. The device may not be able to scan all towers when the Cellular interface is enabled.

2. If the locked tower does not match the band masking or APN parameters in your cellular settings, the router will not be able to connect to the cellular network.

3. After locking a cell tower, if you move the router to another location, it will still attempt to reconnect to the locked tower after rebooting. This may prevent the router from connecting to the cellular network automatically at the new location. In this case, you need to either unlock the current cell tower, or manually lock it to a new tower.

## Historical Signal Record

In the Cellular section, click the **Signal** icon in the upper-right corner to check the historical signal strength.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

This helps you determine the quality of your cellular connection. If the signal is weak, try switching towers for a better signal.

You can view the cellular signal strength history by selecting different time frames.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking

In the Cellular section, click **View More** and select **Cells Info** to check the cells details.

You will see the current bands you are using and their signal status.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

If the signal is weak, you can enable Band Masking to block certain bands. Alternatively, if the signal is good, you can allow the router to use only specific cellular bands.

Click **Manual Setup** to enter the Cellular Settings page, then enable **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Select the **Masking Mode** (Block or Open), then select the LTE Bands, 5G NSA Bands, and 5G SA Bands.

## Troubleshooting

If you fail to establish a cellular connection, click the error message below for relevant solutions.

??? note "No SIM / Your SIM card has not been detected"
    
    1. Refresh the page and wait a few minutes to check if the SIM card can be detected.
    
    2. Ensure the SIM card is installed correctly. Align the notch on the SIM card with the corresponding mark on the card slot to confirm proper insertion orientation.
    
    3. Power off the router, remove and reinsert the SIM card, then power the router back on.
    
    4. Try using another SIM card if available.

    If the issue persists, download the logs and send them to [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Refresh the page and wait a few minutes to check if the error disappears.
    
    2. Click **Disconnect**/**Abort**, then click **Connect** to try reconnecting.
    
    3. Restart the router.
    
    4. Verify the SIM card status and ensure it is activated. Test the SIM card by inserting it into a smartphone to confirm it can access the internet normally with an active mobile data plan, or contact your network carrier for verification.
    
    5. Some network carriers may require a 3G protocol for network connection. Please go to **Manual Setup** -> **Cellular Settings** -> **Protocol**, select **3G**, then click **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        The device will reconnect automatically. Wait a few minutes to check if the connection is successful.

    6. Some SIM cards may have special usage restrictions (e.g., requiring a specific APN). If your SIM card fails to register, contact your carrier to check for any restrictions. 
    
        If necessary, go to **Manual Setup** -> **Cellular Settings** -> **APN**, configure the correct APN on the router, then click **Apply**.

    7. Click **View More** and select **Cells Info** to check the cellular signal strength. If the signal is weak, ensure the antenna is installed correctly. Move the router to an open and unobstructed location for better signal reception.
    
    8. Check if **Band Masking** or **Lock Tower** is enabled. If so, disable the feature and try reconnecting.

    If the issue persists, download the logs and send them to [support@gl-inet.com](mailto:support@gl-inet.com).

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
