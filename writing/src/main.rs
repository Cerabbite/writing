mod fountain_parser;
mod novel_parser;
mod setting;

use std::env;
use colored::*;

const TARGETS: [&str; 5] = ["screenplay", "novel", "version", "update", "help"];
pub const ERRORCODES: [&str; 1] = ["100A"];

fn main() {
    let _args: Vec<String> = env::args().collect();
    //let target = "None";

    if _args.len() <= 1 {
        println!("No target found");
        println!("{}: writing exited with error code '{}' check 'https://github.com/Cerabbite/writing/blob/main/Documentation/Error%20Codes.md#100a' for more information.", "error".red(), ERRORCODES[0]);
        //std::process::abort();
        return;
    } else {
        println!("2");
        let target = &_args[1];
        println!("{}", target)
    }

    /*if target == "screenplay" {
        fountain_parser::parser(_args);
    } else if target == "novel" {
        novel_parser::parser(_args);
    } else if target == "version" {
        setting::version(_args);
    } else if target == "update" {
        setting::update(_args);
    } else if target == "help" {
        //setting::help(_args);
        println!("Help command is not yet implemented")
    } else {
        println!("Unkown target '{}'", target);
        println!("For help use the '{}' command", TARGETS[4]);
    }*/
}
