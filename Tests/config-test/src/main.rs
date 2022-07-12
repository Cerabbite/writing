use std::env;
use std::fs;
use std::io::prelude::*;

const CONFIG_CONTENT: &[u8] = b"[writing]
author: Cerabbite
copyright: Copyright (c) 2022 Cerabbite
license: MIT License
version: 2.0.0

[novel]
page-size: A4;
font: some-font.ttf
font-size: 12

[screenplay]
page-size: A4";

// Convert &str into char or char into &str
fn main() { //parser() {
    let contents = fs::read_to_string("config/writing.toml")
                    .expect("Something went wrong");

    println!("With text:\n{}", contents);

    //let sections;
    let mut start_section = false;
    let mut section = String::from("");
    let mut section_part = "[ ]".chars();
    let section_begin = section_part.nth(0).unwrap();
    let section_end = section_part.nth(1).unwrap();
    // Section checking loop
    for i in contents.chars() {
        if i == section_begin {
            start_section = true;
        } else if i == section_end && start_section == true {
            start_section = false;
            println!("Found a section: {}", section);
            section = String::from("");
        } else if start_section == true {
            section.push(i);
        }
    }
}

/*
// DO NOT DO THIS IN THE MAIN FUNCTION WHEN IMPLEMENTED!!
fn main() -> std::io::Result<()> {
    // Create path - source: https://stackoverflow.com/questions/59046312/how-can-i-create-a-file-and-its-parent-directories-using-a-single-method-in-rust
    let path = std::path::Path::new("config/config.toml");
    let prefix = path.parent().unwrap();
    std::fs::create_dir_all(prefix).unwrap();

    // Create file - source: https://doc.rust-lang.org/std/fs/struct.File.html
    let mut file = fs::File::create("config/writing.toml")?;
    file.write_all(CONFIG_CONTENT)?;
    Ok(())
}*/

/*use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::create("config/config.toml")?;
    file.write_all(b"Hello, world!")?;
    Ok(())
}*/
