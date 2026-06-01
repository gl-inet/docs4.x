# ACL

> The ACL feature was introduced in firmware v4.9.

ACL, short for Access Control List, lets you create rules to manage network traffic based on connection protocols, device addresses and ports. It controls whether to allow or block network access. If multiple ACL rules conflict, the system applies the one with higher priority.

ACL works differently from Port Forwarding: ACL mainly allows or blocks network access for security purposes, while Port Forwarding redirects external traffic to specific devices on your local network to enable remote access to local services.

---

On the left side of the web Admin Panel, go to **SECURITY** -> **ACL**.

Click the **Add Rule** button on the right.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Create your ACL rule in the pop-up window, then click **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: Enter a custom name for the rule.

- **Protocol**: Specify which type of network traffic the rule applies to. Select a connection protocol from `Any`, `TCP`, `UDP`, `TCP+UDP`, and `ICMP`. 

- **IP Type**: Define the IP address format for network traffic. Select the IP type from `IPv4 & IPv6`, `IPv4`, and `IPv6`. 

- **Source Zone**: Select the network zone where traffic originates. Available options: `LAN`, `Guest`, `IoT`, and `WAN`.

- **Source Address**: (Optional) Restrict the rule to specific source devices or IP addresses. You may select a source address from the drop-down list. 

- **Destination Zone**: This is where the network traffic is heading to. Select the target network zone. Available options: `LAN`, `Guest`, `IoT`, and `WAN`.

- **Destination Address**: (Optional) Restrict the rule to specific destination devices or IP addresses. You may select a destination address from the drop-down list.

- **Action**: Choose to `Accept` or `Block` network traffic matching this rule.

- **Enable**: Toggle to enable or disable this rule.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
