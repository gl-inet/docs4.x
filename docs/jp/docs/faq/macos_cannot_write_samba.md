# macOS で Samba 共有に書き込めない

Samba 共有に exFAT 形式のストレージデバイスを使用している場合、一部の macOS デバイスでは共有へファイルを書き込もうとしたときに、次のいずれかのエラーが表示されることがあります。

- 「予期しないエラーが起きたため、操作を完了できません（エラーコード 100093）。」

    ![error code 100093](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- 「予期しないエラーが起きたため、操作を完了できません（エラーコード -50）。」

    ![error code -50](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

次の方法で問題の解決を試してください。

1. **Samba 共有の権限を確認します。**

    Samba 共有に書き込み権限が設定されていることを確認します。ルーターの Web Admin Panel にログインし、共有フォルダーで該当ユーザーアカウントの「Read/Write」権限が有効になっていることを確認してください。

2. **`cp -X file-name` コマンドでファイルをコピーします。**

    Finder は転送時に拡張属性（リソースフォーク、メタデータなど）を自動的に追加するため、Samba による exFAT ストレージの処理と競合することがあります。**cp -X file-name** コマンドでファイルをコピーしてみてください。

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    フォルダーをコピーする場合は、**cp -rX folder-name** コマンドを使用します。

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/faq/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3. **Mac を再起動します。**

    Apple メニューをクリックし、再起動を選択します。問題が続く場合は、Mac をシャットダウンし、すべての外部デバイスを取り外して 30 秒待ってから再起動してください。

4. **ファイル名を変更します。**

    ファイルを右クリックして Rename をクリックします。シンプルな名前を使用し、!@# やスペースなどの特殊文字を避けてください。

5. **ストレージデバイスを再接続します。**

    USB ドライブなどの外付けドライブを使用している場合は、取り外す前に先に取り出し操作を行い、10 秒待ってから再度接続します。別の USB ポートを試すこともできます。

6. **First Aid でディスクエラーを修復します。**

    破損したディスクデータは書き込み失敗の原因になります。macOS の Disk Utility を使用して問題を修復できます。

    1. Finder -> Applications -> Utilities -> Disk Utility を開きます。
    2. 左側のサイドバーでドライブまたはストレージデバイス（内蔵または外付け）を選択します。
    3. First Aid -> Run をクリックし、処理が完了するまで待ちます。

7. **ファイルシステムを調整するか、ドライブをフォーマットします。**

    exFAT 形式のドライブを使用している場合、macOS で Samba との互換性問題が発生することがあります。次の方法を試してください。

    - **FAT32 にフォーマットする**（外付けドライブ向け、クロスプラットフォーム互換）

        1. まずドライブ上のデータをバックアップします（フォーマットするとすべてのファイルが消去されます）。
        2. Disk Utility を開き、ドライブを選択して Erase をクリックします。
        3. フォーマットとして「MS-DOS (FAT)」（FAT32）を選択し、Erase をクリックします。

    - **ext4 にフォーマットする**

        !!! Note

            ext4 は主に Linux システムでサポートされています。ext4 にフォーマットした後、そのストレージデバイスは Windows オペレーティングシステムと互換性がない場合があり、Windows デバイスで認識できない、または書き込めないなどの問題が発生する可能性があります。

        1. フォーマットするとデータが消去されるため、ドライブ上のすべてのデータをバックアップします。
        2. Disk Utility や Linux システムなどのツールを使用して、ドライブを ext4 にフォーマットします。

8. **macOS を更新し、キャッシュを削除します。**

    古いソフトウェアや破損したキャッシュは競合の原因になります。System Settings -> General -> Software Update に移動して最新バージョンをインストールし、システムキャッシュを削除してください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
