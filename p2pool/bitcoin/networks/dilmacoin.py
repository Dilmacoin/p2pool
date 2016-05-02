import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c0c0c0c0'.decode('hex')
P2P_PORT = 11057
ADDRESS_VERSION = 30
RPC_PORT = 21057
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'dilmacoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
#SUBSIDY_FUNC = lambda height: 24*100000000 >> (height + 1)//840000
SUBSIDY_FUNC = lambda height: 48*100000000 >> (height + 1)//525600
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_hash').getPoWHash(data))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_hash').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'HUE'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Dilmacoin2') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dilmacoin2/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dilmacoin2'), 'dilmacoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.girino.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.girino.org/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.girino.org/tx/'
SANE_TARGET_RANGE = (2**256//2**42, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
MAX_STANDARD_TX_SIZE = 100000
MAX_BLOCK_SIZE = 1000000
