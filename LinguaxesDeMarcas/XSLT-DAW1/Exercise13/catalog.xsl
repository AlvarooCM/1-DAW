<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Catalog</title>
            </head>
            <body>
                <ol>
                    <xsl:apply-templates select="/catalog/book[authors/author/@birthDate &lt; 1970]"/>
                </ol>
            </body>
        </html>
    </xsl:template>

<xsl:template match="book[authors/author/@birthDate &lt; 1970]">

    <li><xsl:value-of select="title"/></li>

    </xsl:template>
</xsl:stylesheet>