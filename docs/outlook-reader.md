# Outlook Reader

**Keyword:** `Mail`

**Functions:** 16

## Description

With this tool you will have the ability to read your emails without the need to have Outlook installed directly on your computer, by connecting to the Microsoft Office 365 mail server, you can move your emails, generate new ones or even filter them for easy reading. Taking control of your mailbox directly from your automation.

## Quick Reference

| Function | Description |
|----------|-------------|
| [ChangeTo](#changeto) | Change a mail status to read. |
| [CheckForIncomingMails](#checkforincomingmails) | Check for incoming mail in a specific mail box. |
| [Connect](#connect) | Connect to outlook mail server. |
| [Decrypt_SMIME_Attachment](#decrypt_smime_attachment) | Decrypts a file attachment with an installed PFX certificate. |
| [DownloadMail](#downloadmail) | Downloads a mail as an .eml file. |
| [Forward](#forward) | Forward a mail. |
| [MoveMail](#movemail) | Moves a mail to an specific folder. |
| [MsgToHtml](#msgtohtml) | Converts .msg file to .html |
| [MsgToPDF](#msgtopdf) | Convert a .msg file to a .pdf file |
| [ReadAllMails](#readallmails) | Read parameters from various Outlook mails. |
| [ReadMail](#readmail) | Read the body or the attachment of an outlook mail. |
| [ReadMailNew](#readmailnew) | Read the selected mails by applying a filter. |
| [ReadMsgFile](#readmsgfile) | Read a mail item from a .msg file. |
| [Reply](#reply) | Reply a mail that fulfills a filter. |
| [ReplyEmptyToMsg](#replyemptytomsg) | Adds an empty reply to a message or thread |
| [SendMail](#sendmail) | Send an e-mail. |

---

## Functions

### ChangeTo

> Change a mail status to read.

Changes a mail status to read.

**Parameters:**
- `filter`

**Syntax:**

```
ChangeTo read with the subject "<filter>"
```

**Examples:**

```
ChangeTo read with the subject "Important"
```

*Added: 2019-Oct-04*

---

### CheckForIncomingMails

> Check for incoming mail in a specific mail box.

Allows to check for incoming mail in a specific mail box.

**Parameters:**
- `mail`
- `Filter`
- `WhereFilterIsApplied`
- `ScriptKey`

**Syntax:**

```
CheckForIncomingMails to "<mail>" and that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and run the script "<ScriptKey>"
```

**Examples:**

```
CheckForIncomingMails to "<mail>" and that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and run the script "<ScriptKey>"
```

*Added: 2019-Oct-09*

---

### Connect

> Connect to outlook mail server.

Connect to the mail the outlook mail server directly without the need to be open or configure in your computer. You can only be connected to one mail server in each script. The exchange web services versions available are [ Exchange2007_SP1 , Exchange2010 , Exchange2010_SP1 , Exchange2010_SP2 , Exchange2013 , Exchange2013_SP1]

**Parameters:**
- `Mail`
- `Password`
- `EWS`
- `Version`

**Syntax:**

```
Connect to mail service "<Mail>" with the password "<Password>"
Connect to mail service "<Mail>" with the password "<Password>" with server auto discoverer
Connect to mail service "<Mail>" with the password "<Password>" with the Exchange Web Services version "<EWS-Version:Exchange2007_SP1|Exchange2010|Exchange2010_SP1|Exchange2010_SP2|Exchange2013|Exchange2013_SP1>"
```

**Examples:**

```
Connect to mail service "example@softtek.com" with the password "ExamplePasword123"
Connect to mail service "example@softtek.com" with the password "ExamplePasword123" with server auto discoverer
Connect to mail service "example@softtek.com" with the password "ExamplePasword123" with the exchange web services version "Exchange2010_SP2"
```

*Added: 2019-Apr-03*

---

### Decrypt_SMIME_Attachment

> Decrypts a file attachment with an installed PFX certificate.

Given a path to a file that was previously attached to an email, we will decrypt it using an installed PFX certificate. This must already be in the CurrentUser certificate store.

**Parameters:**
- `encryptedFile`
- `destination`

**Syntax:**

```
Decrypt_SMIME_Attachment file={<encryptedFile>} output={<destination>}
```

**Examples:**

```
Decrypt_SMIME_Attachment file={C:/Users/gilberto.isida/Downloads/Mails/0/smime.p7m} output={C:/Users/gilberto.isida/Downloads/Mails/0/Decrypted/Movimientos.out}
```

*Added: 2021-Feb-01*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Outlook/Articles/Decrypt_SMIME_Attachment.pdf)

---

### DownloadMail

> Downloads a mail as an .eml file.

Downloads a mail as an .eml file to an specific path given its unique MailID. If the destination folder does not exist, it is created. 

The downloaded file name is by default the mail subject + the date time of reception unless a different name is specified.

**Parameters:**
- `MailID`
- `DownloadMailPath`
- `MailName`

**Syntax:**

```
DownloadMail with Mail ID "<MailID>" to the folder "<DownloadMailPath>"
DownloadMail with Mail ID "<MailID>" to the folder "<DownloadMailPath>" and save as "<MailName>"
```

**Examples:**

```
DownloadMail with Mail ID "AAMkAGVlNjE0ZmMxLWM4MTYtNGJh" to the folder "C:\Users\MyUser\Desktop\DownloadedMails\ProcessID"
DownloadMail with Mail ID "AAMkAGVlNjE0ZmMxLWM4MTYtNGJh" to the folder "C:\Users\MyUser\Desktop\DownloadedMails\ProcessID" and save as "ClientRequirementsMail"
```

*Added: 2021-Aug-31*

---

### Forward

> Forward a mail.

Allows to forward a single read or unread (any unless specified) mail that is the most recent, or has a specific subject or Mail ID. A custom subject, body, recipients, ccrecipients and attachment files can be included in the forwarded mail. 

If no folder is specified, the search is done in the main folder, but it can be done within a diferent folder or even various subfolders.

Use optional syntax 'with new subject' to specify a custom subject for the forwarded mail instead of the default one.

Use syntax ending "and finally move it to" to move the matching mail to a different folder (if the folder does not exist, it will be created).

To copy the CCRecipients of the original mail use the key word "CopyAll" which can be concatenated with additional mail addresses.

Use syntax ending "and remove attachments" to specify file names (with file extension) to remove from the original mail; use "All" to remove all the attachments.

**Parameters:**
- `ReadStatus`
- `FolderName`
- `SubFolderName`
- `Subject`
- `Body`
- `FilePath`
- `Mail`
- `DestinyFolderName`
- `MailID`
- `FileName`

**Syntax:**

```
Forward the most recent <ReadStatus:read|unread> mail in the folder "<FolderName>" subfolder "<SubFolderName>" with the subject "<Subject>" with new subject "<NewSubject>" with the body "<Body>" the attachments "<FilePath1,FilePath2,FilePath3,...,FilePathN>" to the recipients "<Mail1,Mail2,Mail3,...,MailN>" to the ccrecipients "<Mail1,Mail2,Mail3,...,MailN>" finally move it to "<DestinyFolderName>"
Forward the mail with ID "<MailID>" with new subject "<NewSubject>" with the body "<Body>" the attachments "<FilePath1,FilePath2,FilePath3,...,FilePathN>" to the recipients "<Mail1,Mail2,Mail3,...,MailN>" to the ccrecipients "<Mail1,Mail2,Mail3,...,MailN>" finally move it to "<DestinyFolderName>"
Forward the most recent <ReadStatus:read|unread> mail in the folder "<FolderName>" subfolder "<SubFolderName>" with the subject "<Subject>" with new subject "<NewSubject>" with the body "<Body>" the attachments "<FilePath1,FilePath2,FilePath3,...,FilePathN>" to the recipients "<Mail1,Mail2,Mail3,...,MailN>" to the ccrecipients "<Mail1,Mail2,Mail3,...,MailN>" finally move it to "<DestinyFolderName>" and remove attachments "<FileName1,FileName2,FileName3,...,FileNameN>"
Forward the mail with ID "<MailID>" with new subject "<NewSubject>" with the body "<Body>" the attachments "<FilePath1,FilePath2,FilePath3,...,FilePathN>" to the recipients "<Mail1,Mail2,Mail3,...,MailN>" to the ccrecipients "<Mail1,Mail2,Mail3,...,MailN>" finally move it to "<DestinyFolderName>" and remove attachments "<FileName1,FileName2,FileName3,...,FileNameN>"
```

**Options:**

- `ReadStatus`: `read`, `unread`
- `ReadStatus`: `read`, `unread`

**Examples:**

```
Forward the most recent mail
Forward the most recent mail with new subject "Automated Response"
Forward the most recent mail with subject "Important Mail" with the body "This is an automated mail."
```

*Added: 2023-Nov-13*

---

### MoveMail

> Moves a mail to an specific folder.

Moves a mail to an specific folder given its unique MailID. If the destination folder does not exist, it is created.

The downloaded file name is the mail subject + the date time it was received. 

**Parameters:**
- `MailID`
- `DestinyFolder`

**Syntax:**

```
MoveMail with Mail ID "<MailID>" to the folder "<DestinyFolder>"
```

**Examples:**

```
MoveMail with Mail ID "AAMkAGVlNjE0ZmMxLWM4MTYtNGJh" to the folder "ProcessedMails"
```

*Added: 2021-Jan-12*

---

### MsgToHtml

> Converts .msg file to .html

Converts .msg file to .html

**Parameters:**
- `msgFile`
- `outputFile`

**Syntax:**

```
MsgToHtml MsgPath = {<msgFile>} HtmlPath = {<outputFile>}
```

**Examples:**

```
MsgToHtml MsgPath = {C:\Users\frida\Documents\Automatic reply.msg} HtmlPath = {C:\Users\frida\Documents\Automatic reply_replied.html}
```

*Added: 2023-Jul-26*

---

### MsgToPDF

> Convert a .msg file to a .pdf file

Convert a msg file to a pdf file.

**Parameters:**
- `msgFile`
- `outputFile`

**Syntax:**

```
MsgToPDF = {<msgFile>} output pdf = {<outputFile>}
```

**Examples:**

```
MsgToPDF = {C:\Users\frida\Documents\mailTest.msg} output pdf = {C:\Users\frida\Documents\outputs\mailTest.pdf}
```

*Added: 2023-Jun-07*

---

### ReadAllMails

> Read parameters from various Outlook mails.

Reads the unique mail ID and body, subject, date, sender, recipients, ccrecipients, torecipients, flag, importance, or the attachment of various Outlook mails (without the need to have Outlook open) within a specified folder by applying a subject/sender/body/date/attachment filter. 

The output is a JSON List that contains the extracted parameters of all the mails found. 

Use subfolder syntax to specify one or more coma separated subfolder names to be searched within the main folder; use keyword 'AllSubfolders' for the search to be done in all the subfolders contained in the main folder; use sentence 'exclude root' to ignore matching mails from the main folder; mail status can be specified as Any/Read/Unread with optional Flagged/Unflagged. 

When specifying the attachment parameter to get, add sentence 'and attachments in' to the syntax to specify a directory in which the attachments will be downloaded; use syntax 'unsorted' for all the attachments to be downloaded in the specified folder, otherwise they will be sorted in separate folders per matching mail. 

The mails can be moved to another specified folder which is created in case it does not exist; the destination folder can be the same as the searching folder. 

Add sentence 'download results to' so that the matching mail items are downloaded as .eml files.

**Parameters:**
- `ParametersToGet`
- `FolderName`
- `SubfolderName`
- `FilterType`
- `WhereFilterIsApplied`
- `MailStatus`
- `VariableName`
- `AttachmentsDestinyFolder`
- `DownloadedMailsPath`
- `EmailDestinyFolder`

**Syntax:**

```
ReadAllMails and get parameters "<ParametersToGet>" from the folder "<FolderName>" that fulfills the filter "<FilterType>" in the "<WhereFilterIsApplied>" and save as "<VariableName>"
ReadAllMails and get parameters "<ParametersToGet>" from the folder "<FolderName>" that fulfills the filter "<FilterType>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" and finally move it to "<EmailDestinyFolder>"
ReadAllMails and get parameters "<ParametersToGet>,attachment" from the folder "<FolderName>" that fulfills the filter "<FilterType>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" and attachments in "<AttachmentsDestinyFolder>"
ReadAllMails and get parameters "<ParametersToGet>,attachment" from the folder "<FolderName>" that fulfills the filter "<FilterType>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" and attachments in "<AttachmentsDestinyFolder>" and finally move it to "<EmailDestinyFolder>"
ReadAllMails and get parameters "<ParametersToGet>" from the folder "<FolderName>" subfolder "<SubfolderName>" that fulfills the filter "<FilterType>" in the "<WhereFilterIsApplied>" status "<MailStatus:Read|Unread|Any|Read Flagged|Read Unflagged|Unread Flagged|Unread Unflagged|Any Flagged|Any Unflagged>" and save as "<VariableName>" and attachments in "<AttachmentsDestinyPath>" download results to "<DownloadedMailsPath>" and finally move it to "<EmailDestinyFolder>" exclude root
```

**Options:**

- `MailStatus`: `Read`, `Unread`, `Any`, `Read Flagged`, `Read Unflagged`, `Unread Flagged`, `Unread Unflagged`, `Any Flagged`, `Any Unflagged`

**Examples:**

```
ReadAllMails and get parameters "sender,body,date,subject,recipients,torecipients,ccrecipients" from the folder "Bandeja de entrada" that fulfills the filter "Process Request" in the "subject" and save as "Result"
ReadAllMails and get parameters "subject" from the folder "InputMailsFolder" that fulfills the filter "2021/01/12" in the "date" and save as "Result" and finally move it to "ProcessingFolder"
ReadAllMails and get parameters "subject,attachment" from the folder "InputMailsFolder" that fulfills the filter "2021/01/12 13:30" in the "date" and save as "Result" and attachments in "C:\Users\andres.cruz\Desktop\Mails"
```

*Added: 2021-Jan-07*

---

### ReadMail

> Read the body or the attachment of an outlook mail.

Reads the body or the attachment of an outlook mail directly from de mail server (witout the need to have outlook open) by applying a filter on de subject and saving its value on the dictionary vars (<<<...>>>) for future used. The third syntax option reads only from unread mail, marks it as read.

**Parameters:**
- `Filter`
- `VariableName`

**Syntax:**

```
ReadMail body from inbox that fullfill the filter "<Filter>" in the subject and save as "<VariableName>"
ReadMail attachment from inbox that fullfill the filter "<Filter>" in the subject and save as "<VariableName>"
ReadMail attachment from inbox that fullfill the filter "<Filter>" in the subject and save as unread "<VariableName>"
```

**Examples:**

```
ReadMail body from inbox that fullfill the filter "Important" in the subject and save as "VariableName"
ReadMail attachment from inbox that fullfill the filter "Important" in the subject and save as "VariableName"
ReadMail attachment from inbox that fullfill the filter "Important" in the subject and save as unread "VariableName"
```

*Added: 2019-Apr-03*

---

### ReadMailNew

> Read the selected mails by applying a filter.

Reads the selected mails by applying a filter or multifilter in Subject, Sender, Date or Body of emails in a specific Outlook's folder (without the need of having outlook open) and finally saves its value on the dictionary vars (<<<...>>>) for future use or saves the attachments in a destiny folder (All filters are case sensitive). 
If more than one parameter is required at the same time, those parameters will be added in the same variable separated by a comma, if they include attachments those are saved in a new folder inside the given folder with the same name as their corresponding position in the list that is created. 
Use the optional syntax ending 'download results to "<DownloadMailsPath>"' to download the matching mails as .eml files; if the path does not exist, it is created. The downloaded file names are the mail subject + the date time of reception.  
Mailbox syntax will only work on accounts with such permitions.
An error is generated if no matching mails are found.

**Parameters:**
- `ParameterToGet`
- `ParametersToGet`
- `FolderName`
- `Filter`
- `WhereFilter`
- `WhereFilterIsApplied`
- `MailboxName`
- `VariableName`
- `File`
- `varPath`
- `DestinyFolder`
- `DownloadMailsPath`

**Syntax:**

```
ReadMailNew and get "<ParameterToGet>" from the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" finally move it to "<DestinyFolder>" download results to "<DownloadMailsPath>"
ReadMailNew and get "<ParameterToGet>" in the mailbox "<MailboxName>" from the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" finally move it to "<DestinyFolder>" download results to "<DownloadMailsPath>"
ReadMailNew and get "<ParameterToGet>" from unread mails in the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" finally marked as read download results to "<DownloadMailsPath>"
ReadMailNew and get "<ParameterToGet>" from unread mails in the mailbox "<MailboxName>" in the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and save as "<VariableName>" finally marked as read download results to "<DownloadMailsPath>"
ReadMailNew and get "<ParameterToGet>" from unread mails in the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" and save as list "<VariableName>" finally marked as read download results to "<DownloadMailsPath>"
ReadMailNew and get "<ParameterToGet>" from the folder "<FolderName>" that fulfills the multifilter {<Filter1>,<WhereFilter1IsApplied>;<Filte2>,<WhereFilter2IsApplied>...;<FilterN>,<WhereFilterNIsApplied>} and save as "<VariableName>" finally move it to "<DestinyFolder>" download results to "<DownloadMailsPath>"
ReadMailNew and get "<ParameterToGet>" from unread mails in the folder "<FolderName>" that fulfills the multifilter {<Filter1>,<WhereFilter1IsApplied>;<Filte2>,<WhereFilter2IsApplied>...;<FilterN>,<WhereFilterNIsApplied>} and save as "<VariableName>" finally mark as read download results to "<DownloadMailsPath>"
ReadMailNew and get parameters "<ParametersToGet>" from the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" save data as "<VariableName>" and attachments in "<varPath>" finally move it to "<DestinyFolder>" download results to "<DownloadMailsPath>"
ReadMailNew and get parameters "<ParametersToGet>" from unread mails in the folder "<FolderName>" that fulfills the filter "<Filter>" in the "<WhereFilterIsApplied>" save data as "<VariableName>" and attachments in "<varPath>" finally mark as read download results to "<DownloadMailsPath>"
```

**Examples:**

```
ReadMailNew and get "body" from the folder "Bandeja de entrada" that fulfills the filter "Hola" in the "body" and save as "BodyVariable" finally move it to "Notas"
ReadMailNew and get "date" from the folder "Bandeja de entrada" that fulfills the filter "2019/09/10" in the "date" and save as "BodyVariable" finally move it to "Notas" download results to "C:\Users\Downloads\MailResults"
ReadMailNew and get "sender" from the folder "Bandeja de entrada" that fulfills the filter "Hola" in the "subject" and save as "BodyVariable" finally move it to "Notas"
```

*Added: 2019-Sep-11*

---

### ReadMsgFile

> Read a mail item from a .msg file.

Given a MSG file, we can extract the sender, date, recipients, subject, and body. Even the attachments, to relocate them somewhere in your system.

**Parameters:**
- `msgPath`
- `saveDir`

**Syntax:**

```
ReadMsgFile "<msgPath>" save_attachments={"<saveDir>"}
```

**Examples:**

```
ReadMsgFile "C:/Users/gilberto.isida/Downloads/ejemplo.msg" save_attachments={"C:/Users/gilberto.isida/Downloads/Attachments"}
```

*Added: 2021-Mar-15*

---

### Reply

> Reply a mail that fulfills a filter.

Allows to reply to mails that fulfills a filter.

**Parameters:**
- `Filter`
- `Body`
- `Folder`
- `MailID`
- `and`
- `Destiny`
- `folder`

**Syntax:**

```
Reply to most recent mail with subject "<Filter>" with the body "<Body>"
Reply to most recent unread mail with subject "<Filter>" with the body "<Body>"
Reply to most recent mail in the folder "<Folder>" with the body "<Body>" finally move it to "<DestinyFolder>"
Reply to most recent unread mail in the folder "<Folder>" with the body "<Body>" finally move it to "<DestinyFolder>"
Reply to the mail with ID "<MailID>" with the body "<Body>"
```

**Examples:**

```
Reply to most recent mail with subject "Important" with the body "Thanks"
Reply to most recent unread mail with subject "important" with the body "Thanks"
Reply to most recent mail in the folder "Inbox" with the body "Thanks" finally move it to "Processed"
```

*Added: 2019-Sep-27*

---

### ReplyEmptyToMsg

> Adds an empty reply to a message or thread

Adds an empty reply to a message or thread

**Parameters:**
- `msgFile`
- `outputFile`

**Syntax:**

```
ReplyEmptyToMsg MsgPath = {<msgFile>} Output = {<outputFile>}
```

**Examples:**

```
ReplyEmptyToMsg MsgPath = {C:\Users\frida\Documents\Automatic reply.msg} Output = {C:\Users\frida\Documents\Automatic reply_replied.msg}
```

*Added: 2023-Jul-26*

---

### SendMail

> Send an e-mail.

Allows to send mails using the desired account, mails may or may not contain attachments it also works with Cc and Bcc. For mails with several destinataries or attachments, split each element with a coma.
If the mail account has permitions, "mailbox" syntax will allow to send mails signed as the corresponding mailbox.

**Parameters:**
- `DestinyMail`
- `Subject`
- `Body`
- `FilePath`
- `DestinyGroup`
- `Mailbox`

**Syntax:**

```
SendMail to "<DestinyMail>" with the subject "<Subject>" and the body "<Body>"
SendMail to "<DestinyMail>" in mailbox "<Mailbox>" with the subject "<Subject>" and the body "<Body>"
SendMail to "<DestinyMail>" with the subject "<Subject>" the body "<Body>" and the attachments "<FilePath>"
SendMail to group "<DestinyGroup>" with the subject "<Subject>" and the body "<Body>"
SendMail to group "<DestinyGroup>" with the subject "<Subject>" the body "<Body>" and the attachments "<FilePath>"
SendMail to "<DestinyMail>" Bcc to "<DestinyMail>" the subject "<Subject>" and the body "<Body>"
SendMail to "<DestinyMail>" Bcc to "<DestinyMail>" the subject "<Subject>" the body "<Body>" and the attachments "<FilePath>"
SendMail to "<DestinyMail>" Cc to "<DestinyMail>" the subject "<Subject>" and the body "<Body>"
SendMail to "<DestinyMail>" Cc to "<DestinyMail>" the subject "<Subject>" the body "<Body>" and the attachments "<FilePath>"
SendMail to "<DestinyMail>" Cc to {<DestinyMail>} Bcc to {<DestinyMail>} the subject "<Subject>" and the body "<Body>"
SendMail to "<DestinyMail>" Cc to {<DestinyMail>} Bcc to {<DestinyMail>} the subject "<Subject>" the body "<Body>" and the attachments "<FilePath>"
```

**Examples:**

```
SendMail to "example@softtek.com" with the subject "The subject goes here" and the body "The message goes here"
SendMail to "example@softtek.com" with the subject "The subject goes here" the body "The message goes here" and the attachments "C:\Users\user\Desktop\NoteScripts\Coordinates.txt,C:\Users\user\Desktop\Issues.xlsx"
SendMail to "example@softtek.com,example2@softtek.com" with the subject "Subject goes here" the body "Message goes here" and the attachments "C:\Users\user\Pictures\image.png"
```

*Added: 2019-Sep-18*

---
