const DIGITS: &str = "1234567890";
const VALIDCHARS: &str = ".";

fn main() {
    //let number: i32 = 36;
    let number: &str = "346540.";
    let num: String = number.to_string();
    for i in num.chars() {
        if DIGITS.contains(i) == false {
            if VALIDCHARS.contains(i) == false {
                println!("Error: invalid character {:?}", i);
                return;
            }
        }
    }
    println!("{:?} is a number", number);
    //println!("{:?}", DIGITS.contains("2"));
}
