<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="/">
        <products>
            <xsl:apply-templates select="product"/>
        </products>
    </xsl:template>
    <xsl:template name="product">
        <identification>
            <xsl:value-of select="name"/>
        </identification>   
    </xsl:template>
</xsl:stylesheet>