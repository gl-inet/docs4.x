# セルラーでインターネットに接続

ルーターを使用して、セルラーでインターネットにアクセスすることができます。3G/4Gを内蔵している機種とusbポートがあり、usb 3G/4Gモデムに接続できる機種があります。操作手順は似ていて、ここではGL-AXT1800を例にしています。

ウェブ管理画面の左側にある -> INTERNET, Cellular sector.

**ノート:** SIMカードによっては、初回使用時にアクティベーションが必要な場合がありますので、ルーターで使用する前に、携帯電話でアクティベーションを行ってください

1.   まずルーターの電源を切り、SIMカードをUSBモデムに挿入し、USBモデムをルーターのUSBポートに接続してから、再度電源を入れることをお勧めします。電源投入時にUSBモデムを挿入した場合、ページが変化しないことがありますので、ページを更新してください。

2. Web管理パネル→INTERNET、Cellularセクターにアクセスしてください。初回は自動で接続されない場合がありますが、左上のキャリア名とIMEIを読み込んでいますので、**Auto Setup**をクリックしてください。

     *不適合モデム*の警告は無視してください。

    ![usb modem auto setup](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

3. 接続

    **注意:** 一部のSIMカードは、特別なAPNを使用する必要があるなど、特別な使用制限がある場合があります。SIMカードが登録できない場合、特別な制限がある場合は、ネットワークオペレータにご相談ください。

    ![usb modem connecting](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

4.  しばらくすると、接続されます。それ以外の場合は、[マニュアルセットアップ]（#manual-setup）を試してください。

    usbモデムをルーターに接続して2回目に電源を入れると、通常は自動的に認識され、接続が確立されます。信号、モデム名、IMEIなどの情報を取得できない場合があります。

    ![usb modem connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

---

### マニュアルセットアップ

自動セットアップ**がうまくいかない場合もありますので、**手動セットアップ**を試してみてください。

![4g modem manual setup](https://static.gl-inet.com/docs/en/4/tutorials/internet_cellular/cellular_settings.png){class="glboxshadow"}

---

### 適合モデム

以下は、以前にテストしたサポート対象モデムのリストです。

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

*QMI: このモデムはQMIモードをサポートしています。**デバイス** リストで**/dev/cdc-wdm0** を選択してください。

*Host-less: このモデムはテザリング モードをサポートしています。3G/4G モデムではなく、テザリングを使用してセットアップしてください。

 [http://ofmodemsandmen.com/modems.html](http://ofmodemsandmen.com/modems.html){target="_blank"} で、サポートされているモデムの一覧を参照することもできます。

[フォーラム](https://forum.gl-inet.com){target="_blank"} で検索するか、質問用の投稿を作成することもできます。