import aws_cdk as core
import aws_cdk.assertions as assertions

from merkleproof_api_cdk_template.merkleproof_api_cdk_template_stack import MerkleproofApiCdkTemplateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in merkleproof_api_cdk_template/merkleproof_api_cdk_template_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MerkleproofApiCdkTemplateStack(app, "merkleproof-api-cdk-template")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
