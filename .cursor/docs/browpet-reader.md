# Browpet Reader

**Keyword:** `Web2`

**Functions:** 38

## Description

Browpet is designed to automate your web flows adding a resiliency layer that will help you reduce the amount of time you invest in giving support to your a robotic programing automations (RPA). With this tool you will be capable of recording your business web process and with its multi-browser functionality be confident that your web flows will run correctly in any of them. At the same time uses its headless execution mode and let FRIDA do the work without the need of your supervision.

## Quick Reference

| Function | Description |
|----------|-------------|
| [AskDownload](#askdownload) | Change the browser setting, to show (or not) a save file dialog for every fil... |
| [Authenticate](#authenticate) | Does HTTP Basic Authentication. This function can be used with "SetProxyServe... |
| [Back](#back) | Lets you go to the last page you visited. Just like when you click the back b... |
| [Click](#click) | Clicks in an element inside the browser. You can set a timeout to make more t... |
| [ClickDownload](#clickdownload) | Similar to Click, with the addition that this new function expects a new file... |
| [CloseTab](#closetab) | Closes current tab... |
| [Dispose](#dispose) | Close the current browser, cleanup the Web2 environment, ready for a clean st... |
| [DownloadEmbedded](#downloadembedded) | Given the id, xpath or selector of an <embed /> element in the HTML of a load... |
| [ElementExists](#elementexists) | Validates that a certain element is present in the webpage. Returns true if t... |
| [EndContext](#endcontext) | Destroys context... |
| [Evaluate](#evaluate) | This function allows to 'inject' JavaScript to the active page. By default th... |
| [Extract](#extract) | Extracts "textContent" from a html element and saves it to the specified vari... |
| [Focus](#focus) | Focus an html node.... |
| [GoTo](#goto) | Navigates to a specified URL.... |
| [HTMLRevision](#htmlrevision) | Saves a copy of the website's HTML in a private FRIDA Repository. This will t... |
| [In Context](#in context) | Creates a context around the given element. This will help search an item bas... |
| [InsertValue](#insertvalue) | Clears an input and writes into it. Mimics CTRL + A + BACKSPACE -> Write. If ... |
| [Key](#key) | Presses a keyboard key. List of available keys is found here: https://github.... |
| [LoadExtension](#loadextension) | Load a extension to the browser, given a local path.... |
| [Login](#login) | This is a Browpet feature that may help you to log into some basic websites, ... |
| [Navigation](#navigation) | Waits for page to load. Use this only when an action triggers a URL change.... |
| [NewTab](#newtab) | Opens a new tab... |
| [NextAlert](#nextalert) | If you know that an alert is coming, you need to establish how you are going ... |
| [Recaptcha](#recaptcha) | Solves Google's Recaptcha. It is necessary to get the "data-sitekey" property... |
| [Reload](#reload) | Reloads the current window... |
| [RightClick](#rightclick) | Same as Click, but with button: 'right'.... |
| [Screenshot](#screenshot) | Takes a Screenshot of the entire screen if an element is not specified. Other... |
| [Select](#select) | Selects an option in a select element, either by value or by the text contain... |
| [SelectMultiple](#selectmultiple) | Selects multiple options in a select element either by value or by the text c... |
| [SetDownloadsPath](#setdownloadspath) | Change the browser's default directory for downloaded items. The given path m... |
| [SetPermission](#setpermission) | Allows the browser to perform extra-actions that require the user's authoriza... |
| [SetProxyServer](#setproxyserver) | Connect to a proxy server, given the IP address and port. This instructions m... |
| [Sleep](#sleep) | Pauses execution the indicated amount in milliseconds.... |
| [SwitchPage](#switchpage) | Switches execution context to a new tab or pop up window. You can only change... |
| [Type](#type) | Writes inside an input tag. If no attribute is specified, then browpet will u... |
| [UploadFile](#uploadfile) | Uploads a single or multiple local files into an input tag with "type=file". ... |
| [UserAgent](#useragent) | This function allows you to change the Useragent of your page to emulate mult... |
| [Viewport](#viewport) | This function allows you to change the size of the viewport of your browser a... |

---

## Functions

### AskDownload

Change the browser setting, to show (or not) a save file dialog for every file being downloaded. The default value is false. This behaviour must be set BEFORE launching the browser.

**Parameters:**
- `value`

**Syntax:**

```
AskDownload <value>
```

**Examples:**

```
AskDownload true
AskDownload false
```

---

### Authenticate

Does HTTP Basic Authentication. This function can be used with "SetProxyServer".

**Syntax:**

```
Authenticate user = "<user>" pass = "<password>"
```

**Examples:**

```
Authenticate user = "frida" pass = "*******"
```

---

### Back

Lets you go to the last page you visited. Just like when you click the back button on your browser

**Syntax:**

```
Back
```

**Examples:**

```
Back
```

---

### Click

Clicks in an element inside the browser. You can set a timeout to make more tries of clicking. A full failed search takes about 20000ms. If no attribute is specified, then browpet will use a 'magic' algorithm to search for the appropriate element in the DOM.

**Parameters:**
- `attribute`
- `value`
- `time`

**Syntax:**

```
Click in "<value>"
Click in <attribute>="<value>"
Click in <attribute>="<value>" timeout = <time>
```

**Examples:**

```
Click in selector=".class1 > nth-child(2)"
Click in id="js-link-box-es" timeout = 35000
```

---

### ClickDownload

Similar to Click, with the addition that this new function expects a new file to be downloaded. It will check if there are any pending downloads (files with the .crdownload extension), and wait until done or the timeout is reached. Then the function will save the full file path to a new variable named: 'downloaded_file';

**Parameters:**
- `attribute`
- `value`
- `time`

**Syntax:**

```
ClickDownload in "<value>"
ClickDownload in <attribute>="<value>"
ClickDownload in <attribute>="<value>" timeout = <time>
```

**Examples:**

```
ClickDownload in selector=".class1 > nth-child(2)"
ClickDownload in id="js-link-box-es" timeout = 35000
```

---

### CloseTab

Closes current tab

**Syntax:**

```
CloseTab
```

**Examples:**

```
CloseTab
```

---

### Dispose

Close the current browser, cleanup the Web2 environment, ready for a clean start if required

**Syntax:**

```
Dispose
```

**Examples:**

```
Dispose
```

---

### DownloadEmbedded

Given the id, xpath or selector of an <embed /> element in the HTML of a loaded page, browpet will download the document following the src attr of the embed tag.

**Parameters:**
- `attribute`
- `value`

**Syntax:**

```
DownloadEmbedded <attribute>="<value>"
```

**Examples:**

```
DownloadEmbedded selector=\"#app > div > div > div.parent > div.page-content > div > section > div > div > embed\"
DownloadEmbedded id="#doc"
```

---

### ElementExists

Validates that a certain element is present in the webpage. Returns true if the element exists, and false otherwise. A full failed search takes about 20000ms. You can set a timeout before returning false.

**Parameters:**
- `attr`
- `value`
- `attribute`
- `new`
- `var`
- `time`

**Syntax:**

```
ElementExists in <attribute>="<attr-value>" save as "<new-var>"
ElementExists in <attribute>="<attr-value>" save as "<new-var>" timeout = <time>
```

**Examples:**

```
ElementExists in id="error" save as "exists"
ElementExists in id="error" save as "exists" timeout = 3000
```

---

### EndContext

Destroys context

**Syntax:**

```
EndContext
```

**Examples:**

```
EndContext
```

---

### Evaluate

This function allows to 'inject' JavaScript to the active page. By default the output is stored in a variable named web2Output

**Parameters:**
- `JScode`

**Syntax:**

```
Evaluate frame = "<wantedFrame>" `<JScode>`
```

**Examples:**

```
Evaluate frame = "0" `console.log("Helloooo")`
Evaluate frame = "main" `writeAlpha("P")`
Evaluate frame = "1" `your JS code`
```

---

### Extract

Extracts "textContent" from a html element and saves it to the specified variable name.

**Parameters:**
- `attribute`
- `attr`
- `value`
- `var`
- `name`

**Syntax:**

```
Extract from <attribute>="<attr-value>" save as "<var-name>"
```

**Examples:**

```
Extract from id="firstTitle" save as "title"
```

---

### Focus

Focus an html node.

**Parameters:**
- `attr`
- `value`
- `attribute`

**Syntax:**

```
Focus <attribute>="<attr-value>"
```

**Examples:**

```
Focus name="brand-list"
```

---

### GoTo

Navigates to a specified URL.

**Parameters:**
- `url`

**Syntax:**

```
GoTo "<url>"
GoTo <url>
```

**Examples:**

```
GoTo "https://www.google.com"
```

---

### HTMLRevision

Saves a copy of the website's HTML in a private FRIDA Repository. This will trigger an analysis to notify you if the HTML content of the website has changed. (Needs extra setup. Contact FRIDA Support). You may save different pages, only saving them with a different file name.

**Syntax:**

```
HTMLREVISION save as "<filename>"
```

**Examples:**

```
HTMLREVISION save as "index.html"
```

---

### In Context

Creates a context around the given element. This will help search an item based on a sibling item. For example, you want to press a button in the same row as another element, say a <span> element. You give the span as the context to llok for the sibling button.
The instructions following the context will make a recursive search, based on the given context. The algorithm will start looking for the parent elements in order to find an element inside a context, so you don't need to specify the full selector for the item you want to interact. In the last example, we want to click a button, so we will just look for a button inside the context like this: `selector="button"`

**Parameters:**
- `attr`
- `value`
- `attribute`

**Syntax:**

```
In Context of <attribute>="<attr-value>"
```

**Examples:**

```
In Context of dynamic="Número de Documento"
Type "123" in selector="input"
EndContext
```

---

### InsertValue

Clears an input and writes into it. Mimics CTRL + A + BACKSPACE -> Write. If no attribute is specified, then browpet will use a 'magic' algorithm to search for the appropriate element in the DOM.

**Parameters:**
- `text`
- `attribute`
- `attr`
- `value`
- `fieldl`

**Syntax:**

```
InsertValue "<text>" in "<field>"
InsertValue "<text>" in <attribute>="<attr-value>"
```

**Examples:**

```
InsertValue "20/01/19" in name="fechaInicio"
```

---

### Key

Presses a keyboard key. List of available keys is found here: https://github.com/FridaSupport/TuringSupportSSH/blob/master/Docs/Browpet/USKeyboardLayout.ts  or https://devdocs.io/puppeteer/index#class-keyboard

**Parameters:**
- `key`

**Syntax:**

```
Key "<key>"
```

**Examples:**

```
Key "Enter"
Key "Tab"
```

---

### LoadExtension

Load a extension to the browser, given a local path.

**Parameters:**
- `pathToExtension`

**Syntax:**

```
LoadExtension extensionsPath={<pathToExtension>}
```

**Examples:**

```
LoadExtension extensionsPath={C:\Users\fridaRPA\Desktop\Extension\aodjmnfhjibkcdimpodiifdjnnncaaf\1.12_0}
```

---

### Login

This is a Browpet feature that may help you to log into some basic websites, it intelligently looks for the username and password fields, enters the credentials and clicks on the button to sign in. It's been tested with Microsoft 365, and some other user/password websites. There are obvious limitations for more complex log-in forms like captchas, two-factor authentication, account verification, or intermediate buttons.

**Parameters:**
- `username`
- `password`

**Syntax:**

```
Login in <url> user = "<username>" pass = "<password>"
```

**Examples:**

```
Login in https://outlook.office.com user = "user.name@somedomain.com" PASS = "**********"
```

---

### Navigation

Waits for page to load. Use this only when an action triggers a URL change.

**Syntax:**

```
Navigation
```

**Examples:**

```
Navigation
```

---

### NewTab

Opens a new tab

**Syntax:**

```
NewTab
```

**Examples:**

```
NewTab
```

---

### NextAlert

If you know that an alert is coming, you need to establish how you are going to handle the alert. By default, the alert will be dismissed (closed), but, you can change this behaviour with this instructions. The available behaviours are the following: "accept", "cancel", "dismiss", "confirm". ***This must be configured before the alert is triggered***

**Parameters:**
- `behaviour`

**Syntax:**

```
NextAlert "<behaviour>"
```

**Examples:**

```
NextAlert "cancel"
NextAlert "confirm"
```

---

### Recaptcha

Solves Google's Recaptcha. It is necessary to get the "data-sitekey" property for the specific page. Also, the url where the captcha is hosted is necessary.

**Parameters:**
- `data`
- `sitekey`
- `url`

**Syntax:**

```
Recaptcha
Recaptcha sitekey="<data-sitekey>" url="<url>"
```

**Examples:**

```
Recaptcha sitekey="6Lf3iSgTAAAAAFSSa4Ow3_1cKPA7LsUSI24tTtSE" url="https://www.correoargentino.com.ar/formularios/oidn"
```

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Browpet/Articles/Recaptcha.pdf)

---

### Reload

Reloads the current window

**Syntax:**

```
Reload
```

**Examples:**

```
Reload
```

---

### RightClick

Same as Click, but with button: 'right'.

**Parameters:**
- `attribute`
- `value`
- `time`

**Syntax:**

```
RightClick in <attribute>="<value>"
RightClick in <attribute>="<value>" timeout = <time>
```

**Examples:**

```
RightClick in selector=".class1 > nth-child(2)"
RightClick in id="js-link-box-es" timeout = 35000
```

---

### Screenshot

Takes a Screenshot of the entire screen if an element is not specified. Otherwise, takes screenshot only of the specified element. Saves the path of where the screenshot is saved into a variable.

**Parameters:**
- `attribute`
- `attr`
- `value`
- `var`
- `name`

**Syntax:**

```
Screenshot save as "<var-name>"
Screenshot in <attribute>="<attr-value>" save as "<var-name>"
Screenshot save as "<var-name>" path = "<someLocalPath>"
Screenshot in <attribute>="<attr-value>" save as "<var-name>" path = "<someLocalPath>"
```

**Examples:**

```
Screenshot in id="katpchaImage" save as "captcha"
Screenshot save as "result"
Screenshot in id="textarea" save as "captcha" path = "C:/Users/gilberto.isida/Downloads/"
```

---

### Select

Selects an option in a select element, either by value or by the text contained in the options. If no attribute is specified, then browpet will use a 'magic' algorithm to search for the appropriate element in the DOM.

**Parameters:**
- `value`
- `attr`
- `value`
- `option`
- `text`
- `attribute`
- `option`
- `field`

**Syntax:**

```
Select value="<option>" in "<field>"
Select value="<value>" in <attribute>="<attr-value>"
Select "<option-text>" in <attribute>="<attr-value>"
```

**Examples:**

```
Select "Ford" in name="brand-list"
Select value="1" in id="access"
```

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Browpet/Articles/Select.pdf)

---

### SelectMultiple

Selects multiple options in a select element either by value or by the text contained in the options. Options must be ; separated. i.e.: "cars;bikes;trucks".

**Parameters:**
- `values`
- `attr`
- `value`
- `option`
- `texts`
- `attribute`

**Syntax:**

```
SelectMultiple value="<values>" in <attribute>="<attr-value>"
SelectMultiple "<option-texts>" in <attribute>="<attr-value>"
```

**Examples:**

```
SelectMultiple "Ford;Chevrolet;Fiat" in name="brand-list"
SelectMultiple value="1;2;3;4" in id="access"
```

---

### SetDownloadsPath

Change the browser's default directory for downloaded items. The given path must already exist. This behaviour must be set BEFORE launching the browser.

**Parameters:**
- `path`

**Syntax:**

```
SetDownloadsPath <path>
```

**Examples:**

```
SetDownloadsPath C:\Users\gilberto.isida\Documents\FRIDA\DEMOS
```

---

### SetPermission

Allows the browser to perform extra-actions that require the user's authorization. For now, only ['Page.setDownloadBehavior'], but support may be added later for things like PushNotifications.

**Parameters:**
- `permission`

**Syntax:**

```
SetPermission "<permission>"
```

**Examples:**

```
SetPermission "Page.setDownloadBehavior"
```

---

### SetProxyServer

Connect to a proxy server, given the IP address and port. This instructions must be called prior initializing Browpet.

**Parameters:**
- `ipAddress`

**Syntax:**

```
SetProxyServer IP={<ipAddress>}
```

**Examples:**

```
SetProxyServer IP={145.239.85.58:9300}
```

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Browpet/Articles/FRIDA_Proxies.pdf)

---

### Sleep

Pauses execution the indicated amount in milliseconds.

**Syntax:**

```
Sleep <time>
```

**Examples:**

```
Sleep 3000         # waits for 3 seconds
Params: time
```

---

### SwitchPage

Switches execution context to a new tab or pop up window. You can only change to the last opened tab or pop up, or to the main tab.

**Syntax:**

```
SwitchPage Last
SwitchPage Main
```

**Examples:**

```
SwitchPage Main
SwitchPage Last
```

---

### Type

Writes inside an input tag. If no attribute is specified, then browpet will use a 'magic' algorithm to search for the appropriate element in the DOM.

**Parameters:**
- `text`
- `attribute`
- `value`

**Syntax:**

```
Type "<text>" in "<value>"
Type "<text>" in <attribute>="<value>"
```

**Examples:**

```
Type "john.doe" in dynamic="username"
```

---

### UploadFile

Uploads a single or multiple local files into an input tag with "type=file". A global path needs to be specified. e.g. "C:\\usr\\Desktop\\file.txt". If you want to use multiple files, just separate each path with a semicolon ';' and be sure that the input supports multiple file upload.

**Parameters:**
- `path`
- `attribute`
- `attr`
- `value`

**Syntax:**

```
UploadFile "<path>" in <attribute>="<attr-value>"
UploadFile "<path>;<path>;...<path>" in <attribute>="<attr-value>"
```

**Examples:**

```
UploadFile "C:/Users/carlos/Documents/softtek/test.txt" in name="archivo"
UploadFile "C:/Users/OscarLaureano/Documents/test.txt;C:/Users/OscarLaureano/Videos/test 2.mp4;C:/Users/OscarLaureano/Pictures/test 4.png" in name="archivo"
```

---

### UserAgent

This function allows you to change the Useragent of your page to emulate multiple devices and browsers. You can use a predefined UserAgent (chrome/firefox/ie11/ie9/edge/opera/safari) or any other custom useragent string. You can find multiple examples of useragent strings online for many devices and operative systems. Or you can create your own according to the standard defined on the RFC 7231 section 5.5.3 (https://tools.ietf.org/html/rfc7231#section-5.5.3). More info on User Agents: https://www.sistrix.es/preguntale-a-sistrix/que-es-user-agent/

**Parameters:**
- `useragent`

**Syntax:**

```
UserAgent "<useragent>"
```

**Examples:**

```
UserAgent "chrome"
UserAgent "firefox"
UserAgent "ie11"
```

---

### Viewport

This function allows you to change the size of the viewport of your browser and will resize the page. A lot of websites don't expect browsers to change size, so you should set the viewport before navigating to the page.

**Parameters:**
- `width`
- `height`

**Syntax:**

```
Viewport <width> <height>
```

**Examples:**

```
Viewport 1920 1080
Viewport 400 700
```

---
