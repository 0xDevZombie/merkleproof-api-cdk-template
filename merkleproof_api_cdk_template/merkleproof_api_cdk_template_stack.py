from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct


class MerkleproofApiCdkTemplateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_layer = _lambda.LayerVersion(self, 'nodejs',
                                            code=_lambda.AssetCode('lambda/layer/'),
                                            compatible_runtimes=[_lambda.Runtime.NODEJS_16_X],
                                            )

        entry_lambda = _lambda.Function(
            self, 'merkle-api',
            handler='merkle-proof-api.handler',
            code=_lambda.Code.from_asset('lambda/code'),
            runtime=_lambda.Runtime.NODEJS_16_X,
            layers=[lambda_layer],
            timeout=Duration.seconds(3),
        )
        apigw.LambdaRestApi(self, 'EndPoint', handler=entry_lambda)
