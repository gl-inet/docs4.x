# GL DEV BOARD

In order to give users a more intuitive experience of the thread network functions, we have developed a set of Thread development boards. The **GL DEV BOARD** is a page dedicated to controlling the Thread development board for GL development and displaying relevant data.

## Devices

![devices](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/devices.png){class="glboxshadow"}

The TDB(GL Thread DEV Board) can join the network by using thread Commissioning, but you need to know the EUI64 of the TDB and the device pre-shared key PSKd. To simplify the configuration process, we have pre-built fixed keys in the firmware, which can be added quickly as follows.

### Add TDB to the network

1. Click on **Add Devices**.

2. Click on **Allow New Devices To Join** and Click on **Apply**.

    ![open device commissioning](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/add-dev.png){class="glboxshadow"}

3. Power up the TDB, press and hold SW2 for three seconds or more to restore the factory settings, then press SW2 briefly. You can see the green light flashing.

4. When the green light of the development board is always on, it means that it successfully joins the network.

5. The first time a device is successfully added, the web page will automatically pop up New Devices to prompt for configuration Type/Name information

    ![new devices](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/new-devices.png){class="glboxshadow"}

    - **Type**: If theTDB comes with an A0 board, please select "**A0+A1**".
    - **Name**: User defined names.

6. You can see that the development board was successfully added to the **Online** card.

    ![device is online](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/dev-online.png){class="glboxshadow"}

### Control TDB

![control TDB](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/control-tdb.png){class="glboxshadow"}

#### Device Detail

You can view the current data of the TDB on the **Device Detail** page.

![device detail](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/device-detail.png){class="glboxshadow"}

#### View Records

You can view a graph of the TDB's historical data on the **View Records** page.

![view records](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/view-records.png){class="glboxshadow"}

#### Edit Device

You can edit the settings of the TDB on the **Edit Device** page.

![edit device](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/edit-device.png){class="glboxshadow"}

#### Code Examples

We have prepared some sample code to control the TDB. You can run them in the S200 backend, or write your own applications by referring to these examples.

![code examples](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/code-examples.png){class="glboxshadow"}

#### Reset Device

If you want to remove the TDB from the network, use the reset device function. 

![reset device](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/reset-device.png){class="glboxshadow"}

**Note**: This will restore the TDB to its factory settings.

## Automations

To enable users to better test the thread network in real-life situations, we offer some simple, restricted device linkage functions.

![Automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/automations.png){class="glboxshadow"}

### Add an automation with device action

As an example, create an automation example: press a button on either board and the RGB lights on/off on both boards.

1. Create a name

    ![give a name for automation](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/name.png){class="glboxshadow"}

2. Select type of trigger conditions

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/type-of-trigger-conditions.png){class="glboxshadow"}

3. Select the device(s) to be used as an trigger.

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/trigger.png){class="glboxshadow"}

4. Select trigger conditions

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/trigger-conditions.png){class="glboxshadow"}

5. Select the type of operation

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/type-of-operation.png){class="glboxshadow"}

6. Select the device(s) to be used as an actuator

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/actuator.png){class="glboxshadow"}

7. Select actuator's actions

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/actuator-actions.png){class="glboxshadow"}

8. You can see the automation cards that have been created.

    ![create automations](https://static.gl-inet.com/docs/iot/en/dev_board_web_guide/auto-created.png){class="glboxshadow"}

### Add an automation with webhook

A webhook in web development is a method of augmenting or altering the behavior of a web page or web application with custom callbacks.

As an example, I need TDB for home security alarms. When someone enters, send a message to Discord via webhook.

1. Create a webhook url from Discord

    Please refer to the [official Discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). Please copy the url of the webhook, the next steps need to use.

2. Fellow the steps below to create an automation.

    ![create automation, name](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_name.png){class="glboxshadow"}

    Give it a name for the automation.

    ![create automation, trigger type](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_trigger_type.png){class="glboxshadow"}

    Select **Sensor trigger**.

    ![create automation, trigger device](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_trigger_dev.png){class="glboxshadow"}

    Select devices.

    ![create automation, trigger condition](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_trigger_opera.png){class="glboxshadow"}

    Select trigger condition.

    ![create automation, trigger operation type](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_actor_type.png){class="glboxshadow"}

    Select **Webhook**.

    ![create automation, webhook url](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_actor_url.png){class="glboxshadow"}

    Paste the url you got when you created the webhook.

    ![create automation, webhook url](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_actor_msg.png){class="glboxshadow"}

    Enter the message you wish to send to Discord. [Discord specifies that the message sent provide a value for at least one of **content**, **embeds**, **components**, or **file**](https://discord.com/developers/docs/resources/webhook).

    **Note**: Different Internet applications have their own definitions for the content and format of messages, please refer to the relevant documentation.

    Finally, an Automation that triggers the webhook is successfully created.

    ![create automation, done](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/auto_end.png){class="glboxshadow"}

    When the TDB's pyroelectric infrared sensor is triggered, the GL-S200 sends the specified message to the webhook that is set up.

    ![Discord get message](https://static.gl-inet.com/docs/iot/en/tutorials_webhook/final_effect.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
