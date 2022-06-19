#[path="error.rs"] mod error;

use crate::ERRORCODES;
use std::env;
use std::fs;
//use std::io::Split;
use std::string::split;

pub fn parser(_args: Vec<String>) {
    //println!("Arguments: {:?}", _args);
    let contents: Vec<String> = fs::read_to_string(r"E:\GitHub\writing\writing\test\test.txt").split("\n");

    //let first_character = contents.chars().nth(0).unwrap();

    println!("{:?}", contents[0]);

    error::not_implemented("fountain-parser");
}
