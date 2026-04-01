# How to configure Domain and IP Filtering rules for GL.iNet Routers via an online text file

Starting with firmware v4.7, the following features support importing rules from an online text file URL:

- VPN Policy Based on Target Domains or IP Addresses (under VPN)
- Add a New Ruleset (under Parental Control)

This tutorial explains how to use an online text file to import domain and IP filtering rules for GL.iNet routers.

## Supported URL & File Formats

The supported URL formats are as follows:

- Plain text file URLs (HTTP/HTTPS)
- GitHub Raw content URL

The supported file types are `.txt`, `.conf`, `.log`, and other plain text formats.

**Note**: Binary files are not supported, such as `.exe`, `.zip`, `.jpg`, `.png`, etc.

## Use GitHub to Host Text File

If you host the text file in a public GitHub repository, make sure to use the raw content URL instead of the regular GitHub URL. 

For example, the following GitHub URL points to the web content rather than the raw content:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

To ensure the router downloads the correct content, use the raw content URL in the following format:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

In this way, the router will be able to fetch the plain text content of the file.

## Filter Formats for VPN Policy (Domain/IP)

The "VPN Policy Based on Target Domain or IP Address" feature supports the following filter formats in the online text file:

* Domain name: Use the domain name, such as `netflix.com` (matches all subdomains).
* Subdomain: Specify the full subdomain, such as `www.netflix.com` (matches only this subdomain).
* CIDR range: Use CIDR notation to specify IP address ranges, such as `192.168.10.0/24`.
* IPv4 address: Specify individual IPv4 addresses, such as `192.168.10.10`.

## Filter Formats for Parental Control (Ruleset)

The "Add a New Ruleset" feature in Parental Control supports the following filter formats in the online text file:

* Domain name: Use the domain name, such as `instagram.com` (matches all subdomains).
* Subdomain: Specify the full subdomain, such as `www.instagram.com` (matches only this subdomain).

When creating the online text file, use one filter per line. The router will process each line according to the specified format and apply the corresponding rules to the VPN or Parental Control feature.

By following these filter formats, you can easily create and maintain the online text file for configuring the VPN and Parental Control features on your router.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
