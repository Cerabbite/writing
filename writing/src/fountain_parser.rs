#[path="error.rs"] mod error;

use crate::ERRORCODES;

pub fn parser(_args: Vec<String>) {
    println!("Arguments: {:?}", _args);
    error::not_implemented("fountain-parser");
}
