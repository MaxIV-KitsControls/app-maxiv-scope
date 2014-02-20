import re

ALLOWED_MEASUREMENTS = [
    'OFF', 'HIGH', 'LOW', 'AMPLitude', 'MAXimum', 'MINimum', 'PDELta', 'MEAN',
    'RMS', 'STDDev', 'POVershoot', 'NOVershoot', 'AREA', 'RTIMe',
    'FTIMe', 'PPULse', 'NPULse', 'PERiod', 'FREQuency', 'PDCYcle',
    'NDCYcle', 'CYCarea', 'CYCMean', 'CYCRms', 'CYCStddev',
    'PULCnt', 'DELay', 'PHASe', 'BWIDth', 'PSWitching', 'NSWitching',
    'PULSetrain', 'EDGecount', 'SHT', 'SHR', 'PROBemeter',
    'ERPercent', 'ERDB', 'EHEight', 'EWIDth',
    'ETOP', 'EBASe', 'QFACtor', 'RMSNoise', 'SNRatio', 'DCDistortion',
    'ERTime', 'EFTime', 'EBRate', 'EAMPlitude', 'PPJitter', 'STDJitter',
    'RMSJitter', 'CPOWer', 'OBWidth', 'SBWidth', 'THD', 'WCOunt',
    'WSAMples', 'HSAMples', 'HPEak', 'PEAK', 'UPEakvalue', 'LPEakvalue',
    'HMAXimum', 'HMINimum', 'MEDian', 'MAXMin', 'HMEan', 'HSTDdev',
    'M1STddev', 'M2STddev', 'M3STddev', 'MKPositive', 'MKNegativ'
]

ALLOWED_MEASUREMENTS = [(meas, re.match("([A-Z]+).*", meas).groups()[0])
                        for meas in ALLOWED_MEASUREMENTS]

ALLOWED_SOURCES = [
    ("Channel 1", "C1W1"), ("Channel 2", "C2W1"),
    ("Channel 3", "C3W1"), ("Channel 4", "C4W1")
]
