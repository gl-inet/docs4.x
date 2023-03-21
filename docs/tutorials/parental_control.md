# Parental Control

Parental control feature available since V4.2

On the left side of web Admin Panel -> APPLICATIONS -> Parental Control

**Note**: This feature is currently in beta, and may have some bugs.

## Setup

Make sure the time on your router is correct, otherwise, go to Time Zone and synchronize the time first.

![parental control, router time](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/parental_control_time.png){class="glboxshadow"}

Let's take two typical cases as examples here, and you can make adjustments to suit your situation.

### Case 1

In the first use case, we will set up the device to be unable to access the internet by default.

We will create two rulesets, **learning** and **play**, then set the learning time from Monday to Friday from 8am to 11am, 6pm to 8pm of weekend is the play time.

![parental control, enable](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/parental_control_enable.png){class="glboxshadow"}

The first time, it will have a setup wizard.

Give the profile a name.

![create a profile guide](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

Select the devices you want to manage, or manually add device by input their MAC address.

![create a profile guide](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

The default ruleset of access is **Block Internet Access**. We create two rulesets here, which we will use later. Click **Add a New Ruleset**.

![create a profile guide](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

Specify the ruleset name, color, and a list of sites to block.

![create a ruleset guide](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

The domain names entered in the blocklist include their subdomains. For example, if "example.com" is entered, it also includes any subdomain, such as "subdomain.example.com".

In addition to entering domain names, there are also specific syntax options available. Please refer to [this page](https://github.com/gl-inet/gl-feeds/tree/common/gl-sdk4-parental-control#app-feature-library-syntax) for more information.

Similarly, create another ruleset.

![create a ruleset guide](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

At this point, there will be a total of 4 rulesets. Choose **Block Internet Access**.

![create a profile guide](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

Then go to Set Schedule. Click **Go to Set**.

![set schedule](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

It is assumed that 8am to 11am Monday through Friday is the study time, and the ruleset here is **Learning**. Click **Apply**.

![set schedule](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

You will be taken to the edit page of the newly created profile.

![modify profile](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/modify_profile.png){class="glboxshadow"}

It has created a schedule. Click **Add Schedule** 

![schedule](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/schedules_1.png){class="glboxshadow"}

Specify the ruleset name, color, and a list of sites to block.

![add a schedule](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/create_schedule_2.png){class="glboxshadow"}

After creation, the Schedules are shown below.

![schedules](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/schedules_2.png){class="glboxshadow"}

Click on the purple and green parts of the image above, and you can also modify it.

![edit schedule](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/schedule_edit.png){class="glboxshadow"}

As shown below, click Parental Control at the top to return to the Parental Control page.

![back to parental control page](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

The image below shows the final configuration. You can modify existing profiles and rulesets, or add profiles and rulesets, as you see fit.

![parental control, finally](https://static.gl-inet.com/docs/en/4/tutorials/parental_control/parental_control_finally.png){class="glboxshadow"}

### Case 2

In the second use case, we will set up the device to have restricted internet access by default. Then set the weekend evenings from 6pm to 8pm to play games and short videos. Bedtime, 9pm to 7am the next morning, will disable access to the Internet. See the video tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Troubleshooting

There may be several reasons why the settings are not effective after being configured:

1. DNS cache.
  
    Browsers and operating systems have caches, so it takes some time for the changes to take effect. You can try clearing the cache to get it to take effect immediately. 
  
      * [Clear the cache in the desktop Chrome browser](https://support.google.com/accounts/answer/32050)
      
      * [Clear the cache in the desktop Edge browser](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2)
      
      * [Flush the DNS cache in Windows](https://www.bing.com/search?q=how+to+flush+the+dns+cache+in+windows&qs=n&form=QBRE&sp=-1&lq=0&pq=how+to+flush+the+dns+cache+in+windows&sc=10-37&sk=&cvid=B2220ABF33A24232BA98D091A998425F&ghsh=0&ghacc=0&ghpl=)

2. Perhaps the schedule for the profile you set has not yet arrived.

3. The domain name you set may be incorrect.
  
    While a website's domain name is public, the domain name used when an app calls an API is not. To resolve this, you will need to use a tool(e.g. Wireshark) to capture packets or search for it.
