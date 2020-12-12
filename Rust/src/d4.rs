use std::{collections::HashMap, fs::read_to_string};

use regex::Regex;

thread_local! {
    static HCL_RE: Regex = Regex::new(r"#[0-9a-f]{6}").unwrap();
    static ECL: Vec<String> = vec![
        "amb".to_owned(),
        "blu".to_owned(),
        "brn".to_owned(),
        "gry".to_owned(),
        "grn".to_owned(),
        "hzl".to_owned(),
        "oth".to_owned()
    ];
}

type Passport = HashMap<String, String>;

fn parse_file() -> Vec<Passport> {
    read_to_string("res/reddit/d4")
        .unwrap()
        .split("\n\n")
        .map(|p| {
            let mut map = HashMap::new();
            p.split_ascii_whitespace()
                .map(|s| s.split(":").collect())
                .for_each(|kv: Vec<&str>| {
                    if kv.len() == 2 {
                        map.insert(kv[0].to_owned(), kv[1].to_owned());
                    }
                });
            map
        })
        .collect()
}

fn is_valid1(pass: &Passport) -> bool {
    (pass.len() == 8 || (pass.len() == 7 && !pass.contains_key("cid")))
        && pass.iter().all(|p| match p.0.as_str() {
            "byr" => {
                let val = pass["byr"].parse::<u64>().unwrap();
                val >= 1920 && val <= 2002
            }
            "iyr" => {
                let val = pass["iyr"].parse::<u64>().unwrap();
                val >= 2010 && val <= 2020
            }
            "eyr" => {
                let val = pass["eyr"].parse::<u64>().unwrap();
                val >= 2020 && val <= 2030
            }
            "hgt" => {
                let val = &pass["hgt"];
                if val.contains("cm") {
                    let v = val.split("cm").collect::<Vec<_>>()[0]
                        .parse::<u64>()
                        .unwrap();
                    return v >= 150 && v <= 193;
                } else {
                    let v = val.split("in").collect::<Vec<_>>()[0]
                        .parse::<u64>()
                        .unwrap();
                    return v >= 59 && v <= 76;
                }
            }
            "hcl" => HCL_RE.with(|f| f.is_match(&pass["hcl"])),
            "ecl" => ECL.with(|f| f.contains(&pass["ecl"])),
            "pid" => pass["pid"].len() == 9 && pass["pid"].chars().all(char::is_numeric),
            "cid" => true,
            _ => false,
        })
}

#[cfg(test)]
mod test {
    use super::{is_valid1, parse_file};

    #[test]
    fn d4p1() {
        println!(
            "Solution: {}",
            parse_file().iter().filter(|p| is_valid1(p)).count()
        );
    }
}
