from enum import IntEnum


class VendorSpecificEvents(IntEnum):
    HCI_EXTENSION_SET_RX_GAIN = 0X0400
    HCI_EXTENSION_SET_TX_POWER = 0X0401
    HCI_EXTENSION_ONE_PACKET_PER_EVENT = 0X0402
    HCI_EXTENSION_CLOCK_DIVIDE_ON_HALT = 0X0403
    HCI_EXTENSION_DECLARE_NV_USAGE = 0X0404
    HCI_EXTENSION_DECRYPT = 0X0405
    HCI_EXTENSION_SET_LOCAL_SUPPORTED_FEATURES = 0X0406
    HCI_EXTENSION_SET_FAST_TX_RESPONSE_TIME = 0X0407
    HCI_EXTENSION_MODEM_TEST_TX = 0X0408
    HCI_EXTENSION_MODEM_HOP_TEST_TX = 0X0409
    HCI_EXTENSION_MODEM_TEST_RX = 0X040A
    HCI_EXTENSION_END_MODEM_TEST = 0X040B
    HCI_EXTENSION_SET_BDADDR = 0X040C
    HCI_EXTENSION_SET_SCA = 0X040D
    HCI_EXTENSION_ENABLE_PTM = 0X040E
    HCI_EXTENSION_SET_FREQUENCY_TUNING = 0X040F
    HCI_EXTENSION_SAVE_FREQUENCY_TUNING = 0X0410
    HCI_EXTENSION_SET_MAX_DTM_TX_POWER = 0X0411
    HCI_EXTENSION_MAP_PM_IO_PORT = 0X0412
    HCI_EXTENSION_DISCONNECT_IMMEDIATE = 0X0413
    HCI_EXTENSION_PACKET_ERROR_RATE = 0X0414
    HCI_EXTENSION_PACKET_ERROR_RATE_BY_CHANNEL = 0X0415
    HCI_EXTENSION_EXTEND_RF_RANGE = 0X0416
    HCI_EXTENSION_ADVERTISER_EVENT_NOTICE = 0X0417
    HCI_EXTENSION_CONNECTION_EVENT_NOTICE = 0X0418
    HCI_EXTENSION_HALT_DURING_RF = 0X0419
    HCI_EXTENSION_SET_SLAV_LATENCY_OVERRIDE = 0x041A
    HCI_EXTENSION_BUILD_REVISION = 0x041B
    HCI_EXTENSION_DELAY_SLEEP = 0x041C
    HCI_EXTENSION_RESET_SYSTEM = 0x041D
    HCI_EXTENSION_OVERLAPPED_PROCESSING = 0x041E
    HCI_EXTENSION_NUMBER_COMPLETED_PACKETS_LIMIT = 0x041F
    HCI_EXTENSION_GET_CONNECTION_INFORMATION = 0x0420
    HCI_EXTENSION_SET_MAX_DATA_LENGTH = 0x0421
    HCI_EXTENSION_SCAN_EVENT_NOTICE = 0x0422
    HCI_EXTENSION_SCAN_REQUEST_REPORT = 0x0423

    L2CAP_COMMAND_REJECT = 0x0481
    L2CAP_CONNECTION_PARAMETER_UPDATE_RESPONSE = 0x0493
    L2CAP_CONNECTION_REQUEST = 0x0494
    L2CAP_CHANNEL_ESTABLISHED = 0x04E0
    L2CAP_CHANNEL_TERMINATED = 0x04E1
    L2CAP_OUT_OF_CREDIT = 0x04E2
    L2CAP_PEER_CREDIT_THRESHOLD = 0x04E3
    L2CAP_SEND_SDU_DONE = 0x04E4
    L2CAP_DATA = 0x04F0

    ATT_ERROR_RESPONSE = 0x0501
    ATT_EXCHANGE_MTU_REQUEST = 0x0502
    ATT_EXCHANGE_MTU_RESPONSE = 0x0503
    ATT_FIND_INFORMATION_REQUEST2 = 0x0504
    ATT_FIND_INFORMATION_REQUEST = 0x0505
    ATT_FIND_BY_TYPE_VALUE_REQUEST = 0x0506
    ATT_FIND_BY_TYPE_VALUE_RESPONSE = 0x0507
    ATT_READ_BY_TYPE_REQUEST = 0x0508
    ATT_READ_BY_TYPE_RESPONSE = 0x0509
    ATT_READ_REQUEST = 0x050A
    ATT_READ_RESPONSE = 0x050B
    ATT_READ_BLOB_REQUEST = 0x050C
    ATT_READ_BLOB_RESPONSE = 0x050D
    ATT_READ_MULTIPLE_REQUEST = 0x050E
    ATT_READ_MULTIPLE_RESPONSE = 0x050F
    ATT_READ_BY_GROUP_TYPE_REQUEST = 0x0510
    ATT_READ_BY_GROUP_TYPE_RESPONSE = 0x0511
    ATT_WRITE_REQUEST = 0x0512
    ATT_WRITE_RESPONSE = 0x0513
    ATT_PREPARE_WRITE_REQUEST = 0x0516
    ATT_PREPARE_WRITE_RESPONSE = 0x0517
    ATT_EXECUTE_WRITE_REQUEST = 0x0518
    ATT_EXECUTE_WRITE_RESPONSE = 0x0519
    ATT_HANDLE_VALUE_NOTIFICATION = 0x051B
    ATT_HANDLE_VALUE_INDICATION = 0x051D
    ATT_HANDLE_VALUE_CONFIRMATION = 0x051E
    ATT_MTU_UPDATED_EVT = 0x057F

    GAP_DEVICE_INIT_DONE = 0x0600
    GAP_DEVICE_DISCOVERY = 0x0601
    GAP_ADVERT_DATA_UPDATE_DONE = 0x0602
    GAP_MAKE_DISCOVERABLE_DONE = 0x0603
    GAP_END_DISCOVERABLE_DONE = 0x0604
    GAP_LINK_ESTABLISHED = 0x0605
    GAP_LINK_TERMINATED = 0x0606
    GAP_LINK_PARAMETER_UPDATE2 = 0x0607
    GAP_RANDOM_ADDRESS_CHANGED = 0x0608
    GAP_SIGNATURE_UPDATED = 0x0609
    GAP_AUTHENTICATION_COMPLETE = 0x060A
    GAP_PASSKEY_NEEDED = 0x060B
    GAP_SLAVE_REQUESTED_SECURITY = 0x060C
    GAP_DEVICE_INFORMATION = 0x060D
    GAP_BOND_COMPLETE = 0x060E
    GAP_PAIRING_REQUESTED = 0x060F
    GAP_LINK_PARAMETER_UPDATE = 0x0612
    GAP_COMMAND_STATUS = 0x067F