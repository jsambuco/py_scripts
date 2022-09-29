# AWS Lambda Examples
# AWS SDK for Python (Boto3) to manage and invoke AWS Lambda
# List metrics from Cloudwatch
# you will need boto3 installed: python3 -m pip install boto3

import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# List metrics through the pagination interface
paginator = cloudwatch.get_paginator('list_metrics')
for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                   MetricName='IncomingLogEvents',
                                   Namespace='AWS/Logs'):
    print(response['Metrics'])

#Create a subscription filter¶
import boto3

# Create CloudWatchLogs client
cloudwatch_logs = boto3.client('logs')

# Create a subscription filter
cloudwatch_logs.put_subscription_filter(
    destinationArn='LAMBDA_FUNCTION_ARN',
    filterName='FILTER_NAME',
    filterPattern='ERROR',
    logGroupName='LOG_GROUP',
)