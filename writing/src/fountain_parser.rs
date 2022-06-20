#[path="error.rs"] mod error;

use crate::ERRORCODES;
use std::env;
use std::fs;
//use std::io::Split;
//use std::string::split;
use std::string::String;
//https://stackoverflow.com/questions/21669722/what-is-the-simplest-way-to-convert-a-string-to-upper-case-in-rust
//https://www.youtube.com/watch?v=Mcuqzx3rBWc

pub fn parser(_args: Vec<String>) {
    //println!("Arguments: {:?}", _args);
    //let contents: Vec<String> = fs::read_to_string(r"E:\GitHub\writing\writing\test\test.txt").split("\n");

    //let first_character = contents.chars().nth(0).unwrap();

    //println!("{:?}", contents[0]);

    /*for i in contents {
        if i.[..1] == "." and i.[..1] != "." {
            scene_heading();
        } else if i[..4].to_uppercase() == "INT." or i[..4] == "EXT." {
            scene_heading();
        }
    }*/

    error::not_implemented("fountain-parser");
}


fn scene_heading() {
    println!("This is the function for Scene Headings");
}

fn action_line() {
    println!("This is the function for Action Lines")
}

fn character() {
    println!("This is the function for character")
}

fn dialogue() {
    println!("This is the function for dialogue")
}

fn transition() {
    println!("This is the function for transitions")
}
