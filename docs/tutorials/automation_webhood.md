# Set Up Automation -> Webhood on GL-S200

A webhook in web development is a method of augmenting or altering the behavior of a web page or web application with custom callbacks.

GL-S200 supports users to set webhood trigger for triggering messages to various Internet applications.

------

## Create a webhood

We based our demonstration on Discord's webhood. For more information on how to create a webhood on discord, please refer to the [official discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). Please copy the url of the webhood, the next steps need to use.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/discord_webhood.png)

## Create Automations

As an example, I need TDB for home security alarms. When someone enters, send a message to discord via webhood.

The following is the process for creating Automations:

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_name.png)

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_trigger_type.png)

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_trigger_dev.png)

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_trigger_opera.png)

Select the Webhood.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_actor_type.png)

Enter the url you got when you created the webhood.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_actor_url.png)

Enter the message you wish to send to discord. [Discord specifies that the message sent provide a value for at least one of **content**, **embeds**, **components**, or **file**](https://discord.com/developers/docs/resources/webhook).

***Note**: Different Internet applications have their own definitions for the content and format of messages, please refer to the relevant documentation.*

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_actor_msg.png)

Finally, an Automation that triggers the webhood is successfully created.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/auto_end.png)

## Final effect

When the TDB's pyroelectric infrared sensor is triggered, the S200 sends the specified message to the webhood that is set up.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhood/final_effect.png)

