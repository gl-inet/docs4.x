# Connecting the 10G SFP+ port on Flint 4

Flint 4 (GL‑BE14000) comes with a 10G SFP+ port, which can be switched between WAN and LAN modes. This port is compatible with multiple types of SFP+ modules and cables for optical and copper Ethernet connections, meeting diverse networking demands including long-distance fiber access, conventional twisted-pair wiring, and advanced PON fiber termination. 

Below is a detailed introduction to the three connection schemes for the SFP+ port on Flint 4 (GL-BE14000), covering application scenarios, connection topologies, advantages & disadvantages, precautions, and compatible models for reference only.

## Solution 1. Optical Transceiver + Fiber Cable

### 1.1 Scenarios

This solution applies to long-distance, high-stability 10G Ethernet networking scenarios. It is mainly used for two scenarios: 

- Connecting to ISP 10G pure fiber Ethernet uplinks for ultra-high-speed home and commercial broadband access;  
- Deploying long-distance indoor and outdoor network interconnection, such as connecting Flint 4 to a remote 10G switch, cross-floor home network wiring, and small office backbone network deployment. 

### 1.2 Topology

Flint 4 10G SFP+ port → Standard 10G SFP+ optical transceiver (SR/MR/LR) → Optical fiber cable → Remote 10G network switch / ISP fiber‑Ethernet terminal

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology111.png){class="glboxshadow"}

### 1.3 Pros & Cons

The table below evaluates key performance and usability dimensions of the optical transceiver + fiber cable solution, with star ratings and detailed notes for reference:

|Metric|Star Rating|Remarks|
|---|---|---|
|Transmission Distance|★★★★★|Supports up to 300m (multi-mode) or 10km+ (single-mode), breaking copper cable distance limits, suitable for long-range networking.|
|Anti-Interference|★★★★★|Optical signal transmission is immune to electromagnetic interference, static electricity and crosstalk, ensuring stable operation in complex environments.|
|Energy Saving|★★★★★|Low power consumption and low heat generation; mature chip design supports long-term full-load stable operation without overheating risks.|
|Compatibility|★★★★★|Official fully supported, compliant with standard 10G Ethernet protocols, zero firmware adaptation risks.|
|Easy Deployment|★★★☆☆|Requires basic fiber docking specifications; improper operation may cause signal attenuation, slightly higher threshold than copper wiring.|
|Economy|★★★☆☆|Additional optical transceivers and fiber cables are required, with higher overall cost than traditional twisted-pair solutions.|

### 1.4 Precautions

- Only standard 10G Ethernet optical transceivers are supported; PON-protocol optical modules are not applicable to this scheme.

- Select matching single-mode/multi-mode optical modules and fiber cables according to the actual transmission distance to avoid network speed attenuation or link failure.

- This scheme only supports ISP 10G Ethernet-over-fiber services, and cannot be directly connected to traditional GPON/XGS-PON residential fiber lines.

### 1.5 Compatible Models

The following are some standard optic transceivers that have been tested by GL.iNet and friendly users to be compatible with Flint 4, for reference only.

|Model|Tester|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850-nm 300-m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5-m, 30AWG|Friendly user|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300M|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300M|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300M|Friendly user|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300M|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300M|Friendly user|
|XZSNET SFP10G-SR|GL.iNet|
|10Gtek AXS85-192-M3 10GBase-SR 850-nm 300-m|GL.iNet|
|10Gtek AZS85-192-M1 25G SFP28-SR 850-nm100-m|GL.iNet|
|10Gtek ASF85-24-X2-D 1000Base-SX850nm 550M|GL.iNet|
|10Gtek ASF85-24-X2-D 1.25G SFP-SX 850nm 550-m|GL.iNet|
|FS Cisco SFP-10G-SR Compatible 10GBASE-SR|GL.iNet|
|FS Juniper EX-SFP-10GE-SR 10GBASE-SR SFP+|GL.iNet|
|FS Arista SFP-10G-SR 10GBASE-SR SFP+|GL.iNet|
|FS Brocade 10G-SFPP-SR 10GBASE-SR SFP+|GL.iNet|
|HUAWEI 6G-850nm-120m-MM-SFP+ MTRS-6A11-01|GL.iNet|
|HUAWEI 2.5G-1310nm-SM-ESFP MXPD-483II|GL.iNet|
|netLINK 10G/850nm/300M/DDM HTB-10G-SR|GL.iNet|
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100-m|GL.iNet|
|H!Fiber ASF85-24-X2-D 1000Base-SX 850nm 550-m|GL.iNet|
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Friendly user|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100M|Friendly user|

## Solution 2. SFP+ to RJ45 Module (SFP‑10G‑T)

### 2.1 Scenarios

The SFP‑10G‑T module converts the SFP+ optical slot into a standard RJ45 twisted-pair interface, which is suitable for short-distance 10G network scenarios based on conventional network cables. Typical applications include short-distance connection between Flint 4 and 10G switches/NAS devices, rapid expansion of 10G RJ45 network ports without re-laying fiber, and home/SOHO high-speed local area network wiring that retains traditional twisted-pair wiring. It is the best alternative for users who need 10G Ethernet but do not have fiber wiring conditions.

### 2.2 Topology

Flint 4 10G SFP+ port → SFP+ to RJ45 Module (SFP‑10G‑T) → CAT6A/CAT7 twisted-pair cable → 10G switch / 10G wired terminal device

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology222.png){class="glboxshadow"}

### 2.3 Pros & Cons

The table below evaluates key performance and usability dimensions of the SFP+ to RJ45 (SFP‑10G‑T) module solution, with star ratings and detailed notes for reference:

|Metric|Star Rating|Remarks|
|---|---|---|
|Transmission Distance|★★☆☆☆|Limited by PHY chip hardware, maximum stable transmission distance is 30 meters only, not applicable for long-distance wiring.|
|Anti-Interference|★★★☆☆|Traditional twisted-pair transmission, susceptible to electromagnetic interference and crosstalk in complex wiring scenarios.|
|Energy Saving|★★☆☆☆|High power consumption and obvious heat generation under continuous high load; heat dissipation management is required for long-term operation.|
|Compatibility|★★★★☆|Compatible with all standard 10G RJ45 terminals; only CAT6A/CAT7 cables support stable 10G transmission.|
|Easy Deployment|★★★★★|Plug-and-play, no optical path debugging required, compatible with conventional network cable deployment habits, ultra-low operation threshold.|
|Economy|★★★★☆|Reuses existing RJ45 wiring, no fiber transformation cost; only a 10G-T module needs to be purchased separately.|

### 2.4 Precautions

- Must use CAT6A or higher-spec network cables to support stable 10G transmission; CAT6 and lower cables will cause speed reduction and packet loss.

- Control the wiring distance within 30 meters; exceeding the limit will lead to link instability, speed drop or disconnection.

- Reserve heat dissipation space for the SFP‑10G‑T module to avoid equipment failure caused by overheating.

### 2.5 Compatible Models

The following are some SFP+ to RJ45 modules that have been tested by GL.iNet and friendly users to be compatible with Flint 4, for reference only.

|Model|Tester|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Friendly user|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Friendly user|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Friendly user|

## Solution 3. PON‑ONU SFP+ Stick

### 3.1 Scenarios

The PON‑ONU SFP+ stick integrates complete ONU optical modem functions, enabling Flint 4’s SFP+ port to directly terminate traditional GPON/XGS-PON residential fiber lines. This solution cancels the need for an independent external optical modem, realizing one-device fiber access and routing output. It is applicable to enthusiast-level advanced networking scenarios, especially for users who need to simplify home network equipment stacking and directly access operator PON fiber lines through the router.

### 3.2 Topology

Flint 4 10G SFP+ port → PON‑ONU SFP+ stick → ISP GPON/XGS-PON fiber line (including drop cable, PON splitter, and ISP OLT)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology333.png){class="glboxshadow"}

### 3.3 Pros & Cons

The table below evaluates key performance and usability dimensions of the PON‑ONU SFP+ stick solution, with star ratings and detailed notes for reference:

|Metric|Star Rating|Remarks|
|---|---|---|
|Transmission Distance|★★★★★|Adapts to standard PON fiber transmission distance, meeting all household and conventional commercial fiber access scenarios.|
|Anti-Interference|★★★★★|Fiber optical transmission features strong anti-interference and stable signal, consistent with mainstream PON fiber access standards.|
|Energy Saving|★★☆☆☆|High heat generation during high-speed operation; auxiliary heat dissipation is mandatory to avoid performance degradation and disconnection.|
|Compatibility|★★☆☆☆|Unofficially verified enthusiast solution; compatibility depends on ISP whitelist and stick model, with unstable long-term operation.|
|Easy Deployment|★★☆☆☆|Requires advance ISP confirmation, SN/PLOAM authentication configuration and heat dissipation optimization, with high overall deployment threshold.|
|Economy|★★★☆☆|Eliminates independent optical modem cost, but faces potential service risks such as unavailable IPTV/voice services and no official technical support.|

### 3.4 Precautions

- **Confirm ISP permission in advance**: Verify with the operator whether customer-owned third-party ONU hardware is allowed to access the PON network, and obtain mandatory authentication parameters including SN registration code and PLOAM password.

- **Heat dissipation is mandatory**: Equip the PON‑ONU stick with auxiliary heat dissipation measures to avoid frequency reduction, packet loss and disconnection caused by high temperature.

- **No service guarantee**: GL.iNet does not provide technical support for this solution. Problems such as network instability, speed fluctuation and abnormal value-added services cannot be solved by official firmware or after-sales support.

- Different operators have different module model whitelisting rules; please confirm the operator’s supported PON stick models before purchase.

### 3.5 Compatible Models

The following are some PON-ONU SFP+ stick that have been tested by GL.iNet and friendly users to be compatible with Flint 4, for reference only.

|Model|Tester|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Friendly user|

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
