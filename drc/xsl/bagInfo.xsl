<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="1.0" xmlns:mods="http://www.loc.gov/mods/v3" xmlns="http://www.loc.gov/METS/">
    <xsl:output method="text" omit-xml-declaration="yes"/>
    <xsl:template match="/">
        <xsl:value-of select="//mods:note" />
        <xsl:if test="//mods:abstract">
            <xsl:text> | </xsl:text>
            <xsl:value-of select="//mods:abstract" />    
        </xsl:if>
        <xsl:if test="//mods:tableOfContents">
           <xsl:text> | </xsl:text>
           <xsl:value-of select="//mods:tableOfContents" />
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
