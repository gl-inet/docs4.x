# DPI Engine

DPI (Deep Packet Inspection) is a core technology for intelligent network management. Unlike traditional routers that only identify source and destination addresses, DPI performs in-depth analysis of packet payloads and accurately identifies applications and websites using a feature-matching library, enabling fine-grained traffic classification and control.

The GL.iNet DPI Engine runs locally on your router to deliver intelligent network management with complete privacy. It provides full access to traffic statistics, content filtering, and QoS for comprehensive traffic control.

Integrated with [Netify](https://www.netify.ai/){target="_blank"}, GL.iNet DPI adopts a lightweight embedded plug-in for efficient deployment. With Netify online-updated signature database, it enables reliable management, making network control more accurate and efficient.

**Note**: 

1. When the router is in Drop-in Gateway mode, DPI features (including Data Statistics, Content Filter and QoS) and SQM will not take effect.
2. When DPI is enabled, the Network Acceleration will be disabled automatically to ensure stable performance.

## Supported Models

!!! note "Supported Models"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Note: Models marked with ※ support DPI Engine in firmware v4.9 and later.

## Quick Setup

On the left side of the web Admin Panel, go to **FLOW CONTROL** -> **DPI Engine** and click **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

In the pop-up window, read and agree Terms of Service & Privacy Policy, then click **Apply**. 

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Please wait while the router performs system operations. It will disable Network Acceleration and enable Data Statistics and Content Filter.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Once activated, click **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

You will be directed to the **DPI Engine Version Center**, where you can view the DPI Program version and Database version.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Note**: This page displays core system status indicators only. Traffic processing will start once the relevant features are enabled.

## Database Upgrade 

If a newer database version is available, simply click **Upgrade** to update the database.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.