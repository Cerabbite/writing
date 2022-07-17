mod config;

//use args::writingArgs;
/*use clap:: {
    Parser,
    Arg,
    App,
};*/
use clap::{App, load_yaml};
use std::any::Any;

//const data: &dyn Any = config::config();
//const name: String = config::config().writing.name;

fn main() {
    //let values = config::config();
    //println!("{:?}", values.what_is_this());
    //config::rt("name".to_string());
    //let data = config::config();
    //println!("{}", data.writing.name);
    //println!("{}", name);
    //let args = writingArgs::parse();

    //https://rustrepo.com/repo/clap-rs-clap-rust-command-line#using-yaml
    //let writing_yaml = load_yaml!("config/writing.yaml");
    //let matches = App::from(writing_yaml).get_matches();

    let yaml = load_yaml!("..\\config\\writing.yaml");
    let matches = App::from_yaml(yaml).get_matches();

    println!("{:?}", matches);
}
