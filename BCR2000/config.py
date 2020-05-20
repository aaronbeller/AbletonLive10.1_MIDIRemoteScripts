#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/BCR2000/config.py
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {u'STOP': GENERIC_STOP,
 u'PLAY': GENERIC_PLAY,
 u'REC': GENERIC_REC,
 u'LOOP': GENERIC_LOOP,
 u'RWD': GENERIC_RWD,
 u'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = (GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = (97, 98, 99, 100, 101, 102, 103, 104)
TRACKARM_CONTROLS = (GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {u'TOGGLELOCK': GENERIC_BUT9,
 u'BANKDIAL': -1,
 u'NEXTBANK': -1,
 u'PREVBANK': -1,
 u'BANK1': GENERIC_PAD1,
 u'BANK2': GENERIC_PAD2,
 u'BANK3': GENERIC_PAD3,
 u'BANK4': GENERIC_PAD4,
 u'BANK5': GENERIC_PAD5,
 u'BANK6': GENERIC_PAD6,
 u'BANK7': GENERIC_PAD7,
 u'BANK8': GENERIC_PAD8}
CONTROLLER_DESCRIPTION = {u'INPUTPORT': u'BCR2000',
 u'OUTPUTPORT': u'BCR2000',
 u'CHANNEL': 0}
MIXER_OPTIONS = {u'NUMSENDS': 2,
 u'SEND1': GENERIC_SLIDERS,
 u'SEND2': (89, 90, 91, 92, 93, 94, 95, 96),
 u'MASTERVOLUME': -1}
