# LANサブネットの競合を解決する方法

ホームルーターからGL.iNetルーターのWANポートにイーサネットケーブルを接続のとき、このメッセージが表示される場合があります：

「LANサブネットがWANサブネットと競合しています。別のアドレスにLANサブネットを変よりしてください。」

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

これは、ホームルーターがGL.iNetルーターと same じLAN IPを使用しているためです。これをLAN競合と言います。

で下の手順に従ってLANサブネットを変よりします。

## 1. LANサブネットを変よりする

ハイパーリンク「LANサブネットを変よりする」をクリックすると、LAN設定ページにリダイレクトされます。

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

2番目のピリオド後の番号（デフォルトでは8）を別の番号に変よりします。例えば192.168.10.1として、「適用」をクリックします。

変より後、数秒待るとページがアップデートされ、変よりされたIPアドレス192.168.10.1にから動のにリダイレクトされます。サブネット競合のプロンプトが消えたことがわかります。

ページがリダイレクトされない場合は、次の手順に進みます。

## 2. 新しいLAN IPでログインする

アドレスバーに新しいLAN IPを入力してEnterキーを押します。

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

管理者パスワードでログインすると、サブネット競合のプロンプトが消えます。

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
