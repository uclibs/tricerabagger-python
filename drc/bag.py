from bagit import make_bag
from lxml import etree


class Bag:
    """build a bag from the target directory"""

    def __init__(self, directory):
        self.target_directory = directory
        self.identifier = self.target_directory.split("/")[-1]
        self.processors = 4
        self.checksums = ["md5"]
        self.bag_info = {
            "Source-Organization": "University of Cincinnati Libraries",
            "Bag-Count": "1 of 1",
            "Internal-Sender-Identifier": f"https://hdl.handle.net/2374.UC/{self.identifier}",
        }

    def bag(self):
        ## parse description from parent object
        xslt = etree.parse("drc/xsl/bagInfo.xsl")
        doc = etree.parse(f"{self.target_directory}/{self.identifier}/mets.xml")
        transform = etree.XSLT(xslt)
        self.bag_info["Internal-Sender-Description"] = transform(doc)

        make_bag(
            self.target_directory,
            bag_info=self.bag_info,
            processes=self.processors,
            checksums=self.checksums,
        )

        ## add aptrust-info.txt
        xslt = etree.parse("drc/xsl/aptrustInfo.xsl")
        doc = etree.parse(f"{self.target_directory}/data/{self.identifier}/mets.xml")
        transform = etree.XSLT(xslt)
        with open(f"{self.target_directory}/aptrust-info.txt", "w") as f:
            f.write(str(transform(doc)))
