mod fountain_parser;
mod novel_parser;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let target: &String = &args[1];

    settings::version(args)

    if target == "screenplay" {
        fountain_parser::parser(args);
    }
}
