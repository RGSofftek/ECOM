# Word Reader

**Keyword:** `Word`

**Functions:** 34

## Description

Word Reader will allow you to automate the creation of Microsoft Word documents such as reports or evidences, allowing you to add images and paragraphs in an automated way.

## Quick Reference

| Function | Description |
|----------|-------------|
| [AppendParagraph](#appendparagraph) | Write text at the end of the document, creating a new paragraph. |
| [AppendText](#appendtext) | Write text at the end of the document, inside the last paragraph. |
| [AutoFitTable](#autofittable) | Change the size of a table in word using auto fit. |
| [ChangeTableIndent](#changetableindent) | Change the indent of a table in word. |
| [ChangeTableStyle](#changetablestyle) | Change the style of an specific table. |
| [CleanDocument](#cleandocument) | Delete the text from the whole document. |
| [Close](#close) | Close an open Word document. |
| [CreateCustomProperty](#createcustomproperty) | Create a document custom property in an specific book. |
| [CurrentPosition](#currentposition) | Get the current position of the insertion point. |
| [DeleteComments](#deletecomments) | Delete comments from a document. |
| [DeleteCustomProperty](#deletecustomproperty) | Delete an specific custom property in a document by name. |
| [DeleteTable](#deletetable) | Delete a table in the document. |
| [Dispose](#dispose) | Close all Word documents without saving any changes. |
| [FindText](#findtext) | Find a text in the given Word document. |
| [GetMailMergeCount](#getmailmergecount) | Save the number of records from a mail merge source. |
| [GetNumberOfPages](#getnumberofpages) | Returns the number of pages in a given Word document. |
| [GoTo](#goto) | Move the cursor to a place in the document. |
| [InsertField](#insertfield) | Insert a field by name in a word document. |
| [InsertImage](#insertimage) | Inserts an image into a Word document. |
| [InsertImages](#insertimages) | Insert all the images from a folder into a Word document. |
| [InsertJSONTable](#insertjsontable) | Insert a table in a document based on a JSON. |
| [LoadDocument](#loaddocument) | Open a Word document. |
| [LoadHtmlInDoc](#loadhtmlindoc) | Open an html file as a Word document. |
| [ModifyCustomProperty](#modifycustomproperty) | Modify an specific custom property in a document. |
| [ModifyProperty](#modifyproperty) | Modify an specific property value in a document. |
| [NewDocument](#newdocument) | Create a new Word document. |
| [PreviewRecord](#previewrecord) | Preview the results from a certain record of a mail merged document. |
| [ReadText](#readtext) | Read the text of a page in the given Word document. |
| [ResizeTable](#resizetable) | Change the size of a table in word. |
| [Save](#save) | Save a Word document. |
| [SaveDocAs](#savedocas) | Save a Word document with a diferent name. |
| [SelectRecipients](#selectrecipients) | Select the recipients in a mail merged document. |
| [SetFontStyle](#setfontstyle) | Set a font style to a selection of text in the given Word document. |
| [WriteText](#writetext) | Write a text in the given Word document. |

---

## Functions

### AppendParagraph

> Write text at the end of the document, creating a new paragraph.

Writes text at the end of the document, creating a new paragraph.

**Parameters:**
- `DocumentKey`
- `Text`

**Syntax:**

```
AppendParagraph to <DocumentKey> <Text>
```

**Examples:**

```
AppendParagraph to Document1Key New paragraph goes here
```

*Added: 2019-Jul-03*

---

### AppendText

> Write text at the end of the document, inside the last paragraph.

Writes text at the end of the document, inside the last paragraph.

**Parameters:**
- `DocumentKey`
- `Text`

**Syntax:**

```
AppendText to <DocumentKey> <Text>
```

**Examples:**

```
AppendText to Document1Key New text at the end of the document, inside the last paragraph
```

*Added: 2019-Jul-03*

---

### AutoFitTable

> Change the size of a table in word using auto fit.

Changes the sizeof a table in word. It can be donde by autofitting the contents, expanding to the with of the window or fixed column with, the way it is done in a regular word table. 
Title is the one placed in the table's properties. Index begins with 1 and will count tables in in order of appearance.

**Parameters:**
- `documentKey`
- `tableTitle`
- `tableIndex`
- `autoFitType`

**Syntax:**

```
AutoFitTable from document {<documentKey>} in table title {<tableTitle>} type {<autoFitType:autofit to contents|autofit to window|fixed column width>}
AutoFitTable from document {<documentKey>} in table order {<tableIndex>} type {<autoFitType:autofit to contents|autofit to window|fixed column width>}
```

**Options:**

- `autoFitType`: `autofit to contents`, `autofit to window`, `fixed column width`
- `autoFitType`: `autofit to contents`, `autofit to window`, `fixed column width`

**Examples:**

```
AutoFitTable from document {doc1} in table title {Totals} type {autofit to window}
AutoFitTable from document {doc1} in table order {1} type {autofit to contents}
```

*Added: 2022-Dec-15*

---

### ChangeTableIndent

> Change the indent of a table in word.

Change the indent of a table in word by specifying the table title. The LeftIndent units are millimeters.

**Parameters:**
- `DocumentKey`
- `TableTitle`
- `LeftIndent`

**Syntax:**

```
ChangeTableIndent from the document {<DocumentKey>} with the table title {<TableTitle>} to {<LeftIndent>} millimeters
```

**Examples:**

```
ChangeTableIndent from the document {Book1Key} with the table title {Table1} to {-27.6} millimeters
```

*Added: 2021-Jan-19*

---

### ChangeTableStyle

> Change the style of an specific table.

Change the style of an specific table by selecting an existing style by its name. Table Grid, Plain Table 2, Grid Table 5 Dark, Grid Table 3 are some examples of all the posibles styles that can be used. Custom styles can also be selected just specifing the name. If the language of Word its different to english then use the style names available.

**Parameters:**
- `DocumentKey`
- `TableTitle`
- `StyleName`

**Syntax:**

```
ChangeTableStyle in the document {<DocumentKey>} with the table title {<TableTitle>} to {<StyleName:Table Grid|Plain Table 2|Grid Table 5 Dark|Grid Table 3>}
```

**Options:**

- `StyleName`: `Table Grid`, `Plain Table 2`, `Grid Table 5 Dark`, `Grid Table 3`

**Examples:**

```
ChangeTableStyle in the document {Book1Key} with the table title {Table1} to {Table Grid}
```

*Added: 2021-Jan-14*

---

### CleanDocument

> Delete the text from the whole document.

Delete the text from the whole document.

**Parameters:**
- `DocKey`

**Syntax:**

```
CleanDocument {<DocKey>}
```

**Examples:**

```
CleanDocument {Doc1Key}
```

*Added: 2019-Aug-12*

---

### Close

> Close an open Word document.

Close an existing document by a given documentKey.

**Parameters:**
- `documentKey`

**Syntax:**

```
Close <documentKey>
```

**Examples:**

```
Close doc
```

*Added: 2020-Jul-06*

---

### CreateCustomProperty

> Create a document custom property in an specific book.

Create a document custom property in an specific book. These options (text|date|number|yes or no) can be selected for the document property type. The second syntax is to check the "link to content" box, it is unchecked by default. When the "yes or no" type its selected just the values "true" or "false" can be used.

**Parameters:**
- `DocumentKey`
- `PropertyName`
- `PropertyType`
- `PropertyValue`

**Syntax:**

```
CreateCustomProperty in {<DocumentKey>} with the name {<PropertyName>}, type {<PropertyType:text|date|number|yes or no>} and value {<PropertyValue>}
CreateCustomProperty in {<DocumentKey>} with the name {<PropertyName>}, type {<PropertyType:text|date|number|yes or no>} and value {<PropertyValue>} link to content checked
```

**Options:**

- `PropertyType`: `text`, `date`, `number`, `yes or no`
- `PropertyType`: `text`, `date`, `number`, `yes or no`

**Examples:**

```
CreateCustomProperty in {Doc1Key} with the name {Field1}, type {text} and value {Text in the field}
CreateCustomProperty in {Doc1Key} with the name {Checked by}, type {text} and value {Inspector 1} link to content checked
```

*Added: 2020-Dec-22*

---

### CurrentPosition

> Get the current position of the insertion point.

Get the current position of the insertion point. Positions within Tables, Footnotes, Headings, Sections, etc are not supported yet.

**Parameters:**
- `documentKey`
- `varName`

**Syntax:**

```
CurrentPosition from {<documentKey>} save as {<varName>}
```

**Examples:**

```
CurrentPosition from {doc1} save as {myPosition}
```

*Added: 2023-Feb-09*

---

### DeleteComments

> Delete comments from a document.

Delete certain comments from your document. Can be all of them of only that are shown.

**Parameters:**
- `DocKey`

**Syntax:**

```
DeleteComments {<DocKey>} all
DeleteComments {<DocKey>} only shown
```

**Examples:**

```
DeleteComments {Doc1Key} all
DeleteComments {Doc1Key} only shown
```

*Added: 2019-Aug-12*

---

### DeleteCustomProperty

> Delete an specific custom property in a document by name.

Delete an specific custom property in a document by name.

**Parameters:**
- `DocumentKey`
- `PropertyName`

**Syntax:**

```
DeleteCustomProperty from {<DocumentKey>} with the name {<PropertyName>}
```

**Examples:**

```
DeleteCustomProperty from {Doc1Key} with the name {Field1}
```

*Added: 2020-Dec-22*

---

### DeleteTable

> Delete a table in the document.

Delete a table by index or by title within the document. Indexes start with 1.

**Parameters:**
- `documentKey`
- `tableTitle`
- `tableIndex`

**Syntax:**

```
DeleteTable in {<documentKey>} with the table index {<tableIndex>}
DeleteTable in {<documentKey>} with the table title {<tableTitle>}
```

**Examples:**

```
DeleteTable in {doc1} with the table index {1}
DeleteTable in {doc1} with the table title {document versions}
```

*Added: 2022-Jan-30*

---

### Dispose

> Close all Word documents without saving any changes.

Closes all Word documents without saving any changes and kills all Word instances in the machine.

**Syntax:**

```
Dispose
```

**Examples:**

```
Dispose
```

*Added: 2020-Jul-07*

---

### FindText

> Find a text in the given Word document.

Find a text from a given Word document and save the start and end indexes in a 2Dlist. You can look for "next" or "all" repetitions. 
Find next starts searching from the current insertion point. If the list is empty, it means there are no more repetitions. Wildcard syntax is as Word defines it.

**Parameters:**
- `documentKey`
- `searchText`
- `searchType`
- `listVariableName`

**Syntax:**

```
FindText from {<documentKey>} text {<searchText>} look for {<searchType:next|all>} and save as {<listVariableName>}
FindText from {<documentKey>} wildcards {<searchText>} look for {<searchType:next|all>} and save as {<listVariableName>}
```

**Options:**

- `searchType`: `next`, `all`
- `searchType`: `next`, `all`

**Examples:**

```
FindText from {doc1} text {Name} look for {next} and save as {nextNamelist}
FindText from {doc1} wildcards {ID00-*>} look for {all} and save as {allIds}
```

*Added: 2023-Feb-09*

---

### GetMailMergeCount

> Save the number of records from a mail merge source.

Save the number of records from a mail merge source in a given variable. It is intended to be used along with "PreviewRecord next" syntax in a loop.

**Parameters:**
- `docKey`
- `variableName`

**Syntax:**

```
GetMailMergeCount in {<docKey>} and save as <variableName>
```

**Examples:**

```
GetMailMergeCount in {doc1} and save as cuentaRegistros
```

*Added: 2021-Sep-07*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/automation/ExtraDocsFRIDA/Word Reader/GetMailMergeCount.pdf)

---

### GetNumberOfPages

> Returns the number of pages in a given Word document.

Get the number of pages of a given Word document and save it in a variable.

**Parameters:**
- `documentKey`
- `variableName`

**Syntax:**

```
GetNumberOfPages of {<documentKey>} and save as {<variableName>}
```

**Examples:**

```
GetNumberOfPages of {doc1} and save as {totalPages}
```

*Added: 2022-Jan-26*

---

### GoTo

> Move the cursor to a place in the document.

Move the cursor to a place in the document. Page numbers may be specified or character position, index starts with 1. Only text in parragraphs is currently considered. Tables, Footnotes, Headings, Sections, etc are not supported yet.

**Parameters:**
- `index`
- `documentKey`

**Syntax:**

```
GoTo page {<index>} in {<documentKey>}
GoTo position {<index>} in {<documentKey>}
```

**Examples:**

```
GoTo page {3} in {doc1}
GoTo position {310} in {doc1}
```

*Added: 2023-Feb-09*

---

### InsertField

> Insert a field by name in a word document.

Insert a field by name at the beginning or at the end of a word document. Just the option "DocProperty" is available for <FieldName> parameter. The "PropertyName" is also known as a "Field property".

**Parameters:**
- `FieldName`
- `PropertyName`
- `DocumentKey`
- `formatting`
- `position`

**Syntax:**

```
InsertField type {<FieldName>} with the name {<PropertyName>} and preserve formatting {<formatting:true|false>} in the document {<DocumentKey>} at {<position:beginning|end>}
```

**Options:**

- `formatting`: `true`, `false`
- `position`: `beginning`, `end`

**Examples:**

```
InsertField type {DocProperty} with the name {Field1} and preserve formatting {true} in the document {Doc1Key} at {end}
```

*Added: 2020-Dec-21*

---

### InsertImage

> Inserts an image into a Word document.

Inserts an image (.jpg, .jpeg, .jfif, .jpe, .png, .tiff, .tif, .bmp, .dib, .rle, .bmz) given its file path into the indicated Word document. It is by default appended at the end of the document, unless you specify a placeholderText; that will trigger a Search of the text, replacing the first occurrence with the given image. Insertion within a table is done by indexes, starting with 1.

**Parameters:**
- `ImagePath`
- `DocumentKey`
- `PlaceholderText`
- `TableIndex`
- `Row`
- `Column`

**Syntax:**

```
InsertImage from {"<ImagePath>"} into {"<DocumentKey>"}
InsertImage from {"<ImagePath>"} into {"<DocumentKey>"} placeholder {"<PlaceholderText>"}
InsertImage from {"<ImagePath>"} into {"<DocumentKey>"} in table <TableIndex> cell [<Row>,<Column>]
```

**Examples:**

```
InsertImage from {"C:\Users\username\Pictures\Image.png"} into {"doc1Key"}
InsertImage from {"C:\Users\username\Pictures\Image.png"} into {"doc1Key"} placeholder {"imagePlaceholder"}
InsertImage from {"C:\Users\username\Pictures\Image.png"} into {"doc1Key"} in table 1 cell [1,3]
```

*Added: 2019-Nov-21*

---

### InsertImages

> Insert all the images from a folder into a Word document.

Inserts all the images (.jpg, .jpeg, .jfif, .jpe, .png, .tiff, .tif, .bmp, .dib, .rle, .bmz) found in the given folder path into the given Word document. A horizontal line after each image is optional. The images can be inserted in reverse order.

**Parameters:**
- `FolderPath`
- `DocumentKey`
- `lineSep`
- `reverse`

**Syntax:**

```
InsertImages from folder {"<FolderPath>"} into {"<DocumentKey>"} with line separator {"<lineSep:Yes|No>"} in reverse order {"<reverse:Yes|No>"}
```

**Options:**

- `lineSep`: `Yes`, `No`
- `reverse`: `Yes`, `No`

**Examples:**

```
InsertImages from folder {"C:\Users\username\Pictures"} into {"Document1Key"} with line separator {"Yes"} in reverse order {"No"}
```

*Added: 2019-Nov-21*

---

### InsertJSONTable

> Insert a table in a document based on a JSON.

Insert a table at the beginning or at the end of a document based on a JSON in a txt file. This is an example of a JSON that can be used in this function [["1","Number","Name","Sec"],["2","12345","John Simth","0"]]. If the variable syntax is used the variable value must be a list of objects or a list of lists of strings.

**Parameters:**
- `DocumentKey`
- `FilePath`
- `TableTitle`
- `VariableName`
- `JSONString`
- `position`

**Syntax:**

```
InsertJSONTable from {<JSONString>} in the document {<DocumentKey>} at {<position:beginning|end>}
InsertJSONTable from {<JSONString>} in the document {<DocumentKey>} at {<position:beginning|end>} with the title {<TableTitle>}
InsertJSONTable from the file {<FilePath>} in the document {<DocumentKey>} at {<position:beginning|end>}
InsertJSONTable from the file {<FilePath>} in the document {<DocumentKey>} at {<position:beginning|end>} with the title {<TableTitle>}
InsertJSONTable from the variable {<VariableName>} in the document {<DocumentKey>} at {<position:beginning|end>}
InsertJSONTable from the variable {<VariableName>} in the document {<DocumentKey>} at {<position:beginning|end>} with the title {<TableTitle>}
```

**Options:**

- `position`: `beginning`, `end`
- `position`: `beginning`, `end`
- `position`: `beginning`, `end`
- `position`: `beginning`, `end`
- `position`: `beginning`, `end`
- `position`: `beginning`, `end`

**Examples:**

```
InsertJSONTable from {[["1","Number","Name","Sec"],["2","12345","John Simth","0"]]} in the document {Book1Key} at {end}
InsertJSONTable from {[["1","Number","Name","Sec"],["2","12345","John Simth","0"]]} in the document {Book1Key} at {beginning} with the title {Table1}
InsertJSONTable from the file {C:\Users\user\Downloads\PruebaJSON.txt} in the document {Book1Key} at {beginning}
```

*Added: 2021-Jan-14*

---

### LoadDocument

> Open a Word document.

Loads a document from a local path to the docs dictionary.

**Parameters:**
- `FilePath`
- `DocumentKey`

**Syntax:**

```
LoadDocument "<FilePath>" as <DocumentKey>
```

**Examples:**

```
LoadDocument "c:\Users\username\Desktop\MyDoc.docx" as DocumentKey
```

*Added: 2019-Jul-03*

---

### LoadHtmlInDoc

> Open an html file as a Word document.

Loads an HTML document from a local path as a Word document and saves it in a variable.

**Parameters:**
- `FilePath`
- `DocumentKey`

**Syntax:**

```
LoadHtmlInDoc "<FilePath>" as <DocumentKey>
```

**Examples:**

```
LoadHtmlInDoc "c:\Users\username\Desktop\MyDoc.html" as DocumentKey
```

*Added: 2024-Oct-28*

---

### ModifyCustomProperty

> Modify an specific custom property in a document.

Modify an specific custom property in a document. When the type is modified, the value of the property will be null. To give the property a value it can be use the value syntax.

**Parameters:**
- `DocumentKey`
- `PropertyName`
- `PropertyValue`
- `PropertyType`

**Syntax:**

```
ModifyCustomProperty from {<DocumentKey>} with the name {<PropertyName>} to the value {<PropertyValue>}
ModifyCustomProperty from {<DocumentKey>} with the name {<PropertyName>} to the type {<PropertyType:text|date|number|yes or no>}
```

**Options:**

- `PropertyType`: `text`, `date`, `number`, `yes or no`

**Examples:**

```
ModifyCustomProperty from {Doc1Key} with the name {Checked by} to the value {Text in the field}
ModifyCustomProperty from {Doc1Key} with the name {Field1} to the type {text}
```

*Added: 2020-Dec-22*

---

### ModifyProperty

> Modify an specific property value in a document.

Modify an specific property value in a document.

**Parameters:**
- `DocumentKey`
- `PropertyName`
- `PropertyValue`
- `position`

**Syntax:**

```
ModifyProperty from {<DocumentKey>} with the name {<PropertyName>} to the value {<PropertyValue>}
```

**Examples:**

```
ModifyProperty from {Doc1Key} with the name {Checked by} to the value {Text in the field}
```

*Added: 2020-Dec-22*

---

### NewDocument

> Create a new Word document.

Creates a new Word document in a given local path. The document name must be given. Support only for .docx

**Parameters:**
- `FolderPath`
- `FileName`
- `DocumentKey`

**Syntax:**

```
NewDocument in {"<FolderPath>"} named {"<FileName>"} as {"<DocumentKey>"}
```

**Examples:**

```
NewDocument in {"C:\Users\username\Desktop"} named {"Document2.docx"} as {"Document2Key"}
```

*Added: 2019-Nov-20*

---

### PreviewRecord

> Preview the results from a certain record of a mail merged document.

Preview the mailing results from a given a record number or a recipient to be found by value in a mail merged document. First, last, next, previous syntax will preview mail merge with the records in the given position. When looking for an especific record, fieldName + value can be used.

**Parameters:**
- `docKey`
- `fieldName`
- `fieldValue`
- `recordPosition`

**Syntax:**

```
PreviewRecord {<recordPosition:first|last|next|previous>} in {<docKey>}
PreviewRecord with field {<fieldName>} and value {<fieldValue>} in {<docKey>}
```

**Options:**

- `recordPosition`: `first`, `last`, `next`, `previous`

**Examples:**

```
PreviewRecord {next} in {documento}
PreviewRecord with field {Apellido} and value {Juarez} in {Contrato}
```

*Added: 2021-Sep-07*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/automation/ExtraDocsFRIDA/Word Reader/PreviewRecord.pdf)

---

### ReadText

> Read the text of a page in the given Word document.

Read the text contained in a page of a given Word document and save it in a list variable. Page number may be specified, index starts with 1.

**Parameters:**
- `documentKey`
- `pageNumber`
- `listVariableName`

**Syntax:**

```
ReadText of {<documentKey>} in page {<pageNumber>} and save as {<listVariableName>}
ReadText of {<documentKey>} and save as {<listVariableName>}
```

**Examples:**

```
ReadText of {doc1} in page {1} and save as {textFirstPage}
ReadText of {doc1} and save as {allText}
```

*Added: 2022-Jan-26*

---

### ResizeTable

> Change the size of a table in word.

Change the total size, cells height size (row) or cells width size (column) of a table in word. For some syntaxis it can be specified by percentage or by millimeters.

**Parameters:**
- `DocumentKey`
- `CellsHeight`
- `CellsWidth`
- `Aproximation`
- `Unit`
- `TableTitle`
- `TableSize`

**Syntax:**

```
ResizeTable by <Unit:percentage|millimeters> to {<TableSize>} in the document {<DocumentKey>} with the table title {<TableTitle>}
ResizeTable cells height by millimeters to <Aproximation:at least|exactly> {<CellsHeight>} in the document {<DocumentKey>} with the table title {<TableTitle>}
ResizeTable cells width by <Unit:percentage|millimeters> to {<CellsWidth>} in the document {<DocumentKey>} with the table title {<TableTitle>}
```

**Options:**

- `Unit`: `percentage`, `millimeters`
- `Aproximation`: `at least`, `exactly`
- `Unit`: `percentage`, `millimeters`

**Examples:**

```
ResizeTable by percentage to {50} in the document {Book1Key} with the table title {Table1}
ResizeTable by millimeters to {200} in the document {Book1Key} with the table title {Table1}
ResizeTable cells height by millimeters to exactly {40} in the document {Book1Key} with the table title {Table1}
```

*Added: 2021-Jan-19*

---

### Save

> Save a Word document.

Saves a document in its original path.

**Parameters:**
- `DocumentKey`

**Syntax:**

```
Save <DocumentKey>
```

**Examples:**

```
Save Document1Key
```

*Added: 2019-Jul-31*

---

### SaveDocAs

> Save a Word document with a diferent name.

Save a document with a diferent name, with the changes made at the original file. This file is saved in the same path as the original file. It can be saved in .docx or .pdf format.

**Parameters:**
- `DocKey`
- `FileName`

**Syntax:**

```
SaveDocAs {<DocKey>} as {<FileName>}
SaveDocAs PDF {<DocKey>} as {<FileName>}
```

**Examples:**

```
SaveDocAs {DocKey} as {Doc_Edited}
SaveDocAs pdf {DocKey} as {docPdfVersion}
```

*Added: 2019-Jul-29*

---

### SelectRecipients

> Select the recipients in a mail merged document.

Select the recipients in a mail merged document. The source file must be an excel file with a table with headers. Only letter type mail merge is available.

**Parameters:**
- `docKey`
- `excelFilePath`
- `sheetName`

**Syntax:**

```
SelectRecipients in {<docKey>} from the excel source {<excelFilePath>} sheet {<sheetName>}
```

**Examples:**

```
SelectRecipients in {libro} from the excel source {C:\Users\user.surname\Documentos\source.xlsx} sheet {Sheet1}
```

*Added: 2021-Sep-07*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/automation/ExtraDocsFRIDA/Word Reader/SelectRecipients.pdf)

---

### SetFontStyle

> Set a font style to a selection of text in the given Word document.

Sets a font style to a selection of text in the given Word document. Valid styles are "regular", "bold", "italic", "bolditalic". A position range must be specified. Warning: Formating of Tables, Headers, Footnotes, etc is currently not supported.

**Parameters:**
- `fontStyle`
- `documentKey`
- `startPosition`
- `endPosition`

**Syntax:**

```
SetFontStyle to {<fontStyle:regular|bold|italic|bolditalic>} in {<documentKey>} from range {<startPosition>} to {<endPosition>}
```

**Options:**

- `fontStyle`: `regular`, `bold`, `italic`, `bolditalic`

**Examples:**

```
SetFontStyle to {bold} in {doc1} from range {200} to {220}
```

*Added: 2023-Feb-09*

---

### WriteText

> Write a text in the given Word document.

Writes a paragraph with the given text in the given Word document. The paragraph has a new line before and after. Placeholder syntax replaces the text where the placeholder is found. Table syntax, can insert text in a table indicated by index, starting with 1. Placeholders are searched in relation to the cursor's position, so for instance, if the cursor is in page 3 and the instruction is looking to replace a placeholder in page 2, this will not be found. 
 Row and column indexes start with 1. To insert New Lines between text, use {NewLine}.

**Parameters:**
- `Text`
- `DocumentKey`
- `PlaceHolder`
- `TextboxPlaceHolder`
- `TableIndex`
- `Row`
- `Column`

**Syntax:**

```
WriteText {"<Text>"} to {"<DocumentKey>"}
WriteText {"<Text>"} to {"<DocumentKey>"} placeholder {"<PlaceHolder>"}
WriteText {"<Text>"} to {"<DocumentKey>"} textbox {"<TextboxPlaceHolder>"}
WriteText {"<Text>"} to {"<DocumentKey>"} in table <TableIndex> cell [<Row>,<Column>]
```

**Examples:**

```
WriteText {"Write this text in the document"} to {"WordDoc"}
WriteText {"NewText"} to {"WordDoc"} placeholder {"TargetText"}
WriteText {"Turing FRIDA by Softtek"} to {"WordDoc"} textbox {"FullName"}
```

*Added: 2019-Nov-25*

---
