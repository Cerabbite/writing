#[path="error.rs"] mod error;

use std::{env, fs};
use crate::ERRORCODES;

pub fn screenplay(_args: Vec<String>) {

}

fn FDX() {
  //println!("You are currently unable to export to FDX.");
  error::not_implemented("fdx-export");
}

fn PDF() {
  //println!("You are currently unable to export to PDF.");
  error::not_implemented("pdf-export");
}

fn TRELBY() {
  //println!("You are currently unable to export to TRELBY.");
  error::not_implemented("trelby-export");
  /*
Test trelby script:

#Version 3
#Begin-Auto-Completion 
AutoCompletion/Scene/Enabled:True
AutoCompletion/Scene/Items:0
AutoCompletion/Character/Enabled:True
AutoCompletion/Character/Items:0
AutoCompletion/Transition/Enabled:True
AutoCompletion/Transition/Items:12
AutoCompletion/Transition/Items/1:BACK TO:
AutoCompletion/Transition/Items/2:CROSSFADE:
AutoCompletion/Transition/Items/3:CUT TO:
AutoCompletion/Transition/Items/4:DISSOLVE TO:
AutoCompletion/Transition/Items/5:FADE IN:
AutoCompletion/Transition/Items/6:FADE OUT
AutoCompletion/Transition/Items/7:FADE TO BLACK
AutoCompletion/Transition/Items/8:JUMP CUT TO:
AutoCompletion/Transition/Items/9:MATCH CUT TO:
AutoCompletion/Transition/Items/10:SLOW FADE TO BLACK
AutoCompletion/Transition/Items/11:SMASH CUT TO:
AutoCompletion/Transition/Items/12:TIME CUT:
#End-Auto-Completion 
#Begin-Config 
FontSize:12
Margin/Bottom:25.40
Margin/Left:38.10
Margin/Right:25.40
Margin/Top:12.70
Paper/Height:297.00
Paper/Width:210.00
PageBreakActionLines:2
PageBreakDialogueLines:2
SceneContinueds:False
SceneContinuedIndent:45
ShowSceneNumbers:False
IncludeTOC:True
ShowTOC:True
OpenOnCurrentPage:True
RemoveNotes:False
OutlineNotes:True
ShowMargins:False
ShowLineNumbers:False
Cursor/Line:10
Cursor/Column:0
String/MoreDialogue:(MORE)
String/ContinuedPageEnd:(CONTINUED)
String/ContinuedPageStart:CONTINUED:
String/DialogueContinued: (cont'd)
Element/Scene/BeforeSpacing:10
Element/Scene/IntraSpacing:0
Element/Scene/Indent:0
Element/Scene/Width:60
Element/Scene/Screen/AllCaps:True
Element/Scene/Screen/Bold:True
Element/Scene/Screen/Italic:False
Element/Scene/Screen/Underlined:False
Element/Scene/Export/AllCaps:True
Element/Scene/Export/Bold:False
Element/Scene/Export/Italic:False
Element/Scene/Export/Underlined:False
Element/Action/BeforeSpacing:10
Element/Action/IntraSpacing:0
Element/Action/Indent:0
Element/Action/Width:60
Element/Action/Screen/AllCaps:False
Element/Action/Screen/Bold:False
Element/Action/Screen/Italic:False
Element/Action/Screen/Underlined:False
Element/Action/Export/AllCaps:False
Element/Action/Export/Bold:False
Element/Action/Export/Italic:False
Element/Action/Export/Underlined:False
Element/Character/BeforeSpacing:10
Element/Character/IntraSpacing:0
Element/Character/Indent:22
Element/Character/Width:38
Element/Character/Screen/AllCaps:True
Element/Character/Screen/Bold:False
Element/Character/Screen/Italic:False
Element/Character/Screen/Underlined:False
Element/Character/Export/AllCaps:True
Element/Character/Export/Bold:False
Element/Character/Export/Italic:False
Element/Character/Export/Underlined:False
Element/Dialogue/BeforeSpacing:0
Element/Dialogue/IntraSpacing:0
Element/Dialogue/Indent:10
Element/Dialogue/Width:35
Element/Dialogue/Screen/AllCaps:False
Element/Dialogue/Screen/Bold:False
Element/Dialogue/Screen/Italic:False
Element/Dialogue/Screen/Underlined:False
Element/Dialogue/Export/AllCaps:False
Element/Dialogue/Export/Bold:False
Element/Dialogue/Export/Italic:False
Element/Dialogue/Export/Underlined:False
Element/Parenthetical/BeforeSpacing:0
Element/Parenthetical/IntraSpacing:0
Element/Parenthetical/Indent:16
Element/Parenthetical/Width:25
Element/Parenthetical/Screen/AllCaps:False
Element/Parenthetical/Screen/Bold:False
Element/Parenthetical/Screen/Italic:False
Element/Parenthetical/Screen/Underlined:False
Element/Parenthetical/Export/AllCaps:False
Element/Parenthetical/Export/Bold:False
Element/Parenthetical/Export/Italic:False
Element/Parenthetical/Export/Underlined:False
Element/Transition/BeforeSpacing:10
Element/Transition/IntraSpacing:0
Element/Transition/Indent:45
Element/Transition/Width:20
Element/Transition/Screen/AllCaps:True
Element/Transition/Screen/Bold:False
Element/Transition/Screen/Italic:False
Element/Transition/Screen/Underlined:False
Element/Transition/Export/AllCaps:True
Element/Transition/Export/Bold:False
Element/Transition/Export/Italic:False
Element/Transition/Export/Underlined:False
Element/Shot/BeforeSpacing:10
Element/Shot/IntraSpacing:0
Element/Shot/Indent:0
Element/Shot/Width:60
Element/Shot/Screen/AllCaps:True
Element/Shot/Screen/Bold:False
Element/Shot/Screen/Italic:False
Element/Shot/Screen/Underlined:False
Element/Shot/Export/AllCaps:True
Element/Shot/Export/Bold:False
Element/Shot/Export/Italic:False
Element/Shot/Export/Underlined:False
Element/Note/BeforeSpacing:10
Element/Note/IntraSpacing:0
Element/Note/Indent:5
Element/Note/Width:55
Element/Note/Screen/AllCaps:False
Element/Note/Screen/Bold:False
Element/Note/Screen/Italic:True
Element/Note/Screen/Underlined:False
Element/Note/Export/AllCaps:False
Element/Note/Export/Bold:False
Element/Note/Export/Italic:True
Element/Note/Export/Underlined:False
Element/Act break/BeforeSpacing:10
Element/Act break/IntraSpacing:0
Element/Act break/Indent:25
Element/Act break/Width:10
Element/Act break/Screen/AllCaps:True
Element/Act break/Screen/Bold:True
Element/Act break/Screen/Italic:False
Element/Act break/Screen/Underlined:True
Element/Act break/Export/AllCaps:True
Element/Act break/Export/Bold:False
Element/Act break/Export/Italic:False
Element/Act break/Export/Underlined:True
Font/Bold-Italic/Name:
Font/Bold-Italic/Filename:
Font/Bold/Name:
Font/Bold/Filename:
Font/Italic/Name:
Font/Italic/Filename:
Font/Normal/Name:
Font/Normal/Filename:
#End-Config 
#Begin-Locations 
Locations:0
#End-Locations 
#Begin-Spell-Checker-Dict 
Words:0
#End-Spell-Checker-Dict 
#Title-String 0.000000,105.000000,24,cb,Helvetica,,UNTITLED SCREENPLAY
#Title-String 0.000000,120.460000,12,c,Courier,,by\n\nMy Name Here
#Title-String 15.000000,248.460000,12,,Courier,,123/456-7890\nno.such@thing.com
#Header-String 1,0,r,,${PAGE}.
#Header-Empty-Lines 1
#Start-Script 
.\Int. House - day
..Just some test action lines
._Some character
.:Character dialogue
._Voice (V.o)
.:Voice over
._Off (o.S)
.((Parenthetical)
.:Off screen
./CUT TO:
.\
._
  */
}
