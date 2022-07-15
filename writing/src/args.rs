use clap:: {
    Args,
    Parser,
    Subcommand,
};

#[derive(Debug, Parser)]
#[clap(author, version="v0.2.0b-nightly-UTC", about)]
pub struct writingArgs {
    /// A first argument
    pub first_arg: String,
}
