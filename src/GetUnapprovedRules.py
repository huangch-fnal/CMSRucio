from rucio.client.client import Client
from rucio.common.exception import RucioException
from requests.exceptions import ChunkedEncodingError
import pdb
from __future__ import print_function

TARGET_RSE = 'T2_US_MIT'

client = Client()


unapproved_rules = client.list_replication_rules(filters={'state': 'W'})

for rule in unapproved_rules:
    matching_rses = list(client.list_rses(rule['rse_expression']))
    if TARGET_RSE in matching_rses:
        print('Rule %s on %s:%s for %s needs to be approved' % (rule['id'], rule['scope'], rule['name'], rule['account']))
