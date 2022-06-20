#[path="error.rs"] mod error;

use crate::ERRORCODES;
use crate::OS_NAME;
use std::io::{stdin,stdout,Write};

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
    //println!("{}", OS_NAME);

    let response: String = reqwest::blocking::get(
        "https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION",
    )
    .unwrap()
    .text()
    .unwrap();

    let mut release_version = response.to_string();
    let mut current_version = VERSION.to_string();

    release_version.truncate(release_version.len() - 1);
    current_version.truncate(current_version.len() - 1);



    let mut released_seperate = release_version.split("."); //"5.1.3".split(".");
    let mut current_seperate = VERSION.split(".");

    let mut n: i8 = 0;
    let mut r_one = 0;
    let mut r_two = 0;
    let mut r_three = 0;
    for i in released_seperate {
        if n == 0 {
            r_one = i.parse::<i32>().unwrap();
        } else if n == 1 {
            r_two = i.parse::<i32>().unwrap();
        } else if n == 2 {
            r_three = i.parse::<i32>().unwrap();
        }
        n += 1;
    }
    n = 0;
    let mut c_one = 0;
    let mut c_two = 0;
    let mut c_three = 0;
    for i in current_seperate {
        if n == 0 {
            c_one = i.parse::<i32>().unwrap();
        } else if n == 1 {
            c_two = i.parse::<i32>().unwrap();
        } else if n == 2 {
            c_three = i.parse::<i32>().unwrap();
        }
        n += 1;
    }

    let mut update: bool = false;
    let mut want_update: bool = false;

    if r_one > c_one {
        println!("1s");
        update = true;
    } else if r_two > c_two && r_one == c_one{
        println!("2s");
        update = true;
    } else if r_three > c_three && r_two == c_two {
        println!("3s");
        update = true;
    }
    println!("release: {}-{}-{}", r_one, r_two, r_three);
    println!("current: {}-{}-{}", c_one, c_two, c_three);

    if update != true {
        println!("No update available");
        return;
    } else {
        println!("v{} is available.", release_version);
        println!("Do you want to install v{}? (y/n)", release_version);
        let mut inp = String::new();
        if inp.to_uppercase() == "y" {
            want_update = true;
        }
    }

    if OS_NAME != "windows" && want_update == true{
        error::not_implemented("update-writing");
        return;
    }
}

pub fn license(_args: Vec<String>) {
    error::not_implemented("license");
    // Extract license text from Github
}
