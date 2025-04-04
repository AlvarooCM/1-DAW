<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Inventory-List</title>
            </head>
            <body>
                <ul>
                    <li><xsl:value-of select="//product/@code"/></li>
                        <ul>
                            <li><xsl:value-of select="//product/weight[@unit='']/text()"/></li>
                            <li><xsl:value-of select="//product/name/text()"/></li>
                        </ul>
                    <li><xsl:value-of select="//product/@code"/></li>
                        <ul>
                            <li><xsl:value-of select="//product/weight[@unit='']/text()"/></li>
                            <li><xsl:value-of select="//product/name/text()"/></li>
                    </ul>
                </ul>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
