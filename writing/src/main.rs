mod fountain_parser;
mod novel_parser;
mod setting;
mod error;

use std::env;

//const TARGETS: [&str; 5] = ["screenplay", "novel", "version", "update", "help"];
const ERRORCODES: [&str; 3] = ["100A", "100B", "404"];

fn main() {
    let _args: Vec<String> = env::args().collect();

    let mut target: &str = "None";

    if _args.len() <= 1 {
        println!("No target found");
        error::error_handling(ERRORCODES[0]);
        //return;
    } else {
        target = &_args[1];
        //println!("{}", target)
    }

    if target == "screenplay" {
        fountain_parser::parser(_args);
    } else if target == "novel" {
        novel_parser::parser(_args);
    } else if target == "version" {
        setting::version(_args);
    } else if target == "update" {
        setting::update(_args);
    } else if target == "help" {
        //setting::help(_args);
        error::not_implemented("help-command");
    } else {
        println!("Please provide a valid target");
        error::error_handling(ERRORCODES[1]);
    }
}
