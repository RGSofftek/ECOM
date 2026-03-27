# Powerpoint Reader

**Keyword:** `PPT`

**Functions:** 6

## Description

Powerpoint Reader will allow you to automate the creation of Microsoft Powerpoint presentations.

## Quick Reference

| Function | Description |
|----------|-------------|
| [DeleteShapes](#deleteshapes) | Delete a shape. |
| [GetSlide](#getslide) | Gets the slides that contains a given text. |
| [LoadFileFrom](#loadfilefrom) | Loads a PowerPoint file. |
| [PasteShape](#pasteshape) | Paste a shape from the clipboard into a slide. |
| [ReplaceChart](#replacechart) | Copy or replace a chart from Excel to a slide. |
| [Save](#save) | Save a PPT. |

---

## Functions

### DeleteShapes

> Delete a shape.

Remove shapes of a slide by name

**Parameters:**
- `presentation`
- `slidenum`
- `text`

**Syntax:**

```
DeleteShapes in <presentation> slide <slidenum> named <text> 
```

**Examples:**

```
Ppt DeleteShapes in "PDeck" slide 8 named "Picture"
```

---

### GetSlide

> Gets the slides that contains a given text.

Gets the number of a slide that contains a given text

**Parameters:**
- `presentation`
- `text`

**Syntax:**

```
GetSlide in <presentation> containing <text>
```

**Examples:**

```
Ppt GetSlide in "PDeck" containing "Rol Classification"
```

---

### LoadFileFrom

> Loads a PowerPoint file.

Paste values from worksheet "Iniciativa" to presentation

**Parameters:**
- `wb`
- `path`
- `firstval`
- `secondval`
- `key`

**Syntax:**

```
LoadFileFrom <wb_path> containing <firstval> and <secondval> as <key>
```

**Examples:**

```
Date{d-dd-ddd-dddd en}  ---  9-09-Mon-Monday
Date{dddd(-3)-MMMM(-2)-yyyy(-3) es} ---  jueves-junio-2014
Date{1}  ---  9-09-Mon-Monday
```

---

### PasteShape

> Paste a shape from the clipboard into a slide.

Sets Effort and Spend tables from excel in presentation

**Parameters:**
- `presentation`
- `slidenum`
- `position`
- `lpos`
- `tpos`
- `h`
- `w`

**Syntax:**

```
PasteShape in <presentation> slide <slidenum> position <lpos,tpos,h,w>
```

**Examples:**

```
Ppt PasteShape in "PResumen" slide 3 position "46,100,370,440"
```

---

### ReplaceChart

> Copy or replace a chart from Excel to a slide.

Find a given shape into a prsentation slide

**Parameters:**
- `chartname`
- `worksheet`
- `slidenum`
- `presentation`
- `objectname`
- `newobjectname`
- `lpos`
- `tpos`
- `hpos`
- `wpos`

**Syntax:**

```
ReplaceChart <chartname> from <worksheet> in_slide <slidenum> of <presentation> change <objectname> with <newobjectname> in <lpos,tpos,hpos,wpos>
```

**Examples:**

```
ReplaceChart "Gráfico 1" from FinancialsWorkSheet  in_slide 3 of PDeck change "Gráfico 1" with "FinancialsChart" in "502,358,125,214"
```

---

### Save

> Save a PPT.

Save a powerpoint presentation

**Parameters:**
- `Key`
- `presentation`

**Syntax:**

```
Save <key_presentation>
```

**Examples:**

```
Save PDeck
```

---
