use crate::config::config;
use colored::*;

pub fn version() {
    let version = config().writing.version;
    //let release_date = config().writing.release_date;
    println!("writing {}{}", "v".green(), version.green());

    drop(version);
    //drop(release_date);
}

pub fn update(_auto_update: bool) {
    let version = config().writing.version;
    //let type = config().writing.update_type;
    // Go to https://cerabbite.github.io/writing/all-releases.html
    // Pick the latetst release that mathces the users type
    // Check if the 2 matches if so print "No update available" <- Only if it is not from auto_update
    // If not then compare the lengths and the x.y.z part
    // If the latest_release x.y.z part is larget then the current go to download part
    // If they are equal and the mode is set to quarter (forgot that if mode is full only need to check the x's and if half then the x and y's)
    let latest_release = "0.2.0-a-nightly-564613";
    println!("Searching if update is available...");

    drop(version);
    drop(latest_release);
}
