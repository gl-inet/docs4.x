# Cómo configurar reglas de filtrado de dominios e IP para routers GL.iNet mediante un archivo de texto online

A partir del firmware v4.7, las siguientes funciones admiten la importación de reglas desde la URL de un archivo de texto online:

- VPN Policy Based on Target Domains or IP Addresses (en VPN)
- Add a New Ruleset (en Parental Control)

Este tutorial explica cómo usar un archivo de texto online para importar reglas de filtrado de dominios e IP en routers GL.iNet.

## Formatos de URL y archivo compatibles

Los formatos de URL compatibles son los siguientes:

- URL de archivos de texto plano (HTTP/HTTPS)
- URL de contenido Raw de GitHub

Los tipos de archivo compatibles son `.txt`, `.conf`, `.log` y otros formatos de texto plano.

**Nota**: No se admiten archivos binarios, como `.exe`, `.zip`, `.jpg`, `.png`, etc.

## Usar GitHub para alojar el archivo de texto

Si aloja el archivo de texto en un repositorio público de GitHub, asegúrese de usar la URL del contenido Raw en lugar de la URL normal de GitHub.

Por ejemplo, la siguiente URL de GitHub apunta al contenido web en lugar del contenido Raw:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Para asegurarse de que el router descargue el contenido correcto, use la URL de contenido Raw con el siguiente formato:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

De esta forma, el router podrá obtener el contenido de texto plano del archivo.

## Formatos de filtro para VPN Policy (Domain/IP)

La función **VPN Policy Based on Target Domain or IP Address** admite los siguientes formatos de filtro en el archivo de texto online:

* Nombre de dominio: use el nombre de dominio, como `netflix.com` (coincide con todos los subdominios).
* Subdominio: especifique el subdominio completo, como `www.netflix.com` (coincide solo con ese subdominio).
* Rango CIDR: use notación CIDR para especificar rangos de direcciones IP, como `192.168.10.0/24`.
* Dirección IPv4: especifique direcciones IPv4 individuales, como `192.168.10.10`.

## Formatos de filtro para Parental Control (Ruleset)

La función **Add a New Ruleset** de Parental Control admite los siguientes formatos de filtro en el archivo de texto online:

* Nombre de dominio: use el nombre de dominio, como `instagram.com` (coincide con todos los subdominios).
* Subdominio: especifique el subdominio completo, como `www.instagram.com` (coincide solo con ese subdominio).

Al crear el archivo de texto online, use un filtro por línea. El router procesará cada línea según el formato especificado y aplicará las reglas correspondientes a la función VPN o Parental Control.

Siguiendo estos formatos de filtro, puede crear y mantener fácilmente el archivo de texto online para configurar las funciones VPN y Parental Control en su router.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
