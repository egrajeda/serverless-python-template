import os


def main(event, context):
    return {
        "statusCode": 200,
        "body": "Hello! My name is {}.".format(os.environ['NAME'])
    }
