# Comet (GL-RM1) User Guide

GL-RM1 is an open - source remote KVM device with a wide range of applications. For business travelers, it enables remote control of office computers during trips, facilitating access to crucial documents. IT maintenance personnel can use it to remotely manage servers and quickly resolve issues.

It supports remote control of offline devices, allowing you to handle computer boot failures and adjust BIOS settings. It also has a remote file transfer function, enabling easy data transfer for both online and offline computers. With audio support, it provides a more immersive remote interaction experience. In a word, it is an essential tool for remote work and device management.

## Quick Setup Guide

This section will guide you how to set up GL-RM1 quickly. Connect the device, remote and local access to the controlled device.

### Connect the Devices

Connect GL-RM1 to the device you want to control according to the diagram below.

![connect devices](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/connect_devices_1.png){class="glboxshadow"}
![connect devices](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/connect_devices_2.png){class="glboxshadow"}

### Remote Access to the Controlled Device

Follow the steps below.

1. Install the [App](https://link.gl-inet.com/label-rm1-app/){target="_blank"} on your Remote Control Device.

2. Register an Account.
    
    Register a glinet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/sign_up_account.png){class="glboxshadow gl-80-desktop"}

3. Log in to your Account.

    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/log_in.png){class="glboxshadow gl-80-desktop"}

4. Bind your GL-RM1.

    There are two methods to bind GL-RM1 to your account.

    === "Bind via Local Area Network"
    
        Please ensure that the current Remote Control Device is in the same local area network as the GL-RM1.

        Click "Add Device" and select your GL-RM1.

        ![add device via LAN](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/add_device_via_lan){class="glboxshadow gl-80-desktop"}

        ![select device](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/select_device_via_lan){class="glboxshadow"}

    === "Bind via Adding Manually"

        Click the "+" button in the upper right corner.

        ![click + button](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/add_button.png){class="glboxshadow"}

        Customize device name and input the S/N, which is printed on the label on the back of the device.

        ![add manually](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/add_manually.png)

You can now start using GL-RM1 to remote access your device.

### Local Access to the Controlled Device

If you want to locally access the controlled device via GL-RM1, find the IP address of GL-RM1 in its upper router, enter this IP address in the browser, you will be able to access the controlled device through GL-RM1 locally.

Take GL-AXT1800 as an example. Here we connect the GL-RM1 to the LAN port of GL-AXT1800 router through an Ethernet cable, so GL-AXT1800 is the upper router. Log in to the web admin panel of GL-AXT1800, the IP address of RM1 can be found in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Now you can use this IP to access your device locally via GL-RM1.

![local access](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/local_access.png){class="glboxshadow"}

## Function Introduction

=== "Settings"

    Move to the top navigation bar, click **Settings**, you will get a page as below.

    ![settings](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/settings.png){class="glboxshadow"}

    - Video

        It provides modifications of video quality and orientation. You can adjust the video quality according to the connection quality and resolution requirements, and adjust the viewing angles as well.

    - Remote Device Settings

        You can adjust the relevant settings of the controlled device.

        - Audio: Turn on or off the sound of the controlled device.
        - Mouse: Turn on or off the mouse of the controlled device.
        - Keyboard: Turn on or off the keyboard of the controlled device.
        - Show Virtual Keyboard: Whether to display and use the virtual keyboard on the control page.
        - Show Local Cursor: Whether to display the mouse of the current device on the screen.

    - System

        - Language: Switch the language of control page. 
        - Color Mode: Switch the theme color, including dark and light modes.

    - Security

        - Two-Factor Authentication: Enable two factor authentication (2FA) to protect your account.
        - Change Admin Password: Change your administrator password here.

            ![change admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/change_password){class="glboxshadow gl-60-desktop"}

=== "Toolbox"

    In the top navigation bar, click  **Toolbox**.

    ![toolbox](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/toolbox.png){class="glboxshadow"}

    - Clipboard

        The clipboard allows you to paste the text content of the control end into the controlled device.

    - Shortcut

        Here are some common shortcut key options. Click "ALL" to show all options.

        ![all shortcuts](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/shortcut_all.png){class="glboxshadow"}  

    - Terminal

        Access Terminal: You can access the terminal of GL-RM1 through this function.

        ![access terminal](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/access_terminal.png){class="glboxshadow"} 

=== "Accessories"

    GL.iNet provides you with accessories (optional), which you can connect to the GL-RM1 for use.

    In the top navigation bar, click  **Accessories**.

    ![accessories](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/accessories.png){class="glboxshadow"}

    - Fingerbot

        Insert the cover of the Fingerbot into the GL-RM1.
    
        - Time: The duration for which the Fingerbot presses.
        - Strength: Two levels of pressing strength are provided.

    - ATX Power

        - Power: Provides short press and long press functions.
        - Restart: Restart the device.

---

=== "Virtual Media"

    GL-RM1 allows you to transfer files from the host to GL-RM1, and then from GL-RM1 to the controlled device.

    In the top navigation bar, click  **Virtual Media**.

    ![virtual media](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/virtual_media.png){class="glboxshadow"}

    You can drag or click the box to upload files from host or from URL. As an example, two images were uploaded from the host to the GL-RM1 here.

    ![upload files](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/upload_files_example.png){class="glboxshadow"}

    You can perform operations such as deletion and download.

    - Mount To Remote

        Click "Mount To Remote", two options are provided: File Sharing and Image Mounting.
    
        ![mount to remote](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/mount_to_remote){class="glboxshadow"}
    
        - File Sharing: Emulates a read-write USB drive. Upload the files to the KVM (GL-RM1) and transfer from the host to the remoted device.

            Click "File Sharing", a window will pop up in the upper right corner of the control page.
    
            ![file sharing 1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/file_sharing_1){class="glboxshadow"}

            Check the GL-RM1 control page, go to "This PC" of your controlled device, you will see a Drive named "GLKVM(F:)". Now you can view, move or delete the files in this drive.

            ![file sharing 2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/file_sharing_2){class="glboxshadow"}
    
        - Image Mounting: Emulates a read-only CD-Rom, supports BIOS/UEFI boot, for system reinstallation or ISO-based software installation.

            GL-RM1 can simulate a read-only virtual CD/DVD or disk drive on the target host. You can access this drive during the BIOS or UEFI startup process. This function can help you reinstall the operating system or mount an ISO to install applications on the target host and other tasks.
    
            Click "Image Mounting", in the Mount Settings, select the image you need and click "Mount Image". The image will be mounting. 

            ![image mounting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/image_mounting){class="glboxshadow"}

            Then you can use this file on the controlled end.


=== "Help"

    You can upgrade the firmware version here. Local and Online Upgrades are supported.

    ![upgrade firmware](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/upgrade_firmware){class="glboxshadow"}

## Accessories

GL.iNet provides standard accessories that you can connect to the GL-RM1 for use.

### ATX Package

There are some components in the ATX Package box:

- ATX main board
- USB-A to Type-C cable
- 9 PIN Wire Set
- Screw package
- ATX Bracket Set

![components](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/conponents.jpg){class="glboxshadow gl-60-desktop"}

### PIN-OUT of the ATX Board

![pinout board](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/pinout_board.png){class="glboxshadow"}

Explanation of Interfaces with Marked Numbers

1. Type-C Interface: Connect to the RM1 device.
2. Firmware Upgrade button: for the single-chip microcomputer on the ATX main board.
3. Reset button.
4. Connect to the control line of the computer panel.
5. Connect to the F_PANEL interface of the computer.

!!! note

    Interfaces 4 and 5 can be connected interchangeably. That is, interface 5 can be connected to the control line of the computer panel, and interface 4 can be connected to the F_PANEL. The LED status on the board is consistent with the Power LED status on the computer panel.

Interfaces 4/5 diagram

![interface diagram 1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/interfaces.png){class="glboxshadow gl-60-desktop"}

![interface diagram 2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/interfaces_2.png){class="glboxshadow"}

### ATX Main Board Installation

Fix the ATX main board and the ATX Bracket Set with the screws provided.

![screw the mainboard and bracket](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/atx_board_installation/screw_the_mainboard_and_bracket){class="glboxshadow gl-60-desktop"}

Connect the fixed ATX board to the computer host box. Please pay attention to the insertion direction of the cable. 

![install atx board 1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/atx_board_installation/installation_1){class="glboxshadow gl-60-desktop"}

![install atx board 2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/atx_board_installation/installation_2){class="glboxshadow gl-60-desktop"}

Place the AXT board bracket on the side frame of the computer host box.

![install atx board 3](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/atx_board_installation/installation_3){class="glboxshadow gl-60-desktop"}

Connect the external interface to the USB-A interface of the GL-RM1 using the included USB-A to Type-C cable.

![install atx board 4](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/atx_board_installation/installation_4){class="glboxshadow gl-60-desktop"}

![install atx board 5](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-rm1/atx_board_installation/installation_5){class="glboxshadow gl-60-desktop"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.