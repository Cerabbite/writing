#[path="error.rs"] mod error;

use crate::ERRORCODES;

pub fn parser(_args: Vec<String>) {
    error::not_implemented("novel-parser");
}


/*
NOVEL - file format .novel

Start settings with ---
End settings with ---
Between --- and --- you can put all of your desired settings
Possible Settings:
    - title
    - author
    - style
    - font
    - font-size
    - line-spacing
    - left-margin
    - right-margin
    - top-margin
    - bottom-margin

# Chapter Title
## Sub chapter Title
### Sub Sub chapter Title
Chapter content
"Dialogue"
*/
