# FRIDA Readers JSON Schema Reference

This document describes the structure of `readers.json`, the comprehensive documentation database for the FRIDA RPA (Robotic Process Automation) tool.

## File Overview

- **File**: `readers.json`
- **Size**: ~18,670 lines
- **Last Update**: 2025-04-02T18:13:40
- **Purpose**: Contains documentation for all FRIDA Reader modules, their functions, syntax, parameters, and examples

## Top-Level Structure

```json
{
  "0": { /* Excel Reader */ },
  "1": { /* MagicSelenium (deprecated) */ },
  "2": { /* MagicSelenium (deprecated) */ },
  "3": { /* SAP Reader */ },
  "4": { /* Powerpoint Reader */ },
  "5": { /* Mix Reader */ },
  "6": { /* Outlook Reader */ },
  "7": { /* Browpet Reader */ },
  "8": { /* Word Reader */ },
  "9": { /* DB Reader */ },
  "10": { /* File Reader */ },
  "ActionRating": { /* User ratings data */ },
  "Authorized": [ /* Authorized user emails */ ],
  "LastUpdate": "ISO 8601 timestamp"
}
```

## Reader Object Schema

Each Reader (numbered key) has the following structure:

| Field | Type | Description |
|-------|------|-------------|
| `ID` | number | Unique identifier for the reader |
| `Name` | string | Display name (e.g., "Excel Reader") |
| `Description` | string | Full description of the reader's purpose |
| `Keyword` | string | Prefix keyword for commands (e.g., "Excel", "SAP", "Word") |
| `_FAdminKey` | string | Internal admin key |
| `Function` | array | Array of function objects |

### Example Reader Object

```json
{
  "Description": "Excel reader is a C# based tool designed to automate your spreadsheets...",
  "Function": [ /* array of function objects */ ],
  "ID": 0,
  "Keyword": "Excel",
  "Name": "Excel Reader",
  "_FAdminKey": "Excel"
}
```

## Function Object Schema

Each function within a Reader's `Function` array has:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Name` | string | Yes | Function identifier (e.g., "Append", "CopyPaste") |
| `Description` | string | Yes | Full explanation of what the function does |
| `ShortDescription` | string | No | Brief one-line summary |
| `Syntax` | array | Yes | Array of syntax patterns with `<param>` placeholders |
| `SyntaxDetail` | array | No | Detailed syntax with constants/options |
| `Example` | array | No | Array of usage examples |
| `Params` | array | No | Array of parameter names |
| `CreationDate` | string | No | Date function was added (format: "YYYY-Mon-DD") |
| `ExtraDocs` | string | No | URL to additional PDF documentation |
| `Videos` | array | No | Array of URLs to video tutorials |

### Example Function Object

```json
{
  "Name": "Append",
  "CreationDate": "2017-Nov-13",
  "Description": "Adds a value at the end of the columns in a sheet...",
  "ShortDescription": "Adds a value at the end of the columns in a sheet.",
  "Params": ["worksheetKey", "index", "text"],
  "Syntax": [
    "Append from <worksheetKey> at [<index1> =\"<text>\",<index2> =\"<text>\",...,<indexN> =\"<text>\"]"
  ],
  "SyntaxDetail": [
    {
      "Instruction": "Append from <worksheetKey> at [<index1> =\"<text>\",...]"
    }
  ],
  "Example": [
    "Append from wsGE at [2 =\"='[zvf05_prueba.xls]Process'!$B$narow\",4 =\"='[zvf05_prueba.xls]Process'!$D$narow\"]\r",
    "Append from libro at [1 =\"Total\",2 =\"=Sum(B2:B4)\"]\r"
  ]
}
```

## SyntaxDetail Object Schema

The `SyntaxDetail` array contains objects with:

| Field | Type | Description |
|-------|------|-------------|
| `Instruction` | string | The syntax pattern with placeholders |
| `Constants` | array | Optional array of constant options |

### Constants Object

```json
{
  "ParamName": "hasHeader",
  "Options": ["Y", "N"]
}
```

This indicates that the parameter `hasHeader` must be one of: `Y` or `N`.

## Syntax Placeholder Conventions

| Pattern | Meaning |
|---------|---------|
| `<paramName>` | Required parameter placeholder |
| `<param:opt1\|opt2\|opt3>` | Parameter with enumerated options |
| `{<paramName>}` | Parameter wrapped in braces |
| `\"<paramName>\"` | Parameter wrapped in quotes |
| `[<param1>,<param2>]` | Array/list of parameters |

## Variable Interpolation Syntax

FRIDA uses special syntax for variable interpolation:

| Syntax | Description |
|--------|-------------|
| `<<<varName>>>` | Runtime variable interpolation (resolves immediately) |
| `<<varName>>` | Global/input variable reference |
| `{VariableName}` | Alternative variable reference |

## ActionRating Schema

User ratings for functions:

```json
{
  "ReaderName%20URL-encoded": {
    "FunctionName": {
      "timestamp": {
        "Date": "ISO timestamp",
        "Rating": 1-5,
        "User": "user ID or email"
      }
    }
  }
}
```

## Authorized Schema

Array of authorized user email addresses:

```json
[
  "user1@softtek.com",
  "user2@softtek.com"
]
```

## Data Types Reference

| Type | Description |
|------|-------------|
| `worksheetKey` | Reference to a loaded Excel worksheet |
| `workbookKey` | Reference to a loaded Excel workbook |
| `documentKey` | Reference to a loaded Word document |
| `GridId` | SAP GUI grid element identifier |
| `ElementId` | SAP GUI element path |
| `dbKey` | Database connection reference |
| `listName` | Name of a list variable |
| `varName` | Name of any variable |
