# Set Up Automation -> Webhook on GL-S200

A webhook in web development is a method of augmenting or altering the behavior of a web page or web application with custom callbacks.

GL-S200 supports users to set webhook trigger for triggering messages to various Internet applications.

------

## Create a webhook

We based our demonstration on Discord's webhook. For more information on how to create a webhook on discord, please refer to the [official discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). Please copy the url of the webhook, the next steps need to use.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/discord_webhook.png)

## Create Automations

As an example, I need TDB for home security alarms. When someone enters, send a message to discord via webhook.

The following is the process for creating Automations:

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_name.png)

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_trigger_type.png)

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_trigger_dev.png)

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_trigger_opera.png)

Select the Webhook.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_actor_type.png)

Enter the url you got when you created the webhook.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_actor_url.png)

Enter the message you wish to send to discord. [Discord specifies that the message sent provide a value for at least one of **content**, **embeds**, **components**, or **file**](https://discord.com/developers/docs/resources/webhook).

***Note**: Different Internet applications have their own definitions for the content and format of messages, please refer to the relevant documentation.*

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_actor_msg.png)

Finally, an Automation that triggers the webhook is successfully created.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/auto_end.png)

## Final effect

When the TDB's pyroelectric infrared sensor is triggered, the S200 sends the specified message to the webhook that is set up.

![](https://static.gl-inet.com/docs-iot/en/tutorials_webhook/final_effect.png)
