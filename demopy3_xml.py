from xml.dom import minidom

xml = """<?xml version="1.0" ?>
<ProductData>
    <Item Id="P01">
    	<Image>
    	    apple.jpg
    	</Image>
    	<Category>
            <![CDATA[Healthy fruit]]>    	
        </Category>
    </Item>
    <Item Id="P02">
    	<Image>
    	    banana.jpg
    	</Image>
    	<Category>
            <![CDATA[Happy food]]>    	
        </Category>
    </Item>
</ProductData>
"""

# get all XML as a string
xml_data = minidom.parseString(xml).getElementsByTagName('ProductData')

# get all items
parts = xml_data[0].getElementsByTagName('Item')

# loop all items
for part in parts:
    # get id attribute with all spaces removed
    part_id = part.attributes['Id'].value.strip()
    # get image info from simple tag with all spaces removed
    part_image = part.getElementsByTagName('Image')[0].firstChild.nodeValue.strip()
    # get category info from CDATA with all spaces removed
    part_category = part.getElementsByTagName('Category')[0].firstChild.nodeValue.strip()
    # display info
    print("\t".join([part_id, part_image, part_category]))
