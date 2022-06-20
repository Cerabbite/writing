#[path="error.rs"] mod error;

use crate::ERRORCODES;

const VERSION: &str = env!("CARGO_PKG_VERSION"); //"0.1.0";
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
        //println!("{:?}", i);
        if i.contains(VERSION) {
            //println!("Version");
            let mut release_date = i.split(" ");
            for s in release_date {
                let amm_dashes = s.chars().filter(|c| *c == '-').count();
                if amm_dashes == 2 && s.len() == 10 {
                    //println!("Release Date")
                    let release_date = s;
                    println!("writing v{} released on {}", VERSION, release_date);
                    return;
                }
            }
        }
    }
    println!("writing v{} this version is not yet public", VERSION);
    return;
}

pub fn update(_args: Vec<String>) {
    error::not_implemented("update");
}

pub fn license(_args: Vec<String>) {
    error::not_implemented("license");
    // Extract license text from Github
}
