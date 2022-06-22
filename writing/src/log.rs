use crate::LOGFOLDER;
use std::path::Path;
use std::fs;

//Function that checks if this is the first time the program is started
//Function that checks if a log file for today has been created if not it creats one

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

pub fn start() {

}

pub fn end() {
    
}
