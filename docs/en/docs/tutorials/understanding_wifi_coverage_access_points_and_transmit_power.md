---
title: Understanding Wi-Fi Coverage, Access Points, and Transmit Power
---

# Understanding Wi-Fi Coverage, Access Points, and Transmit Power

Many users assume that increasing a router's transmit power always improves Wi-Fi coverage and performance.

While higher transmit power generally increases the coverage of a single router, maximum transmit power is not always ideal in networks with multiple access points (APs), mesh nodes, or enterprise Wi-Fi deployments.

Understanding coverage cells, roaming, channel planning, and transmit power can help improve wireless performance.

## Single router vs. multiple access points

### Single router

If you have only one router providing Wi-Fi coverage:

- Higher transmit power generally increases coverage.
- Client devices can maintain a usable connection farther away.
- Lowering transmit power normally reduces the received signal and downlink signal-to-noise ratio (SNR).

For most users with a single router, leaving transmit power at its default or automatic setting is recommended.

Lowering your router's transmit power does not reduce the RF energy transmitted by neighboring Wi-Fi networks. Their routers and APs continue transmitting at the same power.

### Multiple access points

When multiple APs are deployed, the goal is not necessarily to maximize the coverage area of every AP.

Instead, the objective is to create several smaller, well-defined coverage cells that overlap only enough to provide continuous coverage and reliable roaming.

Appropriate AP placement, transmit power, and channel selection are all important.

## Coverage cell overlap

If every AP transmits at maximum power, their coverage areas may overlap excessively.

A client device may remain connected to a distant AP even when a closer AP provides a stronger signal. This is commonly called a **sticky client**.

A client connected to the wrong AP may experience:

- Lower SNR
- Lower modulation and coding rates
- More retransmissions
- Reduced throughput
- Increased latency

Reducing AP transmit power can shrink the coverage cells and encourage client devices to roam sooner.

## Understanding client roaming

In most Wi-Fi networks, the client device decides when to roam.

The router or AP may provide roaming assistance, but the phone, laptop, tablet, or other client normally makes the final decision to leave one AP and connect to another.

Different client devices use different roaming thresholds and algorithms. A device may therefore remain connected to an AP as long as it considers the connection usable, even when another AP offers a stronger signal.

Reducing excessive coverage overlap can help clients make better roaming decisions.

## Spatial reuse

Wi-Fi is a shared medium.

Before transmitting, Wi-Fi devices listen to determine whether the channel is already in use. If APs using the same channel can hear one another across a large area, they may spend more time waiting for the channel to become available.

This reduces usable airtime and overall throughput.

Appropriately reducing transmit power can allow APs using the same channel in different physical areas to operate more independently. This is known as **spatial reuse**.

Spatial reuse does not mean that lowering your AP's transmit power reduces the interference transmitted by neighboring networks. Instead, properly sized coverage cells can reduce unnecessary contention and allow the same channel to be reused in sufficiently separated areas.

## Channel planning

Transmit power and channel selection should be considered together.

### 2.4 GHz

The 2.4 GHz band has relatively few non-overlapping channels.

In many regulatory regions, channels 1, 6, and 11 are commonly used with a 20 MHz channel width.

Whenever possible, nearby APs should use different non-overlapping channels.

### 5 GHz and 6 GHz

The 5 GHz and 6 GHz bands provide more available channels, making it easier to assign different channels to nearby APs.

Using non-overlapping channels reduces co-channel contention, although excessive coverage overlap can still affect roaming behavior.

Available channels depend on the router model, country or region, channel width, and local regulations.

## Wired APs and mesh networks

### Wired access points

A wired Ethernet connection between the main router and additional APs is generally the preferred deployment.

Because the wired connection carries the backhaul traffic, Wi-Fi transmit power can be adjusted primarily for client coverage, roaming, and spatial reuse.

### Mesh with wired backhaul

Mesh nodes using wired backhaul can be optimized in a similar way to wired APs.

Transmit power can be adjusted to reduce excessive cell overlap while maintaining continuous coverage.

### Mesh with wireless backhaul

In a wireless mesh deployment, the Wi-Fi radios may also carry traffic between mesh nodes.

Reducing transmit power too aggressively can weaken the wireless backhaul connection and reduce overall performance.

When using wireless backhaul, ensure that mesh nodes maintain a strong and stable connection to one another.

## Example multi-AP deployment

Consider two GL.iNet routers connected by Ethernet:

- The primary router provides routing, DHCP, NAT, and firewall services.
- The second router operates in Access Point mode.
- Both devices broadcast the same Wi-Fi network name and security settings.
- Nearby APs use different non-overlapping channels.
- Transmit power is adjusted so the coverage cells overlap enough for roaming, but not excessively.

The ideal transmit power depends on building materials, AP placement, client devices, neighboring Wi-Fi networks, and the desired coverage area.

There is no single transmit-power value that is correct for every deployment.

## Common misconceptions

### Maximum transmit power always provides the best Wi-Fi

Maximum power generally provides the largest coverage area, but it may create excessive overlap and poor roaming behavior in multi-AP deployments.

### Lower transmit power reduces incoming interference

Lowering your AP's transmit power reduces the signal generated by your own AP. It does not reduce the power transmitted by neighboring routers or APs.

### Lower transmit power makes the AP receiver more sensitive

Transmit power and receiver sensitivity are separate characteristics. Lowering transmit power does not inherently improve the AP's ability to receive client transmissions.

### Client devices always connect to the closest AP

Client devices normally select and roam between APs using their own internal algorithms. They may remain connected to a more distant AP even when a closer AP is available.

## Recommended starting points

| Deployment | Recommendation |
| --- | --- |
| Single router | Leave transmit power at its default or automatic setting. |
| Two or more wired APs | Use non-overlapping channels and adjust transmit power to reduce excessive overlap. |
| Mesh with wired backhaul | Optimize coverage cells for reliable roaming. |
| Mesh with wireless backhaul | Avoid reducing power enough to weaken the backhaul connection. |

After making changes, test performance in several locations and verify:

- Signal strength
- Upload and download throughput
- Latency
- Roaming between APs
- Wireless backhaul quality, if applicable

Change one setting at a time so that its effect can be measured accurately.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com) or [Contact us](https://www.gl-inet.com/contact-us/).
