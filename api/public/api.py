from datetime import datetime
import os
import json

import pandas as pd
import numpy as np


ENV1 = os.environ['ENV1']
ENV2 = os.environ['ENV2']


def endpoint1(event, context):
    print('endpoint1')
    print(ENV1)
    return {
        'statusCode': 200,
        'body': json.dumps({ 
            'message' : ENV1
        })
    }


def endpoint2(event, context):
    print('endpoint2')
    print(ENV2)
    return {
        'statusCode': 200,
        'body': json.dumps({ 
            'message' : ENV2
        })
    }
