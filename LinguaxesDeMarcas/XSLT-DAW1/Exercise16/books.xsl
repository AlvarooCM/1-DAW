<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/books">

        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></meta>
                <link rel="stylesheet" type="text/css" href="styles.css"/>
                <title>Books</title>
            </head>
            <body>
                <table border="1">
                    <caption><strong>Numero de libros: </strong><xsl:value-of select="count(book)"/></caption>
                    
                    <tr class="table-header">
                        <th>Title</th>
                        <th>Author</th>
                    </tr>
                    <xsl:apply-templates select="book"/>

                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="book">
        <xsl:if test="price &lt;= 10">
            <tr class="price-low">
                <td><xsl:value-of select="title"/></td>
                <td><xsl:value-of select="author"/></td>
            </tr>
        </xsl:if>

        <xsl:if test="price &lt;= 15">
            <tr class="price-medium">
                <td><xsl:value-of select="title"/></td>
                <td><xsl:value-of select="author"/></td>
            </tr>
        </xsl:if>

        <xsl:if test="price &gt; 15">
            <tr class="price-high">
                <td><xsl:value-of select="title"/></td>
                <td><xsl:value-of select="author"/></td>
            </tr>
        </xsl:if>
    </xsl:template>
    

</xsl:stylesheet>

