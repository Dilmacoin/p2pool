from p2pool.bitcoin import networks

PARENT = networks.nets['dilmacoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'c0c0c0c0c0c0c0c0'.decode('hex')
PREFIX = 'c0c0c0c0c0c0c0c0'.decode('hex')
P2P_PORT = 31057
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 4444
BOOTSTRAP_ADDRS = 'dilmap2pool.girino.org huep2pool.girino.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-HUE'
VERSION_CHECK = lambda v: None
VERSION_WARNING = lambda v: None
