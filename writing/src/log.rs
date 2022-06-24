use crate::LOGFOLDER;
use std::path::Path;
use std::fs;
use chrono::prelude::DateTime;

//Function that checks if this is the first time the program is started
//Function that checks if a log file for today has been created if not it creats one

pub fn CONFIG() {
  // https://www.youtube.com/watch?v=4EmKgrzHfv4
  // Use .toml as config format
  // Also save all the log files in that directory
}

pub fn CheckFile() {
  //println!("Log folder: {}", Path::new(LOGFOLDER).exists());
  let first_time: bool = Path::new(LOGFOLDER).exists();
  if first_time == false {
      fs::create_dir_all(LOGFOLDER);
}

  // If file does not exist create the file and add writing to environment variable
}

pub fn warn(Warning: String) {

}

pub fn info(Information: String) {

}

pub fn error(Information: String) {

}

pub fn debug(Debug: String) {

}

pub fn RUNTIME(StartTime: DateTime, EndTime: DateTime) {
    println!("Start time: {:?}", StartTime)
    println!("End time: {:?}", EndTime)
}
