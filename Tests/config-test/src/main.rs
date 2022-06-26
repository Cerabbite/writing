use directories::ProjectDirs;
use serde::Deserialize;
use std::fs;

#[derive(Deserialize, Debug)]
struct Config {
    name: String,
    number: i32,
}

fn main() {
    if let Some(proj_dirs) = ProjectDirs::from("dev", "cerabbite", "writing-test") {
        let config_dir = proj_dirs.config_dir();

        let config_file = fs::read_to_string(
            config_dir.join("writing-test.toml")
        ).map(|file| {toml::from_str(&file)})
        .unwrap();

        /*let config: Config = toml::from_str(&config_file).unwrap_or(Config {
            name: "Cerabbite".to_string(),
            number: 12,
        });

        dbg!(config);*/

    }
}
