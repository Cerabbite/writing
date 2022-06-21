# writing
Writing is a software made to write novels and screenplay without any heavy text editor.

> If you see any spelling/grammar mistakes, missing information, incorrect information or you think something else can be improved. Please let us know by ....

## Table of Contents
<table>
    <tr><td width=33% valign=top>

- [writing](#writing)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Windows](#windows)
    - [Mac Os](#mac-os)
    - [Linux](#linux)
  - [Fountain](#fountain)
    - [Scene Heading](#scene-heading)
    - [Action](#action)
    - [Character](#character)
    - [Dialogue](#dialogue)
    - [Parenthetical](#parenthetical)
    - [Dual Dialogue](#dual-dialogue)
    - [Lyrics](#lyrics)
    - [Transition](#transition)
    - [Centered Text](#centered-text)
    - [Emphasis](#emphasis)
    - [Title Page](#title-page)
    - [Page Breaks](#page-breaks)
    - [Punctuation](#punctuation)
    - [Line Breaks](#line-breaks)
    - [Indenting](#indenting)
    - [Notes](#notes)
    - [Boneyard](#boneyard)
    - [Sections and Synopses](#sections-and-synopses)
  - [Novel](#novel)
    - [Settings](#settings)
    - [Chapter Titles](#chapter-titles)
    - [Chapter Content](#chapter-content)
    - [Table of Contents](#table-of-contents-1)
    - [Title Page](#title-page-1)
    - [Page Break](#page-break)
    - [Notes](#notes-1)

</td><td width=33% valign=top>

* [Exporting your project](#Exporting-your-project)
    * [Screenplay](#Screenplay)
    * [Novel](#Novel)

</td><td valign=top>

* [Error Codes](#Error-Codes)
* [Contributing to writing](#Contributing-to-writing)

</td></tr>
</table>

## Installation
### Windows
### Mac Os
### Linux

## Fountain
Fountain is not designed for writing. For more information go on their official website https://fountain.io/. The documentation on Fountain is written using their official documentation which you can find [here](https://fountain.io/syntax#section-slug). In this tutorial we only cover the parts of Fountain that writing supports in it's latest version. If you have an older version of writing you can go to the documentation folder and find the documentation for your version.

### Scene Heading
A scene heading consists of a line that begins with ```INT.``` or ```EXT.``` followed by an empty line.
```
INT. WRITING ROOM - DAY

```
<br>
You can also "force" a Scene Heading by starting a line with a single period.

```
.FORCED SCENE HEADING
```
<br>

```INT. WRITING ROOM - DAY``` is interpreted as a Scene Heading because of the keyword ```INT.```, but ```.FORCED SCENE HEADING``` requires the single period start in order to be interperted as a Scene Heading.
<br>

> **_NOTE_:**  Only a line starting with a singular period will be interperted as a Scene Heading. So a line that starts with multiple periods will NOT be interperted as a Scene Heading.
```
.FORCED SCENE HEADING

..Not a forced scene heading
```
<br>

You can also add Scene Numbers. Scene Numbers are wrapped in ```#```.
Valid Scene Numbers:
```
EXT. PARK - DAY #1#
EXT. PARK - DAY #1A#
EXT. PARK - DAY #1a#
EXT. PARK - NIGHT #A1#
EXT. PARK - NIGHT #I-1-A#
EXT. PARK - NIGHT #1.#
EXT. PARK - NIGHT - FLASHBACK (1944) #110A#
```

### Action
### Character
### Dialogue
### Parenthetical
### Dual Dialogue
> Dual dialogue is not yet implemented in writing
### Lyrics
### Transition
### Centered Text
> Centered Text is not yet implemented in writing
### Emphasis
### Title Page
### Page Breaks
### Punctuation
### Line Breaks
### Indenting
### Notes
### Boneyard
### Sections and Synopses
<!-- ### Error Handling -->

## Novel
### Settings
### Chapter Titles
### Chapter Content
### Table of Contents
### Title Page
### Page Break
### Notes

## Exporting your project
### Screenplay
### Novel

## Error Codes
### 100A
#### Causes
- You did not specify a target

#### Solutions
```
writing target
```

### 100B
Target specified by user is not a valid target

#### List of valid targets
<!-- NOTE: Set all valid targets in alphabetical order -->
* screenplay
* novel
* version
* update
* help

### 404
Feature is missing

### 405
Feature is not yet implemented on your OS

## Contributing to writing
### Reporting bugs
