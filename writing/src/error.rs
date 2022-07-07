use colored::*;
use crate::ERRORCODES;

/*
Develop some logical way for error codes like that all 100 numbers are missing arguments all 400 codes are not implemented/unkown feature
*/

const ERRORCODEURL: &str = r"https://github.com/Cerabbite/writing/blob/main/Documentation/Documentation.md#";
// For better and more elegant error handling: https://rust-cli.github.io/book/tutorial/errors.html

pub fn error_display(errorcode: &str) {
    // When user changes the config.toml so that instead of showing a url to possible solutions the solutions are shown in the browser
    not_implemented("error_display");
}

pub fn error_handling(errorcode: &str) {
    println!("{}: writing exited with error code '{}' check '{}{}' for more information.", "error".red(), errorcode, ERRORCODEURL, errorcode);
}

pub fn not_implemented(function: &str) {
    println!("'{}' is not yet implemented", function);
    error_handling(ERRORCODES[2]);
}

pub fn not_implemented_os(function: &str) {
    println!("'{}' is not yet available for your OS", function);
    error_handling(ERRORCODES[3]);
}

pub fn unkown_function(function: &str) {
    // Error code 400    
}

pub fn unkown_character(character: &str) {
    println!("'{}' is not a valid character", character);
    // Error code: 200
    //error_handling(ERRORCODES[4]);
}