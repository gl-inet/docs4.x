# LANサブネットの競合を解決する方法

ホームルーターからGL.iNetルーターのWANポートにイーサネットケーブルを接続のとき、このメッセージが表示される場合があります：

「LANサブネットがWANサブネットと競合しています。別のアドレスにLANサブネットを変更してください。」

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

これは、ホームルーターがGL.iNetルーターと同じLAN IPを使用しているためです。これをLAN競合と言います。

以下の手順に従ってLANサブネットを変更します。

## 1. LANサブネットを変更する

ハイパーリンク「LANサブネットを変更する」をクリックすると、LAN設定ページにリダイレクトされます。

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

2番目のピリオド後の番号（デフォルトでは8）を別の番号に変更します。例えば192.168.10.1として、「適用」をクリックします。

変更後、数秒待るとページがアップデートされ、変更されたIPアドレス192.168.10.1に自動的にリダイレクトされます。サブネット競合のプロンプトが消えたことがわかります。

ページがリダイレクトされない場合は、次の手順に進みます。

## 2. 新しいLAN IPでログインする

アドレスバーに新しいLAN IPを入力してEnterキーを押します。

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

管理者パスワードでログインすると、サブネット競合のプロンプトが消えます。

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
