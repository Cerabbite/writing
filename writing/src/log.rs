use crate::LOGFILE;
use std::path::Path;

pub fn CheckFile() {
  println!("Log file: {}", Path::new("/etc/hosts").exists());
  // If file does not exist create the file and add writing to environment variable
}

pub fn Log() {
  // Write things to the log file in format:
  // 21-06-2022 08:42: "Here the log information";
}
