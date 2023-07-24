# イーサネットケーブルでインターネットに接続する

インターネットにアクセスするには、ルーターのWANポートとモデム、または他のルーターのLANポートをイーサネットケーブルで接続します。

ウェブ管理画面の左側にある -> INTERNET, Ethernet sector.

![ethernet dhcp](https://static.gl-inet.com/docs/en/4/tutorials/internet_ethernet/ethernet_dhcp.png){class="glboxshadow"}

**ノート**:イーサネットケーブルをルーターのWANポートに接続する前に, 　**LANに変更**をクリックして [WANポートをLANポートに設定する](../change_wan_to_lan/). ルーターを[repeater](../internet_repeater)として使用する場合に有効です。 その結果、LANポートを1つ増やすことができます。

## プロトコル

プロトコルは3種類あります。 DHCP, Static, PPPoE. **修正** をクリックして変更します　

* DHCP 

    DHCPは、デフォルトで最も一般的なプロトコルです。インターネットプロトコル（IP）ネットワークで使用されるネットワーク管理プロトコルで、ネットワークに接続された機器にIPアドレスやその他の通信パラメータをクライアント・サーバー方式で自動的に割り当てるためのものです。

* Static

    Staticは、インターネットサービスプロバイダ（ISP）から固定IPアドレスを提供されている場合や、IPアドレス、ゲートウェイ、ネットマスクなどのネットワーク情報を手動で設定する場合に必要です。

     ![ethernet static](https://static.gl-inet.com/docs/en/4/tutorials/internet_ethernet/ethernet_static.png){class="glboxshadow"}

* PPPoE

    PPPoE は、多くのインターネットサービスプロバイダ（ISP）によって要求されます。一般的に、ISPはあなたにモデムを与え、あなたがインターネット接続を作成するときに必要だったユーザー名とパスワードを提供します。

    ![ethernet pppoe](https://static.gl-inet.com/docs/en/4/tutorials/internet_ethernet/ethernet_pppoe.png){class="glboxshadow"}
