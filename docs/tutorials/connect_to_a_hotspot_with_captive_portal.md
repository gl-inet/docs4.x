# キャプティブポータル でホットスポットに接続する

ホテルやカフェ、空港などにある公衆ホットスポットの中には、接続する前にWebページ（ キャプティブポータル ）で認証情報の入力や利用規約への同意が必要なものがあります。

しかし、キャプティブポータルに入ることができないため、ホットスポットに接続したり、インターネットにアクセスしたりできない場合があります。この場合、以下の手順で**DNS Rebinding Attack Protection**を無効にしてください。

1. Web管理パネル（192.168.8.1）にアクセスし、[repeater](../internet_repeater/)を使用して、キャプティブポータルによる認証を必要とするパブリックホットスポットに接続します。

    リピーターセクターの下にある**接続**をクリックします。

    ![リピーター](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_sector.png){class="glboxshadow"}

    接続する公衆回線を選択します。


    ![join wlan](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_wlan.png){class="glboxshadow"}

    **Apply**をクリックします。Rememberボタンを有効にすると、現在選択されているワイヤレスネットワークを保存することもできます。

    ![ネットワークに参加する](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_network.png){class="glboxshadow"} 

    
    ![リピーター接続](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_connected.png){class="glboxshadow"}
    

2. 2. Web管理パネル -> MORE SETTINGS -> DNSに移動します。DNS Rebinding Attack Protection**を無効にし、**Apply**をクリックします。

    ![DNS Rebinding Attack Protection](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow"}。


3. ウェブブラウザでウェブページにアクセスすると、自動的にホットスポットのキャプティブポータルにリダイレクトされます。

    スマートフォンを使用しているにもかかわらず、ウェブブラウザがキャプティブポータルにリダイレクトされない場合。スマートフォンのWi-Fiを一旦オフにしてからオンにし、再度ルーターのWi-Fiに接続してください。Wi-Fiのパスワードを入力すると、キャプティブポータルが直接ポップアップするはずです。

    ![接続](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png)


 