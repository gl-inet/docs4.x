# Cellular Network Troubleshooting Guide

**If you fail to connect, please check whether the following issues exist.**

??? "Please check device hardware"

    **1.1** Please use the device's standard power adapter. Non-standard power adapters may cause insufficient power supply.
    
    **1.2** Please confirm that you can find the modem name, IMEI number and SIM ICCID on the web. 
    
    If you cannot find them, please power off/on the device. If the modem name and IMEI number still cannot be recognized, please contact our customer service to return the device.
    
    **1.3** Please check the signal Cells info to confirm that the signal is normal. If the signal is very poor, please confirm that the antennas have been installed correctly, or move the router to the position with good signal for testing.
    
    **1.4** If your GL.iNet cellular router is an LTE device, please check if the frequency band of the device purchased is suitable for your area.
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/1.png){class="glboxshadow"}

??? "Please check device software config"

    **2.1** Please log in to the Web interface and confirm that the cellular connection program has been started. You can also try to click Abort and Auto Setup again.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow}
    
    **2.2** Some carriers need to use the 3G protocol to connect to the network. Please select the 3G protocol in the Manual Setup on the web page and click Apply for a try.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow}
    
    **2.3** Some SIM cards require a specific APN. Please make sure the correct APN is set on the device.
    
    **2.4** Lock frequency band for testing. For firmware prior to v4.8, refer to [this link](../interface_guide/internet_cellular_v4.7.md/#band-masking) to try Band Masking. For firmware v4.8 or higher, refer to [this link](../interface_guide/internet_cellular.md).

    **2.5** Lock or unlock a signal tower for testing. This feature is supported by GL-X3000, GL-XE3000 and GL-X2000. Click [here](../interface_guide/internet_cellular.md/#lock-tower) for more instructions about tower locking.
    
    Locking to a signal tower may enable the router to connect to high-quality network resources, ensuring stable cellular connectivity. 
    
    However, after locking a signal tower, if the router is moved to another location, it will still attempt to reconnect to the locked tower after booting up. This may consequently prevent the router from connecting to the cellular network automatically at the new location. In this case, you need to either unlock the current signal tower via the router's web admin panel, or manually lock it to a new tower.

??? "Please check the SIM card and device compatibility"

    Among the following measures, if you need to consult the operator, please record the IMEI of the device and the ICCID of the SIM card and inform the operator's customer service, and clearly inform the operator that you are using a router device.
    
    **3.1** Please confirm the SIM type. GL.iNet cellular device is certified based on IOT type devices. In theory, the device can only use IOT type SIM cards. If you are not sure about the card type, please consult the operator.
    
    Common SIM types are: data only, data only + voice, IOT, Hotspot. It is recommended to use IOT and Hotspot type SIM card. We are not sure if a SIM card with data only or data only + voice can definitely be used.
    
    **3.2** Some SIM cards need to be activated on a mobile phone. Ensure that when the SIM card is inserted into a mobile phone, the phone can connect to the internet. Then insert the SIM card into the router for use.
    
    **3.3** Some customized cards can only be used on mobile phones or specific devices. Please confirm if the SIM must be bound to a specific device for use.
    
    **3.4** In some states or cities in the United States (such as AT&T Seattle), you may need to upload the IMEI to the operator's server.
    
    **3.5** If your router displays "SIM Card Not Registered", please try all the above methods first.

    We recommend powering off the router first, inserting the SIM card into the slot, and restarting it. Some models may fail to recognize the SIM card if inserted after booting, as hot swapping is unsupported.

    Ensure all antennas are correctly and securely attached, then test the device in an outdoor location with strong cellular signal. Weak signal conditions may prevent SIM cards from registering with the network.
    
    If the problem persists, it is likely that the SIM cannot be used with the router. Please consult the operator's customer service for details. 
    
    If the operator confirms that it's not the SIM card issue, kindly contact GL.iNet support.
    
    **3.6** If the SIM card can be registered and the IP address can be obtained, but the device cannot connect to the Internet (only data can be uploaded but not downloaded), it is most likely that it has been banned by the operator's backend. You need to ask the operator to lift the restriction, or try setting TTL to 65 for testing. Please refer to the pictures below.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow}
    
If none of the above measures solve the problem, you can try sending an email to [support@glinet.biz](mailto:support@glinet.biz) and contact our technical support staff for support.
