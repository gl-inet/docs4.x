# GL DEV BOARD

In order to give users a more intuitive experience of the thread network functions, we have developed a set of Thread development boards. The **GL DEV BOARD** is a page dedicated to controlling the Thread development board for GL development and displaying relevant data.

## Devices

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Devices.png)

The TDB(GL Thread DEV Board) can join the network by using thread Commissioning, but you need to know the EUI64 of the TDB and the device pre-shared key PSKd. To simplify the configuration process, we have pre-built fixed keys in the firmware, which can be added quickly as follows.

### Add TDB to the network

1. Click on "**Add Devices**"

2. Click on "Allow New Devices To Join" and Click on "**Apply**".

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/add-dev.png)

3. Power up the TDB, press and hold SW2 for three seconds or more to restore the factory settings, then press SW2 briefly. You can see the green light flashing.

4. When the green light of the development board is always on, it means that it successfully joins the network.

5. The first time a device is successfully added, the web page will automatically pop up New Devices to prompt for configuration Type/Name information

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/New-Devices.png)

    - **Type**: If theTDB comes with an A0 board, please select "**A0+A1**"
    - **Name**: User defined names.

6. You can see that the development board was successfully added to the **Online** card.

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/dev-online.png)

### Control TDB

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Control-TDB.png)

#### Device Detail

You can view the current data of the TDB on the **Device Detail** page.

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Device-Detail.png)

#### View Records

You can view a graph of the TDB's historical data on the **View Records** page.

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/View-Records.png)

#### Edit Device

You can edit the settings of the TDB on the **Edit Device** page.

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Edit-Device.png)

#### Code Examples

We have prepared some sample code to control the TDB. You can run them in the S200 backend, or write your own applications by referring to these examples.

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Code-Examples.png)

#### Reset Device

If you want to remove the TDB from the network, use the reset device function. 

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Reset-Device.png)

***Note**: This will restore the TDB to its factory settings.*

## Automations

To enable users to better test the thread network in real-life situations, we offer some simple, restricted device linkage functions.

![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/Automations.png)

### Add an automation

As an example, create an automation example: press a button on either board and the RGB lights on/off on both boards.

1. Create a name

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/name.png)

2. Select type of trigger conditions

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/type-of-trigger-conditions.png)

3. Select the device(s) to be used as an trigger.

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/trigger.png)

4. Select trigger conditions

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/trigger%20conditions.png)

5. Select the type of operation

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/type-of-operation.png)

6. Select the device(s) to be used as an actuator

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/actuator.png)

7. Select actuator's actions

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/actuator%27s-actions.png)

8. You can see the automation cards that have been created.

    ![](https://static.gl-inet.com/docs-iot/en/dev-board-web-guide/auto-created.png)






