# セルラーでインターネットに接続

ルーターを使用して、セルラーでインターネットにアクセスすることができます。3G/4Gを内蔵している機種とusbポートがあり、usb 3G/4Gモデムに接続できる機種があります。操作手順は似ていて、ここではGL-AXT1800を例にしています。

ウェブ管理画面の左側にある -> INTERNET, Cellular sector.

**ノート:** SIMカードによっては、初回使用時にアクティベーションが必要な場合がありますので、ルーターで使用する前に、携帯電話でアクティベーションを行ってください

1.   まずルーターの電源を切り、SIMカードをUSBモデムに挿入し、USBモデムをルーターのUSBポートに接続してから、再度電源を入れることをお勧めします。電源投入時にUSBモデムを挿入した場合、ページが変化しないことがありますので、ページを更新してください。

2. Please access the web Admin Panel -> INTERNET, Cellular sector. The first time, it may not connect automatically, but it has read the name of your carrier in the upper left corner and the IMEI, then please click **Auto Setup**.

    Please ignore the warning of *Incompatible Modem*

    ![usb modem auto setup](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

3. Connecting.

    **Note:** Some SIM cards may have special usage restrictions, such as the need to use a special APN. If your SIM card can't be registered, please consult your network operator if it has special restrictions.

    ![usb modem connecting](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

4. After a while, it will be connected. Otherwise, try [Manual Setup](#manual-setup).

    When the usb modem is plugged into the router the second time it is powered on, it is usually automatically recognized and a connection is established. It may not get the information of signal, modem name and IMEI.

    ![usb modem connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

---

### Manual Setup

Sometimes, **Auto Setup** may not work, you can try **Manual Setup**.

![4g modem manual setup](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/cellular_settings.png){class="glboxshadow"}

---

### Compatible Modems

Here is a list of supported modems that we had tested before.

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel UC20-E                         | 3G    | Yes    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Yes    | GL.iNet         |           |
| Huawei E1550                           | 3G    | Yes    | GL.iNet         |           |
| Huawei E3276                           | 4G    | Yes    | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G    | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Yes    | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Yes    | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Yes    |                 | Host-less |

*QMI: This modem supports QMI mode. Please choose **/dev/cdc-wdm0** in the **Device** list.

*Host-less: This modem supports tethering mode, please set up by using Tethering but not 3G/4G modem.

You can also refer to [http://ofmodemsandmen.com/modems.html](http://ofmodemsandmen.com/modems.html){target="_blank"} for a well supported modem list.

You can also search on the [forum](https://forum.gl-inet.com){target="_blank"} or create a post for asking.