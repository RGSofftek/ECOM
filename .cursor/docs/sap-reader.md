# SAP Reader

**Keyword:** `SAP`

**Functions:** 92

## Description

With SAP Reader you will be able to automate your SAP Logon’s activities such as capturing multiple data or getting it form your sap transactions, making it easier for you to replicate your business process. Powered by Sapscripting, SAP Reader will help you connect without access to the backend source code, performing the same actions you would do as a user. Try out our recorder and see how easy and fast is to start automating your SAP daily tasks.

## Quick Reference

| Function | Description |
|----------|-------------|
| [ChangeSession](#changesession) | Changes the working session by Id. |
| [ClickButton](#clickbutton) | Clicks a button based on the type and identifier.... |
| [ClickGridButton](#clickgridbutton) | Clicks a button inside a grid cell selecting by row and column of a Grid.... |
| [ClickGridToolBtn](#clickgridtoolbtn) | Click toolbutton of Grid.... |
| [ClickSelectedCell](#clickselectedcell) | Click selected cell of a grid by Id.... |
| [ClickToolBarButton](#clicktoolbarbutton) | Clicks a given button from a toolbar control.... |
| [ClickTreeLink](#clicktreelink) | Clicks a link on a Treeviw of SAP... |
| [CloseSap](#closesap) | Closes a SAP instance.... |
| [CloseTrans](#closetrans) | Closes the current transaction.... |
| [ConditionalClick](#conditionalclick) | Clicks an element when a window appears, repeating action until it appears th... |
| [ConditionalClickSAP](#conditionalclicksap) | Clicks an element when a SAP window appears, repeating action until it appear... |
| [CopyGridCells](#copygridcells) | Copy multiple Grid cells to Clipboard. It can take rows from begin an end (1-... |
| [CopyGridCellsToList](#copygridcellstolist) | Copy multiple Grid cells to Clipboard and saves the resutl as a list of strin... |
| [CopyListValues](#copylistvalues) | Copy multiple list cells to Clipboard. It can take rows from begin an end (1-... |
| [DeselectCheckBox](#deselectcheckbox) | Deselects a CheckBox looking control by Id or text of control.... |
| [DoubleClick](#doubleclick) | Performs double click on an ellement looking for it's Id.... |
| [DoubleClickTreeLink](#doubleclicktreelink) | Performs a double click a node form tree control.... |
| [ElementExists](#elementexists) | Find an element by Id. |
| [ElementFocus](#elementfocus) | Sets the focus to a specific element found by Id... |
| [ExpandNode](#expandnode) | Expands tree node from SAP connection.... |
| [FindText](#findtext) | Finds for a text in the window and saves a variable with the element Id.... |
| [GetAllConnections](#getallconnections) | Gets all sap connections and shows the id's in the log file. |
| [GetAllSAPSessions](#getallsapsessions) | Gets all sap sessions and shows the id's in the log file. |
| [GetAllSAPSessions](#getallsapsessions) | Gets all sap sessions and shows the id's in the log file. |
| [GetAllTreeNodeKeys](#getalltreenodekeys) | Gets all id's from a tree control nodes selecting by tree by id and saves a l... |
| [GetArrayRowNumber](#getarrayrownumber) | Gets the number of rows in an array of controls like labels or text fields.... |
| [GetCheckBoxValue](#getcheckboxvalue) | Gets the value of the given checkbox by Id. |
| [GetElementBefore](#getelementbefore) | Gets the element located before the id stated in the function. |
| [GetElementIcoName](#getelementiconame) | Gets the icon name from an elemet found by Id and saves a variable with the t... |
| [GetElementInfo](#getelementinfo) | Shows information of a given element in a windows popup.... |
| [GetGridRowNumber](#getgridrownumber) | Gets the number of rows in a Grid by the GridId.... |
| [GetGridTitle](#getgridtitle) | Gets the title shown in a Grid. |
| [GetHTMLViewerText](#gethtmlviewertext) | Set the focus to a specific element. |
| [GetMaxArrayValueByPos](#getmaxarrayvaluebypos) | Gets the maximun leng of array elements in a line. |
| [GetMaxVerticalScroll](#getmaxverticalscroll) | Gets the maximun numer of scroll clicks of a table, list or user area and sav... |
| [GetRadioButtonValue](#getradiobuttonvalue) | Gets the value of the given radio button by Id. |
| [GetStatusInfo](#getstatusinfo) | Gets the status iformation such as the message, message Id etc. Teh result is... |
| [GetTableRowNumber](#gettablerownumber) | Get the number of rows in a table. |
| [GetTreeItemText](#gettreeitemtext) | Gets the text from an item of a Tree by tree id, item Key and name of column.... |
| [GetTreeNodeText](#gettreenodetext) | Gets text from tree node finding by TreeId and node key and saving text in a ... |
| [GetVisibleGridRowNumber](#getvisiblegridrownumber) | Gets the number of visible rows in a Grid. |
| [GridCellDoubleClick](#gridcelldoubleclick) | Performs a double click on a cell of a grid by Id.... |
| [MakeGridRowVisible](#makegridrowvisible) | Makes visible a row from the Grid looking for row number.... |
| [ManageWinCtl](#managewinctl) | Manages windows pop ups to save or find files. This is a listener beacuse SAP... |
| [ManageWinCtl2](#managewinctl2) | Manages windows pop ups to save or find files. |
| [ManageWinCtl3](#managewinctl3) | Manages windows pop ups to save or find files. |
| [ModifyGridCell](#modifygridcell) | Changes a cell value value of a grid control.... |
| [OpenSap](#opensap) | Opens a SAP instance's LogIn page. This function don't log in the server... |
| [PressGridContextButton](#pressgridcontextbutton) | Clicks a given context button from a grid control.... |
| [PressToolControlContextButton](#presstoolcontrolcontextbutton) | Clicks a given context button from a toolbar control. |
| [ReadElement](#readelement) | Gets the text from an elemet found by Id and saves a variable with the text.... |
| [ReadGridCell](#readgridcell) | Gets the text from a cell in a grid found by GridId, column name and Row. Sav... |
| [ReadStatus](#readstatus) | Gets the status from status bar and saves a variable with the message.... |
| [RunSapInstance](#runsapinstance) | Runs a SAP instance and opens a new SAP conneciton to desired server.... |
| [ScrollToCol](#scrolltocol) | Move the grid's scroll to make a desired column visible. Finds the grid and c... |
| [SelectAllGridCols](#selectallgridcols) | Selects all columns from a given Grid. Finds the grid by Id.... |
| [SelectCheckBox](#selectcheckbox) | Selects a CheckBox looking control by Id or text of control.... |
| [SelectComboBox](#selectcombobox) | Selects a ComboBox option looking control by Id or text of control and select... |
| [SelectComboBox](#selectcombobox) | Selects a ComboBox option looking control by Id or text of control and select... |
| [SelectComboBox](#selectcombobox) | Selects a ComboBox option looking control by Id or text of control and select... |
| [SelectContextMenu](#selectcontextmenu) | Selects context menu of a given grid. Grid and Context menu are selected by I... |
| [SelectElementCM](#selectelementcm) | Selects context menu of a given element. Element and Context menu are selecte... |
| [SelectGridCell](#selectgridcell) | Selects a cell from the Grid looking for row and column.... |
| [SelectGridCellTrigger](#selectgridcelltrigger) | Selects a cell from the Grid looking for row and column and triggers SAP acti... |
| [SelectGridChk](#selectgridchk) | Selects CheckBox control in a given row and column of a Grid... |
| [SelectGridChkTrigger](#selectgridchktrigger) | Selects CheckBox control in a given row and column of a Grid and triggers SAP... |
| [SelectGridCol](#selectgridcol) | Selects a Grid column looking control by Id of control and selects the given ... |
| [SelectGridLabel](#selectgridlabel) | Selects label text of a text grid.... |
| [SelectGridRow](#selectgridrow) | Selects entire row from the Grid looking for row number.... |
| [SelectListItem](#selectlistitem) | Selects a list vew item.... |
| [SelectMenu](#selectmenu) | Selects menu option from SAP menu.... |
| [SelectRb](#selectrb) | Selects a RadioButton looking control by Id or text of control.... |
| [SelecTreeNode](#selectreenode) | Selects tree node finding for node key.... |
| [SelectShellItem](#selectshellitem) | Selects an element from a Shell a listview of menu for example.... |
| [SelectTab](#selecttab) | Selects a Tab looking control by Id or text of control.... |
| [SelectTableColumn](#selecttablecolumn) | Selects entire column of a table control selecting by column id.... |
| [SelectTableRow](#selecttablerow) | Selects entire row from the table looking for Id.... |
| [SelectTreeItem](#selecttreeitem) | Selects tree item from a tree node by tree id, node and item ... |
| [SendKey](#sendkey) | Sends the desired key from Keyboard.... |
| [SetCurrentCellColumn](#setcurrentcellcolumn) | Sets the column to select a cell using it.... |
| [SetSAPParameters](#setsapparameters) | Sets all required parameters to manage SAP connection and Actions.... |
| [ShowAllSAPSessions](#showallsapsessions) | Gets all sap sessions and shows the id's in the log file. |
| [ShowElements](#showelements) | Saves a file with all elements of the current page.... |
| [StartTransaction](#starttransaction) | Starts a SAP transaction.... |
| [TakeScreenShot](#takescreenshot) | Takes a screenshot of current page and save it in the given path.... |
| [TreeItemContextMenu](#treeitemcontextmenu) | Makes context menu of a tree Item accesible to select option.... |
| [TriggerModifiedCell](#triggermodifiedcell) | Triggers the the modified value in a Grid.... |
| [VerticalScroll](#verticalscroll) | Moves the list on or more positions down.... |
| [Wait](#wait) | Waits for an element to appear in the window or for a specific amount of time... |
| [Write](#write) | Writes a text in a TextBox looking control by Id and anchor (reference contro... |
| [WriteGridCell](#writegridcell) | Writes a value in a given gridcell.... |
| [WriteText](#writetext) | Writes a text in any element looking control by Id.... |

---

## Functions

### ChangeSession

> Changes the working session by Id.

Changes the session to a different one triggered by a button, menu or another event in a main session.

**Parameters:**
- `SessionId`

**Syntax:**

```
ChangeSession SessionId <SessionId>
```

**Examples:**

```
ChangeSession SessionId /app/con[0]/ses[1]
```

*Added: 2021-May-11*

---

### ClickButton

Clicks a button based on the type and identifier.

**Parameters:**
- `Type`
- `Identifier`

**Syntax:**

```
ClickButton <Type> <Identifier>
```

**Examples:**

```
ClickButton id btn[0]
ClickButton te Continue
ClickButton tt "Continue   (f8)"
```

*Added: 2018-Apr-06*

---

### ClickGridButton

Clicks a button inside a grid cell selecting by row and column of a Grid.

**Parameters:**
- `GridId`
- `Row`
- `ColumnName`
- `Value`

**Syntax:**

```
SAP ClickGridButton GridId <GridId> RowN <Row>
SAP ClickGridButton GridId <GridId> RowN <Row> Column "<ColumnName>"
```

**Examples:**

```
SAP ClickGridButton GridId /app/con[0]/ses[0]/wnd[0]/usr/cntlGO_CONT_D0100/shellcont/shell RowN 0 Column "CHECK"
SAP ClickGridButton GridId /app/con[0]/ses[0]/wnd[0]/usr/cntlGO_CONT_D0100/shellcont/shell RowN 0 Column "CHECK"
```

*Added: 2020-Jul-31*

---

### ClickGridToolBtn

Click toolbutton of Grid.

**Parameters:**
- `GridId`
- `ButtonId`

**Syntax:**

```
ClickGridToolBtn GridId <GridId> ButtonId <ButtonId>
```

**Examples:**

```
ClickGridToolBtn GridId wnd[0]/usr/cntlALV/shellcont/shell ButtonId Btn[1]
```

*Added: 2020-Jul-31*

---

### ClickSelectedCell

Click selected cell of a grid by Id.

**Parameters:**
- `GridId`

**Syntax:**

```
ClickSelectedCell GridId <GridId>
```

**Examples:**

```
ClickSelectedCell GridId wnd[0]/usr/cntlALV/shellcont/shell
```

*Added: 2018-Oct-18*

---

### ClickToolBarButton

Clicks a given button from a toolbar control.

**Parameters:**
- `ToolBarId`
- `ButtonId`

**Syntax:**

```
ClickToolBarButton ToolBarId <ToolBarId> ButtonId <ButtonId>
```

**Examples:**

```
ClickToolBarButton ToolBarId ToolBarId[1] ButtonId "SAVE_AS"
```

*Added: 2020-Aug-31*

---

### ClickTreeLink

Clicks a link on a Treeviw of SAP

**Parameters:**
- `TreeId`
- `Node`
- `ItemName`

**Syntax:**

```
ClickTreeLink TreeId "<TreeId>" Node "<NodeKey>" Item "<ItemName>"
```

**Examples:**

```
ClickTreeLink TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "02*1*2" Item "1"
ClickTreeLink TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "*****2" Item "1"
```

*Added: 2019-Oct-28*

---

### CloseSap

Closes a SAP instance.

**Syntax:**

```
CloseSap
```

**Examples:**

```
CloseSap
```

*Added: 2018-Jun-27*

---

### CloseTrans

Closes the current transaction.

**Syntax:**

```
CloseTrans
```

**Examples:**

```
CloseTrans
```

*Added: 2018-May-02*

---

### ConditionalClick

Clicks an element when a window appears, repeating action until it appears the number of times stated.

**Parameters:**
- `Window`
- `ButtonId`
- `RepeatTime`

**Syntax:**

```
ConditionalClick if window "<Window>" click on Button \"<ButtonId>" repeat <RepeatTime>
```

**Examples:**

```
ConditionalClick if window "Window[0]" click on Button \"Button[2]" repeat 5
```

---

### ConditionalClickSAP

Clicks an element when a SAP window appears, repeating action until it appears the number of times stated.

**Parameters:**
- `Window`
- `ButtonId`
- `RepeatTime`

**Syntax:**

```
ConditionalClickSAP if window "<Window>" click on Button \"<ButtonId>" repeat <RepeatTime>
```

**Examples:**

```
ConditionalClickSAP if window "Window[0]" click on Button \"Button[2]" repeat 5
```

*Added: 2019-Jun-24*

---

### CopyGridCells

Copy multiple Grid cells to Clipboard. It can take rows from begin an end (1-7) or copy a list of specific rows (1,5,7)

**Parameters:**
- `GridId`
- `RowsRange`
- `Column`
- `VarName`

**Syntax:**

```
CopyGridCells GridId <GridId> Rows "<RowsRange>" Column <Column>
CopyGridCells GridId <GridId> Rows "<RowsRange>" Column <Column> as <VarName>
```

**Examples:**

```
CopyGridCells GridId GridId[1] Rows "1-7" Column NAME
CopyGridCells GridId GridId[1] Rows "1, 5, 7" Column NAME
CopyGridCells GridId GridId[1] Rows "1-7" Column NAME as List
```

*Added: 2019-Jan-29*

---

### CopyGridCellsToList

Copy multiple Grid cells to Clipboard and saves the resutl as a list of strings. It can take rows from begin an end (1-7) or copy a list of specific rows (1,5,7)

**Parameters:**
- `GridId`
- `RowsRange`
- `Column`
- `ListName`

**Syntax:**

```
CopyGridCellsToList GridId <GridId> Rows "<RowsRange>" Column <Column> as <ListName>
```

**Examples:**

```
CopyGridCellsToList GridId GridId[1] Rows "1-7" Column NAME As ListResults
```

*Added: 2019-Jun-07*

---

### CopyListValues

Copy multiple list cells to Clipboard. It can take rows from begin an end (1-7) or copy a list of specific rows (1,5,7)

**Parameters:**
- `Rows`
- `ColummName`

**Syntax:**

```
CopyListValues Rows "<Rows>" Column "<ColummName>"
```

**Examples:**

```
CopyListValues Rows "16-20" Column "Nombre"
```

*Added: 2019-Feb-04*

---

### DeselectCheckBox

Deselects a CheckBox looking control by Id or text of control.

**Parameters:**
- `Type`
- `Identifyer`

**Syntax:**

```
DeselectCheckBox <Type> <Identifyer>
```

**Examples:**

```
DeselectCheckBox id chkbox[1]
DeselectCheckBox te "unchek this box."
```

*Added: 2018-Apr-06*

---

### DoubleClick

Performs double click on an ellement looking for it's Id.

**Parameters:**
- `ElementId`

**Syntax:**

```
DoubleClick ElementId <ElementId>
```

**Examples:**

```
DoubleClick ElementId wnd[0]/sbar
```

*Added: 2019-Jun-07*

---

### DoubleClickTreeLink

Performs a double click a node form tree control.

**Parameters:**
- `TreeId`
- `Node`

**Syntax:**

```
DoubleClickTreeLink TreeId <TreeId> Node "<Node>"
```

**Examples:**

```
DoubleClickTreeLink TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "02*1*2"
DoubleClickTreeLink TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "*****2"
```

*Added: 2019-Nov-06*

---

### ElementExists

> Find an element by Id.

Returs true or false if the elemento given by Id exists or not.

**Parameters:**
- `ElementId`
- `Variable`

**Syntax:**

```
ElementExists ElementId <ElementId> as <Variable>
```

**Examples:**

```
ElementExists ElementId wnd[0]/usr/cntlALV/shellcont/lblId as Result.
```

*Added: 2021-Jun-03*

---

### ElementFocus

Sets the focus to a specific element found by Id

**Parameters:**
- `ElementId`

**Syntax:**

```
SAP ElementFocus ElementId <ElementId>
```

**Examples:**

```
SAP ElementFocus ElementId wnd[0]/tbar[1]/btn[8]
```

*Added: 2019-Jan-29*

---

### ExpandNode

Expands tree node from SAP connection.

**Parameters:**
- `TreeId`
- `Node`

**Syntax:**

```
ExpandNode TreeId "<TreeId>" Node "<Node>"
```

**Examples:**

```
ExpandNode TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "02*1*2"
ExpandNode TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "*******2"
```

*Added: 2019-Oct-28*

---

### FindText

Finds for a text in the window and saves a variable with the element Id.

**Parameters:**
- `text`
- `VarName`

**Syntax:**

```
FindText <"text"> as <VarName>
```

**Examples:**

```
FindText "Error" as ElementId
```

*Added: 2018-Sep-12*

---

### GetAllConnections

> Gets all sap connections and shows the id's in the log file.

Gets all sap connections and shows the id's in the log file.

**Syntax:**

```
GetAllConnections as <List>
```

**Examples:**

```
GetAllConnections as SessionList
```

*Added: 2022-Jun-06*

---

### GetAllSAPSessions

> Gets all sap sessions and shows the id's in the log file.

Gets all sap sessions and shows the id's in the log file.

**Syntax:**

```
GetAllSAPSessions as <List>
```

**Examples:**

```
GetAllSAPSessions as SessionList
```

*Added: 2021-May-11*

---

### GetAllSAPSessions

> Gets all sap sessions and shows the id's in the log file.

Gets all sap sessions and shows the id's in the log file.

**Syntax:**

```
GetAllSAPSessions as <List>
```

**Examples:**

```
GetAllSAPSessions as SessionList
```

*Added: 2021-May-11*

---

### GetAllTreeNodeKeys

Gets all id's from a tree control nodes selecting by tree by id and saves a list of nodes..

**Parameters:**
- `TreeId`
- `Variable`

**Syntax:**

```
SAP GetAllTreeNodeKeys TreeId <TreeId> as "<Variable>"
```

**Examples:**

```
SAP GetAllTreeNodeKeys TreeId wnd[0]/shellcont/shell/shellcont[2]/shell as "ListaNodos"
```

*Added: 2023-Jun-02*

---

### GetArrayRowNumber

Gets the number of rows in an array of controls like labels or text fields.

**Parameters:**
- `LabelId`
- `Variable`

**Syntax:**

```
GetArrayRowNumber LabelId <LabelId> as <Variable>
```

**Examples:**

```
GetArrayRowNumber LabelId wnd[0]/usr/cntlALV/shellcont/lblId as Rows
```

*Added: 2019-Apr-05*

---

### GetCheckBoxValue

> Gets the value of the given checkbox by Id.

Gets the value of the given checkbox by Id.

**Parameters:**
- `CheckBoxId`
- `Value`

**Syntax:**

```
GetCheckBoxValue CheckBoxId <CheckBoxId> as <Value>
```

**Examples:**

```
GetCheckBoxValue CheckBoxId chkbox[1] as Var
```

*Added: 2021-Apr-06*

---

### GetElementBefore

> Gets the element located before the id stated in the function.

Gets the element located before the id stated in the function.

**Parameters:**
- `ElementId`
- `Variable`

**Syntax:**

```
GetElementBefore ElementId <ElementId> as <Variable>
```

**Examples:**

```
GetElementBefore ElementId wnd[0]/sbar as LastElement
```

*Added: 2021-Jun-03*

---

### GetElementIcoName

Gets the icon name from an elemet found by Id and saves a variable with the text.

**Parameters:**
- `ElementId`
- `VarName`

**Syntax:**

```
GetElementIcoName <ElementId> as <VarName>
```

**Examples:**

```
GetElementIcoName ElementId as VarName
```

*Added: 2020-Aug-07*

---

### GetElementInfo

Shows information of a given element in a windows popup.

**Parameters:**
- `ElementId`

**Syntax:**

```
GetElementInfo Id "<ElementId>"
```

**Examples:**

```
GetElementInfo Id "IdElement[1]"
```

*Added: 2019-Jul-09*

---

### GetGridRowNumber

Gets the number of rows in a Grid by the GridId.

**Parameters:**
- `GridId`
- `Variable`

**Syntax:**

```
GetGridRowNumber GridId <GridId> as <Variable>
```

**Examples:**

```
GetGridRowNumber GridId wnd[0]/usr/cntlALV/shellcont/shell as Rows
```

*Added: 2018-Oct-18*

---

### GetGridTitle

> Gets the title shown in a Grid.

Gets the title shown in a Grid and saves iur in the given variable.

**Parameters:**
- `GridId`
- `Variable`

**Syntax:**

```
GetGridTitle GridId <GridId> as <Variable>
```

**Examples:**

```
GetGridTitle GridId wnd[0]/usr/cntlALV/shellcont/shell as VarTitle
```

*Added: 2020-Dec-09*

---

### GetHTMLViewerText

> Set the focus to a specific element.

Sets the focus to a specific element found by Id.

**Parameters:**
- `HTMLViewerId`
- `OutputType`
- `Variable`
- `ElementId`
- `Variable`

**Syntax:**

```
GetHTMLViewerText HTMLViewerId <HTMLViewerId> output <OutputType> as <Variable>
IsElementEnabled ElementId <ElementId> as <Variable>
```

**Examples:**

```
GetTableRowNumber HTMLViewerId wnd[0]/usr/cntlALV/shellcont/lblId as Rows
IsElementEnabled ElementId wnd[0]/tbar[1]/btn[8] as VarEnabled
```

*Added: 2020-Nov-19*

---

### GetMaxArrayValueByPos

> Gets the maximun leng of array elements in a line.

Gets the maximun leng of array elements in a line.

**Parameters:**
- `LabelId`
- `Position`
- `Compare`
- `Variable`

**Syntax:**

```
GetMaxArrayValueByPos LabelId <LabelId> Position <Position> Compare <Compare> as <Variable>
```

**Examples:**

```
SAP GetMaxArrayValueByPos LabelId wnd[0]/usr/lbl Position 0 Compare 30 as LastHijo
```

*Added: 2021-Jun-03*

---

### GetMaxVerticalScroll

> Gets the maximun numer of scroll clicks of a table, list or user area and saves it in the given variable.

Gets the maximun numer of scroll clicks of a table, list or user area and saves it in the given variable.

**Parameters:**
- `GridId`
- `Position`
- `Variable`

**Syntax:**

```
GetMaxVerticalScroll GridId <GridId> as <Variable>
```

**Examples:**

```
GetMaxVerticalScroll GridId wnd[0]/usr/cntlALV/shellcont/shell as ScrollNum
```

*Added: 2021-Jan-12*

---

### GetRadioButtonValue

> Gets the value of the given radio button by Id.

Gets the value of the given radio button by Id.

**Parameters:**
- `RadioButtonId`
- `Value`

**Syntax:**

```
GetRadioButtonValue RadioButtonId <RadioButtonId> as <Value>
```

**Examples:**

```
GetRadioButtonValue RadioButtonId radiobutton[1] as Var
```

---

### GetStatusInfo

Gets the status iformation such as the message, message Id etc. Teh result is a list with the status info. 0 - StatusMessage; 1 - MessageId/MessageNumber; 2 - MessageType

**Parameters:**
- `VarName`

**Syntax:**

```
GetStatusInfo as <VarName>
```

**Examples:**

```
GetStatusInfo as StatInfo
```

*Added: 2019-Jul-10*

---

### GetTableRowNumber

> Get the number of rows in a table.

Gets the number of rows in an Table that can contains labels or another type of controls.

**Parameters:**
- `TableId`
- `Variable`

**Syntax:**

```
GetTableRowNumber TableId <TableId> as <Variable>
```

**Examples:**

```
GetTableRowNumber TableId wnd[0]/usr/cntlALV/shellcont/lblId as Rows
```

*Added: 2020-Nov-19*

---

### GetTreeItemText

Gets the text from an item of a Tree by tree id, item Key and name of column. Saves the result in a given variable.

**Parameters:**
- `TreeId`
- `ItemKey`
- `ColName`
- `Variable`

**Syntax:**

```
GetTreeItemText <TreeId> Key "<ItemKey>" Name "<ColName>" as <Variable>
```

**Examples:**

```
GetTreeItemText TreeId[0] Key "FAX" Name "Waiting" as Value
```

*Added: 2020-Mar-12*

---

### GetTreeNodeText

Gets text from tree node finding by TreeId and node key and saving text in a given variable.

**Parameters:**
- `TreeId`
- `NodeKey`
- `Text`

**Syntax:**

```
GetTreeNodeText TreeId <TreeId> Node "<NodeKey>" as "<Text>"
```

**Examples:**

```
GetTreeNodeText TreeId wnd[0]/shellcont/shell/shellcont[2]/shell Node "<<<Nodo>>>" as "NodeTitle"
```

*Added: 2023-Jun-02*

---

### GetVisibleGridRowNumber

> Gets the number of visible rows in a Grid.

Gets the number of visible rows in a Grid by the GridId.

**Parameters:**
- `GridId`
- `Variable`

**Syntax:**

```
GetVisibleGridRowNumber GridId <GridId> as <Variable>
```

**Examples:**

```
GetVisibleGridRowNumber GridId wnd[0]/usr/cntlALV/shellcont/shell as Rows
```

*Added: 2021-Jan-12*

---

### GridCellDoubleClick

Performs a double click on a cell of a grid by Id.

**Parameters:**
- `GridId`
- `ColumnId`
- `RowNumber`

**Syntax:**

```
GridCellDoubleClick GridId <GridId> Row <RowNumber> Column <ColumnId>
```

**Examples:**

```
GridCellDoubleClick GridId wnd[0]/usr/cntlALV/shellcont/shell Row 1 Column HKONT
```

*Added: 2019-Mar-05*

---

### MakeGridRowVisible

Makes visible a row from the Grid looking for row number.

**Parameters:**
- `GridId`
- `Row`

**Syntax:**

```
MakeGridRowVisible GridId <GridId> RowN <Row>
```

**Examples:**

```
MakeGridRowVisible GridId wnd[0]/usr/cntlALV/shellcont/shell RowN 0
```

*Added: 2020-Jan-02*

---

### ManageWinCtl

Manages windows pop ups to save or find files. This is a listener beacuse SAP waits untile the popup is closed to continue it means that ManageWinCtl has to be placed before the instruction that triggers the pop up.

**Parameters:**
- `WindowTitle`
- `Script`

**Syntax:**

```
ManageWinCtl Window <WindowTitle> Script "<Script>"
```

**Examples:**

```
ManageWinCtl Window <Confirm Save> Script "Send {ENTER}"
```

*Added: 2019-Apr-18*

---

### ManageWinCtl2

> Manages windows pop ups to save or find files.

Manages windows pop ups to save or find files. This is a listener beacuse SAP waits untile the popup is closed to continue it means that ManageWinCtl has to be placed before the instruction that triggers the pop up.

**Parameters:**
- `WindowTitle`
- `Script`
- `TimeOut`
- `Retry`

**Syntax:**

```
ManageWinCtl2 Script "<Script>"
ManageWinCtl2 Script "<Script>" TimeOut <TimeOut> Retry <Retry>
```

**Examples:**

```
ManageWinCtl2 Window Confirm Save Script "Send {ENTER}"
```

---

### ManageWinCtl3

> Manages windows pop ups to save or find files.

Manages windows pop ups to save or find files. This function is used without SAP application for any other popup in any other application.

**Parameters:**
- `WindowTitle`
- `Script`
- `TimeOut`
- `Retry`

**Syntax:**

```
ManageWinCtl3 Script "<Script>"
ManageWinCtl3 Script "<Script>" TimeOut <TimeOut> Retry <Retry>
```

**Examples:**

```
ManageWinCtl3 Window Confirm Save Script "Send {ENTER}"
```

---

### ModifyGridCell

Changes a cell value value of a grid control.

**Parameters:**
- `GridId`
- `RowNum`
- `ColumnId`
- `Value`

**Syntax:**

```
ModifyGridCell GridId <GridId> RowNum <RowNum> ColumnId "<ColumnId>" Value "<Value>"
```

**Examples:**

```
SAP ModifyGridCell GridId wnd[0]/usr/shell RowNum 0 ColumnId "VALUE1" Value "Mensaje"
```

*Added: 2022-May-09*

---

### OpenSap

Opens a SAP instance's LogIn page. This function don't log in the server

**Parameters:**
- `SapServer`

**Syntax:**

```
OpenSap "<SapServer>"
```

**Examples:**

```
OpenSap "CC DEV"
```

*Added: 2018-Apr-06*

---

### PressGridContextButton

Clicks a given context button from a grid control.

**Parameters:**
- `GridId`
- `ButtonId`

**Syntax:**

```
ClickToolBarButton GridId <GridId> ButtonId <ButtonId>
```

**Examples:**

```
ClickToolBarButton ToolBarId GridId[1] ButtonId "SAVE_AS"
```

*Added: 2020-Sep-25*

---

### PressToolControlContextButton

> Clicks a given context button from a toolbar control.

Clicks a given context button from a toolbar control.

**Parameters:**
- `ToolCtlId`
- `ButtonId`

**Syntax:**

```
PressToolControlContextButton ToolControlId <ToolCtlId> ButtonId "<ButtonId>"
```

**Examples:**

```
PressToolControlContextButton ToolControlId ToolCtlId[1] ButtonId "CREATE_ATTA"
```

*Added: 2021-May-11*

---

### ReadElement

Gets the text from an elemet found by Id and saves a variable with the text.

**Parameters:**
- `ElementId`
- `VarName`
- `format`

**Syntax:**

```
ReadElement <ElementId> as <VarName>
ReadElement <ElementId> with format "<format>" as <VarName>
```

**Examples:**

```
ReadElement ElementId as VarName
ReadElement ElementId with format "Take only .+?" as VarName
```

*Added: 2018-Oct-10*

---

### ReadGridCell

Gets the text from a cell in a grid found by GridId, column name and Row. Saves the result in a given variable.

**Parameters:**
- `GridId`
- `ColumnName`
- `RowNumber`
- `Variable`

**Syntax:**

```
ReadGridCell <GridId> Column <ColumnName> Row <RowNumber> as <Variable>
```

**Examples:**

```
ReadGridCell GRIDID[0] Column DOCNUM Row 10 as Value
```

*Added: 2018-Oct-12*

---

### ReadStatus

Gets the status from status bar and saves a variable with the message.

**Parameters:**
- `format`
- `varName`

**Syntax:**

```
ReadStatus as <varName>
ReadStatus with format "<format>" as <varName>
```

**Examples:**

```
ReadStatus as StatusMessage
ReadStatus as StatusMessage
```

*Added: 2018-Sep-12*

---

### RunSapInstance

Runs a SAP instance and opens a new SAP conneciton to desired server.

**Parameters:**
- `SapServer`
- `Mand`
- `SapUser`
- `SapPassword`
- `Lang`
- `Instance`
- `Type`
- `HideMessage`

**Syntax:**

```
RunSapInstance "<SapServer>" <Mand> <SapUser> <SapPassword> <Lang> <Instance Type> <HideMessage>
```

**Examples:**

```
RunSapInstance "CC DEV" 010 <<SapUsr>> <<SAPPwd>> ES
RunSapInstance "CC DEV" 010 <<SapUsr>> <<SAPPwd>> ES HideMessage
RunSapInstance "CC DEV" 010 <<SapUsr>> <<SAPPwd>> ES graphic
```

*Added: 2018-Apr-06*

---

### ScrollToCol

Move the grid's scroll to make a desired column visible. Finds the grid and column by Id.

**Parameters:**
- `Type`
- `Identifier`
- `ColumnId`

**Syntax:**

```
ScrollToCol <Type> <Identifier> <ColumnId>
```

**Examples:**

```
ScrollToCol id grid[1] "VSTEL"
```

*Added: 2018-May-02*

---

### SelectAllGridCols

Selects all columns from a given Grid. Finds the grid by Id.

**Parameters:**
- `Type`
- `Identifier`

**Syntax:**

```
SelectAllGridCols <Type> <Identifier>
```

**Examples:**

```
SelectAllGridCols id grid[1]
```

*Added: 2018-May-02*

---

### SelectCheckBox

Selects a CheckBox looking control by Id or text of control.

**Parameters:**
- `Type`
- `Identifyer`

**Syntax:**

```
SelectCheckBox <Type> <Identifyer>
```

**Examples:**

```
SelectCheckBox id chkbox[1]
SelectCheckBox te "Chek this box."
```

*Added: 2018-Apr-06*

---

### SelectComboBox

Selects a ComboBox option looking control by Id or text of control and selecting the desired item.

**Parameters:**
- `Type`
- `Identifyer`
- `Option`
- `Pos`

**Syntax:**

```
SelectComboBox <Type> <Identifyer> <Option>
SelectComboBox <Type> <Identifyer> <Option> <Pos>
```

**Examples:**

```
SelectComboBox id cmb[1] "1"
SelectComboBox an "Select combo." "1" 1
```

*Added: 2018-May-02*

---

### SelectComboBox

Selects a ComboBox option looking control by Id or text of control and selecting the desired item.

**Parameters:**
- `Type`
- `Identifyer`
- `Option`
- `Pos`

**Syntax:**

```
SelectComboBox2 ComboBoxId <ComboBoxId> Option "<Option>"
```

**Examples:**

```
SelectComboBox id cmb[1] "1"
SelectComboBox an "Select combo." "1" 1
```

*Added: 2018-May-02*

---

### SelectComboBox

Selects a ComboBox option looking control by Id or text of control and selecting the desired item.

**Parameters:**
- `Type`
- `Identifyer`
- `Option`
- `Pos`

**Syntax:**

```
SelectComboBox2 ComboBoxId <ComboBoxId> Option "<Option>"
```

**Examples:**

```
SelectComboBox id cmb[1] "1"
SelectComboBox an "Select combo." "1" 1
```

*Added: 2018-May-02*

---

### SelectContextMenu

Selects context menu of a given grid. Grid and Context menu are selected by Id.

**Parameters:**
- `Type`
- `Identifier`
- `ctxMenu`

**Syntax:**

```
SelectContextMenu <Type> <Identifier> <ctxMenu>
```

**Examples:**

```
SelectContextMenu id grid[1] &XXL
```

*Added: 2018-May-02*

---

### SelectElementCM

Selects context menu of a given element. Element and Context menu are selected by Id.

**Parameters:**
- `ElementId`
- `CmId`

**Syntax:**

```
SelectElementCM ElementId <ElementId> CmId <CmId>
```

**Examples:**

```
SelectElementCM ElementId Element[1] CmId &XXL
```

*Added: 2020-Jan-24*

---

### SelectGridCell

Selects a cell from the Grid looking for row and column.

**Parameters:**
- `GridId`
- `Row`
- `Column`

**Syntax:**

```
SelectGridCell GridId <GridId> Row <Row> Column <Column>
```

**Examples:**

```
SelectGridCell GridId wnd[0]/usr/cntlALV/shellcont/shell Row 0 Column CHAIN
```

*Added: 2018-Oct-18*

---

### SelectGridCellTrigger

Selects a cell from the Grid looking for row and column and triggers SAP action.

**Parameters:**
- `GridId`
- `Row`
- `Column`

**Syntax:**

```
SelectGridCellTrigger GridId <GridId> Row <Row> Column <Column>
```

**Examples:**

```
SelectGridCellTrigger GridId wnd[0]/usr/cntlALV/shellcont/shell Row 0 Column CHAIN
```

*Added: 2019-Nov-06*

---

### SelectGridChk

Selects CheckBox control in a given row and column of a Grid

**Parameters:**
- `GridId`
- `Row`
- `ColumnName`
- `Value`

**Syntax:**

```
SAP SelectGridChk GridId <GridId> RowN <Row> Column <"ColumnName"> Value <Value>
```

**Examples:**

```
SAP SelectGridChk GridId /app/con[0]/ses[0]/wnd[0]/usr/cntlGO_CONT_D0100/shellcont/shell RowN 0 Column "CHECK" Value false
```

*Added: 2018-Dec-26*

---

### SelectGridChkTrigger

Selects CheckBox control in a given row and column of a Grid and triggers SAP action linked tot the selection event.

**Parameters:**
- `GridId`
- `Row`
- `ColumnName`
- `Value`

**Syntax:**

```
SAP SelectGridChkTrigger GridId <GridId> RowN <Row> Column "<ColumnName>" Value <Value>
```

**Examples:**

```
SAP SelectGridChkTrigger GridId wnd[0]/usr/cntlGO_CONT_D0100/shellcont/shell RowN 0 Column "CHECK" Value false
```

*Added: 2019-Aug-26*

---

### SelectGridCol

Selects a Grid column looking control by Id of control and selects the given column by Id.

**Parameters:**
- `Type`
- `Identifier`
- `ColumnId`

**Syntax:**

```
SelectGridCol <Type> <Identifier> <ColumnId>
```

**Examples:**

```
SelectGridCol id grid[1] "NAME1"
```

*Added: 2018-May-02*

---

### SelectGridLabel

Selects label text of a text grid.

**Parameters:**
- `Type`
- `Identifier`

**Syntax:**

```
SelectGridLabel <Type> <Identifier>
```

**Examples:**

```
SelectGridLabel id TitleLabelId(1)
SelectGridLabel te "Title label 1"
```

*Added: 2018-May-02*

---

### SelectGridRow

Selects entire row from the Grid looking for row number.

**Parameters:**
- `GridId`
- `Row`

**Syntax:**

```
SelectGridRow GridId <GridId> RowN <Row>
```

**Examples:**

```
SelectGridRow GridId wnd[0]/usr/cntlALV/shellcont/shell RowN 0
SelectGridRow GridId wnd[0]/usr/cntlALV/shellcont/shell RowN 0,2,8,10
SelectGridRow GridId wnd[0]/usr/cntlALV/shellcont/shell RowN 0-10
```

*Added: 2018-Dec-18*

---

### SelectListItem

Selects a list vew item.

**Parameters:**
- `Type`
- `Identifier`

**Syntax:**

```
SelectListItem <Type> <Identifier>
```

**Examples:**

```
SelectListItem id ListItemId[1]
SelectListItem te "Item 1"
```

*Added: 2018-May-02*

---

### SelectMenu

Selects menu option from SAP menu.

**Parameters:**
- `Type`
- `Identifier`

**Syntax:**

```
SelectMenu <Type> <Identifier>
```

**Examples:**

```
SelectMenu id menu[1,1]
SelectMenu te "Export to excel"
SelectMenu tt "Excel (Alt+f8)"
```

*Added: 2018-May-02*

---

### SelectRb

Selects a RadioButton looking control by Id or text of control.

**Parameters:**
- `Type`
- `Identifyer`

**Syntax:**

```
SelectRb <Type> <Identifyer>
```

**Examples:**

```
SelectRb id radiobt[1]
SelectRb te "Option 1."
```

*Added: 2018-Apr-06*

---

### SelecTreeNode

Selects tree node finding for node key.

**Parameters:**
- `TreeId`
- `NodeKey`

**Syntax:**

```
SelecTreeNode TreeId <TreeId> Node "<NodeKey>"
```

**Examples:**

```
SAP SelectTableColumn TableId wnd[2]/tblSAPLALDBSINGLE ColumnId 1 Selected "true"
```

*Added: 2023-Jun-02*

---

### SelectShellItem

Selects an element from a Shell a listview of menu for example.

**Parameters:**
- `shellId`
- `Row`

**Syntax:**

```
SelectShellItem Id <shellId> Row <Row>
```

**Examples:**

```
SelectShellItem Id wnd[0]/usr/cntlALV/shellcont/shell Row 12
```

*Added: 2018-Oct-18*

---

### SelectTab

Selects a Tab looking control by Id or text of control.

**Parameters:**
- `Type`
- `Identifyer`

**Syntax:**

```
SelectTab <Type> <Identifyer>
```

**Examples:**

```
SelectTab id Tab[1]
SelectTab te "Tab 1."
```

*Added: 2018-May-02*

---

### SelectTableColumn

Selects entire column of a table control selecting by column id.

**Parameters:**
- `TableId`
- `ColumnId`
- `Selected`

**Syntax:**

```
SelectTableColumn TableId <TableId> ColumnId <ColumnId> Selected "<Selected>"
```

**Examples:**

```
SAP SelectTableColumn TableId wnd[2]/tblSAPLALDBSINGLE ColumnId 1 Selected "true"
```

*Added: 2022-Nov-10*

---

### SelectTableRow

Selects entire row from the table looking for Id.

**Parameters:**
- `GridId`
- `RowN`

**Syntax:**

```
SelectTableRow  TableId <GridId> RowN <RowN>
```

**Examples:**

```
SelectTableRow  TableId wnd[0]/usr/cntlALV/shellcont/shell RowN 0
```

*Added: 2019-Jun-07*

---

### SelectTreeItem

Selects tree item from a tree node by tree id, node and item 

**Parameters:**
- `TreeId`
- `Node`
- `Item`

**Syntax:**

```
SelectTreeItem TreeId "<TreeId>" Node "<NodeKey>" Item "<ItemName>"
```

**Examples:**

```
SelectTreeItem TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "02*1*2" Item "Item 1"
SelectTreeItem TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "*****2" Item "Item 1"
```

*Added: 2019-Nov-06*

---

### SendKey

Sends the desired key from Keyboard.

**Parameters:**
- `Key`

**Syntax:**

```
SendKey <Key>
```

**Examples:**

```
SendKey 0
```

*Added: 2018-Dec-18*

---

### SetCurrentCellColumn

Sets the column to select a cell using it.

**Parameters:**
- `GridId`
- `ColumnId`

**Syntax:**

```
SetCurrentCellColumn <GridId> ColumnId <ColumnId>
```

**Examples:**

```
SetCurrentCellColumn Grid[0] ColumnId MNS
```

*Added: 2020-Aug-07*

---

### SetSAPParameters

Sets all required parameters to manage SAP connection and Actions.

**Parameters:**
- `retries`
- `connTime`

**Syntax:**

```
SetSAPParameters SAPConRetries <retries> SAPConnTime <connTime>
```

**Examples:**

```
SetSAPParameters SAPConRetries 1 SAPConnTime 3
```

*Added: 2019-Oct-28*

---

### ShowAllSAPSessions

> Gets all sap sessions and shows the id's in the log file.

Gets all sap sessions and shows the id's in the log file.

**Syntax:**

```
ShowAllSAPSessions
```

**Examples:**

```
ShowAllSAPSessions
```

*Added: 2021-May-11*

---

### ShowElements

Saves a file with all elements of the current page.

**Syntax:**

```
ShowElements
```

**Examples:**

```
ShowElements
```

*Added: 2019-Mar-27*

---

### StartTransaction

Starts a SAP transaction.

**Parameters:**
- `Trans`

**Syntax:**

```
StartTransaction <Trans>
```

**Examples:**

```
StartTransaction MB52
```

*Added: 2018-Apr-06*

---

### TakeScreenShot

Takes a screenshot of current page and save it in the given path.

**Parameters:**
- `FilePath`
- `FileName`

**Syntax:**

```
TakeScreenShot and save in "<FilePath>" with filename "<FileName>"
```

**Examples:**

```
TakeScreenShot and save in "C:\Images" with filename "ErrorImage.jpg"
```

*Added: 2018-Nov-27*

---

### TreeItemContextMenu

Makes context menu of a tree Item accesible to select option.

**Parameters:**
- `TreeId`
- `Node`
- `Item`

**Syntax:**

```
TreeItemContextMenu TreeId "<TreeId>" Node "<NodeKey>" Item "<ItemName>"
```

**Examples:**

```
TreeItemContextMenu TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "02*1*2" Item "Item 1"
TreeItemContextMenu TreeId "wnd[0]/usr/cntlTREE_CONTROL_CONTAINER/shellcont/shell" Node "*****2" Item "Item 1"
```

*Added: 2022-Feb-17*

---

### TriggerModifiedCell

Triggers the the modified value in a Grid.

**Parameters:**
- `GridId`
- `RowNum`
- `ColumnId`
- `Value`

**Syntax:**

```
TriggerModifiedCell GridId <GridId>
```

**Examples:**

```
SAP TriggerModifiedCell GridId wnd[0]/usr/shell
```

*Added: 2022-Jun-06*

---

### VerticalScroll

Moves the list on or more positions down.

**Parameters:**
- `GridId`
- `Position`

**Syntax:**

```
VerticalScroll GridId <GridId> Pos <Position>
```

**Examples:**

```
VerticalScroll GridId wnd[0]/usr/cntlALV/shellcont/shell Pos 1
```

*Added: 2019-Mar-26*

---

### Wait

Waits for an element to appear in the window or for a specific amount of time.

**Parameters:**
- `Mode`
- `Type`
- `Identifier`
- `Time`
- `RetryNo`

**Syntax:**

```
Wait <Mode> <Time>
Wait <Mode> <Type> <Identifier> <Time> <RetryNo>
```

**Examples:**

```
Wait s 10
Wait e id "LabelId[1]" 5 3
Wait e te "Title Label" 5 3
```

*Added: 2018-May-02*

---

### Write

Writes a text in a TextBox looking control by Id and anchor (reference control at the left of the control).

**Parameters:**
- `Type`
- `Identifyer`
- `Text`
- `Pos`

**Syntax:**

```
Write <Type> <Identifyer> <Text>
Write <Type> <Identifyer> <Text> <Pos>
```

**Examples:**

```
Write id txtbx[1] "Test data to write."
Write an "write at the left" "Test data to write." 1
```

*Added: 2018-Apr-06*

---

### WriteGridCell

Writes a value in a given gridcell.

**Parameters:**
- `GridId`
- `Column`
- `Row`
- `Value`

**Syntax:**

```
WriteGridCell GridId <GridId> Column <Column> Row "<Row>" Value "<Value>"
```

**Examples:**

```
WriteGridCell GridId GridId[0] Column "NAME1" Row 0 Value "Person"
```

*Added: 2019-Jun-28*

---

### WriteText

Writes a text in any element looking control by Id.

**Parameters:**
- `ElementId`
- `Text`

**Syntax:**

```
WriteText ElementId <ElementId> Text "<Text>"
```

**Examples:**

```
WriteText ElementId txtbx[1] Text "Test data to write."
```

*Added: 2022-Sep-28*

---
