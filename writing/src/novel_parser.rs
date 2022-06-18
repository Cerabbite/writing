#[path="error.rs"] mod error;

use crate::ERRORCODES;

pub fn parser(_args: Vec<String>) {
    error::not_implemented("novel-parser");
}
