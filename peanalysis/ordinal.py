ord_translate = {

    'WS2_32.DLL': {
        1: b'accept',
        2: b'bind',
        3: b'closesocket',
        4: b'connect',
        5: b'getpeername',
        6: b'getsockname',
        7: b'getsockopt',
        8: b'htonl',
        9: b'htons',
        10: b'ioctlsocket',
        11: b'inet_addr',
        12: b'inet_ntoa',
        13: b'listen',
        14: b'ntohl',
        15: b'ntohs',
        16: b'recv',
        17: b'recvfrom',
        18: b'select',
        19: b'send',
        20: b'sendto',
        21: b'setsockopt',
        22: b'shutdown',
        23: b'socket',
        24: b'GetAddrInfoW',
        25: b'GetNameInfoW',
        26: b'WSApSetPostRoutine',
        27: b'FreeAddrInfoW',
        28: b'WPUCompleteOverlappedRequest',
        29: b'WSAAccept',
        30: b'WSAAddressToStringA',
        31: b'WSAAddressToStringW',
        32: b'WSACloseEvent',
        33: b'WSAConnect',
        34: b'WSACreateEvent',
        35: b'WSADuplicateSocketA',
        36: b'WSADuplicateSocketW',
        37: b'WSAEnumNameSpaceProvidersA',
        38: b'WSAEnumNameSpaceProvidersW',
        39: b'WSAEnumNetworkEvents',
        40: b'WSAEnumProtocolsA',
        41: b'WSAEnumProtocolsW',
        42: b'WSAEventSelect',
        43: b'WSAGetOverlappedResult',
        44: b'WSAGetQOSByName',
        45: b'WSAGetServiceClassInfoA',
        46: b'WSAGetServiceClassInfoW',
        47: b'WSAGetServiceClassNameByClassIdA',
        48: b'WSAGetServiceClassNameByClassIdW',
        49: b'WSAHtonl',
        50: b'WSAHtons',
        51: b'gethostbyaddr',
        52: b'gethostbyname',
        53: b'getprotobyname',
        54: b'getprotobynumber',
        55: b'getservbyname',
        56: b'getservbyport',
        57: b'gethostname',
        58: b'WSAInstallServiceClassA',
        59: b'WSAInstallServiceClassW',
        60: b'WSAIoctl',
        61: b'WSAJoinLeaf',
        62: b'WSALookupServiceBeginA',
        63: b'WSALookupServiceBeginW',
        64: b'WSALookupServiceEnd',
        65: b'WSALookupServiceNextA',
        66: b'WSALookupServiceNextW',
        67: b'WSANSPIoctl',
        68: b'WSANtohl',
        69: b'WSANtohs',
        70: b'WSAProviderConfigChange',
        71: b'WSARecv',
        72: b'WSARecvDisconnect',
        73: b'WSARecvFrom',
        74: b'WSARemoveServiceClass',
        75: b'WSAResetEvent',
        76: b'WSASend',
        77: b'WSASendDisconnect',
        78: b'WSASendTo',
        79: b'WSASetEvent',
        80: b'WSASetServiceA',
        81: b'WSASetServiceW',
        82: b'WSASocketA',
        83: b'WSASocketW',
        84: b'WSAStringToAddressA',
        85: b'WSAStringToAddressW',
        86: b'WSAWaitForMultipleEvents',
        87: b'WSCDeinstallProvider',
        88: b'WSCEnableNSProvider',
        89: b'WSCEnumProtocols',
        90: b'WSCGetProviderPath',
        91: b'WSCInstallNameSpace',
        92: b'WSCInstallProvider',
        93: b'WSCUnInstallNameSpace',
        94: b'WSCUpdateProvider',
        95: b'WSCWriteNameSpaceOrder',
        96: b'WSCWriteProviderOrder',
        97: b'freeaddrinfo',
        98: b'getaddrinfo',
        99: b'getnameinfo',
        101: b'WSAAsyncSelect',
        102: b'WSAAsyncGetHostByAddr',
        103: b'WSAAsyncGetHostByName',
        104: b'WSAAsyncGetProtoByNumber',
        105: b'WSAAsyncGetProtoByName',
        106: b'WSAAsyncGetServByPort',
        107: b'WSAAsyncGetServByName',
        108: b'WSACancelAsyncRequest',
        109: b'WSASetBlockingHook',
        110: b'WSAUnhookBlockingHook',
        111: b'WSAGetLastError',
        112: b'WSASetLastError',
        113: b'WSACancelBlockingCall',
        114: b'WSAIsBlocking',
        115: b'WSAStartup',
        116: b'WSACleanup',
        151: b'__WSAFDIsSet',
        500: b'WEP',
    },
    'OLEAUT32.DLL': {
        2: b'SysAllocString',
        3: b'SysReAllocString',
        4: b'SysAllocStringLen',
        5: b'SysReAllocStringLen',
        6: b'SysFreeString',
        7: b'SysStringLen',
        8: b'VariantInit',
        9: b'VariantClear',
        10: b'VariantCopy',
        11: b'VariantCopyInd',
        12: b'VariantChangeType',
        13: b'VariantTimeToDosDateTime',
        14: b'DosDateTimeToVariantTime',
        15: b'SafeArrayCreate',
        16: b'SafeArrayDestroy',
        17: b'SafeArrayGetDim',
        18: b'SafeArrayGetElemsize',
        19: b'SafeArrayGetUBound',
        20: b'SafeArrayGetLBound',
        21: b'SafeArrayLock',
        22: b'SafeArrayUnlock',
        23: b'SafeArrayAccessData',
        24: b'SafeArrayUnaccessData',
        25: b'SafeArrayGetElement',
        26: b'SafeArrayPutElement',
        27: b'SafeArrayCopy',
        28: b'DispGetParam',
        29: b'DispGetIDsOfNames',
        30: b'DispInvoke',
        31: b'CreateDispTypeInfo',
        32: b'CreateStdDispatch',
        33: b'RegisterActiveObject',
        34: b'RevokeActiveObject',
        35: b'GetActiveObject',
        36: b'SafeArrayAllocDescriptor',
        37: b'SafeArrayAllocData',
        38: b'SafeArrayDestroyDescriptor',
        39: b'SafeArrayDestroyData',
        40: b'SafeArrayRedim',
        41: b'SafeArrayAllocDescriptorEx',
        42: b'SafeArrayCreateEx',
        43: b'SafeArrayCreateVectorEx',
        44: b'SafeArraySetRecordInfo',
        45: b'SafeArrayGetRecordInfo',
        46: b'VarParseNumFromStr',
        47: b'VarNumFromParseNum',
        48: b'VarI2FromUI1',
        49: b'VarI2FromI4',
        50: b'VarI2FromR4',
        51: b'VarI2FromR8',
        52: b'VarI2FromCy',
        53: b'VarI2FromDate',
        54: b'VarI2FromStr',
        55: b'VarI2FromDisp',
        56: b'VarI2FromBool',
        57: b'SafeArraySetIID',
        58: b'VarI4FromUI1',
        59: b'VarI4FromI2',
        60: b'VarI4FromR4',
        61: b'VarI4FromR8',
        62: b'VarI4FromCy',
        63: b'VarI4FromDate',
        64: b'VarI4FromStr',
        65: b'VarI4FromDisp',
        66: b'VarI4FromBool',
        67: b'SafeArrayGetIID',
        68: b'VarR4FromUI1',
        69: b'VarR4FromI2',
        70: b'VarR4FromI4',
        71: b'VarR4FromR8',
        72: b'VarR4FromCy',
        73: b'VarR4FromDate',
        74: b'VarR4FromStr',
        75: b'VarR4FromDisp',
        76: b'VarR4FromBool',
        77: b'SafeArrayGetVartype',
        78: b'VarR8FromUI1',
        79: b'VarR8FromI2',
        80: b'VarR8FromI4',
        81: b'VarR8FromR4',
        82: b'VarR8FromCy',
        83: b'VarR8FromDate',
        84: b'VarR8FromStr',
        85: b'VarR8FromDisp',
        86: b'VarR8FromBool',
        87: b'VarFormat',
        88: b'VarDateFromUI1',
        89: b'VarDateFromI2',
        90: b'VarDateFromI4',
        91: b'VarDateFromR4',
        92: b'VarDateFromR8',
        93: b'VarDateFromCy',
        94: b'VarDateFromStr',
        95: b'VarDateFromDisp',
        96: b'VarDateFromBool',
        97: b'VarFormatDateTime',
        98: b'VarCyFromUI1',
        99: b'VarCyFromI2',
        100: b'VarCyFromI4',
        101: b'VarCyFromR4',
        102: b'VarCyFromR8',
        103: b'VarCyFromDate',
        104: b'VarCyFromStr',
        105: b'VarCyFromDisp',
        106: b'VarCyFromBool',
        107: b'VarFormatNumber',
        108: b'VarBstrFromUI1',
        109: b'VarBstrFromI2',
        110: b'VarBstrFromI4',
        111: b'VarBstrFromR4',
        112: b'VarBstrFromR8',
        113: b'VarBstrFromCy',
        114: b'VarBstrFromDate',
        115: b'VarBstrFromDisp',
        116: b'VarBstrFromBool',
        117: b'VarFormatPercent',
        118: b'VarBoolFromUI1',
        119: b'VarBoolFromI2',
        120: b'VarBoolFromI4',
        121: b'VarBoolFromR4',
        122: b'VarBoolFromR8',
        123: b'VarBoolFromDate',
        124: b'VarBoolFromCy',
        125: b'VarBoolFromStr',
        126: b'VarBoolFromDisp',
        127: b'VarFormatCurrency',
        128: b'VarWeekdayName',
        129: b'VarMonthName',
        130: b'VarUI1FromI2',
        131: b'VarUI1FromI4',
        132: b'VarUI1FromR4',
        133: b'VarUI1FromR8',
        134: b'VarUI1FromCy',
        135: b'VarUI1FromDate',
        136: b'VarUI1FromStr',
        137: b'VarUI1FromDisp',
        138: b'VarUI1FromBool',
        139: b'VarFormatFromTokens',
        140: b'VarTokenizeFormatString',
        141: b'VarAdd',
        142: b'VarAnd',
        143: b'VarDiv',
        144: b'DllCanUnloadNow',
        145: b'DllGetClassObject',
        146: b'DispCallFunc',
        147: b'VariantChangeTypeEx',
        148: b'SafeArrayPtrOfIndex',
        149: b'SysStringByteLen',
        150: b'SysAllocStringByteLen',
        151: b'DllRegisterServer',
        152: b'VarEqv',
        153: b'VarIdiv',
        154: b'VarImp',
        155: b'VarMod',
        156: b'VarMul',
        157: b'VarOr',
        158: b'VarPow',
        159: b'VarSub',
        160: b'CreateTypeLib',
        161: b'LoadTypeLib',
        162: b'LoadRegTypeLib',
        163: b'RegisterTypeLib',
        164: b'QueryPathOfRegTypeLib',
        165: b'LHashValOfNameSys',
        166: b'LHashValOfNameSysA',
        167: b'VarXor',
        168: b'VarAbs',
        169: b'VarFix',
        170: b'OaBuildVersion',
        171: b'ClearCustData',
        172: b'VarInt',
        173: b'VarNeg',
        174: b'VarNot',
        175: b'VarRound',
        176: b'VarCmp',
        177: b'VarDecAdd',
        178: b'VarDecDiv',
        179: b'VarDecMul',
        180: b'CreateTypeLib2',
        181: b'VarDecSub',
        182: b'VarDecAbs',
        183: b'LoadTypeLibEx',
        184: b'SystemTimeToVariantTime',
        185: b'VariantTimeToSystemTime',
        186: b'UnRegisterTypeLib',
        187: b'VarDecFix',
        188: b'VarDecInt',
        189: b'VarDecNeg',
        190: b'VarDecFromUI1',
        191: b'VarDecFromI2',
        192: b'VarDecFromI4',
        193: b'VarDecFromR4',
        194: b'VarDecFromR8',
        195: b'VarDecFromDate',
        196: b'VarDecFromCy',
        197: b'VarDecFromStr',
        198: b'VarDecFromDisp',
        199: b'VarDecFromBool',
        200: b'GetErrorInfo',
        201: b'SetErrorInfo',
        202: b'CreateErrorInfo',
        203: b'VarDecRound',
        204: b'VarDecCmp',
        205: b'VarI2FromI1',
        206: b'VarI2FromUI2',
        207: b'VarI2FromUI4',
        208: b'VarI2FromDec',
        209: b'VarI4FromI1',
        210: b'VarI4FromUI2',
        211: b'VarI4FromUI4',
        212: b'VarI4FromDec',
        213: b'VarR4FromI1',
        214: b'VarR4FromUI2',
        215: b'VarR4FromUI4',
        216: b'VarR4FromDec',
        217: b'VarR8FromI1',
        218: b'VarR8FromUI2',
        219: b'VarR8FromUI4',
        220: b'VarR8FromDec',
        221: b'VarDateFromI1',
        222: b'VarDateFromUI2',
        223: b'VarDateFromUI4',
        224: b'VarDateFromDec',
        225: b'VarCyFromI1',
        226: b'VarCyFromUI2',
        227: b'VarCyFromUI4',
        228: b'VarCyFromDec',
        229: b'VarBstrFromI1',
        230: b'VarBstrFromUI2',
        231: b'VarBstrFromUI4',
        232: b'VarBstrFromDec',
        233: b'VarBoolFromI1',
        234: b'VarBoolFromUI2',
        235: b'VarBoolFromUI4',
        236: b'VarBoolFromDec',
        237: b'VarUI1FromI1',
        238: b'VarUI1FromUI2',
        239: b'VarUI1FromUI4',
        240: b'VarUI1FromDec',
        241: b'VarDecFromI1',
        242: b'VarDecFromUI2',
        243: b'VarDecFromUI4',
        244: b'VarI1FromUI1',
        245: b'VarI1FromI2',
        246: b'VarI1FromI4',
        247: b'VarI1FromR4',
        248: b'VarI1FromR8',
        249: b'VarI1FromDate',
        250: b'VarI1FromCy',
        251: b'VarI1FromStr',
        252: b'VarI1FromDisp',
        253: b'VarI1FromBool',
        254: b'VarI1FromUI2',
        255: b'VarI1FromUI4',
        256: b'VarI1FromDec',
        257: b'VarUI2FromUI1',
        258: b'VarUI2FromI2',
        259: b'VarUI2FromI4',
        260: b'VarUI2FromR4',
        261: b'VarUI2FromR8',
        262: b'VarUI2FromDate',
        263: b'VarUI2FromCy',
        264: b'VarUI2FromStr',
        265: b'VarUI2FromDisp',
        266: b'VarUI2FromBool',
        267: b'VarUI2FromI1',
        268: b'VarUI2FromUI4',
        269: b'VarUI2FromDec',
        270: b'VarUI4FromUI1',
        271: b'VarUI4FromI2',
        272: b'VarUI4FromI4',
        273: b'VarUI4FromR4',
        274: b'VarUI4FromR8',
        275: b'VarUI4FromDate',
        276: b'VarUI4FromCy',
        277: b'VarUI4FromStr',
        278: b'VarUI4FromDisp',
        279: b'VarUI4FromBool',
        280: b'VarUI4FromI1',
        281: b'VarUI4FromUI2',
        282: b'VarUI4FromDec',
        283: b'BSTR_UserSize',
        284: b'BSTR_UserMarshal',
        285: b'BSTR_UserUnmarshal',
        286: b'BSTR_UserFree',
        287: b'VARIANT_UserSize',
        288: b'VARIANT_UserMarshal',
        289: b'VARIANT_UserUnmarshal',
        290: b'VARIANT_UserFree',
        291: b'LPSAFEARRAY_UserSize',
        292: b'LPSAFEARRAY_UserMarshal',
        293: b'LPSAFEARRAY_UserUnmarshal',
        294: b'LPSAFEARRAY_UserFree',
        295: b'LPSAFEARRAY_Size',
        296: b'LPSAFEARRAY_Marshal',
        297: b'LPSAFEARRAY_Unmarshal',
        298: b'VarDecCmpR8',
        299: b'VarCyAdd',
        300: b'DllUnregisterServer',
        301: b'OACreateTypeLib2',
        303: b'VarCyMul',
        304: b'VarCyMulI4',
        305: b'VarCySub',
        306: b'VarCyAbs',
        307: b'VarCyFix',
        308: b'VarCyInt',
        309: b'VarCyNeg',
        310: b'VarCyRound',
        311: b'VarCyCmp',
        312: b'VarCyCmpR8',
        313: b'VarBstrCat',
        314: b'VarBstrCmp',
        315: b'VarR8Pow',
        316: b'VarR4CmpR8',
        317: b'VarR8Round',
        318: b'VarCat',
        319: b'VarDateFromUdateEx',
        322: b'GetRecordInfoFromGuids',
        323: b'GetRecordInfoFromTypeInfo',
        325: b'SetVarConversionLocaleSetting',
        326: b'GetVarConversionLocaleSetting',
        327: b'SetOaNoCache',
        329: b'VarCyMulI8',
        330: b'VarDateFromUdate',
        331: b'VarUdateFromDate',
        332: b'GetAltMonthNames',
        333: b'VarI8FromUI1',
        334: b'VarI8FromI2',
        335: b'VarI8FromR4',
        336: b'VarI8FromR8',
        337: b'VarI8FromCy',
        338: b'VarI8FromDate',
        339: b'VarI8FromStr',
        340: b'VarI8FromDisp',
        341: b'VarI8FromBool',
        342: b'VarI8FromI1',
        343: b'VarI8FromUI2',
        344: b'VarI8FromUI4',
        345: b'VarI8FromDec',
        346: b'VarI2FromI8',
        347: b'VarI2FromUI8',
        348: b'VarI4FromI8',
        349: b'VarI4FromUI8',
        360: b'VarR4FromI8',
        361: b'VarR4FromUI8',
        362: b'VarR8FromI8',
        363: b'VarR8FromUI8',
        364: b'VarDateFromI8',
        365: b'VarDateFromUI8',
        366: b'VarCyFromI8',
        367: b'VarCyFromUI8',
        368: b'VarBstrFromI8',
        369: b'VarBstrFromUI8',
        370: b'VarBoolFromI8',
        371: b'VarBoolFromUI8',
        372: b'VarUI1FromI8',
        373: b'VarUI1FromUI8',
        374: b'VarDecFromI8',
        375: b'VarDecFromUI8',
        376: b'VarI1FromI8',
        377: b'VarI1FromUI8',
        378: b'VarUI2FromI8',
        379: b'VarUI2FromUI8',
        401: b'OleLoadPictureEx',
        402: b'OleLoadPictureFileEx',
        411: b'SafeArrayCreateVector',
        412: b'SafeArrayCopyData',
        413: b'VectorFromBstr',
        414: b'BstrFromVector',
        415: b'OleIconToCursor',
        416: b'OleCreatePropertyFrameIndirect',
        417: b'OleCreatePropertyFrame',
        418: b'OleLoadPicture',
        419: b'OleCreatePictureIndirect',
        420: b'OleCreateFontIndirect',
        421: b'OleTranslateColor',
        422: b'OleLoadPictureFile',
        423: b'OleSavePictureFile',
        424: b'OleLoadPicturePath',
        425: b'VarUI4FromI8',
        426: b'VarUI4FromUI8',
        427: b'VarI8FromUI8',
        428: b'VarUI8FromI8',
        429: b'VarUI8FromUI1',
        430: b'VarUI8FromI2',
        431: b'VarUI8FromR4',
        432: b'VarUI8FromR8',
        433: b'VarUI8FromCy',
        434: b'VarUI8FromDate',
        435: b'VarUI8FromStr',
        436: b'VarUI8FromDisp',
        437: b'VarUI8FromBool',
        438: b'VarUI8FromI1',
        439: b'VarUI8FromUI2',
        440: b'VarUI8FromUI4',
        441: b'VarUI8FromDec',
        442: b'RegisterTypeLibForUser',
        443: b'UnRegisterTypeLibForUser',
    }
}
