# Parental Control

Parental control is a way to keep children safe online by blocking inappropriate websites and limiting how long they use devices. It helps prevent access to harmful content, manage screen time, and ensure children use the internet responsibly.

This feature has been available since firmware v4.2.

Watch this video or follow the steps below to learn more about Parental Control on GL.iNet router.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Local Version

The local version is provided by GL.iNet. It is currently in beta and has no additional cost. In this version, if you need to filter requests by application, you need to enter the domain manually.

### Supported Models

??? "Supported Models"
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Unsupported Models"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Setup

Log in to the router's web admin panel, and navigate to **APPLICATIONS** -> **Parental Control**. 

Ensure the router time is accurate. If not, go to **SYSTEM** -> **Time Zone** to synchronize it first.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Enable Parental Control and click **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: It is used to block unmanaged devices from accessing the Internet.

Then follow the setup wizard to set up Parental Control.

Here are two use cases for your reference, which you can adjust according to your own situation.

#### Case 1

**Scenario**: Devices in the profile can only access the Internet for study from 8 AM to 11 AM on weekdays, and for gaming from 6 PM to 8 PM on weekends. All other times, internet access is blocked by default.

Follow the steps below.

1. Create a profile and give it a name.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

2. Select the devices you want to manage. If they have not been connected to the router, manually add them by inputting their MAC addresses. 

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

3. Set access limit. 

    There are two default rulesets: **Block Internet Access** and **No Limit**. Create two more rulesets here for later use: **Learning** and **Play**. 

    Click **Add a New Ruleset**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

4. Specify the ruleset name (e.g., Learning), color, and a list of sites to block. Then click **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

    **Note**: The domain names entered in the blocklist should include their subdomains. For example, if "example.com" is entered, it also includes any subdomain, such as "subdomain.example.com".

    Similarly, create another ruleset named Play. Specify a color, the sites to block and click **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

5. Upon applied, there will be a total of four rulesets, as shown below. 

    Ensure to select **Block Internet Access** as **Default Ruleset**, and click **Finish**.

    ![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

6. Then go to Set Schedule. Click **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

7. Add the **Learning** ruleset to the schedule. Set the **Execution Time** is from 8 AM to 11 AM on weekdays. Click **Apply**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

8. You will be taken to the edit page of the newly created profile.

    ![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

    You will see that a schedule has been created. Click **Add Schedule** at the upper-right.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/add_schedule.png){class="glboxshadow"}

9. Add another ruleset **Play** to the schedule. Set the **Execution Time** is from 6 PM to 8 PM on weekends. Click **Apply**.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

10. Then you will see that the Play ruleset has also been added into the schedule.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

    **Note**: The red dashed line indicates the current time.

    You can also modify the schedule ruleset by clicking on a certain part in the schedule.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.jpg){class="glboxshadow"}

11. Click **Parental Control** at the top to return to the Parental Control page.

    ![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

    You will see the final configuration. You can modify the existing profiles and rulesets, or add new ones.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/final_configuration.png){class="glboxshadow"}

#### Case 2

**Scenario**: Devices in the profile can only access the Internet for playing games and short videos from 6 PM to 8 PM on weekend evenings. All other times, including the bedtime from 9 PM to 7 AM the next morning, internet access is blocked by default.

See the video tutorial below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Troubleshooting

There may be several reasons why the settings are not effective after being configured:

1. DNS cache.
  
    Browsers and operating systems have caches, so it takes some time for the changes to take effect. You can try clearing the cache to get it to take effect immediately. 
  
      * [Clear the cache in the desktop Chrome browser](https://support.google.com/accounts/answer/32050)
      
      * [Clear the cache in the desktop Edge browser](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2)

2. The schedule for the profile has not yet arrived.

3. The domain name you set may be incorrect.
  
    While a website's domain name is public, the domain name used when an app calls an API is not. To resolve this, you will need to use a tool (e.g. Wireshark) to capture packets or search for it.

    For example, if you want to filter "www.google.com", "google.com" is more appropriate than "www.google.com".

4. The device you want to impose restrictions on uses a random MAC address for each connection, which will result in the rules not taking effect.

## Bark Version

The [Bark](https://www.bark.us/){target="_blank"} version, which is provided and managed by Bark on their own platform, offers the option to filter applications and websites with a single click and monitor request history. 

The Bark Parental Control feature has been available since firmware v4.5, and is supported only on selected GL.iNet routers.

**Note**: 

1. The Bark service is available **only in the United States, Australia, and South Africa**. Click [here](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"} for details.

2. The Bark service typically requires a paid subscription. However, as part of our partnership with Bark, GL.iNet offers the Bark Home plan for free on select router models, providing advanced monitoring and alerts at no extra cost.

3. The two Parental Control versions cannot be enabled at the same time. Switching between versions will automatically disable the other.

### Supported Models

??? "Supported Models"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)

??? "Unsupported Models"
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Usage Scenarios

Bark features monitoring functionality for over 24 different applications and social media networks. These applications and social media networks serve as a pre-set list of items under our local parental control feature.

With its logging function, it knows which client accessed which website during which time period, making it convenient for parents to view the logs and identify websites that are not in the blacklist, and promptly add them to the scope of management control.

### Setup

Log in to the router's web admin panel, and navigate to **APPLICATIONS** -> **Parental Control**. 

Select the Bark version, toggle the switch and click **Apply**. 

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Note:** Bark's service may not be available in certain countries. As GL.iNet is not the provider of this service, should you encounter any issues using Bark, kindly reach out directly to [Bark's Technical Support ](https://www.bark.us/contact-us/?ref=glinet&home=glinet) for assistance.

The Bark service is enabled, but this device is not yet paired with any account. Please use the [Device Pairing Link](https://www.bark.us/app/signup/?ref=glinet&home=glinet) to pair this device with your Bark account.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Once paired, the page displays as follows.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Your device is now connected to Bark Cloud Services and paired with your account. Please [go to Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) and log in to your account to create a profile for network control.

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.