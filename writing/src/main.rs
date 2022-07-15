mod config;
mod args;

use args::writingArgs;
use clap::Parser;

fn main() {
    let values = config::config();
    println!("{:?}", values.what_is_this());
}
