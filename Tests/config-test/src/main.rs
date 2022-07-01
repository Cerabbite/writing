use std::fs::File;
use std::io::prelude::*;

const CONFIG_CONTENT: &[u8] = b"[writing]
author: Cerabbite
copyright: Copyright (c) 2022 Cerabbite
license: MIT License

[novel]
page-size: A4;
font: some-font.ttf
font-size: 12
[screenplay]
page-size: A4";

fn parser() {

}

// DO NOT DO THIS IN THE MAIN FUNCTION WHEN IMPLEMENTED!!
fn main() -> std::io::Result<()> {
    // Create path - source: https://stackoverflow.com/questions/59046312/how-can-i-create-a-file-and-its-parent-directories-using-a-single-method-in-rust
    let path = std::path::Path::new("config/config.toml");
    let prefix = path.parent().unwrap();
    std::fs::create_dir_all(prefix).unwrap();

    // Create file - source: https://doc.rust-lang.org/std/fs/struct.File.html
    let mut file = File::create("config/writing.toml")?;
    file.write_all(CONFIG_CONTENT)?;
    Ok(())
}

/*use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::create("config/config.toml")?;
    file.write_all(b"Hello, world!")?;
    Ok(())
}*/
