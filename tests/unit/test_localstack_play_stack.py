import aws_cdk as core
import aws_cdk.assertions as assertions

from localstack_play.localstack_play_stack import LocalstackPlayStack

# example tests. To run these tests, uncomment this file along with the example
# resource in localstack_play/localstack_play_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LocalstackPlayStack(app, "localstack-play")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
