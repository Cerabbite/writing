mod config;
mod settings;

//use clap::{App, load_yaml, Arg};

fn main() {
    if config::config().writing.auto_update == true {
        settings::update();
    }
    /*
    //https://rustrepo.com/repo/clap-rs-clap-rust-command-line#using-yaml
    let writing_yaml = load_yaml!("..\\config\\writing.yaml");
    let matches = App::from_yaml(writing_yaml).get_matches();
    //println!("{:?}", matches);
    let config = matches.value_of("second").unwrap_or("!$@#ERROR*&%");
    if config != "!$@#ERROR*&%" {
        println!("{}", config);
    }
    */

    settings::version();
}
