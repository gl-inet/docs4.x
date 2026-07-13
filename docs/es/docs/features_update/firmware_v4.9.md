# Firmware v4.9

Esta versión se centra en un control de red más preciso, una mejor gestión del tráfico, mayor seguridad de red y una interfaz de usuario renovada, todo ello diseñado para ofrecer una mejor experiencia general. [Centro de descarga de firmware](https://dl.gl-inet.com/){target="_blank"}

## Flow Control

Flow Control es un módulo central de gestión de red que permite identificar, supervisar, regular y filtrar el tráfico de red con precisión. Optimiza la asignación de recursos de red, elimina la congestión de ancho de banda y normaliza los comportamientos de acceso a la red para ofrecer una experiencia más fluida, segura y controlable. En el firmware v4.9, este módulo se integra con varias funciones prácticas para una gestión integral del tráfico.

El módulo Flow Control incluye las siguientes funciones:

!!! note "DPI Engine"
    
    Tecnología Deep Packet Inspection para identificar con precisión protocolos de aplicaciones, tipos de tráfico y comportamientos de red.

!!! note "Estadísticas de datos"
    
    Recopilación, análisis y visualización de datos de tráfico de red en tiempo real e históricos para supervisar el estado de la red de forma intuitiva.

!!! note "Filtrado de contenido"
    
    Intercepción y filtrado inteligentes de contenido de red inadecuado para normalizar el acceso a la red.

!!! note "QoS (Quality of Service)"
    
    Asignación de ancho de banda y programación de prioridades de tráfico para garantizar la calidad de red de las aplicaciones clave.

!!! note "SQM (Smart Queue Management)"
    
    Optimiza la programación de colas de red para reducir la latencia y la pérdida de paquetes, lo que mejora la fluidez de la transmisión de red.

!!! note "Control parental"
    
    Esta función, que antes estaba clasificada en el menú **Applications**, se migra al menú **Flow Control** en v4.9. Utiliza el DPI Engine actualizado para identificar y bloquear con precisión aplicaciones y contenido de red inadecuados, lo que permite restricciones de acceso basadas en tráfico más profesionales y precisas.

## VPN

El firmware v4.9 mejora de forma integral la lógica de enrutamiento subyacente y la interfaz interactiva del módulo VPN. Corrige posibles conflictos de enrutamiento, simplifica la lógica de configuración y mejora la facilidad de uso.
    
Los ajustes detallados son los siguientes:

!!! note "Agrupación VPN independiente"

    Cada túnel VPN funciona como un grupo independiente, sin conmutación por error entre grupos. Cuando el tráfico de red coincide con un grupo VPN específico, no cambia automáticamente a otros grupos VPN aunque falle el túnel actual, lo que garantiza un enrutamiento del tráfico estable y predecible.

!!! note "Conmutación por error de perfiles dentro del grupo"
    
    Un solo grupo de túneles VPN puede admitir varios perfiles de configuración. Los usuarios pueden personalizar la prioridad de cada perfil dentro del mismo grupo, lo que permite una conmutación por error interna automática para mantener la conectividad VPN cuando falla un perfil.
    
!!! note "Se eliminó la política \"Not Use VPN\""
    
    La opción tradicional "Not Use VPN" para la configuración de políticas VPN se elimina en v4.9. Esto elimina entradas de configuración redundantes y evita eficazmente conflictos complejos de lógica de enrutamiento causados por varias políticas.
    
!!! note "VPN Dashboard rediseñado"
        
    El VPN Dashboard se ha rediseñado por completo con un diseño más intuitivo. Muestra el estado del túnel, la información de conexión y las entradas de configuración con mayor claridad, lo que mejora considerablemente la operación y gestión diarias.

## Protocolo AmneziaWG 2.0

El firmware v4.9 introduce oficialmente el protocolo AmneziaWG 2.0, equipado con varios parámetros nuevos de ofuscación de tráfico. El protocolo actualizado evita eficazmente la detección por DPI y otros sistemas de identificación de tráfico, lo que mejora de forma significativa la ocultación de la conexión y la resistencia a interferencias. Esto permite establecer conexiones VPN estables y fiables en regiones con restricciones de red y en entornos de red complejos.

## Red IoT

La nueva función de red IoT permite crear una red Wi-Fi dedicada e independiente para dispositivos inteligentes IoT. Al estar aislada física y lógicamente de la red principal, evita la ocupación de recursos de red y los riesgos de seguridad derivados del acceso de dispositivos IoT a la red principal. Esta optimización ofrece una compatibilidad más amplia con distintos clientes IoT inteligentes y mejora en conjunto la seguridad de la red doméstica.

## ACL (Access Control List)

ACL, abreviatura de Access Control List, es una función central de gestión de seguridad de red que permite crear reglas de acceso personalizadas para gestionar el tráfico interno y externo según protocolos de conexión, direcciones IP de dispositivos y puertos. Admite un control preciso de permisos para permitir o bloquear comportamientos específicos de acceso a la red. Cuando varias reglas ACL generan conflictos, el sistema ejecuta automáticamente la regla con mayor prioridad para garantizar la aplicación correcta de la política.

ACL se diferencia de Port Forwarding en su objetivo principal: ACL se centra en la gestión de seguridad de red mediante el control de permisos de acceso de dispositivos y tráfico, mientras que Port Forwarding se utiliza para redirigir recursos de red, reenviando tráfico externo a dispositivos locales específicos para implementar acceso remoto a servicios de la red local.

## Otras mejoras

!!! note "Rediseño de la interfaz Wireless"
    
    La interfaz de configuración Wireless se ha rediseñado por completo con un diseño más claro y un estilo visual unificado. Esto reduce la complejidad operativa y mejora considerablemente la simplicidad y facilidad de uso de la interfaz.

!!! note "DNS cifrado actualizado"
    
    El DNS cifrado se amplía para cubrir más protocolos de cifrado, incluidos DoH, DoT y DoQ. Además, se integran más proveedores oficiales de DNS y se añade la configuración manual de servidores DNS cifrados personalizados para satisfacer distintas necesidades de resolución segura de dominios.
    
!!! note "Compatibilidad con Tailscale Exit Node"
    
    Los routers GL.iNet ahora pueden funcionar como Tailscale Exit Node. Todo el tráfico saliente de Internet de los dispositivos del Tailnet puede enrutarse a través de la dirección IP pública del router, lo que permite una gestión de salida de red unificada y segura para toda la red Tailscale.
    
!!! note "Integración de AstroWarp"
    
    AstroWarp se integra oficialmente en el GL.iNet Router SDK en v4.9. Basado en el protocolo AmneziaWG con capacidad nativa de ofuscación de tráfico, proporciona acceso remoto estable, cifrado y seguro. Los usuarios pueden completar rápidamente el emparejamiento del dispositivo y la configuración de la conexión mediante un código de acceso dinámico en el panel de administración web. Admite conexión segura con un clic entre routers de viaje y redes domésticas en cuestión de segundos, sin necesidad de registrar una cuenta ni iniciar sesión.
