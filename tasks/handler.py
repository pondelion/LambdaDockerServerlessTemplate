from datetime import datetime
import os

import pandas as pd
import numpy as np


ENV1 = os.environ['ENV1']


def handler(event, context):
    print('handler1')
    print(ENV1)
    return { 
        'message' : 'ok'
    }
