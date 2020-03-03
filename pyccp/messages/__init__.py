import enum
import cantools


class CommandCodes(enum.IntEnum):
    # Mandatory commands
    CONNECT = 0x01
    GET_CCP_VERSION = 0x1B
    EXCHANGE_ID = 0x17
    SET_MTA = 0x02
    DNLOAD = 0x03
    UPLOAD = 0x04
    GET_DAQ_SIZE = 0x14
    SET_DAQ_PTR = 0x15
    WRITE_DAQ = 0x16
    START_STOP = 0x06
    DISCONNECT = 0x07
    # Optional commands
    GET_SEED = 0x12
    UNLOCK = 0x13
    DNLOAD_6 = 0x23
    SHORT_UP = 0x0F
    SELECT_CAL_PAGE = 0x11
    SET_S_STATUS = 0x0C
    GET_S_STATUS = 0x0D
    BUILD_CHKSUM = 0x0E
    CLEAR_MEMORY = 0x10
    PROGRAM = 0x18
    PROGRAM_6 = 0x22
    MOVE = 0x19
    TEST = 0x05
    GET_ACTIVE_CAL_PAGE = 0x09
    START_STOP_ALL = 0x08
    DIAG_SERVICE = 0x20
    ACTION_SERVICE = 0x21


class ReturnCodes(enum.IntEnum):
    ACKNOWLEDGE = 0x00
    DAQ_PROCESSOR_OVERLOAD = 0x01  # C0
    COMMAND_PROCESSOR_BUSY = 0x10  # C1 NONE (wait until ACK or timeout)
    DAQ_PROCESSOR_BUSY = 0x11  # C1 NONE (wait until ACK or timeout)
    INTERNAL_TIMEOUT = 0x12  # C1 NONE (wait until ACK or timeout)
    KEY_REQUEST = 0x18  # C1 NONE (embedded seed&key)
    SESSION_STATUS_REQUEST = 0x19  # C1 NONE (embedded SET_S_STATUS)
    COLD_START_REQUEST = 0x20  # C2 COLD START
    CAL_DATA_INIT_REQUEST = 0x21  # C2 cal. data initialization
    DAQ_LIST_INIT_REQUEST = 0x22  # C2 DAQ list initialization
    CODE_UPDATE_REQUEST = 0x23  # C2 (COLD START)
    UNKNOWN_COMMAND = 0x30  # C3 (FAULT)
    COMMAND_SYNTAX = 0x31  # C3 FAULT
    PARAMETER_OUT_OF_RANGE = 0x32  # C3 FAULT
    ACCESS_DENIED = 0x33  # C3 FAULT
    OVERLOAD = 0x34  # C3 FAULT
    ACCESS_LOCKED = 0x35  # C3 FAULT
    RESOURCE_FUNCTION_NOT_AVAILABLE = 0x36  # C3 FAULT


class DTOType(enum.IntEnum):
    COMMAND_RETURN_MESSAGE = 0xFF
    EVENT_MESSAGE = 0xFE


COMMANDS_DB = cantools.database.load_file("pyccp/messages/commands.dbc")

COMMAND_DISPATCH = {
    # Mandatory commands
    CommandCodes.CONNECT: COMMANDS_DB.get_message_by_name("connect"),
    CommandCodes.GET_CCP_VERSION: COMMANDS_DB.get_message_by_name("get_ccp_version"),
    CommandCodes.EXCHANGE_ID: COMMANDS_DB.get_message_by_name("exchange_id"),
    CommandCodes.SET_MTA: COMMANDS_DB.get_message_by_name("set_mta"),
    CommandCodes.DNLOAD: COMMANDS_DB.get_message_by_name("dnload"),
    CommandCodes.UPLOAD: COMMANDS_DB.get_message_by_name("upload"),
    CommandCodes.GET_DAQ_SIZE: COMMANDS_DB.get_message_by_name("get_daq_size"),
    CommandCodes.SET_DAQ_PTR: COMMANDS_DB.get_message_by_name("set_daq_ptr"),
    CommandCodes.WRITE_DAQ: COMMANDS_DB.get_message_by_name("write_daq"),
    CommandCodes.START_STOP: COMMANDS_DB.get_message_by_name("start_stop"),
    CommandCodes.DISCONNECT: COMMANDS_DB.get_message_by_name("disconnect"),
    # Optional commands
    # CommandCodes.GET_SEED: getSeed,
    # CommandCodes.UNLOCK: unlock,
    # CommandCodes.DNLOAD_6: dnload6,
    # CommandCodes.SHORT_UP: shortUp,
    # CommandCodes.SELECT_CAL_PAGE: selectCalPage,
    CommandCodes.SET_S_STATUS: COMMANDS_DB.get_message_by_name("set_s_status"),
    # CommandCodes.GET_S_STATUS: getSStatus,
    # CommandCodes.BUILD_CHKSUM: buildChksum,
    # CommandCodes.CLEAR_MEMORY: clearMemory,
    # CommandCodes.PROGRAM: program,
    # CommandCodes.PROGRAM_6: program6,
    # CommandCodes.MOVE: move,
    # CommandCodes.TEST: test,
    # CommandCodes.GET_ACTIVE_CAL_PAGE: getActiveCalPage,
    # CommandCodes.START_STOP_ALL: startStopAll,
}
