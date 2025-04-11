# How to check the carrier aggregation status on your cellular router

Carrier aggregation combines multiple network bands to offer more bandwidth and faster speeds for your cellular connection. You can check the carrier aggregation status via the router admin panel on these GL.iNet cellular routers:

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| Spitz AX (GL-X3000)            | √         |
| Puli AX (GL-XE3000)            | √         |
| Mudi V2 (GL-E750V2)            | √         |
| Mudi (GL-E750)                 | √         |
| Spitz (GL-X750)                | √         |
| Collie (GL-X300B)              | √         |
| Puli (GL-XE300)                | √         |
| Cirrus (GL-AP1300LTE)          | √         |

(You cannot enable carrier aggregation within the router admin panel. This feature is provided by your SIM carrier, not GL.iNet.)

To check the carrier aggregation status, follow these steps: 

1. Make sure you have inserted a SIM card into the router. 
2. In a web browser's address bar, enter `192.168.8.1` and sign in. 
3. Click the icon on the right. 
    ![click icon](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/cellular-click-icon-right.png){class="glboxshadow"}
4. In the **AT Command field**, enter **AT+QCAINFO**.
5. Click **Send**.

If carrier aggregation is active, you will see multiple network bands shown on the list. 

![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-information.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.