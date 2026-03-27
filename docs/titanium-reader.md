# Titanium Reader

**Keyword:** `Titanium`

**Functions:** 25

## Description

With Titanium you will have the ability to type text and to move the cursor interacting with the elements active on your screen. Incorporating functions that will let you take screenshots or detect events such as error messages, letting you take actions and automate all your process as well as its business rules. Titanium is so powerful that you will be able to create a robotic programing automation (RPA) without needing to see the source code of the project by applying computer vision algorithms, you only need to supply an image sample of the element you are searching for. Also you can try its OCR capabilities as see how fast you can start making your own RPA.

## Quick Reference

| Function | Description |
|----------|-------------|
| [CaptureImage](#captureimage) | Take a screenshot. |
| [ClickCoord](#clickcoord) | Click on the (x,y) coordinates. |
| [ClickImage](#clickimage) | Click on an image in the active screen. |
| [ClickOnText](#clickontext) | Click on a word or phrase. |
| [CropImage](#cropimage) | Crop an image using percentages of the screen. |
| [CropImageExact](#cropimageexact) | Crop an image using the exact pixel coordinates to crop the image. |
| [DragAndDrop](#draganddrop) | Click over an image and drag it to another image. |
| [FocusWindow](#focuswindow) | Focus an existing window |
| [GetActiveWindowId](#getactivewindowid) | Saves the process id of the active window |
| [GetLines](#getlines) | Extract text from an image (FRIDA CLOUD). |
| [GetLinesWithSubstring](#getlineswithsubstring) |  Search for phrases with OCR and save it in a list. |
| [ImageAppears](#imageappears) | Search for an image when it appears on the screen. |
| [ImageAppearsError](#imageappearserror) |  Expect for an image to not show, if it shows an error is generated. |
| [LineExists](#lineexists) | Search with OCR if a word or phrase exists. |
| [MoveMouse](#movemouse) | Move the mouse to the (x,y) coordinates. |
| [OCR_GetLines](#ocr_getlines) | Extract text from an image (local computer). |
| [ReadQRCode](#readqrcode) | Searches a QRCode in an image and gets its content. |
| [ResolutionFix](#resolutionfix) | Fix the resolution. |
| [ScreenSnipping](#screensnipping) | Crop an area contained in the space between two images. |
| [Scroll](#scroll) | Simulate a MouseWheel scroll. |
| [Sleep](#sleep) | Make a pause in the process. |
| [SolveCAPTCHA](#solvecaptcha) | Solve a captcha in an image. |
| [Type](#type) | Type a text as written with the keyboard. |
| [TypeBlock](#typeblock) | Text to be written using the Clipboard as an auxiliary. |
| [TypeVirtual](#typevirtual) | Text to be written with SimulateInput. |

---

## Functions

### CaptureImage

> Take a screenshot.

Takes a screenshot of the whole screen and saves it in the application location (App\screenshots\ImageCapture.png) unless other specified.

**Parameters:**
- `ImagePath`

**Syntax:**

```
CaptureImage
CaptureImage and save as <ImagePath>
```

**Examples:**

```
Titanium CaptureImage
Titanium CaptureImage and save as C:\Users\user\Pictures\Image.png
```

*Added: 2019-Feb-20*

---

### ClickCoord

> Click on the (x,y) coordinates.

Make one or more clicks on the desired coordinates (x,y). For a right click, use -1 as the number of clicks.

**Parameters:**
- `xCoord`
- `yCoord`
- `NumberClicks`

**Syntax:**

```
ClickCoord -x <xCoord> -y <yCoord> -clicks <NumberClicks>
```

**Examples:**

```
Titanium ClickCoord -x 414 -y 456 -clicks 1
Titanium ClickCoord -x 550 -y 550 -clicks -1
```

*Added: 2019-Feb-15*

---

### ClickImage

> Click on an image in the active screen.

Make one or more clicks on the image in the active screen. To make a right click send 4 as param in the NumberClicks variable. Also you can add similarity and click position as optional parameters. For click position you have this options (TOP_LEFT,TOP_CENTER,TOP_RIGHT,CENTER_LEFT,CENTER,CENTER_RIGHT,BOTTOM_LEFT,BOTTOM_CENTER,BOTTOM_RIGHT). Default similarity 0.7. Offset coordinates are relative to the click position and can be used to position the click based on where a known image is.

**Parameters:**
- `ImageName`
- `Time`
- `NumberClicks`
- `ClickPosition`
- `Similarity`
- `ClickButton`
- `OffsetCoordX`
- `OffsetCoordY`

**Syntax:**

```
ClickImage <ImageName> Timeout= <Time>
ClickImage <ImageName> Timeout= <Time> NumberClicks= <NumberClicks>
ClickImage <ImageName> Timeout= <Time> NumberClicks= <NumberClicks> Sim= <Similarity>
ClickImage <ImageName> Timeout= <Time> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT>
ClickImage <ImageName> Timeout= <Time> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT> OffsetX= <OffsetCoordX> OffsetY= <OffsetCoordY>
ClickImage <ImageName> Timeout= <Time> NumberClicks= <NumberClicks> ClickButton= <ClickButton>
```

**Options:**

- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`
- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`

**Examples:**

```
Titanium ClickImage test.PNG Timeout= 10000 NumberClicks= 1
Titanium ClickImage test.PNG Timeout= 10000 NumberClicks= 1 Sim= 0.9
Titanium ClickImage test.PNG Timeout= 10000 NumberClicks= 1 ClickPosition= CENTER_LEFT
```

*Added: 2018-May-11*

---

### ClickOnText

> Click on a word or phrase.

Using OCR, search on screen for a word or phrase, if it exists, a click (Use optional parameter NumberClicks to make more than 1. For a right click use -1) is given on it. By default, the click is made in the center of the text but optional parameter ClickPosition allows the use of predifined positions or a word/phrase contained in the SearchString; optional parameters XOffset and YOffset can be defined for position adjustments in pixels. If there are various matches of the SearchString, the optional parameter Index can be used to indicate the number of coincidence to be clicked; if the given Index is greater than the number of matches found, an error is thrown. By default, MatchCase is true, which means the letter casing matters when searching for matches. SpecialCharacters is set to false by default, which means language related characters such as á,é,í,ó,ú,ä,ë,ï,ü,ö will be interpreted as a,e,i,o,u from the SearchString as well from the OCR result. If Turing Titanium Debug Mode is on, an additional screenshot will be taken showing the detected text and the point clicked.

**Parameters:**
- `SearchString`
- `MatchCase`
- `NumberClicks`
- `ClickPosition`
- `XOffset`
- `YOffset`
- `Index`
- `SpecialCharacters`
- `WidthResolution`
- `HeightResolution`

**Syntax:**

```
ClickOnText "<SearchString>" MatchCase= <MatchCase:True|False> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT|"TextContainedInSearchString"> XOffset= <XOffset> YOffset= <YOffset> Index= <Index> SpecialCharacters= <SpecialCharacters:True|False> WidthResolution=<WidthResolution> HeightResolution=<HeightResolution>
ClickOnText "<SearchString>" MatchCase= <MatchCase:True|False> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT|"TextContainedInSearchString"> XOffset= <XOffset> YOffset= <YOffset> Index= <Index> SpecialCharacters= <SpecialCharacters:True|False>
ClickOnText "<SearchString>" MatchCase= <MatchCase:True|False> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT|"TextContainedInSearchString"> XOffset= <XOffset> YOffset= <YOffset> Index= <Index>
ClickOnText "<SearchString>" MatchCase= <MatchCase:True|False> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT|"TextContainedInSearchString"> XOffset= <XOffset> YOffset= <YOffset>
ClickOnText "<SearchString>" MatchCase= <MatchCase:True|False> NumberClicks= <NumberClicks> ClickPosition= <ClickPosition:TOP_LEFT|TOP_CENTER|TOP_RIGHT|CENTER_LEFT|CENTER|CENTER_RIGHT|BOTTOM_LEFT|BOTTOM_CENTER|BOTTOM_RIGHT|"TextContainedInSearchString">
ClickOnText "<SearchString>"
```

**Options:**

- `MatchCase`: `True`, `False`
- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`, `"TextContainedInSearchString"`
- `SpecialCharacters`: `True`, `False`
- `MatchCase`: `True`, `False`
- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`, `"TextContainedInSearchString"`
- `SpecialCharacters`: `True`, `False`
- `MatchCase`: `True`, `False`
- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`, `"TextContainedInSearchString"`
- `MatchCase`: `True`, `False`
- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`, `"TextContainedInSearchString"`
- `MatchCase`: `True`, `False`
- `ClickPosition`: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`, `"TextContainedInSearchString"`

**Examples:**

```
Titanium ClickOnText "PEREZ VAZQUEZ AIDA MARA"
Titanium ClickOnText "PEREZ VAZQUEZ AIDA MARA" MatchCase= False
Titanium ClickOnText "PEREZ VAZQUEZ AIDA MARA" MatchCase= False ClickPosition= TOP_RIGHT
```

*Added: 2021-Jul-28*

---

### CropImage

> Crop an image using percentages of the screen.

This Function is used to crop an image by inputting the cropping percentages desired and creating a copy of it in the "screenshots" Turing folder.

**Parameters:**
- `ImagePathToBeCropped`
- `Width`
- `Height`
- `CropImagePath`
- `TopPercentage`
- `BottomPercentage`
- `LeftPercentage`
- `RightPercentage`

**Syntax:**

```
CropImage <ImagePathToBeCropped> WidthPercentage= <Width> HeightPercentage= <Height> and save as <CropImagePath>
CropImage <ImagePathToBeCropped> Top= <TopPercentage> Bottom= <BottomPercentage> Left= <LeftPercentage> Right= <RightPercentage> and save as <CropImagePath>
```

**Examples:**

```
Titanium CropImage C:\Users\user\Pictures\Image.PNG WidthPercentage= 50 HeightPercentage= 50 and save as CropImagePath
Titanium CropImage C:\Users\user\Pictures\Image.PNG Top= 20 Bottom= 40 Left= 30 Right= 10 and save as CropImagePath
```

*Added: 2018-Dec-11*

---

### CropImageExact

> Crop an image using the exact pixel coordinates to crop the image.

This function crops an image, given the pixel coordinates (x,y) of the top-left and the bottom-right. Additionally, this function can also rotate the image if specified.

**Parameters:**
- `pathIn`
- `pathOut`
- `topPx`
- `leftPx`
- `bottomPx`
- `rightPx`
- `angle`

**Syntax:**

```
CropImageExact src={<pathIn>} out={<pathOut>} top={<topPx>} left={<leftPx>} bottom={<bottomPx>} right={<rightPx>}
CropImageExact src={<pathIn>} out={<pathOut>} top={<topPx>} left={<leftPx>} bottom={<bottomPx>} right={<rightPx>} angle={<angle:0|90|180|270>)}
```

**Options:**

- `angle`: `0`, `90`, `180`, `270`

**Examples:**

```
Titanium CropImageExact src={c:/Users/gilberto.isida/Downloads/image.png} out={c:/Users/gilberto.isida/Downloads/cropped.png} top={10} left={50} bottom={120} right={250}
Titanium CropImageExact src={c:/Users/gilberto.isida/Downloads/image.png} out={c:/Users/gilberto.isida/Downloads/cropped.png} top={10} left={50} bottom={120} right={250} angle={90}
```

*Added: 2021-Apr-19*

---

### DragAndDrop

> Click over an image and drag it to another image.

Click over the image <SelectImageName> and without releasing the button drag and drop it over the image <DropImageName>

**Parameters:**
- `SelectImageName`
- `DropImageName`
- `Time`
- `Sim`

**Syntax:**

```
DragAndDrop select <SelectImageName> and drop in <DropImageName> Timeout= <Time>
DragAndDrop select <SelectImageName> adn drop in <DropImageName> Timeout= <Time> Sim= <Sim>
```

**Examples:**

```
Titanium DragAndDrop select Image.PNG and drop in Image2.PNG Timeout= 20000
Titanium DragAndDrop select Image.PNG and drop in Image2.PNG Timeout= 20000 Sim= 0.7
```

*Added: 2019-Jul-04*

---

### FocusWindow

> Focus an existing window

Focus an existing window either by part of the title found in the window's header or by procId. The focus may be used to maximize or minimize the window, or just place it in the foreground. Use type with maximized, normal or minimized.

**Parameters:**
- `windowTitle`
- `windowProcessId`
- `windowType`

**Syntax:**

```
FocusWindow with title {<windowTitle>} type {<windowType>}
FocusWindow with id {<windowProcessId>} type {<windowType>}
```

**Examples:**

```
FocusWindow with title {Error Log} type {maximized}
FocusWindow with id {Turing Expo} type {minimized}
```

*Added: 2024-Jul-26*

---

### GetActiveWindowId

> Saves the process id of the active window

Saves the process id of the active window in the given variable. This may be used with FocusWindow to hide or show the window.

**Parameters:**
- `varName`

**Syntax:**

```
GetActiveWindowId and save in {<varName>}
```

**Examples:**

```
GetActiveWindowId and save in {turingId}
```

*Added: 2024-Jul-26*

---

### GetLines

> Extract text from an image (FRIDA CLOUD).

Method to extract with OCR the text presented in a .png or .jpg image. Images must be at least 50 pixels in width and height. Version=read option will use an improved OCR algorithm.

**Parameters:**
- `ImagePath`
- `ResultListName`

**Syntax:**

```
GetLines <ImagePath> and save as <ResultListName>
GetLines <ImagePath> and save as <ResultListName> version=read
```

**Examples:**

```
Titanium GetLines C:\Users\user\Pictures\TestImage.png and save as ListResultVar
Titanium GetLines C:\Users\user\Pictures\TestImage.png and save as ListResultVar version=read
```

*Added: 2019-Apr-17*

---

### GetLinesWithSubstring

>  Search for phrases with OCR and save it in a list.

 Method to know by OCR if a phrases exist on the active screen containing the words in <searchString>.It generate a list<string> in vars

**Parameters:**
- `searchString`
- `matchCase`
- `varName`
- `imagePath`

**Syntax:**

```
GetLinesWithSubstring "<searchString>" MatchCase= <matchCase> and save as <varName>
GetLinesWithSubstring from "<imagePath>" with "<searchString>" MatchCase= <matchCase> and save as <varName>
```

**Examples:**

```
GetLinesWithSubstring "Error Message" MatchCase= false and save as errorList
GetLinesWithSubstring from "C:\Users\innovation\Desktop\Document.png" with "Error" MatchCase= false and save as errorList
```

*Added: 2018-Jun-13*

---

### ImageAppears

> Search for an image when it appears on the screen.

Search for an specific period of time if an image is shown or can be found on the screen.

**Parameters:**
- `imageName`
- `time`
- `similarity`
- `varName`

**Syntax:**

```
ImageAppears <imageName> Timeout= <time>
ImageAppears <imageName> Timeout= <time> Sim= <similarity>
ImageAppears <imageName> Timeout= <time> Sim= <similarity> and save result as <varName>
ImageAppears <imageName> Timeout= <time> Sim= <similarity> and save result as "<varName>"
```

**Examples:**

```
Titanium ImageAppears Image.PNG Timeout= 30000
Titanium ImageAppears Image.PNG Timeout= 30000 Sim= 0.8
Titanium ImageAppears MenuOpen.PNG Timeout= 15000 Sim= 0.85 and save result as Success
```

*Added: 2018-Jun-13*

---

### ImageAppearsError

>  Expect for an image to not show, if it shows an error is generated.

 Search for a specific period of time if an image appear or can be found on the screen, it generated an error if the image is found.

**Parameters:**
- `ImageName`
- `Time`
- `Similarity`

**Syntax:**

```
ImageAppearsError <ImageName> Timeout= <Time>
ImageAppearsError <ImageName> Timeout= <Time> Sim= <Similarity>
```

**Examples:**

```
Titanium ImageAppearsError Image.PNG Timeout= 3000
Titanium ImageAppearsError Image.PNG Timeout= 3000 Sim= 0.9
```

*Added: 2018-Jun-13*

---

### LineExists

> Search with OCR if a word or phrase exists.

Method to know by OCR if a word or phrase exists on the active screen or in a specific image.

**Parameters:**
- `ImagePath`
- `SearchString`
- `MatchCase`

**Syntax:**

```
LineExists "<SearchString>" MatchCase= <MatchCase>
LineExists from "<ImagePath>" with "<searchString>" MatchCase= <MatchCase>
```

**Examples:**

```
Titanium LineExists "ThisWord" MatchCase= true
Titanium LineExists from "C:\Users\user\Desktop\Document.png" with "This Word" MatchCase= true
```

*Added: 2018-Jun-13*

---

### MoveMouse

> Move the mouse to the (x,y) coordinates.

Move the mouse to the desired coordinates (x,y).

**Parameters:**
- `xCoord`
- `yCoord`

**Syntax:**

```
MoveMouse -x <xCoord> -y <yCoord>
```

**Examples:**

```
MoveMouse -x 414 -y 456
```

*Added: 2019-Dec-10*

---

### OCR_GetLines

> Extract text from an image (local computer).

Method to extract with OCR the text presented in a .png or .jpg image. If no file parameter is given, we will capture a screenshot.

**Parameters:**
- `varName`
- `filePath`

**Syntax:**

```
OCR_GetLines and save as "<varName>"
OCR_GetLines and save as {<varName>}
OCR_GetLines file="<filePath>" and save as "<varName>"
OCR_GetLines file={<filePath>} and save as {<varName>}
```

**Examples:**

```
Titanium OCR_GetLines and save as {lines}
Titanium OCR_GetLines file={C:\Users\gilberto.isida\Pictures\OCReceipt.png} and save as {lines}
```

*Added: 2020-Nov-24*

---

### ReadQRCode

> Searches a QRCode in an image and gets its content.

This function will process an image and search for the location of a QRCode, then it will read it and get its content. An error will be thrown if no QRCode is detected.

**Parameters:**
- `imagePath`
- `varName`

**Syntax:**

```
ReadQRCode img={<imagePath>} result={<varName>}
```

**Examples:**

```
ReadQRCode img={C:\Users\gilberto.isida\Pictures\someQRcode.png} result={content}
```

*Added: 2021-May-10*

---

### ResolutionFix

> Fix the resolution.

Fix the resolution. Note: Generally avoid this function and use "Titanium Fixed Resolution" in the global Settings section.

**Parameters:**
- `SolutionKey`

**Syntax:**

```
ResolutionFix "<SolutionKey>"
```

**Examples:**

```
ResolutionFix "<SolutionKey>"
```

*Added: 2019-Sep-13*

---

### ScreenSnipping

> Crop an area contained in the space between two images.

Crop a certain area contained in the space between the two images. The first image defines the top left corner and the second image defines the bottom right corner. If the image is found it will be saved in the path where the application is installed + "\screenshotses.png", and it will also be saved to the clipboard.

**Parameters:**
- `ImageNameCornerOne`
- `ImageNameCornerTwo`
- `Time`
- `Sim`

**Syntax:**

```
ScreenSnipping <ImageNameCornerOne> , <ImageNameCornerTwo> Timeout= <Time>
ScreenSnipping <ImageNameCornerOne> , <ImageNameCornerTwo> Timeout= <Time> Sim= <Sim>
```

**Examples:**

```
Titanium ScreenSnipping Corner1.PNG , Corner2.PNG Timeout= 20000
Titanium ScreenSnipping Corner1.PNG , Corner2.PNG Timeout= 20000 Sim= 0.7
```

*Added: 2018-Jun-13*

---

### Scroll

> Simulate a MouseWheel scroll.

Simulate a MouseWheel event, to scroll up or down.

**Parameters:**
- `times`
- `direction`

**Syntax:**

```
Scroll <times> <direction>
```

**Examples:**

```
Scroll 5 up
Scroll 10 down
```

*Added: 2019-Dec-10*

---

### Sleep

> Make a pause in the process.

Method to generate a pause delimited in Milliseconds.

**Parameters:**
- `Time`

**Syntax:**

```
Sleep <Time>
Sleep = <Time>
```

**Examples:**

```
Titanium Sleep 1000
Titanium Sleep = 1000
```

*Added: 2018-Jun-13*

---

### SolveCAPTCHA

> Solve a captcha in an image.

This function can solve a captcha by using a FRIDA web service. Taking an image as an input, and returning the captcha's text. It needs internet connection in order to work, it will not succeed if it is being run as Turing Offline.

**Parameters:**
- `ImagePathToBeSolved`
- `VariableName`

**Syntax:**

```
SolveCAPTCHA <ImagePathToBeSolved> and save as <VariableName>
```

**Examples:**

```
Titanium SolveCAPTCHA C:\Users\user\Pictures\CaptchaImage.png and save as VariableName
Titanium SolveCAPTCHA C:\Users\faustino.villarreal\Pictures\CaptchaImage.jpg and save as VariableName
```

*Added: 2018-Dec-11*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Titanium/Articles/SolveCAPTCHA.pdf)

---

### Type

> Type a text as written with the keyboard.

Type a text or special keys as written with the keyboard's SendKeys. Reference for the syntax of sendkeys in https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.sendkeys?redirectedfrom=MSDN&view=net-5.0

**Parameters:**
- `Text`
- `Bool`

**Syntax:**

```
Type <Text>
Type <Text> BloqMayus= <Bool:True|False>
```

**Options:**

- `Bool`: `True`, `False`

**Examples:**

```
Titanium Type Text goes here
Titanium Type Text goes here BloqMayus= True
```

*Added: 2018-Jun-13*

[Additional Documentation](https://innotekfilestore.file.core.windows.net/frida-docs/Readers/Titanium/Articles/Type.pdf)

---

### TypeBlock

> Text to be written using the Clipboard as an auxiliary.

Text to be written using the Clipboard as an auxiliary. The specified text is loaded to the clipboard and then Titanium.

**Parameters:**
- `Text`

**Syntax:**

```
TypeBlock <Text>
```

**Examples:**

```
Titanium TypeBlock Text goes here
```

*Added: 2019-Aug-23*

---

### TypeVirtual

> Text to be written with SimulateInput.

Text to be written with SimulateInput.

**Parameters:**
- `Text`

**Syntax:**

```
TypeVirtual <Text>
```

**Examples:**

```
Titanium TypeVirtual Text Goes Here
```

*Added: 2018-Jun-13*

---
