#[path="error.rs"] mod error;

use crate::ERRORCODES;

const VERSION: &str = "0.1.0";//env!("CARGO_PKG_VERSION");
const COPYRIGHT: &str = "Copyright (c) 2022 Cerabbite";

pub fn version(_args: Vec<String>) {
    //println!("{:?}", _args);
    //let release_date: &str = "20-07-2022";
    let response: String = reqwest::blocking::get(
        "https://raw.githubusercontent.com/Cerabbite/writing/main/Releases",
    )
    .unwrap()
    .text()
    .unwrap();
    let mut txt = response.split("\n");
    for i in txt {
        println!("{:?}", i);
        if i.contains(VERSION) {
            //println!("Version");
            let mut release_date = i.split(" ");
            for s in release_date {
                if (DateTime::createFromFormat('d-m-Y ', $s) !== false) {
                  println!("{:?}", s)
                }
            }
        }
    }
    //println!("{:?}", release_date);
    /*if release_date == "cannot find" {
        println!("writing v{} this version is not yet public", VERSION);
    } else {
        println!("writing v{} released on {}", VERSION, release_date);
    }*/
}

pub fn update(_args: Vec<String>) {
    error::not_implemented("update");
}

pub fn license(_args: Vec<String>) {
    error::not_implemented("license");
    // Extract license text from Github
}
