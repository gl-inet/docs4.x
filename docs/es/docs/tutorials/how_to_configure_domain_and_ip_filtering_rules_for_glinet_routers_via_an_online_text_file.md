# Cómo configurar reglas de filtrado de dominios e IP para routers GL.iNet mediante un archivo de texto en línea

A partir del firmware v4.7.0, la función "VPN Policy Based on the Target Domain or IP" dentro de VPN y la función "Add a New Ruleset" dentro de Parental Control admiten la importación de reglas desde un enlace a un archivo de texto en línea. Este artículo presenta el formato de ese archivo de texto.

## Descripción del formato de URL

### Formatos de URL admitidos y no admitidos

- Formatos de archivo admitidos para el archivo de texto: .txt, .conf, .log, etc.
- Formatos de archivo no admitidos: archivos binarios como .exe, .zip, .jpg, etc.

### Usar GitHub para alojar el archivo de texto

Si aloja el archivo de texto en un repositorio público de GitHub, asegúrese de usar la URL del contenido sin procesar en lugar de la URL normal de GitHub.

Por ejemplo, la siguiente URL de GitHub apunta al contenido web, no al contenido sin procesar:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Para garantizar que el router descargue el contenido correcto, use la URL del contenido sin procesar con el siguiente formato:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

De este modo, el router podrá obtener el contenido de texto plano del archivo.

## Formatos de filtro para VPN Policy Based on the Target Domain or IP

La función "VPN Policy Based on the Target Domain or IP" admite los siguientes formatos de filtro en el archivo de texto en línea:

- Formato de nombre de dominio: use el nombre de dominio, como `netflix.com`, para coincidir con todos los subdominios de `netflix.com`.
- Formato de subdominio: especifique el subdominio completo, como `www.netflix.com`, para coincidir solo con ese subdominio concreto.
- Formato CIDR: use notación CIDR para especificar rangos de direcciones IP, como `192.168.10.0/24`.
- Formato de dirección IPv4: especifique direcciones IPv4 individuales, como `192.168.10.10`.

## Formatos de filtro para Parental Control Add a New Ruleset

La función "Add a New Ruleset" de Parental Control admite los siguientes formatos de filtro en el archivo de texto en línea:

- Formato de nombre de dominio: use el nombre de dominio, como `instagram.com`, para coincidir con todos los subdominios de `instagram.com`.
- Formato de subdominio: especifique el subdominio completo, como `www.instagram.com`, para coincidir solo con ese subdominio concreto.

Al crear el archivo de texto en línea, use un filtro por línea. El router procesará cada línea según el formato especificado y aplicará las reglas correspondientes a la función VPN o Parental Control.

## Ejemplos

Para "VPN Policy Based on the Target Domain or IP":

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

Para "Parental Control Add a New Ruleset":

```
instagram.com
facebook
x.com
snapchat
```

Siguiendo estos formatos de filtro, puede crear y mantener fácilmente el archivo de texto en línea para configurar las funciones de VPN y Parental Control en su router.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
