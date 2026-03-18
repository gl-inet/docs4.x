# How to check the carrier aggregation status on your cellular router

Carrier aggregation combines multiple network bands to provide greater bandwidth and faster speeds for your cellular connection.

This feature cannot be enabled in the router's web Admin Panel, as it depends on your SIM carrier support.

However, you can check the carrier aggregation status using AT commands in the router's web Admin Panel.

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Follow the steps below to check the carrier aggregation status.

1. Insert a SIM card into the router. 
2. Open a web browser, enter `192.168.8.1` in the address bar and log in. 
3. Go to **INTERNET** -> **Cellular** section, click the three-dot icon in the upper right corner, and click **Modem AT Command**. 
    
    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. In the pop-up window, enter **AT+QCAINFO**, and click **Send**.

    If carrier aggregation is active, you will see multiple network bands shown on the list. 
    
    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.