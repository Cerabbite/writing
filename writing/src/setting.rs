#[path="error.rs"] mod error;

use crate::ERRORCODES;

const VERSION: &str = env!("CARGO_PKG_VERSION");
const COPYRIGHT: &str = "Copyright (c) 2022 Cerabbite";

pub fn version(_args: Vec<String>) {
    //println!("{:?}", _args);
    let release_date: &str = "20-07-2022";
    let response = reqwest::blocking::get(
        "https://raw.githubusercontent.com/Cerabbite/writing/main/Releases",
    )
    .unwrap()
    .text()
    .unwrap();
    println!("{:?}", response);
    if release_date == "cannot find" {
        println!("writing v{} this version is not yet public", VERSION);
    } else {
        println!("writing v{} released on {}", VERSION, release_date);
    }
}

pub fn update(_args: Vec<String>) {
    error::not_implemented("update");
}

pub fn license(_args: Vec<String>) {
    error::not_implemented("license");
    // Extract license text from Github
}
