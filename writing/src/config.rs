use serde_derive::Deserialize;
use std::fs;
use std::process::exit;
use toml;

// Struct to hold toml data
#[derive(Deserialize)]
pub struct Data {
    pub writing: Config,
}


// Struct to hold data from the [writing] section
#[derive(Deserialize)]
pub struct Config {
    pub name: String,
    pub version: String,
    pub release_date: String,
}

pub fn config() -> (String, String, String){
    let filename = "config\\config.toml";

    let contents = match fs::read_to_string(filename) {
        Ok(c) => c,

        Err(_) => {
            eprintln!("Could not read file '{}'", filename);
            //println!("Error reading file")
            exit(101);
        }
    };

    let data: Data = match toml::from_str(&contents) {
        Ok(d) => d,

        Err(err) => {
            eprintln!("Unable to load data from {}", filename);
            println!("{:?}", err);

            exit(102);
        }
    };

    //println!("{}", data.writing.name);
    //println!("{}", data.writing.version);
    //println!("{}", data.writing.release_date);
    let name: String = data.writing.name;
    let version: String = data.writing.version;
    let release_date: String = data.writing.release_date;
    return (name, version, release_date);
}
