# How to set up and use Spitz AX (GL-X3000) in your recreational vehicle

This guide shows you how to set up and use Spitz AX in your recreational vehicle. Before you start, you will or may need to prepare the following additional equipment and services: 

- SIM card(s) or USB cable (for tethering), depending on which internet connection method you use. If you are using SIM card(s), ask your operator for the APN. 
- A roof antenna if you want better coverage. 
- [A subscription to Starlink](https://www.starlink.com/roam), if you go to areas without cellular coverage. 

---

## 1. Install your Spitz AX and other equipment

Before starting your journey, set up your Spitz AX by following these steps.

### Step 1: Choose a location for your Spitz AX 

You are recommended to choose a central and unobstructed location for maximum coverage. Ensure the location is within 1 meter from the power source, which is the length of the power adapter cable. 

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

You can place your Spitz AX on a flat surface or mount it to the wall. If you choose to mount it on the wall, follow the next step. 

### (Optional) Step 2: Install your Spitz AX on the wall 

There are two ways to install your Spitz AX on the wall:
- Use the supplied adhesive pad
- Use the wall mounts

Wall mounts are provided in the package. To mount your Spitz AX to the wall, follow the steps below:

1.	Attach the mount to the wall using screws.
2.	Snap your Spitz AX onto the mount. 

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Optional) Step 3: Install the RV roof antenna

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

To get a better signal, use a roof antenna for your Spitz AX. You are recommended to use [MobileMark's LTMG942 multi-band antenna](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/) which provides optimal network signals. If you want to use roof antennas from other brands, make sure they fulfill the following requirements: 

- 4 cellular antennas, receiving frequency range 600M~6GHz.
- 2 Wi-Fi antennas, receiving frequency range: 2.4G~2.5GHz, 5.15~5.84GHz

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Note:** You can use a 7-in-1 antenna (which includes a GPS antenna) but you will only need to connect the six antennas on your Spitz AX. The DIV/GNSS interface of the Spitz AX supports GPS signals because the cellular antenna (receiving frequency of 600M~6GHz) covers the frequency of GPS. Spitz AX supports viewing your GPS location using the command line but does not currently support showing your location on the map.

To avoid signal attenuation, the radio frequency cable from the roof antenna to your Spitz AX should not exceed 5 meters. (For example, when the radio frequency cable from MobileMark is 5 meters long, the signal reception at 3000MHz is reduced by 3dB, which is half the strength. The higher the frequency of the signal, the greater the attenuation.)

[Learn how to replace the antennas on Spitz AX.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/) 

---

## 2. Set up the internet for your Spitz AX 

To ensure you have internet access during your journey, set up the internet using SIM cards. 

Spitz AX has a built-in 5GNR module and supports dual SIM cards. Different mobile network carriers offer different cellular packages for the SIM card and use different APNs. You will need to enter the APN in the settings, so confirm with your operator what the VPN is. 

To set up your SIM cards, follow these steps: 

1. Insert your SIM card(s). 
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Plug in the power adapter and turn on the router. 

To enter your APN, follow these steps: 

1. enter `192.168.8.1` in a web browser and sign in. 
2. You should see the name of your carrier in the upper left corner. Click **Manual Setup**.
3. Next to **APN**, enter the APN. 
4. Click **Apply**. 

If you are using two SIM cards, note that only one SIM card works at each time. You can manually select which SIM card to use each time. Alternatively, enable the [Auto Switch feature](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models). If the router detects one of the SIM cards cannot access the internet properly, it will automatically switch to another SIM card. The switching takes about 1 minute to complete. 

---

## 3. Use Spitz AX in different scenarios

### On the road

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

When you are driving on the road, you should be able to connect to the internet via SIM card(s) which you set up in the previous step.

### At a campground

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

If you stop at a campground during your trip, you can use the public Wi-Fi network provided by the site and save your cellular data. [Learn how to connect to an existing Wi-Fi network.](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/) 

After you have connected to the Wi-Fi network once, Spitz AX can remember the network name and password. It will connect to the network automatically the next time you are around.

### In areas without cellular coverage

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

If you will drive to an area without cellular coverage (e.g., a sparsely populated desert area), use Starlink, a satellite internet service. In this way, when in areas with great cellular coverage, use the 5G signal received by the Spitz AX, and when in areas with no cellular coverage, use Starlink.

When you set up the Starlink antenna, make sure it is unobstructed. Obstructions on both sides of the road (e.g., trees) will affect the reception, so try to park away from any obstructions. 

---

## 4. Set failover priorities 
Spitz AX supports multi-WAN (failover and load balancing). You can set failover priorities for different networks based on your scenario. 

| Scenario| Priority |
| --------| ------- |
| In the campground (connected to its Wi-Fi network using repeater)    | <p> Assign a higher priority to repeater over cellular.</p> <p>As soon as you leave the campground, your router will automatically switch to cellular.</p>|
| Starlink (ethernet) + cellular | Assign a higher priority to cellular over ethernet. <p>In areas with cellular coverage, your router will use your cellular network.</p> <p>When you get to areas without cellular coverage, your router will automatically switch to Starlink via ethernet.</p>|

To set failover, read the [Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/) section.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.