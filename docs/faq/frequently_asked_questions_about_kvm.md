# Frequently Asked Questions about GL.iNet KVM

This document compiles commonly asked questions and answers about GL.iNet KVM (Remote Keyboard Video Mouse), designed to help you resolve issues quickly and use the device efficiently. 

If your question is not listed here, please contact our technical support team for further assistance.

## Basic Information

**Q1. What devices can GL.iNet KVM control?**

A1. GL.iNet KVM can be used to control any device that uses HDMI output and USB input, such as laptops, desktops, Raspberry Pi, mini hosts, etc.

---

**Q2. Do I need to install any software to use KVM?**

A2. No software is required to be installed on the controlled device. 

- When accessing the controlled device in the local area network (LAN), you can directly launch a browser on the controlling PC to access the KVM control panel; 
    
- For remote access, you need to install the GLKVM application on the controlling device, so as to access KVM and the controlled device.

---

**Q3. How do I access the device connected to GL-RM1 (Comet)? Through Web or a seperate application?**

A3. There are two methods: web or Application.

- Web is suitable for local LAN access, which means that the controlling devices and Comet need to be connected to the same LAN. Then enter "glkvm.local" on the web browser, you will be taken to the local management page. Alternatively, search for Comet's LAN IP address through the router, enter its IP address in the browser, it will take you to the local management page as well.

- Application is suitable for remote access. Install the GLKVM application on the controlling device, so as to access KVM and the controlled device.

---

**Q4. Do I need open ports for Comet to work (exposed to WAN) when accessing KVM from remote location?**

A4. No. No open ports or even a public IP is needed.

---

**Q5. Does it support Chrome OS?**

A5. The GLKVM application currently does not support installation on Chrome OS, so if your controlling device is running Chrome OS, remote access to KVM is not supported. However, you can locally access the controlled device through a web browser in the local LAN network.

---

**Q6. Does it support Linux OS?**

A6. Controlled devices running Linux operating system can be remotely accessed and controlled. If the controlling device runs Linux, installing the desktop application GLKVM is not supported, you can only access the controlled device using a web browser in the local LAN network.

---

**Q7. Can GL.iNet KVM connect to wireless network?**

A7. GL-RM1 (Comet) does not support connecting to wireless network.

---

## Power Management Related

**Q1. Can GL.iNet KVM control the power of a computer?**

A1. Sure. You can control the power of the controlled devices in the following ways:

- Wake on LAN (Built-in software service)

- [ATX board](https://docs.gl-inet.com/router/en/4/user_guide/gl-rm1/#atx-package) (Accessories, additional purchase required)

- [FingerBot](https://docs.gl-inet.com/router/en/4/user_guide/gl-rm1/#fingerbot) (Accessories, additional purchase required, Not yet available for sale)

---

**Q2. How to use ATX Board for remote power management?**

A2. Please refer to this [User Guide](https://docs.gl-inet.com/router/en/4/user_guide/gl-rm1/#atx-package).

---

## Features

**Q1. Do I have to use KVM cloud service?**

A1. No. You can choose to use or not use cloud service.

---

**Q2. What do I need for centralized device management?**

A2. You could get multiple Comet and bind them to one account on GLKVM, or get a KVM switch with hotkeys yourself.

---

**Q3. What is Wake On Lan?**

A3. Wake on LAN (WOL) is a technology that allows a computer or device to be remotely powered on or awakened from a low-power state over a network. It works by sending a "magic packet" containing the target device's MAC address, which triggers the device to start up. Common uses include remote administration, energy-saving standby configurations, and centralized system management.

---

## Troubleshooting

**Q1. Why can't I control the keyboard and mouse even if I have all wires connected?**

A1. Please confirm that the cable used is capable of data transmission, otherwise it will not be able to control the keyboard and mouse.

---

**Q2. Why can't my mouse cursor overlap with that on the controlled device screen when using macOS to remotely connect to KVM?**

A2. You can modify the resolution of the controlled computer to the appropriate parameters, or modify the EDID of the KVM to adjust it.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.