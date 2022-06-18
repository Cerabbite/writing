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
}
