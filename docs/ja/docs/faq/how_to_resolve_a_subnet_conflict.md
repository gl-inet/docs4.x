# LANサブネットの競合を解決する方法 {#how-to-resolve-a-lan-subnet-conflict}

自宅のルーターからGL.iNetルーターのWANポートにイーサネットケーブルを接続すると、次のメッセージが表示される場合があります。

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**（LANサブネットがWANサブネットと競合しています。LANサブネットを別のアドレスに変更してください。）

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

これは、自宅のルーターがGL.iNetルーターと同じLAN IPを使用しているためで、LAN競合と呼ばれます。

以下の手順に従ってLANサブネットを変更します。

## 1. LANサブネットを変更する {#1-change-lan-subnet}

**Change LAN Subnet** のリンクをクリックすると、**LAN** 設定ページに移動します。

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

2番目のドットの後の数字（デフォルトは **8**）を別の数字に変更します。たとえば192.168.10.1に変更し、**Apply** をクリックします。

変更後、数秒待つとページが更新され、変更後のIPアドレス **192.168.10.1** に自動的にリダイレクトされます。サブネット競合のメッセージは表示されなくなります。

ページがリダイレクトされない場合は、次の手順に進みます。

## 2. 新しいLAN IPでログインする {#2-login-with-new-lan-ip}

アドレスバーに変更後のLAN IPを手動で入力し、Enterキーを押します。

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

管理者パスワードでログインすると、サブネット競合のメッセージは表示されなくなります。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
