# Parental Control

Parental control feature available since V4.2

On the left side of web Admin Panel -> APPLICATIONS -> Parental Control

## Local Version

The local version is provided by GL.iNet. It is currently in beta, so there is no additional cost. In this version, if you need to filter requests by application, you need to enter the domain manually.

### Supported Models

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-B3000 (Marble)              | √         |
| GL-MT6000 (Flint2)             | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-MT3000 (Beryl AX)           | √         |
| GL-AXT1800 (Slate AX)          | √         |
| GL-A1300 (Slate Plus)          | √         |
| GL-MT2500/GL-MT2500A (Brume 2) | √         |
| GL-SFT1200 (Opal)              | -         |
| GL-S1300 (Convexa-S)           | -         |
| GL-MT1300 (Beryl)              | -         |
| GL-AX1800 (Flint)              | √         |
| GL-AR750S (Slate)              | -         |
| GL-XE300 (Puli)                | -         |
| GL-X750 (Spitz)                | -         |
| GL-B1300 (Convexa-B)           | -         |
| GL-AP1300 (Cirrus)             | -         |
| GL-X300B (Collie)              | -         |
| GL-MV1000/GL-MV1000W (Brume)   | √         |

### Setup

Make sure the time on your router is correct, otherwise, go to Time Zone and synchronize the time first.

![parental control, router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Let's take two typical cases as examples here, and you can make adjustments to suit your situation.

#### Case 1

In the first use case, we will set up the device to be unable to access the internet by default.

We will create two rulesets, **learning** and **play**, then set the learning time from Monday to Friday from 8am to 11am, 6pm to 8pm of weekend is the play time.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

**Block WAN for Unmanaged Devices** is used to block unmanaged devices from accessing the Internet.

The first time, it will have a setup wizard.

Give the profile a name.

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

Select the devices you want to manage, or manually add device by input their MAC address.

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

You should first connect these devices to the router, otherwise you will need to enter the MAC address manually.

The default ruleset of access is **Block Internet Access**. We create two rulesets here, which we will use later. Click **Add a New Ruleset**.

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

Specify the ruleset name, color, and a list of sites to block.

![create a ruleset guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

The domain names entered in the blocklist include their subdomains. For example, if "example.com" is entered, it also includes any subdomain, such as "subdomain.example.com".

Similarly, create another ruleset.

![create a ruleset guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

At this point, there will be a total of 4 rulesets. Choose **Block Internet Access**.

![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

Then go to Set Schedule. Click **Go to Set**.

![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

It is assumed that 8am to 11am Monday through Friday is the study time, and the ruleset here is **Learning**. Click **Apply**.

![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

You will be taken to the edit page of the newly created profile.

![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

It has created a schedule. Click **Add Schedule** 

![schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_1.png){class="glboxshadow"}

Add another ruleset to the schedule.

![add a schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

After apply, the **Play** schedules are shown below.

![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

Click on the purple or green parts of the image above, and you can also modify it.

![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.png){class="glboxshadow"}

As shown below, click Parental Control at the top to return to the Parental Control page.

![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

The image below shows the final configuration. You can modify existing profiles and rulesets, or add profiles and rulesets, as you see fit.

![parental control, finally](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_finally.png){class="glboxshadow"}

#### Case 2

In the second use case, we will set up the device to have restricted internet access by default. Then set the weekend evenings from 6pm to 8pm to play games and short videos. Bedtime, 9pm to 7am the next morning, will disable access to the Internet. See the video tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Troubleshooting

There may be several reasons why the settings are not effective after being configured:

1. DNS cache.
  
    Browsers and operating systems have caches, so it takes some time for the changes to take effect. You can try clearing the cache to get it to take effect immediately. 
  
      * [Clear the cache in the desktop Chrome browser](https://support.google.com/accounts/answer/32050)
      
      * [Clear the cache in the desktop Edge browser](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2)

2. Perhaps the schedule for the profile you set has not yet arrived.

3. The domain name you set may be incorrect.
  
    While a website's domain name is public, the domain name used when an app calls an API is not. To resolve this, you will need to use a tool(e.g. Wireshark) to capture packets or search for it.

    For example:

    If you want to filter www.google.com, google.com is more appropriate than www.google.com

4. If you have a device that uses a random MAC address for each connection, that will also disable the feature.


## Bark Version

The [Bark](https://www.bark.us/){target="_blank"} version, which is provided and managed by Bark on their own platform, offers the option to filter applications and websites with a single click and monitor request history. Please be aware that an additional subscription fee is payable directly to Bark for this service.

Bark Parental control feature available since v4.5.

**Note:** It's only available in the US, Australia, Guam, and South Africa.

### Usage Scenarios

Bark features monitoring functionality for over 24 different applications and social media networks, which serves as a pre-set list of users under our local parental control feature.

With its logging function, it knows which client accessed which website during which time period, making it convenient for parents to view the logs and identify websites that are not in the blacklist list, and promptly add them to the scope of management control.

### Supported Models

| Router Model        | Support |
| :------------------ | :-----: |
| GL-BE9300 (Flint 3) |    √    |
| GL-MT6000 (Flint 2) |    √    |
| GL-B3000 (Marble)   |    √    |


### Setup

On the left side of web Admin Panel -> APPLICATIONS -> Parental Control.

After selecting the bark version, enable and apply it.Both versions of Parental Controls cannot be enabled at the same time, and the another one will be automatically disabled when you switch versions.


![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

**Please note:** Bark's service may not be available in certain countries. As GL.iNet is not the provider of this service, should you encounter any issues using Bark, kindly reach out directly to [Bark's Technical Support ](https://www.bark.us/contact-us/?ref=glinet&home=glinet)for assistance.


![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

The Bark service is enabled, but this device is not yet paired with any account. Please use the [Device Pairing Link](http://go.bark.us/?ref=glinet&home=glinet) to pair this device with your Bark account.


![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing_link.png){class="glboxshadow"}

The device is connected to Bark Cloud Services and paired with an account. Please [Go to Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) and log in to the paired account to control access.


![device_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/device_set_up.png){class="glboxshadow"}


![bark_success_pair](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_success_pair.png){class="glboxshadow"}
