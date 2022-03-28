# The PEP 484 type hints stub file for the QtNfc module.
#
# Generated by SIP 6.5.1
#
# Copyright (c) 2022 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt6.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Support for QDate, QDateTime and QTime.
import datetime
import enum
import typing

import PyQt6.sip
from PyQt6 import QtCore

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

class QNdefFilter(PyQt6.sip.simplewrapper):
    class Record(PyQt6.sip.simplewrapper):

        maximum = ...  # type: int
        minimum = ...  # type: int
        type = ...  # type: QtCore.QByteArray
        typeNameFormat = ...  # type: 'QNdefRecord.TypeNameFormat'
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: "QNdefFilter.Record") -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: "QNdefFilter") -> None: ...
    def match(self, message: "QNdefMessage") -> bool: ...
    def recordAt(self, i: int) -> "QNdefFilter.Record": ...
    def __len__(self) -> int: ...
    def recordCount(self) -> int: ...
    @typing.overload
    def appendRecord(self, record: "QNdefFilter.Record") -> bool: ...
    @typing.overload
    def appendRecord(self, typeNameFormat: "QNdefRecord.TypeNameFormat", type: QtCore.QByteArray, min: int = ..., max: int = ...) -> bool: ...
    def orderMatch(self) -> bool: ...
    def setOrderMatch(self, on: bool) -> None: ...
    def clear(self) -> None: ...

class QNdefMessage(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, record: "QNdefRecord") -> None: ...
    @typing.overload
    def __init__(self, message: "QNdefMessage") -> None: ...
    @typing.overload
    def __init__(self, records: typing.Iterable["QNdefRecord"]) -> None: ...
    @staticmethod
    def fromByteArray(message: QtCore.QByteArray) -> "QNdefMessage": ...
    def __delitem__(self, i: int) -> None: ...
    def __setitem__(self, i: int, value: "QNdefRecord") -> None: ...
    def __getitem__(self, i: int) -> "QNdefRecord": ...
    def __len__(self) -> int: ...
    def toByteArray(self) -> QtCore.QByteArray: ...

class QNdefRecord(PyQt6.sip.simplewrapper):
    class TypeNameFormat(enum.Enum):
        Empty = ...  # type: QNdefRecord.TypeNameFormat
        NfcRtd = ...  # type: QNdefRecord.TypeNameFormat
        Mime = ...  # type: QNdefRecord.TypeNameFormat
        Uri = ...  # type: QNdefRecord.TypeNameFormat
        ExternalRtd = ...  # type: QNdefRecord.TypeNameFormat
        Unknown = ...  # type: QNdefRecord.TypeNameFormat
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: "QNdefRecord") -> None: ...
    def __hash__(self) -> int: ...
    def clear(self) -> None: ...
    def isEmpty(self) -> bool: ...
    def payload(self) -> QtCore.QByteArray: ...
    def setPayload(self, payload: QtCore.QByteArray) -> None: ...
    def id(self) -> QtCore.QByteArray: ...
    def setId(self, id: QtCore.QByteArray) -> None: ...
    def type(self) -> QtCore.QByteArray: ...
    def setType(self, type: QtCore.QByteArray) -> None: ...
    def typeNameFormat(self) -> "QNdefRecord.TypeNameFormat": ...
    def setTypeNameFormat(self, typeNameFormat: "QNdefRecord.TypeNameFormat") -> None: ...

class QNdefNfcIconRecord(QNdefRecord):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    @typing.overload
    def __init__(self, a0: "QNdefNfcIconRecord") -> None: ...
    def data(self) -> QtCore.QByteArray: ...
    def setData(self, data: QtCore.QByteArray) -> None: ...

class QNdefNfcSmartPosterRecord(QNdefRecord):
    class Action(enum.Enum):
        UnspecifiedAction = ...  # type: QNdefNfcSmartPosterRecord.Action
        DoAction = ...  # type: QNdefNfcSmartPosterRecord.Action
        SaveAction = ...  # type: QNdefNfcSmartPosterRecord.Action
        EditAction = ...  # type: QNdefNfcSmartPosterRecord.Action
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: "QNdefNfcSmartPosterRecord") -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    def setTypeInfo(self, type: str) -> None: ...
    def typeInfo(self) -> str: ...
    def setSize(self, size: int) -> None: ...
    def size(self) -> int: ...
    def setIcons(self, icons: typing.Iterable[QNdefNfcIconRecord]) -> None: ...
    @typing.overload
    def removeIcon(self, icon: QNdefNfcIconRecord) -> bool: ...
    @typing.overload
    def removeIcon(self, type: QtCore.QByteArray) -> bool: ...
    @typing.overload
    def addIcon(self, icon: QNdefNfcIconRecord) -> None: ...
    @typing.overload
    def addIcon(self, type: QtCore.QByteArray, data: QtCore.QByteArray) -> None: ...
    def iconRecords(self) -> typing.List[QNdefNfcIconRecord]: ...
    def iconRecord(self, index: int) -> QNdefNfcIconRecord: ...
    def icon(self, mimetype: QtCore.QByteArray = ...) -> QtCore.QByteArray: ...
    def iconCount(self) -> int: ...
    def setAction(self, act: "QNdefNfcSmartPosterRecord.Action") -> None: ...
    def action(self) -> "QNdefNfcSmartPosterRecord.Action": ...
    @typing.overload
    def setUri(self, url: "QNdefNfcUriRecord") -> None: ...
    @typing.overload
    def setUri(self, url: QtCore.QUrl) -> None: ...
    def uriRecord(self) -> "QNdefNfcUriRecord": ...
    def uri(self) -> QtCore.QUrl: ...
    def setTitles(self, titles: typing.Iterable["QNdefNfcTextRecord"]) -> None: ...
    @typing.overload
    def removeTitle(self, text: "QNdefNfcTextRecord") -> bool: ...
    @typing.overload
    def removeTitle(self, locale: str) -> bool: ...
    @typing.overload
    def addTitle(self, text: "QNdefNfcTextRecord") -> bool: ...
    @typing.overload
    def addTitle(self, text: str, locale: str, encoding: "QNdefNfcTextRecord.Encoding") -> bool: ...
    def titleRecords(self) -> typing.List["QNdefNfcTextRecord"]: ...
    def titleRecord(self, index: int) -> "QNdefNfcTextRecord": ...
    def title(self, locale: str = ...) -> str: ...
    def titleCount(self) -> int: ...
    def hasTypeInfo(self) -> bool: ...
    def hasSize(self) -> bool: ...
    def hasIcon(self, mimetype: QtCore.QByteArray = ...) -> bool: ...
    def hasAction(self) -> bool: ...
    def hasTitle(self, locale: str = ...) -> bool: ...
    def setPayload(self, payload: QtCore.QByteArray) -> None: ...

class QNdefNfcTextRecord(QNdefRecord):
    class Encoding(enum.Enum):
        Utf8 = ...  # type: QNdefNfcTextRecord.Encoding
        Utf16 = ...  # type: QNdefNfcTextRecord.Encoding
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    @typing.overload
    def __init__(self, a0: "QNdefNfcTextRecord") -> None: ...
    def setEncoding(self, encoding: "QNdefNfcTextRecord.Encoding") -> None: ...
    def encoding(self) -> "QNdefNfcTextRecord.Encoding": ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...
    def setLocale(self, locale: str) -> None: ...
    def locale(self) -> str: ...

class QNdefNfcUriRecord(QNdefRecord):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    @typing.overload
    def __init__(self, a0: "QNdefNfcUriRecord") -> None: ...
    def setUri(self, uri: QtCore.QUrl) -> None: ...
    def uri(self) -> QtCore.QUrl: ...

class QNearFieldManager(QtCore.QObject):
    class AdapterState(enum.Enum):
        Offline = ...  # type: QNearFieldManager.AdapterState
        TurningOn = ...  # type: QNearFieldManager.AdapterState
        Online = ...  # type: QNearFieldManager.AdapterState
        TurningOff = ...  # type: QNearFieldManager.AdapterState
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def setUserInformation(self, message: str) -> None: ...
    def isEnabled(self) -> bool: ...
    adapterStateChanged: typing.ClassVar[QtCore.pyqtSignal]
    def isSupported(self, accessMethod: "QNearFieldTarget.AccessMethod" = ...) -> bool: ...
    targetDetectionStopped: typing.ClassVar[QtCore.pyqtSignal]
    targetLost: typing.ClassVar[QtCore.pyqtSignal]
    targetDetected: typing.ClassVar[QtCore.pyqtSignal]
    def stopTargetDetection(self, errorMessage: str = ...) -> None: ...
    def startTargetDetection(self, accessMethod: "QNearFieldTarget.AccessMethod") -> bool: ...

class QNearFieldTarget(QtCore.QObject):
    class Error(enum.Enum):
        NoError = ...  # type: QNearFieldTarget.Error
        UnknownError = ...  # type: QNearFieldTarget.Error
        UnsupportedError = ...  # type: QNearFieldTarget.Error
        TargetOutOfRangeError = ...  # type: QNearFieldTarget.Error
        NoResponseError = ...  # type: QNearFieldTarget.Error
        ChecksumMismatchError = ...  # type: QNearFieldTarget.Error
        InvalidParametersError = ...  # type: QNearFieldTarget.Error
        NdefReadError = ...  # type: QNearFieldTarget.Error
        NdefWriteError = ...  # type: QNearFieldTarget.Error
        CommandError = ...  # type: QNearFieldTarget.Error
        ConnectionError = ...  # type: QNearFieldTarget.Error
        TimeoutError = ...  # type: QNearFieldTarget.Error
    class AccessMethod(enum.Flag):
        UnknownAccess = ...  # type: QNearFieldTarget.AccessMethod
        NdefAccess = ...  # type: QNearFieldTarget.AccessMethod
        TagTypeSpecificAccess = ...  # type: QNearFieldTarget.AccessMethod
        AnyAccess = ...  # type: QNearFieldTarget.AccessMethod
    class Type(enum.Enum):
        ProprietaryTag = ...  # type: QNearFieldTarget.Type
        NfcTagType1 = ...  # type: QNearFieldTarget.Type
        NfcTagType2 = ...  # type: QNearFieldTarget.Type
        NfcTagType3 = ...  # type: QNearFieldTarget.Type
        NfcTagType4 = ...  # type: QNearFieldTarget.Type
        NfcTagType4A = ...  # type: QNearFieldTarget.Type
        NfcTagType4B = ...  # type: QNearFieldTarget.Type
        MifareTag = ...  # type: QNearFieldTarget.Type
    class RequestId(PyQt6.sip.simplewrapper):
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, other: "QNearFieldTarget.RequestId") -> None: ...
        def refCount(self) -> int: ...
        def isValid(self) -> bool: ...
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def maxCommandLength(self) -> int: ...
    def disconnect(self) -> bool: ...  # type: ignore[override]
    error: typing.ClassVar[QtCore.pyqtSignal]
    requestCompleted: typing.ClassVar[QtCore.pyqtSignal]
    ndefMessageRead: typing.ClassVar[QtCore.pyqtSignal]
    disconnected: typing.ClassVar[QtCore.pyqtSignal]
    def requestResponse(self, id: "QNearFieldTarget.RequestId") -> typing.Any: ...
    def waitForRequestCompleted(self, id: "QNearFieldTarget.RequestId", msecs: int = ...) -> bool: ...
    def sendCommand(self, command: QtCore.QByteArray) -> "QNearFieldTarget.RequestId": ...
    def writeNdefMessages(self, messages: typing.Iterable[QNdefMessage]) -> "QNearFieldTarget.RequestId": ...
    def readNdefMessages(self) -> "QNearFieldTarget.RequestId": ...
    def hasNdefMessage(self) -> bool: ...
    def accessMethods(self) -> "QNearFieldTarget.AccessMethod": ...
    def type(self) -> "QNearFieldTarget.Type": ...
    def uid(self) -> QtCore.QByteArray: ...
