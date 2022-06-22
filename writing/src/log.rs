use crate::LOGFILE;
use std::path::Path;

pub fn CheckFile() {
  println!("Log file: {}", Path::new("/etc/hosts").exists());
  // If file does not exist create the file and add writing to environment variable
}

pub fn warn(Warning: String) {

}

pub fn info(Information: String) {

}

pub fn error(Information: String) {

}

pub fn debug(Debug:: String) {

}
