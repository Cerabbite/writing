mod args;

use args::writingArgs;
use clap::Parser;

fn main() {
    let args: writingArgs = writingArgs::parse();
}