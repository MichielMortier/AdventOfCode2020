use lazy_static::lazy_static;
use regex::Regex;

lazy_static! {
    static ref RE: Regex =
        Regex::new(r"(?P<low>\d+)-(?P<high>\d+) (?P<key>\w): (?P<pw>\w+)").unwrap();
}

pub struct Password {
    low: usize,
    high: usize,
    key: char,
    pw: String,
}

impl Password {
    pub fn new(input: &str) -> Password {
        let matches = RE.captures(input).unwrap();
        let key = matches
            .name("key")
            .unwrap()
            .as_str()
            .chars()
            .next()
            .unwrap();
        let low = matches.name("low").unwrap().as_str().parse().unwrap();
        let high = matches.name("high").unwrap().as_str().parse().unwrap();
        let pw = matches.name("pw").unwrap().as_str().to_owned();
        Password { low, high, key, pw }
    }
}

pub fn _validate_password1(input: &str) -> bool {
    let pw = Password::new(input);

    let count = pw.pw.chars().filter(|c| *c == pw.key).count();
    if count >= pw.low && count <= pw.high {
        return true;
    }

    false
}

pub fn _validate_password2(input: &str) -> bool {
    let pw = Password::new(input);

    let chars: Vec<char> = pw.pw.chars().collect();
    let t1 = chars.len() >= pw.low && chars[pw.low - 1] == pw.key;
    let t2 = chars.len() >= pw.high && chars[pw.high - 1] == pw.key;

    (t1 || t2) && !(t1 && t2)
}

#[cfg(test)]
mod test {
    use std::fs::read_to_string;

    use crate::password::{_validate_password1, _validate_password2};

    #[test]
    fn d2p1() {
        let count = read_to_string("res/reddit/d2")
            .unwrap()
            .lines()
            .filter(|l| _validate_password1(l))
            .count();

        println!("Solution: {}", count);
    }
    #[test]
    fn d2p2() {
        let count = read_to_string("res/reddit/d2")
            .unwrap()
            .lines()
            .filter(|l| _validate_password2(l))
            .count();

        println!("Solution: {}", count);
    }
}
