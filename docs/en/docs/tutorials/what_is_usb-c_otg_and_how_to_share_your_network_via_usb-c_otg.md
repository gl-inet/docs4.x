# What is USB-C OTG and How to share your Network via USB-C OTG

## USB OTG
**USB OTG** (On-The-Go) is a USB standard that enables compatible devices like routers to switch between **Host** and **Device** roles, allowing direct data transmission and power interaction without a separate host device. 

The following two modes can be switched via **USB OTG**:

- When a device switches to **Host mode** via USB OTG, it acts as the bus master, initiating data transmission, supplying power, and governing all read and write operations between the two connected devices. 

- In **Device mode**, the device serves as a peripheral, drawing power from the host and responding passively to its commands, without the ability to initiate communication on its own.

## Network sharing via USB‑C OTG on Mudi 7

The OTG-enabled USB‑C port of the Mudi 7 operates in either **Device** or **Host** mode to enable flexible network sharing with external devices. Detailed scenarios are as follows:

### Connect to a Computer  

Most computers operate as hosts only and do not support OTG. When connected via USB, the router shows a mode selection window. Select any mode to auto-negotiate the role. The computer then recognizes it as a USB adapter for direct internet access, no extra drivers needed.

### Connect to a Smartphone
   
- **Device Mode**: The Mudi 7 acts as a USB device, sharing its network with the phone.
  
- **Host Mode**: When you enable USB Tethering on your phone, it can share its cellular network with the Mudi 7 via USB. This USB link can serve as an independent WAN interface, enabling Multi-WAN connectivity.

!!! Note

    1. When you are using the phone's OTG function to interconnect, ensure the phone supports OTG and use a data-capable USB cable. Charge-only cables cannot transmit network signals.   
    
    2. When Device Mode is enabled, the phone will not display a network connection notification. To verify functionality, check the network status in the phone's settings or run a connectivity test.   
   
        For example, if you are sharing the Mudi 7's network to a phone via **Device Mode** (e.g., iPhone 17 Pro), verify that Device Mode is active by following the steps below.

        1. Use a USB cable that supports OTG to connect the USB 3.1 port on the Mudi 7 to your iPhone 17 Pro.  
   
        2. On the Mudi 7, select **Device Mode**.    
   
            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. In your phone's settings, you will see that the Mudi 7 is providing network access to your phone, as shown in the screenshot below.   
   
            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.