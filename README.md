# cdk-github-samcli

Dependency install:
1. Install AWS CLI: https://docs.aws.amazon.com/cli/lates...
2. Install Python: https://www.python.org/downloads/
3. Install aws sam library: https://docs.aws.amazon.com/serverles...
4. Install cdk: https://docs.aws.amazon.com/cdk/v2/gu...
5. Install docker: https://docs.docker.com/engine/instal...

Codebase: https://github.com/nspacer/sam-cdk

cdk init sample-app --Language=python

python3 -m venv .venv

source .venv/bin/activate   # On Linux/macOS

.venv\Scripts\activate      # On Windows

 pip install -r requirements.txt 

cdk synth

sam local invoke sam-cdk --no-event -t cdk.out/CdkSamStack.template.json

cdk bootstrap

cdk deploy

cdk destroy
