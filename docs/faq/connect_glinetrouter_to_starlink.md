# How to Connect GL-iNet Router to a Starlink Dish

## Topology

![starlinkgl](https://static.gl-inet.com/docs/router/en/4/faq/Starlink/starlinkgl.jpg){class="glboxshadow"}

### 1. Connect your Starlink Router power to the Starlink Dish.

### 2. Connect Starlink LAN port to GLiNet Router WAN port.

### 3. Setup GLiNet Router by connecting it's LAN or WiFi. [First time setup](https://docs.gl-inet.com/router/en/4/faq/first_time_setup/)

If you are using GL-XE3000(Puli AX), GL-X3000(Spitz AX), GL-MT3000(Beryl AX), GL-MT2500A(Brume2), GL-SFT1200(Opal), GL-MT1300(Beryl), please go to **Web Admin Panel** >**NETWORK**>**Network Acceleration**, then disable it

![netacc](https://static.gl-inet.com/docs/router/en/4/faq/Starlink/netacc.jpg){class="glboxshadow"}

### 4. Open Starlink App, go to setting, enable the Bypass mode.

### 5. In order to use Starlink App with GLiNet Router network, go to **System**>**Advance**>**Luci**>**Network**>**Static Routes** set a static route, then Save & Apply

![statisroute](https://static.gl-inet.com/docs/router/en/4/faq/Starlink/staticroute.jpg){class="glboxshadow"}
