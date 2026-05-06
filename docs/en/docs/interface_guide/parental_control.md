# Parental Control

Parental control is a way to keep children safe online by blocking inappropriate websites and limiting how long they use devices. It helps prevent access to harmful content, manage screen time, and ensure children use the internet responsibly.

This feature has been available since firmware v4.2. **Note**: Some models, although running firmware v4.2 or higher, do not support Parental Control due to insufficient memory.

Watch this video or follow the steps below to set up Parental Control on GL.iNet routers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Local Version

The local version is provided by GL.iNet. It is currently in beta and has no additional cost. In this version, if you need to filter requests by application, you need to enter the domain manually.

### Supported Models

??? "Supported Models"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
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

### Setup Steps

Log in to the router's web Admin Panel and go to **APPLICATIONS** -> **Parental Control**. 

For firmware ver.4.8.4 and later, navigate to **FLOW CONTROL** -> **Parental Control**.

Ensure the router time is accurate. If not, go to **SYSTEM** -> **Time Zone** to synchronize it first.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Enable Parental Control and click **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Blocks internet access for all devices that are not on the Parental Control list.

Then follow the setup wizard to set up Parental Control.

---

Here is a use case for your reference. You can adjust the settings according to your need.


**Scenario**: Devices in the profile are only allowed to access the Internet for study from 8 AM to 11 AM on weekdays, and for gaming from 6 PM to 8 PM on weekends. Internet access is blocked by default at all other times.

Follow the steps below to set up Parental Control.

1. Create a profile and customize a name.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Select the devices you want to manage. Connect them to the router first. If they have not been connected to the router, add them manually by entering their MAC addresses. 

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Set access limit. 

    There are two default rulesets: **Block Internet Access** and **No Limit**. 

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}
    
    Click **Add a New Ruleset** to create two more rulesets for later use: **Learning** and **Play**. 

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}
    
    Specify the ruleset name (e.g., Learning) and color, enter the websites to block, then click **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Note**: The domain names entered in the blocklist should include their subdomains. For example, if "example.com" is entered, it also includes any subdomain, such as "subdomain.example.com".

    Similarly, create another ruleset. Specify the ruleset name (e.g., Play) and color, enter the websites to block, then click **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}
    
    Upon applied, there will be a total of four rulesets. Select **Block Internet Access** as the **Default Ruleset**, and click **Finish**.

    ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. Next, set schedule for your profile. Click **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}
    
    Add the **Learning** ruleset to the schedule. Set the **Execution Time** from 8 AM to 11 AM on weekdays, then click **Apply**.

    ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. You will then redirected to the edit page of the newly created profile.

    ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    Move to the bottom, and you will see that a schedule has been created. Click the gear icon in the upper right and select **Add Schedule**.

    ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Add another ruleset **Play** to the schedule. Set the **Execution Time** from 6 PM to 8 PM on weekends, then click **Apply**.

    ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    The Play ruleset will then be added into the schedule.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Note**: The red dashed line indicates the current time.

    You can also modify the execution time by clicking on a certain ruleset in the schedule.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Click **Parental Control** at the top to return to the Parental Control page.

    ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    You will see the final configuration. Parental Control is now taking effect as per the schedule. You can modify existing profiles and rulesets, or add new ones as required.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

### Troubleshooting

If your configured settings fail to take effect, check the following possible causes.

1. DNS cache issue.
  
    Browsers and operating systems maintain DNS caches, which may delay the application of configuration changes. Clear the DNS cache to apply changes immediately.
  
      * [Clear DNS cache on desktop Chrome](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [Clear DNS cache on desktop Edge](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. The profile schedule has not yet started.

3. The entered domain name may be incorrect.

    While a website's public domain is easy to find, the API domains used by apps are often not publicly available. To locate the correct domain, use a packet capture tool such as Wireshark or look up the relevant domain information.
    
    For example, when blocking `www.google.com`, entering `google.com` delivers better results than `www.google.com`.

4. The target device uses a randomized MAC address for each network connection, which prevents access rules from taking effect. Disable random MAC address on the target device, then re-add the device to your profile.

## Bark Version

The [Bark](https://www.bark.us/){target="_blank"} version, which is provided and managed by Bark on their own platform, offers the option to filter applications and websites with a single click and monitor request history. 

It offers monitoring functionality for more than 24 popular apps and social media platforms, which are included in the preset list for our local parental control feature.

With its logging function, it records which client accessed which website and at what time. This allows parents to easily view the logs, identify websites not on the blacklist, and quickly add them to the management scope.

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
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
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

### Setup Steps

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