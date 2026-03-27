# Excel Reader

**Keyword:** `Excel`

**Functions:** 199

## Description

Excel reader is a C# based tool designed to automate your spreadsheets, allowing you to automate the actions you make such as applying filters, running macros, or event copying information across files, making it easier for you having more than 180 functions available. This tool will help you reduce the time you invest in creating an automation with languages such as Visual Basic and start focusing instead in capturing all your process business rules. 

## Quick Reference

| Function | Description |
|----------|-------------|
| [Append](#append) | Adds a value at the end of the columns in a sheet. |
| [AppendTableRows](#appendtablerows) | Copies a cell or range from one table to another location in another table. |
| [ApplyFilter](#applyfilter) | Filter a column by a certain criteria. |
| [ApplyFilterStartAt](#applyfilterstartat) | Filter a column by a certain criteria starting in a given row. |
| [ApplyFilterWithEmpty](#applyfilterwithempty) | Filter a column considering empty intermediate cells. |
| [ApplyFormat](#applyformat) | Apply format to a given column. |
| [ApplyFormatFullColumn](#applyformatfullcolumn) | Apply a format to a whole column. |
| [ApplyPivotTableFilter](#applypivottablefilter) | Filter an existing pivot table. |
| [ArrangeByData](#arrangebydata) | Looks for repeated contiguous data in a column. |
| [ArrangeChartLabels](#arrangechartlabels) | Show data labels in an ordered chart |
| [AutoFill](#autofill) | Fill the selected range with the incremental or fixed values. |
| [AutoFit](#autofit) | Re-dimension cell widths or heights in a worksheet. |
| [BackgroundColor](#backgroundcolor) | Changes the background color of one or more cells. |
| [BindXMLField](#bindxmlfield) | Binds fields from the XML map to Excel columns or cells. |
| [BreakLinks](#breaklinks) | Break the source links in a workbook. |
| [CachePivotTable](#cachepivottable) | Loads a table in cache to use Pivot Tables. |
| [CellBorder](#cellborder) | Changes the borders of one or more cells. |
| [ChangeChartProperties](#changechartproperties) | Change some parameters in an existing chart |
| [ChangeChartTable](#changecharttable) | Change a given chart's input data. |
| [ChangeSeries](#changeseries) | Modify the range for the datasource of a chart in a given sheet. |
| [ChangeWSName](#changewsname) | Changes the name of a worksheet. |
| [ClearCells](#clearcells) | Deletes the contents of a range of cells |
| [Close](#close) | Close an open workbook. |
| [ColorDuplicates](#colorduplicates) | Mark duplicate cells in value with a color. |
| [ColumnsFit](#columnsfit) | Autofit all the columns in the sheet. |
| [ColumnTransform](#columntransform) | Transforms the given column, from index to Letter vice versa. |
| [Concatenate](#concatenate) | Concatenate cells values. |
| [ConditionalFormat](#conditionalformat) | Apply format to the cells depending on the condition of each cell value. |
| [ConvertTo2007](#convertto2007) | Convert a given Excel file to the computer's Excel version. |
| [Copy](#copy) | Copy values from a worksheet to another one. |
| [CopyCellUnmerge](#copycellunmerge) | Fill blank cells in a worksheet with the value of the previous row for each c... |
| [CopyChart](#copychart) | Copy a chartIndex to the clipboard. |
| [CopyColumn](#copycolumn) | Copy a column to another column. |
| [CopyPaste](#copypaste) | Copies a cell or a range to another location. |
| [CopyPivotTable](#copypivottable) | Copy a pivot table to the clipboard. |
| [CopyRange](#copyrange) | Copy a range of cells to somewhere else in the worksheet. |
| [CopyRangeFormat](#copyrangeformat) | Copy the format of a range to use it in another range. |
| [CopySheet](#copysheet) | Copies the contents of a sheet to another one. |
| [CountIf](#countif) | Counts how many values of a column occur in another column. |
| [CountIf2](#countif2) | Counts how many values of a column occur in another column and are equal to "... |
| [CountSheets](#countsheets) | Count the number of sheets on a given workbook. |
| [CreateChart](#createchart) | Insert a chart using a defined source table |
| [CreateDropDown](#createdropdown) | Creates a dropdown in a cell with the given information. |
| [CreateHyperlink](#createhyperlink) | Creates a shortcut to a desired sheet in the same book |
| [CreatePivotTable](#createpivottable) | Creates a pivot table using the cached pivot table range. |
| [CreateTable](#createtable) | Create a table from an existing range. |
| [CustomSort](#customsort) | Sort by many Columns. |
| [DataSortByColumn](#datasortbycolumn) | Sort a column from a given worksheet. |
| [DateFormat](#dateformat) | Change date formats in a column. |
| [DateFormat2SC](#dateformat2sc) | Change the date format of a column to yyyymmdd. |
| [Dateformat3](#dateformat3) | Change the date format of a column to DD.MM.yyyy. |
| [DateMathOperation](#datemathoperation) | Make a math operation between two columns with dates and write the result on ... |
| [DebugVariables](#debugvariables) | Print the Turing Excel variables to the log file. |
| [DeleteAll](#deleteall) | Delete all data from the worksheet. |
| [DeletePivotTable](#deletepivottable) | Delete an existing Pivot Table. |
| [DeletePrevMonth](#deleteprevmonth) | Delete all rows that have a date from last n months. |
| [DeleteRows](#deleterows) | Delete all rows in a given sheet. |
| [DeleteValue](#deletevalue) | Delete all repetitions of a value from a column. |
| [Dispose](#dispose) | Close Excel without saving any changes. |
| [EditLinks](#editlinks) | Change the source links in a workbook. |
| [ExcludeFilterValues](#excludefiltervalues) | Filter a column excluding certain values. |
| [ExportChart](#exportchart) | Exports all charts images to the given path. |
| [ExportImage](#exportimage) | Export a range of cells as an image. |
| [ExportXML](#exportxml) | Export the previously loaded XML with filled in data from the worksheet. |
| [FieldLength](#fieldlength) | Fills the values in a given column with a character. |
| [Filter](#filter) | Filter a column using the mentioned criteria. |
| [Filter2](#filter2) | Filter a column by name using the mentioned criteria. |
| [FilterHeader](#filterheader) | Filter a given column that matches the criteria. |
| [FilterOff](#filteroff) | Remove filters. |
| [FilterPivotTableSlicer](#filterpivottableslicer) | Select items from a pivot table slicer. |
| [FindRow](#findrow) | Get the row index after searching for a value |
| [FixUsedRange](#fixusedrange) | Delete empty rows from a sheet's used range. |
| [FormatExcelDate](#formatexceldate) | Convert an Excel date to another format |
| [FreezePane](#freezepane) | Freeze a row to make it visible all the time. |
| [GetCellValue](#getcellvalue) | Get the value of a cell and save it in a variable. |
| [GetLastRow](#getlastrow) | Find the last row with data in a column. |
| [GetPivotTableNames](#getpivottablenames) | Get a list of the pivot table names in a sheet. |
| [GetSheetName](#getsheetname) | Save the name of a worksheet in a variable. |
| [GetSheetNames](#getsheetnames) | Get a list of the sheet names in a book. |
| [GetSpecial](#getspecial) | Get the location of a cell indicated by "special" identifiers like lastCell. |
| [GetTableNames](#gettablenames) | Get a list of the table names in a sheet. |
| [GetUnique](#getunique) | Saves in a variable a list of unique values in a given column. |
| [GetXSD](#getxsd) | Extract the schema from a previously loaded XML in excel. |
| [GoToCell](#gotocell) | Move the active cell to a given a sheet. |
| [GroupRange](#grouprange) | Groups a range of rows or columns. |
| [Hide](#hide) | Hide one or more rows or columns in a sheet. |
| [IfColExists](#ifcolexists) | Ensures that a column header exists. |
| [IfContains](#ifcontains) | Looks for all ocurrences of a value in a column and changes the value in anot... |
| [IfEmpty](#ifempty) | Fill empty values in a column. |
| [ImportImage](#importimage) | Import an image to a specific position. |
| [InsertCol](#insertcol) | Insert a Column to the worksheet. |
| [InsertRow](#insertrow) | Insert a Row to the worksheet. |
| [IsRegexMatch](#isregexmatch) | Not working yet. Check for regex matches. |
| [IsSheetVisible](#issheetvisible) | Show the visibility status in a given sheet. |
| [KeepCols](#keepcols) | Deletes all columns except those specified by a given index. |
| [KeepColsHeaders](#keepcolsheaders) | Deletes all columns except those specified by Name. |
| [KeepHeaders](#keepheaders) | Deletes all data except headers. |
| [KeepRows](#keeprows) | Deletes rows acording to a list of values in a given column index. |
| [LoadChart](#loadchart) | Loads a Chart from a Worksheet to a variable. |
| [LoadCSV](#loadcsv) | Open a csv file as a workbook. |
| [LoadCSV2](#loadcsv2) | Open a csv file separated by (, or ;) as a workbook. |
| [LoadCSVFixed](#loadcsvfixed) | Open a csv file separated by (, or ;) as a workbook. |
| [LoadFileFrom](#loadfilefrom) | Loads a file based in up to two query parameters. |
| [LoadWBook](#loadwbook) | Open a workbook. |
| [LoadWSfrom](#loadwsfrom) | Loads a Worksheet searching it by part of its name within a workbook. |
| [LoadWSheet](#loadwsheet) | Loads a Worksheet to a variable. |
| [LoadXSD](#loadxsd) | Loads an XML Map to the workbook for exporting data in an XML. |
| [MakeZip](#makezip) | Currently not working. Makes a zip file made out of workbooks. |
| [MoveCol](#movecol) | Moves a column to a diferent one. |
| [MoveField](#movefield) | Move a pivot table field to another field type. |
| [MoveRow](#moverow) | Moves a row to a diferent one. |
| [MoveSheet](#movesheet) | Move a worksheet to a different position in the same workbook. |
| [MoveTableFieldPosition](#movetablefieldposition) | Switch position of a field in a pivot table. |
| [MultiFilter](#multifilter) | Filter a column with many criteria. |
| [NewWB](#newwb) | Create a new workbook. |
| [NewWs](#newws) | Add a new worksheet to the workbook. |
| [NormalizeHeaders](#normalizeheaders) | Uppercase all contents in a row. |
| [PageSetup](#pagesetup) | Setup Page properties |
| [PivotFieldDesign](#pivotfielddesign) | Modify the pivot table's field design and field settings. |
| [Protect](#protect) | Protect a workbook or sheet. |
| [RangeDelete](#rangedelete) | Delete cells from a range. |
| [RangeToImage](#rangetoimage) | Copy a range of a worksheet to an image. |
| [ReadCell](#readcell) | Read a cell from a worksheet and save it in a variable. |
| [ReadCellText](#readcelltext) | Read a cell's value and save it in a variable. |
| [ReadColumn](#readcolumn) | Read a column and save it in a variable. |
| [ReadFields](#readfields) | Read the name of the pivot table fields and save them in a list. |
| [ReadPivotTable](#readpivottable) | Load existing pivot tables in a worksheet. |
| [ReadRange](#readrange) | Read a Range of a worksheet as a Row x Column List. |
| [ReadRows](#readrows) | Read the Used Range of a worksheet as a Row x Column List. |
| [ReadRowsCSV](#readrowscsv) | Read all rows in a sheet and separate the values by a delimiter. |
| [ReadRowsWithFormat](#readrowswithformat) | Read the Used Range of a worksheet as a Row x Column List and keep the format... |
| [ReadValueThatMatch](#readvaluethatmatch) | Filter a column by a value and read the corresponding value from another column. |
| [RefreshAll](#refreshall) | Get the latest data by refreshing all sources in the workbook. |
| [RefreshAllPT](#refreshallpt) | Refresh all pivot tables that exist in a workbook. |
| [RefreshPivotTable](#refreshpivottable) | Refreh a given Pivot Table. |
| [RemoveAllTableFilters](#removealltablefilters) | Remove the existing filters in a worksheet that contains tables. |
| [RemoveCharacter](#removecharacter) | Remove a set of character(s) from a text file. |
| [RemoveCols](#removecols) | Delete the specified columns. |
| [RemoveDuplicates](#removeduplicates) | Remove the duplicate rows from a given sheet. |
| [RemoveEmptyRow](#removeemptyrow) | Deletes all empty rows from a worksheet. |
| [RemoveFilters](#removefilters) | Remove the existing filters in a worksheet. |
| [RemoveMacros](#removemacros) | Remove all the existing macros in a workbook. |
| [RemoveRows](#removerows) | Delete rows in a worksheet. |
| [RemoveRowsHeader](#removerowsheader) | Deletes rows in a given column header. |
| [RemoveSheets](#removesheets) | Remove worksheets from a workbook. |
| [RemoveTableDuplicates](#removetableduplicates) | Remove the duplicate rows from a given sheet and table. |
| [RemoveWorkbookConnections](#removeworkbookconnections) | Remove all connections in a workbook. |
| [RepeatAllLabels](#repeatalllabels) | Change repeat all item labels option in a pivot table. |
| [ReplaceAll](#replaceall) | Replace a text sequence for another one. |
| [ReplaceCharacter](#replacecharacter) | Replaces a character or substring with another. |
| [ReplaceText](#replacetext) | Replace a text sequence for another one. |
| [ReplaceTextVisible](#replacetextvisible) | Replace the text in a visible cell and replace it for another. |
| [ResizeTable](#resizetable) | Resize an existing table. |
| [RunMacro](#runmacro) | Run a macro in a workbook. |
| [RunMacroAsync](#runmacroasync) | Run a macro asynchronously in a workbook. |
| [Save](#save) | Save a workbook. |
| [SaveAs](#saveas) | Save a workbook as a different file. |
| [SaveAsCSV](#saveascsv) | Save the active worksheet as a CSV file. |
| [SaveWBMonth](#savewbmonth) | Currently not working. Save workbook with the name of the current month. |
| [SetErrorChecking](#seterrorchecking) | Enable or disable an ErrorCheckingOption. |
| [SetSheetVisibility](#setsheetvisibility) | Hide or unhide sheets in a given book. |
| [SetTableStyle](#settablestyle) | Set a predefined style in an existing table. |
| [ShowAllData](#showalldata) | Show all data in worksheet. |
| [ShowChartDataLabels](#showchartdatalabels) | Show the data labels in a chart |
| [ShowPivotTableFields](#showpivottablefields) | Show names of fields from an existing pivot table. |
| [SortColumns](#sortcolumns) | Sort by a Column. |
| [SortPivotTableField](#sortpivottablefield) | Sort an existing field in a pivot table. |
| [SpecificFontValues](#specificfontvalues) | Change cell properties such as font color, size, etc. |
| [SplitInFiles](#splitinfiles) | Split file into other files. |
| [Subtotal](#subtotal) | Calculate the subtotal within a range. |
| [SumAllColumnValues](#sumallcolumnvalues) | Sum all the values on a column. |
| [TableField](#tablefield) | Define how the fields for a given pivot table are used. |
| [TableGetSpecial](#tablegetspecial) | Get the location of a cell indicated in a table by "special" identifiers such... |
| [TextFormat](#textformat) | Set a text format to a given column. |
| [TextFormat2](#textformat2) | Set a text format to a given column by header name. |
| [TextFormatAll](#textformatall) | Set a text format to all the sheet. |
| [TextToColumns](#texttocolumns) | Separate text in a range to columns |
| [TurnAlertsTo](#turnalertsto) | Turn Excel displayed alerts on or off. |
| [TurnHeadlessTo](#turnheadlessto) | Turn the headless flag to true or false just for the excel processes. If it i... |
| [Unhide](#unhide) | Unhide all rows or columns in a given range. |
| [UnloadXSD](#unloadxsd) | Unload the XSD schema or XML from a workbook. |
| [Unmerge](#unmerge) | Unmerge all cells from the worksheet. |
| [Unprotect](#unprotect) | Unlock the protection from a workbook or sheet. |
| [UpdatePT](#updatept) | Update the pivot table range. |
| [UpdatePTChangingSource](#updateptchangingsource) | Update a Pivot table by name changing the data source. |
| [Write](#write) | Write something in a given cell in a worksheet. |
| [Write2DList](#write2dlist) | Write the values in a 2D List variable starting at a given cell on a worksheet. |
| [WriteAll](#writeall) | Write something in all the cells of a given column. |
| [WriteFormula](#writeformula) | Write a formula in a given cell or range of visible cells. |
| [WriteFormulaVisible](#writeformulavisible) | Write a formula in a cell or range. |
| [WriteInRange](#writeinrange) | Write a value on an especific range of cells. |
| [WriteList](#writelist) | Write a list of values from a list variable into a range or column. |
| [WriteListOnColumn](#writelistoncolumn) | Write the values in a List Variable to a column on a worksheet. |
| [WriteListOnRow](#writelistonrow) | Write the values in a List Variable to a row on a worksheet. |
| [WriteTable](#writetable) | Write a table in the last row of a worksheet using the given variable. |
| [WriteValueThatMatch](#writevaluethatmatch) | Deprecated. Apply a filter to a column and write the given value to a corresp... |
| [WriteValueThatMatches](#writevaluethatmatches) | Apply a filter to a column and write the given value(s) in another column(s). |
| [WriteVariableValue](#writevariablevalue) | Write the data saved in a variable, to a given cell location. |
| [Zoom](#zoom) | Apply Zoom in a given worksheet. |

---

## Functions

### Append

> Adds a value at the end of the columns in a sheet.

Adds a value at the end of the columns in a sheet, it can be one or more columns. Column A is index 1. Spaces between index and text are important.

**Parameters:**
- `worksheetKey`
- `index`
- `text`

**Syntax:**

```
Append from <worksheetKey> at [<index1> ="<text>",<index2> ="<text>",...,<indexN> ="<text>"]
```

**Examples:**

```
Append from wsGE at [2 ="='[zvf05_prueba.xls]Process'!$B$narow",4 ="='[zvf05_prueba.xls]Process'!$D$narow"]
Append from libro at [1 ="Total",2 ="=Sum(B2:B4)"]
```

*Added: 2017-Nov-13*

---

### AppendTableRows

> Copies a cell or range from one table to another location in another table.

Copies a cell or range from a table to another location or another table, just as ctrl+c ctrl+v would. CopyRange can be ranges such as A1:B12, A1,lastD or UsedRange. n. The available types are all, except_borders, column_widths, comments, formats, formulas, formulas_and_number_formats, validation, values, values_and_number_formats or no type. 

**Parameters:**
- `worksheetKey`
- `type`
- `tablesource`
- `range`
- `worksheetKey2`
- `tabledestination`
- `column`

**Syntax:**

```
AppendTableRows from <worksheetKey> table <tablesource> range <Range> to <worksheetKey2> table <tabledestination>
AppendTableRows from <worksheetKey> table <tablesource> range <Range> to <worksheetKey2> in column <column>
AppendTableRows from <worksheetKey> table <tablesource> range <Range> to <worksheetKey2> table <tabledestination> in column <column>
AppendTableRows from <worksheetKey> range <Range> to <worksheetKey2> table <tabledestination>
AppendTableRows from <worksheetKey> range <Range> to <worksheetKey2> table <tabledestination> in column <column>
AppendTableRows <type:all|except_borders|column_widths|comments|formats|formulas|formulas_and_number_formats|validation|values|values_and_number_formats|> from <worksheetKey> table <tablesource> range <Range> to <worksheetKey2> table <tabledestination>
```

**Options:**

- `type`: `all`, `except_borders`, `column_widths`, `comments`, `formats`, `formulas`, `formulas_and_number_formats`, `validation`, `values`, `values_and_number_formats`

**Examples:**

```
AppendTableRows values from hoja1 table Table1 range A6:lastD to hoja1 table Table2
AppendTableRows all from hoja1 table Table1 range A6:lastD to hoja1 in column H
AppendTableRows from hoja1 table Table1 range B6:lastD to hoja1 table Table2 in column 2
```

*Added: 2021-Oct-27*

---

### ApplyFilter

> Filter a column by a certain criteria.

Apply a filter to a column located in a given index. Index begins with 1.
Criteria refers to the word(s) used to apply the filter, use wildcard "*" to represent any series of characters, "?" to represent any single character in the criteria.
Comparison operators may be used at the begining of the criteria to indicate the following: "<>" different than the criteria, "<" less than, ">" more than, "<=" less or equal than,  ">=" more or equal than, "=" equal, if not stated this is the default comparison operator.  
There are options to filter by cellcolor or fontcolor, stating the RGB values in the criteria. 
The "delete rows" syntax will delete the rows that match the criteria. The "copy their value" syntax will create a List with the filtered values and save it in a given variable. Comparison operators are required in this syntax. Wildcard characters do not work in this syntax. 
The "LetterIndex" syntax takes the letter of the column instead of the index, and will write aditional numbers on a given columnIndex whenever the criteria is matched. 
Up to two criteria can be stated, separated by ";", corresponding number results must be indicated aswell. Wildcard characters do not work in this syntax. 
Table syntaxes must be used when an excel table is involved and indexes start with 1 relative to the table, for instance if a table is in range D2:F10, index 1 will refer to column D.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `columnLetterIndex`
- `criteria`
- `saveVariable`
- `columnIndex`
- `numberValue`
- `tableName`

**Syntax:**

```
ApplyFilter to the worksheet <worksheetKey> to the column with the index {<columnIndex>} with the criteria "<criteria>"
ApplyFilter to the worksheet <worksheetKey> in table {<tableName>} to the column with the index {<columnIndex>} with the criteria "<criteria>"
ApplyFilter to the worksheet <worksheetKey> in table {<tableName>} to the column with the index {<columnIndex>} with the criteria "<criteria>" and delete the rows
ApplyFilter to the worksheet <worksheetKey> to the column with the index {<columnIndex>} with the criteria "<criteria>" and delete the rows
ApplyFilter to the worksheet <worksheetKey> to the column with the index {<columnIndex>} with the criteria "<criteria>" and copy their value on "<saveVariable>"
ApplyFilter to the worksheet <worksheetKey> in table {<tableName>} to the column with the index {<columnIndex>} by <criteriaOption:cellcolor|fontcolor> with the criteria "<criteria:R,G,B|Automatic|NoFill>"
ApplyFilter to the worksheet <worksheetKey> to the column with the index {<columnIndex>} by <criteriaOption:cellcolor|fontcolor> with the criteria "<criteria:R,G,B|Automatic|NoFill>" and delete the rows
ApplyFilter to the worksheet <worksheetKey> in table {<tableName>} to the column with the index {<columnIndex>} by <criteriaOption:cellcolor|fontcolor> with the criteria "<criteria:R,G,B|Automatic|NoFill>" and delete the rows
ApplyFilter to the worksheet <worksheetKey> to the column with the LetterIndex {<columnLetterIndex>} with the criteria "<criteria>" and write on the column {<columnIndex>} "<numberValue>"
```

**Options:**

- `criteriaOption`: `cellcolor`, `fontcolor`
- `criteria`: `R,G,B`, `Automatic`, `NoFill`
- `criteriaOption`: `cellcolor`, `fontcolor`
- `criteria`: `R,G,B`, `Automatic`, `NoFill`
- `criteriaOption`: `cellcolor`, `fontcolor`
- `criteria`: `R,G,B`, `Automatic`, `NoFill`

**Examples:**

```
ApplyFilter to the worksheet WSExampleName to the column with the index {2} with the criteria "Error"
ApplyFilter to the worksheet WSExampleName to the column with the index {2} by cellcolor with the criteria "255,255,0"
ApplyFilter to the worksheet WSExampleName in table {Table1} to the column with the index {2} with the criteria "Si"
```

*Added: 2020-Nov-06*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/ApplyFilter.pdf)

---

### ApplyFilterStartAt

> Filter a column by a certain criteria starting in a given row.

Apply a filter to a column located in a given index starting at a desired row. Index begins with 1. 
Criteria refers to the word(s) used to apply the filter, use wildcard "*" to represent any series of characters, "?" to represent any single character in the criteria. 
Comparison operators may be used at the begining of the criteria to indicate the following: "<>" different than the criteria, "<" less than, ">" more than, "<=" less or equal than,  ">=" more or equal than, "=" equal, if not stated this is the default comparison operator.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `rowIndex`
- `columnLetterIndex`
- `criteria`
- `saveVariable`
- `numberValue`

**Syntax:**

```
ApplyFilterStartAt to the worksheet {<worksheetKey>} start at row {<rowIndex>} to the column with the index {<columnIndex>} with the criteria "<criteria>"
ApplyFilterStartAt to the worksheet {<worksheetKey>} start at row {<rowIndex>} to the column with the index {<columnIndex>} with the criteria "<criteria>" and copy their value on "<SaveVariable>"
ApplyFilterStartAt to the worksheet {<worksheetKey>} start at row {<rowIndex>} to the column with the index {<columnIndex>} with the criteria "<criteria>" and delete the rows
ApplyFilterStartAt to the worksheet {<worksheetKey>} start at row {<rowIndex>} to the column with the index {<columnIndex>} by <criteriaOption:cellcolor|fontcolor> with the criteria "<criteria:R,G,B|Automatic|NoFill>"
ApplyFilterStartAt to the worksheet {<worksheetKey>} start at row {<rowIndex>} to the column with the LetterIndex {<columnLetterIndex>} with the criteria "<criteria>" and write on the column {<columnIndex>} "<numberValue>"
```

**Options:**

- `criteriaOption`: `cellcolor`, `fontcolor`
- `criteria`: `R,G,B`, `Automatic`, `NoFill`

**Examples:**

```
ApplyFilterStartAt to the worksheet {WSExampleName} start at row {5} to the column with the index {2} with the criteria "Error"
ApplyFilterStartAt to the worksheet {WSExampleName} start at row {5} to the column with the index {2} by cellcolor with the criteria "255,255,0"
ApplyFilterStartAt to the worksheet {WSExampleName} start at row {5} to the column with the index {2} by cellcolor with the criteria "NoFill"
```

*Added: 2020-Nov-06*

---

### ApplyFilterWithEmpty

> Filter a column considering empty intermediate cells.

Apply a filter to a column by their index, it considers intermediate empty cells. Matching results are saved un a given Variable. Index starts from 1. Criteria must start with a comparison operator (=,<>,<,<=,>,>=).

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `criteria`
- `variableName`

**Syntax:**

```
ApplyFilterWithEmpty to the worksheet {<worksheetKey>} to the column with the index {<columnIndex>} with the criteria {<criteria>} and copy their value on {<variableName>}
```

**Examples:**

```
ApplyFilterWithEmpty to the worksheet {sheet} to the column with the index {3} with the criteria {=VALUE} and copy their value on {filtrado}
```

*Added: 2019-Jun-04*

---

### ApplyFormat

> Apply format to a given column.

Apply format to a given column index or heading. Format is applied only to filled in cells, to apply to the whole column use "all" syntax. Index starts with 1. The link describes the different format options available. https://exceljet.net/custom-number-formats

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `rowindex`
- `format`
- `columnName`

**Syntax:**

```
ApplyFormat from <worksheetKey> in_column_index <columnIndex> format <format>
ApplyFormat from <worksheetKey> in_column_index <columnIndex> all format <format>
ApplyFormat from <worksheetKey> in_column "<columnName>" format <format>
ApplyFormat from <worksheetKey> in_column "<columnName>" all format <format>
ApplyFormat from "<worksheetKey>" in_column_index "<columnIndex>" from row "<rowIndex>" to "<rowIndex>" format "<format>"
```

**Examples:**

```
ApplyFormat from sheet1WS in_column_index 15 format General
ApplyFormat from sheet1WS in_column "UnTexto" all format @
ApplyFormat from sheet1WS in_column "NumeroConDecimales" format ##.00
```

*Added: 2018-Feb-06*

---

### ApplyFormatFullColumn

> Apply a format to a whole column.

Applies a desired format to a full column, this sintax works for empty columns. Index starts with 1. The link describes the different format options available. https://exceljet.net/custom-number-formats

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `format`
- `columnName`

**Syntax:**

```
ApplyFormatFullColumn from <worksheetKey> in_column_index <columnIndex> format <format>
ApplyFormatFullColumn from <worksheetKey> in_column "<columnName>" format <format>
```

**Examples:**

```
ApplyFormatFullColumn from sheet1WS in_column_index 15 format General
ApplyFormatFullColumn from sheet1WS in_column "UnTexto" format @
ApplyFormatFullColumn from sheet1WS in_column "NumeroConDecimales" format ##.00
```

*Added: 2020-Jul-02*

---

### ApplyPivotTableFilter

> Filter an existing pivot table.

Filter a specific pivot table by pivot field name, and search criteria. ReadPivotTable instruction must be used prior applying any filter. Use "(All)" criteria to clear all filter values of the given field name. Check extra docs to understand "in table field" syntax for filtering values of fields that are not of "filter" type. 
Date filtering requires source syntax to indicate the format of the criteria. If no criteria is found an error will be raised.

**Parameters:**
- `pivotTableKey`
- `pivotTableFieldName`
- `criteria`
- `dateFormat`
- `pivotTableFieldCaption`

**Syntax:**

```
ApplyPivotTableFilter to the table {<pivotTableKey>} in field {<pivotTableFieldName>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in field {<pivotTableFieldName>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>} source {<dateFormat>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in caption {<pivotTableFieldCaption>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in caption {<pivotTableFieldCaption>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>} source {<dateFormat>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in table field {<pivotTableFieldName>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in table field {<pivotTableFieldName>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>} source {<dateFormat>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in table caption {<pivotTableFieldCaption>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>}
ApplyPivotTableFilter to the table {<pivotTableKey>} in table caption {<pivotTableFieldCaption>} with the criteria {<criteria1;criteria2;...criteriaN|(All)>} source {<dateFormat>}
```

**Examples:**

```
ReadPivotTable "DynamicTable1" From WSTable As PivotTableKey
ApplyPivotTableFilter to the table {PivotTableKey} in field {Country} with the criteria {USA}
ApplyPivotTableFilter to the table {PivotTableKey} in caption {Start Date} with the criteria {13/01/2022} source {dd/MM/yyyy}
```

*Added: 2021-Jul-12*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### ArrangeByData

> Looks for repeated contiguous data in a column.

Looks for minNumber of contiguous values in a given column, starting at a given row, saving a list variable defined by variableKey where it stores the row index of the first occurrence found and the row index where the occurrence chaged its value. For instance, supose minNumber is 2 and Cells A3 to A6 have the value "Yes" and A7 the value "No". Given that it was looking for at least 2 values to be repeated, the result would return [3,7] meaning cells in 3,4,5,6 have the same value. The parameter "reverse" will return [7,3] in this example.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `rowIndex`
- `minNumber`
- `variableKey`
- `direction`

**Syntax:**

```
ArrangeByData {<worksheetKey>} in_column_index {<columnIndex>} start_at {<rowIndex>} min_number {<minNumber>} save_as {<variableKey>} <direction:none|reverse>
```

**Options:**

- `direction`: `none`, `reverse`

**Examples:**

```
ArrangeByData {hoja} in_column_index {5} start_at {2} min_number {3} save_as {grupo} none
ArrangeByData {hoja} in_column_index {5} start_at {2} min_number {3} save_as {grupo} reverse
```

*Added: 2019-Dec-18*

---

### ArrangeChartLabels

> Show data labels in an ordered chart

Display the data labels for a given series in an orderly presentation chart.Series are identified by index starting with 1.

**Parameters:**
- `chartKey`
- `seriesNumber`
- `colorNumber`

**Syntax:**

```
ArrangeChartLabels in <chartKey> series <seriesNumber> with color <colorNumber>
```

**Examples:**

```
ArrangeChartLabels in graf series 1 with color 1
ArrangeChartLabels in graf series 2 with color 2
```

*Added: 2021-Mar-30*

---

### AutoFill

> Fill the selected range with the incremental or fixed values.

Fills the column or row with the formula and value that contains the original cell. Range values can use the word "UsedRange" which indicates all cells modified in the sheet. 
Start_at syntax must use A1 type values and is only taken into account when used together with "UsedRange" parameter. 
Direction values can be (down,up,right,left). To clarify, direction "up" from range A3:A10 will use the contents and format of downmost cell, which is A10 and fill with it the rest of cells in the range. 
In_sheet syntax without "direction" parameter only works for ranges within the same column. 
Start_from syntax can use the following incrementTypes fillSeries, flashfill, formats, values, days, months, years, weekdays. Start_from can be cells or ranges.

**Parameters:**
- `worksheetKey`
- `range`
- `cell`
- `startRange`
- `direction`
- `incrementType`

**Syntax:**

```
AutoFill <worksheetKey> range UsedRange start_from <startRange> direction <direction:down|up|right|left>
AutoFill <worksheetKey> range UsedRange start_from <startRange> direction <direction:down|up|right|left> autoincrement <incrementType:fillSeries|flashfill|formats|values|days|months|years|weekdays>
AutoFill <worksheetKey> range <range> start_from <startRange> direction <direction:down|up|right|left> autoincrement <incrementType:fillSeries|flashfill|formats|values|days|months|years|weekdays>
AutoFill <worksheetKey> range <range> direction <direction:down|up|right|left>
AutoFill in_sheet <worksheetKey> using_range_from <range>
AutoFill in_sheet <worksheetKey> using_range_from <range> direction <direction:down|up|right|left>
AutoFill in_sheet <worksheetKey> using_range_from <range> start_at <cell>
AutoFill in <worksheetKey> range <range> start_at <cell>
AutoFill in <worksheetKey> range <range> start_at <cell> direction <direction:down|up|right|left>
```

**Options:**

- `direction`: `down`, `up`, `right`, `left`
- `direction`: `down`, `up`, `right`, `left`
- `incrementType`: `fillSeries`, `flashfill`, `formats`, `values`, `days`, `months`, `years`, `weekdays`
- `direction`: `down`, `up`, `right`, `left`
- `incrementType`: `fillSeries`, `flashfill`, `formats`, `values`, `days`, `months`, `years`, `weekdays`
- `direction`: `down`, `up`, `right`, `left`
- `direction`: `down`, `up`, `right`, `left`
- `direction`: `down`, `up`, `right`, `left`

**Examples:**

```
AutoFill Hoja range A1:G20 direction down
AutoFill Hoja range A1:G20 start_from A1:A20 direction right autoincrement FillSeries
AutoFill Hoja range UsedRange start_from B2:B2 direction down
```

*Added: 2017-Nov-13*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/AutoFill.pdf)

---

### AutoFit

> Re-dimension cell widths or heights in a worksheet.

Autofit cell widths or heights in a worksheet, it can be in the entire worksheet, by column or by row.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
AutoFit <worksheetKey>
AutoFit <worksheetKey> by column
AutoFit <worksheetKey> by row
```

**Examples:**

```
AutoFit WSvar
AutoFit WSvar by column
AutoFit WSvar by row
```

*Added: 2017-Aug-23*

---

### BackgroundColor

> Changes the background color of one or more cells.

Changes the background color of a specific cell, range, rows or columns. It has the posibility to change only the visible cells of a filtered range, columns or rows. For the colors available refer to: "https://docs.microsoft.com/en-us/dotnet/api/system.drawing.knowncolor?view=netframework-4.8". Index starts with 1.

**Parameters:**
- `worksheetKey`
- `cellName`
- `columnIndex`
- `rowIndex`
- `colorNameOrRGB`
- `visibleFlag`

**Syntax:**

```
BackgroundColor from {<worksheetKey>} cell {<cellName>} to {<colorNameOrRGB:R,G,B|colorName>}
BackgroundColor from {<worksheetKey>} range {<range>} to {<colorNameOrRGB:R,G,B|colorName>}
BackgroundColor from {<worksheetKey>} column {<columnIndex>} start_at {<rowIndex>} to {<colorNameOrRGB:R,G,B|colorName>} visible
BackgroundColor from {<worksheetKey>} column {<columnIndex>} start_at {<rowIndex>} to {<colorNameOrRGB:R,G,B|colorName>}
BackgroundColor from {<worksheetKey>} column {<columnIndex>,<columnIndex>,<columnIndex>} start_at {<rowIndex>} to {<colorNameOrRGB:R,G,B|colorName>} visible
BackgroundColor from {<worksheetKey>} column {<columnIndex>,<columnIndex>,<columnIndex>} start_at {<rowIndex>} to {<colorNameOrRGB:R,G,B|colorName>}
BackgroundColor from {<worksheetKey>} row {<rowIndex>} start_at {<columnIndex>} to {<colorNameOrRGB:R,G,B|colorName>} visible
BackgroundColor from {<worksheetKey>} row {<rowIndex>} start_at {<columnIndex>} to {<colorNameOrRGB:R,G,B|colorName>}
BackgroundColor from {<worksheetKey>} row {<rowIndex>,<rowIndex>,<rowIndex>} start_at {<columnIndex>} to {<colorNameOrRGB:R,G,B|colorName>} visible
BackgroundColor from {<worksheetKey>} row {<rowIndex>,<rowIndex>,<rowIndex>} start_at {<columnIndex>} to {<colorNameOrRGB:R,G,B|colorName>}
```

**Options:**

- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`
- `colorNameOrRGB`: `R,G,B`, `colorName`

**Examples:**

```
BackgroundColor from {Wsheet1} cell {B5} to {255,255,255}
BackgroundColor from {Wsheet1} range {B5:D5} to {255,255,255}
BackgroundColor from {Wsheet1} range {B5:D5} to {Blue}
```

*Added: 2019-Jun-06*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/BackgroundColor.pdf)

---

### BindXMLField

> Binds fields from the XML map to Excel columns or cells.

Binds fields from the XML map to Excel columns or cells. Use cell syntax for single non repiting elements in an XML. 
When using repeating elements, use column syntax to bind the whole column to the field. XPath is used indicate the exact field in the loaded XML to be binded. 
Query syntax from xpath can not be used. Has headings syntax is used when the column starts with a heading, so it will be omitted from the binding.

**Parameters:**
- `xpath`
- `workbookKey`
- `worksheetKey`
- `rowIndex`
- `columnIndex`

**Syntax:**

```
BindXMLField "<xpath>" in <workbookKey> sheet <worksheetKey> to cell {<rowIndex>,<columnIndex>}
BindXMLField "<xpath>" in <workbookKey> sheet <worksheetKey> to column {<columnIndex>}
BindXMLField "<xpath>" in <workbookKey> sheet <worksheetKey> to column {<columnIndex>} has heading
```

**Examples:**

```
BindXMLField "/factura/informacionpersonal/curp" in wbFacturas sheet wsSheet to cell {1,2}
BindXMLField "/factura/cuenta/clabe" in wbFacturas sheet wsSheet to column {1}
```

*Added: 2020-Jun-19*

---

### BreakLinks

> Break the source links in a workbook.

Breaks all the source links in a workbook. If a known link needs to be broken, "previous link" can be specified. If that link does not exist it will throw an exception.

**Parameters:**
- `workbookKey`
- `path`
- `previousPath`
- `link`

**Syntax:**

```
BreakLinks from {<workbookKey>}
BreakLinks from {<workbookKey>} previous link "<link>"
```

**Examples:**

```
BreakLinks from {WBook}
BreakLinks from {WBook} previous link "C:\Users\softtek\files\some file.xlsx"
```

*Added: 2022-Dec-12*

---

### CachePivotTable

> Loads a table in cache to use Pivot Tables.

Loads a table in cache, this is the first step to use Pivot Tables. 
FirstCell indicates the top, leftmost cell in the table range and finalCell is the bottom, rightmost cell. Following step is to use CreatePivotTable. 
If its necessary to specify the pivot table version use the syntax option with the version field. The option that can be used in the PivotTableVersion field are xlPivotTableVersion10, xlPivotTableVersion11, xlPivotTableVersion12, xlPivotTableVersion13, xlPivotTableVersion14, xlPivotTableVersion15, xlPivotTableVersion2000 and xlPivotTableVersionCurrent. 
For more information about PivotTableVersions open this link "https://docs.microsoft.com/en-us/office/vba/api/excel.xlpivottableversionlist".

**Parameters:**
- `workbookKey`
- `worksheetKey`
- `firstCell`
- `finalCell`
- `cachePTkey`
- `PivotTableVersion`

**Syntax:**

```
CachePivotTable <workbookKey> in <worksheetKey> from UsedRange as <cachePTkey>
CachePivotTable <workbookKey> in <worksheetKey> from <firstCell> to <finalCell> as <cachePTkey>
CachePivotTable <workbookKey> in <worksheetKey> from UsedRange as <cachePTkey> version <PivotTableVersion:xlPivotTableVersion10|xlPivotTableVersion11|xlPivotTableVersion12|xlPivotTableVersion13|xlPivotTableVersion14|xlPivotTableVersion15|xlPivotTableVersion2000|xlPivotTableVersionCurrent>
CachePivotTable <workbookKey> in <worksheetKey> from <firstCell> to <finalCell> as <cachePTkey> version <PivotTableVersion:xlPivotTableVersion10|xlPivotTableVersion11|xlPivotTableVersion12|xlPivotTableVersion13|xlPivotTableVersion14|xlPivotTableVersion15|xlPivotTableVersion2000|xlPivotTableVersionCurrent>
```

**Options:**

- `PivotTableVersion`: `xlPivotTableVersion10`, `xlPivotTableVersion11`, `xlPivotTableVersion12`, `xlPivotTableVersion13`, `xlPivotTableVersion14`, `xlPivotTableVersion15`, `xlPivotTableVersion2000`, `xlPivotTableVersionCurrent`
- `PivotTableVersion`: `xlPivotTableVersion10`, `xlPivotTableVersion11`, `xlPivotTableVersion12`, `xlPivotTableVersion13`, `xlPivotTableVersion14`, `xlPivotTableVersion15`, `xlPivotTableVersion2000`, `xlPivotTableVersionCurrent`

**Examples:**

```
CachePivotTable Libro1 in Sheet1key from UsedRange as CachePT1
CachePivotTable Libro1 in Sheet1key from A1 to F20 as CachePT1
CachePivotTable Libro1 in Sheet1key from UsedRange as CachePT1 version xlPivotTableVersion14
```

*Added: 2017-Aug-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### CellBorder

> Changes the borders of one or more cells.

Changes the borders of a specific cell, range of cells. Range values can use "UsedRange" or ranges using A1:lastF to get a range from A to the last row of F. 
Valid styles are continuous, dash, dashdot, dashdotdot, dot, double, none, slantdashdot. Valid line weights are thin, medium, thick, hairLine. Valid border types are left, right, bottom, top, insideHorizontal, insideVertical, diagonalDown, diagonalUp. Inside horizontal and vertical mean that the border will be drawn in the inside lines of a range and not in the outer borders. Only visible cells are modified.
Index starts with 1.

**Parameters:**
- `worksheetKey`
- `range`
- `border`
- `borderStyle`
- `weight`

**Syntax:**

```
CellBorder from {<worksheetKey>} range {<range>} style {<borderStyle:continuous|dash|dashdot|dashdotdot|dot|double|none|slantdashdot>} line weight {<weight:thin|medium|thick|hairLine>}
CellBorder from {<worksheetKey>} range {<range>} border {<border:left|right|bottom|top|insideHorizontal|insideVertical|diagonalDown|diagonalUp>} style {<borderStyle:continuous|dash|dashdot|dashdotdot|dot|double|none|slantdashdot>} line weight {<weight:thin|medium|thick|hairLine>}
```

**Options:**

- `borderStyle`: `continuous`, `dash`, `dashdot`, `dashdotdot`, `dot`, `double`, `none`, `slantdashdot`
- `weight`: `thin`, `medium`, `thick`, `hairLine`
- `border`: `left`, `right`, `bottom`, `top`, `insideHorizontal`, `insideVertical`, `diagonalDown`, `diagonalUp`
- `borderStyle`: `continuous`, `dash`, `dashdot`, `dashdotdot`, `dot`, `double`, `none`, `slantdashdot`
- `weight`: `thin`, `medium`, `thick`, `hairLine`

**Examples:**

```
CellBorder from {sheetVar} range {A2:lastA} style {continuous} line weight {thin}
CellBorder from {thisSheet} range {UsedRange} style {double} line weight {thick}
CellBorder from {thisSheet} range {B3} style {none} line weight {hairLine}
```

*Added: 2024-Jan-25*

---

### ChangeChartProperties

> Change some parameters in an existing chart

Changes one or more parameters in an existing chart. They must follow the following syntax. ParamName : Value ; ParamName : Value. Valid parameters are Title, TitleX, TitleY, Type, PlotBy. Type posible values are BarClustered, BarStacked, Line, Pie, Area, AreaStacked, XYScatter, ColumnClustered, ColumnStacked. PlotBy posible values are Columns, Rows. Some charts don't support all parameters and therefore the order in which parameters are placed may be relevant.

**Parameters:**
- `chartKey`
- `properties`

**Syntax:**

```
ChangeChartProperties in <chartKey:BarClustered|BarStacked|Line|Pie|Area|AreaStacked|XYScatter|ColumnClustered|ColumnStacked> with {<properties>}
```

**Options:**

- `chartKey`: `BarClustered`, `BarStacked`, `Line`, `Pie`, `Area`, `AreaStacked`, `XYScatter`, `ColumnClustered`, `ColumnStacked`

**Examples:**

```
ChangeChartProperties in graf with {Title: Summary ; titleX: horizontal ; titleY: vertical ; Type: BarClustered ; PlotBy: rows}
ChangeChartProperties in graf with {Title: Invert Summary ; PlotBy: Columns}
ChangeChartProperties in graf with {Type: BarClustered ; titleX: this has X titles}
```

*Added: 2020-Sep-12*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/ChangeChartProperties.pdf)

---

### ChangeChartTable

> Change a given chart's input data.

Changes a given chart's input data. The range can be contiguous or using different columns like A1:A5,D1:D5,G1:E5, the list separator may be different depending on Excel's regional configuration. The source worksheet key reffers to the sheet where the data is taken from.

**Parameters:**
- `chartKey`
- `sourceWorksheetKey`
- `range`

**Syntax:**

```
ChangeChartTable <chartKey> in <sourceWorksheetKey> with range <range>
```

**Examples:**

```
ChangeChartTable totalsChart in WS with range A1:D10
ChangeChartTable chartVar in WS2 with range A1:C11,E1:E11
```

*Added: 2020-Sep-12*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/ChangeChartTable.pdf)

---

### ChangeSeries

> Modify the range for the datasource of a chart in a given sheet.

Modify the range for the datasource of a chart in a given sheet. It will switch column data without changing de number of rows. 
Index starts with 1. NameSerie is the title in the table of the range it belongs to. Range is a positive number, which indicates relative columns forward from the actual column. Direction h stands for horizontal, v for vertical.

**Parameters:**
- `worksheetKey`
- `nameChart`
- `nameSerie`
- `direction`

**Syntax:**

```
ChangeSeries in <worksheetKey> chart <nameChart> the series <nameSerie> with range plus 1 only series <direction:h|v>
```

**Options:**

- `direction`: `h`, `v`

**Examples:**

```
ChangeSeries in hola chart chart1 the series Poblacion with range plus 1 only series h
```

*Added: 2017-Aug-23*

---

### ChangeWSName

> Changes the name of a worksheet.

Changes the name of a worksheet to the one specified (worksheet key is not modified). Consider that the name must be less than 31 characters.

**Parameters:**
- `workbookKey`
- `worksheetKey`
- `actualSheetName`
- `wsName`

**Syntax:**

```
ChangeWSName in {<workbookKey>} worksheet {<actualSheetName>} to {<wsName>}
ChangeWSName in {<workbookKey>} WsKey {<worksheetKey>} to {<wsName>}
```

**Examples:**

```
ChangeWSName in {Libro1} worksheet {Sheet1} to {newName}
ChangeWSName in {Libro1} WsKey {FirstSheet} to {Tablas Consolidadas}
```

*Added: 2019-Nov-26*

---

### ClearCells

> Deletes the contents of a range of cells

Deletes the contents of a range of cells, as if manually selecting a range and deleting. It can be ranges such as A1:B12, A1,lastD or UsedRange. 

**Parameters:**
- `worksheetKey`
- `RangeOrCell`

**Syntax:**

```
ClearCells from {<worksheetKey>} in {<RangeOrCell>}
```

**Examples:**

```
ClearCells from {​​​​​sheet}​​​​​ in {​​​​​A1:LastS}​​​​​
ClearCells from {sheet} in {A9:lastA}
ClearCells from {sheet} in {A6:A9}
```

---

### Close

> Close an open workbook.

Close an existing workbook by a given workbookKey.

**Parameters:**
- `workbookKey`

**Syntax:**

```
Close <workbookKey>
```

**Examples:**

```
Close Libro1
```

*Added: 2019-Feb-27*

---

### ColorDuplicates

> Mark duplicate cells in value with a color.

Apply a color to the duplicate cells in value from a given column. Index starts from 1.

**Parameters:**
- `worksheetKey`
- `index`
- `R`
- `G`
- `B`

**Syntax:**

```
ColorDuplicates from <worksheetKey> column <index> background_values [<R>, <G>, <B>] text_values [<R>, <G>, <B>]
```

**Examples:**

```
ColorDuplicates from hoja2 column 11 background_values [255, 255, 0] text_values [0, 0, 0]
```

*Added: 2018-Mar-02*

---

### ColumnsFit

> Autofit all the columns in the sheet.

Autofit all the columns in the sheet with text in it.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
ColumnsFit in <worksheetKey>
```

**Examples:**

```
ColumnsFit in sheetOne
```

*Added: 2017-Aug-01*

---

### ColumnTransform

> Transforms the given column, from index to Letter vice versa.

Transforms the given column, from index to Letter and vice versa. Values must not exceed the total columns of an Excel Worksheet.

**Parameters:**
- `valueToTransform`
- `varName`
- `filePath`
- `worksheetKey`
- `cellName`

**Syntax:**

```
ColumnTransform value to transform {<valueToTransform>} and save as var {<varName>}
```

**Examples:**

```
ColumnTransform value to transform {AB} and save as var {ColumnIndex}
ColumnTransform value to transform {24} and save as var {ColumnName}
```

*Added: 2022-May-22*

---

### Concatenate

> Concatenate cells values.

Concatenate cell values with a separator between them.

**Parameters:**
- `sheetkey`
- `separatorkey`
- `cell`

**Syntax:**

```
Concatenate in <sheetkey> with "<separatorkey>" [<cell1>,<cell2>,...,<celln>]
Concatenate in <sheetkey> with "<separatorkey>" [<cell1>,<cell2>]
```

**Examples:**

```
Concatenate in ProcessNG with "/" [C11,C12]
```

*Added: 2017-Nov-13*

---

### ConditionalFormat

> Apply format to the cells depending on the condition of each cell value.

Apply format (textcolor, backgroundcolor, borderstyle, bodercolor) depending on the condition (equals, notequals, greater, greaterequals, less, lessequals, between, notbetween) of each cell value. The different types of bordestyle are: dash, dashdot, dashdotdot, dot, double, none, slantdashdot.

**Parameters:**
- `worksheetKey`
- `range`
- `typeofFormat`
- `condition`
- `value`

**Syntax:**

```
ConditionalFormat in <worksheetKey> range <range> format "<typeofFormat:textcolor|backgroundcolor|borderstyle|bodercolor>:<value>" where cell_value <condition:equals|notequals|greater|greaterequals|less|lessequals|between|notbetween> value <value>
ConditionalFormat in <worksheetKey> range <range> format "<typeofFormat:textcolor|backgroundcolor|borderstyle|bodercolor>:<value>" where cell_value between value <value> and <value>
ConditionalFormat in <worksheetKey> used_range format "<typeofFormat:textcolor|backgroundcolor|borderstyle|bodercolor>:<value>" where cell_value <condition:equals|notequals|greater|greaterequals|less|lessequals|between|notbetween> value <value>
ConditionalFormat in <worksheetKey> used_range format "<typeofFormat:textcolor|backgroundcolor|borderstyle|bodercolor>:<value>" where cell_value between value <value> and <value>
ConditionalFormat in <worksheetKey> start_at <startCell> used_range format "<typeofFormat>:<value>" where cell_value <condition> value <value>
```

**Options:**

- `typeofFormat`: `textcolor`, `backgroundcolor`, `borderstyle`, `bodercolor`
- `condition`: `equals`, `notequals`, `greater`, `greaterequals`, `less`, `lessequals`, `between`, `notbetween`
- `typeofFormat`: `textcolor`, `backgroundcolor`, `borderstyle`, `bodercolor`
- `typeofFormat`: `textcolor`, `backgroundcolor`, `borderstyle`, `bodercolor`
- `condition`: `equals`, `notequals`, `greater`, `greaterequals`, `less`, `lessequals`, `between`, `notbetween`
- `typeofFormat`: `textcolor`, `backgroundcolor`, `borderstyle`, `bodercolor`

**Examples:**

```
ConditionalFormat in WSheet2 range A1:D5 format "textcolor:Green" where cell_value equals value OK
ConditionalFormat in Wsheet1 used_range format "backgroundcolor:Red" where cell_value notequals value OK
ConditionalFormat in Wsheet1 range A1:D5 format "borderstyle:dashdotdot" where cell_value between value 100 and 80
```

*Added: 2017-Aug-23*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/AvailableColors.pdf)

---

### ConvertTo2007

> Convert a given Excel file to the computer's Excel version.

Convert a given Excel file to the computer's Excel version.

**Parameters:**
- `workbookKey`

**Syntax:**

```
ConvertTo2007 <workbookKey>
```

**Examples:**

```
ConvertTo2007 book
```

*Added: 2017-Aug-23*

---

### Copy

> Copy values from a worksheet to another one.

Copy values with special considerations in a given worksheet's usedrange and paste it in another one. Range can have values like "lastrow" or the cell where it will be pasted. Typekey can be either all, except_borders, column_widths,comments, formats, formulas,formulas_and_number_formats, validation, values or values_and_number_formats.

**Parameters:**
- `typeKey`
- `worksheetKey`
- `workbookKey`
- `destWorksheetKey`
- `originRange`
- `destRange`
- `transposeValue`

**Syntax:**

```
Copy <typeKey:all|except_borders|column_widths|comments|formats|formulas|formulas_and_number_formats|validation|values|values_and_number_formats> from <worksheetKey> to <workbookKey> sheet_name <destWorksheetKey> start_at <range> transpose <transposeValue:true|false>
Copy <typeKey:all|except_borders|column_widths|comments|formats|formulas|formulas_and_number_formats|validation|values|values_and_number_formats> from_sheet <worksheetKey> to <workbookKey> sheet_name <destWorksheetKey> start_at <originRange> transpose <transposeValue:true|false> paste_in <destRange>
```

**Options:**

- `typeKey`: `all`, `except_borders`, `column_widths`, `comments`, `formats`, `formulas`, `formulas_and_number_formats`, `validation`, `values`, `values_and_number_formats`
- `transposeValue`: `true`, `false`
- `typeKey`: `all`, `except_borders`, `column_widths`, `comments`, `formats`, `formulas`, `formulas_and_number_formats`, `validation`, `values`, `values_and_number_formats`
- `transposeValue`: `true`, `false`

**Examples:**

```
Copy values from sheetOne to bookName sheet_name Sheet1 start_at C1 transpose true
Copy values from sheetOne to bookName sheet_name Sheet1 start_at lastrow transpose false
```

*Added: 2017-Aug-23*

---

### CopyCellUnmerge

> Fill blank cells in a worksheet with the value of the previous row for each column.

Fill blank cells in a worksheet with the value of the previous row for each column.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
CopyCellUnmerge <worksheetKey>
```

**Examples:**

```
CopyCellUnmerge bitacora
```

*Added: 2018-Mar-05*

---

### CopyChart

> Copy a chartIndex to the clipboard.

Copy a given chartIndex in a worksheet to the clipboard. Index starts with 1.

**Parameters:**
- `chartIndex`
- `worksheetKey`

**Syntax:**

```
CopyChart "<chartIndex>" from <worksheetKey>
```

**Examples:**

```
CopyChart "1" from FinancialsWorkSheet
```

*Added: 2018-Jan-30*

---

### CopyColumn

> Copy a column to another column.

Copy a full column to another place (in the same sheet or another), the value indicated after "start at" in the instruction is the offset value, hence if value equals 1, it will be displaced one row, pasting the value in the second row.

**Parameters:**
- `worksheetKeyOrig`
- `worksheetKeyDest`
- `columnIndexOrig`
- `columnIndexDest`
- `rowOffsetOrig`
- `rowOffsetDest`

**Syntax:**

```
CopyColumn <columnIndexOrig> from <worksheetKeyOrig> start_at <rowOffsetOrig> to the sheet <worksheetKeyDest> in column <columnIndexDest> start_at <rowOffsetDest>
CopyColumn <columnIndexOrig> from <worksheetKeyOrig> to the sheet <worksheetKeyDest> in column <columnIndexDest> start_at <rowOffsetDest> --visible
CopyColumn value <columnIndexOrig> from <worksheetKeyOrig> start_at <rowOffsetOrig> to the sheet <worksheetKeyDest> in column <columnIndexDest> start_at <rowOffsetDest>
```

**Examples:**

```
CopyColumn 10 from hoja2 start_at 1 to the sheet hoja3 in column 4 start_at 1
CopyColumn value 20 from hojaCostos start_at 2 to the sheet hoja4 in column 4 start_at 3
```

*Added: 2017-Sep-07*

---

### CopyPaste

> Copies a cell or a range to another location.

Copy a cell or range to another location, just like ctrl + c ctrl + v would. CopyRange can be ranges like A1: B12, A1, lastD, or UsedRange. 
Available types are all, except_borders, column_widths, comments, formats, formulas, formulas_and_number_formats, validation, values, values_and_number_formats, or no type. 
"Optimized" will correct incorrect behavior when using ranges of type of last <Column>.
"Visible" will copy visible items in filtered data, keep in mind that the copyRange is not equal to the number of visible rows.

**Parameters:**
- `worksheetKey`
- `type`
- `worksheetKey2`
- `copyRangeOrCell`
- `pasteCell`
- `isOptimized`
- `isVisible`

**Syntax:**

```
CopyPaste <type:all|except_borders|column_widths|comments|formats|formulas|formulas_and_number_formats|validation|values|values_and_number_formats|> <worksheetKey> <copyRangeOrCell> to <worksheetKey2> <pasteCell> <isOptimized:optimized|> <isVisible:visible|>
```

**Options:**

- `type`: `all`, `except_borders`, `column_widths`, `comments`, `formats`, `formulas`, `formulas_and_number_formats`, `validation`, `values`, `values_and_number_formats`
- `isOptimized`: `optimized`
- `isVisible`: `visible`

**Examples:**

```
CopyPaste hoja1 C9:F18 to hoja2 B3
CopyPaste hoja1 C9 to hoja2 G7
CopyPaste hoja1 UsedRange to hoja2 G7
```

*Added: 2019-May-30*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/automation/ExtraDocsFRIDA/Excel Reader/CopyPaste.pdf)

---

### CopyPivotTable

> Copy a pivot table to the clipboard.

Copy a pivot table from a given worksheet to the clipboard.

**Parameters:**
- `tableName`
- `worksheetKey`

**Syntax:**

```
CopyPivotTable "<tableName>" from <worksheetKey>
```

**Examples:**

```
Excel CopyPivotTable "Tabla dinámica2" from BUWorkSheet
```

*Added: 2017-Aug-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### CopyRange

> Copy a range of cells to somewhere else in the worksheet.

Copy a range of cells to somewhere else in the worksheet, it can be a column for example. Columns and rows indexes begin with 1. LastRow and LastCol will operate according to UsedRange behaviour.

**Parameters:**
- `StartRow`
- `StartCol`
- `EndRow`
- `EndCol`
- `Row`
- `Col`

**Syntax:**

```
CopyRange from the worksheet <worksheetKey> from the cell {<StartRow>,<StartCol>} up to the cell {<EndRow>,<EndCol>} to the cell {<Row>,<Col>}
CopyRange from the worksheet <worksheetKey> from the cell {<StartRow>,<StartCol>} up to the cell {<EndRow>,LastCol} to the cell {LastRow,<Col>}
CopyRange from the worksheet <worksheetKey> from the cell {<StartRow>,<StartCol>} up to the cell {LastRow,<EndCol>} to the cell {<Row>,LastCol}
CopyRange from the worksheet <worksheetKey> from the cell {<StartRow>,<StartCol>} up to the cell {LastRow,LastCol} to the cell {LastRow,LastCol}
```

**Examples:**

```
CopyRange from the worksheet WorkSheetExampleName from the cell {2,5} up to the cell {LastRow,5} to the cell {2,6}
CopyRange from the worksheet WorkSheetExampleName from the cell {2,15} up to the cell {2,LastCol} to the cell {2,LastCol}
CopyRange from the worksheet WorkSheetExampleName from the cell {1,15} up to the cell {LastRow,15} to the cell {LastRow,15}
```

*Added: 2018-Sep-17*

---

### CopyRangeFormat

> Copy the format of a range to use it in another range.

Copy the format of a specific range and paste in another specific range with the same format.

**Parameters:**
- `worksheetKey1`
- `range1`
- `worksheetKey2`
- `range2`

**Syntax:**

```
CopyRangeFormat from sheet <worksheetKey1> with range <range1> to sheet <worksheetKey2> in the range <range2>
```

**Examples:**

```
CopyRangeFormat from sheet WSExampleName1 with range A1,B1 to sheet WSExampleName2 in the range C1,D1
CopyRangeFormat from sheet WSExampleName1 with range A1:A2 to sheet WSExampleName2 in the range C1:C2
CopyRangeFormat from sheet WSExampleName1 with range A1:A2 to sheet WSExampleName2 in the range B1:J1
```

*Added: 2017-Sep-07*

---

### CopySheet

> Copies the contents of a sheet to another one.

Copies the contents of a sheet (by Key) to book (by Key). Index will insert the worksheet at the indicated position of the workbook. If the position is larger, it will be placed at the end. Index is 1-based. Otherwise it will be inserted at the end.

**Parameters:**
- `worksheetKey`
- `workbookKey`
- `sheetPosition`

**Syntax:**

```
(Deprecated) CopySheet <worksheetKey> to <workbookKey> as <worksheetKey>
CopySheet {<worksheetKey>} to {<workbookKey>} as {<worksheetKey>}
CopySheet <worksheetKey> to <workbookKey> in index <sheetPosition> as <worksheetKey>
```

**Examples:**

```
CopySheet {CostWS} to {WBook1} as {CostWS2}
CopySheet CostWS to WBook1 in index 3 as CostWS3
CopySheet CostWS to WBook1 in index end as CostLast
```

*Added: 2017-Aug-01*

---

### CountIf

> Counts how many values of a column occur in another column.

Counts how many a value of col1 occurs in col2. Col1 and col2 indexes start with 1. Resulting count will be placed in colRes. Header will consider the column header.

**Parameters:**
- `worksheetKey`
- `col`
- `index`

**Syntax:**

```
CountIf <worksheetKey1> <col1> start_at <index1> in <worksheetKey2> <col2> start_at <index2> out <colRes>
CountIf <worksheetKey1> header "<colName1>" start_at <index1> in <worksheetKey2> header2 "<colName2>" start_at rowindex <indexB> out <colNameResult>
```

**Examples:**

```
CountIf SheetA 3 start_at 2 in SheetB 3 start_at 2 out 10
CountIf SheetA header "Names" start_at 2 in SheetB header2 "Names" start_at rowindex 2 out Comparativo
```

*Added: 2017-Aug-01*

---

### CountIf2

> Counts how many values of a column occur in another column and are equal to "something".

Counts how many a value of col1 occurs in col2, and are equal to "something" (for now, not a number). Indexes start with 1. Resulting count will be placed in colNameResult. Header will consider the column header.

**Parameters:**
- `worksheetKey1`
- `worksheetKey2`
- `colName1`
- `colName2`
- `colName3`
- `index1`
- `index2`
- `something`
- `colNameResult`
- `col1`
- `colIndex2`
- `col3`
- `colResult`
- `rowIndex`

**Syntax:**

```
CountIf2 <worksheetKey1> <col1> start_at <index1> in <worksheetKey2> <colIndex2> and <col3> equals "<something>" out <colResult>
CountIf2 <worksheetKey1> header "<colName1>" start_at <index1> in <worksheetKey2> header2 "<colName2>" start_at rowindex <rowIndex> and "<colName3>" equals "<something>" out <colNameResult>
```

**Examples:**

```
CountIf2 SheetA 3 start_at 2 in SheetB 2 start_at 2 and 3 equals "Ahorro" out 15
CountIf2 SheetA header "Names" start_at 2 in SheetB header2 "Names" start_at rowindex 2 and "Tipo" equals "Ahorro" out Numero de Cuentas
```

*Added: 2017-Aug-01*

---

### CountSheets

> Count the number of sheets on a given workbook.

Count the number of sheets on a given workbook.

**Parameters:**
- `workbookKey`
- `varName`

**Syntax:**

```
CountSheets From <workbookKey> As <varName>
```

**Examples:**

```
CountSheets From wbClientes As Counter
```

*Added: 2019-Nov-06*

---

### CreateChart

> Insert a chart using a defined source table

Creates a chart using a defined table data and is saved in a given chart variable. Position and dimensions are expressed in pixels. Valid chartTypes are BarClustered, BarStacked, Line, Pie, Area, AreaStacked, XYScatter, ColumnClustered, ColumnStacked. 
Ranges may be expresed as A1:A3,C1:C3, the list separator may be different depending on Excel's regional configuration.

**Parameters:**
- `worksheetKey`
- `sourceWorkSheetKey`
- `range`
- `x`
- `y`
- `width`
- `height`
- `chartType`
- `chartKey`

**Syntax:**

```
CreateChart in <worksheetKey> with table <range> in position {<x>,<y>,<width>,<height>} type <chartType:BarClustered|BarStacked|Line|Pie|Area|AreaStacked|XYScatter|ColumnClustered|ColumnStacked> save as <chartKey>
CreateChart in <worksheetKey> with table <range> from <sourceWorkSheetKey> in position {<x>,<y>,<width>,<height>} type <chartType:BarClustered|BarStacked|Line|Pie|Area|AreaStacked|XYScatter|ColumnClustered|ColumnStacked> save as <chartKey>
```

**Options:**

- `chartType`: `BarClustered`, `BarStacked`, `Line`, `Pie`, `Area`, `AreaStacked`, `XYScatter`, `ColumnClustered`, `ColumnStacked`
- `chartType`: `BarClustered`, `BarStacked`, `Line`, `Pie`, `Area`, `AreaStacked`, `XYScatter`, `ColumnClustered`, `ColumnStacked`

**Examples:**

```
CreateChart in WS with table B1:E11 in position {150,10,500,300} type BarStacked save as graficaKey
CreateChart in WS with table B1:B11,C1:C11,E1:E11 from WS2 in position {150,10,500,300} type Line save as graficaKey
```

*Added: 2020-Sep-12*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/CreateChart.pdf)

---

### CreateDropDown

> Creates a dropdown in a cell with the given information.

Creates a dropdown in the specified cell with the given information, it requires a title to work as the cell's default value

**Parameters:**
- `WsKey`
- `Row`
- `Col`
- `Value1`
- `Value2`
- `Value3`
- `ValueN`
- `Title`

**Syntax:**

```
CreateDropDown in "<WsKey>" in the cell {<Row>,<Col>} with the values {<Value1>,<Value2>,<Value3>....<ValueN>} and the title <Title>
```

**Examples:**

```
CreateDropDown in "MainSheet" in the cell {2,5} with the values {Word,Excel,PowerPoint,Outlook} and the title MicrosoftOffice
```

*Added: 2020-May-06*

---

### CreateHyperlink

> Creates a shortcut to a desired sheet in the same book

Creates a shortcut to a desired sheet in the same book.

**Parameters:**
- `ColRow`
- `TextToDisplay`
- `WsKey`

**Syntax:**

```
CreateHyperlink in sheet <WsKey> cell <ColRow> to the sheet <WsKey> cell <ColRow> and the text to display <TextToDisplay>
```

**Examples:**

```
CreateHyperlink in sheet Sheet1 cell A2 to the sheet Sheet2 cell B20 and the text to display This is a hiperlink
```

*Added: 2020-Oct-23*

---

### CreatePivotTable

> Creates a pivot table using the cached pivot table range.

Creates a pivot table using the cached pivot table range. CellKey indicates where the pivot table will be placed using tableTitle and saving the PivotTableKey variable.

**Parameters:**
- `cacheKey`
- `worksheetKey`
- `cellKey`
- `tableTitle`
- `pivotTableKey`

**Syntax:**

```
CreatePivotTable <cacheKey> in <worksheetKey> cell <cellKey> with_name "<tableTitle>" as <pivotTableKey>
```

**Examples:**

```
CreatePivotTable Cache in PT GE cell A3 with_name "Table" as PivotTable
```

*Added: 2017-Aug-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### CreateTable

> Create a table from an existing range.

Create a table with a given range. 
When specifing a range, A1:B2 style is accepted, also A1:lastF or with UsedRange. Table may have it's own headers in the first row, hasHeader can use Y or N to indicate this.

**Parameters:**
- `tableName`
- `worksheetKey`
- `range`
- `hasHeader`

**Syntax:**

```
CreateTable {<tableName>} in worksheet {<worksheetKey>} with range {<range>} has headers {<hasHeaders:Y|N>}
```

**Options:**

- `hasHeaders`: `Y`, `N`

**Examples:**

```
CreateTable {TableInvoice} in worksheet {WSExampleName} with range {A1:J10} has headers {Y}
```

*Added: 2025-Feb-18*

---

### CustomSort

> Sort by many Columns.

Sort by many Columns. 
The range may be in the style of A1:B2, also A1:lastF or with UsedRange.
 Relative columns means that for a range D1:F10, column 1 is D, column 2 is E, and so on. Order values can be asc, desc for ascending or descending order. If you want to use a custom list, it must be enclosed with double quotes. 
If match case is false, the text's casing will not be considered. Data will be sorted considering existing headers.

**Parameters:**
- `worksheetKey`
- `range`
- `col`
- `ascOrDesc`
- `case`

**Syntax:**

```
CustomSort in <worksheetKey> with range {<range>} relative columns [<col1>,<col2>,...<coln>] order [<ascOrDesc1>,<ascOrDesc2>,...<ascOrDescn>] match case {<case:Yes|No>}
```

**Options:**

- `case`: `Yes`, `No`

**Examples:**

```
CustomSort in WSName1 with range {UsedRange} relative columns [1,4,6] order [asc,desc,desc] match case {Yes}
CustomSort in WSName1 with range {D1:lastG} relative columns [1,2] order [asc,asc] match case {No}
CustomSort in WSName1 with range {A1:F10} relative columns [1,2] order ["com,net,org",asc] match case {No}
```

*Added: 2023-Feb-22*

---

### DataSortByColumn

> Sort a column from a given worksheet.

Sort a column from a given worksheet. When a range is used, sorting a column considers the rest of cells to be related, and those cells will be moved according to the sorted column. Index begins with 1. Selecting "Y" in header means that it will affect the header with all data.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `range`
- `sortOption`

**Syntax:**

```
DataSortByColumn {<worksheetKey>} by_column {<columnIndex>} with_header {<sortOption:Y|N>}
DataSortByColumn {<worksheetKey>} by_column {<columnIndex>} range {<range>} with_header {<sortOption:Y|N>}
```

**Options:**

- `sortOption`: `Y`, `N`
- `sortOption`: `Y`, `N`

**Examples:**

```
DataSortByColumn {hoja} by_column {3} with_header {Y}
DataSortByColumn {hoja} by_column {5} range {A589:Z1080} with_header {N}
```

*Added: 2019-Oct-18*

---

### DateFormat

> Change date formats in a column.

The simple syntax converts requires that all values in a cell are dates, and it changes it's format to yyyyMMdd. Column index begins with 1. The string syntax converts all the dates to dateFormatOutput, if the cell is Text format, it will only change those with source format indicated, otherwise it will format all dates. Source format can be "unknown" and will only consider dates with default format (culture specific).

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `currentDateFormat`
- `dateformatOutput`
- `worksheetKey`
- `colIndex`
- `rowIndex`
- `varkey`

**Syntax:**

```
DateFormat in <worksheetKey> in column <columnIndex>
DateFormat <worksheetKey> column_index <columnIndex> source "<currentDateFormat>" string("<dateformatOutput>")
```

**Examples:**

```
DateFormat in Sheet1 in column 6
DateFormat hoja column_index 2 source "dd-MM-yyyy" string("dd.MM.yy")
DateFormat hoja column_index 2 source "unknown" string("dd.MM.yy")
```

*Added: 2017-Aug-01*

---

### DateFormat2SC

> Change the date format of a column to yyyymmdd.

Convert the date format to yyyymmdd in a given column name.

**Parameters:**
- `worksheetKey`
- `headerName`

**Syntax:**

```
DateFormat2SC in <worksheetKey> in column <headerName>
```

**Examples:**

```
DateFormat2SC in Sheet4 in column Fechas
```

*Added: 2017-Oct-13*

---

### Dateformat3

> Change the date format of a column to DD.MM.yyyy.

Adds a dateformat DD.MM.yyyy to a given column.

**Parameters:**
- `worksheetKey`
- `indexColumn`

**Syntax:**

```
Dateformat3 in <worksheetKey> in column <indexColumn>
```

**Examples:**

```
Dateformat3 in sheet in column 3
```

*Added: 2017-Nov-13*

---

### DateMathOperation

> Make a math operation between two columns with dates and write the result on a third column.

Make a math operation between two columns and write the result on a third column. Format parameter indicates the format of dates in all columns. Currently dates in both columns must be text format. "Applying filter" syntax is used to perform the action in the values where the output column has "-1" in each cell.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `language`
- `format`

**Syntax:**

```
DateMathOperation from the worksheet <worksheetKey> on ColumnIndex1 {<columnIndex1>} - ColumnIndex2 {<columnIndex2>} languageDate {<language>} format {<format>} write on ColumnIndex3 {<columnIndex3>}
DateMathOperation from the worksheet <worksheetKey> on ColumnIndex1 {<columnIndex1>} - ColumnIndex2 {<columnIndex2>} languageDate {<language>} format {<format>} write on ColumnIndex3 {<columnIndex3>} applying the filter -1
```

**Examples:**

```
DateMathOperation from the worksheet WorkSheetName ColumnIndex1 {2} - ColumnIndex2 {3} languageDate {en-CA} format {d.M.yyyy} write on ColumnIndex3 {4}
DateMathOperation from the worksheet WorkSheetName ColumnIndex1 {2} - ColumnIndex2 {3} languageDate {en-CA} format {d.M.yyyy} write on ColumnIndex3 {4} applying the filter -1
```

*Added: 2018-Sep-17*

---

### DebugVariables

> Print the Turing Excel variables to the log file.

Print the Turing Excel variables to the log file.

**Syntax:**

```
DebugVariables
```

**Examples:**

```
DebugVariables
```

*Added: 2021-May-24*

---

### DeleteAll

> Delete all data from the worksheet.

Delete all data from the worksheet. The option to include images is optional

**Parameters:**
- `worksheetKey`

**Syntax:**

```
DeleteAll from <worksheetKey>
DeleteAll from <worksheetKey> including images
```

**Examples:**

```
DeleteAll from Sheet3
DeleteAll from Sheet1 including images
```

*Added: 2018-Mar-02*

---

### DeletePivotTable

> Delete an existing Pivot Table.

Delete a specific Pivot Table by key or name of the Pivot Table. It can also delete all pivot tables in a given worksheet or workbook.

**Parameters:**
- `pivottableKey`
- `pivottableName`
- `workbookKey`
- `worksheetKey`

**Syntax:**

```
DeletePivotTable by key {<pivottableKey>}
DeletePivotTable from {<workbookKey>} by name {<pivottableName>}
DeletePivotTable all from worksheet {<worksheetKey>}
DeletePivotTable all from workbook {<workbookKey>}
```

**Examples:**

```
DeletePivotTable by key {PT1}
DeletePivotTable from {Wbook1} by name {PivotTable1}
DeletePivotTable all from worksheet {sheet3}
```

*Added: 2019-Jun-17*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### DeletePrevMonth

> Delete all rows that have a date from last n months.

Delete all rows that have a date lower than "01/current month minus numberMonths/current year". Column index indicates the column that will be compared. Row index indicates where the filter will start comparing, when it has 1, first row is the column title and it will delete the following rows. When row is 2, it assumes title is in row 2.

**Parameters:**
- `worksheetKey`
- `numberMonths`
- `rowIndex`
- `columnIndex`

**Syntax:**

```
DeletePrevMonth from <worksheetKey> amount <numberMonths> row <rowIndex> column <columnIndex>
```

**Examples:**

```
DeletePrevMonth from libro amount 2 row 2 column 3
DeletePrevMonth from libro amount 3 row 1 column 6
```

*Added: 2018-Mar-02*

---

### DeleteRows

> Delete all rows in a given sheet.

Delete all rows in a given sheet. It may be indicated to delete all rows or background coloured cells in A column, or rows where a cell contains a given value (Currently, only "start at" syntax can read numbers, others must be text format cells).
Conditions syntax can compare exact values or only contain a part of the constraint. 
When looking to delete multiple constraints in one column syntax can be "A":"constraint1|constraint2" to delete all rows where column A has either "constraint1" or "constraint2" in their values.

**Parameters:**
- `searchType`
- `type`
- `worksheetKey`
- `columnIndex`
- `rowIndex`
- `column1`
- `conditions1`
- `column2`
- `conditions2`
- `caseSensitive`
- `compareType`
- `value`

**Syntax:**

```
DeleteRows <type:Colored|All> from_sheet <worksheetKey>
DeleteRows Cond <searchType:Contains|All> Value "<value>" Column <columnIndex> from_sheet <worksheetKey>
DeleteRows Cond Contains Value "<value>" Column <columnIndex> start at <rowIndex> from_sheet <worksheetKey>
DeleteRows from <worksheetKey> with <compareType:exact|> conditions {"<column1>":"<conditions1>";"<column2>":"<conditions2>"} <caseSensitive:ignore case|>
```

**Options:**

- `type`: `Colored`, `All`
- `searchType`: `Contains`, `All`
- `compareType`: `exact`
- `caseSensitive`: `ignore case`

**Examples:**

```
DeleteRows All from_sheet mySheet
DeleteRows Colored from_sheet mySheet
DeleteRows Cond Contains Value "0" Column 2 from_sheet mySheet
```

*Added: 2018-Jun-20*

---

### DeleteValue

> Delete all repetitions of a value from a column.

Delete all repetitions of a value from a column. ColIndex starts with 1.

**Parameters:**
- `worksheetKey`
- `colIndex`
- `value`

**Syntax:**

```
DeleteValue <worksheetKey> col_index {<colIndex>} value "<value>"
```

**Examples:**

```
DeleteValue Hoja col_index {3} value "0"
```

*Added: 2019-May-23*

---

### Dispose

> Close Excel without saving any changes.

Closes, without saving changes, all open Excel workbooks and kills all the Excel tasks on the computer unless just a specific WorkBook is specified.

**Parameters:**
- `workbookKey`

**Syntax:**

```
Dispose
Dispose <workbookKey>
```

**Examples:**

```
Dispose
Dispose WSLogWorkBook
```

*Added: 2019-Dec-17*

---

### EditLinks

> Change the source links in a workbook.

Changes the first source links in a workbook. If the workbook has more than one asociated source, "previous link" can specify the link to be edited. The new source, must have the same worksheet names indicated by the links.

**Parameters:**
- `workbookKey`
- `path`
- `previousPath`

**Syntax:**

```
EditLinks from {<workbookKey>} with file "<path>"
EditLinks from {<workbookKey>} with file "<path>" previous link "<previousPath>"
```

**Examples:**

```
EditLinks from {WBook} with file "C:\input\source.xlsx"
EditLinks from {WBook} with file "C:\input\source-June.xlsx" previous link "C:\input\source-May.xlsx"
```

*Added: 2020-Jul-13*

---

### ExcludeFilterValues

> Filter a column excluding certain values.

Allows to filter a column excluding desired values. Indexes start with 1.

**Parameters:**
- `worksheetKey`
- `rowIndex`
- `columnIndex`
- `criteria`

**Syntax:**

```
ExcludeFilterValues from {<worksheetKey>} start_at {<rowIndex>} at_column {<columnIndex>} exclude criteria [<criteria1>, <criteria2>,...,<criteriaN>]
ExcludeFilterValues from {<worksheetKey>} start_at {<rowIndex>} at_column {<columnIndex>} exclude_criteria_start_with [<criteria1>, <criteria2>,...,<criteriaN>]
```

**Examples:**

```
ExcludeFilterValues from {hoja} start_at {2} at_column {5} exclude criteria [Pago con pagos exprés, Pago Móvil, Pago General]
ExcludeFilterValues from {hoja} start_at {2} at_column {5} exclude_criteria_start_with [SCOT, SANTA, BANCOM]
```

*Added: 2019-Sep-24*

---

### ExportChart

> Exports all charts images to the given path.

Exports all charts in a book or a sheet as images to the given path.

**Parameters:**
- `workbookKey`
- `worksheetKey`
- `workbookIndex`
- `worksheetIndex`
- `saveDirectoryPath`

**Syntax:**

```
ExportChart in book "<workbookKey>" to "<saveDirectoryPath>"
ExportChart in sheet "<worksheetKey>" to "<saveDirectoryPath>"
```

**Examples:**

```
ExportChart in book "book1" to "C:\Users\user.name\Downloads"
ExportChart in sheet "sheetname" to "C:\Users\user.name\Downloads"
```

*Added: 2017-Aug-23*

---

### ExportImage

> Export a range of cells as an image.

Export a range of cells as an image. You can used the keywords "LastRow" and "LastCol" to selct all the cells active in those row and columns 

**Parameters:**
- `worksheetKey`
- `StartRow`
- `StartCol`
- `EndRow`
- `EndCol`
- `ImagePath`

**Syntax:**

```
ExportImage from the worksheet <worksheetKey> from the cell {<StartRow>,<StartCol>} up to the cell {<EndRow>,<EndCol>} and save in the file "<ImagePath>"
```

**Examples:**

```
ExportImage from the worksheet Hoja1 from the cell {1,2} up to the cell {LastRow,LastCol} and save in the file "C:\Users\Innovation\Desktop\TuringExpo\Local\screenshots\CaptureImage.png"
```

*Added: 2020-Apr-27*

---

### ExportXML

> Export the previously loaded XML with filled in data from the worksheet.

After loading a schema to excel and binding cells to it. The function will export the correspondig XML with filled in data. When XML is baddly built or fields are not well binded, for further support refer to: https://support.microsoft.com/en-us/office/export-xml-data-0b21f51b-56d6-48f0-83d9-a89637cd4360?ocmsassetid=hp010206401&correlationid=abe81eda-43d6-45a7-afa7-76733b2a5ba4&ui=en-us&rs=en-us&ad=us#BM3

**Parameters:**
- `workbookKey`
- `outputXMLpath`

**Syntax:**

```
ExportXML from <workbookKey> to "<outputXMLpath>"
```

**Examples:**

```
ExportXML from wbFacturas to "C:\salida\facturas2020Jun.xml"
```

*Added: 2020-Jun-19*

---

### FieldLength

> Fills the values in a given column with a character.

Fills the values in a given column with a character. It can be added either before or after de cell's value. For example "limit 5 start_at 2 filltxt '-' before" will output "--abc" in "abc", but leave "abcde" as it is. 

**Parameters:**
- `worksheetKey`
- `colindex`
- `lenght`
- `rowindex`
- `fillType`
- `header`
- `char`
- `position`

**Syntax:**

```
FieldLength <worksheetKey> col_index <colIndex> limit <length> start_at <rowIndex>
FieldLength <worksheetKey> col_index <colIndex> limit <length> start_at <rowIndex> <fillType:fillnum|filltxt> '<char>' <position:before|after>
FieldLength <worksheetKey> col_index <colIndex> limit <length> start_at <rowIndex> <fillType1:fillnum|filltxt> '<char1>' <position1:before|after> <fillType2:fillnum|filltxt> '<char2>' <position2:before|after>
FieldLength <worksheetKey> col_header "<header>" limit <length> start_at <rowIndex>
FieldLength <worksheetKey> col_header "<header>" limit <length> start_at <rowIndex> <fillType:fillnum|filltxt> '<char>' <position:before|after>
FieldLength <worksheetKey> col_header "<header>" limit <length> start_at <rowIndex> <fillType1:fillnum|filltxt> '<char1>' <position1:before|after> <fillType2:fillnum|filltxt> '<char2>' <position2:before|after>
```

**Options:**

- `fillType`: `fillnum`, `filltxt`
- `position`: `before`, `after`
- `fillType1`: `fillnum`, `filltxt`
- `position1`: `before`, `after`
- `fillType2`: `fillnum`, `filltxt`
- `position2`: `before`, `after`
- `fillType`: `fillnum`, `filltxt`
- `position`: `before`, `after`
- `fillType1`: `fillnum`, `filltxt`
- `position1`: `before`, `after`
- `fillType2`: `fillnum`, `filltxt`
- `position2`: `before`, `after`

**Examples:**

```
FieldLength wsheet1 col_index 3 limit 5 start_at 2
FieldLength wsheet1 col_index 3 limit 5 start_at 2 filltxt '-' after
FieldLength wsheet1 col_header "People" limit 6 start_at 2 filltxt 'a' before
```

*Added: 2017-Nov-14*

---

### Filter

> Filter a column using the mentioned criteria.

Filters a given column by key within the used range, using the mentioned criteria.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `criteria`

**Syntax:**

```
Filter in <worksheetKey> in column <columnIndex> with criteria <criteria>
```

**Examples:**

```
Filter in Sheet1 in column 5 with criteria Comprado
```

*Added: 2017-Aug-01*

---

### Filter2

> Filter a column by name using the mentioned criteria.

Filters a given column by name within the used range, using the mentioned criteria.

**Parameters:**
- `worksheetKey`
- `header`
- `criteria`

**Syntax:**

```
Filter in <worksheetKey> in column <header> with criteria <criteria>
```

**Examples:**

```
Filter in Sheet2 in column Clientes with criteria HEB
```

*Added: 2017-Aug-01*

---

### FilterHeader

> Filter a given column that matches the criteria.

Adds a filter in a given column that matches the criteria. Index begins with 1. Criteria can have wildcards (*?). A given range can be clearly specified, to stop Excel from guessing the range it will filter.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `criteria`
- `range`

**Syntax:**

```
FilterHeader {<worksheetKey>} column_index {<columnIndex>} criteria {<criteria>}
FilterHeader {<worksheetKey>} column_index {<columnIndex>} range {<range>} criteria {<criteria>}
```

**Examples:**

```
FilterHeader {hojaWS} column_index {4} criteria {PAID}
FilterHeader {hojaWS} column_index {4} criteria {Mar*}
FilterHeader {hojaWS} column_index {6} range {A1:L1} criteria {REJECTED}
```

*Added: 2019-Nov-14*

---

### FilterOff

> Remove filters.

Set the filter off in a worksheet.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
FilterOff in {<worksheetKey>}
```

**Examples:**

```
FilterOff in {banca}
```

*Added: 2019-Oct-18*

---

### FilterPivotTableSlicer

> Select items from a pivot table slicer.

Select items from a pivot table slicer. Check the extra docs to know how to find the slicerName.

**Parameters:**
- `pivotTableKey`
- `slicerName`
- `criteria`

**Syntax:**

```
FilterPivotTableSlicer in pivot table key {<pivotTableKey>} to slicer {<slicerName>} with the criteria {<criteria1>;<criteria2>;...<criteriaN>}
```

**Examples:**

```
FilterPivotTableSlicer in pivot table key {PTKey} to slicer {Cities} with the criteria {London;Mexico;New York;Paris}
```

*Added: 2023-Dec-04*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### FindRow

> Get the row index after searching for a value

Search for the exact word occurrence in a given column, this words may use * at the start, end, or both sides to indicate a word ending with, begining with o that it is in the middle. Order values can be "first|last". 
Use start_at to indicate where the search row begins.
 If the word is not found it won't raise an exception, it will just not update the variable. Column index is 1-based.  

**Parameters:**
- `worksheetKey`
- `order`
- `word`
- `columnIndex`
- `rowIndex`
- `variableKey`

**Syntax:**

```
FindRow from {<worksheetKey>} <order:first|last> occurrence of {<word>} in column {<columnIndex>} as {<variableKey>}
FindRow from {<worksheetKey>} <order:first|last> occurrence of {<word>} in column {<columnIndex>} start_at {<rowIndex>} as {<variableKey>}
```

**Options:**

- `order`: `first`, `last`
- `order`: `first`, `last`

**Examples:**

```
FindRow from {hoja} first occurrence of {*Abril*} in column {5} as {IndMesActual}
FindRow from {hoja} first occurrence of {Success} in column {2} as {Existoso}
FindRow from {hoja} last occurrence of {BANC*} in column {2} start_at {7} as {Bancos}
```

*Added: 2020-Dec-14*

---

### FixUsedRange

> Delete empty rows from a sheet's used range.

Delete empty rows from a sheet's used range. An used range are the cells with data or a format set. When you press Ctrl+end you will notice if there are many empty rows that shouldn't be taken into account for operations. Note: After using FixUsedRange, Excel will recognize the new size of UsedRange after you save the workbook, so it is recomended to execute SaveWB after using this function.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
FixUsedRange from {<worksheetKey>}
```

**Examples:**

```
FixUsedRange from {sheetVar}
```

*Added: 2023-Aug-01*

---

### FormatExcelDate

> Convert an Excel date to another format

Change the format of an Excel's numeric date and save the value in a varable

**Parameters:**
- `excelNumericDate`
- `formatString`
- `varKey`

**Syntax:**

```
FormatExcelDate {<excelNumericDate>} to format {<formatString>} as {<varKey>}
```

**Examples:**

```
FormatExcelDate {20115} to format {dd-MM-yyyy} as {formatedDate}
```

*Added: 2022-Sep-29*

---

### FreezePane

> Freeze a row to make it visible all the time.

Freeze a row or column to make it visible all the time. To unfreeze rows/columns, use -1 as the index. Index start from 1.

**Parameters:**
- `worksheetKey`
- `rowIndex`
- `columnIndex`

**Syntax:**

```
FreezePane {<worksheetKey>} in_row {<rowIndex>}
FreezePane {<worksheetKey>} in_column {<columnIndex>}
```

**Examples:**

```
FreezePane {MyWorksheet} in_row {2}
FreezePane {MyWorksheet} in_column {2}
FreezePane {MyWorksheet} in_row {-1}
```

*Added: 2019-Sep-18*

---

### GetCellValue

> Get the value of a cell and save it in a variable.

Get the value of a single cell and save as a variable. Column and Row indexes start from 1.

**Parameters:**
- `worksheetKey`
- `cellName`
- `columnIndex`
- `rowIndex`
- `varName`

**Syntax:**

```
GetCellValue from the worksheet <worksheetKey> in cell {<columnIndex>,<rowIndex>} and save as <varName>
GetCellValue from the worksheet <worksheetKey> in column {<columnIndex>} and row {<rowIndex>} and save as <varName>
```

**Examples:**

```
GetCellValue from the worksheet WorkSheetName in cell {1,2} and save as promedio
GetCellValue from the worksheet WorkSheetName in column {5} and row {7} and save as constante
```

*Added: 2019-Jan-07*

---

### GetLastRow

> Find the last row with data in a column.

Find the last row with data in a column and save it in a given variable. Index is 1-based

**Parameters:**
- `worksheetKey`
- `columnNumberOrLetter`
- `variableName`

**Syntax:**

```
GetLastRow from {<worksheetKey>} in column {<columnNumberOrLetter>} and save as {<variableName>}
```

**Examples:**

```
GetLastRow from {sheetVar} in column {4} and save as {lastRow}
GetLastRow from {sheetVar} in column {WD} and save as {lastRowWD}
```

*Added: 2023-Aug-02*

---

### GetPivotTableNames

> Get a list of the pivot table names in a sheet.

Get the names of the pivot tables in a given sheet and save it in a list variable. If there are no pivot tables in the sheet, the list will be empty.

**Parameters:**
- `worksheetKey`
- `variableName`

**Syntax:**

```
GetPivotTableNames from {<worksheetKey>} and save as <variableName>
```

**Examples:**

```
GetPivotTableNames from {ws} and save as ptNames
```

*Added: 2023-Jun-12*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### GetSheetName

> Save the name of a worksheet in a variable.

Saves the name of a given worksheetKey in a variable.

**Parameters:**
- `worksheetKey`
- `VarName`

**Syntax:**

```
GetSheetName From <worksheetKey> As <VarName>
```

**Examples:**

```
GetSheetName From HistorialWS As sName
```

*Added: 2019-Nov-06*

---

### GetSheetNames

> Get a list of the sheet names in a book.

Get the names of the sheets in a given book and save it in a list variable. If there are no sheets, the list will be empty.

**Parameters:**
- `workbookKey`
- `variableName`

**Syntax:**

```
GetSheetNames from {<workbookKey>} and save as <variableName>
```

**Examples:**

```
GetPivotTableNames from {theBook} and save as ptNames
```

*Added: 2023-Jun-12*

---

### GetSpecial

> Get the location of a cell indicated by "special" identifiers like lastCell.

Saves in a variable, the index of a column or row where a given instruction is found. Instruction can be lastRow, lastVisibleRow, lastCell, lastVisibleCell, visibleCellsCount, visibleCells. 

It can find the first or last ocurrence of a word in a column, either reading from top to bottom or the other way around.
VisibleRows Syntax will return a list of visible rows
 Syntax finding occurrences uses regex, so escaped characters are valid as well as regexSyntax. Backslash must be escaped with \\.

**Parameters:**
- `worksheetKey`
- `occurrence`
- `instruction`
- `variableKey`
- `rowIndex`
- `columnIndex`
- `word`
- `startOrder`

**Syntax:**

```
GetSpecial <instruction:lastRow|lastCol|lastCell|lastVisibleRow|lastVisibleCol|lastVisibleCell|visibleCellsCount|visibleRows> from <worksheetKey> and save as <variableKey>
GetSpecial {<worksheetKey>} appearance {<occurrence:first|last>} of {<word>} in_index_column {<columnIndex>} and_save_as {<variableKey>} none
GetSpecial {<worksheetKey>} appearance {<occurrence:first|last>} of {<word>} in_index_column {<columnIndex>} and_save_as {<variableKey>} start_at {<rowIndex>}
GetSpecial {<worksheetKey>} column {<columnIndex>} row_appear_start_with {<word>} save_as {<variableKey>} <startOrder:none|reverse>
```

**Options:**

- `instruction`: `lastRow`, `lastCol`, `lastCell`, `lastVisibleRow`, `lastVisibleCol`, `lastVisibleCell`, `visibleCellsCount`, `visibleRows`
- `occurrence`: `first`, `last`
- `occurrence`: `first`, `last`
- `startOrder`: `none`, `reverse`

**Examples:**

```
GetSpecial lastRow from wsheet and save as LRow
GetSpecial lastCol from wsheet and save as LCol
GetSpecial lastCell from wsheet and save as LCell
```

*Added: 2019-May-10*

---

### GetTableNames

> Get a list of the table names in a sheet.

Get the names of the tables in a given sheet and save it in a list variable. If there are no tables in the sheet, the list will be empty.

**Parameters:**
- `worksheetKey`
- `variableName`

**Syntax:**

```
GetTableNames from {<worksheetKey>} and save as <variableName>
```

**Examples:**

```
GetTableNames from {ws} and save as tableNames
```

*Added: 2023-Jun-12*

---

### GetUnique

> Saves in a variable a list of unique values in a given column.

Saves in a variable a list of unique values in a given column. Start_at is the row where the table's name is. Indexes start with 1 except first syntax, where "start_at" begins from 0. Col_header option looks for the name of the given column.

**Parameters:**
- `worksheetKey`
- `index`
- `header`
- `colIndex`
- `colHeader`
- `rowIndex`
- `variableName`

**Syntax:**

```
GetUnique values from "<worksheetKey>" col_index "<index>" start_at <rowIndex> as <variableName>
GetUnique values from "<worksheetKey>" col_header "<header>" start_at <rowIndex> as <variableName>
GetUnique values from {<worksheetKey>} col_index {<colIndex>} start_at {<rowIndex>} as {<variableName>} filter
```

**Examples:**

```
GetUnique values from "Sheet2" col_index "3" start_at 2 as promedios
GetUnique values from "wsheetA" col_header "Promedios Totales" start_at 2 as promedios
GetUnique values from {hoja} col_index {2} start_at {7} as {etiquetas} filter
```

*Added: 2017-Aug-23*

---

### GetXSD

> Extract the schema from a previously loaded XML in excel.

When an XML was loaded to the excel, excel autobuilds the corresponding schema. This schema may not include all the validation rules desired. This function can be used for schema analysis and improvement, before setting a final xsd to be loaded to Excel.

**Parameters:**
- `workbookKey`
- `path`

**Syntax:**

```
GetXSD from <workbookKey> to "<path>"
```

**Examples:**

```
GetXSD from wbLibro to "C:\templates\facturasSchema.xsd"
```

*Added: 2020-Jun-19*

---

### GoToCell

> Move the active cell to a given a sheet.

Move the active cell to a given a sheet and a cell range. The cell can be either a single one like A4 or a range such as A1:B3.

**Parameters:**
- `wsName`
- `cellName`

**Syntax:**

```
GoToCell {<wsName>} cell {<cellName>}
```

**Examples:**

```
GoToCell {miHoja} cell {G5}
GoToCell {miHoja} cell {G5:K10}
```

*Added: 2019-Dec-10*

---

### GroupRange

> Groups a range of rows or columns.

Groups a range of rows or columns. For the rows it is only needed the numbers. For the columns, it must be specified the first cell of each column.

**Parameters:**
- `orientation`
- `worksheetKey`
- `firstCell`
- `lastCell`

**Syntax:**

```
GroupRange <orientation:rows|cols> in <worksheetKey> range <firstCell>:<lastCell>
```

**Options:**

- `orientation`: `rows`, `cols`

**Examples:**

```
GroupRange rows in sheet range 5:10
GroupRange cols in sheet range c1:e1
```

*Added: 2020-Aug-26*

---

### Hide

> Hide one or more rows or columns in a sheet.

Hide one or more rows or columns in a sheet.

**Parameters:**
- `worksheetKey`
- `index`

**Syntax:**

```
Hide from <worksheetKey> at columns [<index1>,<index2>,...,<indexN>]
Hide from <worksheetKey> at rows [<index1>,<index2>,...,<indexN>]
```

**Examples:**

```
Hide from hoja1 at columns [3,4,8,10]
Hide from WSheet1 at rows [3,4]
```

*Added: 2023-Nov-29*

---

### IfColExists

> Ensures that a column header exists.

Ensures that a column header exists, if false inserts the column in a given index.

**Parameters:**
- `worksheetKey`
- `headerName`
- `newcolIndex`

**Syntax:**

```
IfColExists <worksheetKey> "<headerName>" <newcolIndex>
```

**Examples:**

```
IfColExists WSheetA "Totales" 20
```

*Added: 2017-Aug-01*

---

### IfContains

> Looks for all ocurrences of a value in a column and changes the value in another column.

Looks for all ocurrences of a given value in columnSearch, it may be a substring. If found, it copies the contents of the row from columnPaste to columnCopy. Valid column names must be placed.

**Parameters:**
- `worksheetKey`
- `columnSearchHeader`
- `columnCopyHeader`
- `columnPasteHeader`
- `value`

**Syntax:**

```
IfContains <worksheetKey> "<columnSearchHeader>" value "<value>" then set "<columnCopyHeader>" value "<columnPasteHeader>"
```

**Examples:**

```
IfContains SheetA "Status" value "OK" then set "Total" value "Approved"
IfContains SheetA "Concept" value "Impuesto" then set "Import" value "Deductions"
```

*Added: 2017-Aug-01*

---

### IfEmpty

> Fill empty values in a column.

In the column index fill every cell that is empty with a value, all within the used range of cells. Indexes are 1-based.

**Parameters:**
- `worksheetKey`
- `colIndex`
- `rowIndex`
- `value`

**Syntax:**

```
IfEmpty {<worksheetKey>} col_index {<colIndex>} put {<value>} start at {<rowIndex>}
(deprecated)IfEmpty <worksheetKey> col_index {<colIndex>} put "<value>"
```

**Examples:**

```
IfEmpty {Hoja} col_index {3} put {0} start at {1}
```

*Added: 2019-May-23*

---

### ImportImage

> Import an image to a specific position.

Import an image in an excel file in a specific position.

**Parameters:**
- `ImagePath`
- `worksheetKey`
- `Cell`
- `Row`
- `Column`

**Syntax:**

```
ImportImage from "<ImagePath>" in the worksheet "<worksheetKey>" in the cell "<Cell>"
ImportImage from "<ImagePath>" in the worksheet "<worksheetKey>" in the row "<Row>" and in the column "<Column>"
```

**Examples:**

```
ImportImage from "C:\Users\Innovation\Desktop\TuringExpo\Local\screenshots\CaptureImage.png" in the worksheet "WS" in the cell "B3"
ImportImage from "C:\Users\Innovation\Desktop\TuringExpo\Local\screenshots\CaptureImage.png" in the worksheet "WS" in the row "4" in the column "2"
```

*Added: 2017-Aug-01*

---

### InsertCol

> Insert a Column to the worksheet.

Inserts a Column at index (1-based).

**Parameters:**
- `worksheetKey`
- `colIndex`

**Syntax:**

```
InsertCol in <worksheetKey> at <colIndex>
```

**Examples:**

```
InsertCol in Sheet1 at 6
```

*Added: 2017-Aug-01*

---

### InsertRow

> Insert a Row to the worksheet.

Inserts a Row at index (1-based).

**Parameters:**
- `worksheetKey`
- `rowIndex`

**Syntax:**

```
InsertRow in <worksheetKey> at <rowIndex>
```

**Examples:**

```
InsertRow in Sheet4 at 6
```

*Added: 2017-Aug-01*

---

### IsRegexMatch

> Not working yet. Check for regex matches.

Not working yet. Check if a cell's value matches the given regex. Functions may be ActualValue, ActualRow or excelium functions.

**Parameters:**
- `regex`
- `worksheetKey`
- `colindex`
- `colheader`
- `value`
- `functions`

**Syntax:**

```
IsRegexMatch "regex" in sheet <worksheetKey> in columns [<colindex>]
IsRegexMatch "regex" in sheet <worksheetKey> in headers [<colheader>]
IsRegexMatch "regex" in sheet <worksheetKey> in columns [<colindex>] else value "<value>"
IsRegexMatch "regex" in sheet <worksheetKey> in headers [<colheader>] else value "<value>"
IsRegexMatch "regex" in sheet <worksheetKey> in columns [<colindex>] else functions [<functions>]
IsRegexMatch "regex" in sheet <worksheetKey> in headers [<colheader>] else functions [<functions>]
```

**Examples:**

```
IsRegexMatch "([0-9]+)(?!mm)" in sheet Sheet1 in columns [3]
IsRegexMatch "[0-9]+" in sheet WSheet2 in headers [Fechas]
IsRegexMatch "([0-9]+)(?!mm)" in sheet SheetA in columns [4] else value "No coincide"
```

*Added: 2017-Nov-13*

---

### IsSheetVisible

> Show the visibility status in a given sheet.

Get the visibility status of a given sheet. The result is stored as true/false in a variable.

**Parameters:**
- `worksheetKey`
- `variableName`

**Syntax:**

```
IsSheetVisible with name {<worksheetKey>} and save as <variableName>
```

**Examples:**

```
IsSheetVisible with name {theHiddenOne} and save as isVisible
```

*Added: 2023-Jun-05*

---

### KeepCols

> Deletes all columns except those specified by a given index.

Deletes all columns except those specified by a given index. Indexes begin with 1.

**Parameters:**
- `worksheetKey`
- `index`

**Syntax:**

```
KeepCols from <worksheetKey> at [<index1>,<index2>,...,<indexN>]
```

**Examples:**

```
KeepCols from WSheet1 at [3,4,7]
```

*Added: 2017-Aug-01*

---

### KeepColsHeaders

> Deletes all columns except those specified by Name.

Deletes all columns except those specified by Name. It is case sensitive. Currently all columns must have a header for it to work correctly.

**Parameters:**
- `worksheetKey`
- `header1`
- `header2`
- `headerN`

**Syntax:**

```
KeepColsHeaders from <worksheetKey> ["<header1>","<header2>",...,"<headerN>"]
```

**Examples:**

```
KeepColsHeaders from WSheetA ["Costos","Fechas","Totales"]
```

*Added: 2017-Aug-01*

---

### KeepHeaders

> Deletes all data except headers.

Deletes all data except headers (considering headers are in row 1).

**Parameters:**
- `worksheetKey`

**Syntax:**

```
KeepHeaders from <worksheetKey>
```

**Examples:**

```
KeepHeaders from WSheetA
```

*Added: 2018-Jun-26*

---

### KeepRows

> Deletes rows acording to a list of values in a given column index.

Deletes rows acording to a list of values in a given column index. Index begins with 1. "In" syntax will delete all rows that do not match the given list values. "Not" syntax will delete only those that match the given list. Date format in cells is currently not considered.

**Parameters:**
- `worksheetKey`
- `colIndex`
- `something`
- `rowIndex`
- `val1`
- `valN`

**Syntax:**

```
KeepRows from <worksheetKey> where <colIndex> not <something> start_at <rowIndex>
KeepRows from <worksheetKey> where <colIndex> in ["<val1>", "...", "<valN>"]
KeepRows from <worksheetKey> where <colIndex> not ["<val1>", "...", "<valN>"]
```

**Examples:**

```
KeepRows from wsheetA where 5 not OK start_at 2
KeepRows from wsheetA where 1 in ["Monday", "Tuesday", "Friday", "Sunday"]
KeepRows from wsheetA where 3 not ["Pizza", "Salad", "Soup"]
```

*Added: 2017-Aug-01*

---

### LoadChart

> Loads a Chart from a Worksheet to a variable.

Loads a Chart from a Worksheet to a variable for future reference. 

**Parameters:**
- `NameChart`
- `worksheetKey`
- `chartKey`

**Syntax:**

```
LoadChart {NameChart} of worksheet <worksheetKey> as <chartKey>
```

**Examples:**

```
LoadChart {Chart 1} of worksheet WSChart as graficakey
```

*Added: 2021-Mar-30*

---

### LoadCSV

> Open a csv file as a workbook.

Load a CSV file as a workbook given a delimiter. WorksheetKey is saved with the same name as the WorkbookKey. Delimiters can be any single character or in the simple syntax it can be "fixed"; use TAB as delimiter for tab separated files. Fixed length files must be separated by spaces. For the formated syntax, values can be Text, General for numbers, and date formats YMD, MDY and DMY. Non specified columns are formated as General.

**Parameters:**
- `Filepath`
- `delimiter`
- `workbookKey`
- `posibleFormats`

**Syntax:**

```
LoadCSV "<filepath>" separated_by <delimiter> as <workbookKey>
LoadCSV "<filepath>" separated_by <delimiter> as <workbookKey> with format [<posibleFormats:Text,General,YMD,MDY,DMY,Skip>]
```

**Options:**

- `posibleFormats`: `Text,General,YMD,MDY,DMY,Skip`

**Examples:**

```
LoadCSV "C:\Users\user.surname\Desktop\LoadCSV\file.csv" separated_by ; as delimiter
LoadCSV "C:\Users\user.surname\Desktop\LoadCSV\file.txt" separated_by fixed as delimiter
LoadCSV "C:\Users\user.surname\Desktop\LoadCSV\file.txt" separated_by | as CSVKey with format [ ]
```

*Added: 2017-Aug-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/LoadCSV.pdf)

---

### LoadCSV2

> Open a csv file separated by (, or ;) as a workbook.

Load a csv file separated by a delimiter (, or ;) as a workbook identified with a given workbook key. Use the ending flag CSVExclusive for Excel to load the original .csv file without creating a .txt file.

**Parameters:**
- `filePath`
- `delimiter`
- `workbookKey`

**Syntax:**

```
LoadCSV2 "<filePath>" separated_by <delimiter> as <workbookKey>
LoadCSV2 "<filePath>" separated_by <delimiter> as <workbookKey> CSVExclusive
```

**Examples:**

```
LoadCSV2 "C:\Users\user.surname\Desktop\LoadCSV\file.csv" separated_by , as MyWorkBook
LoadCSV2 "C:\Users\user.surname\Desktop\LoadCSV\file.csv" separated_by , as MyWorkBook CSVExclusive
```

*Added: 2019-Nov-27*

---

### LoadCSVFixed

> Open a csv file separated by (, or ;) as a workbook.

Load a csv file separated by a delimiter (, or ;) as a workbook identified with a given workbook key.

**Parameters:**
- `filePath`
- `delimiter`
- `workbookKey`

**Syntax:**

```
LoadCSVFixed "<filePath>" separated_by <delimiter> as <workbookKey>
```

**Examples:**

```
LoadCSVFixed "C:\Users\user.surname\Desktop\LoadCSV\file.csv" separated_by , as MyWorkBook
```

*Added: 2019-Jun-06*

---

### LoadFileFrom

> Loads a file based in up to two query parameters.

Loads a file inside a given the path, searching for up to two query parameters. Secondval can be EMPTY when there are no more search parameters left.

**Parameters:**
- `workbookPath`
- `firstval`
- `secondval`
- `key`

**Syntax:**

```
LoadFileFrom "<workbookPath>" containing <firstval> and <secondval> as <key>
```

**Examples:**

```
LoadFileFrom "<<WorkBookDeck>>" containing COBRO and Date{MMMM(-1) es} as WorkBookC
```

*Added: 2018-Jan-20*

---

### LoadWBook

> Open a workbook.

Opens a given workbook and saves a variable for future reference. Optional parameters are: Password:"<password>", UpdateLinks:yes|no 

**Parameters:**
- `workbookPath`
- `workbookKey`
- `password`
- `updateLinksAnswer`
- `updLinks`

**Syntax:**

```
LoadWBook "<workbookPath>" as <workbookKey>
LoadWBook "<workbookPath>" as <workbookKey> with_parameters UpdateLinks: <updLinks:yes|no>
LoadWBook "<workbookPath>" as <workbookKey> with_parameters Password: "<password>"
LoadWBook "<workbookPath>" as <workbookKey> with_parameters Password: "<password>" UpdateLinks: <updLinks:yes|no>
```

**Options:**

- `updLinks`: `yes`, `no`
- `updLinks`: `yes`, `no`

**Examples:**

```
LoadWBook "C:\Users\productivity\Desktop\Book1.xlsx" as book1
LoadWBook "C:\Users\productivity\Desktop\SecretBook.xlsx" as book1 with_parameters Password: "1234"
LoadWBook "C:\Users\productivity\Desktop\Summary.xlsx" as book1 with_parameters UpdateLinks: yes
```

*Added: 2017-Aug-01*

---

### LoadWSfrom

> Loads a Worksheet searching it by part of its name within a workbook.

Loads a Worksheet searching it by part of its name within a workbook. It will return the first match with the available worksheet names. It is case sensitive and if it does not find any matches it will add a variable as null. Warning: Avoid this function, use LoadWS sintax instead.

**Parameters:**
- `workbookKey`
- `text`
- `worksheetKey`

**Syntax:**

```
(deprecated)LoadWSfrom <workbookKey> containing "<text>" as <worksheetKey>
```

**Examples:**

```
LoadWSfrom WorkBookADC containing "abl" as TblWorkSheetADC
```

*Added: 2018-Jan-30*

---

### LoadWSheet

> Loads a Worksheet to a variable.

Loads a Worksheet to a variable. Syntax with sheet_index is 1-based and it will take the sheet in the order of appearance. 
Sheet_exact may be used when the sheet's name starts or ends with spaces. 
Sheet `that contains` will look for part of the name and return the first match, if there are no matches it will return an error. The name is not case sensitive.

**Parameters:**
- `workbookKey`
- `sheetName`
- `sheetIndex`
- `worksheetKey`

**Syntax:**

```
LoadWSheet <workbookKey> sheet "<sheetName>" as <worksheetKey>
LoadWSheet <workbookKey> sheet_index <sheetIndex> as <worksheetKey>
LoadWSheet {<workbookKey>} sheet_exact {<sheetName>} as {<worksheetKey>}
LoadWSheet {<workbookKey>} sheet that contains {<sheetName>} as {<worksheetKey>}
```

**Examples:**

```
LoadWSheet Book1 sheet "Sheet 1" as Finanzas
LoadWSheet Book1 sheet_index 1 as Finanzas
```

*Added: 2017-Aug-01*

---

### LoadXSD

> Loads an XML Map to the workbook for exporting data in an XML.

Loads an XML Map to the workbook for exporting data in an XML. When available load the schema (XSD) file, if not available an example output of the XML can be loaded. Refer to https://spreadsheeto.com/xml/ for excel usage

**Parameters:**
- `XML`
- `or`
- `XSD`
- `path`
- `workbookKey`

**Syntax:**

```
LoadXSD path "<XML_or_XSD_path>" to <workbookKey>
```

**Examples:**

```
LoadXSD path "C:\templates\facturaSchema.xsd" to bookWB
LoadXSD path "C:\templates\factura.xml" to bookWB
```

*Added: 2020-Jun-19*

---

### MakeZip

> Currently not working. Makes a zip file made out of workbooks.

Makes a zip file with the given workbook keys and saves it in the first workbook's location. Currently not working.

**Parameters:**
- `workbookKey1`
- `workbookKey2`
- `workbookKeyN`
- `zipName`

**Syntax:**

```
MakeZip [<workbookKey1>, <workbookKey2>, ..., <workbookKeyN>] as "<zipName>"
```

**Examples:**

```
MakeZip [Book3, Wbook2] as "Exceles"
```

*Added: 2017-Oct-31*

---

### MoveCol

> Moves a column to a diferent one.

Moves a column to a diferent index. Indexes start with 1.

**Parameters:**
- `worksheetKey`
- `originIndex`
- `destIndex`

**Syntax:**

```
MoveCol <worksheetKey> from <originIndex> to <destIndex>
```

**Examples:**

```
MoveCol WSheet2 from 5 to 9
```

*Added: 2017-Aug-01*

---

### MoveField

> Move a pivot table field to another field type.

Move a pivot table field to another field type (row|column|value|filter). It can be moved using the field name or the PivotFieldKey. To debug posible field names use instruction SetLogLevel Debug.

**Parameters:**
- `fieldType`
- `pivotTableKey`
- `fieldName`
- `pivotFieldKey`

**Syntax:**

```
MoveField <pivotFieldKey> to <fieldType:row|column|value|filter>
MoveField from the pivottable <pivotTableKey> and name "<fieldName>" to <fieldType:row|column|value|filter>
```

**Options:**

- `fieldType`: `row`, `column`, `value`, `filter`
- `fieldType`: `row`, `column`, `value`, `filter`

**Examples:**

```
MoveField pivotFieldKey1 to column
MoveField from the pivottable PivotTableKey1 and name "Names" to row
```

*Added: 2020-Sep-01*

---

### MoveRow

> Moves a row to a diferent one.

Moves a row to a diferent index. Indexes start with 1.

**Parameters:**
- `worksheetKey`
- `originIndex`
- `destinyIndex`
- `columnIndex`
- `wordStart`
- `startRow`
- `endRow`
- `destinyRow`

**Syntax:**

```
MoveRow {<worksheetKey>} from {<originIndex>} to {<destinyIndex>}
MoveRow {<worksheetKey>} range_start {<startRow>} range_end {<endRow>} to_row {<destinyRow>}
```

**Examples:**

```
MoveRow {sheet} from {5} to {2}
MoveRow {sheet} from_column_index {4} start_with {BANCA} to_row {6}
MoveRow {sheet} range_start {50} range_end {75} to_row {5}
```

*Added: 2019-Oct-18*

---

### MoveSheet

> Move a worksheet to a different position in the same workbook.

Move a worksheet to a different position in the same workbook.

**Parameters:**
- `workbookKey`
- `worksheetKey`
- `worksheetName`
- `worksheetKey2`

**Syntax:**

```
MoveSheet <workbookKey> sheet_key <worksheetKey> before_key <worksheetKey2>
MoveSheet <workbookKey> sheet_key <worksheetKey> before_name <worksheetName>
MoveSheet <workbookKey> sheet_key <worksheetKey> after_key <worksheetKey2>
MoveSheet <workbookKey> sheet_key <worksheetKey> after_name <worksheetName>
MoveSheet <workbookKey> sheet_key <worksheetKey> toEnd
```

**Examples:**

```
MoveSheet libro sheet_key mover before_key referencia
MoveSheet Book sheet_key saldos before_name Sheet2
MoveSheet miLibro sheet_key usuarios after_key hojaFija
```

*Added: 2019-Nov-27*

---

### MoveTableFieldPosition

> Switch position of a field in a pivot table.

Move the position of a field in a pivot table. It will stay in the same field type, but it will switch positions in the order of appearance. Key will use an existing pivot field variable to indicate which field must be moved. Name and caption are the same in most cases unless using OLAP data sources. Index is 1-based.

**Parameters:**
- `tableFieldKey`
- `fieldCaption`
- `fieldName`
- `pivotTableKey`
- `index`

**Syntax:**

```
MoveTableFieldPosition key {<tableFieldKey>} from {<pivotTableKey>} to index {<index>}
MoveTableFieldPosition caption {<fieldCaption>} from {<pivotTableKey>} to index {<index>}
MoveTableFieldPosition name {<fieldName>} from {<pivotTableKey>} to index {<index>}
```

**Examples:**

```
MoveTableFieldPosition key {orderFieldKey} from {pivotKey} to index {1}
MoveTableFieldPosition caption {Order} from {pivotKey} to index {2}
MoveTableFieldPosition name {[TRANSACTION].[ORDER_ID].[ORDER_ID]} from {pivotKey} to index {3}
```

*Added: 2023-Dec-20*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### MultiFilter

> Filter a column with many criteria.

Add a filter to the used range in a sheet with many criteria. Column index begins with 1 and indicates where the filter will be applied. Start at is the row where the filter controls will be placed, and the lower rows will be subject to the filter. The criteria indicates filter values and it can have wildcards (*?). 
The first and second syntax uses AutoFilters and require that each cell in the start_at row must have a value (column name). 
The third syntax allows to filter by more than 2 criteria, you just need to specify the column header where the criteria will apply. Using the same criteria and order in the third syntax may cause some troubles. 
The MANAGE CRITERIA option solves this problems reordering the criterias. Start_at syntax can filter with excluding criteria. 
For more explanation reffer to Excel's advanced filters documentation.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `rowIndex`
- `headerRow`
- `criteria`
- `columnHeader`

**Syntax:**

```
MultiFilter from <worksheetKey> in_column_index <columnIndex> with_criteria [<criteria 1, <criteria 2>]
MultiFilter from <worksheetKey> in_column_index <columnIndex> start_at <rowIndex> with_criteria [<criteria 1, criteria 2>]
MultiFilter from <worksheetKey> in_range <range|UsedRange> with_criteria [<columnHeader 1>, <criteria 1>, <criteria 2>,..., criteria n; <columnHeader 2>, <criteria 1>, <criteria 2>,..., <criteria n>;...; <columnHeader n>, <criteria 1>, <criteria 2>,..., <criteria n>]
MultiFilter from <worksheetKey> in_range <range|UsedRange> with_criteria [<columnHeader 1>, <criteria 1>, <criteria 2>,..., criteria n; <columnHeader 2>, <criteria 1>, <criteria 2>,..., <criteria n>;...; <columnHeader n>, <criteria 1>, <criteria 2>,..., <criteria n>] -managecriteria
MultiFilter from <worksheetKey> start_at <headerRow> <find|except> with_criteria [<columnHeader 1>, <criteria 1>, <criteria 2>,..., <criteria n>; <columnHeader 2>, <criteria 1>, <criteria 2>,..., <criteria n>;...; <columnHeader n>, <criteria 1>, <criteria 2>,..., <criteria n>]
MultiFilter from <worksheetKey> start_at <headerRow> <find|except> with_criteria [<columnHeader 1>, <criteria 1>, <criteria 2>,..., <criteria n>; <columnHeader 2>, <criteria 1>, <criteria 2>,..., <criteria n>;...; <columnHeader n>, <criteria 1>, <criteria 2>,..., <criteria n>] date source [<columnHeader 1>,<criteria 1>;...;<columnHeader n>,<criteria n>]
```

**Examples:**

```
MultiFilter from Sheet2 in_column_index 5 with_criteria [HEB, Home Depot]
MultiFilter from Sheet2 in_column_index 5 with_criteria [venta-201512, venta-2016*]
MultiFilter from Sheet2 in_column_index 5 start_at 2 with_criteria [HEB, Home Depot]
```

*Added: 2018-Mar-02*

---

### NewWB

> Create a new workbook.

Creates a new Workbook in a path where the client wants (only creates file of type "xlsx"). You CANNOT use special characters that Windows does NOT allow. WorkbookName is also saved as a variable. "Create in" syntax will save the workbook without saving a variable.

**Parameters:**
- `path`
- `workbookName`
- `pathWithName`

**Syntax:**

```
(Deprecated) NewWB in "<path>" as <workbookName>
NewWB in {<path>} as {<workbookName>}
NewWB create in {<pathWithName>}
```

**Examples:**

```
NewWB in {C:\Users\user_name\Desktop} as {Book_03-03-2019}
NewWB create in {C:\Users\user_name\Desktop\Book_03-03-2019.xlsx}
```

*Added: 2017-Aug-01*

---

### NewWs

> Add a new worksheet to the workbook.

Adds a new worksheet to a given workbook. With name sintax allows worksheetKeys to be different from the intended visible name of the sheet.

**Parameters:**
- `workbookKey`
- `worksheetKey`
- `worksheetName`
- `wsName`

**Syntax:**

```
NewWs in <workbookKey> as <worksheetKey>
NewWs in_Wb <workbookKey> as <worksheetKey> after <wsName>
NewWs in_Wb <workbookKey> as {<worksheetKey>} with name {<worksheetName>} after {<wsName>}
```

**Examples:**

```
NewWs in Libro1 as Sheet1
NewWs in_Wb Libro1 as WsSheet2 after Sheet1
NewWs in_Wb {Libro1} as {WsSheet2} with name {Procesos en curso} after {Procesos pendientes}
```

*Added: 2017-Aug-01*

---

### NormalizeHeaders

> Uppercase all contents in a row.

Process all the contents of a row, and format them so they are all in Uppercase and with no leading or trailing blank spaces. This works with the UsedRange, so be careful when indicating the row parameter.

**Parameters:**
- `sheetKey`
- `rowIndex`

**Syntax:**

```
NormalizeHeaders in <sheetKey> row=<rowIndex>
```

**Examples:**

```
NormalizeHeaders in mySheet row=5
```

*Added: 2020-Jan-10*

---

### PageSetup

> Setup Page properties

Set page properties for printing or saving to PDF. Many PageSetup instructions may be used per worksheet to set for example portrait orientation from range C30:lastT and with automatic scale.
Orientation values can be landscape or portrait. 
Scale values can be automatic or scalePercent.

**Parameters:**
- `worksheetKey`
- `orientation`
- `range`
- `scale`

**Syntax:**

```
PageSetup in {<worksheetKey>} with orientation {<orientation:landscape|portrait>}
PageSetup in {<worksheetKey>} with print area {<range>}
PageSetup in {<worksheetKey>} with scale {<scale:automatic|scalePercent>}
```

**Options:**

- `orientation`: `landscape`, `portrait`
- `scale`: `automatic`, `scalePercent`

**Examples:**

```
PageSetup in {wssheet1} with orientation {landscape}
PageSetup in {wssheet1} with print area {A3:J50}
PageSetup in {wssheet1} with print area {A1:lastC}
```

*Added: 2022-May-17*

---

### PivotFieldDesign

> Modify the pivot table's field design and field settings.

Modify the pivot table's field design. Position can be changed, considering that the value stated is equal or lower than the amount of pivotFields in the same area. Meaning, if there are 2 fields in "Filter" type, position, can only be 1 or 2.
 You can also change the Field Settings to repeat item labels, for example.

**Parameters:**
- `pivotfieldKey`
- `attributeType`
- `value`

**Syntax:**

```
PivotFieldDesign <pivotfieldKey> attribute <attributeType:position|subtotals|layoutform|RepeatItemLabels> value <value>
```

**Options:**

- `attributeType`: `position`, `subtotals`, `layoutform`, `RepeatItemLabels`

**Examples:**

```
PivotFieldDesign estadoKey attribute position value 1
PivotFieldDesign poblacionKey attribute subtotals value false
PivotFieldDesign ciudad attribute layoutform value true
```

*Added: 2018-Mar-02*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### Protect

> Protect a workbook or sheet.

Protects a given workbook or sheet. If there is no password, do not send a text in the password field. "Book" can either protect the book from opening or the structure (no other sheets inserted, deleted, etc) in the workbook. "Sheet" can protect from modifying images, or cell contents. 
 ProtectProperties values can be OpenBook or Structure

**Parameters:**
- `item`
- `workbookKey`
- `worksheetKey`
- `password`
- `protectProperties`
- `structure`

**Syntax:**

```
Protect {book} by_name {<workbookKey>} with_password {<password>} properties [<protectProperties:OpenBook|Structure>]
Protect {book} by_name {<workbookKey>} with_password {<password>} properties [<structure>]
Protect {sheet} by_name {<worksheetKey>} with_password {<password>} properties [<protectProperties:DrawingObjects|Contents>]
```

**Options:**

- `protectProperties`: `OpenBook`, `Structure`
- `protectProperties`: `DrawingObjects`, `Contents`

**Examples:**

```
Protect {book} by_name {LibroUsado} with_password {secreto} properties [OpenBook]
Protect {sheet} by_name {hoja} with_password {secreto} properties [DrawingObjects, Contents]
Protect {sheet} by_name {hoja} with_password {secreto} properties [Contents]
```

*Added: 2020-Jul-06*

---

### RangeDelete

> Delete cells from a range.

Delete cells from a range or an individual cell. The cells will be deleted, therefore cells on the right will be moved.
Beware, filtered ranges can only delete the whole row.
The range may be in the style of A1:B2, also A1:lastF or with UsedRange, it's also accepted to put the name of the Table.

**Parameters:**
- `worksheetKey`
- `range`

**Syntax:**

```
RangeDelete from <worksheetKey> in <range>
```

**Examples:**

```
RangeDelete from sheet in A1:B7
RangeDelete from sheet in A2:lastA
RangeDelete from sheet in UsedRange
```

*Added: 2018-Jan-16*

---

### RangeToImage

> Copy a range of a worksheet to an image.

Copies a given range in a worksheet to an image stored with a given name in a given path. It considers filters applied in the worksheet.

**Parameters:**
- `range`
- `worksheetName`
- `workbookKey`
- `imageName`
- `folderPath`

**Syntax:**

```
RangeToImage "<range>" FromSheet "<worksheetName>" FromBook <workbookKey> ToImage "<imageName>" InFolder "<folderPath>"
```

**Examples:**

```
RangeToImage "A1:C3" FromSheet "Sheet1" FromBook bookWB ToImage "evidencia.jpg" InFolder "C:espaldo"
```

*Added: 2018-Jun-20*

---

### ReadCell

> Read a cell from a worksheet and save it in a variable.

Read a specific cell from a worksheet by its position {<Row>,<Column>}. The index of the column and the row start at 1. Indexes can be LastRow or LastCol and addition and substraction operations can be done within.

**Parameters:**
- `worksheetKey`
- `Row`
- `Column`
- `variableKey`

**Syntax:**

```
ReadCell from the worksheet <worksheetKey> from the cell {<Row>,<Column>} and save its value as {<variableKey>}
ReadCell from the worksheet <worksheetKey> from the cell {LastRow,<Column>} and save its value as {<variableKey>}
ReadCell from the worksheet <worksheetKey> from the cell {<Row>,LastCol} and save its value as {<variableKey>}
ReadCell from the worksheet <worksheetKey> from the cell {<Row>-2,<Column>+3} and save its value as {<variableKey>}
```

**Examples:**

```
ReadCell from the worksheet WSheet1 from the cell {100,2} and save its value as {RUC}
ReadCell from the worksheet WSheet1 from the cell {100+4,2-1} and save its value as {RUC}
ReadCell from the worksheet WSheet1 from the cell {LastRow,2} and save its value as {RUC}
```

*Added: 2019-Jan-07*

---

### ReadCellText

> Read a cell's value and save it in a variable.

Read a specific cell form a Worksheet by position {<Row>,<Column>}, keeping the number format. The index of the column and the row start at 1.

**Parameters:**
- `worksheetKey`
- `Row`
- `Column`
- `varName`

**Syntax:**

```
ReadCellText from the worksheet {<worksheetKey>} from the cell {<Row>,<Column>} and save its value as {<varName>}
ReadCellText from the worksheet {<worksheetKey>} from the cell {LastRow,<Column>} and save its value as {<varName>}
ReadCellText from the worksheet {<worksheetKey>} from the cell {<Row>,LastCol} and save its value as {<varName>}
ReadCellText from the worksheet {<worksheetKey>} from the cell {<Row>-2,<Column>+3} and save its value as {<varName>}
```

**Examples:**

```
ReadCellText from the worksheet {WSheet1} from the cell {100,2} and save its value as {RUC}
ReadCellText from the worksheet {WSheet1} from the cell {100+4,2-1} and save its value as {RUC}
ReadCellText from the worksheet {WSheet1} from the cell {LastRow,2} and save its value as {RUC}
```

*Added: 2019-Jun-07*

---

### ReadColumn

> Read a column and save it in a variable.

Read a given column indicated by index and save it in a variable. The index of the column starts at 1. First syntax saves only non-empty values. If the first columns are empty, columnIndex 1 will be the one with values.
 "With nulls" syntax saves also empty values. 
"Visible" syntax will consider filters, and save visible values, in this syntax start_at will read properly without considerations whether the column is empty or not. 
Warning: Reading a large amount of information will take long to write in the log, consider turning log printing off for this instruction.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `rowIndex`
- `varName`

**Syntax:**

```
ReadColumn from the worksheet <worksheetKey> with the column index {<columnIndex>} and save its value as {<varName>}
ReadColumn from the worksheet <worksheetKey> with the column index {<columnIndex>} and save its value as {<varName>} with nulls
ReadColumn from the worksheet {<worksheetKey>} with the column index {<columnIndex>} start_at {<rowIndex>} and save its value as {<varName>} visible
ReadColumn from the worksheet {<worksheetKey>} with the column index {<columnIndex>} start_at {<rowIndex>} and save its value as {<varName>} visible without nulls
```

**Examples:**

```
ReadColumn from the worksheet WS_Sheet with the column index {1} and save its value as {IDs}
ReadColumn from the worksheet WS_Sheet with the column index {1} and save its value as {IDs} with nulls
ReadColumn from the worksheet {banca} with the column index {3} start_at {7} and save its value as {pagos} visible
```

*Added: 2018-Nov-06*

---

### ReadFields

> Read the name of the pivot table fields and save them in a list.

Read the name of the pivot table fields and save them in a list, this function may help if you are using the MoveField function and only works for existing pivot tables.

**Parameters:**
- `PivotTableKey`
- `VariableKey`

**Syntax:**

```
ReadFields from <PivotTableKey> and save as <VariableKey>
```

**Examples:**

```
ReadFields from PivotTableKey1 and save as FieldNames
```

*Added: 2020-Sep-01*

---

### ReadPivotTable

> Load existing pivot tables in a worksheet.

Loads existing pivot tables in a worksheet to a given pivotTableKey.

**Parameters:**
- `pivotTableName`
- `worksheetKey`
- `pivotTableKey`

**Syntax:**

```
ReadPivotTable "<pivotTableName>" From <worksheetKey> As <pivotTableKey>
```

**Examples:**

```
ReadPivotTable "Tabla Pivote" From wsKey As tblPivote
```

*Added: 2018-Jun-20*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### ReadRange

> Read a Range of a worksheet as a Row x Column List.

Reads a Range of cells in a worksheet as a List of n elements (rows), containing m items (columns). The empty cells will be empty strings.
Syntaxes with include formulas, will get the formula in the cell instead of the value.
Syntaxes with "visible" will only read the visible elements in filtered data. 
Range values can use "UsedRange" or ranges using A1:lastF to get a range from A to the last row of F.

**Parameters:**
- `worksheetKey`
- `cellRange`
- `varKey`

**Syntax:**

```
ReadRange from {<worksheetKey>} in range {<cellRange>} as <varKey>
ReadRange from {<worksheetKey>} in range {<cellRange>} include formulas as <varKey>
ReadRange from {<worksheetKey>} in range {<cellRange>} visible as <varKey>
ReadRange from {<worksheetKey>} in range {<cellRange>} visible include formulas as <varKey>
```

**Examples:**

```
ReadRange from {sheetVar} in range {B2:D15} as var2DList
ReadRange from {sheetVar} in range {B2:D15} visible as visible2DList
ReadRange from {sheetVar} in range {UsedRange} visible include formulas as visible2DList
```

*Added: 2022-Sep-29*

---

### ReadRows

> Read the Used Range of a worksheet as a Row x Column List.

Reads the UsedRange of a worksheet as a List of n elements (rows), containing m items (columns). The empty cells will be strings = "". With the "update" function you can update the variable list with different values. Syntax with "visible" will only read the visible elements in filtered data.

**Parameters:**
- `worksheetKey`
- `rowIndex`
- `varKey`
- `col1`
- `col2`

**Syntax:**

```
ReadRows from <worksheetKey> start_at <rowIndex> as <varKey>
ReadRows v2 from <worksheetKey> start_at <rowIndex> as <varKey>
ReadRows v2 from <worksheetKey> start_at <rowIndex> as <varKey> visible
ReadRows from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} update
ReadRows from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} without nulls
ReadRows from <worksheetKey> start_at <rowIndex> as <varKey> cols [<col1>,<col2>...]
ReadRows v2 from <worksheetKey> start_at <rowIndex> as <varKey> cols [<col1>,<col2>...]
ReadRows v2 from <worksheetKey> start_at <rowIndex> as <varKey> visible cols [<col1>,<col2>...]
ReadRows from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} update cols [<col1>,<col2>...]
ReadRows from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} without nulls cols [<col1>,<col2>...]
```

**Examples:**

```
ReadRows from yaraWS start_at 2 as data
ReadRows from yaraWS start_at 2 as data cols [3,6,8]
ReadRows from {contador} start_at {2} as {lista} update
```

*Added: 2018-Jun-12*

---

### ReadRowsCSV

> Read all rows in a sheet and separate the values by a delimiter.

Reads all rows in a sheet and if posible it separetes lines using a delimiter character. Read values are stored in a list variable. It will not necesarily be of N x M dimension, it depends on the amount of delimiters in each row individualy. Empty cells will be stored as "". Row index starts at 1 and indicates where to start saving the list. Only one column must be filled per row, for delimiter separation. Otherwise each cell in the row will be saved in the list.

**Parameters:**
- `worksheetKey`
- `rowIndex`
- `varKey`
- `delimiter`

**Syntax:**

```
ReadRowsCSV from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} by {<delimiter>}
```

**Examples:**

```
ReadRowsCSV from {sheetcsv} start_at {2} as {list} by {,}
```

*Added: 2019-Aug-27*

---

### ReadRowsWithFormat

> Read the Used Range of a worksheet as a Row x Column List and keep the format displayed.

Reads the UsedRange of a worksheet as a List of n elements (rows), containing m items (columns) keeping the displayed format in numbers and dates. The empty cells will be strings = "". 

Keep in mind that this function may be a lot slower than ReadRows because formats are retrieved individualy per cell.

**Parameters:**
- `worksheetKey`
- `rowIndex`
- `varKey`
- `col1`
- `col2`

**Syntax:**

```
ReadRowsWithFormat from <worksheetKey> start_at <rowIndex> as <varKey>
ReadRowsWithFormat from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} without nulls
ReadRowsWithFormat from <worksheetKey> start_at <rowIndex> as <varKey> cols [<col1>,<col2>...]
ReadRowsWithFormat from {<worksheetKey>} start_at {<rowIndex>} as {<varKey>} without nulls cols [<col1>,<col2>...]
```

**Examples:**

```
ReadRowsWithFormat from someWS start_at 2 as data
ReadRowsWithFormat from someWS start_at 2 as data cols [3,6,8]
ReadRows from {someWS} start_at {12} as {Data} without nulls
```

*Added: 2023-Feb-01*

---

### ReadValueThatMatch

> Filter a column by a value and read the corresponding value from another column.

Apply a filter to a column A by the value given and read the value in the same row from the colum B saving it on a dictionary variable, in case it does not exist it saves -1. If it finds exactly one value, it the variable will be saved as a string instead of the dictionary. 
If you expect to look for values starting or ending with spaces, use the syntax that has "exact". Indexes are 1-based.

**Parameters:**
- `worksheetKey`
- `columnIndex1`
- `columnIndex2`
- `criteria`
- `varName`

**Syntax:**

```
(Deprecated) ReadValueThatMatch in the worksheet <worksheetKey> at the column {<columnIndex1>} maching the value "<criteria>" and read the column {<columnIndex2>} and save it value as {<varName>}
ReadValueThatMatch in the worksheet <worksheetKey> at the column {<columnIndex1>} matching the value "<criteria>" and read the column {<columnIndex2>} and save it value as {<varName>}
ReadValueThatMatch in the worksheet <worksheetKey> at the column {<columnIndex1>} matching the exact value "<criteria>" and read the column {<columnIndex2>} and save it value as {<varName>}
```

**Examples:**

```
ReadValueThatMatch in the worksheet worksheetName at the column {1} matching the value "111001110" and read the column {3} and save it value as {TicketAuthor}
ReadValueThatMatch in the worksheet worksheetName at the column {1} matching the exact value "  111001110" and read the column {3} and save it value as {TicketAuthor}
```

*Added: 2018-Nov-05*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/automation/ExtraDocsFRIDA/Excel Reader/ReadValueThatMatch.pdf)

---

### RefreshAll

> Get the latest data by refreshing all sources in the workbook.

Get the latest data by refreshing all sources in the workbook. Expecting popups syntax will close emerging database messages popups, saving the RefreshStatus variable with either "OK" if there were no popups present or "Error" whenever data base error messages appeared and were taken care of.

**Parameters:**
- `WorkbookKey`

**Syntax:**

```
RefreshAll <WorkbookKey>
RefreshAll <WorkbookKey> expecting popups
```

**Examples:**

```
RefreshAll Book1Key
RefreshAll Book1Key expecting popups
```

*Added: 2018-Oct-29*

---

### RefreshAllPT

> Refresh all pivot tables that exist in a workbook.

Refresh all pivot tables that exist in a workbook.

**Parameters:**
- `WorkbookKey`

**Syntax:**

```
RefreshAllPT <WorkbookKey>
```

**Examples:**

```
RefreshAllPT workb
```

*Added: 2017-Aug-23*

---

### RefreshPivotTable

> Refreh a given Pivot Table.

Refreh a given Pivot Table.

**Parameters:**
- `PivotTableKey`

**Syntax:**

```
RefreshPivotTable <PivotTableKey>
```

**Examples:**

```
RefreshPivotTable pivotVariable
```

*Added: 2017-Aug-23*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### RemoveAllTableFilters

> Remove the existing filters in a worksheet that contains tables.

Remove the existing filters in a worksheet that contains tables.

**Parameters:**
- `worksheetKey`
- `tableTitle`

**Syntax:**

```
RemoveAllTableFilters from <worksheetKey> with_name "<tableTitle>"
```

**Examples:**

```
RemoveAllTableFilters from sheet1 with_name "Table1"
```

*Added: 2021-Jun-08*

---

### RemoveCharacter

> Remove a set of character(s) from a text file.

Remove a specific character or sequence of characters from a text file. Saves the content in UTF32.

**Parameters:**
- `filePath`
- `charString`

**Syntax:**

```
RemoveCharacter from <filePath> the character <charString>
```

**Examples:**

```
RemoveCharacter from C:\archivo.txt the character \
RemoveCharacter from C:\archivo.txt the character .00
```

*Added: 2018-May-22*

---

### RemoveCols

> Delete the specified columns.

Deletes the specified columns. Index starts with 1.

**Parameters:**
- `worksheetKey`
- `index`

**Syntax:**

```
RemoveCols from <worksheetKey> at [<index1>,<index2>,...,<indexN>]
```

**Examples:**

```
RemoveCols from hoja1 at [3,4,8,10]
RemoveCols from WSheet1 at [3,4]
```

*Added: 2017-Aug-01*

---

### RemoveDuplicates

> Remove the duplicate rows from a given sheet.

Removes the duplicate rows from a given sheet. When many column indexes are specified, the deletion will be based on the repetition of values in all those columns. Indexes start with 1.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `hasHeader`

**Syntax:**

```
RemoveDuplicates from <worksheetKey>
RemoveDuplicates from <worksheetKey> with_header <hasHeader:Y|N>
RemoveDuplicates from <worksheetKey> at [<columnIndex1,columnIndex2,...,columnIndexn>]
RemoveDuplicates from <worksheetKey> at [<columnIndex1,columnIndex2,...,columnIndexn>] with_header <hasHeader:Y|N>
```

**Options:**

- `hasHeader`: `Y`, `N`
- `hasHeader`: `Y`, `N`

**Examples:**

```
RemoveDuplicates from WSheet1
RemoveDuplicates from WSheet1 at [2,8,9]
RemoveDuplicates from WSheet1 at [1] with_header Y
```

*Added: 2017-Nov-14*

---

### RemoveEmptyRow

> Deletes all empty rows from a worksheet.

Deletes all empty rows from a desired work sheet.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
RemoveEmptyRow from {<worksheetKey>}
```

**Examples:**

```
RemoveEmptyRow from {hoja1}
```

*Added: 2019-Aug-29*

---

### RemoveFilters

> Remove the existing filters in a worksheet.

Remove the existing filters in a worksheet.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
RemoveFilters from <worksheetKey>
```

**Examples:**

```
RemoveFilters from sheet1
```

*Added: 2017-Aug-23*

---

### RemoveMacros

> Remove all the existing macros in a workbook.

Remove all the existing macros in a workbook.

**Parameters:**
- `workbookKey`

**Syntax:**

```
RemoveMacros from <workbookKey>
```

**Examples:**

```
RemoveMacros from WBook2
```

*Added: 2017-Aug-23*

---

### RemoveRows

> Delete rows in a worksheet.

Deletes rows that contain a given value in a column. It can also be used to delete row indicated by index. Indexes begin with 1, LastRow can be used instead of the index.

**Parameters:**
- `worksheetKey`
- `colIndex`
- `something`
- `rowIndex`
- `rowStartIndex`
- `rowEndIndex`

**Syntax:**

```
RemoveRows from <worksheetKey> where <colIndex> equals <something> start_at <rowIndex>
RemoveRows from the worksheet <worksheetKey> with the index <rowIndex>
RemoveRows from the worksheet <worksheetKey> with the index LastRow
RemoveRows from the worksheet <worksheetKey> from the index <rowStartIndex> to <rowEndIndex>
RemoveRows from the worksheet <worksheetKey> from the index <rowStartIndex> to LastRow
RemoveRows from the worksheet {<worksheetKey>} in index_column {<colIndex>} start_at {firstempty} to {lastrow}
```

**Examples:**

```
RemoveRows from hoja1 where 4 equals Error start_at 2
RemoveRows from the worksheet hoja1 with the index 5
RemoveRows from the worksheet hoja1 with the index LastRow
```

*Added: 2017-Aug-01*

---

### RemoveRowsHeader

> Deletes rows in a given column header.

Deletes rows that contain a value in a column (by header). Index start with 1.

**Parameters:**
- `worksheetKey`
- `colHeader`
- `something`
- `rowIndex`

**Syntax:**

```
RemoveRowsHeader from <worksheetKey> where "<colHeader>" equals "<something>" start_at <rowIndex>
```

**Examples:**

```
RemoveRowsHeader from SheetCostos where "Totales" equals "0" start_at 2
```

*Added: 2017-Aug-01*

---

### RemoveSheets

> Remove worksheets from a workbook.

Remove worksheets from a workbook. "except sheets" syntax currently not working. Index begins with 1.

**Parameters:**
- `workbookKey`
- `worksheetName`
- `worksheetKey`
- `worksheetIndex`

**Syntax:**

```
RemoveSheets from <workbookKey> sheet <worksheetName>
RemoveSheets from <workbookKey> sheet <worksheetKey>
RemoveSheets from <workbookKey> all except "<worksheetName>"
RemoveSheets from <workbookKey> sheets [<worksheetName1>,<worksheetName2>,<worksheetName3>,...]
RemoveSheets from <workbookKey> all except sheets [<worksheetName1>,<worksheetName2>,<worksheetName3>,...]
RemoveSheets from <workbookKey> sheet_index <worksheetIndex>
```

**Examples:**

```
RemoveSheets from WBook2 sheet USA
RemoveSheets from WBook3 all except "Mex"
RemoveSheets from WBalance sheets [USA,Mex,Sheet1]
```

*Added: 2017-Dec-29*

---

### RemoveTableDuplicates

> Remove the duplicate rows from a given sheet and table.

Removes duplicate rows from all existing tables on a given sheet or sheet and table. When many column indexes are specified, the deletion will be based on the repetition of values in all those columns. Indexes start with 1 for each table. 

**Parameters:**
- `worksheetKey`
- `tablename`
- `columnIndex`

**Syntax:**

```
RemoveTableDuplicates from <worksheetKey>
RemoveTableDuplicates from <worksheetKey> in table <tablename>
RemoveTableDuplicates from <worksheetKey> in table <tablename> at [<columnIndex1,columnIndex2,...,columnIndexn>]
```

**Examples:**

```
RemoveTableDuplicates from WSheet1
RemoveTableDuplicates from WSheet1 in table Tabla1
RemoveTableDuplicates from WSheet1 in table Tabla1 at [2,8,9]
```

---

### RemoveWorkbookConnections

> Remove all connections in a workbook.

Remove all connections in a workbook.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
RemoveWorkbookConnections <worksheetKey>
```

**Examples:**

```
RemoveWorkbookConnections book1
```

*Added: 2020-Aug-21*

---

### RepeatAllLabels

> Change repeat all item labels option in a pivot table.

Change repeat all item labels option in a given pivot table.

**Parameters:**
- `pivotTableKey`

**Syntax:**

```
RepeatAllLabels off in pivot table <pivotTableKey>
RepeatAllLabels in pivot table <pivotTableKey>
```

**Examples:**

```
RepeatAllLabels in pivot table pivotTable1
RepeatAllLabels off in pivot table pivotTable1
```

*Added: 2022-Nov-29*

---

### ReplaceAll

> Replace a text sequence for another one.

Replace one text sequence with another in an entire worksheet. The replacement can be done in formulas. The search text can be exact or just a portion. 
You can make the replacement for an empty string. When specifing a range, A1:B2 style is accepted, also A1:lastF or with UsedRange.

**Parameters:**
- `worksheetKey`
- `searchText`
- `typeSearch`
- `rangekey`
- `replacementText`

**Syntax:**

```
ReplaceAll from {<worksheetKey>} <typeSearch:contains|exacty> this {<searchText>} with {<replacementText>} in range {<rangekey>}
ReplaceAll from {<worksheetKey>} <typeSearch:contains|exacty> this {<searchText>} with {<replacementText>} in formulas
ReplaceAll from {<worksheetKey>} <typeSearch:contains|exacty> this {<searchText>} with {<replacementText>} in range formulas {<rangekey>}
```

**Options:**

- `typeSearch`: `contains`, `exacty`
- `typeSearch`: `contains`, `exacty`
- `typeSearch`: `contains`, `exacty`

**Examples:**

```
ReplaceAll from {wsSheet} this exactly {OK} with {Approved} in range {B3:lastB}
ReplaceAll from {wsSheet} this contains {NoOp} with {} in range {B2:D10}
ReplaceAll from {wsSheet} this exactly {fill date} with {=TODAY()} in formulas
```

*Added: 2022-Oct-06*

---

### ReplaceCharacter

> Replaces a character or substring with another.

Replaces a character or substring with another. Row o column indexes can be specified to delimit affected cells. Indexes start with 1. If newSubstring expected is "", write "non"  (syntax 1 and 4 have problems for now).

**Parameters:**
- `worksheetKey`
- `oldSubstring`
- `newSubstring`
- `rowIndex`
- `colIndex`
- `rowStartIndex`
- `rowEndIndex`

**Syntax:**

```
ReplaceCharacter "<oldSubstring>" from the worksheet <worksheetKey> with "<newSubstring>" in the row with the index <rowIndex>
ReplaceCharacter "<oldSubstring>" from the worksheet <worksheetKey> with "<newSubstring>" in the column with the index <colIndex>
ReplaceCharacter {<oldSubstring>} from the worksheet <worksheetKey> with "<newSubstring>" in the column with the index <colIndex>
ReplaceCharacter "<oldSubstring>" from the worksheet <worksheetKey> with "<newSubstring>" from cell {<colIndex>,<rowIndex>} up to the cell {"<colIndex or Letter>","<rowIndex or Letter>"}
```

**Examples:**

```
ReplaceCharacter "?" from the worksheet WSheet with "." in the row with the index 2
ReplaceCharacter "?" from the worksheet WSheet with "." in the column with the index 3
ReplaceCharacter ".00" from the worksheet WSheet with "non" in the column with the index 3
```

*Added: 2018-Sep-12*

---

### ReplaceText

> Replace a text sequence for another one.

Replace a text sequence for another one in a given worksheet column. Use "has header" whenever you want to avoid replacing text in the header.
Index starts with 1. If new line must be replaced use 
.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `text`
- `newText`

**Syntax:**

```
(Deprecated) ReplaceText from <worksheetKey> in_column_index <columnIndex> this "<text>" by "<newText>"
ReplaceText from {<worksheetKey>} in column {<columnIndex>} this {<text>} with {<newText>}
ReplaceText from {<worksheetKey>} in column {<columnIndex>} this {<text>} with {<newText>} has header
```

**Examples:**

```
ReplaceText from {MyWS} in column {10} this {OK} with {Approved}
ReplaceText from {MyWS} in column {10} this {Approved} with {Approved}
ReplaceText from {MyWS} in column {1} this {text\nbelow} by {one line} has header
```

*Added: 2018-Mar-02*

---

### ReplaceTextVisible

> Replace the text in a visible cell and replace it for another.

Find the exact text in a visible cell and replace it for another. Index starts with 1.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `oldCharacters`
- `newCharacters`

**Syntax:**

```
ReplaceTextVisible from {<worksheetKey>} in_column_index {<columnIndex>} this {<oldCharacters>} by {<newCharacters>}
```

**Examples:**

```
ReplaceTextVisible from {hoja} in_column_index {6} this {Completado} by {Pendiente}
```

*Added: 2019-Sep-24*

---

### ResizeTable

> Resize an existing table.

Resize an existing table to add rows or columns to the current range. 
When specifing a range, A1:B2 style is accepted, also A1:lastF or with UsedRange. Take notice that the table requires headers to remain in the same row and include at least one row of data, and the new range should overlap the existing table.

**Parameters:**
- `tableName`
- `worksheetKey`
- `range`

**Syntax:**

```
ResizeTable {<tableName>} in worksheet {<worksheetKey>} to range {<range>}
```

**Examples:**

```
ResizeTable {Table3} in worksheet {WSExampleName} to range {A1:J10}
ResizeTable {Table3} in worksheet {WSExampleName} to range {A4:lastD}
ResizeTable {Table3} in worksheet {WSExampleName} to range {UsedRange}
```

*Added: 2023-Feb-21*

---

### RunMacro

> Run a macro in a workbook.

Run a macro in a workbook.

**Parameters:**
- `macroName`
- `workbookKey`

**Syntax:**

```
RunMacro "<macroName>" InBook <workbookKey>
```

**Examples:**

```
RunMacro "Summarize" InBook regiones
```

*Added: 2018-Jun-20*

---

### RunMacroAsync

> Run a macro asynchronously in a workbook.

Run a macro asynchronously in a workbook. 
Warning: It is not recomended to execute macros asynchronously, if it is not properly handled, unexpected errors may happen. Use it when macros show message boxes to interact with the user.

**Parameters:**
- `macroName`
- `workbookKey`

**Syntax:**

```
RunMacroAsync "<macroName>" InBook <workbookKey>
```

**Examples:**

```
RunMacroAsync "Summarize" InBook regiones
```

*Added: 2024-Jun-21*

---

### Save

> Save a workbook.

Saves the last edition of the workbook.

**Parameters:**
- `workbookKey`

**Syntax:**

```
Save <workbookKey>
Save <workbookKey> and close
```

**Examples:**

```
Save libro
Save libro and close
```

*Added: 2017-Aug-23*

---

### SaveAs

> Save a workbook as a different file.

Save a file from dictionary with new name but don't add it to the dictionary. DO NOT include special characters like [, ], \, *, :, ?, <, >, |, / or " in the name. In_base syntax will close the excel book and remove variables, and afterwards open it with the new variable name. 
PDF syntax will save a pdf file with the contents o the book. 
XLSX syntax may be used to convert an open csv file to xlsx.

**Parameters:**
- `workbookKey`
- `name`
- `folder`
- `initialSheetVar`
- `endSheetVar`
- `newWorkbookKey`

**Syntax:**

```
SaveAs <workbookKey> as "<name>" in "<folder>"
SaveAs <workbookKey> as <name> in <folder>
SaveAs <workbookKey> as "<name>" in_base <newWorkbookKey>
SaveAs PDF <workbookKey> as "<name>" in "<folder>"
SaveAs PDF <workbookKey> as "<name>" in "<folder>" from sheet {<initialSheetVar>} to {<endSheetVar>} autoscale
SaveAs PDF <workbookKey> as "<name>" in "<folder>" from sheet {<initialSheetVar>} to {<endSheetVar>} no scale
SaveAs XLSX <workbookKey> as "<name>" in "<folder>"
SaveAs PRN <workbookKey> as "<name>" in "<folder>"
```

**Examples:**

```
SaveAs Libro1 as "MiLibro" in "C:\Users\productivity\Desktop"
SaveAs Libro1 as "MiLibro" in_base Libro3
SaveAs PDF Libro1 as "MiLibro" in "C:\Users\productivity\Desktop"
```

*Added: 2017-Aug-23*

---

### SaveAsCSV

> Save the active worksheet as a CSV file.

Save the active worksheet of a given workbook key to a CSV file. This does not save the file inside the dictionary. If you want to use the saved file use the LoadCSV function. DO NOT include special characters like [, ], \, *, :, ?, <, >, |, / or " at the folder name to avoid error messages.

**Parameters:**
- `workbookKey`
- `fileName`
- `path`

**Syntax:**

```
SaveAsCSV {<workbookKey>} as {<fileName>} in {<path>}
```

**Examples:**

```
SaveAsCSV {consolidado} as {PPView} in {C:\Users\user.user\Documents\Folder}
```

*Added: 2019-Sep-24*

---

### SaveWBMonth

> Currently not working. Save workbook with the name of the current month.

Save workbook with the name of the current month. Currently not working.

**Parameters:**
- `There`
- `are`
- `no`
- `parameters`

**Syntax:**

```
(Deprecated)SaveWBMonth
```

**Examples:**

```
SaveWBMonth
```

*Added: 2017-Sep-07*

---

### SetErrorChecking

> Enable or disable an ErrorCheckingOption.

Enable the running Excel Application to check the opened Workbooks for errors. Currently, the option NumberAsText is supported.

**Parameters:**
- `opt`
- `boolValue`

**Syntax:**

```
SetErrorChecking option={<opt>} value={<boolValue>}
```

**Examples:**

```
SetErrorChecking option={NumberAsText} value={false}
```

*Added: 2020-Oct-19*

---

### SetSheetVisibility

> Hide or unhide sheets in a given book.

Unhide a given sheet in a workbook or all. Hide a sheet.

**Parameters:**
- `worksheetKey`
- `workbookKey`

**Syntax:**

```
SetSheetVisibility to visible in all sheets in workbook <workbookKey>
SetSheetVisibility to <value:visible|hidden> in worksheet <worksheetKey>
```

**Options:**

- `value`: `visible`, `hidden`

**Examples:**

```
SetSheetVisibility to visible in all worksheets in workbook wbook
SetSheetVisibility to hidden in worksheet wsheet1
```

*Added: 2022-Nov-30*

---

### SetTableStyle

> Set a predefined style in an existing table.

Sets one of the following predefined styles to a table: Light1, Light2, Light3, Light4, Medium1, Medium2, Medium3, Medium4, Dark1, Dark2, Dark3, Dark4.

**Parameters:**
- `tableName`
- `worksheetKey`
- `styleName`

**Syntax:**

```
SetTableStyle in table {<tableName>} in worksheet {<worksheetKey>} with style {<styleName:Light1|Light2|Light3|Light4|Medium1|Medium2|Medium3|Medium4|Dark1|Dark2|Dark3|Dark4>}
```

**Options:**

- `styleName`: `Light1`, `Light2`, `Light3`, `Light4`, `Medium1`, `Medium2`, `Medium3`, `Medium4`, `Dark1`, `Dark2`, `Dark3`, `Dark4`

**Examples:**

```
SetTableStyle in table {Table3} in worksheet {WSExampleName} with style {Light2}
```

*Added: 2025-Feb-18*

---

### ShowAllData

> Show all data in worksheet.

Show al the data hiden in a worksheet. This function can be used to remove advanced filters. If no filters are applied, the function will return an error.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
ShowAllData in <worksheetKey>
```

**Examples:**

```
ShowAllData in sheet1
```

*Added: 2020-Oct-16*

---

### ShowChartDataLabels

> Show the data labels in a chart

Show the data lables from a given series in a chart with some options of presentation. Series are identified by index begining with 1. Optional parameters can be Rotation with the angle and Position with the following options [above, below, center].

**Parameters:**
- `path`
- `chartKey`
- `seriesNumber`
- `properties`

**Syntax:**

```
ShowChartDataLabels in <chartKey> series <seriesNumber> with {<properties>}
```

**Examples:**

```
ShowChartDataLabels in graf series 1 with {Rotation: 90}
ShowChartDataLabels in graf series 2 with {Rotation: 45 ; Position : above}
```

*Added: 2021-Feb-12*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/ShowChartDataLabels.pdf)

---

### ShowPivotTableFields

> Show names of fields from an existing pivot table.

Show names of fields from an existing pivot table. This will print information in the log such as the caption, name and where it is used in the pivot table. On OLAP data source, names may be different. This name could be required for functions such as ApplyPivotTableFilter.

**Parameters:**
- `pivotTableKey`

**Syntax:**

```
ShowPivotTableFields of table {<pivotTableKey>}
```

**Examples:**

```
ShowPivotTableFields of table {DynamicTable1}
```

*Added: 2023-Nov-30*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### SortColumns

> Sort by a Column.

Sort by a Column. Maximum 3 columns to sort in a worksheet. Order direction must be set (ascending/descending). If header is Yes, it will not sort the first value, since it considers it to be a header.

**Parameters:**
- `worksheetKey`
- `colIndex`
- `order`
- `isHeader`

**Syntax:**

```
SortColumns in <worksheetKey> by column {<colindex>} <order:ascending|descending> header <isHeader:Yes|No>
SortColumns in <worksheetKey> in UsedRange by columns {<colindex1|order1>,<colindex2|order2>,<colindex3|order3>} header <isHeader:Yes|No>  --Function still under development
```

**Options:**

- `order`: `ascending`, `descending`
- `isHeader`: `Yes`, `No`
- `isHeader`: `Yes`, `No`

**Examples:**

```
SortColumns in WSName1 by column {10} ascending header Yes
SortColumns in WSName1 in UsedRange by columns {1/ascending,2/descending,3/descending} header Yes
SortColumns in WSName1 in B10:D18 by columns {1/asc,2/desc} header No
```

*Added: 2019-Jan-11*

---

### SortPivotTableField

> Sort an existing field in a pivot table.

Sort an existing field in a pivot table. The field may be sorted ascending or descending with asc or desc.
Caption is de value shown in the excel, but if it repeats you may need to use the name. 
Field names may be different if using OLAP data sources. Check ShowPivotTableFields when in doubt.

**Parameters:**
- `pivotTableKey`
- `pivotTableFieldName`
- `pivotTableFieldCaption`
- `sortOrder`

**Syntax:**

```
SortPivotTableField in table {<pivotTableKey>} table field name {<pivotTableFieldName>} order {<sortOrder:asc|desc>}
SortPivotTableField in table {<pivotTableKey>} table field caption {<pivotTableFieldCaption>} order {<sortOrder:asc|desc>}
```

**Options:**

- `sortOrder`: `asc`, `desc`
- `sortOrder`: `asc`, `desc`

**Examples:**

```
SortPivotTableField in table {group1SCM2PT} table field caption {grades} order {desc}
SortPivotTableField in table {group1SCM2PT} table field name {[RECORDS].[GRADES]} order {desc}
```

*Added: 2023-Dec-14*

---

### SpecificFontValues

> Change cell properties such as font color, size, etc.

Make changes in cell properties such as font color, size, cell alignment, cell color, typographical emphasis and Font Family. It can be applied to a range of cells or starting from a cell until the end of the column. Name: changes the font type, or sets the text on Bold, Italic or Underline. Size: changes the font size. Textcolor: changes the font color. Color: change the color of the BACKGROUND of the selected cell. Alignments: changes the alignment of the desired range. FontFamily: changes the font family of the desired range, the font must be installed in Office

**Parameters:**
- `worksheetKey`
- `cellRange`
- `condition`
- `value`
- `fontProperties`
- `alignment`
- `R`
- `G`
- `B`

**Syntax:**

```
SpecificFontValues from_sheet <worksheetKey> range <cellRange:cell1|cell1:cell2> condition name values "<fontProperties:Bold|Italic|Underline>"
SpecificFontValues from_sheet <worksheetKey> range <cellRange:cell1|cell1:cell2> condition alignment values "<alignment:top|middle|bottom|left|center|right|justify>"
SpecificFontValues from_sheet <worksheetKey> range <cellRange:cell1|cell1:cell2> condition size values <value>
SpecificFontValues from_sheet <worksheetKey> range <cellRange:cell1|cell1:cell2> condition fontfamily values <value>
SpecificFontValues from_sheet <worksheetKey> range <cellRange:cell1|cell1:cell2> condition color values [<R>,<G>,<B>]
SpecificFontValues from_sheet <worksheetKey> range <cellRange:cell1|cell1:cell2> condition textcolor values [<R>,<G>,<B>]
SpecificFontValues from_sheet <worksheetKey> start_at <cellRange:cell1|cell1:cell2> condition <condition:name|size|color|textcolor> values <value>
```

**Options:**

- `cellRange`: `cell1`, `cell1`
- `fontProperties`: `Bold`, `Italic`, `Underline`
- `cellRange`: `cell1`, `cell1`
- `alignment`: `top`, `middle`, `bottom`, `left`, `center`, `right`, `justify`
- `cellRange`: `cell1`, `cell1`
- `cellRange`: `cell1`, `cell1`
- `cellRange`: `cell1`, `cell1`
- `cellRange`: `cell1`, `cell1`
- `cellRange`: `cell1`, `cell1`
- `condition`: `name`, `size`, `color`, `textcolor`

**Examples:**

```
SpecificFontValues from_sheet hoja1 range A1 condition textcolor values [255,0,0]
SpecificFontValues from_sheet hoja1 range A1:A5 condition name values "Bold"
SpecificFontValues from_sheet hoja1 range A1:A5 condition fontfamily values "Arial"
```

*Added: 2018-Mar-02*

---

### SplitInFiles

> Split file into other files.

Split file into files named with the value of a column. Second syntax doesn't work.

**Parameters:**
- `worksheetKey`
- `worksheetKey2`
- `columnIndex`
- `rowIndex`
- `columnOriginIndex`
- `variable`

**Syntax:**

```
SplitInFiles <worksheetKey> by column <columnIndex> start_at <rowIndex>
SplitInFiles <worksheetKey> by column <columnIndex> start_at <rowIndex> with elements from <worksheetKey2> in column <columnOriginIndex> and with variables "<variable>"
```

**Examples:**

```
SplitInFiles WSheet1 by column 3 start_at 2
SplitInFiles WSheet1 by column 3 start_at 2 with elements from WSOrigin in column 2 and with variables "MX"
```

*Added: 2017-Aug-23*

---

### Subtotal

> Calculate the subtotal within a range.

Calculate the subtotal by column grouping. The range may be in the style of A1:B2, also A1:lastF or with UsedRange.
Syntax 1 and 2: Groups a range of cells, divides them according to the specified column and sums up the last specified for each range. If the table range goes from columns A to J but the column to be summed up is E, then that should be the column stated as last in the range. 
Syntax 3 and 4: Select a range and indicates the grouping column and all the subtotal columns to be calculated. "Function" indicates the type of operation to perform on the corresponding grouped columns (SUM|COUNT|AVG|MAX|MIN|PRODUCT|COUNTNUM|STDEV|STDEVP|VAR|VARP). 
The use of "replace current subtotals false" will avoid deleting previous subtotals calculated in the range. If not specified they will be replaced. Indexes are 1-based.

**Parameters:**
- `worksheetKey`
- `range`
- `column`
- `grpColumnIndex`
- `subtColumnIndex`
- `functionName`
- `replace`

**Syntax:**

```
Subtotal in <worksheetKey> range <range> split by <column>
Subtotal in <worksheetKey> range <range> split by <column> replace current subtotals <replace:true|false>
Subtotal in <worksheetKey> range <range> group by <grpColumnIndex> add subtotal to [<subtColumnIndex1>,<subtColumnIndex2>,<subtColumnIndexn>] use function <functionName:SUM|COUNT|AVG|MAX|MIN|PRODUCT|COUNTNUM|STDEV|STDEVP|VAR|VARP>
Subtotal in <worksheetKey> range <range> group by <grpColumnIndex> add subtotal to [<subtColumnIndex1>,<subtColumnIndex2>,<subtColumnIndexn>] use function <functionName:SUM|COUNT|AVG|MAX|MIN|PRODUCT|COUNTNUM|STDEV|STDEVP|VAR|VARP> replace current subtotals <replace:true|false>
```

**Options:**

- `replace`: `true`, `false`
- `functionName`: `SUM`, `COUNT`, `AVG`, `MAX`, `MIN`, `PRODUCT`, `COUNTNUM`, `STDEV`, `STDEVP`, `VAR`, `VARP`
- `functionName`: `SUM`, `COUNT`, `AVG`, `MAX`, `MIN`, `PRODUCT`, `COUNTNUM`, `STDEV`, `STDEVP`, `VAR`, `VARP`
- `replace`: `true`, `false`

**Examples:**

```
Subtotal in sheet range a1:e26 split by 4
Subtotal in sheet range a1:e26 split by 4 replace current subtotals false
Subtotal in WS range UsedRange group by 1 add subtotal to [7] use function SUM
```

*Added: 2020-Sep-03*

---

### SumAllColumnValues

> Sum all the values on a column.

Sum all the values on a column. Index starts with 1.

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `variableName`

**Syntax:**

```
SumAllColumnValues in <worksheetKey> in the column_index "<columnIndex>" and save as "<variableName>"
```

**Examples:**

```
SumAllColumnValues in Hoja1 in the column_index "4" and save as "FilaCuatro"
```

*Added: 2019-Nov-13*

---

### TableField

> Define how the fields for a given pivot table are used.

Defines how the fields for a given pivot table are used. This corresponds to the pivot table area, where different filtering methods are applied to pivot table fields. FieldType valid values are row,column,filter. 
FunctionName valid values are average, sum, count, countnums, distinctcount, max, min, product, stdev, stdevp, unknown, var, varp.
FieldCaption is the name of the column title in the input table. FieldName is in most cases the same as FieldCaption, preferably use the "caption" syntax. If data source does not come from the same book, check ShowPivotTableFields to find the correct FieldName in case "caption" syntax does not resolve correctly. 
PivotFieldKey is the variable name of each particular field.
The syntax with remove may be used to un select fields in the pivot table.

**Parameters:**
- `fieldType`
- `pivotTableKey`
- `functionName`
- `fieldCaption`
- `fieldName`
- `pivotFieldKey`

**Syntax:**

```
TableField <fieldType:row|column|filter> from <pivotTableKey> fname "<fieldName>" as <pivotFieldKey>
TableField <fieldType:row|column|filter> from <pivotTableKey> caption "<fieldCaption>" as <pivotFieldKey>
TableField value function <functionName:average|sum|count|countnums|distinctcount|max|min|product|stdev|stdevp|unknown|var|varp> from <pivotTableKey> fname "<fieldName>" as <pivotFieldKey>
TableField value function <functionName:average|sum|count|countnums|distinctcount|max|min|product|stdev|stdevp|unknown|var|varp> from <pivotTableKey> caption "<fieldCaption>" as <pivotFieldKey>
TableField remove from <pivotTableKey> fname "<fieldName>"
TableField remove from <pivotTableKey> caption "<fieldCaption>"
```

**Options:**

- `fieldType`: `row`, `column`, `filter`
- `fieldType`: `row`, `column`, `filter`
- `functionName`: `average`, `sum`, `count`, `countnums`, `distinctcount`, `max`, `min`, `product`, `stdev`, `stdevp`, `unknown`, `var`, `varp`
- `functionName`: `average`, `sum`, `count`, `countnums`, `distinctcount`, `max`, `min`, `product`, `stdev`, `stdevp`, `unknown`, `var`, `varp`

**Examples:**

```
TableField row from PivotTable caption "Nombre del pagador" as PivotFieldRow1
TableField column from PivotTable fname "Elemento PEP" as PivotFieldRow2
TableField value function sum from PivotTable fname "[Measures].[Ingresos]" as PivotFieldRow3
```

*Added: 2017-Aug-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### TableGetSpecial

> Get the location of a cell indicated in a table by "special" identifiers such as lastCell.

Saves in a variable, the index of a column or row of a table, where a certain statement is located. The instruction can be lastRow, lastCell. 

**Parameters:**
- `instruction`
- `worksheetKey`
- `tablekey`
- `variableKey`

**Syntax:**

```
TableGetSpecial <instruction:lastRow|lastCol> from <worksheetKey> table <tablekey> and save as <variableKey>
```

**Options:**

- `instruction`: `lastRow`, `lastCol`

**Examples:**

```
TableGetSpecial lastRow from wsheet table Table2 and save as LRow
TableGetSpecial lastCol from wsheet table Table2 and save as LCol
```

*Added: 2021-Nov-22*

---

### TextFormat

> Set a text format to a given column.

Sets a text format to a given column by index. Index starts with 1.

**Parameters:**
- `worksheetKey`
- `indexcol`

**Syntax:**

```
TextFormat in <worksheetKey> in column <indexColum>
```

**Examples:**

```
TextFormat in sheet1 in column 3
```

*Added: 2017-Aug-01*

---

### TextFormat2

> Set a text format to a given column by header name.

Set a text format to a given column by header name.

**Parameters:**
- `worksheetKey`
- `header`

**Syntax:**

```
TextFormat2 in <worksheetKey> in column <headerName>
```

**Examples:**

```
TextFormat2 in Sheet1 in column Clientes
```

*Added: 2017-Aug-01*

---

### TextFormatAll

> Set a text format to all the sheet.

Set a text format to all the sheet.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
TextFormatAll in <worksheetKey>
```

**Examples:**

```
TextFormatAll in sheet1
```

*Added: 2017-Aug-01*

---

### TextToColumns

> Separate text in a range to columns

Separates a character delimited text in a given range to columns with defined formats. Tab delimiter must specify TAB. Permited formats are Text,General,YMD,MDY,DMY,Skip. Optional DelimiterBehaviour can be "consecutive" which will consider consecutive delimiters as one. In fixed columns must be one fewer than the formats because the first column is from 0 to the first position. If everything needs to be of a certain format then only one format is allowed. When nothing is specified in format, it will be interpreted by Excel

**Parameters:**
- `worksheetKey`
- `range`
- `delimiter`
- `posibleFormats`
- `columns`
- `delimiterBehaviour`

**Syntax:**

```
TextToColumns <worksheetKey> in column range <range> delimited by {<delimiter>} with format [<posibleFormats:Text,General,YMD,MDY,Skip,DMY>] <delimiterBehaviour:consecutive|>
TextToColumns <worksheetKey> in column range <range> fixed [<columns>] with format [<posibleFormats:Text,General,YMD,MDY,Skip,DMY>]
```

**Options:**

- `posibleFormats`: `Text,General,YMD,MDY,Skip,DMY`
- `delimiterBehaviour`: `consecutive`
- `posibleFormats`: `Text,General,YMD,MDY,Skip,DMY`

**Examples:**

```
TextToColumns sheetKey in column range A2:A20 delimited by {,} with format [Text,General,YMD,MDY,Skip,DMY]
TextToColumns sheetKey in column range A2:A20 delimited by {TAB} with format [ Text ] consecutive
TextToColumns sheetKey in column range A2:A20 delimited by {|} with format [ ] consecutive
```

*Added: 2020-Nov-25*

---

### TurnAlertsTo

> Turn Excel displayed alerts on or off.

Turn Excel displayed alerts on or off. Set this property to false to suppress prompts and alert messages while a macro is running.

**Parameters:**
- `alertValue`

**Syntax:**

```
TurnAlertsTo <alertValue:true|false>
```

**Options:**

- `alertValue`: `true`, `false`

**Examples:**

```
TurnAlertsTo true
TurnAlertsTo false
```

*Added: 2019-Jun-28*

---

### TurnHeadlessTo

> Turn the headless flag to true or false just for the excel processes. If it is true then the excel windows will hide and if it is false the excel windows will appear.

Turn the headless flag to true or false just for the excel processes. If it is true then the excel windows will hide and if it is false the excel windows will appear.

**Parameters:**
- `headlessFlag`

**Syntax:**

```
TurnHeadlessTo <headlessFlag:true|false>
```

**Options:**

- `headlessFlag`: `true`, `false`

**Examples:**

```
TurnHeadlessTo true
TurnHeadlessTo false
```

*Added: 2019-Jun-19*

---

### Unhide

> Unhide all rows or columns in a given range.

Unhide all rows or columns from a worksheet in a given range

**Parameters:**
- `worksheetKey`

**Syntax:**

```
Unhide all from <worksheetKey>
Unhide from <worksheetKey> all columns
Unhide from <worksheetKey> all rows
```

**Examples:**

```
Unhide all from hoja1key
Unhide from hoja1key all columns
Unhide from hoja1key all rows
```

*Added: 2021-Nov-17*

---

### UnloadXSD

> Unload the XSD schema or XML from a workbook.

Unload the XSD schema or XML from a workbook. This operation will also unbind all fields.

**Parameters:**
- `workbookKey`
- `path`

**Syntax:**

```
UnloadXSD in <workbookKey>
```

**Examples:**

```
UnloadXSD in FacturasWB
```

*Added: 2020-Jun-19*

---

### Unmerge

> Unmerge all cells from the worksheet.

Unmerge all cells from the worksheet.

**Parameters:**
- `worksheetKey`

**Syntax:**

```
Unmerge <worksheetKey>
```

**Examples:**

```
Unmerge WSheet2
```

*Added: 2017-Aug-23*

---

### Unprotect

> Unlock the protection from a workbook or sheet.

Unlock the protection from the desired workbook or sheet. If there is no password, use "none" at the password field.

**Parameters:**
- `item`
- `workbookKey`
- `worksheetKey`
- `password`

**Syntax:**

```
Unprotect {book} by_name {<workbookKey>} with_password {<password>}
Unprotect {sheet} by_name {<worksheetKey>} with_password {<password>}
```

**Examples:**

```
Unprotect {book} by_name {LibroUsado} with_password {secreto}
Unprotect {sheet} by_name {hoja} with_password {secreto}
Unprotect {sheet} by_name {hoja} with_password {none}
```

*Added: 2019-Jun-21*

---

### UpdatePT

> Update the pivot table range.

Update the pivot table range of a given pivot table key. New_sheet is the sheet where the input table is located. Ranges are defined with UsedRange or notation as R=<relative rows> C=<relative columns>, where "-1" indicates one column or row less from the original range, and "1" is one column or row additional from the original range.

**Parameters:**
- `pivotTableKey`
- `worksheetKey`
- `rangeKey`

**Syntax:**

```
UpdatePT <pivotTableKey> new_sheet <worksheetKey> new_range <rangeKey>
```

**Examples:**

```
UpdatePT PivotTable new_sheet GE new_range UsedRange
UpdatePT PivotTable new_sheet GE new_range R=-2 C=-1
UpdatePT PivotTable new_sheet GE new_range R=-2
```

*Added: 2017-Sep-09*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### UpdatePTChangingSource

> Update a Pivot table by name changing the data source.

Updates a Pivot table by name in a specific worksheet changing the data source. Range can only change in columns taken and input tables must start from A1.

**Parameters:**
- `pivotTableName`
- `worksheetKey`
- `worksheetSourceKey`
- `column`

**Syntax:**

```
UpdatePTChangingSource <pivotTableName> sheet <worksheetKey> from <worksheetSourceKey> range <column>
```

**Examples:**

```
UpdatePTChangingSource "Tabla dinámica11" sheet IniciativaWorkSheet from DeckWorkSheet range C33
```

*Added: 2018-Jan-30*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Excel/Articles/Tablas%20Pivote.pdf)

---

### Write

> Write something in a given cell in a worksheet.

Write something in a given cell in a worksheet. ColRow can take values such as A1, D15, etc. RowIndex and colIndex must take numerical values and it starts from 1, or either "lastrow" or "lastcol". Format will be applied to the cell after writting the text. Original format is mainly intended for dates, to identify the origin date parts in the text. Excel formats are different from this, refer to https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings for further information.

**Parameters:**
- `something`
- `worksheetKey`
- `ColRow`
- `rowIndex`
- `colIndex`
- `format`
- `originalFormat`

**Syntax:**

```
Write "<something>" in <worksheetKey> cell <ColRow>
Write "<something>" in <worksheetKey> cell <ColRow> with format <format>
Write "<something>" in <worksheetKey> cell <ColRow> with format <format> source <originalFormat>
Write "<something>" in <worksheetKey> row <rowIndex> and column <colIndex>
```

**Examples:**

```
Write "Nombres" in hoja1 cell E1
Write "05/07/2020" in hoja1 cell E1 with format dd/mm/yyyy
Write "05-07-2020 14:10" in hoja1 cell E1 with format dd/mm/yyyy hh:mm source dd-MM-yyyy hh:mm
```

*Added: 2017-Aug-01*

---

### Write2DList

> Write the values in a 2D List variable starting at a given cell on a worksheet.

Write the values in a 2D List variable starting at a given cell on a worksheet. Indexes start at 1. It will only write in visible cells.

**Parameters:**
- `worksheetKey`
- `variableKey`
- `columnIndex`
- `rowIndex`

**Syntax:**

```
Write2DList {<variableKey>} in <worksheetKey> row {<rowIndex>} and column {<columnIndex>}
```

**Examples:**

```
Write2DList {subRange} in WSName row {2} and column {2}
```

*Added: 2023-Jul-10*

---

### WriteAll

> Write something in all the cells of a given column.

Write something in all the cells of a given column. The flag -visible limits the writing to those cells that are visible (i.e., after a filter). 
Original format is mainly intended for dates, to identify the origin date parts in the text. Excel formats are different from this, refer to https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings for further information. Take notice that month in "format" is mm, and in "source" is MM.
Indexes start with 1.

**Parameters:**
- `something`
- `worksheetKey`
- `cell`
- `format`
- `originalFormat`

**Syntax:**

```
WriteAll "<something>" in <worksheetKey> start_at <cell>
WriteAll "<something>" in <worksheetKey> start_at <cell> -visible
WriteAll "<something>" in <worksheetKey> start_at <cell> with format <format> source <originalFormat>
WriteAll "<something>" in <worksheetKey> start_at <cell> with format <format> source <originalFormat> -visible
```

**Examples:**

```
WriteAll "Tiendas" in Sheet4 start_at B4
WriteAll "25-01-1985" in Sheet4 start_at B4 with format dd/mm/yyyy source dd-MM-yyyy
WriteAll "Filtrada" in Sheet4 start_at B4 -visible
```

*Added: 2017-Aug-01*

---

### WriteFormula

> Write a formula in a given cell or range of visible cells.

Write a formula in a given cell or range of visible cells. Use "LastRow" when the last row is unknown. Values hidden due to applied filters will not be affected. "Paste only value" syntax will not paste formulas, but the result value instead. 
When the formula uses quotation marks ("), it is best to use key syntax ({}). 
[IMPORTANT] In runtime, Excel formulas are expected in English and with the comma as separator: Example: =IF(A1>10,"Correct","Incorrect")

**Parameters:**
- `worksheetKey`
- `rangeKey`
- `formula`

**Syntax:**

```
WriteFormula <worksheetKey> in <rangeKey> formula "<formula>"
WriteFormula <worksheetKey> in <rangeKey> formula <formula>
WriteFormula <worksheetKey> in <rangeKey> formula {<formula>}
WriteFormula <worksheetKey> in <rangeKey> formula "<formula>" paste only value
WriteFormula <worksheetKey> in <rangeKey> formula <formula> paste only value
WriteFormula <worksheetKey> in <rangeKey> formula {<formula>} paste only value
```

**Examples:**

```
WriteFormula WSExampleName in Q2:Q400 formula =IF(A2 > 10 , "Correct" , "Incorrect")
WriteFormula WSExampleName in Q2:LastRow formula =IF(A2 > 10 , "Correct" , "Incorrect")
WriteFormula sociedadesS in B9 formula "=VLOOKUP(A1, $A$1:$G$15,7,FALSE)"
```

*Added: 2017-Aug-23*

---

### WriteFormulaVisible

> Write a formula in a cell or range.

Write a formula in a specified cell or range, it works if you have a filter applied. "LastRow" can be used when the last cell is unknown. "Paste only value" will apply the formula and paste the result. [IMPORTANT] In runtime, Excel formulas are expected in English and with the comma as separator: Example: =IF(A1>10,"Correct","Incorrect")

**Parameters:**
- `worksheetKey`
- `cell`
- `range`
- `formula`

**Syntax:**

```
WriteFormulaVisible <worksheetKey> in <cell or range> formula "<formula>"
WriteFormulaVisible <worksheetKey> in <cell or range> formula "<formula>" paste only value
WriteFormulaVisible <worksheetKey> in <cell or range> formula <formula>
WriteFormulaVisible <worksheetKey> in <cell or range> formula <formula> paste only value
```

**Examples:**

```
WriteFormulaVisible WSExampleName in Q2:Q400 formula =IF(A2 > 10 , "Correct" , "Incorrect")
WriteFormulaVisible WSExampleName in Q2:LastRow formula =IF(A2 > 10 , "Correct" , "Incorrect")
WriteFormulaVisible sociedadesS in B9 formula =VLOOKUP(A1, $A$1:$G$15,7,FALSE)
```

*Added: 2019-Oct-18*

---

### WriteInRange

> Write a value on an especific range of cells.

Write a value on an especific range of cells. In the end cell LastCol and LastRow can be used. Indexes start with 1.

**Parameters:**
- `worksheetKey`
- `Value`
- `StartCol`
- `StartRow`
- `EndCol`
- `EndRow`

**Syntax:**

```
WriteInRange from the worksheet <worksheetKey> the value "<value>" from the cell {<StartRowIndex>,<StartColIndex>} up to the cell {<EndRowIndex>,<EndColIndex>}
```

**Examples:**

```
WriteInRange from the worksheet worksheetName the value "10/10/2018" from the cell {2,4} up to the cell {4000,5}
WriteInRange from the worksheet worksheetName the value "10/10/2018" from the cell {2,4} up to the cell {4000,LastCol}
WriteInRange from the worksheet worksheetName the value "10/10/2018" from the cell {2,4} up to the cell {LastRow,6}
```

*Added: 2018-Sep-12*

---

### WriteList

> Write a list of values from a list variable into a range or column.

Write a list of values from a list variable into a range or column. Starting row can be indicated with start_at. Indexes start with 1.

**Parameters:**
- `varKey`
- `worksheetKey`
- `columnIndex`
- `colummnHeader`
- `rowIndex`

**Syntax:**

```
WriteList <varKey> in <worksheetKey> col_index <columnIndex> start_at <rowIndex>
WriteList <varKey> in <worksheetKey> col_header <colummnHeader> start_at <rowIndex>
```

**Examples:**

```
WriteList Nombres in WSheet3 col_index 10 start_at 2
WriteList Nombres in WSMex col_header Nombres start_at 2
```

*Added: 2017-Aug-23*

---

### WriteListOnColumn

> Write the values in a List Variable to a column on a worksheet.

Write the values in a List Variable to a column on a worksheet. Indexes start at 1. If "visible" flag is on, values will only be written in not filtered cells.

**Parameters:**
- `worksheetKey`
- `variableKey`
- `columnIndex`
- `rowIndex`
- `visibleFlag`

**Syntax:**

```
WriteListOnColumn in <worksheetKey> the variable "<variableKey>" on the column "<columnIndex>" <visibleFlag:visible|>
(Deprecated)WriteListOnColumn in <worksheetKey> the variable "<variableKey>" on the column "<columnIndex>" start_at <rowIndex> <visibleFlag:visible|>
WriteListOnColumn in <worksheetKey> the variable "<variableKey>" on the column "<columnIndex>" start_at row <rowIndex> <visibleFlag:visible|>
```

**Options:**

- `visibleFlag`: `visible`
- `visibleFlag`: `visible`
- `visibleFlag`: `visible`

**Examples:**

```
WriteListOnColumn in WSName the variable "Datos" on the column "2"
WriteListOnColumn in WSName the variable "Acceptados" on the column "2" visible
WriteListOnColumn in WSName the variable "Actividad" on the column "3" start_at row 4
```

*Added: 2019-Mar-27*

---

### WriteListOnRow

> Write the values in a List Variable to a row on a worksheet.

Write the values in a List Variable to a row on a worksheet. Available syntax to indicate a starting column index. Indexes start at 1.

**Parameters:**
- `worksheetKey`
- `variableKey`
- `columnIndex`
- `rowIndex`

**Syntax:**

```
WriteListOnRow in <worksheetKey> the variable "<variableKey>" on the row "<rowIndex>"
WriteListOnRow in <worksheetKey> the variable "<variableKey>" on the row "<rowIndex>" start_at <columnIndex>
```

**Examples:**

```
WriteListOnRow in WSName the variable "Datos" on the row "2"
WriteListOnRow in WSName the variable "Actividad" on the row "3" start_at 4
```

*Added: 2020-Nov-18*

---

### WriteTable

> Write a table in the last row of a worksheet using the given variable.

Write a table in the last row of a worksheet using the given variable. Index starts with 1.

**Parameters:**
- `worksheetKey`
- `variableKey`
- `columnIndex`

**Syntax:**

```
WriteTable in <worksheetKey> the values of "<variableKey>" in last row and column <columnIndex>
```

**Examples:**

```
WriteTable in WSheet2 the values of "Lista" in last row and column 8
```

*Added: 2017-Nov-06*

---

### WriteValueThatMatch

> Deprecated. Apply a filter to a column and write the given value to a corresponding row in another column.

Mostly deprecated. Use WriteValueThatMatches. 
Apply a filter to a column A and write the given value in the same row but in another column (column B), in case it does not exist it writes the filter in column A and the value in column B at the end of the file. "Single value" syntax will only write the first instance of the searched value. 
The column where you expect it to write must be visible to the used range, i.e. there must be at least a value somewhere in that column, for example the header.
Warning: Formulas will usually get lost in the sheet unless using "keep formulas".

**Parameters:**
- `worksheetKey`
- `ColumnAIndex`
- `ColumnBIndex2`
- `ColumnBStartIndex2`
- `Criteria`
- `value`
- `value1`
- `value2`
- `valueN`

**Syntax:**

```
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" and writing in the column {<ColumnBIndex2>} the value {<value>}
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" and writing in the column {<ColumnBIndex2>} the value {<value>} keep formulas
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" starting at {<ColumnBStartIndex2>} and writing in the column {<ColumnBIndex2>} the value {<value>} keep formulas
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" starting at {<ColumnBStartIndex2>} and writing in the column {<ColumnBIndex2>} the value {<value>}
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" and writing in the column {<ColumnBIndex2>} the single value {<value>}
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" and writing in the column {<ColumnBIndex2>} the single value {<value>} keep formulas
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" and writing in column starting at {<ColumnBStartIndex2>} the values {<value1>,<value2>....,<valueN>}
WriteValueThatMatch in the worksheet <worksheetKey> at the column {<ColumnAIndex>} matching the value "<Criteria>" and writing in column starting at {<ColumnBStartIndex2>} the values {<value1>,<value2>....,<valueN>} keep formulas
```

**Examples:**

```
WriteValueThatMatch in the worksheet wsheet at the column {1} matching the value "111001110" and writing in the column {3} the value {TicketAuthor}
WriteValueThatMatch in the worksheet wsheet at the column {1} matching the value "111001110" starting at {2} and writing in the column {8} the value {TicketAuthor}
WriteValueThatMatch in the worksheet wsheet at the column {1} matching the value "Entregado" and writing in the column {2} the single value {OK} keep formulas
```

*Added: 2018-Nov-05*

---

### WriteValueThatMatches

> Apply a filter to a column and write the given value(s) in another column(s).

Apply a filter to a column and write the given values in the same row but other columns. The quantity parameter when set to "the first", will only write the first occurrence of the searched value. 
Starting at will begin the search parting from the given row index. Write columns and values must match in number. The first value will be placed in the first column, the second value in the second column, and so on. 
"Exact" means that the value searched must be exactly it, and "part of" will look for the text being contained in the whole text of the cell. When using date filter, the date must be followed by the format it comes from. 
The column where you expect it to write must be visible to the used range, i.e. there must be at least a value somewhere in that column, for example the header. 
 If part of the text is a comma, it may be escaped with \,. 
Indexes start from 1.

**Parameters:**
- `worksheetKey`
- `searchColumn`
- `searchType`
- `searchText`
- `searchAmount`
- `writeColumns`
- `writeValues`

**Syntax:**

```
WriteValueThatMatches in worksheet {<worksheetKey>} column {<searchColumn>} matching <searchType:exact|part of|date> {<searchText>} and writing {<searchAmount:first|all>} found in columns [<writeColumns>] the values [<writeValues>]
WriteValueThatMatches in worksheet {<worksheetKey>} column {<searchColumn>} matching <searchType:exact|part of|date> {<searchText>} and writing {<searchAmount:first|all>} found in columns [<writeColumns>] the values [<writeValues>] starting at {<startAtRow>}
```

**Options:**

- `searchType`: `exact`, `part of`, `date`
- `searchAmount`: `first`, `all`
- `searchType`: `exact`, `part of`, `date`
- `searchAmount`: `first`, `all`

**Examples:**

```
WriteValueThatMatches in worksheet {wsheet} column {4} matching exact {Ticket} and writing {first} found in columns [2,5] the values [Working on, 1\,234]
WriteValueThatMatches in worksheet {wsheet} column {3} matching exact {Shop} and writing {all} found in columns [2] the values [Softtek] starting at {6}
WriteValueThatMatches in worksheet {wsheet} column {2} matching part of {Err-} and writing {all} found in columns [6,7,8] the values [Assigned,Joe,Dow]
```

*Added: 2022-Apr-05*

---

### WriteVariableValue

> Write the data saved in a variable, to a given cell location.

Write the data saved in a variable, to a given cell location. Indexes start with 1. Row index can be "LastRow".

**Parameters:**
- `worksheetKey`
- `columnIndex`
- `rowIndex`
- `variableName`

**Syntax:**

```
WriteVariableValue {<variableName>} in {<worksheetKey>} start_at_row {<rowIndex>} start_at_column {<columnIndex>}
```

**Examples:**

```
WriteVariableValue {filtrado} in {wsheet1} start_at_row {1} start_at_column {1}
WriteVariableValue {filtrado} in {wsheet1} start_at_row {LastRow} start_at_column {1}
```

*Added: 2019-Jun-04*

---

### Zoom

> Apply Zoom in a given worksheet.

Apply Zoom in a given worksheet.

**Parameters:**
- `worksheetKey`
- `number`

**Syntax:**

```
Zoom in <worksheetKey> number <number>
```

**Examples:**

```
Zoom in workSheet number 80
```

*Added: 2018-Mar-02*

---
