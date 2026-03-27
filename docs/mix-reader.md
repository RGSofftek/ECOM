# Mix Reader

**Functions:** 135

## Description

Mix-Reader is the most powerful of all the readers, its design allows you to create RPAs (Robotic Process Automations) by using the instructions available in all the other readers and even more, like form example “try catch” and “for” logic instructions as if you were using a programming language. It has its own functions to really put the readers potential to the highest point and to be able to create any type of RPAs without the limitation of the technologies involved, the amount of time you need to do a task, or the diversification of the flows as a consequence of an error, you can even declare variables in the script to store information and share it with other readers. 

## Quick Reference

| Function | Description |
|----------|-------------|
| [AddListVarToList](#addlistvartolist) | Add the values of a list variable to a list. |
| [AddValueTo2DList](#addvalueto2dlist) | Add values or a 1D list to a 2D list variable. |
| [AddValueToList](#addvaluetolist) | Add values to a list variable. |
| [AddVarToList](#addvartolist) | Add the value in a variable to a list. |
| [ApplyFilterInList](#applyfilterinlist) | Filter elements in a list |
| [ApplyRegex](#applyregex) | Apply a regex to a specific string and save the result in a variable. |
| [Attendedelements](#attendedelements) | Reports the attended elements within a script for analytics purpuses. |
| [AttendedElementsWithError](#attendedelementswitherror) | Reports the attended elements with error in a script for analytics purpuses, ... |
| [B64](#b64) | Base 64 encoding/decoding. |
| [ChangeValueTo2DList](#changevalueto2dlist) | Changes a value in an existing 2Dlist variable. |
| [ChangeValueToList](#changevaluetolist) | Changes a value in an existing list variable. |
| [CheckNull](#checknull) | Check if a variable has a null value saved |
| [ClearClipboard](#clearclipboard) | Removes the content in the clipboard.... |
| [CommitLog](#commitlog) | Save the RPA's execution log file until the current instruction. |
| [CopyDirectory](#copydirectory) | Copies a directory to another location. |
| [CountItems](#countitems) | Count the elements in a list or variable. |
| [CreateMailFrom](#createmailfrom) | Edit a body template stored in the Turing variables. |
| [DateAdd](#dateadd) | Returns a Date value containing a date and time value to which a specified ti... |
| [DateDiff](#datediff) | Get the difference between two dates. |
| [DebugVariables](#debugvariables) | Print the Turing variables to the log file. |
| [DefineVariable](#definevariable) | Create a FRIDA variable. |
| [Delete](#delete) | Delete a caracter on a string or list and saves the result in a variable. |
| [Finish](#finish) | Create an error message to stop the execution of a process. |
| [For](#for) | Loops a code fragment a specified number of times. |
| [For-ForEach](#for-foreach) | Loops a code fragment a specified number of times, or based on a list-type va... |
| [FTP_Download](#ftp_download) | Downloads a file or an entire directory to a local folder. |
| [FTP_List](#ftp_list) | Get all the file and directory names inside a directory in an FTP Server. |
| [FTP_Rename](#ftp_rename) | Rename or move a file in an FTP Server. |
| [GetAllImages](#getallimages) | Read all the images from a PDF file and save them in the given path. |
| [GetAllLines](#getalllines) | Reads all the text from a file to a list variable. |
| [GetAllText](#getalltext) | Reads all the text from a file saves it in a variable. |
| [GetCombinationsSum](#getcombinationssum) | Get all the possible combinations of items within a numeric list. |
| [GetCulture](#getculture) | Create a variable for the current CultureInfoName. |
| [GetCurrentDate](#getcurrentdate) | Read the computer's current date. |
| [GetEnviromentPath](#getenviromentpath) | Read "home" and "root" locations. |
| [GetFileFromURL](#getfilefromurl) | Download a file from a URL. |
| [GetHome](#gethome) | Read "home" location. |
| [GetHostName](#gethostname) | Get the computer name where the process is running. |
| [GetLastDayOfMonth](#getlastdayofmonth) | Returns the date of the last day of the month, adding or subtracting days, sp... |
| [GetListenerID](#getlistenerid) | Gets the Listener ID where the process is running. |
| [GetListenerQueueId](#getlistenerqueueid) | Get the process' queue Id.  |
| [GetProcessId](#getprocessid) | Get the process id of the process being executed.  |
| [GetProcessName](#getprocessname) | Get the process name of the process being executed.  |
| [GetRoot](#getroot) | Read "root" location. |
| [GetRunId](#getrunid) | Get the run id of the execution being made.  |
| [GetTableVarValue](#gettablevarvalue) | Gets the value from a 2D list or table |
| [GetTextFromClipboard](#gettextfromclipboard) | Get a string from the clipboard and save it in a variable. |
| [GetUser](#getuser) | Get the mail of the user that is executing. |
| [IF](#if) | Makes a comparison. Uses the logical operators <, >, >=, <=, ==, !=... |
| [IndexOf](#indexof) | Get the Index (zero-based) of an element in a List. |
| [IndexOf2DList](#indexof2dlist) | Find the index where a text is located in a 2Dlist. |
| [IndexOfList](#indexoflist) | Find the index where a text appears in a list. |
| [IsMatch](#ismatch) | Find if one or more regex strings are matched within a text |
| [JoinListValues](#joinlistvalues) | Join all values in a list as a single string. |
| [JSON](#json) | Build a JSON variable. |
| [ListOperation](#listoperation) | Do "Set theory" operations with lists. i.e. union, insersect, substract. |
| [LoadDataDrivenList](#loaddatadrivenlist) | Load the Data Driven Json file from the process as a list of strings objects. |
| [LoadDataDrivenObject](#loaddatadrivenobject) | Load a JSON Object into the process variable dictionary with their respective... |
| [LoadIMGToClipboard](#loadimgtoclipboard) | Load an image to the clipboard. |
| [LoadJSON](#loadjson) | Read a JSON string and load its keys as variables. |
| [LoadVarToClipboard](#loadvartoclipboard) | Load a variable to the clipboard. |
| [Lowercase](#lowercase) | Make a string lowercase and save it in a variable. |
| [MakeRandom](#makerandom) | Generate a Random number between two numbers. |
| [MathOperation](#mathoperation) | Do a math operation and save the result in a variable. |
| [Message](#message) | Displays a given mesage in the run window.... |
| [MEX_Factura_SAT](#mex_factura_sat) | MEXICO: Validate an XML file of an invoice against an IRS (Hacienda) webservice. |
| [NotificationService](#notificationservice) | Call an existing NotHub service. |
| [NotifyDelays](#notifydelays) | Configure the Notification via mail of unexpected delays in the execution.  |
| [ParseDate](#parsedate) | Change a date's format. |
| [ParseExactDate](#parseexactdate) | Change a date's format. |
| [ParseVariable](#parsevariable) | Extract the value of a list, dictionary or XML variable in the dictionary and... |
| [PasteVar](#pastevar) | Load a variable's content to the clipboard and paste it in the active window/... |
| [Ping](#ping) | Send a ping to a host by url or IP address. |
| [ReadPDFasText](#readpdfastext) | Read the whole content of a PDF file and store it as text in a variable. |
| [RegexReplace](#regexreplace) | Replace a regular expresion match for a substring in a variable or a list of ... |
| [RemoveDuplicatesInList](#removeduplicatesinlist) | Remove duplicate elements in a list variable. |
| [RemoveFromList](#removefromlist) | Remove elements from a list by index or a criteria |
| [RemoveNonAscii](#removenonascii) | Change a string to remove mainly accents and other diacritics and save it in ... |
| [ReplaceFromVariable](#replacefromvariable) | Replace text in a variable. |
| [ResetVariables](#resetvariables) | Empty the contents of the given mixed reader variables. |
| [REST](#rest) | Call an external API. |
| [ReverseString](#reversestring) | Reverse the order of the characters in a string. |
| [RoundAllNumbersTo](#roundallnumbersto) | Round all the numbers that have decimal value and are going to be saved in th... |
| [RunAsync](#runasync) | Run an external program (CustomLocal), but asynchronously. |
| [RunBatch](#runbatch) | Run a Batch script. |
| [RunBatchAsync](#runbatchasync) | Run a Batch script in asynchronous mode. |
| [RunCustomLocal](#runcustomlocal) | Run an external program (CustomLocal). |
| [RunFRIDAProcess](#runfridaprocess) | Run a FRIDA Process. |
| [RunPowerShell](#runpowershell) | Run a PowerShell script. |
| [RunScript](#runscript) | Run a FRIDA Script. |
| [SaveClipboardImage](#saveclipboardimage) | Save an image from the clipboard. |
| [SaveExactValues](#saveexactvalues) | Set state to save variables with unchanged texts. |
| [SendEmailAttach2](#sendemailattach2) | Send an email with multiple attachments. |
| [SendEmailAttachEmbebed](#sendemailattachembebed) | Send an email with multiple attachments embeded in mail's body. |
| [SendEmailAttachments](#sendemailattachments) | Send an email with multiple attachments. |
| [SendEmailSelectSender](#sendemailselectsender) | Send an email with multiple attachments from a given account. |
| [SendFile](#sendfile) | If the file exists in the path it will be uploaded to Azure at the end of the... |
| [SendMail](#sendmail) | Send an email to a list of email addresses. |
| [SendNotification](#sendnotification) | Sends a Mail using the given notification template. |
| [SendSMTP](#sendsmtp) | Send an email through the SMTP protocol. |
| [SendTeamsMessage](#sendteamsmessage) | Sends a message to a teams channel via webhook |
| [SendVariable](#sendvariable) | Upload a variable to the FRIDA database at the end of the execution without g... |
| [SetCulture](#setculture) | [BETA] Change the current thread's Culture, for interpreting dates and numbers. |
| [SetLogLevel](#setloglevel) | Change level of detail in log. |
| [SetRunTimeout](#setruntimeout) | Limit the time an automation will be allowed to run. |
| [SetVarMode](#setvarmode) | [BETA] Enable or disable the CultureProvider when saving variables. |
| [SFTP Change Permissions](#sftp change permissions) | Change the permissions of a file in an FTP directory. |
| [SFTP Create Directory](#sftp create directory) | Create a directory in an FTP server, if multiple levels are needed the instru... |
| [SFTP Download](#sftp download) | Download a file from an FTP server. |
| [SFTP List](#sftp list) | List all the directories and files from an FTP Location. |
| [SFTP Upload](#sftp upload) | Upload a file to a remote FTP server. |
| [SHA1](#sha1) | Hashes a string. |
| [ShowLogInfo](#showloginfo) | Turn verbose printing of aditional information of some instructions in the log. |
| [SOAP](#soap) | Call an external SOAP WebService. |
| [SplitIntoList](#splitintolist) | Split a text into a list considering a separation character. |
| [SSH](#ssh) | Send a command or script by SSH to a host machine. If result variables are ne... |
| [StringCase](#stringcase) | Change a string casing and save it in a variable. |
| [StringToList](#stringtolist) | Parses a string variable and saves it as a List. |
| [Substring](#substring) | Extract part of the content of a string. |
| [SWITCH](#switch) | Control statement that executes a set of logic reader instructions based on t... |
| [SystemNotify](#systemnotify) | Generate a Windows pop-up notification. |
| [TemplateFrom](#templatefrom) | Read preferably an html mail body template and save it as a variable.  |
| [Transpose2DList](#transpose2dlist) | Transpose a 2Dlist. |
| [Trim](#trim) | Remove the leading and trailing blank spaces of a string variable. |
| [TrimChar](#trimchar) | Remove a character from a string variable. |
| [TrimLast](#trimlast) | Delete the last n characters from a string and save it as a given variable. |
| [TrimList](#trimlist) | Remove the leading and trailing blank spaces of every string item of a list. |
| [TRY-CATCH](#try-catch) | Control statement that allows error and exception handling.... |
| [UpdateTemplate](#updatetemplate) | Update de CustomLocal template in the cloud. |
| [Uppercase](#uppercase) | Make a string uppercase and save it in a variable. |
| [UseVBAlpha](#usevbalpha) | Run a VBS Script.  |
| [WHILE](#while) | Loops a code fragment for an undefined amount of times allowing to be execute... |
| [WriteAllLines](#writealllines) | Writes all the lines in a list variable to a file. |
| [WriteAllText](#writealltext) | Writes all the text from a variable to a file. |
| [XMLQuery](#xmlquery) | Extract the value of a XML variable in the dictionary and saves it in another... |

---

## Functions

### AddListVarToList

> Add the values of a list variable to a list.

Adds the values of a list variable to an existing list variable, if the list does not exist, it will be created.

**Parameters:**
- `joinListName`
- `secondListName`

**Syntax:**

```
AddListVarToList "<joinListName>" values "<secondListName>"
```

**Examples:**

```
AddListVarToList "users" values "joinedUsers"
```

*Added: 2023-Feb-10*

---

### AddValueTo2DList

> Add values or a 1D list to a 2D list variable.

Adds a set of values or a 1D list to a 2D list defined in the variables, if the 2D list does not exist, it will be created.

**Parameters:**
- `2DListName`
- `Item`
- `1DListName`

**Syntax:**

```
AddValueTo2DList "<2DListName>" value {"<Item1>", "<Item2>", ... , "<ItemN>"}
AddValueTo2DList "<2DListName>" value {<1DListName>}
```

**Examples:**

```
AddValueTo2DList "EmployeesList" value {"John Doe", "California", "4566", "Active"}
AddValueTo2DList "EmployeesList" value {AnEmployeeList}
```

*Added: 2021-Aug-04*

---

### AddValueToList

> Add values to a list variable.

Adds values or the values of another list to a list of strings defined in the variables, if the list does not exist, it will be created. If you want to write quotation marks (") use \".

**Parameters:**
- `listName`
- `newValue`
- `item`
- `otherListName`

**Syntax:**

```
AddValueToList "<listName>" value "<newValue>"
AddValueToList "<listName>" value {"<item1>", "<item2>", ... , "<itemN>"}
AddValueToList "<listName>" value {<otherListName>}
```

**Examples:**

```
AddValueToList "SofttekUsers" value "erlik.corona"
AddValueToList "SofttekUsers" value {"alan.gonzalez", "andres.cruz", "gilberto.isida"}
AddValueToList "AllUsers" value {SofttekUsers}
```

*Added: 2020-Mar-17*

---

### AddVarToList

> Add the value in a variable to a list.

Adds the value inside a variable (as a string) to an existing list variable, if the list does not exist, it will be created.

**Parameters:**
- `listName`
- `variableName`

**Syntax:**

```
AddVarToList "<listName>" value "<variableName>"
```

**Examples:**

```
AddVarToList "users" value "var1"
```

*Added: 2020-Mar-17*

---

### ApplyFilterInList

> Filter elements in a list

Filter elements in a list. 
FilterType "all" looks for the matches in the criteria. 
FilterType "except" looks for matches that don't meet the criteria. 
MatchContents "exact" will look for exact values. 
 MatchContents "contains" will look for the word as a regex. If no special regex is used, it will behave as "contains".  
Criteria can be comma separated for multiple values. Whenever a comma is part of the search word, it can be escaped as follows \,

**Parameters:**
- `listName`
- `filterType`
- `matchContents`
- `criteria`
- `newListName`

**Syntax:**

```
ApplyFilterInList {<listName>} find {<filterType:all|except>} match contents {<matchContents:exact|contains>} with values [<criteria>] and save as {<newListName>}
```

**Options:**

- `filterType`: `all`, `except`
- `matchContents`: `exact`, `contains`

**Examples:**

```
ApplyFilterInList {charactersList} find {all} match contents {exact} with values [Leo,Mike,Rafael,Donatello] and save as {turtlesList}
ApplyFilterInList {ticketsList} find {all} match contents {contains} with values [^Error.*,.+falla] and save as {errorsFoundList}
ApplyFilterInList {namesList} find {except} match contents {exact} with values [Mike] and save as {notMikeList}
```

*Added: 2022-Apr-22*

---

### ApplyRegex

> Apply a regex to a specific string and save the result in a variable.

Apply a regex to a specific string and save the result in the variable declared at the end of the instruction, if the variable hasn't been declared yet it will be created. 
If no matches are found an error will be raised. 
The "save as a list" option, will store all matches of the regex in a list. Save with the exact value keeps numbers with thousands separator and other formats that otherwise are removed.

**Parameters:**
- `Regex`
- `String`
- `List`
- `VarName`

**Syntax:**

```
ApplyRegex "<Regex>" to the string "<String>" and save as "<VarName>"
ApplyRegex "<Regex>" to the string "<String>" and save with the exact value as "<VarName>"
ApplyRegex "<Regex>" to the string "<String>" and save as a list "<VarName>"
ApplyRegex "<Regex>" to the List "<List>" and save as "<VarName>"
ApplyRegex "<Regex>" to the List "<List>" and save with the exact value as "<VarName>"
ApplyRegex "<Regex>" to the List "<List>" and save as a List "<VarName>"
```

**Examples:**

```
ApplyRegex "(?<=ClickImage )(.*)(?=Timeout)" to the string "ClickImage Casilla.PNG Timeout= 20000 NumberClicks= 1 Sim= 0.95" and save as "clickimage1"
ApplyRegex "(?<=Ticket#)(.*)(?= — Baja de inventario)" to the List "RegexString1" and save as "ticket1"
ApplyRegex "(?<=Ticket#)(.*)(?= — Baja de inventario)" to the List "TicketsList" and save as a List "ResultList"
```

*Added: 2018-May-21*

---

### Attendedelements

> Reports the attended elements within a script for analytics purpuses.

Reports the attended elements within a script for analytics purpuses. This will help to report the number of cicles performed in a script or other bussiness related actions that have taken place in the excecution of the script.

**Parameters:**
- `JSONList`
- `StringToDisplay`
- `UserMail`
- `ColumnLabel`
- `ColumnValue`

**Syntax:**

```
Attendedelements "<JSONList>"
Attendedelements "<StringToDisplay>"
Attendedelements "null"
Attendedelements "<JSONList>" by "<UserMail>"
Attendedelements "<StringToDisplay>" by "<UserMail>"
Attendedelements "null" by "<UserMail>"
Attendedelements "<JSONList>" with the column "<ColumnLabel>" and its value "<ColumnValue>"
Attendedelements "<StringToDisplay>" with the column "<ColumnLabel>" and its value "<ColumnValue>"
Attendedelements "null" with the column "<ColumnLabel>" and its value "<ColumnValue>"
Attendedelements "<JSONList>" by "<UserMail>" with the column "<ColumnLabel>" and its value "<ColumnValue>"
Attendedelements "<StringToDisplay>" by "<UserMail>" with the column "<ColumnLabel>" and its value value "<ColumnValue>"
Attendedelements "null" by "<UserMail>" with the column  "<ColumnLabel>" and its value "<ColumnValue>"
```

**Examples:**

```
Attendedelements "["Item 1 served","Item 2 served","Item 3 served"]" by "innovation@softtek.com"
Attendedelements "The element 123456789 was attended"
Attendedelements "null"
```

*Added: 2020-May-08*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/Attendedelements.pdf)

---

### AttendedElementsWithError

> Reports the attended elements with error in a script for analytics purpuses, this elements are going to be taken into account for error saving metrics.

Reports the attended elements with error in a script for analytics purpuses, these items will be taken into account for the error saving metrics. This will help to report the number of cicles performed in a script with error separately from the success elements or other bussiness related actions that have taken place in the excecution of the script.

**Parameters:**
- `JSONList`
- `StringToDisplay`

**Syntax:**

```
AttendedElementsWithError "<JSONList>"
AttendedElementsWithError "<StringToDisplay>"
```

**Examples:**

```
AttendedElementsWithError "["Item 1 served","Item 2 served","Item 3 served"]"
AttendedElementsWithError "The element 123456789 was attended"
```

*Added: 2021-Sep-13*

---

### B64

> Base 64 encoding/decoding.

Encodes or decodes a string to Base 64. The byte information is read as UTF8 encoded unless other is specified (UTF7, UTF32, ASCII, Unicode, BigEndianUnicode). The SaveImage syntax takes a variable whose value is a Base 64 image string and saves the converted image to the given path. The supported image formats are BMP, EMF, GIF, ICON, JPEG, PNG, TIFF, WMF. The EncodeImage syntax converts a local image to a B64 string.

**Parameters:**
- `action`
- `VariableName`
- `OutputFilePath`

**Syntax:**

```
B64 <action:encode|decode> inputVar={<VariableName>} output={<VariableName>}
B64 SaveImage inputVar={<VariableName>} output={<OutputFilePath>}
B64 EncodeImage inputVar={<VariableName>} output={<VariableName>}
```

**Options:**

- `action`: `encode`, `decode`

**Examples:**

```
B64 encode inputVar={fuente} output={b64Str}
B64 decode inputVar={facturaQR} output={facturaData}
B64 encode inputVar={fuente} output={b64Str} encoding={Unicode}
```

*Added: 2021-May-10*

---

### ChangeValueTo2DList

> Changes a value in an existing 2Dlist variable.

Changes a value in an existing 2Dlist defined in the variables, index are 0-based.

**Parameters:**
- `listName`
- `columnIndex`
- `rowIndex`
- `newValue`

**Syntax:**

```
ChangeValueTo2DList "<listName>" index [<rowIndex>,<columnIndex>] value "<newValue>"
```

**Examples:**

```
ChangeValueToList "SofttekUsers" index [3,0] value "some.person"
```

*Added: 2023-Aug-24*

---

### ChangeValueToList

> Changes a value in an existing list variable.

Changes a value in an existing list of strings defined in the variables, index is 0-based.

**Parameters:**
- `listName`
- `indexNumber`
- `newValue`

**Syntax:**

```
ChangeValueToList "<listName>" index <indexNumber> value "<newValue>"
```

**Examples:**

```
ChangeValueToList "SofttekUsers" index 3 value "some.person"
```

*Added: 2023-Aug-24*

---

### CheckNull

> Check if a variable has a null value saved

Check if a FRIDA variable (runtime created or from the process variables) has a null value. The result is stored as a true/false value in a new runtime variable with the given name.

**Parameters:**
- `VariableName`
- `ResultVariableName`

**Syntax:**

```
CheckNull "<VariableName>" and save as "<ResultVariableName>"
```

**Examples:**

```
CheckNull "Username" and save as "IsUsernameNull"
CheckNull "APIResponse" and save as "IsResponseNull"
```

*Added: 2022-May-17*

---

### ClearClipboard

Removes the content in the clipboard.

**Syntax:**

```
ClearClipboard
```

**Examples:**

```
ClearClipboard
```

---

### CommitLog

> Save the RPA's execution log file until the current instruction.

Saves the RPA's execution log until the current instruction. Log is handled in memory and the txt file is written at the end of the execution, so if you need this file before the end of the execution, you must "CommitLog".

**Parameters:**
- `none`

**Syntax:**

```
CommitLog
```

**Examples:**

```
CommitLog
```

*Added: 2019-Nov-25*

---

### CopyDirectory

> Copies a directory to another location.

Copies a directory to another location, optionally you can decide whether to copy all files and inner directories or not.

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

### CountItems

> Count the elements in a list or variable.

Counts the elements inside a list or dictionary variable. Angle brackets (<>) are not required. If it's a 2D list, it will return the count of the first dimension, for example in a list with last index [4.3], it will return 5 (meaning 4 + 1), considering that lists begin with 0. 
For strings it counts the number of chars. If variable is null it will return an error.

**Parameters:**
- `varName`
- `varName2`

**Syntax:**

```
CountItems in <varName> and save_as <varName2>
```

**Examples:**

```
CountItems in list and save_as users
CountItems in string and save_as numChars
CountItems in rows and save_as filas
```

*Added: 2019-Jun-19*

---

### CreateMailFrom

> Edit a body template stored in the Turing variables.

Edits a body template stored in the Turing variables, replacing Variables present within the template with predefined Turing variables. The result is saved in DestVar.

**Parameters:**
- `varTemplate`
- `var1`
- `var2`
- `varN`
- `destVar`

**Syntax:**

```
CreateMailFrom <varTemplate> Variables "<var1>,<var2>...<varN>" As <destVar>
```

**Examples:**

```
CreateMailFrom plantilla Variables "NomPersona" As plantillaPersonal
```

*Added: 2018-Jun-27*

---

### DateAdd

> Returns a Date value containing a date and time value to which a specified time interval has been added.

Use this if you need to project a date or time in the future or in the past. You can project the result into years, months, weeks, days, hours, minutes, seconds, and milliseconds. If you know the input date string format, it would be better to write it in the line of code. If you want a specific output format, you must type it. In both formats you can enter the desired language

**Parameters:**
- `timeUnit`
- `interval`
- `date`
- `inputformat`
- `outputformat`
- `varName`
- `language`

**Syntax:**

```
DateAdd {<timeUnit>} {<interval:years|months|weeks|days|hours|minutes|seconds|milliseconds>} {<date>} input format={<inputformat>} and save as {<varName>}
DateAdd {<timeUnit>} {<interval>} {<date>} input format={<inputformat>} and save as {<varName>}
DateAdd {<timeUnit>} {<interval>} {<date>} input format={<inputformat>} output format={<outputformat>} and save as {<varName>}
DateAdd {<timeUnit>} {<interval>} {<date>} input format={<inputformat> <language>} output format={<outputformat> <language>} and save as {<varName>}
```

**Options:**

- `interval`: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`

**Examples:**

```
DateAdd {2} {years} {18-08-2021} input format={dd-MM-yyyy es} output format={dd-MMMM-yyyy es} and save as {EndDay}
DateAdd {-2} {years} {18-08-2021} input format={dd-MM-yyyy} output format={dd-MMMM-yyyy en} and save as {EndDay}
DateAdd {10} {days} {21-Aug-2021} input format={dd-MMM-yyyy} output format={dd-MMM-yyyy} and save as {Days}
```

*Added: 2021-Aug-19*

---

### DateDiff

> Get the difference between two dates.

Use this if you need to compare two date strings and get the time difference between both. You can get the result in years, months, weeks, days, hours, minutes, seconds, and milliseconds. If you know the input date string format, it would be better to enter it in your line of code. The time difference will be returned if date1 > date2. Just for clarification, years = 365 days, months = 30 days, weeks = 7 days. [UPDATE] use the "absolute" keyword to avoid negative numbers.

**Parameters:**
- `timeUnit`
- `date1`
- `date2`
- `dateFormat`
- `varName`

**Syntax:**

```
DateDiff {<timeUnit:years|months|weeks|days|hours|minutes|seconds|milliseconds>} {<date1>} vs {<date2>} and save as {<varName>}
DateDiff {<timeUnit:years|months|weeks|days|hours|minutes|seconds|milliseconds>} {<date1>} vs {<date2>} format={<dateFormat>} and save as {<varName>}
DateDiff absolute {<timeUnit:years|months|weeks|days|hours|minutes|seconds|milliseconds>} {<date1>} vs {<date2>} format={<dateFormat>} and save as {<varName>}
```

**Options:**

- `timeUnit`: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`
- `timeUnit`: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`
- `timeUnit`: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`

**Examples:**

```
DateDiff {hours} {20/09/2020} vs {28/09/2020} and save as {time}
DateDiff {years} {27-Oct-2020} vs {21-Nov-1991} format={dd-MMM-yyyy} and save as {age}
DateDiff absolute {years} {21-Nov-1991} vs {27-Oct-2020} format={dd-MMM-yyyy} and save as {age}
```

*Added: 2020-Oct-27*

---

### DebugVariables

> Print the Turing variables to the log file.

Print the Turing variables to the log file.

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

### DefineVariable

> Create a FRIDA variable.

Create a variable in the runtime FRIDA variables dictionary that can be used in other instructions. VariableType "date" converts OLE Automation Dates. Use "with the exact value" syntax to save a numeric value with its separators. VariableType "password" creates a password variable that can only be used with two <<>>.

**Parameters:**
- `variableType`
- `variableName`
- `value`

**Syntax:**

```
DefineVariable as "<variableName>"
DefineVariable as "<variableName>" with the value "<value>"
DefineVariable as "<variableName>" with the exact value "<value>"
DefineVariable type "<variableType:string|date|password|List>" as "<variableName>"
DefineVariable type "<variableType:string|date|password|List>" as "<variableName>" with the value "<value>"
DefineVariable type {<variableType:string|date|password|List>} as {<variableName>} with the exact value {<value>}
```

**Options:**

- `variableType`: `string`, `date`, `password`, `List`
- `variableType`: `string`, `date`, `password`, `List`
- `variableType`: `string`, `date`, `password`, `List`

**Examples:**

```
DefineVariable as "UserName"
DefineVariable as "UserEmail" with the value "innovation@softtek.com"
DefineVariable as "ExpectedResult" with the exact value "   100,300.68 "
```

*Added: 2018-Feb-06*

---

### Delete

> Delete a caracter on a string or list and saves the result in a variable.

Delete a specific caracter on a string or list and saves the result in a variable. Lists must be saved previously on theVariablesHelper.vars dictionary. For spaces, Character must say <blank>.

**Parameters:**
- `Character`
- `Text`
- `varName`

**Syntax:**

```
Delete character "<Character>" in the string "<Text>" and save as "<varName>"
Delete character "<Character>" in the list "<Text>" and save as "<varName>"
```

**Examples:**

```
Delete character "/" in the string "Ruta/" and save as "cadena"
Delete character ";" in the list "listaNombres" and save as "listaModificada"
Delete character "<blank>" in the string "hola mundo" and save as "cadSinEspacios"
```

*Added: 2019-Apr-23*

---

### Finish

> Create an error message to stop the execution of a process.

Creates an error message, this message can be used to stop the execution of a process and to disply an especific message in run window.

**Parameters:**
- `ErrorMessage`

**Syntax:**

```
Finish
Finish "<ErrorMessage>"
```

**Examples:**

```
Finish
Finish "Element not found"
```

*Added: 2020-Feb-23*

---

### For

> Loops a code fragment a specified number of times.

Loops a code fragment a specified number of times.

**Parameters:**
- `numberOfTimes`

**Syntax:**

```
for <numberOfTimes> times {
##code goes here
}
```

**Examples:**

```
for 10 times {
for <<NumberOfTimes>> times {
for <<<NumberOfTimes>>> times {
```

---

### For-ForEach

> Loops a code fragment a specified number of times, or based on a list-type variable.

Loops a code fragment a specified number of times, or based on a list-type variable. When iterating a Dictionary<key, value> the iterator name must be "key" or "value" in order to get its respective value.

**Parameters:**
- `iteratorName`
- `listName`
- `stringVariableName`

**Syntax:**

```
foreach <iteratorName> in <listName> {
##code goes here
}
foreach <iteratorName> in <stringVariableName> {
##code goes here
}
```

**Examples:**

```
foreach item in ItemList {
foreach Invoice in Invoices {
foreach char in Date {
```

*Added: 2018-Mar-23*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/For-ForEach.pdf)

---

### FTP_Download

> Downloads a file or an entire directory to a local folder.

Downloads a file or an entire directory to a local folder. The syntax supports anonymous and basic authentication. Use 'strict' to interrupt the execution if there's an error downloading any file. 'url' and 'out' parameters must be directory paths, the files will be saved to the local directory with the original name.

**Parameters:**
- `host`
- `user`
- `pass`
- `filename`
- `destinationFolder`
- `isStrict`
- `version`

**Syntax:**

```
FTP_Download strict={<isStrict:true|false>} url={<host>} out={<destinationFolder>}
FTP_Download strict={<isStrict:true|false>} url={<host>} ssl={<version:Tls|Tls11|Tls12>} out={<destinationFolder>}
FTP_Download strict={<isStrict:true|false>} url={<host>} credentials={<user>,<pass>} out={<destinationFolder>}
FTP_Download strict={<isStrict:true|false>} url={<host>} credentials={<user>,<pass>} ssl={<version:Tls|Tls11|Tls12>} out={<destinationFolder>}
FTP_Download strict={<isStrict:true|false>} url={<host>} file={<filename>} credentials={<user>,<pass>} out={<destinationFolder>}
FTP_Download strict={<isStrict:true|false>} url={<host>} file={<filename>} credentials={<user>,<pass>} ssl={<version:Tls|Tls11|Tls12>} out={<destinationFolder>}
```

**Options:**

- `isStrict`: `true`, `false`
- `isStrict`: `true`, `false`
- `version`: `Tls`, `Tls11`, `Tls12`
- `isStrict`: `true`, `false`
- `isStrict`: `true`, `false`
- `version`: `Tls`, `Tls11`, `Tls12`
- `isStrict`: `true`, `false`
- `isStrict`: `true`, `false`
- `version`: `Tls`, `Tls11`, `Tls12`

**Examples:**

```
FTP_Download strict={false} url={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/someDir} out={C:/Users/gilberto.isida/Documents/FTPTests}
FTP_Download strict={false} url={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/someDir} credentials={frida,innovation} out={C:/Users/gilberto.isida/Documents/FTPTests}
FTP_Download strict={true} url={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/Content/Resources/Examples} file={helloworld.txt} credentials={frida,innovation} out={C:/Users/gilberto.isida/Documents/FTPTests}
```

*Added: 2021-Jun-01*

---

### FTP_List

> Get all the file and directory names inside a directory in an FTP Server.

Get all the files and directory names inside a directory in an FTP Server. The syntax supports anonymous and basic authentication. The result will be saved as an iterable list. The 'details' parameter will make the output as if given by CMD.

**Parameters:**
- `host`
- `user`
- `pass`
- `varName`
- `type`
- `version`

**Syntax:**

```
FTP_List type={<type:files|directories|all>} url={<host>} out={<varName>}
FTP_List type={<type:files|directories|all>} url={<host>} ssl={<version:Tls|Tls11|Tls12>} out={<varName>}
FTP_List type={<type:files|directories|all>} url={<host>} credentials={<user>,<pass>} out={<varName>}
FTP_List type={<type:files|directories|all>} url={<host>} credentials={<user>,<pass>} ssl={<version:Tls|Tls11|Tls12>} out={<varName>}
```

**Options:**

- `type`: `files`, `directories`, `all`
- `type`: `files`, `directories`, `all`
- `version`: `Tls`, `Tls11`, `Tls12`
- `type`: `files`, `directories`, `all`
- `type`: `files`, `directories`, `all`
- `version`: `Tls`, `Tls11`, `Tls12`

**Examples:**

```
FTP_List type={files} url={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest} credentials={frida,innovation} out={lista}
FTP_List type={all} url={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/FTPExample} credentials={frida,innovation} out={lista}
FTP_List type={all} url={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/FTPExample} credentials={frida,innovation} ssl={Tls12} out={lista}
```

*Added: 2021-Jun-01*

---

### FTP_Rename

> Rename or move a file in an FTP Server.

Rename or move a file in an FTP Server. The syntax supports anonymous and basic authentication. Use 'overwrite' if you want to discard any previously existing data in the destination path.

**Parameters:**
- `source`
- `destination`
- `user`
- `pass`
- `isOverwrite`

**Syntax:**

```
FTP_Rename overwrite={<isOverwrite:true|false>} source={<sourcePath>} destination={<destinationPath>}
FTP_Rename overwrite={<isOverwrite:true|false>} source={<sourcePath>} destination={<destinationPath>} credentials={<user>,<pass>}
```

**Options:**

- `isOverwrite`: `true`, `false`
- `isOverwrite`: `true`, `false`

**Examples:**

```
FTP_Rename overwrite={false} source={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/frida.png} destination={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/Move/fridamoved.png}
FTP_Rename overwrite={false} source={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/frida.png} destination={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/frida_renamed.png}
FTP_Rename overwrite={true} source={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/frida.png} destination={ftp://waws-prod-bay-041.ftp.azurewebsites.windows.net/site/wwwroot/TonyTest/Move/fridamoved.png} credentials={frida,innovation}
```

*Added: 2021-Jun-01*

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

> Reads all the text from a file to a list variable.

Reads all the text from the indicated file (pdf, txt) as a list and saves it value in the given variable. The separation character may be indicated if new line is not desired. [This function uses PDF Clown covered by LGPL Licence (library source code : http://www.pdfclown.org)]

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

> Reads all the text from a file saves it in a variable.

Reads all the text from the indicated file (pdf , txt) as one single string and save it's value in the given variable. [This function uses PDF Clown covered by LGPL Licence (library source code : http://www.pdfclown.org)]

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

### GetCombinationsSum

> Get all the possible combinations of items within a numeric list.

Get all the possible combinations of items within a list (numeric), which sum is equal to a known number (N). The return type is a List of Lists(values). If the flag "-indices" exists, then instead of returning the values that sum (N), the return List of Lists(indices). If we expect a sum=7, and the list is [1,2,...6], the result would be [[1,6], [2,5], [3,4]]. Returns an error if the input variable is not a list, if the ist is not numeric, if the list is empty, and if there are no combinations.

**Parameters:**
- `list`
- `expectedSum`
- `varName`

**Syntax:**

```
GetCombinationsSum from <list> sum <expectedSum> and save as <varName>
GetCombinationsSum from <list> sum <expectedSum> and save as <varName> -indices
```

**Examples:**

```
GetCombinationsSum from digits sum 10 and save as theseSum7 -indices
GetCombinationsSum from digits sum 10 and save as theseSum7
```

*Added: 2019-Apr-26*

---

### GetCulture

> Create a variable for the current CultureInfoName.

Retrieves and saves the current Culture provider Name in a default (fixed) variable "CultureInfoName".

**Parameters:**
- `none`

**Syntax:**

```
GetCulture
```

**Examples:**

```
GetCulture
```

*Added: 2020-Nov-04*

---

### GetCurrentDate

> Read the computer's current date.

Read the current date of the computer that is running the process, To add a day, month or year just put a parenthesis with the number that you want to add. The format of the date and the language can be specified. 
For formats that have, hour, minutes and/or seconds, use "dd/MM/yyyy HH:mm:ss" with quotation marks.

**Parameters:**
- `format`
- `language`
- `date`

**Syntax:**

```
GetCurrentDate format={<format:Month|Day|Year|hour|minutes|seconds|hour&minutes|hour&minutes&seconds>} and save as <date>
GetCurrentDate format={<format>} and save as <date>
GetCurrentDate format={<format> <language>} and save as <date>
```

**Options:**

- `format`: `Month`, `Day`, `Year`, `hour`, `minutes`, `seconds`, `hour&minutes`, `hour&minutes&seconds`

**Examples:**

```
GetCurrentDate format={Month} and save as Month
GetCurrentDate format={Day} and save as Day
GetCurrentDate format={Year} and save as CurrentYear --- CurrentYear = 2019
```

*Added: 2018-Jun-11*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/GetCurrentDate.pdf)

---

### GetEnviromentPath

> Read "home" and "root" locations.

With the syntax "GetEnviromentPath" and "GetPath" you will get three new variables, named "home", "root" and "resources", being home the root folder of your user account on windows and root the folder where Turing is located. Also You can use "GetHome" , "GetRoot" and "GetResources" to only get one of them, with the option of changing  the default name that is being assigned to it. 

**Parameters:**
- `varName`

**Syntax:**

```
GetEnvironmentPath
GetPath
GetHome
GetRoot
GetResources
GetHome as "<varName>"
GetRoot as "<varName>"
GetResources as "<varName>"
```

**Examples:**

```
GetEnvironmentPath
GetPath
GetHome
```

*Added: 2019-Feb-21*

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

### GetHome

> Read "home" location.

Read the folder where Turing is located and store it in a variable.

**Parameters:**
- `varName`

**Syntax:**

```
GetHome as "<varName>"
GetHome
```

**Examples:**

```
GetHome as "HomePath"
```

*Added: 2018-Nov-27*

---

### GetHostName

> Get the computer name where the process is running.

Get the computer name where the process is running. With the syntax "GetHostName" will create a variable with the name "hostname".

**Parameters:**
- `VarName`

**Syntax:**

```
GetHostName
GetHostName as "<VarName>"
```

**Examples:**

```
GetHostName
GetHostName as "ComputerName"
```

*Added: 2021-Jan-04*

---

### GetLastDayOfMonth

> Returns the date of the last day of the month, adding or subtracting days, specifying the input and output format.

Use this if you need to get the last day of the current month or the last day of the month of the specified date and project a date into the future or past. You must enter the format of the date entered. If you want a specific output format, you must type it.

**Parameters:**
- `date`
- `timeUnit`
- `inputformat`
- `outputformat`
- `language`
- `varName`

**Syntax:**

```
GetLastDayOfMonth offset {<timeUnit>|<-timeUnit>} and save as {<varName>}
GetLastDayOfMonth base {<date>} offset {<timeUnit>|<-timeUnit>} input format={<dateFormat>} and save as {<varName>}
GetLastDayOfMonth base {<date>} offset {<timeUnit>|<-timeUnit>} input format={<dateFormat> <language>} output format={<dateFormat> <language>} and save as {<varName>}
```

**Examples:**

```
GetLastDayOfMonth offset {-1} output format={dd/MMMM/yyyy es} and save as {fecha}
GetLastDayOfMonth base {07-18-2021} offset {-2} input format={MM-dd-yyyy} and save as {fecha}
GetLastDayOfMonth base {01-04-2021} offset {-2} input format={dd-MM-yyyy} output format={dd-MMMM-yyyy es} and save as {fecha}
```

*Added: 2021-Aug-19*

---

### GetListenerID

> Gets the Listener ID where the process is running.

Gets the Listener ID (Turing Watcher) where the process is running. By default the ID is stored in a variable named "ActiveListenerID" unless a different name is specified.
If used without a listener, an error is generated.

**Parameters:**
- `VarName`

**Syntax:**

```
GetListenerID
GetListenerID as "<VarName>"
```

**Examples:**

```
GetListenerID
GetListenerID as "ComputerName"
```

*Added: 2021-Aug-20*

---

### GetListenerQueueId

> Get the process' queue Id. 

Get the process queue id returned by the API RunProcess. 

**Parameters:**
- `VarName`

**Syntax:**

```
GetListenerQueueId as "<VarName>"
```

**Examples:**

```
GetListenerQueueId as "IdPOST"
```

*Added: 2020-Nov-23*

---

### GetProcessId

> Get the process id of the process being executed. 

Get the process id of the process being executed. 

**Parameters:**
- `VarName`

**Syntax:**

```
GetProcessId as "<VarName>"
```

**Examples:**

```
GetProcessId as "ProcessId"
```

*Added: 2020-Jul-16*

---

### GetProcessName

> Get the process name of the process being executed. 

Get the process name of the process being executed. 

**Parameters:**
- `VarName`

**Syntax:**

```
GetProcessName as "<VarName>"
```

**Examples:**

```
GetProcessName as "ProcessName"
```

*Added: 2022-Feb-03*

---

### GetRoot

> Read "root" location.

Read the root folder of your user account on windows and store it in a variable.

**Parameters:**
- `varName`

**Syntax:**

```
GetRoot as "<varName>"
GetRoot
```

**Examples:**

```
GetRoot as "TuringFolderPath"
```

*Added: 2018-Nov-27*

---

### GetRunId

> Get the run id of the execution being made. 

Get the run id of the execution being made. 

**Parameters:**
- `VarName`

**Syntax:**

```
GetRunId as "<VarName>"
```

**Examples:**

```
GetRunId as "RunId"
```

*Added: 2020-Jul-17*

---

### GetTableVarValue

> Gets the value from a 2D list or table

Saves a specific value from a 2D list or table into a variable given two indexes. If the variable doesn't exist, it will be created. Instructions such as Excel ReadRows and DB RunOutputQuery generate 2D lists.

**Parameters:**
- `tableName`
- `row`
- `col`
- `varName`

**Syntax:**

```
GetTableVarValue "<tableName>" row={<row>} col={<col>} and save as "<varName>"
```

**Examples:**

```
GetTableVarValue "table1" row={1} col={5} and save as "value"
GetTableVarValue "UsersList" row={0} col={0} and save as "User1Name"
GetTableVarValue "UsersList" row={3} col={1} and save as "User4ID"
```

*Added: 2021-Apr-24*

---

### GetTextFromClipboard

> Get a string from the clipboard and save it in a variable.

Gets a string from the clipboard and saves it in a variable. With the exact value will avoid interpreting numbers when saved in the variable.

**Parameters:**
- `varName`

**Syntax:**

```
GetTextFromClipboard and save as "<varName>"
GetTextFromClipboard and save as "<varName>" with the exact value
```

**Examples:**

```
GetTextFromClipboard and save as "username"
GetTextFromClipboard and save as "numeroTexto" with the exact value
```

*Added: 2019-May-27*

---

### GetUser

> Get the mail of the user that is executing.

Get the mail of the user that is executing.

**Parameters:**
- `VarName`

**Syntax:**

```
GetUser as "<VarName>"
```

**Examples:**

```
GetUser as "ReportTo"
```

*Added: 2022-Feb-25*

---

### IF

Makes a comparison. Uses the logical operators <, >, >=, <=, ==, !=

**Parameters:**
- `booleanExpression`

**Syntax:**

```
if (<booleanExpression>)
##code goes here
end
```

**Examples:**

```
if (a < b)
if (a >= b)
if (a == b)
```

*Added: 2018-Mar-23*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/IF.pdf)

---

### IndexOf

> Get the Index (zero-based) of an element in a List.

Get the Index (zero-based) of a specific element in a List, and save it in the variables. You need to add as a parameter the name of the list and the string to be searched on the list. If the item does not exist in the list, the instruction will throw an error, unless you set the "--ignore" flag. If you don´t asign a name to the variable, the value of the index will save in a variable with the name "Index".

**Parameters:**
- `list`
- `element`
- `varName`
- `num`

**Syntax:**

```
IndexOf (<listName>,<element>) and save as <varName>
IndexOf (<listName>,<element>) and save as <varName> --ignore
IndexOf that contains (<list>,<element>) and save as <varName>
IndexOf that contains (<list>,<element>) and save as <varName> ; index= <num>
```

**Examples:**

```
IndexOf (TicketList,TicketNumber) and save as TicketListIndex
IndexOf that contains (TicketList,PORCENTAJE) and save as TicketListIndex
IndexOf that contains (TicketList,TicketNumber) and save as Var1 ; index= 2
```

*Added: 2018-Jun-11*

---

### IndexOf2DList

> Find the index where a text is located in a 2Dlist.

Find the index where a certain text or part of a text appears in a list. Only 2D lists are valid. 
Use rowIndexStartAt and columnIndexStartAt to set the initial position to start searching. SearchDirection means that when looking for a value, it will start looking for a value to the right (rows) o down (columns).
"Starting at" means that if for instance you are searching starting at 0,0. If the criteria is met, then it will return 0,0. When using "after" if will move either to the right o down depending on the searchDirection, and then it will start searching. 
If no occurrence is found, index will be -1, -1. 
Index is 0-based. 

**Parameters:**
- `list2DName`
- `rowIndexStartAt`
- `columIndexStartAt`
- `matchContents`
- `searchDirection`
- `criteria`
- `rowIndexVariable`
- `columnIndexVariable`

**Syntax:**

```
IndexOf2DList {<list2DName>} starting at [<rowIndexStartAt>,<columIndexStartAt>] match contents {<matchContents:exact|contains>} move {<searchDirection:rows|columns>} value {<criteria>} and save as [<rowIndexVariable>,<columnIndexVariable>]
IndexOf2DList {<list2DName>} after [<rowIndexStartAt>,<columIndexStartAt>] match contents {<matchContents:exact|contains>} move {<searchDirection:rows|columns>} value {<criteria>} and save as [<rowIndexVariable>,<columnIndexVariable>]
```

**Options:**

- `matchContents`: `exact`, `contains`
- `searchDirection`: `rows`, `columns`
- `matchContents`: `exact`, `contains`
- `searchDirection`: `rows`, `columns`

**Examples:**

```
IndexOf2DList {names} starting at [1,3] match contents {exact} move {rows} value {Gonzalez} and save as [rowIdx,columnIdx]
IndexOf2DList {names} after [1,3] match contents {exact} move {rows} value {Gonzalez} and save as [rowFound,columnFound]
IndexOf2DList {Comments} starting at [0,0] match contents {contains} move {columns} value {Err[0-9]{3}} and save as [rowIdx,columnIdx]
```

*Added: 2023-Jul-13*

---

### IndexOfList

> Find the index where a text appears in a list.

Find the index where a certain text or part of a text appears in a list. If no occurrence is found, index will be -1. Only 1D lists are valid. Use indexStartAt to find following occurrences. Index is 0-based. 

**Parameters:**
- `listName`
- `indexStartAt`
- `matchContents`
- `criteria`
- `indexVariable`

**Syntax:**

```
IndexOfList {<listName>} starting at {<indexStartAt>} match contents {<matchContents:exact|contains>} value {<criteria>} and save as {<indexVariable>}
```

**Options:**

- `matchContents`: `exact`, `contains`

**Examples:**

```
IndexOfList {names} starting at {0} match contents {contains} value {Gonzalez} and save as {index}
IndexOfList {names} starting at {100} match contents {exact} value {Ana} and save as {nextIndex}
IndexOfList {Comments} starting at {0} match contents {contains} value {Err[0-9]{3}} and save as {errorIdx}
```

*Added: 2023-Feb-20*

---

### IsMatch

> Find if one or more regex strings are matched within a text

Find if a list of one or more regex strings appear in a given text. It can be configured if all matches must be successful or if at least one is successful. 
If a comma is the subtext, the following regex expresion must be used [,] for it to be considered. The resulting variable will return True or False which can be compared in a regular if sentence (avoid powershell ifs).

**Parameters:**
- `variableName`
- `regex`
- `resultVariable`

**Syntax:**

```
IsMatch in variable {<variableName>} match any of [<regex1>,<regex2>...<regexN>] and save in {<resultVariable>}
IsMatch in variable {<variableName>} match all [<regex1>,<regex2>...<regexN>] and save in {<resultVariable>}
```

**Examples:**

```
IsMatch in variable {description} match any of [spanish,english,french] and save in {hasALanguage}
IsMatch in variable {description} match all [car,leather,red] and save in {isSportsCar}
IsMatch in variable {texto} match any of [[Ee]rror,warning] and save in {result}
```

*Added: 2022-Dec-16*

---

### JoinListValues

> Join all values in a list as a single string.

Join all values in a two dimentional list and save it as a variable, values can be appended with starting, ending characters and al different final character, or one of them or none. 
If new line is needed use \ n. 
 "Last with" syntax will replace the character at the very end with something else. It is specially useful when joining lists with commas with out ending in a comma, for example.

**Parameters:**
- `listVariableName`
- `variableName`
- `separatingCharactersIni`
- `separatingCharactersEnd`

**Syntax:**

```
JoinListValues from list {<listVariableName>} and save as {<variableName>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} starting with {<separatingCharactersIni>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} ending with {<separatingCharactersEnd>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} starting with {<separatingCharactersIni>} ending with {<separatingCharactersEnd>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} last with {<separatingCharactersLast>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} starting with {<separatingCharactersIni>} last with {<separatingCharactersLast>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} ending with {<separatingCharactersEnd>} last with {<separatingCharactersLast>}
JoinListValues from list {<listVariableName>} and save as {<variableName>} starting with {<separatingCharactersIni>} ending with {<separatingCharactersEnd>} last with {<separatingCharactersLast>}
```

**Examples:**

```
JoinListValues from list {theList} and save as {paragraph}
JoinListValues from list {idsList} and save as {joinedStrings} starting with {"} ending with {",} last with {"}
JoinListValues from list {idsList} and save as {joinedIds} ending with {,} last with {}
```

*Added: 2021-Jul-13*

---

### JSON

> Build a JSON variable.

Function used to build a JSON variables (dynamic key-value pairs).Used the "name" param to defined where to store the result or the variable to be modify(Variable Name).The merge syntax is used to join a JSON string into a existing JSON variable preloaded in the vars dictionary (defined by using the param name).The addKey syntax is abel to incorporated a new key an value to a preloaded JSON variable in the vars dictionary (defined by using the param name).

**Parameters:**
- `varName`
- `newKey`
- `jsonString`

**Syntax:**

```
JSON name=<varName> <jsonString>
JSON name=<varName> merge <jsonString>
JSON name=<varName> addKey="<newKey>" <jsonString>
```

**Examples:**

```
JSON name=item {"id":1}
JSON name=item merge {"role":"player"}
JSON name=item addKey="address" {"street1":"3098 Constitucion", "city":"Monterrey", "country":"Mexico"}
```

*Added: 2020-Feb-27*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/JSON.pdf)

---

### ListOperation

> Do "Set theory" operations with lists. i.e. union, insersect, substract.

Perform set theory operations on lists to get union, intersection or substraction of elements. Substraction will return the elements in listA that are not in listB but not otherwise. Union will return a list with all elements without repetition. Intersection will return a list with the elements that are present in all lists.

**Parameters:**
- `operation`
- `listName`
- `resultList`

**Syntax:**

```
ListOperation do {<operation:union|intersection|substraction>} with lists [<listNameA>,<listNameB>,...,<listNameN>] and save as {<resultList>}
```

**Options:**

- `operation`: `union`, `intersection`, `substraction`

**Examples:**

```
ListOperation do {union} with lists [listGroupA,listGroupB,listGroupC,listGroupD] and save as {allStudents}
ListOperation do {intersection} with lists [fordFeatures,nisanFeatures,hondaFeatures] and save as {commonFeatures}
ListOperation do {substraction} with lists [allTeams,teamsLost] and save as {notLosingTeams}
```

*Added: 2023-Feb-09*

---

### LoadDataDrivenList

> Load the Data Driven Json file from the process as a list of strings objects.

Load the Data Driven Json file from the process as a list of strings objects in the variables dictionary in order to be used with the foreach instruction and LoadDataDrivenObject.

**Parameters:**
- `VarName`

**Syntax:**

```
LoadDataDrivenList and save as "<VarName>"
```

**Examples:**

```
LoadDataDrivenList and save as "<VarName>"
```

*Added: 2020-Jul-30*

---

### LoadDataDrivenObject

> Load a JSON Object into the process variable dictionary with their respective keys keeping their values ​​as strings.

Loads a JSON Object into the process variable dictionary with their respective keys keeping their values ​​as strings.

**Parameters:**
- `InputJsonText`

**Syntax:**

```
LoadDataDrivenObject <InputJsonText>
```

**Examples:**

```
LoadDataDrivenObject <InputJsonText>
```

*Added: 2020-Jul-30*

---

### LoadIMGToClipboard

> Load an image to the clipboard.

Given a path to an image file, it will be loaded to the clipboard (as an image), so you will be able to paste it elsewhere.

**Parameters:**
- `path`

**Syntax:**

```
LoadIMGToClipboard "<path>"
```

**Examples:**

```
LoadIMGToClipboard "C:\Users\gilberto.isida\Pictures\word.PNG"
```

*Added: 2019-Dec-06*

---

### LoadJSON

> Read a JSON string and load its keys as variables.

Function used to read a JSON string and load its keys as variables. Use the object syntax to load JSON objects directly as FRIDA variables. List syntax will generate a list of JSON objects that can be iterated in a foreach and load their values with the object syntax. 
Object variable and list variable syntaxes may be better to avoid printing large json texts on log.

**Parameters:**
- `JsonString`
- `varName`
- `listVarName`

**Syntax:**

```
LoadJSON object "<JsonString>"
LoadJSON object variable "<varName>"
LoadJSON list "<JsonString>" and save as "<varName>"
LoadJSON list variable "<listVarName>" and save as "<varName>"
```

**Examples:**

```
LoadJSON object "{"street1":"3098 Constitucion", "city":"Monterrey", "country":"Mexico"}"
LoadJSON object variable "jsonVar"
LoadJSON list "[{ID:12345 , "Name" : "Innovation"},{ID:67890 , "Name" : "Softtek"}]" and save as "JsonObjectList"
```

*Added: 2020-Aug-24*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/LoadJSON.pdf)

---

### LoadVarToClipboard

> Load a variable to the clipboard.

Loads a variable to the clipboard.

**Parameters:**
- `varName`

**Syntax:**

```
LoadVarToClipboard "<varName>"
```

**Examples:**

```
LoadVarToClipboard "roles"
```

*Added: 2019-Mar-13*

---

### Lowercase

> Make a string lowercase and save it in a variable.

Make a string lowercase and save it in a variable.

**Parameters:**
- `aString`
- `newVarName`

**Syntax:**

```
Lowercase "<aString>" and save as "<newVarName>"
```

**Examples:**

```
Lowercase "someString, whatever you need" and save as "lower"
```

*Added: 2019-Dec-09*

---

### MakeRandom

> Generate a Random number between two numbers.

Generates a Random number between X and Y. Decimals and negatives are supported.

**Parameters:**
- `X`
- `Y`
- `varName`

**Syntax:**

```
MakeRandom between <X> and <Y> and save as <varName>
```

**Examples:**

```
MakeRandom between -500 and 1970.85 and save as rand
```

*Added: 2019-Aug-27*

---

### MathOperation

> Do a math operation and save the result in a variable.

Do a math operation (+ , - , * , / ) and save the result in the variable declared at the end of the instruccion, if the variable hasn't been declared it will be created.

**Parameters:**
- `number1`
- `operator`
- `number2`
- `number3`
- `result`

**Syntax:**

```
MathOperation <number1> <operator:+|-|*|/> <number2> and save as <result>
MathOperation <number1> * (<number2> - <number3>) and save as <result>
```

**Options:**

- `operator`: `+`, `-`, `*`, `/`

**Examples:**

```
MathOperation 2.22 + 5 and save as Result
MathOperation (5 * ( 1 + 3 ))/10 and save as Result
```

*Added: 2018-Jun-06*

---

### Message

Displays a given mesage in the run window.

**Parameters:**
- `text`

**Syntax:**

```
Message <text>
```

**Examples:**

```
Message The End
```

*Added: 2019-Nov-25*

---

### MEX_Factura_SAT

> MEXICO: Validate an XML file of an invoice against an IRS (Hacienda) webservice.

MEXICO: Validate an XML file of an invoice against an IRS (Hacienda) webservice. The 'rfcs' variable is a list of valid RFC codes, used to validate if the invoice was generated with the correct billing contact information. The result will be saved in a fixed variable named: CFDI_Result. The result is a Dictionary<string, dynamic>, you can read iterate it or use the 'ParseVariable' instruction.

**Parameters:**
- `archivoXML`
- `listaRFC`

**Syntax:**

```
MEX_Factura_SAT file={"<archivoXML>"}
```

**Examples:**

```
MEX_Factura_SAT file={"C:/Users/gilberto.isida/Downloads/factura.xml"}
```

*Added: 2021-Feb-11*

---

### NotificationService

> Call an existing NotHub service.

Calls a NotHub service that you previously created in http://automationplatform.azurewebsites.net/NotHub. If no message param is sent, the notification will contain the default message that was set at the moment of creation of the service.

**Parameters:**
- `id`
- `customMessage`

**Syntax:**

```
NotificationService "<id>"
NotificationService "<id>" message "<customMessage>"
```

**Examples:**

```
NotificationService "Jg5JUam9DloahQYywPWEKbH43"
NotificationService "Jg5JUam5DloahQYywPWEKbH43" message "This is an example"
```

*Added: 2018-Nov-26*

---

### NotifyDelays

> Configure the Notification via mail of unexpected delays in the execution. 

When excetuting with Turing Watcher, a notification mail will be sent to the "Disconnection Mail" list previously configured. This notification will be triggered when a line takes more than "delayTimeout" miliseconds to execute. Please configure accordingly to avoid a saturation of mails being sent. 
Normally this behaviour will happen when a popup blocks the RPA's execution or when DB or SAP instructions suffer a disconection or a delay of some sort. The RPA's excecution will not stop, but it will give a timely notification to diagnose and decide what to do with the process. 
Minimum delayTimeout is 10000 ms. 

**Parameters:**
- `delayTimeout`
- `additionalMessage`

**Syntax:**

```
NotifyDelays between instructions timeout "<delayTimeout>"
NotifyDelays between instructions timeout "<delayTimeout>" additional message "<additionalMessage>"
```

**Examples:**

```
NotifyDelays between instructions timeout "12000"
NotifyDelays between instructions timeout "15000" additional message "input sent. user: joe. File: file123.txt"
```

*Added: 2023-Nov-08*

---

### ParseDate

> Change a date's format.

This function reads a date and saves the date with the output format that is given.

**Parameters:**
- `inputDate`
- `cultureIn`
- `format`
- `cultureOut`
- `varName`

**Syntax:**

```
ParseDate from={<inputDate>} to={<format>} toCulture={<cultureOut>} out={<varName>}
ParseDate from={<inputDate>} fromCulture={<cultureIn:setCulture|cultureName>} to={<format>} toCulture={<cultureOut:setCulture|cultureName>} out={<varName>}
```

**Options:**

- `cultureIn`: `setCulture`, `cultureName`
- `cultureOut`: `setCulture`, `cultureName`

**Examples:**

```
ParseDate from={28/12/2020} to={dd/MMM/yyyy} toCulture={en} out={fecha}
ParseDate from={07/12/2021} fromCulture={setCulture} to={dd/MMM/yyyy} toCulture={en} out={fecha}
ParseDate from={44546} to={dd/MMM/yyyy} toCulture={setCulture} out={fecha}
```

*Added: 2022-Jan-20*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/ParseDate.pdf)

---

### ParseExactDate

> Change a date's format.

This function reads a date depending on the input's format that is used and saves the date with the output format that is given. This languages can be used (en,es,fr,de,pt). The default language is english.

**Parameters:**
- `Date`
- `InputFormat`
- `OutputFormat`
- `VariableName`

**Syntax:**

```
ParseExactDate from {<Date>} input {<InputFormat>} to output {<OutputFormat>} and save as {<VariableName>}
```

**Examples:**

```
ParseExactDate from {05/05/19} input {dd/MM/yy} to output {dd-MMM-yyyy} and save as {Date}
ParseExactDate from {30-Jun-2005} input {dd-MMM-yyyy es} to output {dd.MM.yy} and save as {Date}
ParseExactDate from {30-Jun-2005} input {dd-MMM-yyyy} to output {dd.MM.yy fr} and save as {Date}
```

*Added: 2019-Jul-09*

---

### ParseVariable

> Extract the value of a list, dictionary or XML variable in the dictionary and saves it in another one as a string.

Extracts the value of a list, dictionary or XML variable in the dictionary and saves it in another one as a string. This is useful for typing something contained in a collection or object. An XML with namespaces may need to use "default:" namespace in the XPath whenever a tag without a namespace is looked for.

**Parameters:**
- `varname`
- `childtree`
- `newVarName`

**Syntax:**

```
ParseVariable "<varname>" and save as "<newVarName>"
ParseVariable "<varname>" child "<childtree>" and save as "<newVarName>"
```

**Examples:**

```
ParseVariable "projectID" and save as "idProyecto"
ParseVariable "factura" child "TicketForXML/Header/Fields/field[@Name='NombreEmisor']/Value" and save as "nombreEmisor"
ParseVariable "XMLwithNamespaces" child "/default:TicketForXML/h:Header/h:Fields/c:field/c:name" and save as "nameFound"
```

*Added: 2019-Jan-25*

---

### PasteVar

> Load a variable's content to the clipboard and paste it in the active window/field.

Loads an item of theVariablesHelper.vars dictionary to the clipboard, and then it is pasted in the active window/field.

**Parameters:**
- `varName`

**Syntax:**

```
PasteVar "<varName>"
```

**Examples:**

```
PasteVar "roles"
```

*Added: 2019-Jan-30*

---

### Ping

> Send a ping to a host by url or IP address.

Send a ping to a host by url or IP address. Variables for PING_STATUS and PING_TRIPTIME are created automatically.

**Parameters:**
- `host`

**Syntax:**

```
Ping <host>
```

**Examples:**

```
Ping 216.58.193.132
Ping www.google.com
```

*Added: 2019-Dec-10*

---

### ReadPDFasText

> Read the whole content of a PDF file and store it as text in a variable.

Reads the whole content of a PDF file and stores it as text in a variable.

**Parameters:**
- `path`
- `varKey`

**Syntax:**

```
ReadPDFasText "<path>" as "<varKey>"
```

**Examples:**

```
ReadPDFasText "C:\entradas\archivo.pdf" as "pdfKey"
```

*Added: 2020-Nov-10*

---

### RegexReplace

> Replace a regular expresion match for a substring in a variable or a list of expresions.

Replaces all occurrences of searchSubstring in the varName's contents for the value in replaceSubstring and saves the result back in varName. Beware that "\" is escaped in the replaceSubtring and special characters as new line or tab can only be used with "unescaped" syntax.
The "list" syntax can replace a list of expresions at once. If you need to replace a comma, it must be escaped with a backslash before the comma (\) so it will not be interpreted as the next element in the list of expresions. 
To make sure it replaces whole words enclose the word between \b
.  
Capture groups are valid and $CaptureGroupNum may be used to include the group in the replaceSubtring, for example considering search string "(.+)\.", replace string "$1_old." and string "C:\Documents\user\file.txt". Capture group (.+) is taking all characters until a "." is found (\.). So the value after the replacemet will be "C:\Documents\user\file_old.txt".

**Parameters:**
- `searchSubstring`
- `replaceSubstring`
- `varName`

**Syntax:**

```
RegexReplace {<searchSubstring>} for {<replaceSubstring>} in {<varName>}
RegexReplace {<searchSubstring>} for unescaped {<replaceSubstring>} in {<varName>}
RegexReplace list [<searchSubstring1>,<searchSubstring2>,...,<searchSubstringn>] for [<replaceSubstring>,<replaceSubstring1>,...,<replaceSubstringn>] in {<varName>}
RegexReplace list [<searchSubstring1>,<searchSubstring2>,...,<searchSubstringn>] for unescaped [<replaceSubstring>,<replaceSubstring1>,...,<replaceSubstringn>] in {<varName>}
```

**Examples:**

```
RegexReplace { } for {|} in {varLines}
RegexReplace {\n} for {} in {varLines}
RegexReplace {found,} for unescaped {found\n} in {varLines}
```

*Added: 2021-Jun-23*

---

### RemoveDuplicatesInList

> Remove duplicate elements in a list variable.

Remove duplicate elements from a List or 2D List. The elements will be removed from the original List unless specified to be saved with a different variable name.

**Parameters:**
- `ListName`
- `NewListName`

**Syntax:**

```
RemoveDuplicatesInList {<ListName>}
RemoveDuplicatesInList {<ListName>} and save as {<NewListName>}
```

**Examples:**

```
RemoveDuplicatesInList {RunDateList}
RemoveDuplicatesInList {UsersInfo2DList}
RemoveDuplicatesInList {RunDateList} and save as {DaysExecuted}
```

*Added: 2022-Apr-22*

---

### RemoveFromList

> Remove elements from a list by index or a criteria

Remove elements from a list by specifying an index, set of comma separated indexes, a contained string or a given RegEx. Syntaxes include an "except" variation that removes all the elements from the list except the ones at the given index(es) or matching the given criteria. Using -1 as an index will point to the last element of the list.

**Parameters:**
- `ListName`
- `Index`
- `Text`
- `RegEx`

**Syntax:**

```
RemoveFromList {<ListName>} elements by index {<Index>}
RemoveFromList {<ListName>} elements by index except {<Index>}
RemoveFromList {<ListName>} elements that contain {<Text>}
RemoveFromList {<ListName>} elements that contain except {<Text>}
RemoveFromList {<ListName>} elements that match {@RegEx(<RegEx>)}
RemoveFromList {<ListName>} elements that match except {@RegEx(<RegEx>)}
```

**Examples:**

```
RemoveFromList {MyNumbers} elements by index {3}
RemoveFromList {MyNumbers} elements by index except {0,1,2,-1}
RemoveFromList {MailsList} elements that contain {@gmail.com}
```

*Added: 2021-Dec-28*

---

### RemoveNonAscii

> Change a string to remove mainly accents and other diacritics and save it in a variable.

Change a string to remove mainly accents and other diacritics and save it in a variable.

**Parameters:**
- `varName`
- `newVar`

**Syntax:**

```
RemoveNonAscii variable {<varName>} and save as {<newVar>}
```

**Examples:**

```
RemoveNonAscii variable {Name} and save as {NameNoAccents}
```

*Added: 2023-Aug-25*

---

### ReplaceFromVariable

> Replace text in a variable.

Replaces on an existing variable a text for a different one. 
List syntax must have the same amount of items in the searching list an the replacement list. It will change every subtext in the order it is given for the corresponding item in the same position of the replacement list. 
If a comma is the subtext you must write COMMA so the function will recognize the subtext

**Parameters:**
- `VariableName`
- `TextToReplace`
- `NewText`

**Syntax:**

```
ReplaceFromVariable {<VariableName>} this {<TextToReplace>} for {<NewText>}
ReplaceFromVariable {<VariableName>} this list [<TextToReplace1>,<TextToReplace2>,...,<TextToReplacen>] for [<NewText1>,<NewText2>,...,<NewTextn>]
```

**Examples:**

```
ReplaceFromVariable {MyVariable} this {+} for {-}
ReplaceFromVariable {MyNumber} this {.00} for {}
ReplaceFromVariable {MyEmail} this {@vectoritc.com} for {@softtek.com}
```

*Added: 2019-Sep-25*

---

### ResetVariables

> Empty the contents of the given mixed reader variables.

Erases the content on existing variables, setting them to null by default or empty string. Lists will be cleared. Numbers will always be set to 0.

**Parameters:**
- `variableName1`
- `variableName2`
- `variableNameN`

**Syntax:**

```
ResetVariables [<variableName1>,<variableName2>...<variableNameN>]
ResetVariables [<variableName1>,<variableName2>...<variableNameN>] with empty string
```

**Examples:**

```
ResetVariables [fileName] with initial value
ResetVariables [counter1, counter2, counter3]
ResetVariables [totalVar,nombreVar,usuarioList]
```

*Added: 2022-Aug-31*

---

### REST

> Call an external API.

Calls an external API, similar to cURL. The request's headers and body can be defined. You may define any of the following in any order: Authorization, body, Parameters, headers, requestType, files, timeout. The Content-Type is set by default to application/json;charset=utf-8, it can only be changed to multipart/form-data or text/plain by specifying it through the Request-Type. Timeout values are in milliseconds. 
The API call saves the request's response as "statusCode[string]", "restResponseTime[string]", "response[string]". "responseList[List]"* and "responseDict[Dictionary]"* in the variables. 
If the response is an image, it's value will be stored as a Base 64 string. 
*Only if the response can be deserialized as such objects.

**Parameters:**
- `verb`
- `url`
- `H`
- `body`
- `json`
- `headerName`
- `headerValue`
- `basic`
- `filePath`
- `timeoutMS`

**Syntax:**

```
REST <verb> url=<url>
REST <verb> url=<url> body <json>
REST <verb> url=<url> timeout={<timeoutMs>}
REST <verb> url=<url> headers(<headerName>:<headerValue>, ... ,<headerNameN>:<headerValueN>) body <json>
REST <verb> url=<url> Authorization={<Basic User:Password/Bearer token/BasicB64 B64EncodedUserAndPassword/NTLM User:Password>}
REST <verb> url=<url> requestType={text/plain} body <json>
REST <verb> url=<url> requestType={multipart/form-data} Authorization={<Basic User:Password/Bearer token/BasicB64 B64EncodedUserAndPassword/NTLM User:Password>}
REST <verb> url=<url> requestType={multipart/form-data} Parameters={<params>} files=[<filePath1>, ... , <filePathN>]
REST <verb> url=<url> requestType={multipart/form-data} files=[<filePath1>, ... ,<filePathN>]
```

**Examples:**

```
REST GET url=http://www.google.com
REST POST url=https://innotek-8f84c.firebaseio.com/REST_TESTS/PUT?auth=XYZ Authorization={Bearer OAuthToken} body {"Player":"One"} timeout={10000}
REST POST url=https://innotek-8f84c.firebaseio.com/REST_TESTS/PUT?auth=XYZ requestType={multipart/form-data} Authorization={Basic User:Password} body {"Player":"One"} files=["C:\Users\gilberto.isida\Downloads\pruebas.txt","C:\Users\gilberto.isida\Downloads\pruebas2.txt"]
```

*Added: 2019-May-07*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/REST.pdf)

---

### ReverseString

> Reverse the order of the characters in a string.

This will reverse the order of the characters that are contained in a string. Example: given "Hello", the return will be "olleH".

**Parameters:**
- `inputString`
- `newVarName`

**Syntax:**

```
ReverseString "<inputString>" and save as "<newVarName>"
```

**Examples:**

```
ReverseString "Hello" and save as "reversed"
```

*Added: 2019-Dec-09*

---

### RoundAllNumbersTo

> Round all the numbers that have decimal value and are going to be saved in the variables to a specific amount of decimal places.

Round all the numbers that have decimal value and are going to be saved in the variables to a specific amount of decimal places. 
By default all numbers are rounded to 2 decimal numbers, if no rounding is desired, use "none".

**Parameters:**
- `Int`

**Syntax:**

```
RoundAllNumbersTo "<Int>"
RoundAllNumbersTo "none"
```

**Examples:**

```
RoundAllNumbersTo "5"
RoundAllNumbersTo "none"
```

*Added: 2020-Apr-21*

---

### RunAsync

> Run an external program (CustomLocal), but asynchronously.

Run an external program (CustomLocal), but asynchronously... that means, it will be invoked in a thread and continue the current script without waiting for the CustomLocal to finish. There will be no communication from the CustomLocal back to the FRIDA main thread.

**Parameters:**
- `Script`
- `Argument`

**Syntax:**

```
RunAsync <Script>
RunAsync <Script> <Argument1>
RunAsync <Script> "<Argument1>" , "<Argument2>"
```

**Examples:**

```
RunAsync MyCustomAsync
RunAsync FileDownLoad TestArgument
RunAsync CaptchaSolver Username Password
```

*Added: 2021-Jan-25*

---

### RunBatch

> Run a Batch script.

Run a Batch script. To use a variable inside your script use the placeholders <<VarName>> and <<<VarName>>> on your script as you would on a Reader Script. WriteInput may take "y" or "N" as values. Warning: UTF8 is not supported.

**Parameters:**
- `Script`
- `input`

**Syntax:**

```
Bat <Script>.txt
Batch <Script>.txt
RunBatch <Script>.txt
RunBat <Script>.txt
RunBat <Script>.txt writeInput={<input:y|N>}
```

**Options:**

- `input`: `y`, `N`

**Examples:**

```
Bat Write.txt
Batch Write.txt
RunBatch Write.txt
```

*Added: 2019-Sep-09*

---

### RunBatchAsync

> Run a Batch script in asynchronous mode.

Run a Batch script asynchronously. To use a variable inside your script use the placeholders <<VarName>> and <<<VarName>>> on your script as you would on a Reader Script. The actions performed by the batch script will not be waited upon by Turing, and there will be no comunication back to Turing.

**Parameters:**
- `Script`

**Syntax:**

```
RunBatchAsync <Script>.txt
```

**Examples:**

```
RunBatchAsync LoadExternalApp.txt
```

*Added: 2021-Feb-11*

---

### RunCustomLocal

> Run an external program (CustomLocal).

Run a RunCustomLocal script, to assign a value to a defined FRIDA variable from within the CustomLocal script use Console.WriteLine("<VarName> : <Value>"); To throw an error use the syntax Console.WriteLine("Error : <Value>"); To force availability of console outputted variables even when an error is thrown, ForceVarsToSave syntax can be used.

**Parameters:**
- `script`
- `argument1`
- `argument2`

**Syntax:**

```
RunCustomLocal <script>
RunCustomLocal <script> <argument1>
RunCustomLocal <script> "<argument1>" , "<argument2>"
RunCustomLocal <script> ForceVarsToSave
RunCustomLocal <script> ForceVarsToSave "<argument1>" , "<argument2>"
```

**Examples:**

```
RunCustomLocal MyProgram
RunCustomLocal MyProgram TestArgument1
RunCustomLocal MyProgram TestArgument1 , TestArgument2
```

*Added: 2018-Sep-28*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/RunCustomLocal.pdf)

---

### RunFRIDAProcess

> Run a FRIDA Process.

Run a FRIDA Process sharing all the variables that are active on the main script. Step variables must be declared in both processes or given as arguments.

**Parameters:**
- `processID`
- `stepVarName1`
- `stepVarName2`
- `arg1`
- `arg2`

**Syntax:**

```
RunFRIDAProcess <processID>
RunFRIDAProcess <processID> , <stepVarName1> : <arg1> , <stepVarName2> : <arg2> , ...
RunProcess <processID>
RunProcess <processID> , <stepVarName1> : <arg1> , <stepVarName2> : <arg2> , ...
```

**Examples:**

```
RunFRIDAProcess 123456
RunFRIDAProcess 123456 , UserName : Innovation@softtek.com , Password : Pa$$word
RunProcess 123456
```

*Added: 2020-May-25*

---

### RunPowerShell

> Run a PowerShell script.

Run a PowerShell script. To add a variable as a result, use "Write-Output <VarName> : <Value>" within the powershell script. To report an error use "Write-Output Error : <Value>". 
If <Value> contains the word "error", RunPowerShell will interpret it as if an error has occurred, to avoid the interpretation use "avoid error interpretation" syntax.

**Parameters:**
- `Script`

**Syntax:**

```
PowerShell <Script>
RunPowerShell <Script>
RunPowerShell <Script> avoid error interpretation
```

**Examples:**

```
PowerShell Write.txt
RunPowerShell Write.txt
RunPowerShell Write.ps1
```

*Added: 2018-Jun-27*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/RunPowerShell.pdf)

---

### RunScript

> Run a FRIDA Script.

Run a FRIDA Script sharing all the variables that are active on the main script. 

**Parameters:**
- `Script`

**Syntax:**

```
RunScript <Script>.txt
RunScript<Script>
```

**Examples:**

```
RunScript Write.txt
RunScript Write
```

*Added: 2019-Aug-09*

---

### SaveClipboardImage

> Save an image from the clipboard.

Gets an image from the clipboard and saves a PNG file in the given path.

**Parameters:**
- `path`

**Syntax:**

```
SaveClipboardImage {"<path>"}
```

**Examples:**

```
SaveClipboardImage {"C:\\Users\\gilberto.isida\\Desktop\\prueba.png"}
```

*Added: 2019-Jul-31*

---

### SaveExactValues

> Set state to save variables with unchanged texts.

On activation, all other Turing functions will save variables with the value as is. Meaning it won't try to convert the value to number and therefore loose the thousands separator or decimal digits. If needed, the state can be turned off to take advantage of variables interpreted as numbers.

**Parameters:**
- `saveState`

**Syntax:**

```
SaveExactValues <saveState:On|Off>
```

**Options:**

- `saveState`: `On`, `Off`

**Examples:**

```
SaveExactValues On
SaveExactValues Off
```

*Added: 2019-Jul-05*

---

### SendEmailAttach2

> Send an email with multiple attachments.

Send an email with multiple attachments. This function does not require the <<<>>> to indicate the variable that defines the body for the email.

**Parameters:**
- `varKey`
- `Address`
- `Subject`
- `Attachment`
- `Path`

**Syntax:**

```
SendEmailAttach2 <varKey> To "<Address>" Subject "<Subject>" Attachments "<Attachment1>,<Attachment2>" Path "<Path>"
```

**Examples:**

```
SendEmailAttach2 body To "faustino.villarreal@softtek.com" Subject "TestSub" Attachments "Book1.xlsx,acciones.txt" Path "C:\Users\productivity\Desktop"
```

*Added: 2019-Oct-06*

---

### SendEmailAttachEmbebed

> Send an email with multiple attachments embeded in mail's body.

Send an email with multiple attachments embeded in mail's body. This function does not require the <<<>>> to indicate the variable that defines the body for the email.

**Parameters:**
- `varKey`
- `Address`
- `Subject`
- `Attachment1`
- `Attachment2`
- `Path`

**Syntax:**

```
SendEmailAttachEmbebed <varKey> To "<Address>" Subject "<Subject>" Attachments "<Attachment1>,<Attachment2>" Path "<Path>"
```

**Examples:**

```
SendEmailAttachEmbebed body To "faustino.villarreal@softtek.com" Subject "TestSub" Attachments "Book1.xlsx,acciones.txt" Path "C:\Users\productivity\Desktop"
```

*Added: 2020-Jun-17*

---

### SendEmailAttachments

> Send an email with multiple attachments.

Send an email with multiple attachments located in a given path.

**Parameters:**
- `varKey`
- `Address`
- `Subject`
- `Attachment`
- `Path`

**Syntax:**

```
SendEmailAttachments <varKey> To "<Address>" Subject "<Subject>" Attachments "<Attachment>" Path "<Path>"
SendEmailAttachments <varKey> To "<Address>" Subject "<Subject>" Attachments "<Attachment1>,<Attachment2>" Path "<Path>"
```

**Examples:**

```
SendEmailAttachments body To "faustino.villarreal@softtek.com" Subject "TestSub" Attachments "Book1.xlsx,acciones.txt" Path "C:\Users\productivity\Desktop"
SendEmailAttachments body To "andres.cruz@softtek.com" Subject "FRIDA Test SendEmailAttachments" Attachments "NO" Path "C:"
```

*Added: 2020-Jun-27*

---

### SendEmailSelectSender

> Send an email with multiple attachments from a given account.

Sends an email with multiple attachments from a desired account specified as "Sender" in the function. BodyVarKey variable is where the e-mail's body will be read from. It doesn't require the enclosing <<<>>>. It may include HTML tags to format the body's content, including <BR> for new line. Attachment files must be stored in "Path". If none is required, the word "NO" must be placed instead. You can also specify the name of a variable that contains the HTML string for the email signature.

**Parameters:**
- `bodyVarKey`
- `address`
- `sender`
- `CCAddress`
- `subject`
- `attachment`
- `path`
- `signatureVar`

**Syntax:**

```
SendEmailSelectSender <bodyVarKey> From "<sender>" To "<address>" Subject "<subject>" Attachments "<attachment>" Path "<path>"
SendEmailSelectSender <bodyVarKey> From "<sender>" To "<address>" CC "<CCAddress>" Subject "<subject>" Attachments "<attachment>" Path "<path>"
SendEmailSelectSender <bodyVarKey> From "<sender>" To "<address>" CC "<CCAddress>" Subject "<subject>" Attachments "<attachment>" Path "<path>" Signature {"<signatureVar>"}
SendEmailSelectSender <bodyVarKey> From "<sender>" To "<address>;<address>" Subject "<subject>" Attachments "<attachment1>,<attachment2>" Path "<path>"
SendEmailSelectSender <bodyVarKey> From "<sender>" To "<address>;<address>" CC "<CCAddress>;<CCAddress>" Subject "<subject>" Attachments "<attachment1>,<attachment2>" Path "<path>"
```

**Examples:**

```
SendEmailSelectSender body From "softtekaccount@softtek.com" To "faustino.villarreal@softtek.com" Subject "TestSub" Attachments "Book1.xlsx,acciones.txt" Path "C:\Users\productivity\Desktop"
SendEmailSelectSender body From "softtekaccount@softtek.com" To "faustino.villarreal@softtek.com" Subject "TestSub" Attachments "NO" Path "C:\"
SendEmailSelectSender body From "softtekaccount@softtek.com" To "faustino.villarreal@softtek.com" CC "user@softtek.com;seconduser@softtek.com" Subject "TestSub" Attachments "NO" Path ""
```

*Added: 2019-Dec-10*

---

### SendFile

> If the file exists in the path it will be uploaded to Azure at the end of the execution without generating an error if it doesn't exist.

If the file exists in the path it will be uploaded to Azure at the end of the execution without generating an error if it doesn't exist.

**Parameters:**
- `FilePath`

**Syntax:**

```
SendFile <FilePath>
sendfile <FilePath>
```

**Examples:**

```
SendFile C:\Users\andres.cruz\Desktop\file.txt
sendfile C:\Users\andres.cruz\Desktop\file.txt
```

*Added: 2018-Mar-02*

---

### SendMail

> Send an email to a list of email addresses.

Sends an email to a list of email addresses. The subject and body must be set. Optionally, Multiple files can be included as attachment.

**Parameters:**
- `Subject`
- `Mail`
- `Body`
- `FilePath`
- `TemplateName`

**Syntax:**

```
SendMail with the template "<TemplateName>"
SendMail with subject "<Subject>" to "<Mail>" with body "<Body>"
SendMail with subject "<Subject>" to "<Mail>" with body "<Body>" and a file attachment "<FilePath>"
SendMail with subject "<Subject>" to "<Mail>" with body "<Body>" and the file attachments "<FilePath>,<FilePath>,..."
SendMail with subject "<Subject>" to "<Mail>" with htmlbody "<Body>"
SendMail with subject "<Subject>" to "<Mail>" with htmlbody "<Body>" and a file attachment "<FilePath>"
SendMail with subject "<Subject>" to "<Mail>" with htmlbody "<Body>" and a file attachment "<FilePath>,<FilePath>,..."
```

**Examples:**

```
SendMail with the template "ErrorMailTemplate"
SendMail with subject "Test Send Mail" to "andres.cruz@softtek.com , gilberto.isida@softtek.com" with body "Test mail"
SendMail with subject "Test Send Mail" to "andres.cruz@softtek.com" with body "Test mail" and a file attachment "C:\Users\user\Downloads\log.txt"
```

*Added: 2021-Aug-25*

---

### SendNotification

> Sends a Mail using the given notification template.

Sends a Mail using the given notification template which was previously defined using the "Notification" tab.

**Parameters:**
- `NotificationTemplate`

**Syntax:**

```
SendNotification "<NotificationTemplate>"
```

**Examples:**

```
SendNotification "DefaultNotificationTemplate1"
```

*Added: 2021-Aug-06*

---

### SendSMTP

> Send an email through the SMTP protocol.

Send an email to a single receiver using the SMTP protocol. The body message can be in HTML. Use optional parameter Attachments to include comma-separated file paths to be attached to the mail. Use optional parameters CC or BCC to add comma-separated carbon copy recipients. Unless explicitly specified, the host will be smtp.office365.com  through the port 587.

**Parameters:**
- `Mail`
- `Password`
- `DestinyMail`
- `Subject`
- `Body`
- `host`
- `port`
- `FilePath`
- `CCMail`
- `BCCMail`

**Syntax:**

```
SendSMTP From={Mail:<Mail>, Pass:<Password>} To={<DestinyMail1>,<DestinyMail2>,...,<DestinyMailN>} Subject={<Subject>} Body={<Body>} Attachments={<FilePath1>,<FilePath2>,...,<FilePathN>} CC={<CCMail1>,<CCMail2>,...,<CCMailN>} BCC={<BCCMail1>,<BCCMail2>,...,<BCCMailN>}
SendSMTP Host={<host>} Port={<port>} From={Mail:<Mail>, Pass:<Password>} To={<DestinyMail1>,<DestinyMail2>,...,<DestinyMailN>} Subject={<Subject>} Body={<Body>} Attachments={<FilePath1>,<FilePath2>,...,<FilePathN>} CC={<CCMail1>,<CCMail2>,...,<CCMailN>} BCC={<BCCMail1>,<BCCMail2>,...,<BCCMailN>}
```

**Examples:**

```
SendSMTP From={Mail:innovation@softtek.com, Pass:MyPassword} To={username@company.com} Subject={SMTP Test Mail} Body={This is a test message}
SendSMTP From={Mail:innovation@softtek.com, Pass:MyPassword} To={username@company.com} Subject={SMTP Test Mail} Body={This is a test message} Attachments={C:\Users\Desktop\ExcelFile1.xlsx,C:\Users\Desktop\ExcelFile2.xlsx} CC={username2@company.com,username4@othercompany.com} BCC={support@company.com}
SendSMTP Host={smtp.office365.com} Port={587} From={Mail:innovation@softtek.com, Pass:MyPassword} To={username@company.com} Subject={SMTP Test Mail} Body={This is a test message}
```

*Added: 2021-Apr-15*

---

### SendTeamsMessage

> Sends a message to a teams channel via webhook

Sends a message request to a specified teams webhook, the request contains an optional title and the text of the message (in markdown)

**Parameters:**
- `url`
- `title`
- `message`

**Syntax:**

```
SendTeamsMessage url={<url>} message={<message>}
SendTeamsMessage url={<url>} title={<title>} message={<message>}
```

**Examples:**

```
SendTeamsMessage url={https://webhookurl.com} message={How are you?}
SendTeamsMessage url={https://webhookurl.com} title={Example title} message={# Hello!}
```

*Added: 2021-Jun-03*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/SendTeamsMessage.pdf)

---

### SendVariable

> Upload a variable to the FRIDA database at the end of the execution without generating an error if it doesn't exist. The variable will be displayed as a string in the process analytics dashboard.

If the variable exists in the process it will be uploaded to the FRIDA database at the end of the execution without generating an error if it doesn't exist. The variable will be will be displayed as a string in the process analytics dashboard.

**Parameters:**
- `VariableName`

**Syntax:**

```
SendVariable "<VariableName>"
```

**Examples:**

```
SendVariable "DocumentosProcesados"
sendvariable "NumeroDeIncidencias"
Sendvariable "CorreosIdentificados"
```

*Added: 2020-Jul-13*

---

### SetCulture

> [BETA] Change the current thread's Culture, for interpreting dates and numbers.

[BETA] This function changes the Culture provider that allows the machine's understanding of dates and numbers (decimal and thousand separator). This is still under consideration, and not generally available.

**Parameters:**
- `cultureName`

**Syntax:**

```
SetCulture <cultureName>
```

**Examples:**

```
SetCulture en-US
SetCulture es-MX
SetCulture es-ES
```

*Added: 2020-Nov-04*

---

### SetLogLevel

> Change level of detail in log.

Changes the amount of information written in the log. Levels are Verbose, Log, OnlyErrors, Debug and Off. By default it is in Verbose. 
Log level shows only RPAs initial general information, entry points in functions and result (Success, Error), as well as logical structure logs. 
OnlyErrors will only show error detail if any. 
Debug will print any available additional details. 
Off will turn log printing off until stated otherwise.

**Parameters:**
- `level`

**Syntax:**

```
SetLogLevel <level:Verbose|Log|OnlyErrors|Debug|Off>
```

**Options:**

- `level`: `Verbose`, `Log`, `OnlyErrors`, `Debug`, `Off`

**Examples:**

```
SetLogLevel Off
SetLogLevel OnlyErrors
```

*Added: 2022-Sep-21*

---

### SetRunTimeout

> Limit the time an automation will be allowed to run.

Setting a timeout will enable a rule that terminates the execution if the specified time exceeds. When we reach the timeout, the ongoing instruction is allowed to end before throwing an error.

**Parameters:**
- `hours`
- `minutes`
- `seconds`

**Syntax:**

```
SetRunTimeout <hours> <minutes> <seconds>
```

**Examples:**

```
SetRunTimeout 0 0 30
SetRunTimeout 1 30 0
```

*Added: 2021-Mar-08*

---

### SetVarMode

> [BETA] Enable or disable the CultureProvider when saving variables.

[BETA] Sets a runtime configuration parameter, for deciding how to save the variable values. Select "infer" to use the current Culture Provider and parse the value to an appropriate numeric or DateTime object. Select "object" to save the variable AS-IS, with no parsing applied. This is still under consideration, and not generally available.

**Parameters:**
- `mode`

**Syntax:**

```
SetVarMode <mode>
```

**Examples:**

```
SetVarMode object
SetVarMode infer
```

*Added: 2020-Nov-04*

---

### SFTP Change Permissions

> Change the permissions of a file in an FTP directory.

Change the permissions of a file in an FTP directory, mode should be written in octal representation.

**Parameters:**
- `host`
- `port`
- `user`
- `password`
- `file`
- `path`
- `mode`

**Syntax:**

```
SFTP Change Permissions host={<host>} user={<UserName>} password={<Password>} file path={<FilePath>} mode={<mode>}
SFTP Change Permissions host={<host>} port={<port>} user={<UserName>} password={<Password>} file path={<FilePath>} mode={<mode>}
```

**Examples:**

```
SFTP Change Permissions host={frida.server.com} user={frida} password={********} file path={/FRIDA_Files/File.txt} mode={0777}
SFTP Change Permissions host={frida.server.com} port={4222} user={frida} password={********} file path={/FRIDA_Files/File.txt} mode={0777}
```

*Added: 2021-Nov-17*

---

### SFTP Create Directory

> Create a directory in an FTP server, if multiple levels are needed the instruction will create them recursively.

Create a directory in an FTP server, if multiple levels are needed the instruction will create them recursively.

**Parameters:**
- `host`
- `user`
- `password`
- `directory`
- `port`

**Syntax:**

```
SFTP Create Directories host={<Host>} user={<UserName>} password={<Password>} directory={<Directory>}
SFTP Create Directories host={<Host>} port={<Port>} user={<UserName>} password={<Password>} directory={<Directory>}
```

**Examples:**

```
SFTP Create Directories host={frida.server.com} user={frida} password={********} directory={/FRIDA_Files/Scripts/RPA/Execute/}
SFTP Create Directories host={frida.server.com} port={4222} user={frida} password={********} directory={/FRIDA_Files/Scripts/RPA/Execute/}
SFTP Create Directories host={frida.server.com} port={4222} user={frida} password={********} directory={/FRIDA_Files/Scripts/RPA/Execute/}
```

*Added: 2021-Dec-16*

---

### SFTP Download

> Download a file from an FTP server.

Download a file to a local directory from an FTP server. If the local directory does not exist, it is created.

**Parameters:**
- `host`
- `port`
- `user`
- `password`
- `fileName`
- `destinyFolderName`
- `originFolderName`

**Syntax:**

```
SFTP Download host={<host>} user={<userName>} password={<password>} remote location={<originFolderName>} file name={<fileName>} local destination={<destinyFolderName>}
SFTP Download host={<host>} port={<port>} user={<userName>} password={<password>} remote location={<originFolderName>} file name={<fileName>} local destination={<destinyFolderName>}
```

**Examples:**

```
SFTP Download host={frida.server.com} user={frida} password={********} remote location={/FRIDA_Files/transactions/} file name={TextFile.txt} local destination={C:\Users\frida\Desktop\DestinyFolder}
SFTP Download host={frida.server.com} port={4222} user={frida} password={********} remote location={/FRIDA_Files/transactions/} file name={TextFile.txt} local destination={C:\Users\frida\Desktop\DestinyFolder}
```

*Added: 2021-Nov-16*

---

### SFTP List

> List all the directories and files from an FTP Location.

List all the directories and files from an FTP Location, output will be stored in a list named "Output".

**Parameters:**
- `host`
- `port`
- `user`
- `password`
- `folder`
- `name`

**Syntax:**

```
SFTP List host={<host>} user={<UserName>} password={<Password>} location={<FolderName>}
SFTP List host={<host>} port={<port>} user={<UserName>} password={<Password>} location={<FolderName>}
```

**Examples:**

```
SFTP List host={frida.server.com} user={frida} password={*******} location={/FRIDA_Files/}
SFTP List host={frida.server.com} port={4222} user={frida} password={*******} location={/FRIDA_Files/}
```

*Added: 2021-Nov-16*

---

### SFTP Upload

> Upload a file to a remote FTP server.

Upload a file to a remote FTP server.

**Parameters:**
- `host`
- `userName`
- `password`
- `destinationFolder`
- `filetoUpload`
- `port`

**Syntax:**

```
SFTP Upload host={<host>} user={<userName>} password={<password>} location={<destinationFolder>} file={<filetoUpload>}
SFTP Upload host={<host>} port={<port>} user={<userName>} password={<password>} location={<destinationFolder>} file={<filetoUpload>}
```

**Examples:**

```
SFTP Upload host={frida.server.com} user={frida} password={*********} location={/FRIDA_Files/} file={C:\Users\frida\Desktop\Samples\sample1.xlsx}
SFTP Upload host={frida.server.com} port={4222} user={frida} password={*********} location={/FRIDA_Files/} file={C:\Users\frida\Desktop\Samples\sample1.xlsx}
```

*Added: 2020-Oct-11*

---

### SHA1

> Hashes a string.

(THIS IS NOT ENCRYPTION) Hashes a string using this class reference https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha1cryptoserviceprovider?view=netframework-4.8. The result will be saved in a new variable named "shaString".

**Parameters:**
- `yourString`

**Syntax:**

```
SHA1 <yourString>
```

**Examples:**

```
SHA1 HelloWorld
```

*Added: 2019-Dec-05*

---

### ShowLogInfo

> Turn verbose printing of aditional information of some instructions in the log.

Prints aditional information of instructions in the log. By default it is On. If turned off, it will no longer show the list values when extracted by some instructions. 

**Parameters:**
- `showState`

**Syntax:**

```
ShowLogInfo <showState:On|Off>
```

**Options:**

- `showState`: `On`, `Off`

**Examples:**

```
ShowLogInfo Off
```

*Added: 2020-Jul-02*

---

### SOAP

> Call an external SOAP WebService.

Calls an external SOAP WebService. It can contain Basic auth, and request params. An xml template is required. The response is saved as a plain string. See ExtraDocs for more details.

**Parameters:**
- `theURL`
- `xmlBodyTemplate`
- `userName`
- `thePass`
- `responseName`
- `hostAddress`
- `h1`
- `h2`
- `val1`
- `val2`

**Syntax:**

```
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} and save as <responseName>
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} params=<jsonParams> and save as <responseName>
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} host={<hostAddress>} params=<jsonParams> and save as <responseName>
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} host={<hostAddress>} params=<jsonParams> tls={true} and save as <responseName>
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} host={<hostAddress>} headers={"<h1>":"<val1>", "<h2>":"<val2>"} params=<jsonParams> and save as <responseName>
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} auth=Basic{"user":"<userName>", "pass":"<thePass>"} and save as <responseName>
SOAP url={"<theURL>"} template={"<xmlBodyTemplate>"} auth=Basic{"user":"<userName>", "pass":"<thePass>"} params=<jsonParams> and save as <responseName>
```

**Examples:**

```
SOAP url={"http://frida.example.com"} template={"ReqFromSOAP.txt"} params={"SomeParam":"XYUSZ"} tls={true} and save as WSResponse
SOAP url={"https://sub.domain.abc/XISOAPAdapter/MessageServlet?channel=:CHAT_INNOVATION_DEV"} template={"c:\\Users\\gilberto.isida\\Downloads\\wsTemplate.txt"} auth=Basic{"user":"Usr123", "pass":"MyPa$$"} and save as res
SOAP url={"https://sub.domain.abc/Service"} template={"c:\\Users\\gilberto.isida\\Downloads\\wsTemplate.txt"} params={"question_Id":"Citi_01", "mail_phone":"gilberto.isida@softtek.com"} and save as res
```

*Added: 2019-Jun-27*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/SOAP.pdf)

---

### SplitIntoList

> Split a text into a list considering a separation character.

Split a text into a list with various texts according to a given character that separates. Use "variableName" syntax when using text comming from an other variable to be split. 
Use "consider consecutive" syntax, to divide the list and include empty strings when the delimiter character is repeated in the string.

**Parameters:**
- `text`
- `delimiterCharacter`
- `variableName`
- `listVariableName`

**Syntax:**

```
SplitIntoList the value "<text>" every "<delimiterCharacter>" character and save as a list "<listVariableName>"
SplitIntoList the value "<text>" every "<delimiterCharacter>" character consider consecutive and save as a list "<listVariableName>"
SplitIntoList the variable "<variableName>" every "<delimiterCharacter>" character and save as a list "<listVariableName>"
SplitIntoList the variable "<variableName>" every "<delimiterCharacter>" character consider consecutive and save as a list "<listVariableName>"
```

**Examples:**

```
SplitIntoList the value "This$is$an$example" every "$" character and save as a list "MyList"
SplitIntoList the variable "Data" every "," character consider consecutive and save as a list "MyList"
```

*Added: 2019-Nov-04*

---

### SSH

> Send a command or script by SSH to a host machine. If result variables are needed, make sure it prints something such as "myvariable : a value".

Send a command or script by SSH to a host machine.

**Parameters:**
- `commandFile`
- `host`
- `userName`
- `password`

**Syntax:**

```
SSH {<commandFile>} host={<host>} user={<userName>} pass={<password>}
```

**Examples:**

```
SSH {command.txt} host={40.114.13.15} user={DAFS2} pass={********}
```

*Added: 2020-Aug-05*

---

### StringCase

> Change a string casing and save it in a variable.

Change the string to either "Title Case", "PascalCase", "camelCase", "snake_case" or "kebab-case" and save it in a variable.

**Parameters:**
- `input`
- `inputVarName`
- `caseType`
- `outputVarName`

**Syntax:**

```
StringCase input variable={<inputVarName>} case={<caseType:title|snake|camel|pascal|kebab>} out={<outputVarName>}
StringCase input={<input>} case={<caseType:title|snake|camel|pascal|kebab>} out={<outputVarName>}
```

**Options:**

- `caseType`: `title`, `snake`, `camel`, `pascal`, `kebab`
- `caseType`: `title`, `snake`, `camel`, `pascal`, `kebab`

**Examples:**

```
StringCase input variable={mes} case={title} out={TitleMes}
StringCase input={"<<<FileName>>><<<Month>>>.txt"} case={snake} out={FileName}
```

*Added: 2021-Sep-10*

---

### StringToList

> Parses a string variable and saves it as a List.

Parses a string variable and saves it as a List, so it can be used within a foreach loop. The source variable must be a JSON encoded array. In this example json is a string like this "[1,2,3,4]".

**Parameters:**
- `varname`
- `listName`

**Syntax:**

```
StringToList <varName> and save as <listName>
```

**Examples:**

```
StringToList json and save as lista
```

*Added: 2019-Feb-28*

---

### Substring

> Extract part of the content of a string.

Extracts part of the content of a string, given the input and the startIndex. Optionally, you can ask for a length. Given the string "Hello world!", a substring starting in 4 will return "o world!"; and a substring with length 4 will return "o wor".

**Parameters:**
- `inputString`
- `startIndex`
- `stringLength`
- `newVarName`

**Syntax:**

```
Substring "<inputString>" start <startIndex> and save as "<newVarName>"
Substring "<inputString>" start <startIndex> length <stringLength> and save as "<newVarName>"
```

**Examples:**

```
Substring "Hello world!" start 0 and save as "subString"
Substring "Hello world" start 3 length 5 and save as "newString"
```

*Added: 2019-Dec-09*

---

### SWITCH

Control statement that executes a set of logic reader instructions based on the result of a variable or statment define in the switch block

**Parameters:**
- `expression`
- `value`

**Syntax:**

```
switch (<expression>) {
case "<value>" :
##Code goes here...
end
}
switch (<expression>) {
case "<value>" :
##Code goes here...
end
default :
##Code goes here...
end
}
```

**Examples:**

```
switch (<<<docName>>>-<<entity>>) {
case "payments-RH" :
##Code goes here...
```

*Added: 2021-Oct-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/Switch.pdf)

---

### SystemNotify

> Generate a Windows pop-up notification.

Generates a Windows pop-up notification. The notifications can be of two types: Validation and Notification. "Validation" means that a user must either accept or cancel the process that is running. "Notification" means that the pop-up will only be informative and the process will continue its execution after the pop-up is closed. Warning, do not use when using browpet instructions.

**Parameters:**
- `Message`

**Syntax:**

```
SystemNotify Type "Notification" with message "<Message>"
SystemNotify Type "Validation" with message "<Message>"
```

**Examples:**

```
SystemNotify Type "Notification" with message "Test Message"
SystemNotify Type "Validation" with message "Test Message"
```

*Added: 2019-Feb-26*

---

### TemplateFrom

> Read preferably an html mail body template and save it as a variable. 

Reads preferably an html mail body template and stores it in theVariablesHelper.vars dictionary with the name defined in TempVar. File must exist in the Path given. Inside the template, var dictionary names can be set, these will be replaced using the CreateMailFrom statement.

**Parameters:**
- `Path`
- `TemplateFile`
- `TempVar`

**Syntax:**

```
TemplateFrom "<Path>" TemplateName "<TemplateFile>" As <TempVar>
```

**Examples:**

```
TemplateFrom "C:\Users\MailTemplates\" TemplateName "InviteTemplate.html" As plantilla
```

*Added: 2018-Jun-27*

---

### Transpose2DList

> Transpose a 2Dlist.

Transpose a 2D list, meaning that rows will be columns and columns will be rows. Index is 0-based. 

**Parameters:**
- `list2DName`
- `newListVariable`

**Syntax:**

```
Transpose2DList {<list2DName>} and save as {<newListVariable>}
```

**Examples:**

```
Transpose2DList {titles} and save as {titlesEnumeration}
```

*Added: 2023-Jul-11*

---

### Trim

> Remove the leading and trailing blank spaces of a string variable.

Removes the leading and trailing blank spaces of a string variable. You must pass the name of the desired variable (not the value). If no newVarName is given, the result of the trimming will replace the original value for the variable.

**Parameters:**
- `yourVarName`
- `newVarName`

**Syntax:**

```
Trim <yourVarName>
Trim <yourVarName> and save as <newVarName>
```

**Examples:**

```
Trim prodCode
Trim prodCode and save as trimmedCode
```

*Added: 2019-Dec-06*

---

### TrimChar

> Remove a character from a string variable.

Removes a character or characters that contain a string variable, at the beginning, at the end, or both sides. You must pass the name of the desired variable (not the value). If newVarName is not given, the result of the cropping will replace the original value of the variable.

**Parameters:**
- `type`
- `searchchar`
- `varinput`
- `varoutput`

**Syntax:**

```
TrimChar mode={<type: start|end|both>} chars=[<searchchar>] input={<varinput>} output={<varoutput>}
```

**Options:**

- `type`: ` start`, `end`, `both`

**Examples:**

```
TrimChar mode={start} chars=["0"] input={miVarInput} output={miVarOutput}
TrimChar mode={end} chars=["0","-"] input={miVarInput} output={miVarOutput}
TrimChar mode={both} chars=["*","#","'","0","1"," ","-","\n","\t"] input={miVarInput} output={miVarOutput}
```

*Added: 2021-Sep-29*

---

### TrimLast

> Delete the last n characters from a string and save it as a given variable.

Delete the last n characters from a string and save it as a given variable.

**Parameters:**
- `Number`
- `Text`
- `VariableName`

**Syntax:**

```
TrimLast "<Number>" characters from the value "<Text>" and save as "<VariableName>"
```

**Examples:**

```
TrimLast "4" characters from the value "<<<myLongWord>>>" and save as "myShorterWord"
```

*Added: 2019-Nov-15*

---

### TrimList

> Remove the leading and trailing blank spaces of every string item of a list.

Removes the leading and trailing blank spaces of all the items of either a 1D or 2D list. If no newVarName is given, the result of the trimming will replace the original value for the variable.

**Parameters:**
- `yourVarName`
- `newVarName`

**Syntax:**

```
TrimList <yourVarName>
TrimList <yourVarName> and save as <newVarName>
```

**Examples:**

```
TrimList prodCode
TrimList prodCode and save as trimmedCode
```

*Added: 2021-Jan-26*

---

### TRY-CATCH

Control statement that allows error and exception handling.

**Parameters:**
- `none`

**Syntax:**

```
try
##Code goes here
catch
##Code goes here
end
```

**Examples:**

```
try
Web Click in "Login"
catch
```

*Added: 2018-Mar-23*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Mixed/Articles/Try-Catch.pdf)

---

### UpdateTemplate

> Update de CustomLocal template in the cloud.

If the file exists in the path it will be uploaded to Azure to the process CustomLocal folder updating the file template. The file Located at the process CustomLocal folder will be versioned by FRIDA, being downloaded every time the file changes an is uploaded.

**Parameters:**
- `FilePath`

**Syntax:**

```
UpdateTemplate "<FilePath>"
```

**Examples:**

```
UpdateTemplate "C:\Users\andres.cruz\Desktop\file.txt"
UpdateTemplate "C:\Users\andres.cruz\Desktop\file.xlsx"
```

*Added: 2020-Aug-21*

---

### Uppercase

> Make a string uppercase and save it in a variable.

Make a string uppercase and save it in a variable.

**Parameters:**
- `aString`
- `newVarName`

**Syntax:**

```
Uppercase "<aString>" and save as "<newVarName>"
```

**Examples:**

```
Uppercase "someString, whatever you need" and save as "upper"
```

*Added: 2019-Dec-09*

---

### UseVBAlpha

> Run a VBS Script. 

Run a VBS Script. The script does not use Turing variables.

**Parameters:**
- `Script`

**Syntax:**

```
UseVBAlpha <Script>.vbs
```

**Examples:**

```
UseVBAlpha innerprocess.vbs
```

*Added: 2020-Nov-10*

---

### WHILE

Loops a code fragment for an undefined amount of times allowing to be executed repeatedly based on a given Boolean condition. Uses the logical operators <, >, >=, <=, ==, !=

**Parameters:**
- `booleanExpression`

**Syntax:**

```
while (<booleanExpression>) {
##code goes here
}
```

**Examples:**

```
while (a < b)
while (a >= b)
while (a == b)
```

*Added: 2019-Nov-07*

---

### WriteAllLines

> Writes all the lines in a list variable to a file.

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

> Writes all the text from a variable to a file.

Writes all the text contained in a variable to a file. It creates the file if it does not exist yet.

**Parameters:**
- `varName`
- `savePath`

**Syntax:**

```
WriteAllText var="<varName>" path="<savePath>"
WriteAllText var="<varName>" path="<savePath>" -isJSON
WriteAllText from the variable "<varName>" in the file "<savePath>"
WriteAllText from the variable "<varName>" in the file "<savePath>" -isJSON
```

**Examples:**

```
WriteAllText var="username" path="C:\Users\gilberto.isida\Downloads\file.txt"
WriteAllText from the variable "UserNames" in the file "C:\Users\andres.cruz\Downloads\Users.txt"
WriteAllText from the variable "IsonUserNames" in the file "C:\Users\andres.cruz\Downloads\Users.txt" -isJSON
```

*Added: 2020-Apr-21*

---

### XMLQuery

> Extract the value of a XML variable in the dictionary and saves it in another one as a Json.

Extracts the value of a XML variable in the dictionary and saves it in another one as a Json with the list portion of the xml. Use the instruction SetLogLevel Debug to inspect errors thrown. 

**Parameters:**
- `varname`
- `XPath`
- `newVarName`

**Syntax:**

```
XMLQuery "<varname>" where "<XPath>" and save as "<newVarName>"
```

**Examples:**

```
XMLQuery "txtxml" where "/default:AttachedDocument/cac:SenderParty/cac:PartyTaxScheme/cac:Lista" and save as "listaVariables"
```

*Added: 2021-Apr-13*

---
