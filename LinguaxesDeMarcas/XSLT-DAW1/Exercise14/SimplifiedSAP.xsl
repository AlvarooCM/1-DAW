<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/root">
        <html>
            <head>
                <title>SimplifiedSAP</title>
            </head>
            <body>
    
                <h1><xsl:value-of select="count(record[date/year = 1790 and city = 'Glasgow'])"/> records found</h1>
                
                <xsl:apply-templates select="record[date/year = 1790 and city = 'Glasgow']"/>
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="record">
        <p>
            <span style="color:red;">[<xsl:value-of select="id"/>]</span>
        </p>
        <p><xsl:value-of select="city"/></p>
        <p><xsl:value-of select="text/p[1]"/></p>
    </xsl:template>
    
</xsl:stylesheet>
