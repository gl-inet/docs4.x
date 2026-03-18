# GL-X3000/GL-XE3000/GL-X2000がEE SIMカードで動作しない問題のお知らせと解決策

お客様各位

最も近、GL-X3000/GL-XE3000/GL-X2000でEE SIMカードを使用する際に接続の問題が発生している客様がいることがわかりました。さらにトラブルシューティングを行ったところ、特定のEE SIMカードはIPv4プロトコルのみをサポートしていることがわかりました。しかし、GL.iNetモバイルルーターのデフォルト設定ではIPv4とIPv6の両方が同時に有効になっているため、この問題が発生しています。

## 解決策と回避策

1. **ファームウェアアップデート**

    問題を解決するために、デフォルトのプロトコルをIPv4に変更した新しいファームウェアアップデートをリリースしました。IPv6が必要なお客様は、管理パネルで設定をIPv4とIPv6に変更できます。

    | ルーターモデル                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [ファームウェアダウンロード](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [ファームウェアダウンロード](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [ファームウェアダウンロード](https://dl.gl-inet.com/router/x2000/stable)   |

2. **彼のモデルの回避策**

    彼のモデルをお持ちの場合、または上記のファームウェアを使用したくない場合は、モバイル接続を開始した後、ATコマンドを順番に実行してください。

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **注意**：「User_APN」はEE SIMカードの場合通例「everywhere」です。ルー器の再起動ごとにこのプロセスを繰り返してください。

    ??? note "ATコマンドの実行方法は？"

        1. Web管理パネルで、INTERNET -> モバイルセクションに移動し、右上の三時リーダーをクリックして**モデムATコマンド**を選択します。
        
            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}
        
            古いファームウェアの場合は、右上のツールボタンをクリックしてモデム管理ページに入ります。

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}
        
        2. 以下に示すように、ATコマンドを見つけます。

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

問題が解決しない場合は、[support@gl-inet.com](mailto:support@gl-inet.com)までサポートチームにご連絡ください。

<br>

敬上

GL.iNet テクニカルサポート

2025年6月17日
