# How to block specific client devices on a GL.iNet router

This tutorial will show you how to block specific client devices on a GL.iNet router. By blocking client devices, you prevent unauthorized access to your network. This helps to enhance your network security or control your family's access to the internet.

GL.iNet routers block client devices based on their MAC addresses (a unique 12-character identifier assigned to individual devices on a network). This method is also called MAC address filtering. 

There are two methods of blocking client devices on your GL.iNet router: via the [router admin panel](#block-client-devices-via-the-admin-panel) or the [GL.iNet mobile app](#block-client-devices-via-the-glinet-mobile-app). 

## Block client devices via the admin panel

### 1. Sign in to the admin panel

In a web browser, enter `192.168.8.1`. Enter your password, then click **Login**. 

### 2. Block client devices

There are two ways to block client devices, depending on whether you have their MAC addresses:

* If you do not have their MAC addresses: Use the [first method](#method-1-block-devices-without-their-mac-addresses) which allows you to block the devices that appear in the lists.
* If you have their MAC addresses: Use the [second method](#method-2-block-devices-with-their-mac-addresses). 

#### Method 1: Block devices without their MAC addresses

1. In the left sidebar, click **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Next to the device, toggle the switch to on. 
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

If you do not see the devices you want to block in the lists, you will need to block them by [adding their MAC addresses to the blocklist](#method-2-block-devices-with-their-mac-addresses). 

#### Method 2: Block devices with their MAC addresses

To use this method, you will need to obtain the MAC address of the device. Refer to the instructions provided by the device manufacturer. 
Once you have the device's MAC address, follow these steps: 

1. In the left sidebar, click **Clients**.
2. At the top, click **Blocklist**. 
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Follow either method to block devices: 
    - To enter the MAC addresses individually: Enter them in the empty field.
    - To import a list of MAC addresses: Click **Import Clients**. Import a file, then click **Import**. 
4. Click **Apply**. 
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Block client devices via the GL.iNet mobile app

**Note:** Before you start, install and set up the GL.iNet mobile app on your device. 

There are two ways to block client devices, depending on whether you have their MAC addresses:

* If you do not have their MAC addresses: Use the [first method](#mobile-1) which allows you to block the devices that appear in the list. 
* If you have their MAC addresses: Use the [second method](#mobile-2). 

### Method 1: Block devices without their MAC addresses {#mobile-1}

1. On the main app screen, tap the device you want to block under **Connected Clients** and **Office Clients**. 
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. Under **Settings**, toggle the **Block** switch to on. 
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

If you do not see the devices you want to block in the lists, you will need to block them by [adding their MAC addresses to the blocklist](#method-2-block-devices-with-their-mac-addresses-1)

### Method 2: Block devices with their MAC addresses {#mobile-2}

To use this method, you will need to obtain the MAC address of the device you want to block. Refer to the instructions provided by your manufacturer. 
Once you have the device's MAC address, follow these steps: 

1. On the main app screen, tap the Settings icon > **Access Control**. 
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Tap **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Follow either method to block devices: 
    - To enter the MAC addresses individually: Tap **Add MAC address**. Enter the MAC address, then tap **Done**.  
    - To import a list of MAC addresses, click **Import Clients** > **Import Clients**. Tap a file.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.