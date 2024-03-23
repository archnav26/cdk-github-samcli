#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_sam.cdk_sam_stack import CdkSamStack


app = cdk.App()
CdkSamStack(app, "CdkSamStack")

app.synth()
