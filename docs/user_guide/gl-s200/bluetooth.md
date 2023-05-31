# Bluetooth

## Bluetooth Devices

On the Bluetooth devices page you can turn the current Bluetooth function on/off and modify the Bluetooth scanning settings.

### Scan Settings

![ble-scan-settings](https://static.gl-inet.com/docs/iot/en/ble_web_guide/ble-scan-settings.png){class="glboxshadow"}

- **Scan type**: switching between **active** or **passive** scanning.
- **Scan Interval Time**: the interval between the start times of two consecutive scan windows.
- **Scan Window Time**: the width of time to perform a scan.
- **PHY**: Physical Layer modulation method, currently only supports 1M.

Click on **Apply** to complete the setup of Bluetooth scanning.

### Broadcast Packets

After setting the Bluetooth scan settings correctly, click the Refresh button to see the Bluetooth broadcast data collected within one second.

![broadcast-packets](https://static.gl-inet.com/docs/iot/en/ble_web_guide/broadcast-packets.png){class="glboxshadow"}

- **RSSI**: the wireless signal strength of this broadcast packet.
- **Device Name**: the data segment of this broadcast packet with an AD Type of 0x09, or Unknow if it does not exist.
- **MAC**: the MAC address of the source of this broadcast.
- **Packet Type**: divided into ordinary packet and scan reply packet, only scan reply packet can be scanned in active scan mode, passive scan mode can only scan ordinary packet. Note that the s200 can only be made to scan under active scan if the broadcast device comes with a scan reply packet.
- **Raw Data**: the original data of this broadcast packet.

If you need to see the details of a broadcast packet, please click on it. We provide two ways of presenting the data.

- **Structured data presentation**: parsing the broadcast packet data according to the AD structure defined by the Bluetooth Alliance, splitting and parsing the data of the individual AD segments.

    ![bp-structured-data-presentation](https://static.gl-inet.com/docs/iot/en/ble_web_guide/bp-structured-data-presentation.png){class="glboxshadow"}

- **Raw data presentation**: parsing of broadcast packet data according to the AD structure defined by the Bluetooth Alliance, splitting but not parsing out the raw data of individual AD segments.

## Bluetooth Remote Manage

On the Bluetooth Remote Management page you can choose to turn remote management on/off and modify the relevant remote server configuration.

![bluetooth-remote-manage](https://static.gl-inet.com/docs/iot/en/ble_web_guide/bluetooth-remote-manage.png){class="glboxshadow"}

We provide two methods of communication to the server: MQTT and HTTP.

### MQTT

![mqtt-settings](https://static.gl-inet.com/docs/iot/en/ble_web_guide/mqtt-settings.png){class="glboxshadow"}

- **Host**：server address, either a domain name or an IP address；
- **Port**：server port；
- **Enable TLS**：whether to enable TLS configuration;
- **Username**：the MQTT client username;
- **Password**：the MQTT client password；
- **Topic**
    - **Report**: the gateway will use this topic to push the scanned Bluetooth data to the MQTT Broker.;
    - **Command**: the gateway will subscribe to the topic to receive control commands issued by the remote server;
    - **Response**: the gateway will use the topic to send the command's response or execution result in response to the remote server.

If you need to enable TLS configuration, please click on the **Enable TLS** button and proceed to configure your TLS parameters.

![mqtt-tls](https://static.gl-inet.com/docs/iot/en/ble_web_guide/mqtt-tls.png){class="glboxshadow"}

- **Encryption Mode**：Encryption mode with the server side, either one-way or two-way encryption；

    ![mqtt-tls-encryption](https://static.gl-inet.com/docs/iot/en/ble_web_guide/mqtt-tls-encryption.png){class="glboxshadow"}

- **CA Certificate**：a CA root certificate file must be uploaded when TLS encryption is enabled；
  
    - You can copy the contents of the relevant certificate directly into the input box or click the **Upload** button to upload a file from your device.
- **Client Cerificate**：a client certificate file must be uploaded when TLS bidirectional encryption is enabled；
  
    - You can copy the contents of the relevant certificate directly into the input box or click the **Upload** button to upload a file from your device.
- **Client Private Key**：a client key file must be uploaded when TLS bidirectional encryption is enabled；
  
    - You can copy the contents of the relevant certificate directly into the input box or click the **Upload** button to upload a file from your device.
- **Password of Key**：optional setting, password for encryption the client private key.

If you also need to set up more advanced MQTT options, you can click on **Advance Settings**.

![mqtt-advance](https://static.gl-inet.com/docs/iot/en/ble_web_guide/mqtt-advance.png){class="glboxshadow"}

- **Client ID**：the client ID used by the gateway to connect to the server；
- **QoS Level**：QoS level of all topics, default is 0；
- **Keep Alive Interval**：the heartbeat interval when the gateway connects to the server, default is 60 seconds.

### HTTP

![http-settings](https://static.gl-inet.com/docs/iot/en/ble_web_guide/http-settings.png){class="glboxshadow"}

- **Report Url**：link to data reporting
- **Authentication Type**：set the authentication method for http, currently choose between None or Basic authentication.

    - If **Basic** is selected, the following configuration needs to be entered according to the server settings.

        ![http-basic](https://static.gl-inet.com/docs/iot/en/ble_web_guide/http-basic.png){class="glboxshadow"}

        - **Username**: the HTTP authentication username
        - **Password**: the HTTP authentication password

## Bluetooth Report

On the Bluetooth report page, there are three tabs, Base, MAC Filter and Raw Data Filter, where you can set up the reporting parameters and data filtering functions.

### Base

![report](https://static.gl-inet.com/docs/iot/en/ble_web_guide/report.png){class="glboxshadow"}

- **Report Interval**：the interval in seconds for the gateway to report data to the server；
- **Data Format**：the data format reported by the gateway to the server, currently only Json format is supported；
- **Enable Broadcast Data Report**：if the option is enabled, each reported data will include complete broadcast packet data; otherwise, each reported data will only include the device MAC address and RSSI;
- **RSSI Threshold**：if you set the threshold, the gateway will only report data from devices whose signal strength is greater than the value.

### MAC Filters

Filtering of report data based on the broadcast source MAC address.

![repoet-mac-filter](https://static.gl-inet.com/docs/iot/en/ble_web_guide/repoet-mac-filter.png){class="glboxshadow"}

We support the following MAC address completion rules:

- Case insensitive;
- Several MAC addresses distinguished by line feeds;
- Single MAC addresses support splitting by the character ':' and the character '**-**' ;
- Support for regular expressions with *****, currently requires a minimum of the first 8 bits (4 bytes) to be specified.

**Note**: When there is a non-compliant writeup, it will be red-flagged to indicate that the user needs to make changes.

### Raw Data Filters

Broadcast packets with set filter items in the data are filtered according to AD Type according to the broadcast format defined by the Bluetooth Alliance.

![report-raw-filter](https://static.gl-inet.com/docs/iot/en/ble_web_guide/report-raw-filter.png){class="glboxshadow"}

![report-raw-any](https://static.gl-inet.com/docs/iot/en/ble_web_guide/report-raw-any.png){class="glboxshadow"}

- When **In Any** is selected, the gateway will match the entire broadcast packet data as the content;
- The AD data format is currently only supported in Hex;
- AD data supports the input of **regular expressions**.

## Bluetooth Settings Backup/Restore

### Backup

You can export all Bluetooth-related settings on the page, including scan, connection, remote manage, report, data definition.

![backup](https://static.gl-inet.com/docs/iot/en/ble_web_guide/backup.png){class="glboxshadow"}

If you would like to export the SSL certificate associated with the server connection configured on the device, please tick the "**Include SSL certificate**" option.

### Restore

You can import a Bluetooth configuration that you have previously backed up or exported from another machine on the Bluetooth configuration restore page.

![restore](https://static.gl-inet.com/docs/iot/en/ble_web_guide/restore.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
