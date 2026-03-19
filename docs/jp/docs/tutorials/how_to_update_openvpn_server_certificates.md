# OpenVPNサーバー証明書を更新する方法

このチュートリアルでは、GL.iNetルーターでOpenVPNサーバー証明書を更新する方法を説明します。

**Note**: この操作ではRoot CA証明書を更新するため、既存のすべてのクライアント証明書（設定ファイルに埋め込まれている証明書）が無効になります。OpenVPNクライアントを再接続するには、すべての設定ファイルを再エクスポートする必要があります。

1. ルーターのウェブ管理画面にログインし、**VPN** -> **OpenVPN Server** に移動します。

   OpenVPNサーバーが稼働中の場合は、サービスを停止してください。

2. Configurationタブで **Advanced Configuration** をクリックし、設定を展開します。

   ![advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/advanced.png){class="glboxshadow"}

3. **Server Root Certificate** を見つけ、テキストボックス内の内容をすべて削除します。

   ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate1.png){class="glboxshadow"}

   以下のように、対応するServer CertificateとServer Keyも自動的に削除されます。

   ![certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/certificate2.png){class="glboxshadow"}

4. 3つのボックスをすべて空欄のままにし、下部の **Apply** をクリックします。新しい証明書が自動的に生成され、各ボックスに入力されます。

   ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/update_ovpn_certificate/apply.png){class="glboxshadow"}

5. これでOpenVPN Server証明書の更新は完了です。接続に使用する新しい設定ファイルをエクスポートするため、下部の **Export Client Configuration** をクリックしてください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} にアクセスするか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} ください。
