#[path="error.rs"] mod error;

use crate::ERRORCODES;
use crate::OS_NAME;

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
    // Maybe use the version function to check if an update is available faster?
    println!("{}", OS_NAME);

    let response: String = reqwest::blocking::get(
        "https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION",
    )
    .unwrap()
    .text()
    .unwrap();

    let mut released_seperate = "5.1.3".split(".");//response.split(".");
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

    println!("release: {}-{}-{}", r_one, r_two, r_three);
    println!("current: {}-{}-{}", c_one, c_two, c_three);

    /*if update != true {
        println!("No update available")
        return;
    }
    if OS_NAME == "windows" {

    }*/
    error::not_implemented("update");
}

pub fn license(_args: Vec<String>) {
    error::not_implemented("license");
    // Extract license text from Github
}
