<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0">
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/">
        
        <html>
            <head>
                <title>Movies</title>
            </head>
            
            <body>
                <header> <h1> The number of films listed are: <xsl:value-of select="count(movies/movie)"/></h1> </header>
                <ul>
                    <xsl:apply-templates select="movies/movie"/>
                </ul>
            </body>
        </html>
        
    </xsl:template>
    
    <xsl:template match="movie">

        <li>
            <xsl:value-of select="title"/> - <xsl:value-of select="@year"/>
        </li>

    </xsl:template>
    
</xsl:stylesheet>