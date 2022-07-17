use crate::config::config;

pub fn version() {
    let version = config().writing.version;
    let release_date = config().writing.release_date;
    let copyright = config().writing.copyright;
    println!("writing v{} released on {}", version, release_date);
    println!("{}", copyright)

    drop(version);
    drop(release_date);
    drop(copyright);
}

pub fn update(auto_update: bool) {
    let version = config().writing.version;
    let type = config().writing.update;
    // Go to https://cerabbite.github.io/writing/all-releases.html
    // Pick the latetst release that mathces the users type
    // Check if the 2 matches if so print "No update available" <- Only if it is not from auto_update
    // If not then compare the lengths and the x.y.z part
    // If the latest_release x.y.z part is larget then the current go to download part
    // If they are equal and the mode is set to quarter (forgot that if mode is full only need to check the x's and if half then the x and y's)
    // DOWNLOAD PART:
    let latest_release = "0.2.0-a-nightly-564613";
    println!("Searching if update is available...");
    drop(version);
    drop(latest_release);
}
