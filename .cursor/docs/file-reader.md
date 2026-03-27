# File Reader

**Keyword:** `File`

**Functions:** 37

## Description

File Reader allows you to interact with your local files on your computer having the ability to move, copy, list, read or even create a new one directly from your script.

## Quick Reference

| Function | Description |
|----------|-------------|
| [AddToZip](#addtozip) | Add files to a zip file. |
| [ChangeCSVSeparator](#changecsvseparator) | Change the separator character in a CSV file. |
| [ChangeEncoding](#changeencoding) | Change the encoding of a txt file. |
| [CheckIfDirExist](#checkifdirexist) | Check if a directory exists in a path creating an error if it doesn't. |
| [CheckIfFileExists](#checkiffileexists) | Check if a file exists in a directory creating an error if it doesn't or retu... |
| [Compress](#compress) | Compress a folder. |
| [CopyDirectory](#copydirectory) | Copies a directory to another location. |
| [CopyFile](#copyfile) | Copy a file from one destination to another. |
| [DeleteAllFiles](#deleteallfiles) | Delete files from a folder. |
| [DeleteFile](#deletefile) | Delete a file. |
| [DeleteFolder](#deletefolder) | Delete a folder. |
| [ExtractFile](#extractfile) | Extract the files from a compressed file. |
| [FileInfo](#fileinfo) | Get file attributes. |
| [GetAllFiles](#getallfiles) | Get all file names inside a folder with a given path. The first syntax will r... |
| [GetAllFolderNames](#getallfoldernames) | Get all folders names inside a folder with a given path. |
| [GetAllImages](#getallimages) | Read all the images from a PDF file and save them in the given path. |
| [GetAllLines](#getalllines) | Read all the text from a file and save it in a variable. |
| [GetAllText](#getalltext) | Read all the text from a file and save it in a variable. |
| [GetDifferences](#getdifferences) | Read all text from two files and return the differences between them. |
| [GetDirectoryName](#getdirectoryname) | Get the directory part of a file. |
| [GetEmlText](#getemltext) | Read all the text from a .eml file and save it in a variable. |
| [GetFileFromURL](#getfilefromurl) | Download a file from a URL. |
| [GetFileName](#getfilename) | Get the name of a file. |
| [GetFileSize](#getfilesize) | Get the size of a File. |
| [GetLastFileInTheFolder](#getlastfileinthefolder) | Get the path of the last file in a folder. |
| [GetLastFolder](#getlastfolder) | Get the path of the last folder modified. |
| [MoveFile](#movefile) | Move a file from one destination to another. |
| [NewFolder](#newfolder) | Create a new folder. |
| [PDF_Merge](#pdf_merge) | Merges two PDF files into a new one. |
| [PDFToImage](#pdftoimage) | Converts a PDF to image with PNG encoding. |
| [PDFTotalPages](#pdftotalpages) | Gets the number of pages in a PDF. |
| [RegexReplace](#regexreplace) | Replace a regular expresion match for a substring in a file. |
| [RenameDirectory](#renamedirectory) | Change the name of a directory. |
| [RenameFile](#renamefile) | Change the name of a file. |
| [WriteAllLines](#writealllines) | Writes all the lines contained in a list variable to a file. |
| [WriteAllText](#writealltext) | Write all the text contained in a variable to a file. |
| [WriteAndKeep](#writeandkeep) | Write the text in a variable to a file without overwriting its content. |

---

## Functions

### AddToZip

> Add files to a zip file.

Adds a file or folder to a zip file. If any of the files added already exists, they will be duplicated, and no error will be thrown.

**Parameters:**
- `sourcePath`
- `zipPath`

**Syntax:**

```
AddToZip file "<sourcePath>" to zip file "<zipPath>"
AddToZip folder "<sourcePath>" to zip file "<zipPath>"
```

**Examples:**

```
AddToZip file "C:\Users\productivity\Desktop\Excel\newFile.txt" to zip file "C:\Users\productivity\Desktop\Excel.zip"
AddToZip folder "C:\Users\productivity\Desktop\Excel\tests" to zip file "C:\Users\productivity\Desktop\Excel.zip"
```

*Added: 2023-Aug-24*

---

### ChangeCSVSeparator

> Change the separator character in a CSV file.

Changes the separator character in a CSV file avoiding replacement in the inner text. Original and new separators must be a single character. By default encoding will be interpreted from BOM identifier. Other encoding options are available, if the file has no BOM identifier ASCII will be defaulted. Consider using ISO-8859-1 (alias latin) for latin characters or utf-8, for further reference consult https://learn.microsoft.com/es-es/dotnet/api/system.text.encoding?view=net-7.0#list-of-encodings

**Parameters:**
- `csvPath`
- `originalSeparator`
- `newSeparator`
- `encodingText`

**Syntax:**

```
ChangeCSVSeparator in the file {<csvPath>} from {<originalSeparator>} to {<newSeparator>}
ChangeCSVSeparator in the file {<csvPath>} from {<originalSeparator>} to {<newSeparator>} encoding {<encodingText>}
```

**Examples:**

```
ChangeCSVSeparator in the file {c:\Users\Softtek\file.csv} from {,} to {;}
ChangeCSVSeparator in the file {c:\Users\Softtek\file.csv} from {,} to {;} encoding {ISO-8859-1}
ChangeCSVSeparator in the file {c:\Users\Softtek\file.csv} from {,} to {;} encoding {latin}
```

*Added: 2022-Dec-05*

---

### ChangeEncoding

> Change the encoding of a txt file.

Changes the encoding of a txt file. ANSI to UTF-8 for example. Currently source can only be ansi or ebcdic and destFormat can only be ascii or utf8.

**Parameters:**
- `source`
- `destFormat`
- `filePath`

**Syntax:**

```
ChangeEncoding <source> to <destFormat> "<filePath>"
```

**Examples:**

```
ChangeEncoding ansi to utf8 "C:\Users\gilberto.isida\Downloads\file.txt"
```

*Added: 2019-Dec-17*

---

### CheckIfDirExist

> Check if a directory exists in a path creating an error if it doesn't.

Check if a directory exists in a path creating an error if it doesn't. There's an available syntax for the instruction to return a true/false string stored in a variable.

**Parameters:**
- `Path`
- `FolderName`
- `VarName`

**Syntax:**

```
CheckIfDirExist in the path "<Path>" with the name "<FolderName>"
CheckIfDirExist in the path "<Path>" with the name "<FolderName>" and save result as "<VarName>"
```

**Examples:**

```
CheckIfDirExist in the path "C:\Usersodrigo.gracia\Desktop" with the name "Images"
CheckIfDirExist in the path "C:\Usersodrigo.gracia\Desktop" with the name "Images" and save result as "Result"
```

*Added: 2020-Apr-14*

---

### CheckIfFileExists

> Check if a file exists in a directory creating an error if it doesn't or return true/false as the content of a variable.

Check if a file exists in a directory creating an error if it doesn't. By using the syntax "and save result as" you can store the result as a variable (true, false) that can be used with another logic.

**Parameters:**
- `Directory`
- `FileName`
- `VariableName`

**Syntax:**

```
CheckIfFileExists in the directory "<Directory>" with the name "<FileName>"
CheckIfFileExists in the directory "<Directory>" with the name "<FileName>" and save result as "<VariableName>"
```

**Examples:**

```
CheckIfFileExists in the directory "C:\Users\andres.cruz\Desktop" with the name "ExceliaDemoFile.xlsx"
CheckIfFileExists in the directory "C:\Users\andres.cruz\Desktop" with the name "ExceliaDemoFile.xlsx" and save result as "Success"
```

*Added: 2020-Nov-06*

---

### Compress

> Compress a folder.

This function converts a folder into a .zip file and saves de final path in a variable.

**Parameters:**
- `sourcePath`
- `zipPath`
- `varKey`

**Syntax:**

```
Compress this folder path "<sourcePath>" to this zipPath "<zipPath>" and save as <varKey>
```

**Examples:**

```
Compress this folder path "C:\Users\productivity\Desktop\Excel" to this zipPath "C:\Users\productivity\Desktop\Excel.zip" and save as zipPath
```

*Added: 2020-Nov-10*

---

### CopyDirectory

> Copies a directory to another location.

Copies a directory to another location, optionally you can decide whether to copy all files and inner directories or not. To visualize in the log which files are copied, set log level to debug. 

**Parameters:**
- `srcPath`
- `destPath`
- `recursive`
- `overwrite`

**Syntax:**

```
CopyDirectory source={<srcPath>} destination={<destPath>} recursive={<recursive:true|false>} overwrite={<overwrite:true|false>}
```

**Options:**

- `recursive`: `true`, `false`
- `overwrite`: `true`, `false`

**Examples:**

```
CopyDirectory source={C:\Users\gilberto.isida\Documents\Directorio - Prueba Función 2021} destination={D:\Backup\PruebaCopyDir} recursive={true} overwrite={false}
```

*Added: 2020-Dec-11*

---

### CopyFile

> Copy a file from one destination to another.

Copies the file in InputFolder and moves it to OutputFolder with the given name, and save it in theVariablesHelper.vars diccionary.

**Parameters:**
- `InputFolderPathPlusName`
- `OutputFolderPathPlusName`
- `Variable`

**Syntax:**

```
CopyFile "<InputFolderPathPlusName>" to "<OutputFolderPathPlusName>" and save as "<Variable>"
```

**Examples:**

```
CopyFile "C:\Users\andres.cruz\Downloads\Template.xlsx" to "C:\Users\andres.cruz\Downloads\Reporte20190214.xlsx" and save as "copiado"
```

*Added: 2019-Mar-13*

---

### DeleteAllFiles

> Delete files from a folder.

Delete all files from a specific folder in a certain path. You can delete the files of a specific extension

**Parameters:**
- `FolderPath`
- `FileExtension`

**Syntax:**

```
DeleteAllFiles from "<FolderPath>"
DeleteAllFiles from "<FolderPath>" including subfolders
DeleteAllFiles from "<FolderPath>" with the extension "<FileExtension>"
```

**Examples:**

```
DeleteAllFiles from "C:\Users\Admin\Desktop\ToDelete" including subfolders
DeleteAllFiles from "C:\Users\Admin\Desktop\ToDelete"
DeleteAllFiles from "C:\Users\Admin\Desktop\ToDelete" with the extension ".docx"
```

*Added: 2021-Jul-05*

---

### DeleteFile

> Delete a file.

Deletes a specific file in a given path. The file name needs to include the extension.

**Parameters:**
- `FileName`
- `Path`

**Syntax:**

```
DeleteFile <FileName> from "<path>"
```

**Examples:**

```
DeleteFile log.txt from "C:\Users\productivity\Desktop"
```

*Added: 2019-Jul-01*

---

### DeleteFolder

> Delete a folder.

Deletes a specific folder in a given path. It may delete recursively the content within, using the "and its content" syntax. 
Make sure there are no Windows Explorers open inside the delete path o its subdirectories.

**Parameters:**
- `Path`

**Syntax:**

```
DeleteFolder from "<path>"
DeleteFolder and its content from "<path>"
```

**Examples:**

```
DeleteFolder from "C:\Users\Admin\Desktop\ToDelete"
DeleteFolder and its content from "C:\Users\Admin\Desktop\ToDelete"
```

*Added: 2019-Dec-26*

---

### ExtractFile

> Extract the files from a compressed file.

Extract the files from a ZIP, 7Z or TAR compressed file into a specific location. The paths of the extracted files are saved as a list variable.

**Parameters:**
- `inputCompressedFile`
- `outputDirectory`
- `varName`

**Syntax:**

```
ExtractFile "<inputCompressedFile>" into "<outputDirectory>" delete the zip and save as "<varName>"
```

**Examples:**

```
ExtractFile "C:\Users\andres.cruz\Desktop\DirecCartolas.zip" into "C:\Users\andres.cruz\Desktop\Test\" delete the zip and save as "Res"
```

*Added: 2019-Dec-17*

---

### FileInfo

> Get file attributes.

Gets information about a file, given its full path. The possible attributes are CreationTime, LastAccessTime, LastWriteTime, CreationTimeUTC, LastAccessTimeUTC, LastWriteTimeUTC. This info will be saved in a new variable with the name of the selected attribute.

**Parameters:**
- `attribute`
- `path`

**Syntax:**

```
FileInfo <attribute:CreationTime|LastAccessTime|LastWriteTime|CreationTimeUTC|LastAccessTimeUTC|LastWriteTimeUTC> <path>
```

**Options:**

- `attribute`: `CreationTime`, `LastAccessTime`, `LastWriteTime`, `CreationTimeUTC`, `LastAccessTimeUTC`, `LastWriteTimeUTC`

**Examples:**

```
FileInfo LastAccessTime C:\Users\gilberto.isida\Desktop\log.txt
FileInfo CreationTime C:\Users\gilberto.isida\Downloads\RPA\archivo.xlsx
```

*Added: 2019-Dec-05*

---

### GetAllFiles

> Get all file names inside a folder with a given path. The first syntax will read files that start with that extension and read aditional variants of the extention (e,g. xls reads xls, xlsm, xlsx). "Exact" syntax will read the exact extension indicated. Search pattern may use wildcards asterisk (*) to search zero or more characters an question mark (?) to search zero or one character.

Get all file names inside a folder with a given path.

**Parameters:**
- `folderPath`
- `searchPattern`
- `fileExtension`
- `objectName`

**Syntax:**

```
GetAllFiles in "<folderPath>" with extension "<fileExtension>" and save as "<objectName>"
GetAllFiles in "<folderPath>" with exact extension "<fileExtension>" and save as "<objectName>"
GetAllFiles in "<folderPath>" search pattern "<searchPattern>" with extension "<fileExtension>" and save as "<objectName>"
GetAllFiles in "<folderPath>" search pattern "<searchPattern>" with exact extension "<fileExtension>" and save as "<objectName>"
GetAllFiles in "<folderPath>" and save as "<objectName>"
```

**Examples:**

```
GetAllFiles in "C:\Users\Documents\Extract" and save as "BankExtract"
GetAllFiles in "C:\Users\Documents\logs\" search pattern "log202?-??-01" with extension ".txt" and save as "LogsFirstDay"
GetAllFiles in "C:\Users\Documents\logs\" search pattern "*error" with extension ".txt" and save as "archErrores"
```

*Added: 2018-Dec-03*

---

### GetAllFolderNames

> Get all folders names inside a folder with a given path.

Get all folders names inside a folder with a given path.

**Parameters:**
- `folderPath`
- `listName`

**Syntax:**

```
GetAllFolderNames in "<folderPath>" and save as <listName>
```

**Examples:**

```
GetAllFolderNames in "C:\Users\andres.cruz\Documents\Extractos" and save as CarpetasMeses
```

*Added: 2018-Dec-20*

---

### GetAllImages

> Read all the images from a PDF file and save them in the given path.

Reads all the images from the pdf file and saves them them in a given path naming them with numbers.

**Parameters:**
- `filepath`
- `folderName`

**Syntax:**

```
GetAllImages from the file "<filepath>" and save them in "<folderName>"
```

**Examples:**

```
GetAllImages from the file "C:\Users\andres.cruz\Downloads\Documentacion.pdf" and save them in "C:\Users\andres.cruz\Desktop\RPAImages"
```

*Added: 2020-Dec-11*

---

### GetAllLines

> Read all the text from a file and save it in a variable.

Reads all the text from the indicated file (pdf, txt) as a list and saves it's value in the given variable. The separation character may be indicated if new line is not desired. [This function uses PDF Clown covered by LGPL Licence (library source code : http://www.pdfclown.org)]

**Parameters:**
- `filepath`
- `varname`
- `separationChar`

**Syntax:**

```
GetAllLines from "<filepath>" and save as "<varname>"
GetAllLines from the file "<filepath>" and save as "<varname>"
GetAllLines from "<filepath>" and separate its value by "<separationChar>" and save as "<varname>"
```

**Examples:**

```
GetAllLines from "C:\Users\gilberto.isida\Downloads\userIDs.txt" and save as "newUsers"
GetAllLines from "C:\Users\andres de la cruz\Desktop\Invoice.pdf" and save as "Invoice"
GetAllLines from "C:\Users\gilberto.isida\Downloads\userIDs.txt" and separate its value by ";" and save as "newUsers"
```

*Added: 2020-Apr-22*

---

### GetAllText

> Read all the text from a file and save it in a variable.

Reads all the text from the indicated file (pdf , txt) as one single string and save it's value in the given variable.

**Parameters:**
- `filepath`
- `varname`

**Syntax:**

```
GetAllText from "<filepath>" and save as "<varname>"
GetAllText from the file "<filepath>" and save as "<varname>"
```

**Examples:**

```
GetAllText from "C:\Users\gilberto.isida\Downloads\userIDs.txt" and save as "newUsers"
GetAllText from the file "C:\Users\andres.cruz\Downloads\IDs.txt" and save as "IDs"
```

*Added: 2020-Apr-21*

---

### GetDifferences

> Read all text from two files and return the differences between them.

Read all text from two files and return a text document containing the differences between them. If the output text file is empty it means the two files are the same. 
Syntaxes with field definition file must comply with the rules explained in extra docs. The separator character will be used to output a CSV-like file with the differences. Max differences parameter means the amount of field differences it will report before the comparison is stopped.
 --debug will output other intermediate files and logs to validate how the file is being broken down and compared based on the definition file provided.

**Parameters:**
- `filePath`
- `outputPath`
- `fieldDefinitionFilePath`
- `separatorCharacter`
- `maxDifferences`

**Syntax:**

```
GetDifferences between "<filePath1>" and "<filePath2>" and save as "<outputPath>"
GetDifferences between "<filePath1>" and "<filePath2>" with definition file "<fieldDefinitionFilePath>" separator "<separatorCharacter>" and save as "<outputPath>"
GetDifferences between "<filePath1>" and "<filePath2>" with definition file "<fieldDefinitionFilePath>" separator "<separatorCharacter>" and save as "<outputPath> --debug"
GetDifferences between "<filePath1>" and "<filePath2>" with definition file "<fieldDefinitionFilePath>" separator "<separatorCharacter>" stop at <maxDifferences> and save as "<outputPath>"
GetDifferences between "<filePath1>" and "<filePath2>" with definition file "<fieldDefinitionFilePath>" separator "<separatorCharacter>" stop at <maxDifferences> and save as "<outputPath> --debug"
```

**Examples:**

```
GetDifferences between "C:\Users\usr\userIDs.txt" and "C:\Users\usr\otherIDs.txt" and save as "C:\Users\usr\Downloads\diferenciaIDs.txt"
GetDifferences between "C:\Users\usr\fileA.txt" and "C:\Users\usr\fileB.txt" with definition file "C:\Users\usr\definitions.txt" separator "|" stop at 10 and save as ""C:\Users\usr\differences.txt"
```

*Added: 2023-Mar-08*

---

### GetDirectoryName

> Get the directory part of a file.

Get the directoy part in a path and save it in a variable.

**Parameters:**
- `filePath`
- `varName`

**Syntax:**

```
GetDirectoryName from the file "<filePath>" and save as "<varName>"
```

**Examples:**

```
GetDirectoryName from the file "C:\Users\user\Documents\Extractos.xlsx" and save as "ExtractosDirectory"
```

*Added: 2024-Nov-14*

---

### GetEmlText

> Read all the text from a .eml file and save it in a variable.

Reads the different sections in an .eml file (body,htmlbody,date,subject,from,cc) as one single string and saves it's value in the given variable.

**Parameters:**
- `filepath`
- `varname`
- `emlSection`

**Syntax:**

```
GetEmlText from "<filepath>" <emlSection:body|htmlbody|date|subject|from|cc> section and save as "<varname>"
```

**Options:**

- `emlSection`: `body`, `htmlbody`, `date`, `subject`, `from`, `cc`

**Examples:**

```
GetEmlText from "C:\Users\user\Downloadseplied.eml" body section and save as "body"
GetEmlText from "C:\Users\user\Downloadseplied.eml" subject section and save as "subjectText"
```

*Added: 2024-Oct-24*

---

### GetFileFromURL

> Download a file from a URL.

Downloads a file from an online URL and saves it to a given path.

**Parameters:**
- `url`
- `localPath`

**Syntax:**

```
GetFileFromURL "<url>" and save file as "<localPath>"
GetFileFromURL {<url>} and save as {<localPath>}
```

**Examples:**

```
GetFileFromURL "https://some.server.com/Dir/Dir2/file.png" and save file as "C:/Users/gilberto.isida/Downloads/file.png"
GetFileFromURL {https://some.server.com/Dir/Dir2/file.png} and save as {C:/Users/gilberto.isida/Downloads/file.png}
```

*Added: 2020-Nov-08*

---

### GetFileName

> Get the name of a file.

Get the name of a file in a path and save it in a variable.

**Parameters:**
- `filePath`
- `varName`

**Syntax:**

```
GetFileName from the file "<filePath>" and save as "<varName>"
```

**Examples:**

```
GetFileName from the file "C:\Users\User\Documents\Extractos.xlsx" and save as "ExtractosName"
```

*Added: 2018-Dec-03*

---

### GetFileSize

> Get the size of a File.

Gets the size of a specific File in Bytes and saves it in a variable.

**Parameters:**
- `FilePathPlusName`
- `varName`

**Syntax:**

```
FileSize "<FilePathPlusName>" and save as "<varName>"
GetFileSize "<FilePathPlusName>" and save as "<varName>"
```

**Examples:**

```
FileSize "C:\1012SAT\Factura.pdf" and save as "FacturaSize"
GetFileSize "C:\1012SAT\Factura.pdf" and save as "FacturaSize"
```

*Added: 2019-Aug-14*

---

### GetLastFileInTheFolder

> Get the path of the last file in a folder.

Get the path of the last file on a folder (test.txt, test (1).txt, test (2).txt ... etc) returning the full file path with the name of the file.[C:\Users\andres.cruz\Downloads\test (1).txt].
 Wildcards * and ? can be used in FileName, regex is not supported. 
The resulting list can retrieve the last file modified or the last file ordered by name.

**Parameters:**
- `folderPath`
- `fileName`
- `orderOption`
- `fileNameVar`

**Syntax:**

```
GetLastFileInTheFolder "<folderPath>" with the name "<fileName>" and save as "<fileNameVar>"
GetLastFileInTheFolder "<folderPath>" with the name "<fileName>" and save as <fileNameVar>
GetLastFileInTheFolder "<folderPath>" ordered by <orderOption:time|name> with the name "<fileName>" and save as <fileNameVar>
GetLastFileInTheFolder "<folderPath>" and save as "<fileNameVar>"
GetLastFileInTheFolder "<folderPath>" and save as <fileNameVar>
```

**Options:**

- `orderOption`: `time`, `name`

**Examples:**

```
GetLastFileInTheFolder "C:\Users\andres.cruz\Downloads\" and save as "LastFile"
GetLastFileInTheFolder "C:\Users\andres.cruz\Desktop\" and save as FileName
GetLastFileInTheFolder "C:\Users\andres.cruz\Downloads\" ordered by name with the name "Resumen_2021_05_*" and save as UltimoMayo
```

*Added: 2018-Sep-19*

---

### GetLastFolder

> Get the path of the last folder modified.

Get the path of the last folder modified and save the full path in a variable. [C:\Users\User\Downloads\Temp123].
 Wildcards * and ? can be used in FolderName, regex is not supported. The last folder may be regarding last date modified or the last folder ordered by name.

**Parameters:**
- `folderPath`
- `folderName`
- `orderOption`
- `folderNameVar`

**Syntax:**

```
GetLastFolder "<folderPath>" with the name "<folderName>" and save as "<folderNameVar>"
GetLastFolder "<folderPath>" with the name "<folderName>" and save as <folderNameVar>
GetLastFolder "<folderPath>" ordered by <orderOption:time|name> with the name "<folderName>" and save as <folderNameVar>
```

**Options:**

- `orderOption`: `time`, `name`

**Examples:**

```
GetLastFolder "C:\Users\User\AppData\Local\Temp" with the name "*" and save as LastTempFolder
GetLastFolder "C:\Users\User\Downloads\" ordered by name with the name "*" and save as LastFolder
GetLastFolder "C:\Users\User\Downloads\" ordered by time with the name "Resume_2021_05_??_18_00" and save as LastMay6Pm
```

*Added: 2024-Apr-12*

---

### MoveFile

> Move a file from one destination to another.

Moves the file from InputFolder to OutputFolder with the given name, and saves it in the dictionaryVariablesHelper.vars.

**Parameters:**
- `fileName`
- `inputFolder`
- `outputFolder`
- `variable`

**Syntax:**

```
MoveFile "<fileName>" from the folder "<inputFolder>" to the folder "<outputFolder>" and save as <variable>
```

**Examples:**

```
MoveFile "ejemplo.docx" from the folder "C:\Datos\Origen" to the folder "C:\Datos\Destino" and save as Mivariable
MoveFile "ejemplo.docx" from the folder "C:\Datos\Origen" to the folder "C:\Datos\Destino" and save as "Mivariable"
```

*Added: 2021-Jun-29*

---

### NewFolder

> Create a new folder.

Creates a new folder in a given Path, if it already exists the function will not generate an error.

**Parameters:**
- `path`
- `folderName`

**Syntax:**

```
NewFolder in "<path>" with the name "<folderName>"
```

**Examples:**

```
NewFolder in "C:\\SomeFolder" with the name "Temporal"
```

*Added: 2019-Dec-17*

---

### PDF_Merge

> Merges two PDF files into a new one.

Combine the pages of two PDF files into a new file. The new file will be at the path specified by the 'out' parameter. TargetFile is the first PDF file to be merged. FilesToMerge are the following PDF files to merge. If a file already exists at that path, it will be over-written. The order of the pages will be first file1, then file2.

**Parameters:**
- `file1`
- `file2`
- `out`
- `filesToMerge`
- `targetFile`
- `inputPDF`
- `pages`
- `fromFolder`

**Syntax:**

```
PDF_Merge file1={<pathToFile1>} file2={<pathToFile2>} out={<pathToNewFile>}
PDF_Merge multiplePDFS filesToMerge={<pdf1>, <pdf2>, <pdf3>, ... <pdfn>} to targetFile={<pathToOutputPDF>} out={<pathToNewFile>}
PDF_Merge SpecificPages from inputPDF={<pathToInputPDF>} pages={<pageIndex1>, <pageIndex2>,...<pageIndexn>} to targetFile={<pathToOutputPDF>} out={<pathToNewFile>}
PDF_Merge SpecificPages from inputPDF={<pathToInputPDF>} pages={<pageIndex1>, <pageIndex2>,...<pageIndexn>} out={<pathToNewFile>}
PDF_Merge fromFolder={<folderPath>} out={<pathToNewFile>}
```

**Examples:**

```
PDF_Merge file1={C:/Users/gilberto.isida/first.pdf} file2={C:/Users/gilberto.isida/second.pdf} out={C:/Users/gilberto.isida/result.pdf}
PDF_Merge multiplePDFS filesToMerge={C:\Users\frida\pdf1.pdf, C:\Users\frida\pdf2.pdf, C:\Users\frida\pdf3.pdf} to targetFile={C:\Users\frida\pdfOutput.pdf} out={C:\Users\frida\pdfMerged.pdf}
PDF_Merge SpecificPages from inputPDF={C:\Users\frida\pdf1.pdf} pages={1, 3, 7} to targetFile={C:\Users\frida\pdfOutput.pdf} out={C:\Users\frida\pdfMerged.pdf}
```

*Added: 2023-Jan-25*

---

### PDFToImage

> Converts a PDF to image with PNG encoding.

Extracts a page of a PDF file and rasterizes it as PNG image to the desired location. If page input is not specified, only the first one will be extracted. Page number starts at 1.
By default images are 96dpi.

**Parameters:**
- `inputFile`
- `outputFile`
- `pageNumber`
- `dpiSize`

**Syntax:**

```
PDFToImage file={<inputFile>} output={<outputFile>}
PDFToImage file={<inputFile>} output={<outputFile>} dpi={<dpiSize>}
PDFToImage file={<inputFile>} page={<pageNumber>} output={<outputFile>}
PDFToImage file={<inputFile>} page={<pageNumber>} output={<outputFile>} dpi={<dpiSize>}
```

**Examples:**

```
PDFToImage file={C:\Users\gilberto.isida\Documents\file.pdf} output={C:\Users\gilberto.isida\Pictures\converted.png}
PDFToImage file={C:\Users\gilberto.isida\Documents\file.pdf} page={3} output={C:\Users\gilberto.isida\Pictures\converted.png}
PDFToImage file={C:\Users\gilberto.isida\Documents\file.pdf} page={3} output={C:\Users\gilberto.isida\Pictures\converted.png} dpi={200}
```

*Added: 2021-Mar-30*

---

### PDFTotalPages

> Gets the number of pages in a PDF.

Gets the number of pages in a given PDF file.

**Parameters:**
- `inputFile`
- `variableName`

**Syntax:**

```
PDFTotalPages file={<inputFile>} and save as <variableName>
```

**Examples:**

```
PDFTotalPages file={C:\SomePath\file.pdf} and save as totalPages
```

*Added: 2022-Sep-27*

---

### RegexReplace

> Replace a regular expresion match for a substring in a file.

Replaces all occurrences of searchSubstring for the value in replaceSubstring and saves the result back in the file. Beware that "\" is escaped in the replaceSubtring and special characters as new line or tab can only be used with "unescaped" syntax.
Capture groups are valid and $CaptureGroupNum may be used to include the group in the replaceSubtring, for example considering search string "(.+)\.", replace string "$1_old." and string "C:\Documents\user\file.txt". Capture group (.+) is taking all characters until a "." is found. So the value after the replacemet will be "C:\Documents\user\file_old.txt".

**Parameters:**
- `searchSubstring`
- `replaceSubstring`
- `filePath`

**Syntax:**

```
RegexReplace {<searchSubstring>} for {<replaceSubstring>} in {<filePath>}
RegexReplace {<searchSubstring>} for unescaped {<replaceSubstring>} in {<filePath>}
```

**Examples:**

```
RegexReplace { } for {|} in {C:\Dir\SomeFile.txt}
RegexReplace {\n} for {} in {C:\Dir\SomeFile.txt}
RegexReplace {\x00\x3F\x00} for unescaped {\n} in {<<<convertedFile>>>}
```

*Added: 2023-Jun-06*

---

### RenameDirectory

> Change the name of a directory.

Changes the name of a directory and save the new path in a variable. If it fails it will throw an exception.

**Parameters:**
- `path`
- `directoryName`
- `newPath`

**Syntax:**

```
RenameDirectory "<path>" with "<directoryName>" and save as "<newPath>"
```

**Examples:**

```
RenameDirectory "C:\Users\user\Downloads\TestDir" with "ProdDir" and save as "prodPath"
```

*Added: 2024-Nov-14*

---

### RenameFile

> Change the name of a file.

Change the name of a file, and save the new path in a variable.

**Parameters:**
- `folderPathPlusName`
- `FileName`
- `variable`

**Syntax:**

```
RenameFile "<folderPathPlusName>" with "<fileName>" and save as "<variable>"
```

**Examples:**

```
RenameFile "C:\Users\user\Downloads\001100.xlsx" with "Reporte.xlsx" and save as "fileRenamed"
RenameFile "C:\Users\user\Downloads\test.zip" with "C:\Users\user\Desktop\TestReporte.xlsx" and save as "changed"
```

*Added: 2018-Oct-11*

---

### WriteAllLines

> Writes all the lines contained in a list variable to a file.

Writes all the lines contained in a variable (of type LIST), to a file. It creates the file if it does not exist yet.

**Parameters:**
- `variableName`
- `savePath`

**Syntax:**

```
WriteAllLines var="<variableName>" path="<savePath>"
WriteAllLines from the variable "<variableName>" in the file "<savePath>"
```

**Examples:**

```
WriteAllLines var = "username" path = "C:\Users\gilberto.isida\Downloads\file.txt"
WriteAllLines from the variable "TicketList" in the file "C:\Users\andres.cruz\Downloads\Result.txt"
```

*Added: 2020-Apr-21*

---

### WriteAllText

> Write all the text contained in a variable to a file.

Writes all the text contained in a variable to a file. It creates the file if it does not exist yet.

**Parameters:**
- `varName`
- `savePath`

**Syntax:**

```
WriteAllText from the variable "<varName>" in the file "<savePath>"
WriteAllText from the variable "<varName>" in the file "<savePath>" -isJSON
```

**Examples:**

```
WriteAllText from the variable "UserNames" in the file "C:\Users\andres.cruz\Downloads\Users.txt"
WriteAllText from the variable "IsonUserNames" in the file "C:\Users\andres.cruz\Downloads\Users.txt" -isJSON
```

*Added: 2020-Apr-21*

---

### WriteAndKeep

> Write the text in a variable to a file without overwriting its content.

Allows to write all the text contained in a variable to a file without overwriting its content.  It creates the file if it does not exist.

**Parameters:**
- `varName`
- `savePath`

**Syntax:**

```
WriteAndKeep from the variable "<varName>" in the file "<savePath>"
```

**Examples:**

```
WriteAndKeep from the variable "<varName>" in the file "<savePath>"
```

*Added: 2020-Aug-03*

---
