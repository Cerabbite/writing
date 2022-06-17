mod fountain_parser;
mod novel_parser;
mod setting;
use std::env;

fn main() {
    let _args: Vec<String> = env::args().collect();
    let target: &String = &_args[1];

    setting::version(_args);

    if target == "screenplay" {
        fountain_parser::parser(_args);
    }
}
