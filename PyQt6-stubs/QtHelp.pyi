# The PEP 484 type hints stub file for the QtHelp module.
#
# Generated by SIP 6.6.2
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
from PyQt6 import QtCore, QtGui, QtWidgets

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

class QCompressedHelpInfo(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: "QCompressedHelpInfo") -> None: ...
    def isNull(self) -> bool: ...
    @staticmethod
    def fromCompressedHelpFile(documentationFileName: str) -> "QCompressedHelpInfo": ...
    def version(self) -> QtCore.QVersionNumber: ...
    def component(self) -> str: ...
    def namespaceName(self) -> str: ...
    def swap(self, other: "QCompressedHelpInfo") -> None: ...

class QHelpContentItem(PyQt6.sip.simplewrapper):
    def childPosition(self, child: "QHelpContentItem") -> int: ...
    def parent(self) -> "QHelpContentItem": ...
    def row(self) -> int: ...
    def url(self) -> QtCore.QUrl: ...
    def title(self) -> str: ...
    def childCount(self) -> int: ...
    def child(self, row: int) -> "QHelpContentItem": ...

class QHelpContentModel(QtCore.QAbstractItemModel):

    contentsCreated: typing.ClassVar[QtCore.pyqtSignal]
    contentsCreationStarted: typing.ClassVar[QtCore.pyqtSignal]
    def isCreatingContents(self) -> bool: ...
    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def parent(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex: ...  # type: ignore[override]
    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex: ...
    def data(self, index: QtCore.QModelIndex, role: int) -> typing.Any: ...  # type: ignore[override]
    def contentItemAt(self, index: QtCore.QModelIndex) -> QHelpContentItem: ...
    def createContents(self, customFilterName: str) -> None: ...

class QHelpContentWidget(QtWidgets.QTreeView):

    linkActivated: typing.ClassVar[QtCore.pyqtSignal]
    def indexOf(self, link: QtCore.QUrl) -> QtCore.QModelIndex: ...

class QHelpEngineCore(QtCore.QObject):
    def __init__(self, collectionFile: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def setReadOnly(self, enable: bool) -> None: ...
    def isReadOnly(self) -> bool: ...
    @typing.overload
    def documentsForKeyword(self, keyword: str) -> typing.List["QHelpLink"]: ...
    @typing.overload
    def documentsForKeyword(self, keyword: str, filterName: str) -> typing.List["QHelpLink"]: ...
    @typing.overload
    def documentsForIdentifier(self, id: str) -> typing.List["QHelpLink"]: ...
    @typing.overload
    def documentsForIdentifier(self, id: str, filterName: str) -> typing.List["QHelpLink"]: ...
    def usesFilterEngine(self) -> bool: ...
    def setUsesFilterEngine(self, uses: bool) -> None: ...
    def files(self, namespaceName: str, filterName: str, extensionFilter: str = ...) -> typing.List[QtCore.QUrl]: ...
    def filterEngine(self) -> "QHelpFilterEngine": ...
    warning: typing.ClassVar[QtCore.pyqtSignal]
    setupFinished: typing.ClassVar[QtCore.pyqtSignal]
    setupStarted: typing.ClassVar[QtCore.pyqtSignal]
    def setAutoSaveFilter(self, save: bool) -> None: ...
    def autoSaveFilter(self) -> bool: ...
    def error(self) -> str: ...
    @staticmethod
    def metaData(documentationFileName: str, name: str) -> typing.Any: ...
    def setCustomValue(self, key: str, value: typing.Any) -> bool: ...
    def customValue(self, key: str, defaultValue: typing.Any = ...) -> typing.Any: ...
    def removeCustomValue(self, key: str) -> bool: ...
    def fileData(self, url: QtCore.QUrl) -> QtCore.QByteArray: ...
    def findFile(self, url: QtCore.QUrl) -> QtCore.QUrl: ...
    def registeredDocumentations(self) -> typing.List[str]: ...
    def documentationFileName(self, namespaceName: str) -> str: ...
    def unregisterDocumentation(self, namespaceName: str) -> bool: ...
    def registerDocumentation(self, documentationFileName: str) -> bool: ...
    @staticmethod
    def namespaceName(documentationFileName: str) -> str: ...
    def copyCollectionFile(self, fileName: str) -> bool: ...
    def setCollectionFile(self, fileName: str) -> None: ...
    def collectionFile(self) -> str: ...
    def setupData(self) -> bool: ...

class QHelpEngine(QHelpEngineCore):
    def __init__(self, collectionFile: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def searchEngine(self) -> "QHelpSearchEngine": ...
    def indexWidget(self) -> "QHelpIndexWidget": ...
    def contentWidget(self) -> QHelpContentWidget: ...
    def indexModel(self) -> "QHelpIndexModel": ...
    def contentModel(self) -> QHelpContentModel: ...

class QHelpFilterData(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: "QHelpFilterData") -> None: ...
    def __ne__(self, other: object): ...
    def versions(self) -> typing.List[QtCore.QVersionNumber]: ...
    def components(self) -> typing.List[str]: ...
    def setVersions(self, versions: typing.Iterable[QtCore.QVersionNumber]) -> None: ...
    def setComponents(self, components: typing.Iterable[str]) -> None: ...
    def swap(self, other: "QHelpFilterData") -> None: ...
    def __eq__(self, other: object): ...

class QHelpFilterEngine(QtCore.QObject):
    @typing.overload
    def indices(self) -> typing.List[str]: ...
    @typing.overload
    def indices(self, filterName: str) -> typing.List[str]: ...
    def availableVersions(self) -> typing.List[QtCore.QVersionNumber]: ...
    filterActivated: typing.ClassVar[QtCore.pyqtSignal]
    def namespacesForFilter(self, filterName: str) -> typing.List[str]: ...
    def removeFilter(self, filterName: str) -> bool: ...
    def setFilterData(self, filterName: str, filterData: QHelpFilterData) -> bool: ...
    def filterData(self, filterName: str) -> QHelpFilterData: ...
    def availableComponents(self) -> typing.List[str]: ...
    def setActiveFilter(self, filterName: str) -> bool: ...
    def activeFilter(self) -> str: ...
    def filters(self) -> typing.List[str]: ...
    def namespaceToVersion(self) -> typing.Dict[str, QtCore.QVersionNumber]: ...
    def namespaceToComponent(self) -> typing.Dict[str, str]: ...

class QHelpFilterSettingsWidget(QtWidgets.QWidget):
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def applySettings(self, filterEngine: QHelpFilterEngine) -> bool: ...
    def readSettings(self, filterEngine: QHelpFilterEngine) -> None: ...
    def setAvailableVersions(self, versions: typing.Iterable[QtCore.QVersionNumber]) -> None: ...
    def setAvailableComponents(self, components: typing.Iterable[str]) -> None: ...

class QHelpIndexModel(QtCore.QStringListModel):

    indexCreated: typing.ClassVar[QtCore.pyqtSignal]
    indexCreationStarted: typing.ClassVar[QtCore.pyqtSignal]
    def isCreatingIndex(self) -> bool: ...
    def filter(self, filter: str, wildcard: str = ...) -> QtCore.QModelIndex: ...
    def createIndex(self, customFilterName: str) -> None: ...  # type: ignore[override]
    def helpEngine(self) -> QHelpEngineCore: ...

class QHelpIndexWidget(QtWidgets.QListView):

    documentsActivated: typing.ClassVar[QtCore.pyqtSignal]
    documentActivated: typing.ClassVar[QtCore.pyqtSignal]
    def activateCurrentItem(self) -> None: ...
    def filterIndices(self, filter: str, wildcard: str = ...) -> None: ...

class QHelpLink(PyQt6.sip.simplewrapper):

    title = ...  # type: str
    url = ...  # type: QtCore.QUrl

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QHelpLink") -> None: ...

class QHelpSearchQuery(PyQt6.sip.simplewrapper):
    class FieldName(enum.Enum):
        DEFAULT = ...  # type: QHelpSearchQuery.FieldName
        FUZZY = ...  # type: QHelpSearchQuery.FieldName
        WITHOUT = ...  # type: QHelpSearchQuery.FieldName
        PHRASE = ...  # type: QHelpSearchQuery.FieldName
        ALL = ...  # type: QHelpSearchQuery.FieldName
        ATLEAST = ...  # type: QHelpSearchQuery.FieldName
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, field: "QHelpSearchQuery.FieldName", wordList: typing.Iterable[str]) -> None: ...
    @typing.overload
    def __init__(self, a0: "QHelpSearchQuery") -> None: ...

class QHelpSearchEngine(QtCore.QObject):
    def __init__(self, helpEngine: QHelpEngineCore, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def search(self, searchInput: str) -> None: ...
    def searchInput(self) -> str: ...
    def searchResults(self, start: int, end: int) -> typing.List["QHelpSearchResult"]: ...
    def searchResultCount(self) -> int: ...
    searchingFinished: typing.ClassVar[QtCore.pyqtSignal]
    searchingStarted: typing.ClassVar[QtCore.pyqtSignal]
    indexingFinished: typing.ClassVar[QtCore.pyqtSignal]
    indexingStarted: typing.ClassVar[QtCore.pyqtSignal]
    def cancelSearching(self) -> None: ...
    def cancelIndexing(self) -> None: ...
    def reindexDocumentation(self) -> None: ...
    def resultWidget(self) -> "QHelpSearchResultWidget": ...
    def queryWidget(self) -> "QHelpSearchQueryWidget": ...

class QHelpSearchResult(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: "QHelpSearchResult") -> None: ...
    @typing.overload
    def __init__(self, url: QtCore.QUrl, title: str, snippet: str) -> None: ...
    def snippet(self) -> str: ...
    def url(self) -> QtCore.QUrl: ...
    def title(self) -> str: ...

class QHelpSearchQueryWidget(QtWidgets.QWidget):
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def setSearchInput(self, searchInput: str) -> None: ...
    def searchInput(self) -> str: ...
    def setCompactMode(self, on: bool) -> None: ...
    def isCompactMode(self) -> bool: ...
    search: typing.ClassVar[QtCore.pyqtSignal]
    def collapseExtendedSearch(self) -> None: ...
    def expandExtendedSearch(self) -> None: ...

class QHelpSearchResultWidget(QtWidgets.QWidget):

    requestShowLink: typing.ClassVar[QtCore.pyqtSignal]
    def linkAt(self, point: QtCore.QPoint) -> QtCore.QUrl: ...
