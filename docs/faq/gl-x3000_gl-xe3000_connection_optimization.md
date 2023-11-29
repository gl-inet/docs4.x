# GL-X3000 and GL-XE3000 connection optimization

**If you fail to connect, please check whether the following issues exist.**

??? "Please check device hardware"

    1.1 Please use the device's standard power adapter. Non-standard power adapters may cause insufficient power supply.
    
    1.2 Please confirm that you can find the modem, IMEI number and SIM ICCID on the web. 
    
    If you cannot find it, please power off/on the device, if it still can’t be recognized, please contact customer service to return the device.
    
    1.3 Please check the signal Cells info to confirm that the signal is normal. If the signal is very poor, please confirm that the antennas have been installed correctly, or change the position with good signal for testing.
    
    1.4 If the device is an LTE device, please check that the frequency band of the device purchased is suitable for your area.
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/1.png){class="glboxshadow"}

??? "Please check device software config"

    2.1 Please login the Web interface and confirm that the LTE/5G NR connect program has been started. You can also try to click Abort and  Auto Setup again.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow}
    
    2.2 Some devices can reselect the ttyUSBx interface for networking in the Manual Setup on the web. Each modem manufacturer uses different data interfaces. Please refer to the web page prompts for details.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow}
    
    2.3 Some sim cards require a specific APN, please make sure the correct APN is set on the device
    
    2.4 Please try to use the locked frequency band function for testing. Please refer to the following link for using locked frequency band function.
    
    [https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#band-masking](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#band-masking)

??? "Please check the sim card and device compatibility implication"

    Among the following measures, if you need to consult the operator, please record the IMEI of the device and the ICCID of the sim card and inform the operator's customer service, and clearly inform the operator that you are using a router device.
    
    3.1 Please confirm the SIM type. This device is certified based on IOT type devices. In theory, the device can only use IOT type SIM cards. If you are not sure about the card type, you need to consult the operator
    
    Common SIM types are: data only, data only+voice, IOT, Hostpot. It is recommended to use IOT and Hostpot; not sure about data only, data only+voice can definitely be used.
    
    3.2 Some SIM cards need to be activated on the mobile phone. You can try to confirm on the mobile phone that the mobile phone card can connect to the internet, and then move it to the router for use.
    
    3.3 Some customized cards can only be used on mobile phones or specific devices. Please confirm whether the sim must be bound to a specific device for use.
    
    3.4 In some states or cities in the United States (such as AT&T Seattle), you may need to upload the IMEI to the operator's server.
    
    3.5 If it prompts that the SIM card registration failed, it is most likely that the SIM cannot be used on the router. Please consult the operator's customer service for details.
    
    3.6 If the SIM card can be registered and the IP address can be obtained, but cannot be connected to the Internet (only data can be uploaded but not downloaded), in this case, it is most likely that it has been banned by the operator's backend. You need to ask the operator to lift the restriction, or try Set TTL to 65 for testing, please refer to pictures below.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow}
    
If none of the above measures solve the problem, you can try sending an email to [support@glinet.biz](mailto:support@glinet.biz) and contact our technical support staff for support.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
