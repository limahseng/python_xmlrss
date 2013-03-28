from xml.dom import minidom
import re

xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
	<channel>
		<title><![CDATA[What's New?]]></title>
		<link>http://www.dhs.sg/</link>
		<description><![CDATA[]]></description>
		<language>en-us</language>
		<copyright>http://www.dhs.sg/</copyright>
		<generator>Interspire Website Publisher</generator>
		<lastBuildDate>Tue, 26 Mar 2013 11:26:57 SGT</lastBuildDate>
		<ttl>20</ttl>
		<item>
			<title><![CDATA[Mar 19: ODAC Cycling Expedition 2013, Desaru]]></title>
			<link>http://www.dhs.sg/mar-19-odac-cycling-expedition-2013-desaru-2.html</link>
			<description><![CDATA[<p style="text-align: justify;">On the 19<sup>th</sup> of March, 26 students and 4 teachers from ODAC took bumboat from Changi jetty to Tanjong Pengelih jetty, Johore, Malaysia to embark on our 2 days 1 night ODAC Desaru Cycling Expedition... <a href="/mar-19-odac-cycling-expedition-2013-desaru.html" target="_blank">read more</a></p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Mon, 25 Mar 2013 10:47:06 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-19-odac-cycling-expedition-2013-desaru-2.html</guid>
		</item>
		<item>
			<title><![CDATA[Mar 19: Library Book Club]]></title>
			<link>http://www.dhs.sg/mar-19-library-book-club-2.html</link>
			<description><![CDATA[<p style="text-align: justify;">Dunman High School Library Society held its inaugural Book Club Event on the 19<sup>th</sup> of March, 2013... <a href="/mar-19-library-book-club.html" target="_blank">read more</a></p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Wed, 20 Mar 2013 11:04:12 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-19-library-book-club-2.html</guid>
		</item>
		<item>
			<title><![CDATA[Mar 13: Service Learning Symposium 2013]]></title>
			<link>http://www.dhs.sg/mar-13-service-learning-symposium-2013-2.html</link>
			<description><![CDATA[<p class="ParaAttribute1" style="text-align: justify;">The Dunman High School Service Learning Symposium has come a long way since its inception. It has grown significantly over the years, positively impacting more students and promoting volunteerism that benefits society at large... <a href="/mar-13-service-learning-symposium-2013.html" target="_blank">read more</a> </p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Wed, 20 Mar 2013 11:01:41 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-13-service-learning-symposium-2013-2.html</guid>
		</item>
		<item>
			<title><![CDATA[Mar 13: School Visit by Rivervale Primary School]]></title>
			<link>http://www.dhs.sg/mar-13-school-visit-by-rivervale-primary-school-2.html</link>
			<description><![CDATA[<p style="text-align: justify;">13<sup>th</sup> March 2013 was a special day for 120 Rivervale Primary 6 students as they stepped into the Dunman High School campus... <a href="/mar-13-school-visit-by-rivervale-primary-school.html" target="_blank">read more</a></p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Mon, 18 Mar 2013 10:14:36 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-13-school-visit-by-rivervale-primary-school-2.html</guid>
		</item>
		<item>
			<title><![CDATA[Mar 07: SDMA 2013 Ceremony]]></title>
			<link>http://www.dhs.sg/mar-07-sdma-2013-ceremony-2.html</link>
			<description><![CDATA[<p style="text-align: justify;">Dunman High School is pleased to announce that this year we have two teams that have been awarded the ‘Merit’ Award... <a href="/mar-07-sdma-2013-ceremony.html" target="_blank">read more</a></p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Mon, 25 Mar 2013 10:44:15 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-07-sdma-2013-ceremony-2.html</guid>
		</item>
		<item>
			<title><![CDATA[Mar 05: Visit by Beijing No. 2 Middle School]]></title>
			<link>http://www.dhs.sg/mar-05-visit-by-beijing-no-2-middle-school-2.html</link>
			<description><![CDATA[<p style="text-align: justify;">北京市第二中学创建于1724年，是一所拥有超过280年历史的名校。在中国驻新加坡大使馆教育参赞周建平女士的介绍和陪同下，北京二中师生一行34人，于3月5日来我校参观访问... <a href="/mar-05-visit-by-beijing-no-2-middle-school.html" target="_blank">read more</a></p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Sun, 10 Mar 2013 18:42:00 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-05-visit-by-beijing-no-2-middle-school-2.html</guid>
		</item>
		<item>
			<title><![CDATA[Mar 01: A Level Results]]></title>
			<link>http://www.dhs.sg/mar-01-a-level-results-2.html</link>
			<description><![CDATA[<p style="text-align: justify;">Dunman High School is proud of the 2012 Year 6 cohort for their hard work and achievements at the 2012 GCE A-Level Examination!... <a href="/mar-01-a-level-results.html" target="_blank">read more</a> </p>]]></description>
			<author>no@spam.com (none)</author>
			<lastBuildDate>Fri, 01 Mar 2013 18:00:37 SGT</lastBuildDate>
			<guid isPermaLink="true">http://www.dhs.sg/mar-01-a-level-results-2.html</guid>
		</item>
	</channel>
</rss>
"""

# get all XML as a string
xml_data = minidom.parseString(xml).getElementsByTagName('channel')

# get all items
parts = xml_data[0].getElementsByTagName('item')

# loop all items
for part in parts:
    # get title
    title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    # get link
    link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    # get description
    description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
    description = re.sub("<[^>]*>", "", description)
    description = description[:-10]
    # display info
    print "\n".join([title, link, description, ""])
