# FRIDA Syntax Cheatsheet

Quick reference for the most commonly used FRIDA patterns and syntax.

## Variable Syntax

### Variable Interpolation

| Syntax | Description | Example |
|--------|-------------|---------|
| `<<<varName>>>` | Runtime variable (resolves immediately) | `<<<Contador>>>` |
| `<<varName>>` | Global/input variable | `<<sapUser>>` |
| `{varName}` | Alternative reference | `{WSName}` |

### Variable Declaration

```
DefineVariable as "myVar" with the value "Hello"
DefineVariable type "int" as "counter" with the value "0"
DefineVariable type "List" as "myList"
```

### Variable Operations

```
## Increment
counter++

## Math operations
MathOperation <<<value1>>> + <<<value2>>> and save as result
MathOperation <<<value1>>> - <<<value2>>> and save as result
MathOperation <<<value1>>> * <<<value2>>> and save as result
MathOperation <<<value1>>> / <<<value2>>> and save as result

## String replacement
ReplaceFromVariable {myVar} this {oldText} for {newText}
```

## Control Flow

### For Loop

```
for <N> times {
    ## Code here
}

## Example with counter
for 10 times {
    Message "Iteration: <<<Contador>>>"
    Contador++
}
```

### ForEach Loop

```
foreach item in myList {
    Message "Item: <<<item>>>"
}
```

### While Loop

```
while (<<<condition>>>) {
    ## Code here
}
```

### If/Else Conditionals

```
if ("<<<variable>>>" -eq "value")
    ## Code for true
end

if ("<<<variable>>>" -ne "value")
    ## Code for not equal
else
    ## Code for equal
end

if (<<<number>>> > 10)
    ## Greater than
end

if (<<<number>>> <= 5)
    ## Less than or equal
end
```

### Switch Statement

```
switch (<<<expression>>>) {
    case "value1" :
        ## Code for value1
    end
    case "value2" :
        ## Code for value2
    end
    default :
        ## Default code
    end
}
```

### Try/Catch

```
try
    ## Risky code here
catch
    ## Error handling
end

try
    ## Risky code
catch as ex
    ## ex contains error message
    Message "Error: <<<ex>>>"
end
```

## Lists

### Create and Populate Lists

```
DefineVariable type "List" as "myList"
AddValueToList "myList" value "item1"
AddValueToList "myList" value {"item2", "item3", "item4"}
AddVarToList "myList" value "myVariable"
```

### List Operations

```
## Count items
CountItems in myList and save_as itemCount

## Filter list
ApplyFilterInList {myList} find {all} match contents {exact} with values [value1,value2] and save as {filteredList}

## Get item at index
Get2DListItem from {myList} at [<<<index>>>] and save as itemValue
```

### 2D Lists

```
AddValueTo2DList "my2DList" value {"col1", "col2", "col3"}
Get2DListItem from {my2DList} at [<<<row>>>,<<<col>>>] and save as cellValue
```

## Excel Operations

### Load Workbook/Worksheet

```
Excel LoadWBook "C:\path\to\file.xlsx" as WBName
Excel LoadWSheet WBName sheet "Sheet1" as WSName
```

### Read Cells

```
Excel ReadCell from the worksheet WSName from the cell {<<<row>>>,<<<col>>>} and save its value as {cellValue}
Excel ReadCellText from the worksheet {WSName} from the cell {1,1} and save its value as {headerText}
Excel ReadColumn from the worksheet {WSName} with the column index {1} start_at {2} and save its value as {columnData} visible without nulls
```

### Write Cells

```
Excel WriteCell from the worksheet {WSName} with text "Hello" in the cell with index {1,1}
Excel Append from WSName at [1 ="Value1",2 ="Value2"]
```

### Save and Close

```
Excel Save WBName
Excel Save WBName and close
```

## SAP Operations

### Connect to SAP

```
SAP RunSapInstance "Connection Name" <client> <<user>> <<password>> <language> graphic
```

### Navigation

```
SAP StartTransaction <tcode>
SAP SendKey 0
SAP ClickButton id <buttonId>
```

### Read/Write

```
SAP ReadElement <elementId> as variableName
SAP WriteText ElementId <elementId> Text "<<<value>>>"
```

### Grids and Tables

```
SAP ReadGridCell GridId <gridId> RowN <row> Column "<column>" as value
SAP VerticalScroll GridId <gridId> Pos <position>
```

### Trees

```
SAP SelectTreeItem TreeId <treeId> Node "<node>" Item "<item>"
SAP DoubleClickTreeItem TreeId <treeId> Node "<node>" Item "<item>"
```

## File Operations

### Check/Create

```
File CheckIfDirExist in the path "C:\path" with the name "folder"
File NewFolder in "C:\path" with the name "newFolder"
```

### Read/Write

```
File GetAllLines from "C:\path\file.txt" and save in "linesVariable"
WriteAllLines from the variable "myList" in the file "C:\path\output.txt"
WriteAllText from the variable "myVar" in the file "C:\path\output.txt"
```

### Copy/Move

```
File CopyFile from "C:\source\file.txt" to "C:\dest\file.txt"
File MoveFile from "C:\source\file.txt" to "C:\dest\"
```

## Utility Functions

### Date and Time

```
GetCurrentDate format={"yyyy-MM-dd_HH-mm-ss" en} and save as timestamp
GetCurrentDate format={"MM/dd/yyyy HH:mm:ss" en} and save as readableDate
```

### Path Operations

```
GetHome as "home"
## Result: C:\Users\username\
```

### Regex

```
ApplyRegex "pattern" to the string "<<<input>>>" and save as "result"
ApplyRegex "(?<=prefix)(.*)(?=suffix)" to the string "<<<text>>>" and save as "extracted"
```

### String Operations

```
Trim variableName
Trim variableName and save as trimmedVar
Substring "Hello World" start 0 length 5 and save as "sub"
```

### Messaging

```
Message "Display this message"
SystemNotify Type "Notification" with message "Task completed"
SystemNotify Type "Validation" with message "Continue?"
```

## Common Patterns

### Excel + Loop Pattern

```
Excel LoadWBook "<<<filePath>>>" as WB
Excel LoadWSheet WB sheet "Data" as WS
Excel ReadColumn from the worksheet {WS} with the column index {1} start_at {2} and save its value as {items} visible without nulls
CountItems in items and save_as totalItems

DefineVariable type "int" as "row" with the value "2"
for <<<totalItems>>> times {
    Excel ReadCell from the worksheet WS from the cell {<<<row>>>,1} and save its value as {currentItem}
    ## Process currentItem
    row++
}
```

### SAP Transaction Pattern

```
try
    SAP StartTransaction <tcode>
    ## Fill fields
    SAP WriteText ElementId <field1> Text "<<<value1>>>"
    SAP SendKey 0
    ## Execute
    SAP ClickButton id wnd[0]/tbar[1]/btn[8]
catch as ex
    Message "Error: <<<ex>>>"
end
```

### Resume/Checkpoint Pattern

```
## Track processed items in separate sheet
Excel ReadColumn from the worksheet {WSProcessed} with the column index {1} start_at {2} and save its value as {processed} visible without nulls
CountItems in processed and save_as totalProcessed
MathOperation <<<totalProcessed>>> + 2 and save as startRow

## Process remaining
for <<<remaining>>> times {
    ## Process item
    ## Log success
    Excel Append from WSProcessed at [1 ="<<<rowNum>>>",2 ="SUCCESS",3 ="<<<timestamp>>>"]
    Excel Save WB
}
```

## Comparison Operators

| Operator | Meaning |
|----------|---------|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-lt` | Less than |
| `-le` | Less than or equal |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |
| `-like` | Pattern match (wildcards) |
| `-match` | Regex match |

## Script Structure Best Practices

```
#%region SECTION_NAME ─────────────────────────────────────
## Description of this section

## Code here

#%endregion
```

## Comments

```
## This is a comment
##This is also a comment
```
