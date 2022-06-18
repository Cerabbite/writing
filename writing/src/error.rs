use colored::*;

const ERRORCODEURL: &str = r"https://github.com/Cerabbite/writing/blob/main/Documentation/Error%20Codes.md#";

pub fn error_handling(errorcode: &str) {
    println!("{}: writing exited with error code '{}' check '{}{}' for more information.", "error".red(), errorcode, ERRORCODEURL, errorcode);
}

pub fn not_implemented(function: &str) {
    println!("'{}' is not yet implemented", function)
}
