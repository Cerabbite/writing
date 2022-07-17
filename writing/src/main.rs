mod config;

use clap::{App, load_yaml, Arg};
use std::any::Any;

fn main() {
    //https://rustrepo.com/repo/clap-rs-clap-rust-command-line#using-yaml
    let writing_yaml = load_yaml!("..\\config\\writing.yaml");
    let matches = App::from_yaml(writing_yaml).get_matches();
    //println!("{:?}", matches);
    let config = matches.value_of("second").unwrap_or("!$@#ERROR*&%");
    if config != "!$@#ERROR*&%" {
        println!("{}", config);
    }
}
