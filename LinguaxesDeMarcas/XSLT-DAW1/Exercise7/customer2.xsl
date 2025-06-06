<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Customer</title>
            </head>
            <body>
                <h1>Our customer</h1>
                <p>The name of the cliente is <xsl:value-of select="customer/name/first"/> and his surname is <xsl:value-of select="customer/name/last"/> . He lives at <xsl:value-of select="customer/address/street"/> in <xsl:value-of select="customer/address/city"/>.</p>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>