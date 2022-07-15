use crate::config::config;

use clap:: {
    Args,
    Parser,
    Subcommand,
};

#[derive(Debug, Parser)]
#[clap(author, version=&*config().writing.version, about)]
pub struct writingArgs {
    /// A first argument
    pub first_arg: String,
}
