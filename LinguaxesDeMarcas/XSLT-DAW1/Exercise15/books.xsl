<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/books">
        <html>
            <head>
                <title>Books</title>
            </head>
            <body>
                <ol>
                    <xsl:apply-templates select="books/book"/>
                </ol>
            </body>
        </html>
    </xsl:template>

<xsl:template match="book">
    <xsl:if test="price &gt; 10">
        
    </xsl:if>

    <li>
        <xsl:value-of select="title"/>
        <xsl:value-of select="author"/>
        <xsl:value-of select="price"/>
    </li>

    </xsl:template>
</xsl:stylesheet>