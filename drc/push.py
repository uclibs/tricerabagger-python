import subprocess


class Push:
    """send the bag to ap trust - uses aws-cli"""

    def __init__(self, bag_name, production=False):
        self.bag_name = bag_name
        if production:
            self.bucket = "s3://aptrust.receiving.uc.edu"
            self.profile = "aptrust-prod"
        else:
            self.bucket = "s3://aptrust.receiving.test.uc.edu"
            self.profile = "aptrust-test"

    def push(self):
        subprocess.run(
            ["aws", "s3", "cp", "--profile", self.profile, self.bag_name, self.bucket]
        )
