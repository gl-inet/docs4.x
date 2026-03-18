# モバイルネットワークのトラブルシューティングガイド

モバイルネットワークに接続できない場合は、以下の項目を確認してください。

??? "デバイスのハードウェアを確認"

    **1.1** デバイスには標準の電源アダプタを使用してください。標準で外の電源アダプタを使用すると、電力供給が不足する可能性があります。
    
    **1.2** Web管理パネルに**Modem名**、**IMEI**、**SIM ICCID**が表示されていることを確認してください。

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}
    
    ファームウェアver.4.8で降では、**View More Information**をクリックしてSIM ICCIDを確認できます。

    これらが表示されない場合は、ルーターを再起動してください。モデム名とIMEIが認識されない場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までお問い合わせください。
    
    **1.3** **View More**をクリックして**Cells Info**を確認し、シグナルが安定していることを確認してください。シグナルが非常に弱い場合は、アンテナが正しく設置されていることを確認するか、シグナルの良い場所にルーターを移動して再テストしてください。

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}
    
    **1.4** **View More**をクリックして、お使いのデバイスが対応する周波数帯がに域と互換性があるかどうかを確認してください。

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "ソフトウェア設定を確認"

    **2.1** Web管理パネルにログインし、モバイルネットワーク接続プログラムが開始されていることを確認してください。**中止**をクリックしてから**接続**をクリックすることもできます。
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}
    
    **2.2** 一部の通信事業者では**3Gプロトコル**での接続が必要な場合があります。3Gプロトコルに切り替え、再テストしてください。

    ファームウェアver.4.7で前では、**Manual Setup** -> **Protocol**に移動し、**3G**を選択して**Apply**をクリックしてください。
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    ファームウェアver.4.8で降では、**SIM Card Settings** -> **Protocol**に移動し、**3G**を選択して**Apply**をクリックしてください。

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    デバイスは自動的に再接続されます。接続が成功したかどうかを確認するために数分お待ちください。

    **2.3** 一部のSIMカードには特定のAPNが必要です。SIMカードが登録できない場合は、通信事業者に制限がないかどうかを確認してください。必要な場合は、ルーター上で正しいAPNを設定し、**Apply**をクリックしてください。

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}
    
    **2.4** **Band Masking**を有効にして再テストしてください。ファームウェアver.4.7で前については、[このリンク](../interface_guide/internet_cellular_v4.7.md/#band-masking)を参照してください。ファームウェアver.4.8で降については、[このリンク](../interface_guide/internet_cellular.md/#band-masking)を参照してください。

    **2.5** 通信基地局をロックまたはロック解除して再テストしてください。この機能はGL-X3000 (Spitz AX)、GL-XE3000 (Puli AX)、GL-X2000 (Spitz Plus)でのみ利用可能です。詳細については[ここ](../interface_guide/internet_cellular.md/#lock-tower)をクリックしてください。
    
    特定の通信基地局にロックすると、ルーターは高品質のネットワークリソースにアクセスし、安定したモバイル接続を維持できます。
    
    しかし、基地局にロックすると、新しい場所に移動しても、ルーターは再起動後もその基地局への接続を試み続けます。これにより、ルーターが自動的にモバイルネットワークに接続できなくなる可能性があります。この場合、ルーターのWeb管理パネルから現にの基地局のロックを解除するか、新しい基地局に手動でロックしてください。

    **注意:** ロックされた基地局は、キャリアとデバイスがサポートする周波数帯と一致する必要があります。一致しない場合、接続に失敗する可能性があります。

??? "SIM互換性を確認"
    
    **3.1** SIMタイプを確認してください。GL.iNetモバイルルーターはIoTデバイスとして認定されています。理論上、デバイスはIoTタイプのSIMカードのみをサポートします。SIMタイプがわからない場合は、キャリアにお問い合わせください。
    
    一般的なSIMタイプには、データ専用、データ専用 + 音声、IoT、およびホットスポットが含まれます。IoTまたはホットスポットのSIMカードを使用することをお勧めします。データ専用またはデータ専用 + 音声のSIMカードは動作することを保証できません。
    
    **3.2** 一部のSIMカード最初に有効化が必要な場合があります。SIMカードを電話に移動してインターネットにアクセスできることを確認してから、ルーターに移動してください。
    
    **3.3** 一部のカスタマイズされたSIMカードは、モバイル電話または特定のデバイスでのみ使用できます。SIMカードが特定のデバイスにロックされているかどうかを確認してください。
    
    **3.4** 米国の一部の州や都市（シアトルでのAT&Tなど）では、デバイスのIMEIをキャリアに登録する必要がある場合があります。登録がわからない場合は、キャリアにお問い合わせください。
    
    **3.5** Web管理パネルに「SIMカード未登録」と表示された場合、まず上記のステップを試してください。

    ルーターの電源をオフにし、SIMカードを差し込んでから、ルーターを再起動することをお勧めします。一部のモデルはホットスワップをサポートしておらず、電源がオンになっている間に差し込むとSIMカードを検出できない場合があります。

    アンテナがすべて正しく設置されていることを確認し、強力なモバイルシグナルのある屋外エリアで再テストしてください。シグナルが弱いと、SIMカードがネットワークに登録されない可能性があります。

    問題が解決しない場合、SIMカードルーターと互換性がない可能性があります。ネットワークキャリアにさらに支援を求めてください。

    キャリアがSIMカードの問題ではないことを確認した場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までお問い合わせください。

    **3.6** SIMカードが登録されてIPアドレスを取なければならないできるが、インターネットにアクセスできない場合（アップロードは動作するがダウンロードは動作しない）、SIMカードキャリアによって制限されている可能性があります。キャリアに連絡して制限を解除するか、下図のようにTTLを65に設定して再テストしてください。
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    ネットワークキャリアに連絡する際は、デバイスのモデム名、IMEI、SIM ICCID、およびルーター型番を提供してください。
    
上記のいずれのステップでも問題が解決しない場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までお問い合わせください。
