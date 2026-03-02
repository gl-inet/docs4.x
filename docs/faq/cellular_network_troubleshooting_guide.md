# Cellular Network Troubleshooting Guide

If you cannot establish a cellular connection, please check for the following issues.

??? "Check device hardware"

    **1.1** Use a standard power adapter for your device. Non-standard power adapters may cause insufficient power supply.
    
    **1.2** Make sure the **Modem name**, **IMEI** and **SIM ICCID** are displayed on the web Admin Panel.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}
    
    For firmware ver.4.8 and later, click **View More Information** to find the SIM ICCID.

    If you cannot find them, restart your router. If the modem name and IMEI still cannot be recognized, please contact us at [support@gl-inet.com](mailto:support@gl-inet.com).
    
    **1.3** Click **View More** to check the **Cells Info** and confirm that the signal is stable. If the signal is very weak, ensure the antennas are installed correctly, or move the router to an area with good signal and test again.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}
    
    **1.4** Click **View More** to check if the frequency band supported by your device is compatible with your region.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Check software settings"

    **2.1** Log in to the web Admin Panel and ensure the cellular connection program has been started. You can also click **Abort** and then click **Connect**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}
    
    **2.2** Some network carriers may require the **3G protocol** to connect. Switch to 3G protocol and test again.

    For firmware ver.4.7 and earlier, go to **Manual Setup** -> **Protocol**, select **3G**, then click **Apply**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    For firmware ver.4.8 and later, go to **SIM Card Settings** -> **Protocol**, select **3G**, then click **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    The device will reconnect automatically. Wait a few minutes to check if the connection is successful.

    **2.3** Some SIM cards require a specific APN. If your SIM card fails to register, contact your carrier to check for any restrictions. Configure the correct APN on your router if necessary, then click **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}
    
    **2.4** Enable **Band Maksing** and test again. For firmware ver.4.7 and earlier, refer to [this link](../interface_guide/internet_cellular_v4.7.md/#band-masking). For firmware ver.4.8 and later, refer to [this link](../interface_guide/internet_cellular.md/#band-masking).

    **2.5** Lock or unlock a signal tower and test again. This feature is available only on GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) and GL-X2000 (Spitz Plus). Click [here](../interface_guide/internet_cellular.md/#lock-tower) for more instructions.
    
    Locking to a specific signal tower allows the router to access a high-quality network resource and maintain stable cellular connectivity.
    
    However, once a tower is locked, the router will keep trying to reconnect to it after rebooting even if moved to a new location. This may prevent the router from connecting to the cellular network automatically. If this happens, you can either unlock the current tower via the router's web admin panel or manually lock it to a new tower.

    **Note:** The locked tower must match the frequency bands supported by your carrier and device; otherwise, the connection may fail.

??? "Check SIM compatibility"
    
    **3.1** Confirm the SIM type. GL.iNet cellular routers are certified as IoT devices. In theory, the device supports only IoT‑type SIM cards. If you are unsure about the SIM type, please contact your carrier.
    
    Common SIM types include: data‑only, data‑only + voice, IoT, and hotspot. We recommend using IoT or hotspot SIM cards. Data-only or data-only + voice SIM cards are not guaranteed to work.
    
    **3.2** Some SIM cards must first be activated. Make sure the SIM card can access the Internet when inserted into a phone, then move it to the router.
    
    **3.3** Some customized SIM cards can only be used on mobile phones or specific devices. Please confirm whether the SIM card is locked to a particular device.
    
    **3.4** In some states or cities in the United States (e.g., AT&T in Seattle), you may need to register the device IMEI with your carrier. If you are unsure about the registration, please contact your carrier.
    
    **3.5** If the web Admin Panel shows "SIM card not registered", try the steps above first.

    We recommend you power off the router, insert the SIM card, then restart the router. Some models do not support hot swapping and may fail to detect the SIM card if inserted while powered on.

    Make sure all antennas are properly installed, then test again in an outdoor area with strong cellular signal. Weak signal may prevent the SIM card from registering on the network.

    If the problem persists, the SIM card may be incompatible with the router. Contact your network carrier for further assistance.

    If your carrier confirms the issue is not related to the SIM card, please contact our support team at [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** If the SIM card can register and obtain an IP address but cannot access the Internet (upload works but download does not), the SIM card is most likely restricted by your network carrier. Contact your carrier to remove the restriction, or set TTL to 65 and test again as shown below.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    When contacting your network carrier, please provide your device modem name, IMEI, SIM ICCID, and router model.
    
If none of the above solves the problem, please contact our support team at [support@gl-inet.com](mailto:support@gl-inet.com).
