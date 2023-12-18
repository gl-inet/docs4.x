# MacOSはSambaに書き込みできない

一部の Mac デバイスでは、ExFAT 形式を使用してファイルを書き込むときにエラー メッセージが表示される場合があります。

![macopyerror](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

これは、Finder が転送前にファイルに属性を追加し、対処のためにオリジナルとは異なるファイルを作成するためです。この問題を解決するには:

方法　1. ストレージデバイスを**NTFS**フォーマットに変更します。

方法　2. **cp -X file-name** コマンドを使用してファイルをコピーします。

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    Or use **cp -rX floder-name** command to copy the folder.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

