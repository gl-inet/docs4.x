# モバイルネットワークのトラブルシューティングガイド {#cellular-network-troubleshooting-guide}

モバイルネットワークに接続できない場合は、以下の項目を確認してください。

??? "デバイスのハードウェアを確認"

    **1.1** デバイスには標準の電源アダプターを使用してください。標準以外の電源アダプターを使用すると、電力供給が不足する可能性があります。

    **1.2** Web管理パネルに**Modem name**、**IMEI**、**SIM ICCID**が表示されていることを確認してください。

    ![modem name](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/no_sim.png){class="glboxshadow"}
    
    ファームウェアv4.8以降では、**View More Information**をクリックしてSIM ICCIDを確認できます。

    これらが表示されない場合は、ルーターを再起動してください。それでもモデム名とIMEIが認識されない場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までお問い合わせください。
    
    **1.3** **View More**をクリックして**Cells Info**を確認し、信号が安定していることを確認してください。信号が非常に弱い場合は、アンテナが正しく取り付けられていることを確認するか、電波状況の良い場所にルーターを移動して再テストしてください。

    ![cells info](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/cells_info.png){class="glboxshadow"}
    
    **1.4** **View More**をクリックして、お使いのデバイスが対応している周波数帯がお住まいの地域で利用できるかどうかを確認してください。

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/frequency_band.png){class="glboxshadow"}

??? "ソフトウェア設定を確認"

    **2.1** Web管理パネルにログインし、モバイルネットワークの接続処理が開始されていることを確認してください。**Abort**をクリックしてから**Connect**をクリックすることもできます。
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/2.png){class="glboxshadow gl-90-desktop"}
    
    **2.2** 一部の通信事業者では**3Gプロトコル**での接続が必要な場合があります。3Gプロトコルに切り替え、再テストしてください。

    ファームウェアv4.7以前では、**Manual Setup** -> **Protocol**に移動し、**3G**を選択して**Apply**をクリックしてください。
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/3.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/4.png){class="glboxshadow gl-90-desktop"}

    ファームウェアv4.8以降では、**SIM Card Settings** -> **Protocol**に移動し、**3G**を選択して**Apply**をクリックしてください。

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    デバイスは自動的に再接続されます。数分待ってから、接続に成功したかどうかを確認してください。

    **2.3** 一部のSIMカードには特定のAPNが必要です。SIMカードが登録できない場合は、通信事業者に問い合わせて制限がないか確認してください。必要な場合は、ルーター上で正しいAPNを設定し、**Apply**をクリックしてください。

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}
    
    **2.4** **Band Masking**を有効にして再テストしてください。ファームウェアv4.7以前については、[このリンク](../interface_guide/internet_cellular_v4.7.md#band-masking)を参照してください。ファームウェアv4.8以降については、[このリンク](../interface_guide/internet_cellular.md#band-masking)を参照してください。

    **2.5** 通信基地局をロックまたはロック解除して再テストしてください。この機能はGL-X3000 (Spitz AX)、GL-XE3000 (Puli AX)、GL-X2000 (Spitz Plus)でのみ利用可能です。詳細については[ここ](../interface_guide/internet_cellular.md#lock-tower)をクリックしてください。
    
    特定の通信基地局にロックすると、ルーターは高品質のネットワークリソースにアクセスし、安定したモバイル接続を維持できます。
    
    しかし、基地局にロックすると、新しい場所に移動しても、ルーターは再起動後もその基地局への接続を試み続けます。これにより、ルーターが自動的にモバイルネットワークに接続できなくなる可能性があります。この場合、ルーターのWeb管理パネルから現在の基地局のロックを解除するか、新しい基地局に手動でロックしてください。

    **注意:**   
    1. ロックする基地局は、通信事業者とデバイスがサポートする周波数帯と一致している必要があります。一致しない場合、接続に失敗する可能性があります。  
    2. ルーターのセルラーモジュールでは、**International Data Roaming** がデフォルトで有効です。このオプションを無効にすると、SIM カードがインターネットに接続できなくなる場合があります。この機能は有効のままにしてください。

??? "SIM互換性を確認"
    
    **3.1** SIMタイプを確認してください。GL.iNetのセルラールーターはIoTデバイスとして認証されています。理論上、デバイスはIoTタイプのSIMカードのみをサポートします。SIMタイプがわからない場合は、通信事業者にお問い合わせください。
    
    一般的なSIMタイプには、データ専用、データ専用 + 音声、IoT、ホットスポットがあります。IoTまたはホットスポットのSIMカードの使用をお勧めします。データ専用またはデータ専用 + 音声のSIMカードは、動作を保証できません。
    
    **3.2** 一部のSIMカードは、最初にアクティベーションが必要です。SIMカードをスマートフォンに挿入してインターネットにアクセスできることを確認してから、ルーターに挿入してください。
    
    **3.3** 一部のカスタマイズされたSIMカードは、携帯電話または特定のデバイスでのみ使用できます。SIMカードが特定のデバイスにロックされているかどうかを確認してください。
    
    **3.4** 米国の一部の州や都市（シアトルのAT&Tなど）では、デバイスのIMEIを通信事業者に登録する必要がある場合があります。登録が必要かどうかわからない場合は、通信事業者にお問い合わせください。
    
    **3.5** Web管理パネルに「SIM card not registered」と表示された場合は、まず上記の手順を試してください。

    ルーターの電源をオフにし、SIMカードを差し込んでから、ルーターを再起動することをお勧めします。一部のモデルはホットスワップをサポートしておらず、電源がオンになっている間に差し込むとSIMカードを検出できない場合があります。

    すべてのアンテナが正しく取り付けられていることを確認し、モバイル信号の強い屋外で再テストしてください。信号が弱いと、SIMカードがネットワークに登録されない可能性があります。

    問題が解決しない場合は、SIMカードがルーターと互換性がない可能性があります。通信事業者にお問い合わせください。

    通信事業者がSIMカードの問題ではないと確認した場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までお問い合わせください。

    **3.6** SIMカードが登録されてIPアドレスを取得できるものの、インターネットにアクセスできない場合（アップロードはできるがダウンロードはできない）、SIMカードが通信事業者によって制限されている可能性が高いです。通信事業者に連絡して制限を解除してもらうか、下図のようにTTLを65に設定して再テストしてください。
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/5.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/6.png){class="glboxshadow gl-90-desktop"}

    通信事業者に連絡する際は、デバイスのモデム名、IMEI、SIM ICCID、ルーターのモデルをお伝えください。
    
上記のいずれのステップでも問題が解決しない場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までお問い合わせください。
