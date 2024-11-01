# How to Configure Domain and IP Filtering Rules for GL.iNet Routers via an Online Text File

Starting from firmware v4.7.0, the "VPN Policy Based on the Target Domain or IP" and "Add a New Ruleset" in Parental Control features support importing rules from a link to an online text file. This article will introduce the format of this text file.

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

