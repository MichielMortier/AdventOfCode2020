use regex::Regex;

thread_local! {
    static RE: Regex = Regex::new(r"(?P<comm>\w+) (?P<sign>[+-])(?P<val>\d+)").unwrap();
}

struct State {
    line: i64,
    acc: i64,
}

fn exec_line(line: &str, state: &mut State) {
    let cap = RE.with(|f| f.captures(line).unwrap());
    let comm = cap.name("comm").unwrap();
    let sign = cap.name("sign").unwrap();
    let val = cap.name("val").unwrap();

    match comm.as_str() {
        "nop" => state.line += 1,
        "acc" => {
            state.acc += str_to_val(sign.as_str(), val.as_str());
            state.line += 1;
        }
        "jmp" => state.line += str_to_val(sign.as_str(), val.as_str()),
        _ => panic!("Unknown command!"),
    }
}

fn str_to_val(sign: &str, val: &str) -> i64 {
    match sign {
        "+" => val.parse().unwrap(),
        _ => -val.parse::<i64>().unwrap(),
    }
}

#[cfg(test)]
mod test {
    use std::{collections::HashSet, fs::read_to_string};

    use super::{exec_line, State};

    #[test]
    fn d8p1() {
        let lines = read_to_string("res/reddit/d8").unwrap();
        let lines: Vec<_> = lines.lines().collect();

        let mut state = State { line: 0, acc: 0 };
        let mut seen_lines = HashSet::<i64>::new();

        while !seen_lines.contains(&state.line) {
            seen_lines.insert(state.line);
            exec_line(&lines[state.line as usize], &mut state);
        }
        println!("Solution: {}", state.acc);
    }
    #[test]
    fn d8p2() {
        let lines = read_to_string("res/reddit/d8").unwrap();
        let lines: Vec<_> = lines.lines().map(|s| s.to_string()).collect();

        for i in 0..lines.len() {
            let mut state = State { line: 0, acc: 0 };
            let mut seen_lines = HashSet::<i64>::new();

            let mut lines_c: Vec<_> = lines.clone();
            if lines_c[i].contains("nop") {
                lines_c[i] = lines_c[i].replace("nop", "jmp");
            } else if lines_c[i].contains("jmp") {
                lines_c[i] = lines_c[i].replace("jmp", "nop");
            } else {
                continue;
            }

            while (state.line as usize) < lines_c.len() && !seen_lines.contains(&state.line) {
                seen_lines.insert(state.line);
                exec_line(&lines_c[state.line as usize], &mut state);
            }

            if state.line as usize == lines_c.len() {
                println!("Solution: {}", state.acc);
                return;
            }
        }
    }
}
