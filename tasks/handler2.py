from datetime import datetime
import os

import pandas as pd
import numpy as np


ENV2 = os.environ['ENV2']


def handler(event, context):
    print('handler2')
    print(ENV2)
    print(np.random.randn(10))
    return { 
        'message' : 'ok'
    }
