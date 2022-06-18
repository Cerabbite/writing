#[path="error.rs"] mod error;

use crate::ERRORCODES;

pub fn version(_args: Vec<String>) {
    println!("{:?}", _args);
}

pub fn update(_args: Vec<String>) {
    error::not_implemented("update");
}
