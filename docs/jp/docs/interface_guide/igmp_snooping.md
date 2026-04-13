# IGMPスヌーピング

Web Admin Panel の左側で、**NETWORK** -> **IGMP Snooping** に移動します。

IGMP snooping を有効にすると、ルーターのマルチキャスト機能を利用できます。

IGMP Snooping は IGMP プロトコルパケットを監視し、対応する情報を抽出して、レイヤー 2 のマルチキャスト転送情報を確立・維持します。その後、マルチキャストグループのデータは、そのグループに参加しているホストにのみ転送され、ほかのホストはマルチキャストグループデータを受信できません。

**Note**: IGMPv3 は v1 および v2 と互換性があります。デフォルトでは v3 を使用し、問題が発生した場合は切り替えてください。

![IGMP Snooping](https://static.gl-inet.com/docs/router/en/4/tutorials/igmp_snooping/igmp_snooping.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
