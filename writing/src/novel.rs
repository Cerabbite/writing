#[path="error.rs"] mod error;

use std::{env, fs};
use crate::ERRORCODES;

pub fn novel(_args: Vec<String>) {

}

fn DOCX() {
  //println!("You are currently unable to export to DOCX.");
  // Create a .docx file and rename it to .zip to see the xml content and base everything of of that
  // https://superuser.com/questions/278260/how-do-i-see-the-xml-of-my-docx-document for more information
  
  /*
  To create the .docx file:
    Create a folder with the output file name as its name in the temp folder of the OS
    Create the file and folder structure of .docx files
    Write content to the correct .xml file
    Once everything is written create a .zip file from the folder and copy that one in to the output folder
    Rename the .zip file to .docx
  */
  // This method does not seem to work, but ill keep it there for inspiration
  error::not_implemented("docx-export");
}

fn PDF() {
  //println!("You are currently unable to export to PDF.");
  error::not_implemented("pdf-export");
}

fn RTF() {
  //println!("You are currently unable to export to RTF.");
  error::not_implemented("rtf-export");
}
