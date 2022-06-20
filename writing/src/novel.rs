#[path="error.rs"] mod error;

use std::{env, fs};
use crate::ERRORCODES;

pub fn novel(_args: Vec<String>) {

}

fn DOCX() {
  //println!("You are currently unable to export to DOCX.");
  // Create a .docx file and rename it to .zip to see the xml content and base everything of of that
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
