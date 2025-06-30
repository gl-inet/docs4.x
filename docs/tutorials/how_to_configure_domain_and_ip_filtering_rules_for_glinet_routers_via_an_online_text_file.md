# How to Configure Domain and IP Filtering Rules for GL.iNet Routers via an Online Text File

Starting from firmware v4.7.0, the "VPN Policy Based on the Target Domain or IP" in VPN feature and "Add a New Ruleset" in Parental Control feature support importing rules from a link to an online text file. This article will introduce the format of this text file.

## URL Format Description

### Supported and Unsupported URL Formats

- Supported file formats for the text file: .txt, .conf, .log, etc.
- Unsupported file formats: binary files such as .exe, .zip, .jpg, etc.

### Using GitHub to Host the Text File

If you host the text file in a public GitHub repository, make sure to use the raw content URL instead of the regular GitHub URL. 

For example, the following GitHub URL points to the web content rather than the raw content:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

To ensure the router downloads the correct content, use the raw content URL in the following format:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

This way, the router will be able to fetch the plain text content of the file.

## Filter Formats for VPN Policy Based on the Target Domain or IP

The "VPN Policy Based on the Target Domain or IP" feature supports the following filter formats in the online text file:

* Domain name format: Use the domain name, such as `netflix.com`, to match all subdomains of `netflix.com`.
* Subdomain format: Specify the full subdomain, such as `www.netflix.com`, to match only the specific subdomain.
* CIDR format: Use CIDR notation to specify IP address ranges, such as `192.168.10.0/24`.
* IPv4 address format: Specify individual IPv4 addresses, such as `192.168.10.10`.

## Filter Formats for Parental Control Add a New Ruleset

The "Add a New Ruleset" feature in Parental Control supports the following filter formats in the online text file:

* Domain name format: Use the domain name, such as `instagram.com`, to match all subdomains of `instagram.com`.
* Subdomain format: Specify the full subdomain, such as `www.instagram.com`, to match only the specific subdomain.

When creating the online text file, use one filter per line. The router will process each line according to the specified format and apply the corresponding rules to the VPN or Parental Control feature.

## Examples

For "VPN Policy Based on the Target Domain or IP":

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

For "Parental Control Add a New Ruleset":

```
instagram.com
facebook
x.com
snapchat
```

By following these filter formats, you can easily create and maintain the online text file for configuring the VPN and Parental Control features on your router.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
