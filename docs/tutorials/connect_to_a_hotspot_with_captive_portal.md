# キャプティブポータル でホットスポットに接続する

ホテルやカフェ、空港などにある公衆ホットスポットの中には、接続する前にWebページ（ キャプティブポータル ）で認証情報の入力や利用規約への同意が必要なものがあります。

しかし、キャプティブポータルに入ることができないため、ホットスポットに接続したり、インターネットにアクセスしたりできない場合があります。この場合、以下の手順で**DNS Rebinding Attack Protection**を無効にしてください。
 
## 解決策 1： *DNS Rebinding Attack Protection*を無効にしてください。

1. Web管理パネル（192.168.8.1）にアクセスし、[repeater](../internet_repeater/)を使用して、キャプティブポータルによる認証を必要とするパブリックホットスポットに接続します。

    リピーターセクターの下にある**接続**をクリックします。

    ![リピーター](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_sector.png){class="glboxshadow"}

    接続する公衆回線を選択します。


    ![join wlan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_wlan.png){class="glboxshadow"}

    **Apply**をクリックします。Rememberボタンを有効にすると、現在選択されているワイヤレスネットワークを保存することもできます。

    ![ネットワークに参加する](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_network.png){class="glboxshadow"} 

    
    ![リピーター接続](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_connected.png){class="glboxshadow"}
    

2. 2. Web管理パネル -> MORE SETTINGS -> DNSに移動します。DNS Rebinding Attack Protection**を無効にし、**Apply**をクリックします。

    ![DNS Rebinding Attack Protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow"}。


3. ウェブブラウザでウェブページにアクセスすると、自動的にホットスポットのキャプティブポータルにリダイレクトされます。

    スマートフォンを使用しているにもかかわらず、ウェブブラウザがキャプティブポータルにリダイレクトされない場合。スマートフォンのWi-Fiを一旦オフにしてからオンにし、再度ルーターのWi-Fiに接続してください。Wi-Fiのパスワードを入力すると、キャプティブポータルが直接ポップアップするはずです。

    ![接続](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png)

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png)

## 解決策 2：MAC クローン

*DNS Rebinding Attack Protection* を無効にしても、この問題を解決できない場合があります。その場合は、以下の解決策に基づいて、**MAC Clone**を試す必要があります。

1. スマートフォンをネットワークに登録する。

2. ウェブ管理画面の左側→MORE SETTINGS→MAC Cloneをクリックします。

3. スマートフォンのMACアドレスをルーターにクローンする。
![MACCLONE](https://d2jbioc4ahy17s.cloudfront.net/docs/en/4/tutorials/mac_clone/macclone4.0.jpg)
4. 有効にするには、ルーターを再起動する必要がある場合があります。

## 解決策3：ホテルのスタッフに相談する

ホテルのネットワークは、非常に厳しい検証ポリシーを持っている場合があります。解決策1でも2でもうまくいかない場合は、ホテルのスタッフに、ルーターのMACアドレス（工場出荷時のもの）を直接「ホワイトリスト」に追加できるかどうか相談してみてください。
